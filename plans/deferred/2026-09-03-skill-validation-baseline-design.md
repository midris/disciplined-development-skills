# Skill Validation Baseline Organization Design

> **Abandoned testing process — historical reference only (2026-09-11).**
> Testing-framework instructions, approvals and pending work below are no longer current. Follow the [new framework spec](../specs/2026-09-11-model-driven-skill-testing-framework.md) and [new testing plan](../2026-09-11-model-driven-skill-testing.md).
> The original text is preserved as history; this notice does not retire existing runner tooling or core skills.


**Status:** Deferred on 2026-09-03 after the review loop exposed an unresolved end-to-end authority and evidence lifecycle. This document remains design input, not implementation authority. The owner authorized only the legacy-record archive and root validation index before selecting the next incremental baseline step.

## Purpose

Establish a consistent, catalog-by-catalog process for auditing the existing validation portfolio and recording reproducible baselines for the skills currently on `main`.

The baseline is descriptive, not aspirational.
A judgeable failure is valid baseline evidence when it accurately records current behavior.
Rewrite evaluation begins only after the current-skill baseline campaign is complete.

## Authority and Scope

This design extends the testing methodology in [`plans/completed/specs/2026-09-02-skill-testing-methodology-design.md`](../completed/specs/2026-09-02-skill-testing-methodology-design.md).

The existing methodology remains authoritative for:

- provider approval gates;
- mechanical runner responsibilities;
- semantic review responsibilities;
- run identity and provenance;
- infrastructure retry classification; and
- accepted-result replacement through Git history.

This design becomes authoritative for validation-record organization, portfolio classification, catalog-level baseline rollups, and accepted baseline-set layout after implementation.
Its accepted baseline-set layout supersedes the single-run `accepted/` layout in the earlier methodology.

The initial implementation sequence includes only repository organization and the `disciplined-research` audit.
It does not authorize provider invocations.
It changes Markdown documentation only; runner code, skills, scenario configurations, prompts, rubrics, and executable fixtures remain unchanged.

## Resolution of Earlier Open Decisions

The earlier methodology listed five decisions as open when it was completed.
This design resolves or defers them as follows:

| Earlier decision | Resolution |
|---|---|
| Exact provider, model, effort, and invocation for the DR-02 pilot | Resolved operationally on 2026-09-03 under a separately approved Codex `gpt-5.6-sol` high-effort command. The pilot remains scratch-only and does not authorize future commands. |
| Review required before accepted replacement | Resolved below: the orchestrator completes the candidate set in scratch, and the owner explicitly approves that exact set before one atomic accepted-record replacement. |
| When repetitions, comparison arms, or advisory scorers are justified | Current-skill repetitions are chosen in each catalog's execution policy and require exact-command approval. Comparison arms and advisory scorers remain deferred until current baselines are complete. |
| When execution or draft scoring may move to a test subagent | Deferred until repeated manual use demonstrates a stable delegation boundary. |
| Skill- and suite-level rollup | Resolved below through catalog READMEs, the suite index, and descriptive state rather than numeric aggregation. |

## Design Principles

1. **Colocate the audit with the scenarios.**
   The scenario hierarchy is already the natural unit of validation work, so a second per-skill hierarchy under a top-level `baselines/` directory would create duplicate navigation and unclear ownership.
2. **Separate current authority from historical evidence.**
   Active contracts and audit state remain easy to find, while the pre-baseline validation records remain available for provenance.
3. **Keep semantic judgment human-owned.**
   Scripts may generate or validate mechanical artifacts, but they do not decide scenario purpose, portfolio classification, coverage, or verdict.
4. **Finish one catalog before starting the next.**
   Each catalog receives a coherent portfolio review, repair pass, execution policy, and baseline rollup rather than accumulating cross-catalog partial work.
5. **Preserve historical truth.**
   Commit-qualified references keep the path that was valid at the named commit, even after the live file moves.

## Baseline Campaign Anchor

Before the first catalog audit, resolve `main` once to a full commit ID and record it in the suite index as the baseline campaign anchor.
Every catalog baseline subject and provider run in the campaign uses skill bytes from that commit.
Documentation-only audit branches may advance independently, but the supplied skill hashes must match the campaign anchor before every run.

Later movement of `main` does not change the campaign anchor.
Replacing the anchor requires explicit owner approval and starts a replacement campaign; prior evidence remains historical but does not satisfy the replacement campaign.
One campaign-wide anchor is required because per-catalog commits would make cross-catalog and `skill-discovery` evidence incomparable.

The scratch-only [DR-02 pilot outcome](../completed/specs/2026-09-02-skill-testing-methodology-design.md#dr-02-pilot-outcome) predates the campaign anchor and informs methodology only.
It is not campaign baseline evidence.

## Target Directory Structure

```text
skill-validation/
  README.md
  charter/
    core-contracts.md
  runner/
  scenarios/
    README.md
    <catalog>/
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
It lists every catalog, its kind, audit state, scenario count, baseline subject, and README link.
It defines the required catalog README sections so the repository does not need a separate generated manifest or template file.

The suite has two catalog kinds:

- `SKILL` for each of the nine directories under `skills/`; and
- `SUITE_COMPOSITION` for `skill-discovery`, whose scenarios test routing and composition across the nine-skill bundle rather than a nonexistent `skill-discovery` skill.

### `skill-validation/scenarios/<catalog>/README.md`

The manually maintained catalog audit and baseline rollup.
It contains:

- the catalog kind;
- the exact baseline subject;
- the applicable charter invariants;
- a complete scenario inventory;
- each scenario's portfolio classification, owner, and rationale;
- invariant and behavior coverage;
- overlap and identified gaps;
- the approved execution policy, once one exists;
- links to accepted scenario summaries; and
- the catalog-level conclusion, including failures and limitations.

A `SKILL` catalog records the campaign anchor, one skill path, and that file's anchored content hash.
The `SUITE_COMPOSITION` catalog records the same anchor plus all nine skill paths and anchored hashes.

This file is the proposed manifest under the cleaner name `README.md`.
It is a semantic review artifact and is not generated.

### `skill-validation/scenarios/<catalog>/<scenario>/README.md`

The scenario-package contract.
It records the scenario's purpose, provenance, intended invariant or behavior, portfolio classification, owning catalog, and any task-fidelity constraints that the rubric must enforce.
It links to the accepted baseline summary when accepted evidence exists.

Physical catalog location identifies the owner unless the audit explicitly rehomes the scenario.
Non-owning catalogs link to composition coverage without duplicating its execution or rollup.

### `accepted/summary.md`

The human-reviewed conclusion for the most recently accepted baseline set.
It records:

- the baseline subject and run identities;
- provider, model, effort, and repetition policy;
- the ordered run verdicts and run-set characterization;
- semantic, protocol, task-fidelity, and composition findings as applicable;
- infrastructure retries and their effect on interpretation;
- whether the set is current or stale, including the reason and date when stale; and
- reviewer notes and known limitations.

`summary.md` is not generated.
The runner may continue to generate worksheet skeletons and mechanical run bundles, but the reviewer completes the worksheets and writes the summary.

### `accepted/runs/<repetition-id>/`

The immutable-in-review evidence bundle for one accepted repetition.
Repetition identifiers use the stable sequence `r1`, `r2`, and so on within the accepted set.
Each repetition retains the generated result, final provider text, completed worksheet, and any supporting evidence.
The summary maps every repetition identifier to the runner's globally unique run ID.

The `accepted/` directory represents the latest reviewed baseline set, whether current or subsequently marked stale.
When a new set supersedes it, the set is replaced in place and prior sets remain recoverable through Git history.

## Accepted Baseline-Set Lifecycle

All attempts, completed worksheets, and the draft summary remain in scratch until review finishes.
Only judgeable `PASS` and `FAIL` runs may enter an accepted set.
Infrastructure failures, `SCENARIO_INVALID` results, and row-level `NOT_JUDGEABLE` results remain scratch-only; the summary may describe retries without copying their bundles.

Every repetition in one candidate or accepted set must share this stable comparison key:

- campaign anchor and supplied skill hashes;
- scenario ID and checked-in prompt-template, rubric, execution-configuration, fixture, and dependency hashes;
- provider, model, and effort; and
- runner result-schema version.

Run identity, timestamps, duration, run-owned absolute paths substituted into the rendered prompt, provider stdout and stderr, telemetry, response, and produced evidence may differ between repetitions.
The reviewer must confirm that rendered-prompt differences are limited to declared run-root substitution; any other rendered-prompt difference makes the run ineligible for that candidate set.

A run whose stable comparison key differs starts a separate candidate set and cannot be characterized with the existing repetitions.
Creating or reviewing such a candidate has no effect on the current accepted set.
An accepted set becomes stale only after an authoritative, owner-approved change to its campaign anchor, checked-in scenario or evaluation inputs, approved execution policy, or runner result contract.
When that happens, its summary records the invalidation reason and date, the catalog returns to `IN_PROGRESS`, and the existing files remain clearly labeled stale evidence until an approved replacement is promoted atomically.
Stale evidence does not satisfy the current campaign, but Git history continues to preserve it for its original inputs.

The orchestrator presents the complete candidate tree, its run IDs, and its file hashes to the owner.
The owner must explicitly approve that exact candidate set before any `accepted/` write.
Promotion replaces the whole accepted set in one repository change; partial replacement is invalid.

The summary preserves every per-run verdict and assigns only one run-set characterization:

| Characterization | Meaning |
|---|---|
| `SINGLE` | The approved policy required one judgeable run. |
| `CONSISTENT` | Two or more judgeable runs have the same verdict. |
| `MIXED` | Judgeable runs contain both `PASS` and `FAIL`. |

The summary does not synthesize a new PASS or FAIL verdict across repetitions.
A mixed set remains valid descriptive baseline evidence when it fulfills the approved repetition policy.

### `skill-validation/archive/`

The home for pre-baseline validation records that currently sit at the `skill-validation/` root.
The archive README explains that relocation is organizational, not a claim that the evidence is obsolete or invalid.
Until an approved catalog replaces a legacy skill record, that archived record remains the update target required by `CLAUDE.md`; after cutover it becomes read-only historical evidence.

The move preserves prose and evidence.
Only links and navigation metadata needed for the new location may change.

## Historical Reference Rule

References that describe live repository authority must follow moved files to their new paths.

References qualified by a historical commit retain the displayed path that was correct at that commit.
For example, `skill-validation/disciplined-research.md at commit 13599fb` remains unchanged even after that file moves into the archive, because changing it would falsify the provenance statement.

Unqualified scenario provenance is normalized only during its owning catalog audit, not during the archive move.
When repository evidence establishes the source commit, the audit preserves the historical path text, adds the source commit, and links separately to the record's current archive location.
It must not describe the archive path as existing at a commit where the record still had its original path.
When the source commit cannot be established, the audit preserves the statement and assigns `REPAIR` rather than inventing provenance.

Markdown link destinations are current navigation rather than historical claims, so links to moved records retarget the archive copy even when their displayed historical path remains unchanged.
Completed plans and other historical documents retain historical path text but receive working archive link destinations.
Current navigation, authority, and backlog references change both their text and destination to the archive path.
The implementation must classify references by meaning before editing them; a global path replacement is not acceptable.

## Portfolio Classifications

Every inventoried scenario receives exactly one portfolio classification.

| Classification | Meaning |
|---|---|
| `CORE` | Directly tests a required invariant or primary catalog behavior and remains in the baseline portfolio. |
| `COMPOSITION` | Tests interaction with another skill or process and remains in the portfolio under one named owning catalog. |
| `DIAGNOSTIC` | Intentionally isolates a narrower behavior or failure mode and remains useful as non-core evidence. |
| `MERGE` | Temporarily marks scenarios whose useful coverage should be consolidated into one retained scenario. |
| `REPAIR` | Temporarily marks a scenario that should remain but cannot be relied on until its prompt, fixture, rubric, or provenance is corrected. |
| `HISTORICAL` | Preserved for provenance but excluded from future baseline execution. |

`MERGE` and `REPAIR` are transitional.
A catalog audit is not complete while either classification remains.
A merged-away scenario finishes as `HISTORICAL` and links to the retained scenario that absorbed its coverage.
A repaired scenario is reassigned one of the four final classifications after provider-free validation.

Composition scenarios have one owner to prevent duplicate execution and conflicting rollups.
Non-owning catalogs may link to the scenario as coverage but do not count or run it independently.

Portfolio classification is separate from the existing run verdict and evidence disposition:

- portfolio classification: `CORE`, `COMPOSITION`, `DIAGNOSTIC`, `MERGE`, `REPAIR`, or `HISTORICAL`;
- run verdict: `PASS`, `FAIL`, `SCENARIO_INVALID`, or `INFRA_RETRY`; and
- evidence disposition: accepted or scratch-only.

Every final active classification—`CORE`, `COMPOSITION`, or `DIAGNOSTIC`—requires accepted baseline evidence under its approved execution policy.
`HISTORICAL` scenarios are not executed.

## Audit Workflow

The audit proceeds one catalog at a time:

1. Re-read the current skill or skill bundle and its charter invariants.
2. Read the campaign anchor and freeze the applicable anchored skill paths and hashes.
3. Inventory every scenario currently associated with the catalog.
4. Audit each prompt, rubric, fixture, and provenance record.
5. Separate semantic correctness, protocol compliance, task fidelity, and composition concerns.
6. Assign a portfolio classification, owning catalog, and written rationale.
7. Map retained scenarios to invariants and behaviors; identify overlap and gaps.
8. Merge, repair, or retire scenarios until all classifications are final.
9. Run provider-free structural validation for every retained scenario.
10. Propose the exact provider, model, effort, repetition policy, and commands for owner approval.
11. Invoke providers only after explicit approval of those exact commands.
12. Review the evidence and record scenario and catalog baseline conclusions.

No scenario result is promoted merely because the runner completed.
The worksheet and summary must account for all applicable dimensions before recording a verdict.

## Audit and Baseline States

The suite index uses four catalog states:

| State | Meaning |
|---|---|
| `NOT_STARTED` | The legacy inventory exists, but the catalog-level audit has not begun. |
| `IN_PROGRESS` | Inventory, classification, repair, provider-free validation, approved provider execution, evidence review, or candidate assembly is underway. |
| `REVIEW_READY` | The portfolio and current review packet—execution proposal or completed baseline rollup—await an owner decision. |
| `BASELINED` | Final classifications are recorded and every active scenario has reviewed accepted evidence fulfilling its approved policy. |

A `BASELINED` catalog may include passing, failing, and mixed scenario sets.
The state means the evidence is complete and reviewed, not that every scenario passed.
The normal transition is `NOT_STARTED` to `IN_PROGRESS` for audit and repair, then `REVIEW_READY` for the execution proposal, back to `IN_PROGRESS` for approved runs, evidence review, and candidate assembly, then `REVIEW_READY` for the completed rollup, and finally `BASELINED` after owner approval.
An invalidated accepted set returns a `BASELINED` catalog to `IN_PROGRESS` as defined above.
After all required scenario sets are accepted, the orchestrator presents the completed catalog README and suite-index transition to the owner.
The owner must explicitly approve the catalog conclusion before its state changes to `BASELINED`.

## Initial Implementation Sequence

The first implementation plan contains two documentation-only merge boundaries.

### Boundary 1: Validation record organization

1. Add the root validation authority map.
2. Add the archive explanation and create the archive categories.
3. Move the nine skill records and three shared records into the archive.
4. Retarget current navigation and Markdown link destinations while preserving historical path text; defer scenario-provenance normalization to each catalog audit.
5. Resolve and record the single baseline campaign anchor.
6. Update the suite catalog with catalog kinds, the catalog README contract, and audit-state fields.
7. Run repository documentation checks.

### Boundary 2: `disciplined-research` portfolio audit

1. Create `skill-validation/scenarios/disciplined-research/README.md` and audit all seven scenario packages from repository evidence.
2. Add portfolio classification, ownership, coverage, and audit status to the seven scenario READMEs.
3. Use the durable [DR-02 pilot outcome](../completed/specs/2026-09-02-skill-testing-methodology-design.md#dr-02-pilot-outcome) as audit input without moving or promoting the raw scratch artifacts; surviving scratch may corroborate the record but is not required.
4. Run provider-free validation without changing scenario inputs.

This boundary ends at `REVIEW_READY` only if every classification is final and the execution proposal is complete.
If the audit finds `MERGE` or `REPAIR` work, it ends at `IN_PROGRESS` and records the exact follow-up instead of expanding scope.

Any scenario merge or repair is a later, separately approved boundary.
It may change scenario documentation or test inputs, but it does not change runner or skill code unless a new design explicitly authorizes that work.

The initial plan stops before scenario repair and provider execution.
Any later provider run requires the existing exact-command approval gate.

## End Goal

The current-skill baseline phase is complete when all nine `SKILL` catalogs and the `SUITE_COMPOSITION` catalog are `BASELINED` and:

- every scenario has a final portfolio classification;
- every retained scenario has a clear owner and invariant or behavior mapping;
- every active scenario has provider-free validation and reviewed accepted evidence fulfilling its approved repetition policy;
- every catalog README states current behavior, including failures and limitations;
- suite-wide overlaps and gaps are visible; and
- the exact skill source, run configuration, and evidence are reproducible.

Only then should the rewrite branch be evaluated against the frozen portfolio or receive portfolio changes justified by newly discovered gaps.

## Non-Goals

This design does not:

- change or evaluate rewritten skills;
- compare current and rewritten skills;
- require current behavior to pass;
- authorize a provider invocation;
- automate semantic classification, coverage, or verdict decisions;
- add a `manifest.md` generator;
- add a new structural checker without an observed recurring failure;
- move or promote the DR-02 manual-pilot outputs from `scratch/`;
- change runner code, skill content, scenario configurations, prompts, rubrics, or executable fixtures in the initial implementation plan; or
- bulk-edit scenario content before its owning skill is audited.

## Rationale for Deferred Tooling

The runner already owns deterministic bundle creation, hashing, and worksheet scaffolding.
The proposed README and summary files capture judgments that require reading the skill, scenario, rubric, evidence, and intent together.
Generating those judgments would conceal reviewer decisions rather than make the process more reproducible.

A future checker may validate required files, links, hashes, identifiers, or state transitions if manual work demonstrates a repeated mechanical error.
It must not infer portfolio classifications, run verdicts, or evidence dispositions.

## Review and Implementation Boundary

This document records the approved conversational design but remains subject to owner review as a written artifact.
No file moves, scenario edits, accepted-evidence migrations, or provider calls follow until the owner approves this spec and a separate implementation plan is written and approved.
