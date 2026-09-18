# CW contribution baseline: batch assessment

Format version: `1`
Assessment ID: `contribution-baseline-01`
Study / batch: `concise-writing` / `contribution-baseline-01`
Status: complete policy-4 reassessment of the same eight executions; all three quality criteria met, length reported separately.
Scope and acceptance rules: [protocol](protocol.md#contribution-baseline-contribution-baseline-01) at Git `04b143b30df2cfcd5d73c23f032355edb6f8062f`.
Attempt index: [contribution-baseline-01-run-index.json](contribution-baseline-01-run-index.json) at Git `5bcb2958021a840a3c330fe7a4f43b9fa3e79423`, SHA-256 `97f41234b99140029e4e99bb840a00a96de42971b4e588b906d8e4b9c8b02303`.
Assessor: Codex active session with construction history, prior judgments and owner feedback available. This is neither independent nor blind validation.
The owner changed the scoring contract after seeing outputs; these are retrospective judgments under the revised rule, not a newly collected or prospectively scored sample.

## Coverage and execution results

All eight planned attempts were collected in the approved order and preserved before the next dispatch.
All have valid setup; no retries, replacements, unknown factors, exclusions or unattempted slots remain.
Both cases use gpt-5.6-sol at low effort with matched baseline/task context and frozen configurations.
Session metadata matches each stdout thread and fixture cwd; full CW tool-response exposure precedes editing in all four original executions.
Provider base instructions match across all eight sessions, with native system skills available; only original receives target CW guidance.
No DD, scoring rules or constructed examples were observed in subject guidance. This establishes observed context, not exhaustive host isolation or an immutable model revision.
The attempt index retains actual collection manifests; results identify [recommendation](cases/agent-recommendation/assessment-manifest.json) and [briefing](cases/effective-briefing/assessment-manifest.json) reassessment manifests with exactly unchanged subject-source and condition identities.
Earlier policy-1 judgments remain retrievable in Git. No source document, subject output, raw bundle or skill bytes changed.
Call/time accounting and accepted storage limitations belong to the [protocol](protocol.md#storage-and-accounting).

Every pass below requires F1 correctness, F2 effectiveness at least equal to the source and F3 readability.
Length is separate: shorter is preferred, unchanged is acceptable, and longer is flagged without automatic failure.
Correctness and effectiveness are the primary gates. Editing process is unscored.
Word counts use wc -w on the complete Markdown files, including headings and list markers.

| Order | Case / condition / repetition | Setup | Functional outcome | Source words | Output words | Change | Longer flag |
|---:|---|---|---|---:|---:|---:|---|
| [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json) | agent-recommendation / original / 1 | valid | met | 625 | 217 | -408 | no |
| [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json) | agent-recommendation / control / 1 | valid | met | 625 | 286 | -339 | no |
| [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json) | effective-briefing / control / 1 | valid | met | 279 | 214 | -65 | no |
| [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json) | effective-briefing / original / 1 | valid | met | 279 | 214 | -65 | no |
| [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) | agent-recommendation / control / 2 | valid | met | 625 | 249 | -376 | no |
| [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) | agent-recommendation / original / 2 | valid | met | 625 | 223 | -402 | no |
| [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) | effective-briefing / original / 2 | valid | met | 279 | 240 | -39 | no |
| [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) | effective-briefing / control / 2 | valid | met | 279 | 226 | -53 | no |

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
|---|---:|---:|---:|---:|---:|---:|
| agent-recommendation / original | 2 | 2 | 2 | 0 | 0 | 0 |
| agent-recommendation / control | 2 | 2 | 2 | 0 | 0 | 0 |
| effective-briefing / original | 2 | 2 | 2 | 0 | 0 | 0 |
| effective-briefing / control | 2 | 2 | 2 | 0 | 0 | 0 |

## Aggregate results

Counts are met / not met / insufficient evidence among valid setups.
All three quality factors are required; there is no weighted score, compression bonus or separate process score.
Each execution contributes once to its functional outcome, even if multiple factors share a cause.

| Case / condition / criterion | Met | Not met | Insufficient evidence | Evidence |
|---|---:|---:|---:|---|
| agent-recommendation / original / F1 | 2 | 0 | 0 | [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json), [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) |
| agent-recommendation / original / F2 | 2 | 0 | 0 | [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json), [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) |
| agent-recommendation / original / F3 | 2 | 0 | 0 | [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json), [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) |
| agent-recommendation / original / functional outcome | 2 | 0 | 0 | [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json), [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) |
| agent-recommendation / control / F1 | 2 | 0 | 0 | [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json), [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) |
| agent-recommendation / control / F2 | 2 | 0 | 0 | [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json), [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) |
| agent-recommendation / control / F3 | 2 | 0 | 0 | [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json), [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) |
| agent-recommendation / control / functional outcome | 2 | 0 | 0 | [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json), [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) |
| effective-briefing / original / F1 | 2 | 0 | 0 | [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json), [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) |
| effective-briefing / original / F2 | 2 | 0 | 0 | [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json), [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) |
| effective-briefing / original / F3 | 2 | 0 | 0 | [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json), [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) |
| effective-briefing / original / functional outcome | 2 | 0 | 0 | [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json), [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) |
| effective-briefing / control / F1 | 2 | 0 | 0 | [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json), [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) |
| effective-briefing / control / F2 | 2 | 0 | 0 | [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json), [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) |
| effective-briefing / control / F3 | 2 | 0 | 0 | [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json), [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) |
| effective-briefing / control / functional outcome | 2 | 0 | 0 | [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json), [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) |

All eight outputs meet all three quality factors; all are shorter and none has a longer-output flag. No whole-document failure or unresolved judgment remains in this assessment.
For Recommendation, each edit makes the same limited pilot decision easier to find and act on while retaining evidence, causal explanation, uncertainty, staffing and timing, safeguards and the separate release decision.
The edits remove the source’s digressions and dispersed duplication while keeping usable reasons and warnings. Different section orders all work for the stated reader.

For Briefing, each complete edit still supports a Thursday decision about four additional invitations, subject to checks and approval, within an opt-in preview whose default and wider rollout remain separate decisions.
Evidence limits, responsible people, the timeout threshold and interval, postponement and later review remain usable together.
The opening recommendation is conditional when read with those provisions; it does not announce an unconditional decision.
Order 7 explicitly restates continuing permission for existing teams. Orders 3, 4 and 8 convey continuity through the participating six teams, four more/additional teams and keeping the preview opt-in.
The missing standalone permission sentence does not establish a changed permission or a less effective decision briefing in that context. The previous failure treated a local omission as decisive without demonstrating a whole-document loss; that finding is withdrawn.
This does not make all omissions harmless: a loss that changes the complete document’s correctness or reduces its effectiveness would fail F1 or F2.

All edits are readable, with the decision, evidence, conditions and next actions connected. All are shorter: Recommendation falls from 625 words to 217–286 and Briefing from 279 to 214–240.
These reductions are preferred length outcomes, not evidence for F1–F3. Same-length outputs would be acceptable; longer ones would be flagged without automatically failing. Greater reduction earns no extra credit.

## Comparison and interpretation

Original and control each pass 2/2 on Recommendation and 2/2 on Briefing, with zero unknowns.
The pass counts show equal threshold outcomes, not identical quality. Both conditions produce usable edits; these small observations do not establish an overall or reliable CW advantage. The study does not require a failing control.
Qualitative comparison, separate from pass/fail and length:

| Pair | Effectiveness and reading experience |
|---|---|
| Recommendation, repetition 1: orders 1 / 2 | Both support the same pilot decision and safeguards. Order 1 gives a more continuous read from request through support to action. Order 2 separates recommendation, evidence and mechanism and provides numbered safeguards, making those steps easier to scan independently but adding transitions for a reader reading straight through. Its opening request, rationale and closing confirmation do not by themselves establish harmful padding. |
| Recommendation, repetition 2: orders 6 / 5 | Order 6 gathers request, staffing and both result branches at the start, so the decision reader encounters the operating consequences together. Order 5 gives the stop condition a separate heading and groups untested risks as a list, which aids targeted lookup. Both improve the source’s fragmented reading path; their differences remain visible despite equal passing judgments. |
| Briefing, repetition 1: orders 4 / 3 | Both put the conditional recommendation first, connect bounded evidence to approval checks, and close with later review. Order 3 separates follow-up with a heading; order 4 joins it to the approval consequence. Neither layout demonstrates a consequential quality advantage for the stated decision reader. |
| Briefing, repetition 2: orders 7 / 8 | Order 7 brings readiness/approval immediately after the recommendation; order 8 leads with evidence before the checks. The first favors checking action prerequisites, the second reading the supporting argument first. Both remain clear and preserve the same decision boundaries. |

These are active-session reading judgments, not measured reader timings or numerical quality grades. Future authorized rewrite comparisons should report supported gains and regressions at this level alongside pass counts and length. Policy 4 is the frozen rule for those comparisons unless the owner explicitly amends it; this does not authorize a new comparison.

The corrected results do not support the previously suggested continuing-permissions rewrite target.
No candidate was tested, and no skill rewrite or adoption decision follows from this batch.

The evidence consists of two short constructed software updates, two repetitions per condition and one requested model/effort setting.
The common provider already supplies writing guidance, so control means the ordinary task without CW, not an instruction-free model.
The same informed session authored and reassessed the cases after owner feedback. Counts describe these observations, not population reliability, held-out transfer or a causal estimate of CW’s value.
Long documents, other audiences and genres, plan/spec composition, native discovery and conditional uncertainty handling remain unestablished.
Existing runner/formats supported the reassessment without new repository tooling or model calls.

Verification: the corrected assessment-stage CLI validates this batch using each result’s pinned criteria, while checking that reassessment preserves the actual subject inputs. Both the report and protocol readiness now pass without the former missing-P1 diagnostics. Direct checks also verify all 16 aggregate rows, evidence hashes, word counts and policy-copy equality.
