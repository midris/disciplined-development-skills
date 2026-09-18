# CW criterion examples

Status: case design owner-accepted; constructed examples checked in the active session. Collection is approved; committed input freeze remains outstanding. No subject executions.
Authority: [protocol](protocol.md), [recommendation case](cases/agent-recommendation/assessment.md) and [briefing case](cases/effective-briefing/assessment.md).

The active agent constructed these fictional sources and edits using the complete preserved skill, accepted owner clarifications and the case rules, then inspected each complete document against its source. The same session authored and judged them with all guidance available. This is a worked boundary check, not independent validation, blind assessment or evidence of skill performance. All examples are controller-only. Git preserves revisions; no separate execution-result records are created for examples.

The judgments below apply F1 (meaning/framing), F2 (contextual concision) and F3 (readability). `M` means met; `N` means not met. A functional result requires all three. We do not infer process compliance from constructed prose, so P1 is not assessed here.

| Case / complete document | F1 | F2 | F3 | Evidence and boundary checked |
|---|---|---|---|---|
| A: [untouched source](cases/agent-recommendation/fixture/report.md) | M | N | N | All meaning survives by identity. Empty introduction, adjacent restatement and two separated full mechanism explanations remain. The reader reaches the actual recommendation only after fragmented checks, mechanics, timing, warnings and the second explanation. Faithfulness alone is insufficient. |
| A: [effective edit](cases/agent-recommendation/examples/effective.md) | M | M | M | Decision first, evidence and limits together, then action. Preserves all scenario facts, cursor mechanism, limited approval and evidence-retention rationale; repeated stop/retain reminder serves the final action summary. |
| A: [effective alternative](cases/agent-recommendation/examples/effective-alternative.md) | M | M | M | Evidence precedes the mechanism and action uses bullets. Warning is consolidated into one usable instruction. Preserves information and function without copying the first example’s wording, order or repeated warning. |
| A: [local cleanup only](cases/agent-recommendation/examples/local-only.md) | M | N | N | Removes the empty introduction, adjacent 50-export restatement, communication digression and inflated encouragement. Facts remain, but both complete mechanism explanations and fragmented path to the late recommendation survive. This is also the fact-preserving edit that leaves the reading difficulty unresolved. |
| A: [over-trimmed edit](cases/agent-recommendation/examples/over-trimmed.md) | N | M | M | Derived from the effective edit by removing production/cross-region limitations, why exposure is limited and why both files matter. The remaining prose is concise and organized; those successes cannot compensate for lost qualifications and rationale. |
| B: [untouched source](cases/effective-briefing/fixture/report.md) | M | M | M | Decision, evidence, prerequisites and follow-up are already grouped. The invitation/default distinction helps at the opening, action point and closing recap; no change is necessary merely to demonstrate editing. |
| B: [effective alternative](cases/effective-briefing/examples/effective.md) | M | M | M | Retains numerical facts, evidence limitations, scope, responsible people, consent/switch-back checks, strict greater-than threshold and time window, approval sequence and seven-day review. Rephrasing and useful reinforcement remain acceptable. |
| B: [over-trimmed edit](cases/effective-briefing/examples/over-trimmed.md) | N | M | M | Removes the no-reports/actual-correctness qualification and replaces the exact timeout condition and mandatory postponement with “if the rate is high, investigate.” The shorter, still-organized document changes the decision rule. F1 carries that semantic failure; F3 is not automatically failed as well. |

The examples distinguish purposeless duplication from useful reinforcement without requiring a fixed number of repetitions. They also allow different faithful structures and preserve a successful unchanged document. No example is the sole accepted answer, and no count of removed words or planted passages contributes a score.

## Saved-file boundary

These are constructed evidence scenarios applying the same cards, not additional subject executions or new document variants. They distinguish the artifact from claims about editing it.

| Captured state | Expected judgment |
|---|---|
| A’s original file remains; the completion message describes an unsaved edit | F1 met; F2 and F3 not met, as for the untouched source above. The unsaved edit cannot improve the saved document’s outcome, and the delivery claim cannot turn preserved meaning into a failure. |
| B’s original file remains, with or without a claim that it was edited | F1–F3 met, as for the already-effective source above. Record an unsupported editing claim separately; infer no process compliance from the artifact. |
| A partial edit is saved | Apply each criterion to that file. For example, the local-only variant keeps F1 met while F2 and F3 fail; no blanket delivery verdict overrides it. |
| Reliable final-state evidence shows the subject deleted or emptied the file | F1–F3 not met: no document remains to preserve meaning or provide concise, readable guidance. Record the shared delivery cause once at execution level. |
| Final-state capture is incomplete, so the file’s presence or contents cannot be established | Apply the setup/uncertainty boundary; do not treat missing evidence as proof that the subject deleted the file or failed the criteria. |

Limits: both contexts are short software-change updates. B supports a useful decision recap, but does not exercise navigation through a long document. A’s generic communication advice is an obvious noncontributing digression, not a difficult judgment about novel advice. Conditional uncertainty handling, plan/spec completeness, broader genres and long-document behavior remain untested. No new mechanical checker is needed: ordinary file comparison establishes bytes; the recorded semantic judgments require reading.
