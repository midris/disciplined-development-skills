# WER offline qualification

In the original offline exercise the operator constructed 17 sample outputs and read the complete project artifacts under opaque labels before opening the sample key and response texts. The same operator authored the examples. This checks that the evidence and criteria distinguish the intended cases. It supplies no independent reviewer result or provider baseline.

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

## Post-review qualification

The eighteenth constructed output substitutes lookup time for downgrade time when testing token eligibility. The previous replay accepted it. The revised replay covers tokens issued at the change and just afterward, then used later during the grace period. In the example downgrade from 100 to 30 at second 200, either token must receive 30 at second 210. The mutation returns 100. The same replay applies to the repeated-review fixture.

The 17 original readings above were made by a single operator across examples. They illustrate scoring boundaries. For the study, each first reading uses an isolated context and one project. The offline generator now emits one self-contained prompt payload per example, separate from the controller’s output map and responses. Actual model delivery and session isolation will be qualified during runtime preparation.

For the helper rename, the worked missed-caller output fails T1. With a complete native trace showing the skill was available and untouched, D1 would be met. With a load, D1 would be not met. With missing exposure or incomplete trace evidence, D1 would be unresolved. These are scoring walkthroughs without observed native runs.

## External review follow-up

The three later samples below were inspected during controller verification. Their readings are source-aware walkthroughs, separate from the original 17 readings. All three pass the starting project tests and fail the private quota replay.

| Worked output | What the final source actually permits |
| --- | --- |
| lookup-time-bug | The comment describes old tokens. The code also grants a higher limit to a new token as soon as lookup time exceeds its issue time. |
| recent-only | The code honors only old tokens issued within 60 seconds before the change. Authentication is upstream and this extra issue-age cutoff rejects eligible requests. |
| assumed-lifetime | The lookup invents a 300-second token lifetime. An authenticated token can lose its prior limit during the agreed downgrade window. |

The private replay now exercises authenticated tokens issued one second and 10,000 seconds before the change at seconds 0, 30 and 59 afterward. Subject materials specify that the new limit applies from second 60. A working implementation with a comment implying a general downgrade delay fails the rationale criterion even if the replay passes. A correct PR-only answer that leaves XML promised in v1 fails the task criterion. An accurate durable comment simply restating the helper rename fails restraint in either case.

In the repeated-review fixture the commit attachment is mounted separately. The reverse-patch check verifies the submitted change against the starting tree. Offline projection checks recover newly added text files, exclude the verified attachment and Git internals, and reject missing supplemental inputs, unexpected changes outside the review channel, project symlinks and invalid UTF-8. Live reader isolation and provider delivery remain unqualified.

External re-review qualification covers both native skill-mount roots, nested Python and pytest caches, and new or amended review correspondence. The controller records omitted paths and reasons beside the payload identity. The retained final project remains available for full-evidence reconciliation.

The latest dry run mounts a root task file in all 20 constructed trees. The builder derives its exclusion from each offline runner config. A separate regression exercises an explicit skill at an ordinary documentation path alongside a legitimate new project document. Rationale supplied only in the subject’s commit message fails placement for the plan, quota, and repeated-review decisions.

## Offline case review closed

In the owner-supplied re-review of `550bc6b3`, Claude confirmed the wrong-directory regression was fixed and reported no further case findings. With the correct fixture directory, the reader received the two unchanged quota project files and the newly added decision file. An unrelated directory stopped packet creation. Use a clean checkout of the frozen source when preparing live packets because the coverage check examines every file in that directory.

The active session reran all nine reader-payload tests and the 20 constructed outputs successfully. These checks close preparation of the four cases. The provider configurations, manifests, runtime qualification and model-call allocation remain open.

## Suite extension

The initial extension constructed 30 outputs. For dispatch hold, both a precise spec reference and an accurate explanation at each consumer preserve the decision. A contradictory local comment and an invented carrier naming rule each pass the private replay but create separate rationale and restraint misses. Dropping already-loaded holds from the morning planner fails the private replay even with the worked explanation intact.

For scope trim, read the complete plan before the supplied handoff. The worked repair preserves both daily and both weekly decisions. The four contrasts omit the weekly alert from the plan, promise delivery when Finance agrees, make Support's manual comparison compulsory every week, or leave the underlying reason and condition solely in the response. Score the specific effect on scope, timing or Support's obligations. These are controller-authored examples. Equivalent concise prose can pass.

### Extension scoring walkthrough

The extension now adds 18 examples to the 20 original examples. These source-aware walkthroughs describe the intended semantic judgments. The generator verifies the replay and reader-packet mechanics.

| Dispatch variant | What a maintainer can recover | Expected judgment |
| --- | --- | --- |
| complete | The references lead to the current reason and dispatcher exception. | Pass |
| bare | Both planners use statuses named in the readily identifiable spec. | Pass without comments |
| local-reasons | Each site explains the consequence accurately. | Pass |
| conflicting-copy | Overflow directs removal of loaded parcels despite the spec. | R1 miss |
| lost-policy | The spec preserves behavior but drops the reason and dispatcher role. | R1 miss |
| full-copies | Three complete copies create separate update obligations. | Pass with a density caveat |
| title-story | The title acquires an invented carrier contract. | R2 miss |
| ready-only | Overflow drops an ordinary sorted parcel. | T1 miss, replay fails |
| loaded-regression | Morning drops an assigned held parcel. | T1 miss, replay fails |

| Scope variant | What Operations or Support can recover | Expected judgment |
| --- | --- | --- |
| complete | The adoption review and Finance trigger have separate homes. | Pass |
| gate-only | Finance agreement is a prerequisite. The plan makes no delivery promise. | Pass with a precision caveat |
| implicit-week | Nearby text supports the affected-week reading. | Pass with a precision caveat |
| lost-impact | The plan gives the reason and trigger but loses the possible Support workload. | R1 miss |
| silent-cut | The weekly deliverables disappear entirely. | T1 and R1 miss, one omission |
| lost-weekly-alert | A reader cannot tell what happened to the weekly alert. | T1 miss for missing scope |
| firm-promise | Finance agreement commits Operations to delivery. | R1 miss |
| weekly-duty | Support is told to do mandatory weekly comparisons. | R1 miss |
| summary-only-reason | A correct reply leaves the plan with only the names of deferred items. | R1 miss |
