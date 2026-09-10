# CW-05 loaded prose behavior — evaluator only

Source: [historical rubric](../../../scenarios/concise-writing/cw-05/rubric.md).
This variant measures loaded prose behavior, not native discovery.
The same behavioral criteria apply to both conditions when a no-DD control exists; absent DD is not a failure.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| Preserve authoritative facts | CW-I1 / semantic | Nightly generation at 02:00 UTC; completed orders from the previous UTC day; 30-day retention. |
| Remove unsupported elaboration | CW-I2 / semantic | Remove both immediate-download/data-loss advice and before-business-hours/performance advice. |
| Add no claim | CW-I1 / semantic | No new claim beyond authoritative notes. |
| Requested loading | Task fidelity | Current-DD visibly reads the full CW body before the task; no-DD is N/A. |
| Deliverable and boundaries | Task fidelity | Return only the requested revision, without procedural narration; no edits, Git mutation, outside-fixture reads, network or dispatch. |

Semantic PASS requires every semantic row; any failed semantic row is FAIL.
Assess readability separately; deterministic protocol is N/A because no authenticated consumer parses this response.
Inspect the full response trace, including model-authored narration, not only final.txt.
Use tool output for reads/actions, not as the model's deliverable.
Missing required controls or unjudgeable evidence follows the [runbook](../../cw-runbook.md#handoff-and-retention) and [recovery policy](../../README.md#failure-and-recovery), not an assumed PASS.
