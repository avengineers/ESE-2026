# Brainstorming: Faden durch den Vortrag

<!-- The result of our brainstorming on 2026-09-24. The notes for the slides of this talk.
     The article is in article/index.md.
     The section "Ablauf des Vortrags" was added on 2026-10-29 and is the plan for the slides. -->

## Ablauf des Vortrags

Stand 2026-10-29. Der Plan, nach dem die Folien entstehen.

### Die Idee

Der Artikel endet mit dem Satz: Der Agent liefert für jedes Problem eine Antwort, und wir müssen
lernen, diese Antwort zu bewerten. Der Vortrag zeigt das, statt es nur zu erzählen. Am Anfang
bekommt ein Agent live eine echte Aufgabe. Während er arbeitet, halten wir den Vortrag. Am Ende
bewerten wir vor dem Publikum, was er geliefert hat.

Die Rollen bilden eine Klammer: Karsten ist der Product Owner (PO), der die Aufgabe vergibt,
Judith die Entwicklerin, die sie bekommt. Am Anfang vergibt der PO die Aufgabe, am Ende nimmt er
sie ab. Bewerten wird so zu einer Abnahme, die jeder im Saal kennt.

### Ziele

- Das Publikum sieht einen Agenten eine User Story von der Anforderung bis zum getesteten Code
  umsetzen, nach Automotive SPICE, an SPLed.
- Das Publikum sieht, wie wir das Ergebnis bewerten: was stimmt, was fehlt, welche Fragen der
  Agent gestellt hat.
- Der Vortrag folgt dem Artikel. Wer den Tagungsband liest, erkennt ihn wieder.

### Was wir nicht wollen

- Eine Demo, die gecoacht wirkt. Der Prompt ist kurz, die Aufgabe steht auf der Folie, und wie
  man in SPLed eine Komponente baut, steht im Repository, nicht im Prompt.
- Ein Ergebnis, das wir schönreden. Scheitert der Agent oder wird er nicht fertig, sagen wir das
  offen. Auch das belegt die Botschaft.
- Den Eindruck, das Feature habe es nie gegeben. Wir sagen offen: Auto Off gibt es in SPLed, wir
  haben es entfernt, damit ihr zuseht, wie es neu entsteht.

### Zeitplan

30 Minuten: 5 Minuten Demo starten, 20 Minuten Vortrag, 5 Minuten Demo-Ergebnis.

**Teil 1 · Demo starten (5 min)**

1. Titelfolie, Karsten: Begrüßung. Er entschuldigt sich beim Publikum: Wir müssen erst noch
   unserer SW Factory eine Aufgabe geben.
2. Die Aufgabe, für Judith überraschend: eine User Story vom PO. Judith reagiert genervt und
   gestresst („Jetzt? Ich halte gerade einen Vortrag!“) und sagt dann den Titel des Vortrags:
   „Frag doch den Agenten!“
3. Judith gibt den vorbereiteten, kurzen Prompt ein, und der Agent legt los. Das Terminal bleibt
   kurz sichtbar.

**Teil 2 · Vortrag (20 min)**

| min | Abschnitt | Wer | Artikel |
|---|---|---|---|
| 1 | Wer sind wir? | beide, jede Person über sich | — |
| 4 | Ein Schülerpraktikant im Editor: Code Completion seit 2022, ChatGPT, Vibe Coding | Judith | Kap. 1 |
| 3 | Der Wendepunkt: Ende 2025, Schulung, neue Modelle, MCP, eine ganze Story für den Agenten | Karsten | Kap. 2 |
| 2,5 | Skills I: „Meine Claude programmiert besser als deiner!“, persönliche Setups, ein Skill als Beispiel | Judith | Kap. 3 |
| 2,5 | Skills II: Skills als Produkt eines Plattform-Teams | Karsten | Kap. 3 |
| 1,5 | Beispiel Backlog: Die Story auf Folie 2 und das Ticket für diesen Vortrag hat der Agent geschrieben; auf der Folie steht eine bereinigte Kopie ohne Ticket-Nummer und interne Links *(Entscheidung von Claude)* | Karsten | Kap. 4 |
| 1,5 | Beispiel Folien als Code: auch diese Folien | Judith | Kap. 4 |
| 4 | Jede Antwort klingt gut: Vibe Coding gegen produktiven Code, der Agent hilft beim Bewerten, die letzte Entscheidung bleibt beim Menschen | beide, als Dialog | Kap. 5 |

Wir wechseln etwa alle drei Minuten. Das erste Beispiel des Artikels, Automotive SPICE, hat
in Teil 2 keinen eigenen Abschnitt: Es ist die Demo, und wir zeigen es in Teil 3. Seine zwei
Minuten gehen an den Schülerpraktikanten und an „Jede Antwort klingt gut“.
*(Verteilung: Entscheidung von Claude.)*

**Teil 3 · Demo-Ergebnis (5 min)**

1. Judith zeigt, was der Agent geliefert hat: Detailed Design, Testspezifikation,
   Konfigurationsschalter, Code, Unit-Tests und den Komponentenbericht mit Coverage und
   Traceability.
2. Karsten nimmt als PO ab, live, nach den Kriterien der User Story: angenommen, mit Fragen
   zurück oder abgelehnt. Die Maßstäbe kommen aus dem Artikel: Stimmt es? Passt es zu unserer
   Architektur und Arbeitsweise? Kann ein Mensch es gut lesen? Dazu: Welche Fragen hat der
   Agent gestellt, und was hat er stillschweigend entschieden?
3. Wir bewerten das Ergebnis für sich, ohne Vergleich mit der Implementierung, die es schon gab.
4. Karsten schließt mit der Zusammenfassung: Aus dem Schülerpraktikanten ist ein Kollege
   geworden.
5. Die Fragerunde. Sie ist die einzige Stelle, an der das Publikum spricht. Eine Folie vor
   „Questions?“ zeigt die drei offenen Fragen aus dem Artikel als Einstieg in eine kurze
   Diskussion: Ist ein möglichst kurzer Prompt besser, der dem Agenten viel Freiheit lässt? Oder
   soll der Agent lieber alles nachfragen? Wie viel Kontrolle braucht ein Agent? Die Demo hat
   gerade eine Antwort gezeigt, die wir zur Diskussion stellen: ein Prompt von einer Zeile, und
   der Agent sammelt seine Fragen, statt nachzufragen. Die Fragen stehen auf einer eigenen
   Folie, weil „Questions?“ in allen drei Decks gleich aussieht. *(Eigene Folie: Entscheidung
   von Claude.)*
6. Dann folgen „Questions?“ und „Some Links“.

### Die Demo

- **Aufgabe:** Auto Off in SPLed. Das Licht geht nach einer einstellbaren Zeit ohne Bedienung
  aus. Es ist ein wählbares Feature der Produktlinie: Die Varianten Sleep und IDEA/Sloemada
  wählen es, Disco und Spa nicht.
- **Folie 2 ist die User Story.** Sie entsteht aus der User Story der Demo beim International
  Software Workshop in Rietheim: auf Deutsch, gekürzt, so dass das Publikum sie lesen kann. Sie
  nennt die Anforderungen REQ_39, REQ_40 und REQ_59 und enthält kein Design, keinen Algorithmus
  und keine Dateinamen. Ein Kriterium bleibt auf jeden Fall drin: Was die Anforderungen
  offenlassen, meldet der Agent als Frage, statt es stillschweigend zu entscheiden.
- **Der Agent liest die Aufgabe von der Folie.** Die User Story steht in einer eigenen
  Markdown-Datei, die `index.html` als eigene `<section>` lädt. So sieht der Agent nur die
  Aufgabe, nicht den Rest des Decks mit Teil 3 und den Kriterien unserer Bewertung. Er liest sie
  über GitHub, denn das Repository ist zum Vortrag öffentlich; eine lokale Kopie liegt als
  Rückfall bereit. *(Entscheidung von Claude.)*
- **Der Prompt** ist eine Zeile, etwa: „Setz die User Story auf Folie 2 in SPLed um.“
- **Fragen des Agenten:** Er hält nicht an, um auf Antworten zu warten. Er schreibt seine Fragen
  auf und arbeitet weiter, und in Teil 3 zeigen wir die Liste. Die User Story sagt das so, damit
  der Agent nicht 20 Minuten auf eine Antwort wartet. Er läuft in einem Modus ohne
  Bestätigungen, im Dev Container. *(Entscheidung von Claude.)*
- **Der Startstand** ist der aus Rietheim: SPLed ohne die Komponente Auto Off, ohne Feature-Schalter
  und ohne Auswahl in den Varianten. Die Anforderungen, die Schnittstelle in der RTE und der
  Verbraucher in `power_signal_processing` sind da. Die Lücken in den Anforderungen bleiben
  absichtlich drin: Zum Beispiel legt keine Anforderung den Zustand nach dem Einschalten fest.
- **Umgebung:** Der Agent ist Claude Code und läuft lokal auf Karstens Rechner, in der WSL, im
  Dev Container von SPLed. Der Startstand liegt vorher lokal vor. Die Demo braucht kein
  Firmennetz, und auf dem Bildschirm erscheint kein interner Hostname. Sie braucht aber eine
  Internetverbindung zu Claude; die prüfen wir vorher ohne Firmen-Proxy.
- **Setup des Agenten:** Karstens echtes Setup, mit seiner globalen `CLAUDE.md`, seinen Skills
  und Plugins. Das sagen wir auf der Bühne offen, am besten in „Skills I“: Der Agent auf der
  Bühne ist „meine Claude“.
- **Ein Rechner:** Deck, Agent und Aufzeichnung laufen auf Karstens Rechner. Wir schalten
  zwischen Folien und Terminal um: in Teil 1 zum Starten, in Teil 3 zum Zeigen. Dazwischen
  bleibt das Terminal im Hintergrund.
- **Vorarbeit in SPLed:** Den Startstand gibt es als internen Branch aus Rietheim. Die Regel für
  Builds im `AGENTS.md` von SPLed fehlt noch. Beides gehört zur Vorbereitung, vor den
  Probeläufen.
- **Zeit:** In Rietheim brauchte der Agent rund 40 Minuten, vor allem wegen zu vieler Builds und
  Testläufe. Hier hat er rund 20 Minuten. Das `AGENTS.md` von SPLed bekommt dafür eine allgemeine
  Regel: nur die betroffenen Varianten bauen und testen, den vollen Lauf über alle Varianten
  einmal am Ende.
- **Probeläufe:** Zwei bis drei Läufe vom kalten Start, mit Stoppuhr. Sie zeigen, ob der Agent
  in 20 Minuten fertig wird, und liefern das Backup.
- **Wenn die Demo nicht fertig ist:** Wir starten den Agenten in jedem Fall live. Ist er in Teil 3
  nicht fertig, zeigen wir entweder, was bis dahin fertig ist, oder das Ergebnis aus einem
  Probelauf, das Backup. Wir sagen offen, was wir zeigen.
- **Plan B:** Ein aufgezeichneter Lauf liegt in jedem Fall bereit, auch für den Fall, dass das
  Netz vor Ort ausfällt.

### Folgen für dieses Repository

- Das Deck weicht von der Regel in `AGENTS.md` ab: Auf die Titelfolie folgt hier die Aufgabe,
  „Who are we?“ steht am Anfang von Teil 2. `AGENTS.md` hält diese Ausnahme fest.

### Was noch offen ist

- Der genaue Text von Folie 2 und der genaue Prompt.
- Die Folien von Teil 2, Abschnitt für Abschnitt, aus dem Artikel und den Notizen unten.
- Wie wir in Teil 3 durch das Ergebnis führen: welche Dateien und welche Seiten des Berichts.
- Modell und Einstellung des Agenten für die Demo, festgelegt nach den Probeläufen.

## Notizen vom 2026-09-24

- Am Anfang Live-Demo starten in SPLed mit GitHub issue (analog zur Demo 1 beim "International Software Workshop" in Rietheim)
- Wie hat alles angefangen:
  - ChatGPT hat mal ein Skript erstellt, oder eine VS Code Extension
  - Code-Vervollständigung in VS Code
  - Code-Vorschläge beim Programmieren: mal ne Funktion, mal ne Schleife.
  - Brauchbar: man musste die Syntax nicht mehr kennen.
  - Große Hilfe bei Python, CMake, C++, GoogleTest
  - Struktur und Architektur kamen immer noch von uns.
  - Vorschläge klangen immer toll.
  - Hilfe bei Erstellung von Dokumentation
  - Trotzdem fehlerhaft und nicht funktional
  - viel halluziniert.
- Dann kamen die Agenten:
  - Eigentlich wie vorher benutzt
  - Aber jetzt mit Prompts wie: schreib mir mal bitte eine Funktion, die das und das macht.
  - Ende 2025 kamen neue Modelle (z.B.: Claude Opus 4.5)
  - Passt gut zu unserem ESE Vortrag, die Folien schrieben sich von alleine. ;-)
- Team Schulung
  - Trainer gaben uns neue Sicht
  - "Frag doch den Agenten!"
    - MCP
    - Skills
    - SDD
    - Plötzlich gab man einem Agenten eine User Story oder ein ganzes Feature zur Bearbeitung.
- Großteil unserer User und auch wir haben GitHub Copilot
- Aber jeder Entwickler im Team benutzt Claude Code (irgendwie besser!?!)
- Meine Claude programmiert besser als deiner!
- Jeder pflegt seinen eigenen DevStack
  - Persönliche CLAUDE.md
  - Favorisierte Skillsets
  - Eigene Skillsets
- Offene Fragen/Diskussionspunkte:
  - Möglichst kurzer Prompt für maximalen Output?
  - Oder besser alles nachfragen?
  - Wie viel Kontrolle braucht ein Agent?
- Use Cases:
  - A.SPICE konforme Softwareentwicklung (Demo am Anfang gestartet.)
    - Requirements sind Vorgabe
    - Erstellt werden
      - Architektur
      - Detailed Design
      - Testspezifikation
      - Source Code
      - Requirements Coverage
      - Traceability
      - Code Coverage
  - Erzeugung von Backlog Tickets
    - Vorteile
      - Einheitliches Format
      - Großes Kontextfenster: der Agent berücksichtigt Fakten und Randbedingungen, an die der Mensch oft nicht gedacht hat.
      - Schnelle Erzeugung von Diskussionsgrundlagen
    - Nachteile
      - Zu viele Details für einen Menschen
  - Fehleranalyse
    - Skill für Jenkins
    - Warum ist mein CI Build rot?
  - Pull Request Review
    - Wirklich? 2000 Zeilen?
  - Urlaubsübergabe
    - Wie weit bin ich gekommen.
    - Wo kannst du weitermachen.
  - Skills als Produkt eines Platform Teams
    - Wie schreibt man gute Unit Tests.
    - Wie starte ich einen Build.
    - Wie erzeugt man einen Test Report.
  - Entwicklungsergebnisse managementtauglich darstellen
    - Präsentationen mit reveal.js
    - Konferenzfolien ;-)
    - Claude kann Excel, Word und Co.
