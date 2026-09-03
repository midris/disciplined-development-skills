# Skill Validation Baseline Organization Design

**Status:** Design approved in conversation on 2026-09-03; written artifact awaiting owner review.

## Purpose

Establish a consistent, skill-by-skill process for auditing the existing validation portfolio and recording reproducible baselines for the skills currently on `main`.

The baseline is descriptive, not aspirational.
A judgeable failure is valid baseline evidence when it accurately records current behavior.
Rewrite evaluation begins only after the current-skill baseline portfolio is complete enough to support a fair comparison.

## Authority and Scope

This design extends the testing methodology in [`plans/completed/specs/2026-09-02-skill-testing-methodology-design.md`](../completed/specs/2026-09-02-skill-testing-methodology-design.md).

The existing methodology remains authoritative for:

- provider approval gates;
- mechanical runner responsibilities;
- semantic review responsibilities;
- run identity and provenance;
- infrastructure retry classification; and
- accepted-result replacement through Git history.

This design becomes authoritative for validation-record organization, scenario disposition, skill-level baseline rollups, and accepted baseline-set layout after implementation.
Its accepted baseline-set layout supersedes the single-run `accepted/` layout in the earlier methodology.

The first implementation slice includes only repository organization and the `disciplined-research` audit.
It does not authorize provider invocations.

## Design Principles

1. **Colocate the audit with the scenarios.**
   The scenario hierarchy is already the natural unit of validation work, so a second per-skill hierarchy under a top-level `baselines/` directory would create duplicate navigation and unclear ownership.
2. **Separate current authority from historical evidence.**
   Active contracts and audit state remain easy to find, while the pre-baseline validation records remain available for provenance.
3. **Keep semantic judgment human-owned.**
   Scripts may generate or validate mechanical artifacts, but they do not decide scenario purpose, disposition, coverage, or verdict.
4. **Finish one skill before starting the next.**
   Each skill receives a coherent portfolio review, repair pass, execution policy, and baseline rollup rather than accumulating cross-skill partial work.
5. **Preserve historical truth.**
   Commit-qualified references keep the path that was valid at the named commit, even after the live file moves.

## Target Directory Structure

```text
skill-validation/
  README.md
  charter/
    core-contracts.md
  runner/
  scenarios/
    README.md
    <skill>/
      README.md
      <scenario>/
        README.md
        accepted/
          summary.md
          runs/
            r1/
              worksheet.md
              result.json
              final.txt
              evidence/
  archive/
    README.md
    skill-records/
      adversarial-review-loop.md
      adversarial-review.md
      concise-writing.md
      disciplined-development.md
      disciplined-research.md
      dispatching-development-subagents.md
      lean-plan-writing.md
      sweeping-stale-references.md
      writing-explicit-rationale.md
    shared-records/
      adversarial-review-loop-scenarios.md
      duplicate-red-flags-scenarios.md
      evaluation-subagents-read-only.md
```

Only files relevant to this design are shown.
Existing scenario fixtures, rubrics, prompts, and other runner artifacts remain within their current scenario packages.

## Responsibility by Level

### `skill-validation/README.md`

The validation authority map and entry point.
It explains where to find the charter, runner, active scenario catalog, accepted evidence, and archived records.
It also states which documents are normative and which are historical.

### `skill-validation/scenarios/README.md`

The suite-wide catalog and progress index.
It lists every skill, its audit state, scenario count, baseline subject, and link to the skill README.
It defines the required skill README sections so the repository does not need a separate generated manifest or template file.

### `skill-validation/scenarios/<skill>/README.md`

The manually maintained skill audit and baseline rollup.
It contains:

- the exact baseline subject: skill path, source commit, and content hash;
- the applicable charter invariants;
- a complete scenario inventory;
- each scenario's disposition and rationale;
- invariant and behavior coverage;
- overlap and identified gaps;
- the approved execution policy, once one exists;
- links to accepted scenario summaries; and
- the skill-level conclusion, including failures and limitations.

This file is the proposed manifest under the cleaner name `README.md`.
It is a semantic review artifact and is not generated.

### `skill-validation/scenarios/<skill>/<scenario>/README.md`

The scenario-package contract.
It records the scenario's purpose, provenance, intended invariant or behavior, disposition, and any task-fidelity constraints that the rubric must enforce.
It links to the accepted baseline summary when accepted evidence exists.

### `accepted/summary.md`

The human-reviewed conclusion for the current accepted baseline set.
It records:

- the baseline subject and run identities;
- provider, model, effort, and repetition policy;
- verdicts by run;
- the scenario-level conclusion;
- semantic, protocol, task-fidelity, and composition findings as applicable;
- infrastructure retries and their effect on interpretation; and
- reviewer notes and known limitations.

`summary.md` is not generated.
The runner may continue to generate worksheet skeletons and mechanical run bundles, but the reviewer completes the worksheets and writes the summary.

### `accepted/runs/<run-id>/`

The immutable-in-review evidence bundle for one accepted repetition.
Run identifiers use the stable sequence `r1`, `r2`, and so on within the accepted set.
Each run retains the generated result, final provider text, completed worksheet, and any supporting evidence.

The `accepted/` directory represents the latest reviewed baseline set.
When a new set supersedes it, the set is replaced in place and prior sets remain recoverable through Git history.

### `skill-validation/archive/`

The home for pre-baseline validation records that currently sit at the `skill-validation/` root.
The archive README explains that relocation is organizational, not a claim that the evidence is obsolete or invalid.
No new results are recorded in the archived files.

The move preserves prose and evidence.
Only links and navigation metadata needed for the new location may change.

## Historical Reference Rule

References that describe live repository authority must follow moved files to their new paths.

References qualified by a historical commit retain the path that was correct at that commit.
For example, `skill-validation/disciplined-research.md at commit 13599fb` remains unchanged even after that file moves into the archive, because changing it would falsify the provenance statement.

The implementation must classify references by meaning before editing them; a global path replacement is not acceptable.

## Scenario Dispositions

Every inventoried scenario receives exactly one disposition.

| Disposition | Meaning |
|---|---|
| `CORE` | Directly tests a required invariant or primary skill behavior and remains in the baseline portfolio. |
| `COMPOSITION` | Tests interaction with another skill or process and remains in the portfolio under one named owning skill. |
| `DIAGNOSTIC` | Intentionally isolates a narrower behavior or failure mode and remains useful as non-core evidence. |
| `MERGE` | Temporarily marks scenarios whose useful coverage should be consolidated into one retained scenario. |
| `REPAIR` | Temporarily marks a scenario that should remain but cannot be relied on until its prompt, fixture, rubric, or provenance is corrected. |
| `HISTORICAL` | Preserved for provenance but excluded from future baseline execution. |

`MERGE` and `REPAIR` are transitional.
A skill audit is not complete while either disposition remains.

Composition scenarios have one owner to prevent duplicate execution and conflicting rollups.
Non-owning skills may link to the scenario as coverage but do not count or run it independently.

## Audit Workflow

The audit proceeds one skill at a time:

1. Re-read the current skill and its charter invariants.
2. Freeze the proposed baseline subject by source commit and skill content hash.
3. Inventory every scenario currently associated with the skill.
4. Audit each prompt, rubric, fixture, and provenance record.
5. Separate semantic correctness, protocol compliance, task fidelity, and composition concerns.
6. Assign a disposition with a written rationale.
7. Map retained scenarios to invariants and behaviors; identify overlap and gaps.
8. Merge, repair, or retire scenarios until all dispositions are final.
9. Run provider-free structural validation for every retained scenario.
10. Propose the exact provider, model, effort, repetition policy, and commands for owner approval.
11. Invoke providers only after explicit approval of those exact commands.
12. Review the evidence and record scenario and skill baseline conclusions.

No scenario result is promoted merely because the runner completed.
The worksheet and summary must account for all applicable dimensions before recording a verdict.

## Audit and Baseline States

The suite index uses four skill states:

| State | Meaning |
|---|---|
| `NOT_STARTED` | The legacy inventory exists, but the skill-level audit has not begun. |
| `IN_PROGRESS` | Inventory, disposition, repair, or provider-free validation is underway. |
| `REVIEW_READY` | The portfolio and execution proposal are complete and await owner approval or review. |
| `BASELINED` | Final dispositions are recorded and all retained run-eligible scenarios have reviewed accepted evidence under the approved policy. |

A `BASELINED` skill may include passing and failing scenarios.
The state means the evidence is complete and reviewed, not that the skill passed every scenario.

## First Implementation Slice

The first implementation plan must cover one reviewable documentation change set:

1. Add the root validation authority map.
2. Add the archive explanation and create the archive categories.
3. Move the nine skill records and three shared records into the archive.
4. Sweep live references while preserving commit-qualified historical paths.
5. Update the suite catalog with the skill README contract and audit-state fields.
6. Create `skill-validation/scenarios/disciplined-research/README.md` and complete the seven-scenario audit from repository evidence.
7. Record the DR-02 scratch pilot as audit input without moving or promoting it; create accepted evidence only through a later, explicitly approved acceptance step.
8. Run provider-free validation and repository documentation checks.

The slice stops before provider execution.
Any later provider run requires the existing exact-command approval gate.

## End Goal

The current-skill baseline phase is complete when every skill in the suite is `BASELINED` and:

- every scenario has a final disposition;
- every retained scenario has a clear owner and invariant or behavior mapping;
- all retained run-eligible scenarios have provider-free validation and reviewed accepted evidence;
- every skill README states current behavior, including failures and limitations;
- suite-wide overlaps and gaps are visible; and
- the exact skill source, run configuration, and evidence are reproducible.

Only then should the rewrite branch be evaluated against the frozen portfolio or receive portfolio changes justified by newly discovered gaps.

## Non-Goals

This design does not:

- change or evaluate rewritten skills;
- compare current and rewritten skills;
- require current behavior to pass;
- authorize a provider invocation;
- automate semantic disposition, coverage, or verdict decisions;
- add a `manifest.md` generator;
- add a new structural checker without an observed recurring failure; or
- move or promote the DR-02 manual-pilot outputs from `scratch/`; or
- bulk-edit scenario content before its owning skill is audited.

## Rationale for Deferred Tooling

The runner already owns deterministic bundle creation, hashing, and worksheet scaffolding.
The proposed README and summary files capture judgments that require reading the skill, scenario, rubric, evidence, and intent together.
Generating those judgments would conceal reviewer decisions rather than make the process more reproducible.

A future checker may validate required files, links, hashes, identifiers, or state transitions if manual work demonstrates a repeated mechanical error.
It must not infer dispositions or verdicts.

## Review and Implementation Boundary

This document records the approved conversational design but remains subject to owner review as a written artifact.
No file moves, scenario edits, accepted-evidence migrations, or provider calls follow until the owner approves this spec and a separate implementation plan is written and approved.
