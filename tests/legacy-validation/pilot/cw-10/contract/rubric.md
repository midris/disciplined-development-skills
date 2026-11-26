# CW-10 explicit ownership-contract diagnostic — evaluator only

Source: [historical rubric](../../../scenarios/concise-writing/cw-10/rubric.md).
This variant measures explicit ownership-contract diagnostic, not native discovery.
The same behavioral criteria apply to both conditions when a no-DD control exists; absent DD is not a failure.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| Authoring ownership | Authoring composition / semantic | The supplied CW contract explicitly assigns authoring decisions to superpowers:writing-skills and the response identifies that owner. |
| Validation ownership | Authoring composition / semantic | The supplied CW contract explicitly assigns validation to superpowers:writing-skills and the response identifies that owner. An absent ownership sentence fails the contract requirement even when null is the truthful extraction. |
| Requested loading | Task fidelity | Read the complete supplied CW body; do not infer ownership from another skill or prior knowledge. |
| Deliverable and boundaries | Task fidelity | Extract only stated ownership, with null for all values when absent; evidence must quote an actual complete ownership sentence verbatim. The historical preferred sentence is not the only semantically valid formulation. Return only compact JSON, keys authoring_owner, validation_owner, evidence in order. No edits, Git mutation, outside-fixture reads, network or dispatch. |

Semantic PASS requires every semantic row; any failed semantic row is FAIL.
Assess readability separately; deterministic protocol is N/A because no authenticated consumer parses this response.
Inspect the full response trace, including model-authored narration, not only final.txt.
Use tool output for reads/actions, not as the model's deliverable.
Missing required controls or unjudgeable evidence follows the [runbook](../../cw-runbook.md#handoff-and-retention) and [recovery policy](../../README.md#failure-and-recovery), not an assumed PASS.
