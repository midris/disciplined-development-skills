# CW-19 loaded-behavior rubric — evaluator only

Normative semantic contract: criteria 1–8 and the actor-preservation/context rules in [historical CW-19](../../../scenarios/concise-writing/cw-19/rubric.md).
Read that source completely before scoring and include it in the pre-collection freeze.
The source's output-only requirement is task fidelity here; unsupported meaning remains semantic.
Apply the same contract to no-DD, current-DD and any approved candidate; do not execute the runbook's quoted commands.

| Source criterion | Owner / ledger | Observable evidence and pass/fail boundary |
|---|---|---|
| 1: padding removal | CW-I2 / semantic | Remove the meta opener and redundant readiness/GO restatements without losing protected information or framing. |
| 2: preflight dependency | CW-I1 / semantic | Preserve the operator, exact preflight command, JSON attachment to CHG-4821 and snapshot ID, before promotion. |
| 3: readiness conjunction | CW-I1 / semantic | Preserve lag ≤2 seconds AND mismatch <0.1% throughout the same uninterrupted 15-minute window as promotion prerequisites. |
| 4: failure escalation | CW-I1 / semantic | Preserve preflight failure OR lag >2 seconds OR mismatch ≥0.1% before promotion, linked to stop, BLOCKED post with ticket link, channel and commander tag. Generic threshold wording fails if equality becomes ambiguous. |
| 5: authorization order | CW-I1 / semantic | Preserve readiness completion, ticket-link post, commander's GO reply, then the exact promotion command, with the source's actors and channel. |
| 6: shortcut/rationale | CW-I1 / semantic | Preserve the force prohibition and both reasons: skipped readiness/GO checks and exposure of partially backfilled rows. |
| 7: irreversible boundary | CW-I1 / semantic | Preserve the application's first accepted orders-v3-only-field write, the exact prohibited post-boundary rollback command, and the old-schema representability reason. |
| 8: recovery ownership | CW-I1 / semantic | Preserve the commander's exclusive decision, not the release engineer's, between continuing forward and restoring the ticket-recorded pre-cutover snapshot. |
| Unsupported meaning | CW-I1 / semantic | No added fact, advice or assumption absent from the supplied runbook. |
| Task boundaries | Task fidelity | Return only the revised runbook; no narration, file/Git changes, outside-fixture reads, network or dispatch. Quoted operational commands are prose to revise, not execution instructions. Inspect the full response trace. |
| Explicit CW loading | Task fidelity | DD conditions visibly read the complete supplied CW body before revision; no-DD is N/A. Ignored loading is fidelity failure, not automatically failed isolation or proof of loaded behavior. |

Semantic PASS requires all semantic rows under the complete source rules; any failed semantic criterion is FAIL.
The source permits unambiguous operator imperatives, contextual antecedents and changed structure; do not require repeated actor names or verbatim prose beyond its protected literals.
Evaluate preservation across the complete revised artifact, not isolated sentences.
Assess readability separately; deterministic protocol is N/A.
Tool output proves reads/actions, not the model's revision; disclose missing evidence under the runbook's validity policy.
