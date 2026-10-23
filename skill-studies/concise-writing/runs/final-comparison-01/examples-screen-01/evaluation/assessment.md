# Short CW examples comparison

The screen found no repeated benefit from replacing the examples.
Apply the owner's accepted fallback: retain the unchanged original body with the selected rewritten description.
The [selected combination](../../../../drafts/baseline-iteration/final-comparison/skills/original-body/SKILL.md) remains byte-identical to the tested 869-word file; the 938-word replacement-examples candidate stays available as development evidence.
This is a conditional body choice under the [fixed exploratory rule](../../../../drafts/baseline-iteration/original-examples/comparison-proposal.md#fixed-execution-and-interpretation), not proof of equivalent reliability or a live deployment decision.

## Results and review provenance

Twelve valid fresh outputs cover three repetitions per body/provider on the same 1,207-word operational handoff.
Codex subjects used gpt-5.6-sol low; Claude subjects used claude-sonnet-5 low.
Both fresh-context reviewers used claude-opus-5-5 medium, different-family relative to the active Codex assessor and same-family as Claude subjects.
Condition labels were visible; review was independent but not blinded.

| Subject provider | Active original-body | Active original-examples | Opus independent first pass | Changes after prior-score access |
| --- | --- | --- | --- | --- |
| Codex | 2/3 pass | 3/3 pass | Both 3/3 pass | Original repetition1 F1/F2 changed from met to not met; F3 remains met. |
| Claude | 3/3 pass | 3/3 pass | Both 3/3 pass | None. |

All F3 judgments pass in both active assessment and the independent reviews.
The [full-ID transcription](judgments.json) preserves all 36 first-pass factors separately from active scores and the two post-prior reversals.
The [Codex first pass](codex-long-handoff-first-pass.md) and [Claude first pass](claude-long-handoff-first-pass.md) are retained unchanged.
The [review ledger](evaluator-run-index.json) locates both raw bundles and final reviews.

### The original-body rollback failure

Codex original repetition1 places destination-status confirmation, cursor reconciliation and lease release under “If an acknowledgement is outstanding”.
The complete source instructs the responder to confirm destination status and reconcile the cursor before release without that restriction.
The output retains the warning that package reversal alone does not restore the cursor, but supplies no unconditional recovery sequence for the other branch.
That narrows a consequential requirement for readers entering Rollback directly: active F1/F2 remain not met.
Other retained safeguards and the strong scan layout do not cancel this failure.

Opus noticed the conditional framing in its independent first pass but initially accepted it.
Only after reading the active assessment did it recognize the lost branch and change F1/F2.
Its further explanation was that confirmation with the operator is itself how an arriving responder can establish outstanding status.
That is reasoned post-prior agreement, not independent first-pass confirmation.
The raw first pass, final explanation and original active scores remain separate; no score is changed by majority vote.

The other two original outputs and all three examples outputs preserve the unconditional sequence.
This is one observed original-body miss, not a repeated constraint-preservation advantage for the new examples.
The screen does not establish that the examples caused the difference or that the original has equal reliability.

## Compression, cleanup and reading quality

| Provider | Original output words, repetitions1–3 | Examples output words, repetitions1–3 | Original mean | Examples mean |
| --- | --- | --- | ---: | ---: |
| Codex | 825 / 1020 / 826 | 1018 / 852 / 876 | 890.3 | 915.3 |
| Claude | 1061 / 1129 / 1080 | 1138 / 1128 / 1049 | 1090.0 | 1105.0 |

Every output is shorter than its source.
The original averages 25 fewer words on Codex and 15 fewer on Claude; neither difference establishes an effectiveness or readability winner.
Both Codex conditions range from conservative edits to substantial reorganization.
All six Codex outputs remove the detached implementation reminder and consolidate duplicate staging counts.
Original repetition1 has especially scannable lists, while original repetition3 compresses almost as strongly without narrowing the recovery instruction.
The examples outputs provide readable connected prose but no repeated cleanup or organization advantage.

Claude mostly preserves the source's layout and operational wording in both conditions.
Every output removes generic opening narration and consolidates duplicated staging evidence.
The detached reminder is removed in original repetitions1/3 and examples repetition3: 2/3 versus 1/3.
That is a modest original cleanup advantage in this sample, not an automatic F3 failure for the retained reminders.
Examples repetition3 makes somewhat deeper cuts to the dry-run summary and closing untested-risk wording, while original repetition1 preserves those caveats and still reads cleanly.
No repeated examples advantage follows from those single-output observations.

Both reviewers' minor narrative errors are qualified in the [Codex audit](codex-long-handoff-audit.json) and [Claude audit](claude-long-handoff-audit.json).
In particular, the Claude review overstates that the entire Handoff section is verbatim; examples repetition3 consolidates its closing untested-risk sentences while preserving handoff obligations.
The Codex first pass's entry-point consistency claim is internally contradictory and is not adopted.
Precision cautions are judged in complete context; an actual introduced inaccuracy is never excused merely because it appears harmless.

## Setup, accounting and limits

The accepted Claude2.1.308/Python3.14.9 substitutions passed thirteen zero-model qualification checks; Codex0.163.0/Git2.56.0, models, efforts and permissions remain fixed.
Every valid subject received the complete assigned body before its first task edit.
Both reviewers received all fifteen required complete files before emitting a first pass, then read prior-assessment.md separately.
Actual models, native Read/Glob/Grep-only tools, protected packet bytes, first-pass/prior order and manual semantic completeness are verified in both audits.
No skill bodies, descriptions, historical output reviews, hypotheses or raw subject traces entered the review packets.

The first Claude attempt failed on expired OAuth before inference and is invalid setup.
It remains retained and charged as a subject invocation.
The owner's “I logged in, please try again” approved exactly one unchanged replacement from the retry pool.
The full [Claude index](../claude-final-examples-screen-01-run-index.json) contains seven attempts yielding six valid outputs; the [Codex index](../codex-final-examples-screen-01-run-index.json) contains six attempts.
Twelve subject-pool charges, one retry-pool charge and two evaluator-pool charges fund this completed screen.
No failed call is hidden, transferred to another pool or included in functional denominators.

The [verification record](verification.json) pins retained audit scripts, manual transcription and logs.
Typed indexes/results, all thirteen subject inventories/captures and the explicit full-index coverage/charge audit pass.
Codex batch assessment readiness passes.
Claude batch assessment readiness reports retry/scope/coverage errors because that checker only implements no-retry membership and computes a negative unattempted count for the extra attempt.
It is not claimed to pass; the [resumption rationale](../preparation/resumption/README.md) preserves the manual scope/retry/aggregate audit, and the active plan tracks the runner-only follow-up.
No runner feature was added during this fixed experiment.

Three repetitions are the accepted exploratory sample below writing-skills' five-plus wording guidance, not a reliability or equivalence estimate.
There is no no-CW arm and no native-invocation measurement; this is a relative examples comparison under explicit complete-body delivery.
Old outputs, scores and reviews are not pooled into this fresh runtime stratum.

The fixed rule requires a repeated, concretely explained difference before treating the new examples as a noticeable improvement.
Quality is mixed, the single original rollback defect is not repeated, and the examples add 69 skill words without a repeated output benefit.
The conditional original-body choice follows that rule while preserving the miss and its limits; it does not invoke a statistical equivalence claim or waive correctness.
The [protocol](../../../../protocol.md) owns current authority, accounting and the next owner decision.
No automatic extension, wording edit, next scenario or live installation follows this report.
