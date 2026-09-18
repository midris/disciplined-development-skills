# CW criterion examples

Status: policy-4 qualification complete in the active session; six existing constructed edits and two unchanged source controls re-judged as whole documents. The eight subject executions were already collected; these examples add no executions.
Authority: [policy](protocol.md#assessment-policy), [recommendation case](cases/agent-recommendation/assessment.md) and [briefing case](cases/effective-briefing/assessment.md).

These fictional sources and edits were constructed and assessed with the skill and case history available. This is a controller-only worked boundary check, not independent validation, a preferred-answer set or evidence of model performance. Earlier policy-1 judgments remain retrievable through the original collection manifests and Git.

F1 is whole-document correctness and fidelity; F2 is effectiveness for the intended reader relative to the complete source; F3 is readability, including unnecessary consumption burden. `M` means met and `N` means not met. All three must pass. Length is measured with wc -w on the full Markdown files and reported separately; process is unscored.

| Case / complete document | F1 | F2 | F3 | Source → output words | Whole-document evidence and boundary |
|---|---|---|---|---|---|
| A: [untouched source](cases/agent-recommendation/fixture/report.md) | M | M | N | 625 → 625; unchanged | Correct and equally effective by identity, but the reader must traverse empty narration, an irrelevant communication digression and two separated mechanism explanations before reaching the recommendation. Facts are available, yet the overall path to the decision is unnecessarily laborious. F2 is a preservation floor; F3 independently rejects this burden. |
| A: [effective edit](cases/agent-recommendation/examples/effective.md) | M | M | M | 625 → 230; shorter | The decision leads into mechanism, evidence and limits, then instructions. Qualifications and the reason for retaining files remain actionable. The closing stop/retain recap reinforces the action after its rationale rather than forcing the reader through a second full explanation. |
| A: [effective alternative](cases/agent-recommendation/examples/effective-alternative.md) | M | M | M | 625 → 217; shorter | The request and staffing lead, evidence and limitations are grouped, and the causal mechanism supports clear outcome branches. Consolidating the warning retains its use at the action point. A different arrangement can satisfy all outcomes. |
| A: [local cleanup only](cases/agent-recommendation/examples/local-only.md) | M | M | N | 625 → 465; shorter | Removing the empty introduction and generic digression improves the source without reducing correctness or usefulness. However, evidence, mechanics, timing and warning remain dispersed; a second full mechanism explanation interrupts the path to the late recommendation. The reader still assembles the decision across the document. This is the shorter, fact-preserving, improved-but-still-laborious F3 failure. |
| A: [over-trimmed edit](cases/agent-recommendation/examples/over-trimmed.md) | N | N | M | 625 → 184; shorter | The overall proposal loses production/cross-region limits and the reason a limited pilot is warranted; it also drops why retained files matter. The reader can no longer evaluate the evidence and risk as well as from the source. Clear remaining prose and lower word count cannot compensate for loss of correctness/completeness and effectiveness. |
| B: [untouched source](cases/effective-briefing/fixture/report.md) | M | M | M | 279 → 279; unchanged | The briefing already connects the decision, bounded evidence, prerequisites and later review. Its recap returns the reader to the limited invitation decision after the conditions. Unchanged length is acceptable; editing is not required merely to demonstrate activity. |
| B: [effective alternative](cases/effective-briefing/examples/effective.md) | M | M | M | 279 → 245; shorter | The complete edit preserves current participation, limited invitation/default distinction, uncertainty, readiness checks and subsequent review. Evidence, conditions and recap support the same decision with a coherent reading path. Reinforcement has an orienting role rather than becoming a second competing argument. |
| B: [over-trimmed edit](cases/effective-briefing/examples/over-trimmed.md) | N | N | M | 279 → 188; shorter | The whole briefing no longer distinguishes quiet support from proven correctness and replaces the specific timeout threshold and mandatory postponement with vague investigation. That changes the decision safeguards and reduces its usefulness for deciding and acting. Organization remains readable; semantic/action loss does not automatically fail F3 as well. |

The controls and local-only edit show why F2 can pass while F3 fails: being no worse than a padded source is insufficient for an overall pass. The over-trimmed edits demonstrate decisive quality failures despite large reductions. The effective edits and untouched briefing show that consolidation, useful repetition and unchanged length can pass.

No existing example is longer than its source. The longer-output flag is therefore specified by policy but not demonstrated by this example set; do not claim that boundary was exercised. It does not need a new model run: a future longer artifact would receive the flag and an independent F1–F3 judgment.

## Saved-file boundary

These are evidence scenarios, not additional document examples or subject executions.

| Captured state | Expected judgment |
|---|---|
| A’s original file remains; completion describes an unsaved edit | F1 and F2 met, F3 not met, unchanged length. Judge the saved source; the completion claim cannot improve it or turn preserved meaning into failure. |
| B’s original file remains, with or without an editing claim | F1–F3 met, unchanged length. Record unsupported claims separately; infer no process compliance. |
| A partial edit is saved | Judge that complete saved file. The local-only example has F1/F2 met, F3 not met and shorter length. |
| Reliable evidence shows a deleted or empty output | F1–F3 not met: no useful document remains. Report the shared delivery cause once. Zero words cannot compensate. |
| Capture is incomplete and contents cannot be established | Setup/assessment uncertainty, not evidence of deletion or failure. |

## Limits

These are short software updates with known construction history. They do not establish long-document navigation, other audiences, plan/spec completeness or uncertainty handling. The examples demonstrate interpretable boundaries, not population reliability or an independent evaluator qualification. Counts and identities are mechanical facts; the whole-document judgments require reading.
