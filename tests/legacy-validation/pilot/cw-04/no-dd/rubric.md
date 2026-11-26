# CW-04 loaded prose behavior — evaluator only

Source: [historical rubric](../../../scenarios/concise-writing/cw-04/rubric.md).
This variant measures loaded prose behavior, not native discovery.
The same behavioral criteria apply to both conditions when a no-DD control exists; absent DD is not a failure.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| Collapse padding structure | CW-I2 / semantic | One compact account without the four one-sentence subheadings; removing substantive information to achieve this fails. |
| Preserve time boundaries | CW-I1 / semantic | Expiration after 20 minutes of inactivity; warning exactly two minutes before expiration. |
| Preserve inputs and recovery | CW-I1 / semantic | Mouse, keyboard and touch reset inactivity; expired sessions require signing in again. |
| Requested loading | Task fidelity | Current-DD visibly reads the full CW body before the task; no-DD is N/A. |
| Deliverable and boundaries | Task fidelity | Return one compact Session behavior section, only the revised text; no edits, Git mutation, outside-fixture reads, network or dispatch. |

Semantic PASS requires every semantic row; any failed semantic row is FAIL.
Assess readability separately; deterministic protocol is N/A because no authenticated consumer parses this response.
Inspect the full response trace, including model-authored narration, not only final.txt.
Use tool output for reads/actions, not as the model's deliverable.
Missing required controls or unjudgeable evidence follows the [runbook](../../cw-runbook.md#handoff-and-retention) and [recovery policy](../../README.md#failure-and-recovery), not an assumed PASS.
