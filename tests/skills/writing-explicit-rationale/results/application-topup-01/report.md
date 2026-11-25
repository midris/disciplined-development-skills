# Shipped WER application benchmark after five scheduled repetitions

Both providers completed all 36 additional subjects. The [schedule](schedule.json) used the existing helper rename, scope trim and dispatch hold tasks and the same shipped WER and no-skill control inputs as the [original benchmark](../application-benchmark-01/benchmark-report.md). Each provider and condition now has five valid outputs on each of these three scenarios.

## Additional repetitions 3–5

Each cell counts the outputs that met every functional criterion over valid outputs. The [Codex assessment](codex-assessment.md), [Claude assessment](claude-assessment.md) and [individual reconciliations](assessment.json) cover all 36 attempts, including misses.

| Scenario | Codex shipped | Codex control | Claude shipped | Claude control |
|---|---:|---:|---:|---:|
| Helper rename | 3/3 | 3/3 | 3/3 | 3/3 |
| Scope trim | 3/3 | 2/3 | 3/3 | 3/3 |
| Dispatch hold | 3/3 | 3/3 | 3/3 | 3/3 |

## Combined benchmark

The following counts include the original 104 attempts and these 36 additional subjects. Of 140 scheduled attempts, 138 had valid setups. Both exclusions were in the original Codex catalog case, one per arm. All 36 new attempts had valid setups. Each subject received its own session. The attempt indices link the retained bundles and their inventories.

| Scenario | Codex shipped | Codex control | Claude shipped | Claude control |
|---|---:|---:|---:|---:|
| Export deferral | 5/5 | 4/5 | 5/5 | 5/5 |
| Quota grace | 5/5 | 0/5 | 5/5 | 0/5 |
| Repeated review | 4/5 | 0/5 | 5/5 | 0/5 |
| Catalog review | 4/4 | 2/4 | 5/5 | 3/5 |
| Helper rename | 5/5 | 5/5 | 5/5 | 5/5 |
| Scope trim | 4/5 | 3/5 | 5/5 | 5/5 |
| Dispatch hold | 5/5 | 5/5 | 5/5 | 5/5 |

| Dimension across all seven scenarios | Shipped WER | Control |
|---|---:|---:|
| All functional criteria | 67/69 | 42/69 |
| Task correctness (T1) | 68/69 | 66/69 |
| Rationale and restraint (all applicable R criteria) | 68/69 | 44/69 |

## Interpretation

The new scope-trim miss was Codex control repetition 5 (slot 29). Its plan put daily reconciliation and alerts under “Monday launch,” and its handoff referred to “Monday’s launch commitments.” The original request dated the handoff only. A team using the plan could reasonably schedule a rollout for Monday. The same output retained the reason both weekly features were deferred, Finance’s close-rule decision and Support’s possible manual comparison. It missed task correctness and met the rationale criterion. Two earlier Codex outputs made the same scheduling error, one in each arm. All 20 scope-trim plans conveyed the consequential rationale.

All 12 additional rename projects produced the same project files. Each preserved the existing explanation for clamping negative billing corrections, changed both callers, and passed the original tests. The final handoffs varied in detail without adding permanent commentary to the code.

In dispatch hold, a short spec and matching status names in both functions let a maintainer recover why a held parcel stays off a new trip and why a loaded parcel stays assigned for redirection. Other projects used a common definition or repeated the explanation locally. Some copies add upkeep, and some specs attribute the new queue status to the carrier, although the input establishes carrier provenance only for the manual hold. Neither detail changed a required dispatch action.

The two restraint cases provide a baseline for detecting regressions in a shorter candidate. Both arms also preserved the Finance rationale in scope trim. The largest observed shipped-control separation still comes from quota grace and repeated review, where an implementation can pass its behavior checks while leaving a maintainer to guess the reason for an exception.

## Scope of the comparison

The first Codex repetition in each of the six topped-up cells ran with account apps discoverable. The other four used the apps-disabled boundary. All new subjects passed the exposure audit. Claude used the same settings throughout. The active Codex assessor recorded [project-only readings](project-only.json) before reconciling each against the original inputs and handoff, with offline behavior replays for rename and dispatch. The original benchmark's 18 independent decision readers and 14 cross-model reviews cover earlier outputs only. This top-up measures explicit application on known development fixtures. Native selection and transfer to new tasks require separate evidence.
