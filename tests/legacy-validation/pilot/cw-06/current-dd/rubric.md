# CW-06 loaded prose behavior — evaluator only

Source: [historical rubric](../../../scenarios/concise-writing/cw-06/rubric.md).
This variant measures loaded prose behavior, not native discovery.
The same behavioral criteria apply to both conditions when a no-DD control exists; absent DD is not a failure.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| Preserve universal requirement | CW-I1 / semantic | Every request requires an API key in the Authorization header; requests without a key are rejected. |
| Remove inflation and repetition | CW-I2 / semantic | State the requirement once and rejection once. Remove redundant universal wording and emphasis, including the source's every single, each and every, redundant always and bold emphasis. Every request must is allowed once to preserve universal scope and obligation. Retaining equivalent padding under different wording also fails. |
| Requested loading | Task fidelity | Current-DD visibly reads the full CW body before the task; no-DD is N/A. |
| Deliverable and boundaries | Task fidelity | Return only the revision; no edits, Git mutation, outside-fixture reads, network or dispatch. |

The named forms illustrate lossless padding removal, not a separate word blacklist: judge whether wording or emphasis adds information or necessary framing.
Score retained padding only under CW-I2, not again as task fidelity.

Semantic PASS requires every semantic row; any failed semantic row is FAIL.
Assess readability separately; deterministic protocol is N/A because no authenticated consumer parses this response.
Inspect the full response trace, including model-authored narration, not only final.txt.
Use tool output for reads/actions, not as the model's deliverable.
Missing required controls or unjudgeable evidence follows the [runbook](../../cw-runbook.md#handoff-and-retention) and [recovery policy](../../README.md#failure-and-recovery), not an assumed PASS.
