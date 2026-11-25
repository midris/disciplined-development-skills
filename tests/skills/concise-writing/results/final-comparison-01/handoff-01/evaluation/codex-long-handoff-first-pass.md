## Independent first-pass assessment (before reading prior-assessment.md)

**Disclosure.** I'm a fresh-context Opus reviewer. That is a different model family from the active Codex assessor and the same family as Claude subjects; the subjects in this index are Codex `gpt-5.6-sol`. I could see the condition labels, so this review is independent but not blinded. Before any judgment I read in full: EVALUATION-INDEX.json, SETUP.md, sources/TASK.md, sources/report.md, policy.txt, criteria.md, INTERPRETATION.md, WORD-COUNTS.json, MECHANICAL-CHECKS.json (contents: `{}`) and all six outputs. I did not open prior-assessment.md, skill bodies, descriptions or traces. Everything was read-only and nothing was executed.

**Source anchors checked in every output:**
- Pilot approval not yet recorded, and a green job doesn't replace it
- Twelve internal accounts, 01:00–02:00 UTC window, forty-minute pilot
- A batch estimated to finish exactly at 02:00 is allowed
- One mismatch stops new batches, and a later match doesn't cancel it
- Latency over 90 s for three consecutive batches; exactly 90 s doesn't count, and a faster batch resets the count
- Don't release the lease while an acknowledgement is outstanding, even if the health check passes; the end of the window doesn't override this
- Rollback doesn't restore the cursor: confirm status with the destination, reconcile, then release; escalate if status is unknown
- Keep the snapshot and comparison files until the incident owner authorizes release
- No restart on the earlier approval
- Handoff record, token held until acceptance (reason not given, requirement still in force)
- Cross-region and production-sized cases remain untested
- Wider release is a separate decision

Source length is 1207 words; all six outputs are shorter.

### Run 1: `20261022T194147448Z-cw-final-codex-long-handoff-original-body-d671ddc4-19d5-4189-95f9-d8c3cba752c0-sigu273f`, original-body, rep 1 (894 words, −313)

- **F1 met.**
  - The opening says operators "can go directly to Deployment before the window; incident responders can go directly to Rollback after an alert."
  - The implementation reminder is merged into Current position: "keeping an unacknowledged batch available for retry once its status is known."
  - The evidence limits are kept: "did not cover a destination outage during acknowledgement, a cross-region outage or a production-sized dataset."
  - The timing rules are kept: "one estimated to finish exactly at 02:00 is permitted… even after the window ends."
  - Precision note: Handoff merges two rules into "Before the outgoing shift leaves, the incoming shift explicitly accepts this record and keeps the write lease token with the incident record." This drops the "until it accepts" end point in that sentence. Deployment still says "keep its token with the incident record until handoff is accepted," so the condition isn't lost.
  - The explicit "do not begin" is dropped, but "Before starting, both must be present… arrange another staffed window" keeps the gate.
- **F2 met.**
  - Both entry points are kept, and the opening says those sections "repeat essential safeguards so each works independently."
  - Rollback starts "Incident responders may begin here" and keeps the stop, reconcile-then-release, escalate, retain-files and no-restart steps.
- **F3 met.** Clear prose paragraphs, padding and the duplicate eighty-export sentence are removed, and the reminder section is absorbed without loss.
- **Overall: pass.**

### Run 2: `20261022T194313605Z-cw-final-codex-long-handoff-revised-body-23a09fab-04c5-469d-99ac-35ad09c6bc92-sxs0jm27`, revised-body, rep 1 (974 words, −233)

- **F1 met.**
  - The latency rules stay exact: "Ninety seconds exactly does not meet this threshold. A faster intervening batch resets the consecutive-batch count."
  - Rollback says "a health check does not establish batch status."
  - Dry run: "package availability is not evidence of data recovery" faithfully restates source line 40.
  - Precision note: "All eighty staging exports completed with matching source and destination row counts" could suggest every staging export completed. The source restricts the claim to "the eighty staging exports that completed," but its own first sentence is just as loose. I judge this not consequential to the pilot decision, because all the limits are kept.
- **F2 met.**
  - The entry-point lines are kept nearly word for word, and "Those sections repeat critical safeguards so they work as independent entry points" is added.
  - Rollback keeps "Incident responders may enter this section directly from an alert."
- **F3 met.** One sentence per line, as in the source. The padding, duplicate sentence and reminder section are removed, and nothing consequential is restated without purpose.
- **Overall: pass.**

### Run 3: `20261022T194428548Z-cw-final-codex-long-handoff-revised-body-c5b68e9e-fdfe-4665-8ca8-3b031811b3b9-fnd0hr89`, revised-body, rep 2 (1001 words, −206)

- **F1 met.**
  - It keeps "do not begin; arrange another staffed window." This is the only output that keeps the explicit "do not begin."
  - "indicating that the implementation behaves as intended in staging" is equivalent to the source's "useful indication… in staging," and the untested-condition limits follow immediately.
  - "Passing the pilot does not supply evidence for those untested cases" is kept.
- **F2 met.**
  - The "How this handoff is used" section is removed entirely, so no opening orientation names the Deployment and Rollback entry points.
  - Rollback still opens "Incident responders may enter this section directly from an alert," and Deployment is self-contained (presence, approval, window, lease, artifacts). That makes this a small orientation loss, not a practical one.
- **F3 met.** This is the least-tightened output. It is close to the source wording, including the awkward "A worker that has sent a batch… is still outstanding." Formatting is mixed: mostly one sentence per line, with the dry-run and token paragraphs merged. It is still easy to scan and has no purposeless restatement; the duplicate sentence, padding and reminder are gone.
- **Overall: pass.**

### Run 4: `20261022T194535385Z-cw-final-codex-long-handoff-original-body-7cfa035a-7f94-4854-a4d5-671404ca9e24-ycbzdmah`, original-body, rep 2 (879 words, −328)

- **F1 met.**
  - Evidence says "the results do not establish safety under those conditions."
  - Handoff says "Keep the write lease token with the incident record until the incoming shift accepts the handoff… the requirement remains in force."
  - "Release operators should start with Deployment" is more prescriptive than the source's "normally open," but has no consequence.
- **F2 met.**
  - The opening keeps both entry points: "operational sections are self-contained where readers must act."
  - Rollback drops its in-section "may enter directly" line, but it opens with the stop-batches step and keeps every safeguard.
- **F3 met.** Concise paragraphs with clear section flow.
- **Overall: pass.**

### Run 5: `20261022T194701944Z-cw-final-codex-long-handoff-original-body-d3edc56f-0ad2-468b-ad72-5fd73473fe4a-bbzyeo3i`, original-body, rep 3 (883 words, −324)

- **F1 met.**
  - The evidence is in bullets, including "This did not test a destination outage during acknowledgement" and "The staging results do not establish safety under untested conditions."
  - Precision note: Deployment turns the preconditions into a checklist ("the pilot is approved; the incident channel is staffed; the twelve accounts are the approved internal pilot accounts; and the staffed window remains open") followed by "If any condition fails, arrange another staffed window." The source applies that remedy explicitly only to absent approval, an unavailable person or an ended window. Extending it to the channel and account checks is conservative and consistent with those checks being start preconditions, so it isn't a consequential distortion.
  - The opening drops "before the window" and "after an alert."
- **F2 met.**
  - The opening says the entry-point sections "repeat critical safeguards so each works independently."
  - The mismatch bullets are actionable: "stop new batches immediately; retain both comparison files; investigate before resuming, even if the next comparison succeeds."
  - The handoff record is a list, which makes it easier to complete.
- **F3 met.** It has the best scannability of the six. Bullets are used where the reader acts or checks, and the reasoning stays in prose.
- **Overall: pass.**

### Run 6: `20261022T194822220Z-cw-final-codex-long-handoff-revised-body-7db7853d-d29b-435f-8738-98d45311dcf1-74o1boxw`, revised-body, rep 3 (876 words, −331)

- **F1 met.**
  - The lease rule is merged into one sentence: "Do not release the lease while a batch acknowledgement is outstanding, even if the worker health check passes." This keeps the health-check boundary.
  - Precision note: "Rae must confirm the incident channel is staffed, and the twelve selected accounts must be the approved internal pilot accounts" drops Rae as the person who confirms the accounts. The requirement is kept, and Rae owns the deployment.
- **F2 met.**
  - Like run 3, the opening orientation section is removed. Rollback keeps "Incident responders may enter here directly from an alert," and both sections are self-contained.
- **F3 met.** Compact paragraphs and a clear sequence.
- **Overall: pass.**

### Condition comparison (Codex only)

| Condition | Pass | Fail | Insufficient | Words |
|---|---|---|---|---|
| original-body (runs 1, 4, 5) | 3 | 0 | 0 | 894, 879, 883 |
| revised-body (runs 2, 3, 6) | 3 | 0 | 0 | 974, 1001, 876 |

**What repeated within a condition:**
- **original-body:** all three outputs moved the orientation into the opening line and said the operational sections work on their own. All three rewrote the text into consolidated prose (run 5 also used bullets) and stayed in a narrow 879–894 word range.
- **revised-body:** behavior varied. Two of three (runs 3 and 6) removed the opening orientation and relied on Rollback's in-section line. Two of three (runs 2 and 3) kept the source's one-sentence-per-line layout and much of its wording. Lengths varied more (876–1001).

**Single-output observations (no factor changes):**
- Run 3 is the only output that keeps "do not begin" and is the least tightened.
- Run 5 has the most usable checklist layout, with a conservatively extended remedy.
- Run 1 merges the token sentence; run 2 has the "All eighty" wording; run 6 drops who confirms the accounts.

**Quality reading:**
- Both conditions reach the threshold in every repetition. The original-body outputs are slightly more consistent at keeping the entry-point orientation and at consolidating. The revised-body outputs are more conservative on wording, and run 3 keeps the explicit "do not begin."
- Neither condition shows a consequential effectiveness advantage. Three repetitions are diagnostic only, and with no no-CW control nothing here supports a causal claim. If the owner judges the conditions equivalent, the shorter-SKILL.md tie-break applies outside this packet.

I'm now reading the prior assessment for comparison.
