# CW-03 loaded prose behavior — evaluator only

Source: [historical rubric](../../../scenarios/concise-writing/cw-03/rubric.md).
This variant measures loaded prose behavior, not native discovery.
The same behavioral criteria apply to both conditions when a no-DD control exists; absent DD is not a failure.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| One definition | CW-I1/I2 / semantic | Define an access link as a single-use URL expiring after 30 minutes exactly once. |
| Preserve use and recovery | CW-I1 / semantic | Send only to the intended recipient; after expiration an administrator must issue a new link. |
| No unsupported facts | CW-I1 / semantic | No added fact. |
| Requested loading | Task fidelity | Current-DD visibly reads the full CW body before the task; no-DD is N/A. |
| Deliverable and boundaries | Task fidelity | Return only the requested revision, without procedural narration; no edits, Git mutation, outside-fixture reads, network or dispatch. |

Semantic PASS requires every semantic row; any failed semantic row is FAIL.
Assess readability separately; deterministic protocol is N/A because no authenticated consumer parses this response.
Inspect the full response trace, including model-authored narration, not only final.txt.
Use tool output for reads/actions, not as the model's deliverable.
Missing required controls or unjudgeable evidence follows the [runbook](../../cw-runbook.md#handoff-and-retention) and [recovery policy](../../README.md#failure-and-recovery), not an assumed PASS.
