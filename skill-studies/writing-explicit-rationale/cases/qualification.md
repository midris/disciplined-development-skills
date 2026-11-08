# WER offline qualification

The operator constructed 17 sample outputs and read the complete project artifacts under opaque labels before opening the sample key and response texts. The same operator authored the examples. This checks that the evidence and criteria distinguish the intended cases. It supplies no independent reviewer result or provider baseline.

| Case | Constructed output | Mechanical observations | First reading, reconciled to the sample label |
| --- | --- | --- | --- |
| export-deferral | complete | Document inspection | XML waits for partner approval of an unstable schema; CSV/JSON still ship and the affected customers wait. |
| export-deferral | invented-date | Document inspection | XML customers wait for the next quarter. Why that timing matters is unclear. |
| export-deferral | pr-only | Document inspection | CSV and JSON ship. The tree says nothing about XML or its customers. |
| helper-rename | complete | project tests pass | Negative corrections cannot grant capacity. The private name needs no additional explanation. |
| helper-rename | lost-reason | project tests pass | Values clamp at zero. The reason for clamping is unclear. |
| helper-rename | missed-caller | project tests fail | The old helper reference in available_units is unresolved. The reason for clamping remains present. |
| helper-rename | rename-clutter | project tests pass | Same reason for clamping, plus a claim that a wire protocol mandates this private name. |
| quota-grace | behavior-only | project tests pass, quota replay pass | Old tokens retain the old limit before the cutoff. Why that is necessary is unclear. |
| quota-grace | complete | project tests pass, quota replay pass | Admitted old-token work keeps its higher quota up to, excluding, second 60. |
| quota-grace | expiry-bug | project tests pass, quota replay fail | The comment says preserve admitted work for 60 seconds. At second 60 the old limit still applies. |
| quota-grace | new-token-bug | project tests pass, quota replay fail | The old-token explanation is present but the implementation also grants new tokens the old quota. |
| quota-grace | starting | project tests pass, quota replay fail | The limit changes immediately; there is no grace explanation. |
| repeated-review | batch-regression | project tests fail, quota replay pass | The source expressly intends approved batches to bypass admission, but imports call the rejecting interactive path. |
| repeated-review | complete | project tests pass, quota replay pass | Both batch-bypass/third-caller and quota/exposure decisions are recoverable; the helper is routine. |
| repeated-review | guard-only | project tests pass, quota replay pass | The two-guard exception and third-caller trigger are explained. The quota grace motive is unclear. |
| repeated-review | reply-only | project tests pass, quota replay pass | Batch imports bypass two interactive guards and there is a timed quota condition. The intended trade-offs and revisit trigger are unclear. |
| repeated-review | unnecessary-comment | project tests pass, quota replay pass | Both decisions are explained; the label helper claims an external billing name requirement. |

For the PR-only deferral the second-pass response accurately gives the schema reason. The release plan still omits XML, so the reason cannot be recovered at the plan item. The invented quarterly date conflicts with the source even though the summary is accurate. In the routine edits, second-pass source comparison establishes that the claimed billing naming requirement is invented.

The reply-only review answer mentions the batch exception and third-caller trigger, but neither decision is explained in the project. The guard-only project explains the first decision while leaving the second unresolved. In the complete example, both reasons are recoverable and behavior is intact. The quota example with comments removed passes the same timing replay as the complete example. The two boundary mutations fail that replay even though the project’s starting tests pass.

Native selection requires an actual catalog and subject trace. All discovery criteria remain unmeasured.
