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

Jede Person sagt in ein oder zwei Sätzen, wer sie ist. Dann: „Und während unser Agent arbeitet,
erzählen wir euch, wie es dazu kam.“

---

### 2022: Ein Schülerpraktikant im Editor

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
jede Zeile zu verstehen. Heute heißt das Vibe Coding. Das kommt später wieder.

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

```text
---
name: c-unit-testing
description: Write GTest/GMock unit tests for embedded
  C components using Arrange-Act-Assert and
  hammocking. […]
---

# GTest Unit Testing for Embedded C

## First Contact

1. Which component? — Ask for the component path
2. What's the goal? — New tests from scratch, add
   tests for a specific function, fix a failing test,
   or refactoring safety net? […]
```

<p class="deck-url">Quelle: <a href="https://github.com/avengineers/sple-skills">avengineers/sple-skills</a>, MIT-Lizenz</p>

Note:

Karsten. Ein Skill ist eine Anleitung in Textform. Der Agent lädt sie, sobald eine Aufgabe dazu
passt. Sie sagt, wie ein Team eine Aufgabe in seiner Umgebung erledigt: Werkzeuge, Konventionen,
Prüfungen am Ende. Das ist ein Ausschnitt aus unserem Skill für Unit-Tests in Embedded C.

---

### Skills als Produkt eines Plattform-Teams

- Werkzeuge, Schulungen – und Skills
- Unit-Tests, Build, Testbericht
- Ein gemeinsamer Stand für alle

Note:

Karsten. Als Plattform-Team liefern wir neben Werkzeugen und Schulungen jetzt auch Skills: wie
man gute Unit-Tests schreibt, wie man einen Build startet, wie man einen Testbericht erzeugt. Der
Entwickler muss diese Regeln nicht auswendig kennen, denn sein Agent lädt sie. So wird aus vielen
persönlichen Setups ein gemeinsamer Stand. Damit ist die Frage von eben beantwortet: Wie passt man
einen Agenten an eine Umgebung an?

---

### Der Agent schreibt das Backlog

- User Stories, Sprintplanung
- Einheitliches Format
- Großes Kontextfenster
- Aber: zu viele Details

<p class="fragment">Auch die User Story auf Folie 2</p>

Note:

Karsten. Kapitel 4 des Artikels, zweites Beispiel. Der Agent schreibt User Stories und
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

### Folien als Code

````text
### Folien als Code

- Markdown, reveal.js
- Git-Repository
- Review wie Code
````

Note:

Judith. Kapitel 4 des Artikels, drittes Beispiel. Das ist der Quelltext einer Folie wie dieser.
Die Präsentationen liegen als Markdown in einem Git-Repository, und wir prüfen und ändern sie wie
Code. Der Agent schreibt auch Tabellen und Dokumente in den gängigen Office-Formaten. Diese Folien
sind genau so entstanden: zwei Menschen und ein Agent.

---

### Jede Antwort klingt gut

- 2022: klingt gut, oft falsch
- Heute: klingt gut, meist richtig
- Der eine Fehler fällt kaum auf

Note:

Judith und Karsten im Dialog. Kapitel 5 des Artikels. Schon 2022 klangen die Vorschläge immer
gut. Das ist geblieben. Geändert hat sich, wie oft sie stimmen. Und das macht die Bewertung
schwerer: Wenn fast alles stimmt, fällt der eine Fehler kaum noch auf.

---

### Vibe Coding: wann ja, wann nein

- Wegwerf-Skript: ja
- Produktiver Code: nein

Note:

Judith. Für ein Skript, das wir einmal ausführen und dann löschen, ist Vibe Coding in Ordnung.
Für produktiven Code, der wiederverwendet wird, nicht: Im Embedded-Umfeld kann niemand Code
freigeben oder warten, den er nicht versteht. „Was ich nicht verstehe, kann ich nicht freigeben.“

---

### Der Agent hilft beim Bewerten

- Pull Request, 2.000 Zeilen
- Agent prüft, Mensch bewertet
- Mensch entscheidet

<p class="fragment">Jetzt: unser Agent</p>

Note:

Karsten. Einen Pull Request mit 2.000 geänderten Zeilen konnte ein Mensch früher kaum prüfen.
Heute prüft der Agent die ganze Änderung, und der Mensch bewertet seine Befunde. Die letzte
Entscheidung liegt weiter beim Menschen.

Und genau das machen wir jetzt mit unserem Agenten. Überleitung zur Demo.

---

### Was hat der Agent geliefert?

- Detailed Design, Testspezifikation
- Feature-Schalter
- Code, Unit-Tests
- Bericht: Coverage, Traceability
- Eigene Entscheidungen

Note:

Judith wechselt ins Terminal und zeigt das Ergebnis. Ist der Agent nicht fertig, zeigt sie, was
bis jetzt fertig ist, oder das Ergebnis aus einem Probelauf. Sie sagt offen, was sie zeigt.

Eigene Entscheidungen: Was hat der Agent festgelegt, wo die Anforderungen nichts sagen?

---

### Die Abnahme

- Korrekt?
- Passend zu Architektur und Arbeitsweise?
- Lesbar?
- Eigene Entscheidungen vertretbar?

<p class="fragment">Angenommen?</p>

Note:

Karsten nimmt als Product Owner ab, nach den Akzeptanzkriterien von Folie 2 und nach diesen
Fragen: Stimmt es, also Tests grün und Anforderungen abgedeckt? Passt es zu unserer Architektur
und Arbeitsweise? Kann ein Mensch es gut lesen? Was hat der Agent selbst entschieden, und können
wir damit leben? Dann das Urteil: angenommen, mit Fragen zurück oder abgelehnt. Ehrlich
bewerten, auch wenn etwas schiefgegangen ist.

---

### Aus dem Praktikanten ist ein Kollege geworden

- Code, Tests, Doku, Stories, Folien
- Skills passen ihn an
- Das Urteil fällen wir

Note:

Karsten. Die Zusammenfassung des Artikels. Er schreibt Code, Tests, Dokumentation, User Stories
und Präsentationen. Mit Skills passen wir ihn an unsere Umgebung an. Seine Ergebnisse bewerten
wir weiter selbst. Dabei hilft er uns, aber das Urteil fällen wir. Auch der Artikel ist so
entstanden: zwei Menschen und ein Agent.

---

### Zur Diskussion

- Kurzer Prompt oder ausführlicher?
- Selbst entscheiden oder nachfragen?
- Wie viel Kontrolle?

Note:

Die drei offenen Fragen aus dem Artikel: Ist ein möglichst kurzer Prompt besser, der dem Agenten
viel Freiheit lässt? Oder soll der Agent lieber alles nachfragen? Wie viel Kontrolle braucht ein
Agent?

Unsere Antwort von heute: ein Prompt von einer Zeile, und der Agent entscheidet selbst, statt
nachzufragen. Was meint ihr?

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
