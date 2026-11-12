## „Frag doch den Agenten!"

<pre class="copyable"><code class="language-plaintext">Setz die User Story auf Folie 2 in SPLed um:
https://avengineers.github.io/ESE-2026/docs/ai_journey/user_story.md</code></pre>

Note:

Judith hat die Folie davor zum ersten Mal gesehen und reagiert genervt und gestresst: „Jetzt? Ich
halte gerade einen Vortrag!“ Pause. Dann: „Frag doch den Agenten!“

Judith wechselt ins Terminal, fügt den vorbereiteten Prompt ein und startet den Agenten. Das
Terminal bleibt kurz sichtbar, dann zurück zu den Folien.

Die Datei user_story.md ist die Folie davor. Der Agent liest sie allein, ohne den Rest des
Decks. Deshalb stehen dort keine Notizen.

---

### Wer sind wir?

<div class="speakers">
<div class="speaker">

![Judith](../images/judith.png)

[Judith](https://www.linkedin.com/in/judith-reichwein-873665258/)

</div>
<div class="speaker">

![Karsten](../images/karsten.png)

[Karsten](https://www.linkedin.com/in/karnangue/)

</div>
</div>

Note:

Jede Person sagt in ein oder zwei Sätzen, wer sie ist.

---

### Wer ist eigentlich der Agent?

**Agent** (vom lateinischen *agere* = handeln, treiben) bezeichnet grundsätzlich eine Person,
ein Programm oder ein System, das <span class="highlighted-yellow">in Vertretung oder im
Auftrag</span> eines anderen agiert.

<p class="deck-url">Nach: <a href="https://www.dwds.de/wb/Agent">DWDS</a> und <a href="https://de.wiktionary.org/wiki/Agent">Wiktionary</a>, Stichwort „Agent“</p>

Note:

Judith fragt: „Wer ist eigentlich der Agent?“ Karsten antwortet mit der Definition. Der Kern ist
„in Vertretung oder im Auftrag“: Der Agent handelt für uns. Genau so hat er eben seine Aufgabe
bekommen, vom Product Owner.

Die Definition fasst zwei Wörterbücher zusammen und ist kein wörtliches Zitat. Das DWDS nennt
den Agenten als jemanden, „der im Auftrag eines anderen Geschäfte vermittelt und abschließt“,
und als Programm, das „selbstständig Entscheidungen trifft“. Herkunft: italienisch agente,
„Vertreter“, von lateinisch agere, „treiben, tun“.

Dann: „Und während unser Agent arbeitet, erzählen wir euch, wie es dazu kam.“

---

### 2022: Ein Schülerpraktikant im Editor

<div class="agent-face"><img src="../images/ai_journey_agent_intern.webp" alt="Der Agent als Schülerpraktikant"></div>

- Code Completion
- Python, CMake, C++, GoogleTest
- Architektur bleibt bei uns
- Vorschläge klingen gut

![Code Completion in einer CMake-Datei: Als erste Zeile schlägt sie einen Copyright-Kommentar einer fremden Firma vor.](../images/ai_journey_completion.png) <!-- .element: class="fragment" style="width: 80%; margin: 0;" -->

Note:

Judith. Kapitel 1 des Artikels. Die Code Completion schlägt beim Programmieren mal eine Funktion
vor, mal eine Schleife. Die Syntax muss man nicht mehr im Kopf haben. Eine große Hilfe bei
Python, CMake, C++, GoogleTest und beim Schreiben von Dokumentation. Struktur und Architektur
kommen weiter von uns. Das Werkzeug entlastet bei Routineaufgaben, und wir gewinnen Zeit für die
kreative Arbeit.

Die Vorschläge klingen immer gut, trotzdem sind sie oft falsch: Der Code läuft nicht, vieles ist
halluziniert. Wir prüfen jede Zeile, wie man die Arbeit eines Praktikanten prüft.

Dann das Bild einblenden: In einer CMake-Datei von uns schlägt die Code Completion als erste Zeile
den Copyright-Kommentar einer ganz anderen Firma vor. Klingt gut, sieht richtig aus, ist falsch.

---

### Chatbots halfen auch mit

- Skripte, kleine VS-Code-Erweiterungen
- Läuft? Übernommen!
- Heute: *Vibe Coding*

Note:

Judith. Ein Chatbot schreibt uns ein Skript oder eine kleine Erweiterung für VS Code. Hier waren
wir weniger streng als bei der Code Completion: Lief das Ergebnis, haben wir es übernommen, ohne
jede Zeile zu verstehen. Heute heißt das Vibe Coding.

Überleitung zur nächsten Folie: „Nicht alles lief.“

---

![Ein Chat: Gefragt war ein Mermaid-Diagramm einer Git-History. Die Antwort sind vier Bilder von Meerjungfrauen.](../images/ai_journey_mermaid.png) <!-- .element: style="height: 660px; margin: 0;" -->

Note:

Judith. Die Frage war: ein Mermaid-Diagramm einer Git-History mit vier Commits und einem
Branch develop, der auf den letzten Commit zeigt. Mermaid ist eine Sprache für Diagramme als
Text. Die Antwort: „I'll try to create that.“ Und dann vier Bilder von Meerjungfrauen, englisch
mermaid, mit Commits und Branches, die „develoop“ und „Develice“ heißen. Die Antwort klingt gut,
sie sieht sogar gut aus, und sie ist trotzdem falsch.

---

### Ende 2025: Der Wendepunkt

- Neue Modelle, z. B. Claude Opus 4.5
- Schulung: agentische Entwicklung
- Repository lesen, bauen, testen, Fehler korrigieren
- MCP: Ticketsystem, CI-Server

<p class="fragment"><strong>„Frag doch den Agenten!“</strong></p>

Note:

Karsten. Kapitel 2 des Artikels. Die ersten Agenten haben wir benutzt wie die Code Completion,
nur mit Prompts. Ende 2025 kamen neue Modelle, und unser Team besuchte eine Schulung zu
agentischer Entwicklung. Die Trainer haben uns gezeigt, was ein Agent kann: Er liest das
Repository, schreibt Code, führt Befehle aus, baut, testet und korrigiert seine eigenen Fehler.
Über MCP, das Model Context Protocol, erreicht er Ticketsystem und CI-Server.

Und auf fast jede Frage im Team heißt die Antwort: „Frag doch den Agenten!“ Das ist der Titel des
Vortrags.

---

### „Mein Agent programmiert besser als deiner!“

- Eigene `AGENTS.md`
- Eigene Skill-Sammlungen
- Gleiches Projekt, andere Ergebnisse

Note:

Judith. Kapitel 3 des Artikels. Jeder pflegt seinen eigenen Werkzeugkasten: eine persönliche
AGENTS.md mit eigenen Regeln, bevorzugte und selbst geschriebene Skills. Dasselbe Projekt liefert
dann verschiedene Ergebnisse, je nachdem, wer fragt.

Keine Produkte nennen und keine bewerten: Es geht um die persönlichen Setups, nicht um das
Werkzeug.

Offen sagen: Der Agent, der gerade für uns arbeitet, läuft mit Karstens Setup. Es ist „sein
Agent“.

---

### Skills: Wie wir Agenten steuern

<div class="joined-code">

```yaml
---
name: c-unit-testing
description: Write GTest/GMock unit tests for embedded
  C components using Arrange-Act-Assert and
  hammocking. […]
---
```

```markdown
# GTest Unit Testing for Embedded C

## First Contact

1. Which component? — Ask for the component path
2. What's the goal? — New tests from scratch, add
   tests for a specific function, fix a failing test,
   or refactoring safety net? […]
```

</div>

<p class="deck-url">Quelle: <a href="https://github.com/avengineers/sple-skills">avengineers/sple-skills</a>, MIT-Lizenz</p>

Note:

Karsten. Ein Skill ist eine Anleitung in Textform. Der Agent lädt sie, sobald eine Aufgabe dazu
passt. Sie sagt, wie ein Team eine Aufgabe in seiner Umgebung erledigt: Werkzeuge, Konventionen,
Prüfungen am Ende. Das ist ein Ausschnitt aus unserem Skill für Unit-Tests in Embedded C.

---

### Skills als Produkt eines Plattform-Teams

- Werkzeuge, Schulungen – und Skills
- Für Unit-Tests, Build, Testbericht
- Ein gemeinsamer Stand für alle

Note:

Karsten. Als Plattform-Team liefern wir neben Werkzeugen und Schulungen jetzt auch Skills: wie
man gute Unit-Tests schreibt, wie man einen Build startet, wie man einen Testbericht erzeugt. Der
Entwickler muss diese Regeln nicht auswendig kennen, denn sein Agent lädt sie. So wird aus vielen
persönlichen Setups ein gemeinsamer Stand. Damit ist die Frage von eben beantwortet: Wie passt man
einen Agenten an eine Umgebung an?

---

### Der Product-Owner-Agent

<div class="agent-face"><img src="../images/ai_journey_agent_product_owner.webp" alt="Der Agent als Product Owner"></div>

- User Stories, Sprintplanung
- Einheitliches Format
- Großes Kontextfenster: denkt an mehr Fakten
- Aber: zu viele Details für Menschen

<p class="fragment"><strong>Auch die User Story auf Folie 2</strong></p>

Note:

Karsten. Kapitel 4 des Artikels, zweites Beispiel. Der Agent in der Rolle des Product Owners:
Er schreibt User Stories und
Backlog-Einträge und bereitet die Sprintplanung vor, immer im gleichen Format. Durch sein großes
Kontextfenster denkt er an Fakten und Randbedingungen, die ein Mensch oft vergisst, und er
liefert schnell eine Grundlage, über die das Team diskutieren kann. Der Nachteil: Für einen
Menschen sind es oft zu viele Details.

Die User Story auf Folie 2 hat der Agent geschrieben, und das Ticket für diese Folien auch.

Das erste Beispiel des Artikels, Automotive SPICE, läuft gerade im Hintergrund. Wir zeigen es am
Ende.

Entwurf: Hier kann eine bereinigte Kopie des Tickets für die Folien hin, ohne Ticket-Nummer und
ohne interne Links.

---

### Der Consultant-Agent

<div class="agent-face"><img src="../images/ai_journey_agent_consultant.webp" alt="Die Agentin als Beraterin"></div>

<div class="flex-container" style="align-items: flex-start;">
<div class="half">

<div class="mermaid git-graph">
<pre>
---
config:
  theme: base
  themeVariables:
    git0: "#4dd0e1"
    git1: "#ffd54f"
    gitBranchLabel0: "#002b36"
    gitBranchLabel1: "#002b36"
    commitLabelColor: "#ffffff"
    commitLabelBackground: transparent
    commitLabelFontSize: 16px
    fontSize: 16px
  gitGraph:
    mainBranchName: develop
---
gitGraph TB:
  commit id: "423436d: draft the article"
  commit id: "3041588: add figure 2" type: HIGHLIGHT
  commit id: "9e6d4c7: apply the review"
  branch feat/ai-journey-slides
  commit id: "ce8a99a: draft the slides"
  commit id: "4e2722f: tighten the slides"
  commit id: "6a7a0a6: show a code completion"
  commit id: "dc38026: highlight the skill excerpt"
</pre>
</div>

</div>
<div class="half" style="flex: 1.4; width: auto;">

![Der Agent im Terminal: „Doch, es geht besser.“ Eine Tabelle vergleicht den Screenshot der Autoren, 1.055 × 791 Pixel, mit seinem, 2.688 × 1.901 Pixel.](../images/ai_journey_better_screenshot.png) <!-- .element: id="better-screenshot" style="width: 100%; margin-top: 0;" -->

</div>
</div>

<svg class="slide-arrow" data-arrow-from=".git-graph .commit-highlight-outer" data-arrow-to="#better-screenshot"></svg>

Note:

Judith. Kapitel 4 des Artikels, drittes Beispiel. Der Agent in der Rolle des Beraters: Er
arbeitet nicht nur am Code mit, sondern auch an Präsentationen und Vorträgen, und er sagt uns,
wo es besser geht. Dieser Vortrag ist so entstanden: zwei Menschen und
ein Agent.

Links: Erinnert ihr euch an die Meerjungfrauen? Das ist das Diagramm, das wir damals wollten: ein
Mermaid-Diagramm einer Git-History mit einem Branch develop. Diesmal hat es der Agent geschrieben,
und alle Commits sind echt: Auf develop stehen der Artikel für den Tagungsband und seine
Abbildung, auf dem Branch daneben die Arbeit an genau diesen Folien. Artikel und Folien liegen als
Markdown in einem Git-Repository, und wir prüfen und ändern sie wie Code.

Vor dem Vortrag prüfen: Jeder Rebase des Branches ändert die Commit-IDs auf dem Branch, und der
Branch zweigt dann von einem neueren Commit auf develop ab.

Der Pfeil: Mit dem markierten Commit kam Abbildung 2 des Artikels ins Repository. Für diese
Abbildung hatten wir einen Screenshot gemacht. Die Antwort des Agenten: „Doch, es geht besser.“
Sein Screenshot hat 2.688 × 1.901 Pixel statt 1.055 × 791, genug für 300 dpi im Druck.

Der Agent schreibt auch Tabellen und Dokumente in den gängigen Office-Formaten.

---

### Der Review-Agent

<div class="agent-face"><img src="../images/ai_journey_agent_reviewer.webp" alt="Der Agent als Reviewer"></div>

- Pull Request mit 2.000 Zeilen
- Agent prüft, Mensch bewertet
- Mensch entscheidet

Note:

Karsten. Der Agent in der Rolle des Reviewers. Einen Pull Request mit 2.000 geänderten Zeilen
konnte ein Mensch früher kaum prüfen. Heute prüft der Agent die ganze Änderung, und der Mensch
bewertet seine Befunde. Die letzte Entscheidung liegt weiter beim Menschen.

Überleitung: „Und wie bewerten wir, was der Agent liefert?“

---

### Unser Zielbild: Closed Loop Engineering

<div class="mermaid loop-graph">
<pre>
---
config:
  theme: base
  themeVariables:
    fontSize: 30px
    lineColor: "#ffffff"
  flowchart:
    curve: basis
---
flowchart LR
  req(["Anforderungen"]):::human <-- Refinement --> story["User Story"]:::agent
  story --> plan["Plan"]:::agent
  plan --> tdd["TDD"]:::agent
  tdd --> review["Review"]:::agent
  review --> gate["Gate"]:::agent
  gate -- grün --> accept(["Abnahme"]):::human
  review -. Befund .-> tdd
  gate -. rot .-> tdd
  linkStyle 0 color:#ffffff
  linkStyle 5 stroke:#76FF03,stroke-width:3px,color:#76FF03
  linkStyle 7 stroke:#FF8A80,stroke-width:3px,color:#FF8A80
  linkStyle 6 color:#ffffff
  classDef human fill:#ffd54f,stroke:#ffd54f,color:#002b36
  classDef agent fill:#4dd0e1,stroke:#4dd0e1,color:#002b36
</pre>
</div>

<p class="deck-url"><span class="highlighted-yellow">Gelb:</span> Mensch · <span class="highlighted-cyan">Blau:</span> Agent</p>

Note:

Karsten. Das ist unser Zielbild, so wollen wir mit dem Agenten arbeiten. Wir sind noch nicht
da. Gelb ist der Mensch, blau der Agent.

Der Mensch bringt die Anforderungen mit. Im Refinement schreibt der Agent mit ihm zusammen die
User Story, im Dialog: Der Agent fragt nach, der Mensch schärft die Anforderungen. Aus der User
Story macht der Agent einen Plan aus kleinen Tasks. Jeden
Task setzt er mit TDD um, testgetrieben: zuerst der Test, dann der Code. Ein zweiter Agent prüft die Änderung
gegen eine Rubrik, also gegen unsere Kriterien. Findet er etwas, ist das ein Befund, und der Agent bessert nach.

Am Ende läuft das Gate: alle Tests, der Lint, die CI. Fertig ist der Loop erst, wenn das Gate
grün ist, nicht wenn ein Agent sagt, es sei gut. Rot schickt die Arbeit zurück, erst grün geht
weiter zur Abnahme.

Dann nimmt der Mensch ab: Er prüft den Nachweis, den der Agent in den Pull Request schreibt.
Die Kriterien stehen in der Rubrik, das Urteil fällt der Mensch. Das führt direkt zur nächsten
Folie.

Offen sagen, wo wir heute stehen: Einzelne Schritte gibt es schon, aber noch nicht als
geschlossenen Loop. Heute stoßen wir viele Schritte von Hand an und prüfen zwischendurch selbst.

---

### Jede Antwort klingt gut

- <span class="highlighted-red">2022:</span> klingt gut, oft falsch
- <span class="highlighted-green">Heute:</span> klingt gut, meist richtig
- Der eine Fehler fällt kaum auf
- Es läuft – aber ist es gut?

<p class="fragment"><strong>Der Agent braucht Qualitätskriterien von uns!</strong></p>

Note:

Judith und Karsten im Dialog. Kapitel 5 des Artikels. Schon 2022 klangen die Vorschläge immer
gut. Das ist geblieben. Geändert hat sich, wie oft sie stimmen. Und das macht die Bewertung
schwerer: Wenn fast alles stimmt, fällt der eine Fehler kaum noch auf.

Und selbst wenn alles funktioniert, ist die Qualität damit nicht sichergestellt. Der Agent kennt
die Kriterien nicht, die uns wichtig sind, solange wir sie ihm nicht sagen: in der `AGENTS.md`,
in den Skills, in der User Story. Im Embedded-Umfeld gilt: „Was ich nicht verstehe, kann ich
nicht freigeben.“

Und genau das prüfen wir jetzt bei unserem Agenten. Überleitung zur Demo.

---

### Die Abnahme

- Anforderungen ↔ SW Detailed Design (SWDD)
- SWDD ↔ Code
- SWDD ↔ Tests
- Tests ↔ Testergebnisse
- UAT: Geht das Licht nach 10 Sekunden aus?

<p class="fragment"><strong>Angenommen?</strong></p>

Note:

Judith wechselt ins Terminal. Karsten nimmt als Product Owner ab und geht die Liste von oben nach
unten durch. Judith zeigt zu jedem Punkt das Work Product, das der Agent geliefert hat. Beim
ersten Punkt einmal sagen: SWDD heißt Software Detailed Design.

1. Anforderungen ↔ SWDD: Verweist das Detailed Design auf REQ_39, REQ_40 und REQ_59?
2. SWDD ↔ Code: Verweist der Code auf das Detailed Design?
3. SWDD ↔ Tests: Verweisen die Unit-Tests auf das Detailed Design?
4. Tests ↔ Testergebnisse: Sind die Tests grün, und zeigt der Bericht Coverage und
   Traceability?
5. UAT: Geht das Licht nach 10 Sekunden ohne Bedienung aus?

Dabei fragt Karsten: Kann ein Mensch es gut lesen? Was hat der Agent dort entschieden, wo die
Anforderungen nichts sagen, und können wir damit leben?

Dann das Urteil: angenommen, mit Fragen zurück oder abgelehnt. Ehrlich bewerten, auch wenn etwas
schiefgegangen ist. Ist der Agent nicht fertig, zeigt Judith, was bis jetzt fertig ist, oder das
Ergebnis aus einem Probelauf. Sie sagt offen, was sie zeigt.

---

### Fazit

- Praktikant ist jetzt Mitarbeiter
- Wir sind Chefs von Agenten
- Skills und Qualitätskriterien passen sie an

<div class="fragment">

**Was meint ihr?**

- Wie sieht euer Workflow aus?
- Wie viel Kontrolle braucht ein Agent?

</div>

Note:

Karsten. Die Zusammenfassung des Artikels. Er schreibt Code, Tests, Dokumentation, User Stories
und Präsentationen. Aus dem Praktikanten ist ein Mitarbeiter geworden, und wir sind die Chefs
von Agenten: Wir geben die Aufgabe vor, und das Urteil fällen wir. Mit Skills und
Qualitätskriterien passen wir sie an unsere Umgebung an. Auch der Artikel ist so entstanden:
zwei Menschen und ein Agent.

Dann die Fragen einblenden. Wie sieht euer Workflow mit Agenten aus? Und wie viel Kontrolle
braucht ein Agent? Unsere Antwort von heute: ein Prompt von einer Zeile, und der Agent
entscheidet selbst, statt nachzufragen. Was meint ihr?

---

### Questions?

<div class="qr">

![QR code of the slides](../images/qr_ai_journey.png)

</div>

https://avengineers.github.io/ESE-2026/docs/ai_journey/ <!-- .element: class="deck-url" -->

---

### Some Links

- [We@GitHub](https://github.com/avengineers)
- [Printable Slides](https://avengineers.github.io/ESE-2026/docs/ai_journey/?print-pdf)
