# Running a skill study

Use the [active plan](../plans/2026-09-11-model-driven-skill-testing.md#current-next-action) to find the current skill and next milestone. Use the [framework](../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#cw-testing-model) for the study design defaults established through CW and SSR.

## Per-skill plan skeleton

Use these milestones in the active plan as each skill is selected. Keep study-specific decisions and evidence in `skill-studies/<skill>/protocol.md`. The existing protocol template has sections for the contract, coverage map, assessment, scope, accounting and decision. Generate it once, then fill it as the work progresses.

| Milestone | What the operator supplies or decides | Mechanics to reuse |
| --- | --- | --- |
| 1. Establish the contract | Read the shipped skill and relevant companions. Identify its user, the outcome that matters, plausible failures and when the skill should stay quiet. Agree what the study could establish. | Create the study directory. Use `skilltest docs new protocol`. Record source revision and preserve the original bytes before collection. |
| 2. Build the suite | Select cases that distinguish useful work from plausible mistakes. Supply ordinary prompts, runnable fixtures, withheld facts, acceptable variants, limits and evidence for each criterion. Challenge the checks with good and broken examples. | Use `docs new case`, existing fixture/config formats and ordinary project tests. Write a case-specific replay only when existing checks cannot establish an observable fact. |
| 3. Freeze the comparison | Choose providers, conditions, repetitions, early stops, review scope, storage and budget. For contribution, pair explicit loading with a no-target control. Test discovery separately with native availability. | Use `docs new manifest` and `docs manifest` for identities and paired inputs. Check preparation, commit reviewed inputs, freeze at that revision, then check collection. Verify changed runtime assumptions and record authorization. |
| 4. Establish a fresh baseline | Run the authorized slots in clean contexts. Inspect complete artifacts, diffs, traces and relevant replays. Score under the frozen policy with reasons for passes, failures and insufficient evidence. | `skilltest run` captures one subject. `docs retain` verifies and registers a stopped initial attempt. Use the index and result formats for provenance, exclusions and separately approved retries. |
| 5. Compare and decide | Review complete outputs across conditions. Reconcile independent cross-model output review at the decision boundary. Identify the failure a change would remedy, or record why the shipped version should be retained. | Use `docs tables` for coverage and arithmetic, complete the assessment and run `docs check --ready-for assessment` on the selected protocol batch. |
| 6. Test the revision and close | When a rewrite is warranted, freeze the candidate, repeat affected cases and relevant regressions, and check the exact final body and description. Record trade-offs, limits and the owner's decision. | Reuse the same cases, commands, manifests and result formats with new version identities. On adoption verify that shipped bytes match the tested candidate. |

**Tooling rule.** A human or agent writes the criteria and judges the work. A command can prove that both exporter invocations returned the expected bytes or that a reviewer opened a file before recording a verdict. The assessor decides whether a preserved explanation is accurate and useful. When a recurring mechanical step lacks support, demonstrate the gap on a real record, extend the existing tool and test it offline. A new skill usually needs new cases and judgments.

The [runner guide](../skill-validation/runner/README.md#study-documents) gives the exact commands and freeze order. The [format contracts](formats/README.md) define the six generated documents, including which records are created before collection and which require observed results. Keep raw evidence in the protocol’s external store.

## Studies

- [WER](writing-explicit-rationale/protocol.md) — current preparation and proposed scope.
- [CW](concise-writing/protocol.md#closure-and-adoption) — completed study and decision.
- [SSR](sweeping-stale-references/protocol.md#full-regression-adoption) — completed study and decision.
