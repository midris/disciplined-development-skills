# CW contribution baseline: batch assessment

Format version: `1`
Assessment ID: `contribution-baseline-01`
Study / batch: `concise-writing` / `contribution-baseline-01`
Status: eight approved attempts collected and assessed; descriptive comparison complete.
Scope and acceptance rules: [protocol](protocol.md#contribution-baseline-contribution-baseline-01) at Git `d68e54f4db53931829cf692c33ec7ad95fc191ed`.
Attempt index: [contribution-baseline-01-run-index.json](contribution-baseline-01-run-index.json) at Git `9dac1487c6f7588e6cd8526574490e2dd1ddd2a6`, SHA-256 `fa279e5be3d6c167448312823cb7db48c7e034c6768d4ee5a554ad48def5c4e5`.
Assessor: Codex active session, continuing with owner decisions, skill, constructed cases/examples and prior work available.
This is neither independent nor blind validation; the fresh continuation does not remove that shared context.

## Coverage and execution results

All eight planned attempts were collected in the approved order, preserved before the next dispatch and assessed under CW-assessment-1.
All have valid setup; no retries, replacements, unknown criteria, exclusions or unattempted slots remain.
Both cases use gpt-5.6-sol at low effort, the same neutral baseline/task setup within each pair and the frozen configuration sources.
The full runner/invocation-authority revision is pinned by each attempt; every session records Codex CLI 0.154.0, and the pre-collection binary hash matched the recorded pin.
Session metadata matches each stdout thread and fixture cwd; complete CW tool-response exposure precedes editing in all four original executions.
The provider base instructions are identical across all eight sessions; native system skills remain available, while the target CW catalog entry/file/read instruction appears only in original.
No DD, controller criteria or constructed examples were observed in subject guidance.
These checks establish observed context, not exhaustive host-wide read isolation or an immutable model revision.

Several subjects recovered from rejected combined delete/add patches; order 8 also recovered from a shell chain stopped by an empty guidance-file search.
The exact baseline and final artifacts survived, so these are in-execution editing/setup recoveries, not extra provider attempts or infrastructure exclusions.
Call/time accounting and the accepted single-host evidence risk belong to the [protocol](protocol.md#storage-and-accounting).

| Order | Case / condition / repetition | Setup | Functional outcome | Procedure |
|---:|---|---|---|---|
| [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json) | agent-recommendation / original / 1 | valid | met | P1 met |
| [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json) | agent-recommendation / control / 1 | valid | met | No CW process obligation |
| [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json) | effective-briefing / control / 1 | valid | not met | No CW process obligation |
| [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json) | effective-briefing / original / 1 | valid | not met | P1 met |
| [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) | agent-recommendation / control / 2 | valid | met | No CW process obligation |
| [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) | agent-recommendation / original / 2 | valid | met | P1 met |
| [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) | effective-briefing / original / 2 | valid | not met | P1 met |
| [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) | effective-briefing / control / 2 | valid | not met | No CW process obligation |

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
|---|---:|---:|---:|---:|---:|---:|
| agent-recommendation / original | 2 | 2 | 2 | 0 | 0 | 0 |
| agent-recommendation / control | 2 | 2 | 2 | 0 | 0 | 0 |
| effective-briefing / original | 2 | 2 | 2 | 0 | 0 | 0 |
| effective-briefing / control | 2 | 2 | 2 | 0 | 0 | 0 |

## Aggregate results

Counts are met / not met / insufficient evidence among valid setups.
Functional outcome requires F1–F3; process success cannot offset a functional defect.
These results are descriptive-only under the frozen rule, with no numerical acceptance threshold or population reliability claim.

| Case / condition / criterion | Met | Not met | Insufficient evidence | Evidence |
|---|---:|---:|---:|---|
| agent-recommendation / original / F1 | 2 | 0 | 0 | [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json), [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) |
| agent-recommendation / original / F2 | 2 | 0 | 0 | [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json), [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) |
| agent-recommendation / original / F3 | 2 | 0 | 0 | [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json), [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) |
| agent-recommendation / original / P1 | 2 | 0 | 0 | [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json), [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) |
| agent-recommendation / original / functional outcome | 2 | 0 | 0 | [1](results/20260918T021815333Z-cw-agent-recommendation-original-766a67ff-ff83-4ea0-91ad-de114a6d15e6-t7l9kcgr.json), [6](results/20260918T022752628Z-cw-agent-recommendation-original-cb45c075-8219-4ae1-ab1a-3514ad06d022-77xm_oea.json) |
| agent-recommendation / control / F1 | 2 | 0 | 0 | [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json), [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) |
| agent-recommendation / control / F2 | 2 | 0 | 0 | [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json), [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) |
| agent-recommendation / control / F3 | 2 | 0 | 0 | [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json), [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) |
| agent-recommendation / control / functional outcome | 2 | 0 | 0 | [2](results/20260918T022032109Z-cw-agent-recommendation-control-471483ac-4bbe-4ac1-a64b-38e6adba5b9c-r7gjiu0e.json), [5](results/20260918T022544885Z-cw-agent-recommendation-control-122d29ec-540b-4558-af42-e3423324c291-8e4z4zfz.json) |
| effective-briefing / original / F1 | 0 | 2 | 0 | [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json), [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) |
| effective-briefing / original / F2 | 2 | 0 | 0 | [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json), [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) |
| effective-briefing / original / F3 | 2 | 0 | 0 | [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json), [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) |
| effective-briefing / original / P1 | 2 | 0 | 0 | [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json), [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) |
| effective-briefing / original / functional outcome | 0 | 2 | 0 | [4](results/20260918T022425145Z-cw-effective-briefing-original-15aee229-607f-4851-8a82-cf8f0aca68f0-xzio0i_c.json), [7](results/20260918T022938090Z-cw-effective-briefing-original-e439ed52-f986-4c15-a81c-fd4bf52a09e5-ii_rdnel.json) |
| effective-briefing / control / F1 | 0 | 2 | 0 | [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json), [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) |
| effective-briefing / control / F2 | 2 | 0 | 0 | [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json), [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) |
| effective-briefing / control / F3 | 2 | 0 | 0 | [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json), [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) |
| effective-briefing / control / functional outcome | 0 | 2 | 0 | [3](results/20260918T022308199Z-cw-effective-briefing-control-fb4c90d8-710e-4ddc-8724-4bcd9fa2f62f-93ryhtqf.json), [8](results/20260918T023131505Z-cw-effective-briefing-control-40542fb3-8168-479f-8abe-42e79c06ec4d-c0yy5ofe.json) |

### Failure patterns and judgment boundaries

All four recommendation edits preserve the evidence, limitations, cursor mechanism, limited pilot authority and stop/retain purpose while removing the empty introduction, generic communication digression and duplicate mechanism explanation.
Their organizations and repetition levels differ; all remain useful for the stated decision.
Repeated scope reminders in the longer control edits serve the approval, recommendation or next-action context and do not fail F2 merely because a shorter edit is possible.

All four briefing edits replace the source’s open Thursday invitation question with an affirmative invitation recommendation.
The source recommends keeping the preview opt-in and asks whether to invite four teams; it does not supply an endorsement of that choice.
The edits introduce “Approve invitations…” or “Invite four more teams…” as the author’s recommendation.
Under fixed F1, this is a changed decision stance in an editing task, not a penalty for using a Recommendation heading or moving the decision first.
The later Thursday approval gate survives, so the finding is semantic fidelity, not a claim that the subject actually sent invitations or granted operational approval.
This is an active-session semantic judgment applying the frozen unsupported-meaning-change rule; no exact wording or preferred layout is required.

Orders 3, 4 and 8 also omit the explicit permission for the existing six teams to continue, mentioning them only as past evidence.
Keeping the preview opt-in describes its mode but does not preserve who may continue while the new invitations await approval.
Order 7 preserves that permission and restores “only invited teams” after comparison, yet retains the newly authored endorsement.
These defects remain one failed execution each, not multiple independent failures.
All briefing edits meet F2 and F3: their remaining prose is purposeful and readable, and the F1 semantic defects do not automatically create separate organization failures.

All four original executions meet P1 on observable evidence: complete source reads, saved drafts addressing local and global concerns, and actual source-to-edit comparisons before completion.
Order 7 additionally revises a nuance after its comparison.
This establishes performed actions, not flawless checking or hidden attention; the two original briefing failures show that performing the process did not ensure preservation.
No explicit unresolved framing/padding uncertainty was observed, so O5 is not scored as a failure or treated as fully tested.

## Comparison and interpretation

For agent-recommendation, original and control each meet the functional outcome in 2/2 executions, with zero unknowns.
For effective-briefing, original and control each meet it in 0/2, with two F1 failures and zero unknowns.
The observed tie supports no contribution advantage for CW on these two cases; it does not establish equivalence or prove that CW has no benefit elsewhere.
Do not pool the cases into one success rate that conceals the preservation failure on already-effective prose.

A possible future rewrite target is preserving decision stance and continuing permissions during tightening, including when the source is already effective.
That is a recommendation for a separately authorized study, not permission to edit CW or collect more observations.
No candidate was tested here, and the findings do not justify an adoption decision.
The owner’s existing deferral remains in force.

Coverage remains two short, constructed software updates with two repetitions per condition on one requested model/effort setting.
The assessor had the fixed rules, selected skill and construction history; there was no held-out or independent evaluation.
The common provider already supplies writing guidance, so control is the ordinary task without CW, not an instruction-free model.
Long-document navigation, other audiences/genres, plan/spec composition, native discovery and conditional uncertainty handling remain unestablished.
No edited-document word count is used as a success target or tie-breaker.
The existing runner and formats supported prose evidence and case-specific semantic assessment without new repository tooling or evaluator calls.
