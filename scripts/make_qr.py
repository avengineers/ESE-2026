# /// script
# requires-python = ">=3.10"
# dependencies = ["segno==1.6.6"]
# ///
"""Make the QR codes of the decks.

Each folder docs/<name>/ with an index.html is a deck. Its QR code for the
"Questions?" slide points to the published deck and goes to
docs/images/qr_<name>.png.

Each entry of LINKS is a page that a slide links to. Its QR code goes to
docs/images/qr_link_<name>.png.

Run from the repository root: uv run scripts/make_qr.py
"""

from pathlib import Path

import segno

BASE_URL = "https://avengineers.github.io/ESE-2026/docs"
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

LINKS = {
    "spled": "https://github.com/avengineers/SPLed",
    "spl_core": "https://github.com/avengineers/spl-core",
    "sphinx_needs": "https://sphinx-needs.readthedocs.io/",
    "sple_skills": "https://github.com/avengineers/sple-skills",
}


def save(url: str, target: Path) -> None:
    segno.make(url, error="m").save(str(target), scale=10, border=2)
    print(f"{target.relative_to(ROOT)} -> {url}")


def main() -> None:
    for deck in sorted(p.parent for p in DOCS.glob("*/index.html")):
        save(f"{BASE_URL}/{deck.name}/", DOCS / "images" / f"qr_{deck.name}.png")
    for name, url in LINKS.items():
        save(url, DOCS / "images" / f"qr_link_{name}.png")


if __name__ == "__main__":
    main()
