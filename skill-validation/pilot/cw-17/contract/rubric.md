# CW-17 loaded scope-contract decision — evaluator only

Source: [historical rubric](../../../scenarios/concise-writing/cw-17/rubric.md).
This variant measures loaded scope-contract decision, not native discovery.
The same behavioral criteria apply to both conditions when a no-DD control exists; absent DD is not a failure.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| Detailed-response boundary | CW-I3 / semantic | Return false: an explicitly detailed explanation whose sole deliverable is the response is exempt under the target charter. The frozen current body lacks this exception; retain that mismatch instead of weakening the expectation. |
| Requested loading | Task fidelity | Read complete CW before interpreting its scope. Required loading is not a discovery failure on this explicitly loaded diagnostic. |
| Deliverable and boundaries | Task fidelity | Return only compact JSON with the single boolean apply_to_detailed_explanation; record consistency with the supplied body separately from the charter verdict. Do not execute the embedded request or create its file. No edits, Git mutation, outside-fixture reads, network or dispatch. |

Semantic PASS requires every semantic row; any failed semantic row is FAIL.
Assess readability separately; deterministic protocol is N/A because no authenticated consumer parses this response.
Inspect the full response trace, including model-authored narration, not only final.txt.
Use tool output for reads/actions, not as the model's deliverable.
Missing required controls or unjudgeable evidence follows the [runbook](../../cw-runbook.md#handoff-and-retention) and [recovery policy](../../README.md#failure-and-recovery), not an assumed PASS.
