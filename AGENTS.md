# Agent rules — ESE-2026

This repository holds the slide decks and the proceedings articles of our talks at the
ESE Kongress 2026, 30 November to 4 December 2026 in Sindelfingen. The [README](README.md)
explains the repository for human readers. This file holds the rules an agent gets wrong
without them.

## This repository goes public

The repository is private until the speakers call the decks finished. Then it goes public,
and GitHub Pages serves the decks. From that day, everyone can read every file, every commit
message and every speaker note.

Write every file and every commit message as if the repository were public today:

- Do not write internal hostnames, internal repository URLs, credentials or customer names.
  This applies to text, images, code listings, speaker notes and commit messages.
- Do not write Jira keys. A reader outside the company cannot open them.
- Check each slide that comes from an internal deck against these rules before you add it.
- Add a speaker's photo and profile link only when that speaker supplies them. Until then,
  use `docs/images/speaker_placeholder.svg` and the first name without a link.

**Caution:** the history goes public with the files. A text that you change or delete stays
readable in the older commits.

Before you make the repository public:

1. Check every file against the rules above.
2. Check every commit message against the rules above.
3. Set the visibility of the repository to public.
4. Switch on GitHub Pages for the `develop` branch and the root folder.
5. Open `https://avengineers.github.io/ESE-2026/` and each deck.

## Structure

```text
ESE-2026/
├── .devcontainer/             dev container for Linux and WSL, also behind a corporate proxy
├── index.html, index.md       landing page: links to the decks
├── docs/
│   ├── _template/             skeleton deck with the common slides
│   ├── <deck>/
│   │   ├── index.html         reveal.js entry point of the deck
│   │   ├── index.md           the slides
│   │   ├── brainstorming.md   optional: notes on the storyline of the talk
│   │   ├── linkedin.html/.md  optional: the title slide as a picture for LinkedIn
│   │   └── article/
│   │       ├── index.md       the proceedings article
│   │       └── index.docx     its Word file for the organiser, made by make_docx.py
│   └── images/                logos, speaker photos, QR codes, figures of the articles,
│                              LinkedIn pictures
├── css/
│   ├── marquardt.css          the theme
│   └── custom.css             shared styles, including the common slides
├── reveal.js/                 submodule: upstream reveal.js, pinned to 6.0.2
└── scripts/
    ├── postCreate.sh          sets up the dev container after it is created
    ├── make_qr.py             makes the QR codes
    └── make_docx.py           makes the Word file of an article and counts its characters
```

| Deck | Talk | Language | Speakers |
|---|---|---|---|
| `docs/ai_journey/` | „Frag doch den Agenten!" – Wie agentische KI unseren Embedded-Entwicklungsalltag verändert hat | German | Judith, Karsten |
| `docs/eng_as_code/` | Beyond Software: The Rise of "Engineering as Code" in Embedded Systems | English | Akshit, Judith |
| `docs/zephyr_meets_sple/` | There Is More to a Product Line Than Zephyr Boards | English | Alexandru |

The folder names are the names of the accepted abstracts, without the year.

## The common slides

Every deck starts with the title slide and "Who are we?". Every deck ends with
"Questions?" and "Some Links". All three decks must look the same on these four slides.

- Take the markup from `docs/_template/index.md`.
- Change the look in `css/custom.css`, section "Common slides". Do not change it in a deck.
- Change the markup in the template first. Then make the same change in each deck.

The decks are copies of the template, and that is deliberate. reveal.js loads a whole
Markdown file or nothing, so a deck cannot pick single slides from a shared file. Of the four
common slides, only "Some Links" is the same in every deck; the other three carry the title,
the speakers or the URL of their deck. A shared file for one slide is not worth the extra
`<section>` in every `index.html`.

`ai_journey` is the one exception. Its talk opens with a live demo: the title slide is
followed by a user story that an agent implements while the speakers talk, and "Who are we?"
comes after it. The agent reads the user story alone, without the rest of the deck, so the
deck has three files, each loaded by its own `<section>` in `index.html`:

- `title.md` holds the title slide.
- `user_story.md` holds the user story. It holds nothing else, speaker notes included: the
  agent would read them as part of its task. Its speaker notes go into the attribute
  `data-speaker-notes` of its `<section>` in `index.html`. The Markdown plugin drops
  `data-notes` from a section it loads from a file, so a script in `index.html` copies
  `data-speaker-notes` into `data-notes`.
- `index.md` holds the rest of the deck.

## The theme

`css/marquardt.css` is a copy of the Marquardt reveal.js theme: the League theme with the
Marquardt gradient. The internal slide decks load the same theme from an internal fork of
reveal.js. This repository cannot use that fork: GitHub Pages and outside readers cannot fetch
it. The fork differs from upstream 6.0.2 only in the theme file, so upstream 6.0.2 with the
copied theme gives the same result.

- Do not edit `css/marquardt.css`. Put a change in `css/custom.css`.
- When you move the `reveal.js` submodule to a new tag, open each deck and check the look.

## Adding a deck

1. Copy `docs/_template/` to `docs/<name>/`.
2. In `index.html`, set `lang` and `<title>`.
3. In `index.md`, replace the title, the subtitle and the speakers.
4. In `index.md`, replace `_template` with `<name>` in the two deck URLs and in the QR image name.
5. Run `uv run scripts/make_qr.py`.
6. Add the deck to the root `index.md`.
7. Add a row to the table in [Structure](#structure).

## The articles

Each talk has its proceedings article in `docs/<deck>/article/index.md`, in the language of
the talk. The organiser's rules are on the page
[Tagungsband-Beitrag](https://ese-kongress.de/frontend/index.php?page_id=53121), read on
2026-09-25. The page links a
[sample manuscript](https://ese-kongress.de/custom/media/ESE_2024/tagungsband/Beispielmanuskript_ESE_Tagungsband_2024.pdf),
which is still the one of 2024. The rules:

- The deadline is 19 October 2026, extended from 11 October.
- The article is a Word file. Upload it to the organiser's speaker database. Do not send it by
  e-mail.
- The length is 7,000 to 12,000 characters in total, spaces included. The main part is about
  10,000 characters.
- German and English are allowed.
- The content is a technical contribution from practice. No advertising, no marketing, no
  product presentation.
- The elements, in this order: title, optional subtitle, authors and company, a lead of one
  paragraph, the main part, a summary, an optional list of abbreviations, optional
  references, a short biography of each author, an optional photo of each author.
- A biography gives the name, the company, the role and the expertise of the author.
- Images and tables go in the text. Each has a number, a caption and a source. Use 300 dpi,
  a high contrast and no dark backgrounds.
- Put code examples and formulas in as images, in Courier New 12 pt.
- The layout: A4 portrait, margins 2 cm at the top and 3 cm at the other sides, one column,
  justified, line spacing 1.15. No headers, no footers, no page numbers, no logos.
- The font is Times New Roman. The title is 16 pt bold. The subtitle, the lead and the
  headings are 12 pt bold. The body text and the captions are 12 pt.
- Use italics for emphasis, and use them sparingly. Do not use bold, underline or colour in
  the body text.
- Do not use automatic numbering or indents.

The sample manuscript shows what the rules do not say. It centres the title, the subtitle
and the authors line. It puts the caption below the figure. It has no space between
paragraphs, and `make_docx.py` adds 6 pt after each paragraph, because no rule forbids it
and the text is easier to read.

Read the page again before you submit. The organiser can change it.

### The Word file

`scripts/make_docx.py` makes the Word file from the Markdown file and counts the characters.
Word counts the same number. Text in an image does not count.

The script draws the code figures in Courier New and needs `cour.ttf` and `courbd.ttf`.
Windows has them. The dev container installs them from the Debian package
`ttf-mscorefonts-installer`, which gives the same figures. On Linux or WSL outside the
dev container, the script stops with "Font cour.ttf or courbd.ttf (Courier New) not found."

**Caution:** the next run of the script overwrites the Word file. Do not edit the Word file.
Edit the Markdown file.

1. Write the article in `docs/<deck>/article/index.md`.
2. Run `uv run scripts/make_docx.py <deck>`.
3. Read the character count in the output.
4. Open `docs/<deck>/article/index.docx` in Word. Check each page.

The script expects this shape of the Markdown file:

- `# Title` comes first. Then come the optional subtitle, the authors line and the lead, one
  paragraph each.
- `##` and `###` start the headings.
- A caption is a paragraph that starts with `Abbildung N:` or `Figure N:`. Put it below its
  figure.
- A code block becomes an image in Courier New 12 pt. Wrap each line at 57 characters or
  fewer. The script stops on a longer line.
- A code block tagged ```` ```text ```` is black. A code block tagged ```` ```code ```` gets
  syntax highlighting on a white background: feature conditions in dark red and bold,
  directives in dark blue, options in dark green, file labels, tree lines and comments in
  dark grey. Each colour has a contrast of 7:1 or more. The bold keeps the feature
  condition visible in a black and white print. `CODE_RULES` in `make_docx.py` holds the
  rules. The `eng_as_code` article uses `code`; `ai_journey` keeps `text`.
- To show the fences of a Markdown code block in a figure, open and close the figure with
  four backticks.
- Every figure gets the same frame: 0.25 cm white padding and a grey line. The script
  draws it around a code image and around a copy of each `![alt](path)` image, so crop a
  screenshot to its content and leave no margin around it.
- `![alt](path)` puts in an image. Give it a width of 1,772 px or more, for 300 dpi at the
  text width of 15 cm. The script warns on a smaller image.
- Use `*italic*` for emphasis. The script stops on other inline Markdown, such as bold, code
  spans or links.
- Write typographic quotes: „…“ in German, “…” in English.
- HTML comments do not go into the Word file.

To take a screenshot of a web page for a figure, use Edge. The command below gives three
times the pixel density and the light theme:

```text
msedge --headless --hide-scrollbars --blink-settings=preferredColorScheme=1 --window-size=1536,1000 --force-device-scale-factor=3 --screenshot=out.png <URL>
```

Then crop the image and save it with 300 dpi.

## The LinkedIn picture

`docs/images/linkedin_<deck>.png` is the title slide of a deck as a picture for posting the
talk on LinkedIn, 1920 × 1080. The page `docs/<deck>/linkedin.html` shows that title slide
with the photos of the speakers in place of the company logos, and the ESE Kongress logo
between them.

- `docs/images/ese_logo_white.svg` is the logo from page 1 of the organiser's
  [fact sheet 2026](https://ese-kongress.de/custom/media/ese_26/downloads/ESE_2026_Fact_Sheet_web_DE.pdf).
  Its lettering is white instead of blue, as in the banner of the organiser's website, so
  that it reads on the dark background.
- Change the title slide in `index.md` first. Then make the same change in `linkedin.md`.
  In `ai_journey`, the title slide is in `title.md`.

To make the picture, run `npm run dev`. Then run the command below. On Linux, use
`chromium` with the same flags.

```text
msedge --headless --hide-scrollbars --window-size=1920,1080 --virtual-time-budget=10000 --screenshot=docs/images/linkedin_<deck>.png http://localhost:3000/docs/<deck>/linkedin.html
```

`--virtual-time-budget` gives reveal.js the time to load the slide before the screenshot.

## Language

- Each deck and its article use the language of the talk. See the table in
  [Structure](#structure).
- `AGENTS.md`, `README.md`, code comments and commit messages are in English.
- On a slide, end a full sentence with a period. End a bullet point without one, even when it
  is a full sentence. A question or an exclamation keeps its `?` or `!`. Titles, subtitles,
  source lines and sentence fragments get no period.
- Write speaker notes as the script: the words the speakers say, in full spoken sentences, each
  part opened with the speaker's name, as in `Karsten: …`. A talk of two speakers is a dialog:
  each speaker carries their own slides and examples, and the other hands over or adds one
  line. Keep the changes of speaker few. Let neither speaker explain to the other what they
  know, and give neither a naive question for the other to answer. Put what a speaker does in
  parentheses, as in `(Judith: nächste Folie)`. Keep it short: say what the slide does not, and
leave out what the audience can see for itself, such as a legend, a colour or a number. Explain how the deck works in
  `AGENTS.md` or in a code comment, never in a note.

## Viewing and checking

- Run `npm install` once. Then run `npm run dev`. The landing page opens at
  `http://localhost:3000/`.
- Run `npm run lint:md` before each commit.
- While the repository is private, `npm run dev` is the only way to see the decks.
- When the repository is public, GitHub Pages serves the `develop` branch from the root
  folder, at `https://avengineers.github.io/ESE-2026/`. The QR codes and the "Some Links"
  slides point there.
- Keep the empty file `.nojekyll`. Without it, GitHub Pages does not publish folders that
  start with `_`, such as `docs/_template/`.

## Commits

Use conventional commits: `feat:`, `fix:`, `docs:`, `chore:`.
