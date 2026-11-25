# Five-run comparison of the residual-risk example

| Whole-output or decision-site observation | 599 words | 604 words |
|---|---:|---:|
| Claude repeated review met all criteria | 5/5 | 5/5 |
| Claude explicitly described the temporary higher quota as accepted | 1/5 | 5/5 |
| Claude identified rejection of admitted work in the quota comment | 5/5 | 5/5 |
| Claude kept future factoring open in the project | 5/5 | 4/5 |
| Claude kept future factoring open throughout the handoff | 1/5 | 2/5 |
| Codex quota grace met all criteria | 5/5 | 5/5 |
| Codex explicitly accepted temporary excess quota | 5/5 | 5/5 |
| Codex explicitly named rejection of already-admitted work | 1/5 | 1/5 |

All four final attempts had valid setups, survived inventory verification, and passed both the original tests and the private quota replay. All ten 604-word attempts across the three allocations are retained. The [first pair](../residual-risk-01/assessment.json), [middle four](../residual-risk-02/assessment.json) and [final four](assessment.json) link the individual judgments and evidence. The comparison uses the corresponding ten subjects from the [599-word benchmark](../rewrite-broad-05/report.md).

Both new Claude projects recovered the quota decision from the submitted change, explained it beside the implementation, and kept the third interactive caller as a trigger to reconsider factoring. Repetition four stated the rejection consequence more definitively than the source. Repetition five invited reconsideration in the reply, then predicted the refactor. Repetition two remains the one 604-word project that committed a future maintainer to factoring. The code still explained why approved imports must bypass interactive admission.

Both final Codex projects explicitly accepted the temporary excess to honor already-admitted work. A maintainer can infer the consequence of immediate enforcement in both. Across five, only repetition two named rejection directly. The accepted cost is supported by the original inputs in all ten 604-word projects.

Prefer the 604-word example for making an accepted cost explicit. Claude improved on this targeted observation and Codex already supplied it consistently. The two variants tied on the whole-output criteria. Five repetitions on each of two known provider–scenario combinations support a narrow wording preference; broader suite, transfer and independent review evidence belongs to the 599-word text.
