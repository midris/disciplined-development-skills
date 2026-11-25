# Skill testing and rewriting — active plan

Study one shipped skill at a time. Establish a fresh baseline, identify a concrete weakness or simplification worth testing, and use the observed work to decide whether to keep or change the skill. The [framework](specs/2026-09-11-model-driven-skill-testing-framework.md) defines the method. Each study protocol owns its scope, evidence links, call accounting and decisions.

## Current next action

| Skill | State | Decision record |
| --- | --- | --- |
| Concise writing (CW) | Closed. The owner adopted the rewritten description with the original body. | [CW adoption](../skill-studies/concise-writing/protocol.md#closure-and-adoption) |
| Sweeping stale references (SSR) | Closed. The owner adopted the compact, count-free skill with the tested description and complete-claim instruction. | [SSR adoption](../skill-studies/sweeping-stale-references/protocol.md#full-regression-adoption) |
| Writing explicit rationale (WER) | Review the [604-word booking-slot transfer comparison](../skill-studies/writing-explicit-rationale/protocol.md#booking-slot-transfer-comparison-for-the-604-word-variant) before selecting a candidate. | [WER protocol](../skill-studies/writing-explicit-rationale/protocol.md) |
| Remaining skills | Select the next skill with the owner after the WER decision. | [Skill inventory and composition](../ARCHITECTURE.md#composition-boundaries) |

### WER milestones

- [x] Read the shipped skill, select the cases and agree how to check what a future reader can recover. [Focused design](specs/2026-11-08-wer-focused-baseline.md)
- [x] Built the four case packages and criterion cards. The [offline dry run](../skill-studies/writing-explicit-rationale/cases/qualification.md) covers 20 constructed outputs and single-project reader payloads. Verify live reviewer access isolation during runtime preparation.
- [x] Prepare provider configs, manifests, schedule, evidence store, indexes and forecast. Verify the mounted inputs and run the offline document checks.
- [x] Resolve the provider shell failures and rerun the [installed qualification probes](../skill-studies/writing-explicit-rationale/protocol.md#qualification-on-2026-11-09).
- [x] Record approval, run one reader smoke and audit its retained evidence. The live catalog added `schedule` to the expected set.
- [x] Diagnose the catalog mismatch offline. The subscription and surrogate API-key profiles expose different catalogs.
- [x] Freeze the [subscription catalog amendment](../skill-studies/writing-explicit-rationale/protocol.md#offline-catalog-diagnosis), dispatch the approved replacement and verify its isolated reading.
- [x] Record approval for 16 application subjects. Retain and score all ten attempted slots through the [checkpoint pause](../skill-studies/writing-explicit-rationale/protocol.md#completed-application-checkpoint).
- [x] Resume the remaining six Claude application slots under owner authority and retain every outcome.
- [x] Clarify whole-output scoring and reread the four export outputs during owner review. The [WER reassessment](../skill-studies/writing-explicit-rationale/protocol.md#completed-application-checkpoint) records the revised judgment and original score.
- [x] Complete owner review and clarify materiality for added claims in scoring, collection pauses and full-evidence reconciliation.
- [x] Run the eight authorized native subjects and record the [native checkpoint](../skill-studies/writing-explicit-rationale/protocol.md#native-discovery-checkpoint).
- [x] Review the native export omission with the owner and seal all 17 authorized independent first readings.
- [x] Review the [reader checkpoint](../skill-studies/writing-explicit-rationale/protocol.md#independent-reader-checkpoint) with the owner before reconciliation.
- [x] Complete both independently scored provider-grouped reconciliations.
- [ ] Review the [reconciliation checkpoint](../skill-studies/writing-explicit-rationale/protocol.md#reconciliation-checkpoint) with the owner.
- [x] Draft a [compact WER candidate](../skill-studies/writing-explicit-rationale/protocol.md#compact-rewrite-candidate) against the preserved original.
- [x] Compare three frozen WER drafts across both providers on the four baseline cases. The [application comparison](../skill-studies/writing-explicit-rationale/protocol.md#application-comparison-results) records the shared Codex regression and four retained setup failures.
- [x] Add and offline-qualify the two [suite extension cases](../skill-studies/writing-explicit-rationale/protocol.md#suite-extension) for independent design review.
- [x] Incorporate independent case-design review, qualify version 2 of both extension cards and document the staged comparison proposal.
- [x] Complete the six-subject [repeated-review checkpoint](../skill-studies/writing-explicit-rationale/protocol.md#six-run-repeated-review-checkpoint). Review with the owner before scope-trim.
- [x] Complete the 12 authorized [scope-trim subjects](../skill-studies/writing-explicit-rationale/protocol.md#scope-trim-checkpoint). Review with the owner before dispatch-hold.
- [x] Review the catalog reader decision exercise alongside the mechanical checks and agree the [functional coverage and limits](../skill-studies/writing-explicit-rationale/protocol.md#coverage-before-the-shipped-benchmark) for the fresh shipped baseline.
- [x] Resolve the pilot case-card and decision-scoring findings and verify both cards against the shipped and control conditions offline.
- [x] Complete the [functional pilot](../skill-studies/writing-explicit-rationale/protocol.md#functional-pilot-checkpoint) and retain all eight subject and four decision-reader outcomes.
- [x] Complete the [six-reader catalog contrast](../skill-studies/writing-explicit-rationale/protocol.md#catalog-decision-contrast-checkpoint).
- [x] Review the reader contrast and select the fresh shipped application matrix for an offline freeze.
- [x] Prepare and freeze the [104-subject application benchmark](../skill-studies/writing-explicit-rationale/protocol.md#shipped-application-benchmark-freeze), scoring rules and evaluator forecast.
- [x] Complete the [shipped application benchmark](../skill-studies/writing-explicit-rationale/runs/application-benchmark-01/benchmark-report.md), including the reader decisions, cross-model judgments and Codex launch phases. Decide native discovery separately.
- [x] Review the shipped baseline, cross-model disagreements and Fable findings with the owner; retain the active judgments.
- [x] Freeze the first candidate screen and its allocation under the [incremental comparison rules](../skill-studies/writing-explicit-rationale/protocol.md#incremental-candidate-screen).

## Starting or resuming without conversation history

1. Read [CLAUDE.md](../CLAUDE.md), this plan and the active protocol above. Inspect the working tree for existing work.
2. For a new skill, follow the [per-skill plan skeleton](../skill-studies/README.md#per-skill-plan-skeleton). Read the shipped skill and its actual dependencies, identify its users and verify which instructions each subject will receive.
3. For an existing study, resolve the first open milestone against its protocol, frozen input identities, attempt index and latest assessment. Resume from the last verified state. The [runner guide](../skill-validation/runner/README.md#study-documents) owns command syntax and supported representations.

## Limits and information boundaries

Accepted outer limits: 1041 subject, 90 evaluator, 4 authoring and 4 retry invocations for the CW/SSR program. The 20-hour active-work figure was a planning guideline. The [combined accounting record](../skill-studies/concise-writing/protocol.md#storage-and-accounting) retains actual spending, estimates and variance. WER needs its own recorded allocation. Unused capacity from earlier studies carries no dispatch authority.

Keep rubrics, expected facts, assessor notes and raw captures outside the subject's accessible inputs. Describe isolation from actual runtime evidence. New studies use fresh baselines. Declare any held-out transfer claim and its stronger isolation separately. [Framework](specs/2026-09-11-model-driven-skill-testing-framework.md#4-pilot-and-freeze-the-experiment-plan)

## Document tooling: after baseline collection

The document tools developed during SSR now support preparation through assessment. Use them from the start of every new study. Approved retry accounting and offline Claude smoke tests were fixed in `45c84e09`. [Runner operations](../skill-validation/runner/README.md#mechanical-study-operations)

The [previous execution checklist](https://github.com/midris/disciplined-development-skills/blob/45c84e090599100f6f1a4d1df4d9352d555a7c4f/plans/2026-09-11-model-driven-skill-testing.md) preserves the research, scope changes, tooling decisions and checkpoints for CW and SSR. Their protocols and assessments remain at their original paths.
