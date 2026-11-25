## Part 1 — Independent first-pass assessment (written before reading prior-assessment.md)

**What I read:** `EVALUATION-INDEX.json`, `SETUP.md`, `sources/TASK.md`, `sources/report.md` (1,207 words), `policy.txt`, `criteria.md`, `INTERPRETATION.md`, `WORD-COUNTS.json`, `MECHANICAL-CHECKS.json` (empty `{}`) and all ten outputs in full. I did not read skill bodies, descriptions, traces or `prior-assessment.md`.

**Review conditions:** This review is independent but not blinded, because condition labels are visible in the filenames and the index. One correction to the brief: the index lists `subject_provider: codex` and `subject_model: gpt-5.6-sol`, so the subjects are not Claude models. That makes me a different model family from both the subjects and the Codex assessor. This changes the disclosure only, not any judgment.

**Notes that apply to all ten outputs:**
- Every output removes the redundant "A reminder about the implementation" section and folds the cursor mechanism into Current position. I accept that.
- Every output removes the padding in the opening section and the duplicate row-count sentence.
- Every output keeps all of the case's key points:
  - **Approval and pilot scope:** approval for the pilot only, not a general release; no approval recorded; green checks don't count as approval; twelve internal accounts.
  - **Time limits:** the 01:00–02:00 UTC window; the forty-minute pilot; no batch that would finish after 02:00, but exactly 02:00 is allowed.
  - **Stop conditions:** one row-count mismatch stops new batches, and a later match doesn't cancel it. Latency over 90 s for three consecutive batches stops new batches; exactly 90 s doesn't count, and a faster batch resets the count.
  - **Lease and acknowledgement:** don't release the lease while an acknowledgement is outstanding, even if health checks pass. Settle the batch status before releasing, even after the window ends.
  - **Rollback:** reverting the package doesn't restore the cursor. Confirm the batch status with the destination operator, reconcile the cursor, then release the lease; escalate if the status is unknown.
  - **Evidence:** keep the cursor snapshot and comparison files until the incident owner authorizes release; a clean rollback is not that authorization.
  - **After rollback:** accounts stay on the existing release policy, and an earlier approval doesn't allow a restart.
  - **Handoff:** the record fields, explicit acceptance before the outgoing shift leaves, keeping the token, and the note that the source gives no reason for keeping the token separately.
  - **Next decision:** cross-region behavior and production-sized data stay untested.
- Deployment and Rollback each keep their own safeguards (lease, evidence and the health-check warning), so each still works when read on its own.
- Word-count changes below use `WORD-COUNTS.json` (source 1,207). Every output is shorter.

### Original-body

**1. `20261022T194147448Z-cw-final-codex-long-handoff-original-body-d671ddc4-19d5-4189-95f9-d8c3cba752c0-sigu273f` — original-body, repetition 1 — 894 words (−313)**
- **F1 — met.** It correctly groups the untested conditions: "These tests did not cover a destination outage during acknowledgement, a cross-region outage or a production-sized dataset."
  - *Precision note:* "the incoming shift explicitly accepts this record and keeps the write lease token with the incident record" drops the source's "until it accepts the handoff" end point. Deployment still says "keep its token with the incident record until handoff is accepted", so nothing is contradicted, and the change only makes the duty stricter. Not consequential.
- **F2 — met.** The opening says "Those sections repeat essential safeguards so each works independently". Rollback begins "Incident responders may begin here." Both entry points are fully self-contained.
- **F3 — met.** Short consolidated paragraphs and clear "because" links ("Do not release the lease…: a second worker could start…"). No reading burden.
- **Overall: Pass.**

**2. `20261022T194535385Z-cw-final-codex-long-handoff-original-body-7cfa035a-7f94-4854-a4d5-671404ca9e24-ycbzdmah` — original-body, repetition 2 — 879 words (−328)**
- **F1 — met.** Evidence limits are kept: "These controlled interruptions did not test a destination outage during acknowledgement… do not establish safety under those conditions."
- **F2 — met.** The opening says "operational sections are self-contained where readers must act". Rollback has no pointer of its own, but the opening and the section's complete safeguards cover it.
- **F3 — met.** Compact and well connected.
- **Overall: Pass.**

**3. `20261022T194701944Z-cw-final-codex-long-handoff-original-body-d3edc56f-0ad2-468b-ad72-5fd73473fe4a-bbzyeo3i` — original-body, repetition 3 — 883 words (−324)**
- **F1 — met.** The Deployment checklist ("the pilot is approved; … the staffed window remains open") followed by "If any condition fails, arrange another staffed window" keeps the start conditions. Presence of both people is still required in the lead sentence.
- **F2 — met.** It has the entry-point opening, and the bulleted mismatch actions ("stop new batches immediately; retain both comparison files; investigate before resuming, even if the next comparison succeeds") are easy to act on.
- **F3 — met.** Lists for evidence, preconditions, mismatch actions and the handoff record make it easy to scan.
- **Overall: Pass.**

**4. `20261022T203848285Z-cw-final-codex-long-handoff-original-body-78629f22-d979-4d64-9d0a-9812ef5f526d-qso2emjy` — original-body, repetition 4 — 898 words (−309)**
- **F1 — met, with two precision notes.**
  - "All eighty staging exports had matching source and destination row counts" drops the source's "that completed" qualifier. It is the only output that does. The source never says any other exports existed, so this doesn't introduce a false fact.
  - "Version 2.5 advances the cursor only after acknowledgement" drops "whole/complete batch". The previous sentence refers to the destination acknowledging "a batch", and the dry-run caveat about a "partially acknowledged production batch" is kept.
  - Neither change affects the pilot decision or any action.
- **F2 — met.** The opening names both entry points and says both operational sections "contain the safeguards needed to act independently".
- **F3 — met.**
- **Overall: Pass.**

**5. `20261022T204041413Z-cw-final-codex-long-handoff-original-body-d5e0cae0-a661-4c43-a81e-8ee7aa9ef4a2-d__6pf6n` — original-body, repetition 5 — 1,007 words (−200)**
- **F1 — met.** "The forty-minute pilot requires approval; this handoff does not request a general release" keeps the scope.
- **F2 — met.** It keeps the "How this handoff is used" section and the "Incident responders may enter this section directly" pointer.
- **F3 — met.** This is the least tightened output. It keeps one sentence per line and the source's leftover restatement ("…remain untested after a successful twelve-account pilot. / Passing the pilot does not supply evidence for those untested cases."). That is a minor quality observation; it doesn't add a meaningful reading burden.
- **Overall: Pass.**

### Revised-body

**6. `20261022T194313605Z-cw-final-codex-long-handoff-revised-body-23a09fab-04c5-469d-99ac-35ad09c6bc92-sxs0jm27` — revised-body, repetition 1 — 974 words (−233)**
- **F1 — met.** "A single row-count mismatch still requires a stop even when latency is normal" keeps the two conditions independent.
- **F2 — met.** The opening says "Those sections repeat critical safeguards so they work as independent entry points"; the Rollback pointer is kept.
- **F3 — met.** Close to the source's layout (one sentence per line), with the padding removed.
- **Overall: Pass.**

**7. `20261022T194428548Z-cw-final-codex-long-handoff-revised-body-c5b68e9e-fdfe-4665-8ca8-3b031811b3b9-fnd0hr89` — revised-body, repetition 2 — 1,001 words (−206)**
- **F1 — met, with one precision note.** "…indicating that the implementation behaves as intended in staging" is slightly firmer than the source's "useful indication… encouraging". It is limited to staging and followed straight away by the untested conditions, so it doesn't overstate.
- **F2 — met.** The top-of-document orientation is removed entirely, but Rollback keeps "Incident responders may enter this section directly from an alert", and both operational sections keep every safeguard.
- **F3 — met.** It is the closest to the source text. It keeps the source's awkward "A worker that has sent a batch… is still outstanding" and the duplicated sentence about untested cases. These are minor.
- **Overall: Pass.**

**8. `20261022T194822220Z-cw-final-codex-long-handoff-revised-body-7db7853d-d29b-435f-8738-98d45311dcf1-74o1boxw` — revised-body, repetition 3 — 876 words (−331)**
- **F1 — met, with one precision note.** "Rae must confirm the incident channel is staffed, and the twelve selected accounts must be the approved internal pilot accounts" no longer names Rae as the person who confirms the accounts. The requirement still stands, so this isn't consequential.
- **F1 (continued).** "Do not release the lease while a batch acknowledgement is outstanding, even if the worker health check passes" keeps the outstanding-state point.
- **F2 — met.** There is no opening orientation, but Rollback starts "Incident responders may enter here directly from an alert."
- **F3 — met.** Compact paragraphs.
- **Overall: Pass.**

**9. `20261022T203714097Z-cw-final-codex-long-handoff-revised-body-11968518-0846-420d-a484-13f6aaad061b-5ihe8wsy` — revised-body, repetition 4 — 887 words (−320)**
- **F1 — met, with one precision note.** "Approve a forty-minute pilot…" turns the team's recommendation into a direct request under the "Status and request" heading. It is paired with "This is not a general-release request. No approval has been recorded," so it doesn't imply that approval exists.
- **F2 — met.** The opening covers both entry points and why the scope is limited; Rollback has its own pointer. The monitoring bullets put both stop conditions side by side, with "These conditions are independent."
- **F3 — met.** Probably the easiest to scan of the ten.
- **Overall: Pass.**

**10. `20261022T204201822Z-cw-final-codex-long-handoff-revised-body-27243e3b-53ac-4683-8414-639615b86cba-5cc_30cg` — revised-body, repetition 5 — 846 words (−361, the shortest)**
- **F1 — met.** It has the same passive-voice account check as #8 ("the twelve selected accounts must be the approved internal pilot accounts"). Not consequential.
- **F2 — met.** The numbered "Before enabling 2.5: 1. Save… 2. Acquire the export write lease" turns the pre-change steps into a sequence that is easy to follow. There is no opening orientation; Rollback starts "Incident responders may begin here."
- **F3 — met.** "stop on either stated condition" in the closing summary is a fine back-reference because the two conditions are listed side by side.
- **Overall: Pass.**

### Condition comparison (first pass)

| Condition | Pass | Fail | Insufficient | Words (source 1,207) |
|---|---|---|---|---|
| original-body | 5 (reps 1–5) | 0 | 0 | 894, 879, 883, 898, 1,007 |
| revised-body | 5 (reps 1–5) | 0 | 0 | 974, 1,001, 876, 887, 846 |

**Repeated behavior across both conditions**
- All ten keep every key point and leave both entry points self-contained.
- Both conditions have one near-source, one-sentence-per-line output (original-body #5; revised-body #1 and #2) as well as more consolidated ones.

**Differences between the conditions**
- **Up-front entry-point orientation:** all five original-body outputs keep it. Revised-body #2, #3 and #5 drop it and rely on the pointer inside Rollback. The practical cost is small, since every Rollback section keeps its pointer and Deployment is self-contained, but original-body is more consistent here.
- **Lists and numbered steps:** revised-body uses them more often (#4 and #5) and has the shortest output (#5) plus the easiest-to-scan one (#4). Original-body has one list-based output (#3).
- **Least-tightened outputs:** each condition has one about 1,000 words long (original-body #5, revised-body #2). Revised-body has two near-source outputs (#1, #2) to original-body's one.
- **Precision notes are single-output observations:** original-body #4 (dropped "completed"); original-body #1 (token time limit); revised-body #2 (firmer "indicating"); revised-body #4 (recommendation turned into a request); revised-body #3 and #5 (passive account check).

**Bottom line:** I see no consequential difference in effectiveness or quality between the conditions. Both are 5/5 passes with similar spread. Five repetitions per condition are diagnostic only. Without a no-CW control, these results say nothing about whether either skill body caused any of this.

Now reading the prior assessment for comparison.
