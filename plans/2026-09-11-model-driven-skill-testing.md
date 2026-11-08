# Skill testing and rewriting — active plan

Study one shipped skill at a time. Establish a fresh baseline, identify a concrete weakness or simplification worth testing, and use the observed work to decide whether to keep or change the skill. The [framework](specs/2026-09-11-model-driven-skill-testing-framework.md) defines the method. Each study protocol owns its scope, evidence links, call accounting and decisions.

## Current next action

| Skill | State | Decision record |
| --- | --- | --- |
| Concise writing (CW) | Closed. The owner adopted the rewritten description with the original body. | [CW adoption](../skill-studies/concise-writing/protocol.md#closure-and-adoption) |
| Sweeping stale references (SSR) | Closed. The owner adopted the compact, count-free skill with the tested description and complete-claim instruction. | [SSR adoption](../skill-studies/sweeping-stale-references/protocol.md#full-regression-adoption) |
| Writing explicit rationale (WER) | Selected. Four cases and the reader-first review are designed. Next comes offline fixture and scoring preparation. | [WER protocol](../skill-studies/writing-explicit-rationale/protocol.md) |
| Remaining skills | Select the next skill with the owner after the WER decision. | [Skill inventory and composition](../ARCHITECTURE.md#composition-boundaries) |

### WER milestones

- [x] Read the shipped skill, select the cases and agree how to check what a future reader can recover. [Focused design](specs/2026-11-08-wer-focused-baseline.md)
- [ ] Build the four case packages and criterion cards. Exercise good, incomplete and misleading outputs locally. Confirm the reader-first evidence boundary works.
- [ ] Prepare provider configs, manifests, schedule and forecast. Check preparation, freeze inputs and check collection readiness. Record the approved allocation before dispatch.
- [ ] Run the authorized baseline stages. Retain every attempt, score complete artifacts, reconcile output reviews and record the decision the evidence supports.
- [ ] If a change is warranted, compare it against the preserved original, regression-test the exact proposed version, then record the owner's decision. Close the study and select the next skill.

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
