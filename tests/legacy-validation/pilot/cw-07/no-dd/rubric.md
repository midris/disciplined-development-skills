# CW-07 direct-load transport with prose checks — evaluator only

Source: [historical rubric](../../../scenarios/concise-writing/cw-07/rubric.md).
This variant measures direct-load transport with prose checks, not native discovery.
The same behavioral criteria apply to both conditions when a no-DD control exists; absent DD is not a failure.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| Standalone task completion | Transport / semantic | Return a revision, not BLOCKED or a requirement for unavailable project state/procedures. |
| Preserve facts once | CW-I1/I2 / semantic | CSV report downloads preserve current filters and use UTF-8; PDF downloads unchanged. Each fact once; remove the opener and repeated filter/PDF statements. |
| Add no fact | CW-I1 / semantic | No unsupported fact or advice. |
| Requested loading | Task fidelity | Current-DD visibly reads the full CW body before the task; no-DD is N/A. |
| Deliverable and boundaries | Task fidelity | Return only the requested revision, without procedural narration; no edits, Git mutation, outside-fixture reads, network or dispatch. |

Semantic PASS requires every semantic row; any failed semantic row is FAIL.
Assess readability separately; deterministic protocol is N/A because no authenticated consumer parses this response.
Inspect the full response trace, including model-authored narration, not only final.txt.
Use tool output for reads/actions, not as the model's deliverable.
Missing required controls or unjudgeable evidence follows the [runbook](../../cw-runbook.md#handoff-and-retention) and [recovery policy](../../README.md#failure-and-recovery), not an assumed PASS.
