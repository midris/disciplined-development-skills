# CW-02 loaded prose behavior — evaluator only

Source: [historical rubric](../../../scenarios/concise-writing/cw-02/rubric.md).
This variant measures loaded prose behavior, not native discovery.
The same behavioral criteria apply to both conditions when a no-DD control exists; absent DD is not a failure.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| Remove duplication | CW-I2 / semantic | Remove the meta opener and one duplicate three-attempt statement. |
| Preserve retry scope and consequence | CW-I1 / semantic | At most three attempts per delivery, not per endpoint; one failing delivery must not exhaust later deliveries' retries. |
| Preserve rationale and navigation | CW-I1 / semantic | Retries stay synchronous because downstream acknowledgements must preserve delivery order; retain the Delivery ordering navigation aid before changes. |
| Preserve failure boundary | CW-I1 / semantic | Mark failed only after the third unsuccessful attempt; changing the count, success/failure predicate or ordering fails. |
| Requested loading | Task fidelity | Current-DD visibly reads the full CW body before the task; no-DD is N/A. |
| Deliverable and boundaries | Task fidelity | Return only the requested revision, without procedural narration; no edits, Git mutation, outside-fixture reads, network or dispatch. |

Semantic PASS requires every semantic row; any failed semantic row is FAIL.
Assess readability separately; deterministic protocol is N/A because no authenticated consumer parses this response.
Inspect the full response trace, including model-authored narration, not only final.txt.
Use tool output for reads/actions, not as the model's deliverable.
Missing required controls or unjudgeable evidence follows the [runbook](../../cw-runbook.md#handoff-and-retention) and [recovery policy](../../README.md#failure-and-recovery), not an assumed PASS.
