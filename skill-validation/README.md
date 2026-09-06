# Skill Validation

This directory contains the repository's validation contracts, packaged scenarios,
mechanical runner, and legacy records. This page is navigation only; it creates no
new validation authority or workflow.

Before authoring, editing or evaluating a skill, read the [charter](charter/core-contracts.md).
It already defines each skill's intended behavior through named invariants; test that contract rather than reconstructing it from the current skill's wording.
The [overall rewrite goal](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#overall-goal) and [RED/GREEN authoring requirement](../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#redgreen-authoring-requirement) explain what this testing infrastructure supports.

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
  It is not yet an approved production implementation specification.

The broader baseline organization design is deferred. This index does not designate
accepted baselines, create manifests or campaign state, or declare any scenario
audited.
