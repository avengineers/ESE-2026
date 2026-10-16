# Our Talks at the ESE Kongress 2026

Slide decks and proceedings articles of our talks at the
[ESE Kongress 2026](https://ese-kongress.de/), 30 November to 4 December 2026 in Sindelfingen.

| Talk | Slides |
|---|---|
| „Frag doch den Agenten!" – Wie agentische KI unseren Embedded-Entwicklungsalltag verändert hat | [ai_journey](https://avengineers.github.io/ESE-2026/docs/ai_journey/) |
| Beyond Software: The Rise of "Engineering as Code" in Embedded Systems | [eng_as_code](https://avengineers.github.io/ESE-2026/docs/eng_as_code/) |
| There Is More to a Product Line Than Zephyr Boards | [zephyr_meets_sple](https://avengineers.github.io/ESE-2026/docs/zephyr_meets_sple/) |

Add `?print-pdf` to a deck URL to get the printable version.

## Editing and viewing locally

1. Clone the repository with its submodule:

   ```powershell
   git clone --recurse-submodules https://github.com/avengineers/ESE-2026.git
   ```

2. Install Node.js and the web server. Run `.\build.ps1 -install`, or use the VS Code task
   `Install dependencies`.
3. Start the web server. Run `npm run dev`, or use the VS Code task `Start local web server`.
4. Open `http://localhost:3000/` in your browser.

Use [Visual Studio Code](https://code.visualstudio.com/) to edit the slides.

On Linux or WSL, open the repository in its dev container instead — with VS Code Dev
Containers or [DevPod](https://devpod.sh/). It installs Node.js, uv, Claude Code and the
Courier New font that `scripts/make_docx.py` needs, and it trusts the CA certificates of
the host, so it also works behind a corporate proxy. Then start the web server with
`npm run dev`.

## Infrastructure

| Piece | Where |
|---|---|
| reveal.js | `reveal.js/` submodule, upstream, pinned to 6.0.2 |
| Theme | `css/marquardt.css` |
| Shared styles | `css/custom.css` |
| Shared images | `docs/images/` |
| Skeleton deck | `docs/_template/` |
| QR codes | `scripts/make_qr.py` |
| Word files of the articles | `scripts/make_docx.py` |

The rules for changing the decks, and for adding one, are in [AGENTS.md](AGENTS.md).

## License

[MIT](LICENSE)
