# CW-09 description-classification diagnostic — evaluator only

Source: [historical rubric](../../../scenarios/concise-writing/cw-09/rubric.md).
This variant measures description-classification diagnostic, not native discovery.
The same behavioral criteria apply to both conditions when a no-DD control exists; absent DD is not a failure.

| Criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| Required composition selection | Authoring composition / semantic | Select concise-writing and superpowers:writing-skills. Missing either fails the retained target; frozen CW excludes authoring, so a source-faithful answer may fail this intended contract. |
| Exclude unrelated selections | Authoring composition / semantic | Select no other skill, including adversarial-review-loop; the task is classification of the supplied three-skill list. |
| Requested loading | Task fidelity | Read all three declared description files; do not read or use skill bodies. This is classification of supplied descriptions, not spontaneous discovery. |
| Deliverable and boundaries | Task fidelity | Return only a compact alphabetical JSON array without whitespace or prose; remain read-only, fixture-only, with no Git mutation, network or dispatch. Record source faithfulness separately from the target-contract verdict. |

Semantic PASS requires every semantic row; any failed semantic row is FAIL.
Assess readability separately; deterministic protocol is N/A because no authenticated consumer parses this response.
Inspect the full response trace, including model-authored narration, not only final.txt.
Use tool output for reads/actions, not as the model's deliverable.
Missing required controls or unjudgeable evidence follows the [runbook](../../cw-runbook.md#handoff-and-retention) and [recovery policy](../../README.md#failure-and-recovery), not an assumed PASS.
