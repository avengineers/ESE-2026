# Beyond Software: The Rise of “Engineering as Code” in Embedded Systems

How requirements, architecture, design and tests become one testable repository

Akshit Kobagapu, Judith Reichwein, Marquardt GmbH

<!-- The proceedings article for this talk, in English.
     The organizer's rules are in AGENTS.md, section "The articles".
     American English throughout, matching the en-US stamp of the Word file.
     Draft of 2026-10-01. scripts/make_docx.py makes the Word file; Figure 1 becomes
     an image there. Figure 2 is a screenshot of a generated component report. -->

However an embedded team keeps its source code, the engineering artifacts around it tend to live somewhere else. Requirements sit in one tool, the architecture in a second, the detailed design in a third, the test results in a fourth. Each tool is good at its job, and the chain between them is held together by people. In this article we describe how we moved those artifacts into the repository, as text, next to the code they describe. We show how the links between them are checked by the build, how one feature model serves many product variants, and why this turns out to be the ground an AI agent needs.

## A day with six tools

Between a new requirement and tested code there are typically half a dozen systems, each owned by a different part of the organization. How well they serve their users varies a great deal. Some teams open a requirement in a second, others wait; some receive an architecture as a live model, others as a picture. That friction is worth fixing, but it is not our argument, because the problem we want to describe is the one that remains after every tool has been chosen well.

At each boundary the information is copied. A copy is accurate on the day it is made, and from then on it is a claim about a document somebody else owns. The developer works against the design they were given, not against the design as it stands today. The tester works against the specification they were given. Each handoff is sound in itself, and none of them is checked again afterwards.

Consistency across the whole chain is therefore a periodic human activity, often a spreadsheet filled in before a review or an audit. It is correct at the moment it is assembled. When a requirement moves afterwards and the design does not follow, nothing in the process objects: the build passes, the tests pass, the review passes, and the spreadsheet is still green. The defect lives in the relationship between two documents, and no tool in the chain owns that relationship.

## What Engineering as Code means

If no tool owns the relationship between two documents, the relationship has to become something a tool can own. That is the whole idea. We move the engineering artifacts into the repository, beside the code they describe, and we write the links between them in a form the build can read. The name follows infrastructure as code and documentation as code, which made the same move for servers and for manuals.

In practice it means three things. The artifacts are text, so they are versioned, diffed and reviewed like code. Each one carries an identifier and names what it depends on, so a link is data rather than a sentence somebody has to notice. And the build resolves those links, so the evidence comes out of the command that compiles the software, every time, instead of out of a person before a review.

This is not the same as keeping documentation in the repository, which many teams already do. A design document can state in its own text that it implements requirement 39, and a person who reads that sentence learns something. The build learns nothing, because a sentence is prose. Written instead as a named link, the same fact becomes a question anyone can ask of the whole repository, and the useful questions are the ones nobody can answer by reading: which requirements have no test, which specifications nothing implements, which results belong to this variant and not that one.

## One repository, one chain

In SPLed [1], a small product line that builds a configurable light, every component is a folder with three parts: src, test and doc. The doc part is not a write-up produced after the work. It holds the detailed design, split into separate specifications, each with its own identifier, and it is built along with the software.

The Light Controller decides whether the light is on, in what color, and whether it blinks. Its three parts are held together by one rule: every artifact names what justifies it, and nothing names what follows from it. A specification refines the architecture. An implementation names the specification it implements and the requirement it fulfills. A test names the specification it verifies. Keeping that direction consistent is what lets a test be added without touching anything above it.

```text
/**
 * @rst
 * .. impl:: Light Controller's main function
 *    :id: SWIMPL_LC-006
 *    :implements: SWDD_LC-100
 *    :fulfills: REQ_44
 * @endrst
 */
void lightController(void)
{
    static LightState currentLightState = LIGHT_OFF;
    const PowerState currentPowerState =
        RteGetPowerState();
#ifdef CONFIG_BLINKING
    static uint32_t blinkCounter = 0;
    const percentage_t mainKnobValue =
        RteGetMainKnobValue();
#endif
```

Figure 1: The main function of the Light Controller, carrying its identifier, the design specification it implements and the requirement it fulfills. The links sit in the comment above the function, and inside it a feature switch decides whether this product blinks at all. Source: SPLed [1], MIT license.

Those identifiers are data rather than sentences, so the build can follow them. It produces a component report with requirements coverage, code coverage, and the path from a requirement to the test result that proves it, from the same command that compiles the software. We use spl-core [2] and Sphinx-Needs [3] for this. What matters is not the choice of tools but that the artifacts are text and the links are data.

<!-- Figure 2: the generated Light Controller report of the Sleep variant, built from
     the public SPLed repository and screenshotted from the local build output with
     Edge headless at device scale factor 3 in the light theme, cropped to the
     first specification card. 2710 px wide at 300 dpi. -->

![One specification in the generated report, showing its links](../../images/spled_light_traceability.png)

Figure 2: The same links in the generated report of the Sleep variant. The build has resolved them in both directions, so SWDD_LC-100 now names SWIMPL_LC-006 from Figure 1 as its implementation, and the test cases that verify it. Source: SPLed [1], MIT license.

The difference shows in review. When a pull request changes a source file, the reviewer can see in the same diff which design changed with it and which requirement that design serves.

## One source, many variants

A product line has a problem the single product does not: the same component behaves differently in each variant. That leaves two bad options, a document per variant or one document that describes all of them and matches none.

We take a third. The design document carries the same feature conditions as the code. A specification that belongs to an optional feature is wrapped in a condition on that feature, and so is the test that verifies it. When the report is generated for one variant, the feature selection resolves the documents as well as the sources, and the reader sees the specifications and test results of that product and nothing else.

Blinking shows it end to end. It is one symbol in the feature model, and every variant answers it.

```text
KConfig
    config BLINKING
        bool "Blinking Feature"
        default n

variants/Disco/config.txt
    CONFIG_BLINKING=y

variants/Sleep/config.txt
    # CONFIG_BLINKING is not set
```

Figure 3: The blinking feature in the feature model, selected by Disco and left out by Sleep. The same symbol guards the implementation in Figure 1 and the specification that describes it. Source: SPLed [1], MIT license.

![The design document source, with one specification inside a feature condition](../../images/spled_variant_source.png)

Figure 4: The design document of the Light Controller. Three specifications are written once, and the middle one stands inside a condition on the blinking feature. Long lines are wrapped for print. Source: SPLed [1], MIT license.

![The same component report for two variants, one with the blinking specification and one without](../../images/spled_variant_comparison.png)

Figure 5: What the build makes of Figure 4. The three specifications written once become three in Disco, which selects the blinking feature, and two in Sleep, which does not. The variant names were added as labels. Source: SPLed [1], MIT license.

One source, one feature model, a correct traceability matrix per variant, and no document maintained twice.

## The requirements come from somewhere else

Requirements usually do not start in the repository, and we do not pretend otherwise. They are authored in a requirements management system, under a process that is not ours to change. The bridge is an export: any such system produces ReqIF [4] or CSV, and we convert that into a small JSON structure with the identifier, the content and the type, imported as the top of the chain.

This keeps the claim honest. We do not author requirements as code; we move them into the repository as versioned objects so the rest of the chain can reach them. It also answers the first objection anyone raises, which is lock-in: the format that brings requirements in takes them out again.

## Why this suits an agent

This benefit was not the reason we started, and it has become the most visible one. An AI agent working on a change needs to know what the change must satisfy. When the artifacts live in four systems behind four logins, the agent sees the code and guesses the rest. When they live in one repository, it reads all of them.

We go one step further and give the agent skills: short written instructions describing how an artifact is written here, which identifier scheme it uses and which links it must carry. The agent then produces a specification, a test and an implementation in the shape the traceability needs, rather than prose a human has to rework.

The structure we built for an audit turned out to be the structure a machine needs to read our work.

## Summary

Moving the engineering artifacts into the repository changed three things for us. The chain from requirement to test result is checked by the build instead of assembled by hand. Every developer generates the full evidence locally, before pushing. And one feature model resolves the documents as well as the code, so each variant has its own correct report from a single source.

None of it depends on our particular tools. It depends on treating an engineering artifact as something with an identifier and a link, rather than as a document. The order of work stays ours, and the honesty of the chain stops being a matter of discipline and becomes a property of the repository. The slides of this talk [5] were written the same way, as text in the same kind of repository.

## References

[1] SPLed, the demonstrator product line: https://github.com/avengineers/SPLed

[2] spl-core, the build framework behind it: https://github.com/avengineers/spl-core

[3] Sphinx-Needs, the traceability extension: https://sphinx-needs.readthedocs.io/

[4] ReqIF, the requirements interchange format: https://www.omg.org/spec/ReqIF/

[5] Slides of this talk: https://avengineers.github.io/ESE-2026/docs/eng_as_code/

## The authors

Akshit is a software engineer in the Rhine-Main Team (RMT) of Marquardt GmbH. He works on software product line engineering, build systems and CI/CD for embedded projects. His focus is the path from an engineering artifact to the evidence a process asks for, with as few manual steps in between as possible.

Judith is a software engineer with more than 14 years of experience in the automotive industry. Her career covers almost the whole V-model, from requirements engineering through software automation and verification, project coordination and unit testing of security components, to simulation. She brings that experience to the Rhine-Main Team (RMT) of Marquardt GmbH as a Senior Software Engineer, where she concentrates on CI/CD, test automation and software product line engineering.
