# Skill Validation

This directory contains the repository's validation contracts, packaged scenarios,
mechanical runner, and legacy records. This page summarizes the testing approach
and links its governing contracts; it creates no new scoring rules or execution authority.

Before authoring, editing or evaluating a skill, read the [charter](charter/core-contracts.md).
It already defines each skill's intended behavior through named invariants; test that contract rather than reconstructing it from the current skill's wording.
The [overall rewrite goal](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#overall-goal) and [RED/GREEN authoring requirement](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#redgreen-authoring-requirement) explain what this testing infrastructure supports.

## Model-led testing

Testing is model-led, built around the existing simple, reusable, deterministic tools: dumb tools for smart agents.
The orchestrating model selects or prepares tests from the charter, audits inputs, invokes the tools, inspects raw evidence and applies the scenario rubrics.
The tools scaffold execution and record results; they do not decide what good skill behavior means.

- [`skilltest run CONFIG`](runner/README.md#run) prepares one declared run, invokes the configured provider and retains mechanical evidence.
- [`skilltest worksheet SCENARIO RUN_BUNDLE --output PATH`](runner/README.md#worksheet) renders run metadata and a blank assessment worksheet for the model to complete.

Reuse these tools for the testing workflow; extend them only when an observed mechanical gap justifies it, rather than building a separate autonomous testing framework.
The intended workflow is agent-followed written runbooks for baseline collection and skill edits, not more shell or Python programs.
Those runbooks specify fixture setup, exact commands, models/effort, actual CLI-version capture, repetitions, validation and evidence review before collection; routine test changes belong in those documents and test inputs, not runner code.
The [pilot-first scope](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-immediate-scope-one-usable-pilot) starts with one provisional runbook and a few Codex / gpt-5.6-sol / low scenarios in the existing layout, with medium available for justified workflow diagnostics; Claude integration, the broader campaign and reorganization wait for practical feedback.
The [provisional pilot runbook](pilot/README.md) provides frozen DR-02/LP-01 inputs, commands and checkpoints; both conditions passed scoped read/write qualification, with results in the implementation plan and scratch summary. No behavioral pilot observations have been collected.
For new controlled testing, keep current accepted evidence in the working tree and recover superseded accepted results from Git history, rather than maintaining dated result archives; commit accepted evidence before replacing it.
Active experiments remain scratch-only pending review; historical baseline judgments and evidence remain protected, with only the [metadata-only CLI-version worksheet backfill](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-baseline-decision-current-dd-and-no-dd-with-cli-provenance) authorized.
The orchestrator owns evidence-backed judgments, the owner retains acceptance authority, and provider calls remain subject to approval.
The [live design](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-methodology-decision-model-led-testing-with-simple-tools) records the accepted model/tool boundary and remaining controlled-comparison work; the Codex runtime controls and worksheet provenance field are implemented, and the behavioral procedure pilot awaits command approval.

## Authority map

- [Core contracts](charter/core-contracts.md) records the owner-approved validation
  architecture and proposed core portfolios. Its own status governs what is active.
- [Scenario index](scenarios/README.md) inventories the packaged schema `"0.2"`
  scenarios and identifies their source and packaging authority.
- [Methodology](../plans/completed/specs/2026-09-02-skill-testing-methodology-design.md)
  defines the evaluation ledgers, evidence review and scenario verdicts.
- [Runner](runner/README.md) defines the mechanical `skilltest` interface. It does
  not score evidence or assign behavioral verdicts, and provider invocation still
  requires explicit owner approval.
- [Legacy archive](archive/README.md) holds the pre-baseline validation records.
  Until an approved catalog replaces one, its archived per-skill record remains the
  update target required by `CLAUDE.md`.
- [Controlled-input design amendment](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md)
  records accepted feasibility constraints and the current step-by-step design discussion.
  Its status identifies approved implementation units separately from deferred work and provider-call approvals.

The broader baseline organization design is deferred. This index does not designate
accepted baselines, create manifests or campaign state, or declare any scenario
audited.
