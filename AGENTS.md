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
├── index.html, index.md       landing page: links to the decks
├── docs/
│   ├── _template/             skeleton deck with the common slides
│   ├── <deck>/
│   │   ├── index.html         reveal.js entry point of the deck
│   │   ├── index.md           the slides
│   │   ├── brainstorming.md   optional: notes on the storyline of the talk
│   │   └── article/index.md   the proceedings article
│   └── images/                logos, speaker photos, QR codes
├── css/
│   ├── marquardt.css          the theme
│   └── custom.css             shared styles, including the common slides
├── reveal.js/                 submodule: upstream reveal.js, pinned to 6.0.2
└── scripts/make_qr.py         makes the QR codes
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
2026-09-24:

- The deadline is 11 October 2026.
- The article is a Word file. Upload it to the organiser's speaker database. Do not send it by
  e-mail.
- The length is 7,000 to 12,000 characters in total, spaces included. The main part is about
  10,000 characters.
- German and English are allowed.
- The content is a technical contribution from practice. No advertising, no marketing, no
  product presentation.
- The elements, in this order: title, optional subtitle, authors and company, a lead of one
  paragraph, the main part, a summary, optional references, a short biography of each author.
- Images and tables go in the text. Each has a number, a caption and a source. Use 300 dpi
  and no dark backgrounds. Put code examples in as images, in a fixed-width font.
- The layout: A4 portrait, margins 2 cm at the top and 3 cm at the other sides, one column,
  justified, line spacing 1.15, Times New Roman 12 pt, the title 16 pt bold. No headers, no
  footers, no page numbers, no logos.

Read the page again before you submit. The organiser can change it.

## Language

- Each deck and its article use the language of the talk. See the table in
  [Structure](#structure).
- `AGENTS.md`, `README.md`, code comments and commit messages are in English.

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
