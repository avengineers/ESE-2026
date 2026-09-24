# „Frag doch den Agenten!"

Wie agentische KI unseren Embedded-Entwicklungsalltag verändert hat

Judith Reichwein, Karsten Guenther, Marquardt GmbH

<!-- The proceedings article for this talk, in German.
     The organiser's rules are in AGENTS.md, section "The articles".
     Draft of 2026-09-24. Figure 1 becomes an image in the Word file. Figure 2 is still missing. -->

2023 setzte unser Team zum ersten Mal KI-gestützte Code Completion ein. Das Ergebnis glich eher der Arbeit eines Schülerpraktikanten als der eines erfahrenen Entwicklers. Heute bekommt bei uns fast jede Frage dieselbe Antwort: „Frag doch den Agenten!" In diesem Beitrag beschreiben wir den Weg dorthin. Wir zeigen, wie wir Agenten mit Skills steuern und an unsere Embedded-Umgebung anpassen, und wir stellen drei Einsatzfelder aus unserem Alltag vor. Am Ende steht unsere wichtigste Erfahrung: Der Agent liefert für jedes Problem eine Antwort, und wir müssen lernen, diese Antwort zu bewerten.

## Ein Schülerpraktikant im Editor

Am Anfang standen einzelne Versuche. ChatGPT schrieb uns ein Skript oder eine kleine Erweiterung für VS Code. Danach zog die Code Completion in den Editor ein. Sie schlug beim Programmieren mal eine Funktion vor, mal eine Schleife. Das war brauchbar, denn wir mussten die Syntax nicht mehr im Kopf haben. Bei Python, CMake, C++ und GoogleTest war das eine große Hilfe, ebenso beim Schreiben von Dokumentation.

Struktur und Architektur kamen weiterhin von uns. Die Vorschläge klangen immer gut, trotzdem waren sie oft fehlerhaft. Der Code funktionierte nicht, und vieles war halluziniert. Wir prüften jede Zeile, so wie man die Arbeit eines Praktikanten prüft. Bei Routineaufgaben entlastete uns das Werkzeug trotzdem, und wir gewannen Zeit für die kreative Arbeit.

## Der Wendepunkt

Die ersten Agenten benutzten wir zunächst wie die Code Completion, nur mit Prompts wie: „Schreib mir bitte eine Funktion, die das und das macht." Ende 2025 änderte sich das. Neue Modelle wie Claude Opus 4.5 kamen auf den Markt, und unser Team besuchte eine Schulung zu agentischer Entwicklung. Die Trainer gaben uns einen neuen Blick auf die Werkzeuge. Ein Agent liest das Repository, schreibt Code, führt Befehle aus, baut, testet und korrigiert seine eigenen Fehler. Über das Model Context Protocol (MCP) [1] erreicht er auch externe Systeme wie das Ticketsystem oder den CI-Server.

Plötzlich gaben wir einem Agenten eine ganze User Story oder ein ganzes Feature zur Bearbeitung. Coding, Testfälle und Dokumentation wurden Routine. Und auf fast jede Frage im Team hieß die Antwort: „Frag doch den Agenten!"

## Skills: Wie wir Agenten steuern

In unserem Umfeld ist GitHub Copilot verbreitet. In unserem Team arbeitet trotzdem jeder mit Claude Code. Eine saubere Begründung dafür haben wir nicht, nur die gemeinsame Beobachtung, dass es für unsere Arbeit besser passt. Außerdem pflegt jeder seinen eigenen Werkzeugkasten: eine persönliche Kontextdatei CLAUDE.md mit eigenen Regeln, bevorzugte Skill-Sammlungen und selbst geschriebene Skills. Bald hieß es im Team: „Meine Claude programmiert besser als deiner!"

Wenn jeder Agent anders arbeitet, liefert dasselbe Projekt unterschiedliche Ergebnisse, je nachdem, wer gerade fragt. Wie steuert man also einen Agenten, und wie passt man ihn an eine bestimmte Umgebung an? Unsere Antwort sind Skills. Ein Skill ist eine Anleitung in Textform, die der Agent lädt, sobald eine Aufgabe dazu passt. Er beschreibt, wie ein Team eine Aufgabe in seiner Umgebung erledigt: welche Werkzeuge es verwendet, welche Konventionen gelten und welche Prüfungen am Ende stehen. Abbildung 1 zeigt einen Ausschnitt aus unserem Skill für Unit-Tests in Embedded C.

```text
---
name: c-unit-testing
description: Write GTest/GMock unit tests for embedded C components
  using Arrange-Act-Assert and hammocking. […]
---

# GTest Unit Testing for Embedded C

## First Contact

1. Which component? — Ask for the component path
2. What's the goal? — New tests from scratch, add tests for a
   specific function, fix a failing test, or refactoring safety net?
3. Existing tests? — Check if test/ directory exists […]
4. Dependencies — Run analyze_dependencies.py […]

## Core Philosophy

Unit tests should:

1. Enable Safe Refactoring
2. Document Behavior
3. Specify Behavior: Describe what the component does, not how
4. Prevent Regressions
```

Abbildung 1: Ausschnitt aus dem Skill „c-unit-testing", gekürzt. Quelle: avengineers/sple-skills [2], MIT-Lizenz.

Als Plattform-Team haben wir deshalb unser Produkt erweitert. Wir liefern neben Werkzeugen und Schulungen jetzt auch Skills: wie man gute Unit-Tests schreibt, wie man einen Build startet, wie man einen Testbericht erzeugt. Der Entwickler muss diese Regeln nicht auswendig kennen, denn sein Agent lädt sie, wenn die Aufgabe passt. So entsteht aus vielen persönlichen Setups ein gemeinsamer Stand für alle Teams, die unsere Plattform nutzen.

## Drei Beispiele aus dem Alltag

Heute hilft uns der Agent an vielen Stellen. Er findet heraus, warum ein CI-Build rot ist. Vor dem Urlaub schreibt er die Übergabe: wie weit wir gekommen sind und wo die Vertretung weitermacht. Drei Einsatzfelder beschreiben wir genauer.

### Von der Anforderung zum getesteten Code

Das erste Beispiel ist Softwareentwicklung nach Automotive SPICE [3]. Wir zeigen es am öffentlichen Demo-Projekt SPLed [4], einer kleinen, aber vollständigen Software-Produktlinie, deren Varianten jeweils eigene Binärdateien erzeugen. Die Funktion heißt Auto Off. Sie schaltet das Licht nach einer einstellbaren Zeit ohne Bedienung aus. Der Agent bekommt eine User Story. Sie nennt die Anforderungen und die gewünschte Wirkung je Variante, enthält aber kein Design, keinen Algorithmus und keine Dateinamen.

Aus der User Story erzeugt der Agent die Kette, die der Prozess verlangt: das Detailed Design, die Testspezifikation, einen Konfigurationsschalter für die Varianten, den Code und die Unit-Tests mit GoogleTest. Danach baut er die Software und führt die Tests aus. Am Ende liegt ein Komponentenbericht vor, mit Requirements Coverage, Code Coverage und Traceability von der Anforderung bis zum Test.

<!-- Figure 2: an excerpt of the component report of SPLed (traceability or coverage).
     Caption: "Abbildung 2: Ausschnitt aus dem Komponentenbericht von Auto Off. Quelle: SPLed [4]."
     300 dpi, light background. -->

Die Gesamtarchitektur bleibt in Menschenhand. Kleinere Entscheidungen trifft der Agent selbst, gestützt auf Skills, zum Beispiel die Frage, wo die Implementierung einer Anforderung am besten hineinpasst. Eine Regel geben wir ihm dabei mit: Was die Anforderungen offenlassen, meldet er als Frage, statt es stillschweigend zu entscheiden.

### Backlog und Planung

Das zweite Beispiel betrifft Teamleiter und Projektmanager. Der Agent schreibt User Stories und Backlog-Einträge und bereitet die Sprintplanung vor. Das Format ist dabei immer gleich. Durch sein großes Kontextfenster berücksichtigt der Agent Fakten und Randbedingungen, an die ein Mensch oft nicht denkt. Außerdem liefert er in kurzer Zeit eine Grundlage, über die das Team diskutieren kann. Der Nachteil ist die Menge: Für einen Menschen enthalten die Einträge oft zu viele Details.

### Ergebnisse managementtauglich darstellen

Das dritte Beispiel steht am Ende der Entwicklung. Oft müssen wir Ergebnisse für Menschen aufbereiten, die den Code nie lesen. Auch das übernimmt der Agent. Er schreibt Präsentationen als Code, bei uns in Markdown mit reveal.js [5], und er erzeugt Tabellen und Dokumente in den gängigen Office-Formaten. Weil die Folien als Text in einem Git-Repository liegen, prüfen und ändern wir sie wie Code. Die Folien zu diesem Vortrag entstehen auf dieselbe Weise [6].

## Jede Antwort klingt gut

Schon 2023 klangen die Vorschläge immer gut. Das ist geblieben. Geändert hat sich, wie oft sie stimmen, und das macht die Bewertung schwerer: Wenn fast alles stimmt, fällt der eine Fehler kaum noch auf. Der Agent liefert für jedes Problem eine Antwort. Die Herausforderung liegt darin, diese Antwort zu bewerten.

Wir warnen deshalb ausdrücklich vor Vibe Coding [7], also davor, generierten Code zu übernehmen, ohne ihn zu verstehen. Im Embedded-Umfeld kann niemand Code freigeben oder warten, den er nicht versteht.

Beim Bewerten hilft der Agent aber selbst mit. Einen Pull Request mit 2.000 geänderten Zeilen konnte ein Mensch früher nur mit hohem Aufwand prüfen. Die Menge der Änderungen war groß, und jeder Kontextwechsel kostete Zeit. Heute prüft der Agent die ganze Änderung, und der Mensch bewertet seine Befunde. Das ist für uns eine große Erleichterung. Die letzte Entscheidung liegt weiterhin beim Menschen.

Einige Fragen sind für uns noch offen. Ist ein möglichst kurzer Prompt besser, der dem Agenten viel Freiheit lässt? Oder soll der Agent lieber alles nachfragen? Und wie viel Kontrolle braucht ein Agent? Diese Fragen diskutieren wir im Vortrag.

## Zusammenfassung

Aus dem Schülerpraktikanten von 2023 ist ein Kollege geworden. Er schreibt Code, Tests, Dokumentation, User Stories und Präsentationen. Mit Skills passen wir ihn an unsere Umgebung an und machen aus vielen persönlichen Setups einen gemeinsamen Stand. Seine Arbeit prüfen wir weiterhin, mit seiner Hilfe, aber nach unserem Urteil. Unser Fazit: Der Mensch als kreativer Treiber wird nicht ersetzt, sondern durch KI unterstützt. Wer KI als Werkzeug begreift, gestaltet seine Arbeit effizienter und kreativer, statt sie als Bedrohung zu fürchten. Auch dieser Beitrag ist so entstanden: Zwei Menschen und ein Agent haben ihn gemeinsam geschrieben.

## Quellen

[1] Model Context Protocol: https://modelcontextprotocol.io/

[2] avengineers/sple-skills: https://github.com/avengineers/sple-skills

[3] Automotive SPICE: https://vda-qmc.de/en/automotive-spice/

[4] SPLed: https://github.com/avengineers/SPLed

[5] reveal.js: https://revealjs.com/

[6] Folien zum Vortrag: https://avengineers.github.io/ESE-2026/docs/ai_journey/

[7] Vibe coding: https://en.wikipedia.org/wiki/Vibe_coding

## Die Autoren

Judith ist Softwareingenieurin mit über 14 Jahren Erfahrung in der Automobilbranche. Ihr beruflicher Werdegang deckt nahezu das gesamte V-Modell ab – von Requirements Engineering über Softwareautomatisierung und Verifikation, Projektkoordination und Unit-Testing von Security-Komponenten bis hin zur Simulation. Diese Erfahrung bringt sie heute als Senior Software Engineer im Rhein-Main Team (RMT) der Marquardt GmbH ein, wo sie sich auf CI/CD, Testautomatisierung und Software Product Line Engineering (SPLE) konzentriert.

Karsten ist seit 25 Jahren leidenschaftlicher Softwareingenieur und kann auf Erfahrungen in der Signalverarbeitung, in eingebetteten Echtzeitsystemen, in der Automatisierung von Entwicklungsprozessen sowie in der Entwicklung von Methoden, Werkzeugen und Pipelines für Continuous Integration (CI) zurückgreifen. Nach Stationen als Ingenieur, Tester und Architekt in der Automobilbranche ist er heute Product Owner der SPLE Platform – Marquardts Internal Developer Platform für eingebettete Softwareteams – im Rhein-Main Team (RMT) der Marquardt GmbH. Er treibt Produktvision und Roadmap, etabliert agentische KI-gestützte Entwicklungspraktiken sowie „Engineering as Code", führt Softwaremetriken und KPIs zur Messung der Produktreife ein und entwickelt das Schulungsprogramm der Plattform kontinuierlich weiter.
