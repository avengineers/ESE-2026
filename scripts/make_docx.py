# /// script
# requires-python = ">=3.10"
# dependencies = ["python-docx==1.2.0", "pillow==11.3.0"]
# ///
"""Make the Word file of a proceedings article and count its characters.

Reads docs/<deck>/article/index.md and writes docs/<deck>/article/index.docx in the
layout of the organiser: the rules on the page "Tagungsband-Beitrag" and the sample
manuscript of 2024. See AGENTS.md, section "The articles".

The Markdown file has this shape:

    # Title
    Subtitle (optional)
    Authors, Company
    Lead: one paragraph
    ## Heading / ### Heading, paragraphs, ```code```, ![alt](image), "Abbildung N: ..."

A code block becomes an image in Courier New 12 pt at 300 dpi, in black for ```text
and highlighted by CODE_RULES for ```code. Every figure, code or image, gets the same
frame. HTML comments are
dropped. Any other inline Markdown stops the script, so that no markup reaches Word.

Run from the repository root: uv run scripts/make_docx.py ai_journey
"""

import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

FONT = "Times New Roman"
TEXT_WIDTH_CM = 21.0 - 3.0 - 3.0  # A4 minus the left and the right margin
LINE_SPACING = 1.15
PARAGRAPH_AFTER_PT = 6
DPI = 300

CODE_FONT = "cour.ttf"  # Courier New
CODE_FONT_BOLD = "courbd.ttf"  # Courier New Bold
CODE_PT = 12
CODE_PAD_CM = 0.25
CODE_BORDER_PX = 3
FRAME_GREY = (128, 128, 128)

# Highlighting of a ```code block: (style, pattern), the first style that claims a
# character wins. Each colour has a contrast of 7:1 or more on white. The feature
# condition is bold as well, so that it stands out in a black and white print.
CODE_STYLES = {
    "feature": ((163, 21, 21), True),  # dark red
    "directive": ((11, 61, 145), False),  # dark blue
    "option": ((27, 94, 32), False),  # dark green
    "dim": ((70, 70, 70), False),  # dark grey
}
CODE_RULES = [
    ("feature", re.compile(r"\{%.*?%\}|\bconfig [A-Z][A-Z0-9_]*|\bCONFIG_[A-Z0-9_]+(=\w+)?")),
    ("directive", re.compile(r"(```)?\{\w+\}|```|\.\. \w+::")),
    ("option", re.compile(r"^\s*:\w+:|^\s+(bool|default)\b")),
    ("dim", re.compile(r"[├└│─]+")),  # tree lines
    ("dim", re.compile(r"(?<=[^\s├└│─])\s{2,}\S.*$")),  # description beside a tree entry
    ("dim", re.compile(r"^\S*[^\s/]$")),  # file label of an excerpt; a folder is not one
    ("dim", re.compile(r"#\s.*$")),  # comment
]
CAPTION = re.compile(r"^(Abbildung|Tabelle|Figure|Table) \d+: ")
SUMMARY = re.compile(r"Zusammenfassung|Fazit|Summary|Conclusion", re.IGNORECASE)
IMAGE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)$")
FORBIDDEN = re.compile(r"\*\*|__|`|\]\(|<[a-z/]")


# --- Markdown ---------------------------------------------------------------------


def parse(md: str) -> list[tuple[str, str]]:
    """Split the article into blocks: (kind, content)."""
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    blocks, para, code, fence, code_kind = [], [], [], "", "code"

    def flush():
        if para:
            blocks.append(("para", " ".join(para)))
            para.clear()

    for line in md.splitlines():
        # As in CommonMark, a block opened by n backticks closes only on a line of n or
        # more, so a block of four can show the fences of three.
        if fence and line.strip().startswith(fence) and not line.strip().strip("`"):
            blocks.append((code_kind, "\n".join(code)))
            code.clear()
            fence = ""
        elif not fence and (m := re.match(r"^(`{3,})(.*)$", line)):
            flush()
            fence = m.group(1)
            code_kind = "colour_code" if m.group(2).strip() == "code" else "code"
        elif fence:
            code.append(line)
        elif not line.strip():
            flush()
        elif m := re.match(r"^(#{1,3}) (.+)$", line):
            flush()
            blocks.append((f"h{len(m.group(1))}", m.group(2).strip()))
        elif IMAGE.match(line.strip()):
            flush()
            blocks.append(("image", line.strip()))
        else:
            para.append(line.strip())
    flush()
    return blocks


def classify(blocks: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Name the front matter and the captions. The title is the only h1."""
    assert blocks[0][0] == "h1", "the article must start with '# Title'"
    first_h2 = next(i for i, b in enumerate(blocks) if b[0] == "h2")
    front = blocks[1:first_h2]
    names = {3: ["subtitle", "authors", "lead"], 2: ["authors", "lead"]}.get(len(front))
    assert names, f"expected subtitle, authors and lead before the first '##', got {len(front)} blocks"
    out = [("title", blocks[0][1])] + [(n, b[1]) for n, b in zip(names, front)]
    for kind, text in blocks[first_h2:]:
        if kind == "para" and CAPTION.match(text):
            kind = "caption"
        out.append((kind, text))
    return out


def inline_runs(text: str) -> list[tuple[str, bool]]:
    """Split a paragraph into (text, italic) runs. Italics are the only emphasis allowed."""
    if bad := FORBIDDEN.search(text):
        sys.exit(f"Inline markup {bad.group(0)!r} is not allowed in the Word file: {text[:80]}…")
    parts = re.split(r"(?<![\w*])\*([^*]+)\*(?![\w*])", text)
    return [(p, i % 2 == 1) for i, p in enumerate(parts) if p]


# --- Figures ----------------------------------------------------------------------


def highlight(line: str) -> list[tuple[str, str | None]]:
    """Split a code line into (text, style) runs by CODE_RULES. None is plain black."""
    styles: list[str | None] = [None] * len(line)
    for style, rule in CODE_RULES:
        for m in rule.finditer(line):
            for i in range(m.start(), m.end()):
                styles[i] = styles[i] or style
    runs: list[tuple[str, str | None]] = []
    for char, style in zip(line, styles):
        if runs and runs[-1][1] == style:
            runs[-1] = (runs[-1][0] + char, style)
        else:
            runs.append((char, style))
    return runs


def code_image(code: str, path: Path, colour: bool = False) -> None:
    """Draw a code block in Courier New 12 pt at 300 dpi, as wide as the text column."""
    px = lambda cm: round(cm / 2.54 * DPI)
    size = round(CODE_PT / 72 * DPI)
    try:
        font = ImageFont.truetype(CODE_FONT, size)
        bold = ImageFont.truetype(CODE_FONT_BOLD, size)
    except OSError:
        sys.exit(f"Font {CODE_FONT} or {CODE_FONT_BOLD} (Courier New) not found.")
    width, pad = px(TEXT_WIDTH_CM), px(CODE_PAD_CM)
    lines = code.splitlines()
    widest = max(font.getlength(line) for line in lines)
    if widest > width - 2 * pad:
        limit = int((width - 2 * pad) // font.getlength("M"))
        sys.exit(f"A code line is too wide for {CODE_PT} pt in the text column; wrap it at {limit} characters.")
    line_h = round(size * LINE_SPACING)
    img = Image.new("RGB", (width, 2 * pad + line_h * len(lines)), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=FRAME_GREY, width=CODE_BORDER_PX)
    for n, line in enumerate(lines):
        x = pad
        for text, style in highlight(line) if colour else [(line, None)]:
            fill, is_bold = CODE_STYLES[style] if style else ((0, 0, 0), False)
            draw.text((x, pad + n * line_h), text, font=bold if is_bold else font, fill=fill)
            x += font.getlength(text)  # monospaced: bold has the same advance
    img.save(path, dpi=(DPI, DPI))


def framed_image(src: Path, path: Path) -> None:
    """Put an image in the frame of the code figures: the same padding and grey line,
    measured on the page, so that all figures look alike. The source stays unchanged."""
    with Image.open(src) as img:
        img = img.convert("RGB")
    ratio = CODE_PAD_CM / TEXT_WIDTH_CM  # the padding as a share of the printed width
    pad = round(img.width * ratio / (1 - 2 * ratio))
    out = Image.new("RGB", (img.width + 2 * pad, img.height + 2 * pad), "white")
    out.paste(img, (pad, pad))
    line = round(CODE_BORDER_PX * out.width / (TEXT_WIDTH_CM / 2.54 * DPI))
    ImageDraw.Draw(out).rectangle([0, 0, out.width - 1, out.height - 1], outline=FRAME_GREY, width=line)
    dpi = out.width / (TEXT_WIDTH_CM / 2.54)
    out.save(path, dpi=(dpi, dpi))


# --- Word -------------------------------------------------------------------------


def set_font(style, size: float, bold: bool = False) -> None:
    """Times New Roman for every script, black, no theme font or theme colour."""
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.italic = False
    style.font.color.rgb = RGBColor(0, 0, 0)
    rpr = style.element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.insert(0, fonts)
    for attr in list(fonts.attrib):
        del fonts.attrib[attr]
    for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn(f"w:{attr}"), FONT)
    color = rpr.find(qn("w:color"))
    for attr in ("w:themeColor", "w:themeShade", "w:themeTint"):
        color.attrib.pop(qn(attr), None)
    # The default Title and Subtitle styles space out their letters
    for spacing in rpr.findall(qn("w:spacing")):
        rpr.remove(spacing)


def paragraph_style(doc, name: str, base: str = "Normal"):
    styles = doc.styles
    style = styles[name] if name in [s.name for s in styles] else styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    style.base_style = styles[base] if name != base else None
    return style


def setup(doc, lang: str) -> dict:
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21.0), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(2), Cm(3)
    section.left_margin, section.right_margin = Cm(3), Cm(3)

    # Language, for the spell check and the hyphenation
    defaults = doc.styles.element.find(qn("w:docDefaults")).find(qn("w:rPrDefault")).find(qn("w:rPr"))
    for old in defaults.findall(qn("w:lang")):
        defaults.remove(old)
    lang_el = OxmlElement("w:lang")
    for attr in ("val", "eastAsia", "bidi"):
        lang_el.set(qn(f"w:{attr}"), lang)
    defaults.append(lang_el)
    # The schema fixes the order of the settings: autoHyphenation follows defaultTabStop
    doc.settings.element.find(qn("w:defaultTabStop")).addnext(OxmlElement("w:autoHyphenation"))

    def para(name, size=12, bold=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, before=0, after=0, base="Normal"):
        style = paragraph_style(doc, name, base)
        set_font(style, size, bold)
        fmt = style.paragraph_format
        fmt.alignment = align
        fmt.line_spacing = LINE_SPACING
        fmt.space_before, fmt.space_after = Pt(before), Pt(after)
        fmt.first_line_indent = fmt.left_indent = Cm(0)
        return style

    center = WD_ALIGN_PARAGRAPH.CENTER
    # The sample manuscript has no space between paragraphs. 6 pt after each paragraph is our
    # choice; no rule forbids it. Headings keep the 12 pt before of the sample: Word uses the
    # larger of "after" and "before", it does not add them.
    styles = {
        "body": para("Normal", after=PARAGRAPH_AFTER_PT),
        "title": para("Title", size=16, bold=True, align=center),
        "subtitle": para("Subtitle", bold=True, align=center),
        "authors": para("ESE Autoren", align=center, before=12, after=12),
        "lead": para("ESE Vorspann", bold=True, after=12),
        "h2": para("Heading 1", bold=True, before=12, after=0),
        "h3": para("Heading 2", bold=True, before=12, after=0),
        "figure": para("ESE Abbildung", align=center, before=12, after=6),
        "caption": para("Caption", after=12),
    }
    for key in ("title", "subtitle", "h2", "h3", "figure"):
        styles[key].paragraph_format.keep_with_next = True
    # The default Title style has a bottom border; the organiser allows none
    ppr = styles["title"].element.get_or_add_pPr()
    for border in ppr.findall(qn("w:pBdr")):
        ppr.remove(border)
    return styles


def build(deck: str) -> None:
    folder = DOCS / deck / "article"
    md = (folder / "index.md").read_text(encoding="utf-8")
    blocks = classify(parse(md))
    lang = "de-DE" if re.search(r"\b(und|der|die|das)\b", md) else "en-US"

    doc = Document()
    styles = setup(doc, lang)
    counts: dict[str, int] = {}
    part = "Titel, Autoren"
    figures = 0

    with tempfile.TemporaryDirectory() as tmp:
        for kind, text in blocks:
            if kind == "lead":
                part = "Vorspann"
            elif kind == "h2":
                part = "Zusammenfassung" if SUMMARY.search(text) else ("Hauptteil" if part in ("Vorspann", "Hauptteil") else text)
            if kind in ("code", "colour_code", "image"):
                figures += 1
                path = Path(tmp) / f"figure_{figures}.png"
                if kind != "image":
                    code_image(text, path, colour=kind == "colour_code")
                else:
                    framed_image((folder / IMAGE.match(text).group(2)).resolve(), path)
                with Image.open(path) as img:
                    dpi = img.width / (TEXT_WIDTH_CM / 2.54)
                if dpi < DPI:
                    print(f"WARNING: figure {figures} has {dpi:.0f} dpi at the text width; the organiser asks for {DPI}.")
                doc.add_paragraph(style=styles["figure"]).add_run().add_picture(str(path), width=Cm(TEXT_WIDTH_CM))
                continue
            p = doc.add_paragraph(style=styles.get(kind, styles["body"]))
            for run_text, italic in inline_runs(text):
                p.add_run(run_text).italic = italic or None
            key = "Beschriftungen" if kind == "caption" else part
            counts[key] = counts.get(key, 0) + len(text)

        title = next(t for k, t in blocks if k == "title")
        authors = next(t for k, t in blocks if k == "authors")
        props = doc.core_properties
        props.title, props.author, props.last_modified_by = title, authors, authors
        props.subject, props.comments, props.keywords, props.category = "", "", "", ""
        props.language, props.revision = lang, 1
        props.created = props.modified = datetime.now(timezone.utc).replace(microsecond=0, tzinfo=None)
        out = folder / "index.docx"
        doc.save(out)

    total = sum(counts.values())
    print(f"Wrote {out.relative_to(ROOT)}: {figures} figures, language {lang}.")
    print("Characters with spaces, as Word counts them (text in images does not count):")
    for key, n in counts.items():
        print(f"  {key:<28} {n:>6,}".replace(f"{n:,}", f"{n:,}".replace(",", ".")))
    print(f"  {'Total':<28} {total:>6,}".replace(f"{total:,}", f"{total:,}".replace(",", ".")) + "   (organiser: 7.000 to 12.000; main part about 10.000)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(sys.argv[1])
