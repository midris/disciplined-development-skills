I've read all source, policy, criteria, interpretation, count and check files and all 15 outputs. Here is my first-pass assessment, given before I open prior-assessment.md.

---

# First-pass independent assessment: long-handoff (Codex `gpt-5.6-sol`, low effort)

**Disclosure:** This review is independent, but it is not blinded because the condition labels are visible. It covers output quality only. I make no claim about whether the skill was invoked or the process was followed.

**Evidence base:** I read in full `sources/report.md`, `sources/TASK.md`, `policy.txt`, `criteria.md`, `INTERPRETATION.md`, `WORD-COUNTS.json` and `MECHANICAL-CHECKS.json`, plus all 15 outputs.
- **Evidence gap:** The criteria and interpretation refer to `boundary-checks.md`, the holistic context review and owner-ruling records. None of these is in the packet, so I could not apply them beyond what the supplied text says.
- `MECHANICAL-CHECKS.json` is empty (`{}`).
- The task's "brief completion message" is not among the saved artifacts, so it is not assessed.

**Readers and anchors used:**
- Readers: release operators (entering at Deployment), incident responders (entering at Rollback) and the incoming shift.
- Anchors checked in every output:
  - approval not yet recorded, and green checks are not approval
  - 12-account, pilot-only scope; 01:00–02:00 UTC window; 40-minute pilot
  - a batch may start if estimated to finish exactly at 02:00
  - one mismatch stops new batches, and a later match does not cancel it
  - latency stop: over 90 s for three consecutive batches; exactly 90 s does not count; a faster batch resets the count
  - the lease is held until acknowledgement is settled, even past the window
  - cursor reconciliation goes through the destination operator, with escalation if status is unknown
  - artifacts are kept until the incident owner authorizes release
  - health checks are not proof of acknowledgement or matching counts
  - after a rollback, the old approval does not authorize a restart
  - the handoff record, the token rule (whose reason the source doesn't explain), and untested conditions after the pilot

**Source length:** 1,207 words (`report.md`); TASK.md is 68.

## Recurring precision observations (not failures)

These patterns appear across conditions. I checked each one in full context.

- **P1 – "has not tested a destination outage during acknowledgement"**
  - Found in control-1, 3, 4, 5; original-1, 5; candidate-2, 3.
  - The source only says the four interruptions "were … not a destination outage during acknowledgement" and lists cross-region and production-sized data as "not exercised."
  - Reading this as "untested" is a reasonable inference that stays within the evidence's limits. It doesn't overstate safety.
- **P2 – "All eighty staging exports completed with matching…"**
  - Found in control-2, candidate-4, candidate-5.
  - The source says "every one of the eighty staging exports that completed," which leaves open whether some exports didn't complete. This wording can suggest all exports completed.
  - The source never says any failed, so this is a minor precision loss, not a consequential distortion.
  - Most other outputs use the faithful "All 80 completed staging exports."
- **P3 – "If any condition is unmet … arrange/schedule another staffed window" without an explicit "do not begin"**
  - Found in control-3, original-1, original-5, candidate-2, candidate-3.
  - Rescheduling clearly implies not starting. No loss.

## Per-output judgments

| Run (short ID) | Condition | Rep | F1 | F2 | F3 | Overall | Words (Δ vs 1,207) |
|---|---|---|---|---|---|---|---|
| …062242372Z…a595cf16 | control | 1 | met | met | met | **pass** | 757 (−450, shorter) |
| …063626456Z…dceae98a | control | 2 | met | met | met | **pass** | 1,000 (−207, shorter) |
| …064033331Z…9a435ac6 | control | 3 | met | met | met | **pass** | 791 (−416, shorter) |
| …064301250Z…7214e72b | control | 4 | met | met | met | **pass** | 829 (−378, shorter) |
| …065150726Z…abdb2f3c | control | 5 | met | met | met | **pass** | 789 (−418, shorter) |
| …062514644Z…bf0742b9 | original | 1 | met | met | met | **pass** | 860 (−347, shorter) |
| …062817943Z…633234ad | original | 2 | met | met | met | **pass** | 974 (−233, shorter) |
| …064155137Z…60b74f6e | original | 3 | met | met | met | **pass** | 997 (−210, shorter) |
| …064437597Z…d04b0974 | original | 4 | met | met | met | **pass** | 1,000 (−207, shorter) |
| …064835849Z…7bcc7b6d | original | 5 | met | met | met | **pass** | 825 (−382, shorter) |
| …062646311Z…50e4359a | candidate-targeted-examples | 1 | met | met | met | **pass** | 954 (−253, shorter) |
| …063447215Z…c7cc739c | candidate-targeted-examples | 2 | met | met | met | **pass** | 889 (−318, shorter) |
| …063852480Z…d4dc1d17 | candidate-targeted-examples | 3 | met | met | met | **pass** | 883 (−324, shorter) |
| …064702796Z…479dcfbb | candidate-targeted-examples | 4 | met | met | met | **pass** | 1,011 (−196, shorter) |
| …065006851Z…966718ef | candidate-targeted-examples | 5 | met | met | met | **pass** | 970 (−237, shorter) |

The full run IDs are in `EVALUATION-INDEX.json`, orders 1–15. Every output contains every anchor listed above, so the evidence below covers only what differs between outputs.

### Controls

**control-1 (757): pass**
- **Strengths:**
  - It leads with "Tonight's decision": the 40-minute, 12-account pilot, "not … general release," "no approval has yet been recorded," and green checks are not approval.
  - Deployment preconditions are a checklist that includes approval (lines 19–25).
  - Pre-enable steps are numbered.
  - The two stop conditions are bullets, with the exact-90 s and reset rules and "independent" (lines 41–46).
  - Rollback is four ordered steps headed "Incident responders may begin here." It covers escalation and "Do not infer status from a worker health check," plus "a clean package rollback is not authorization" and the restart prohibition (lines 52–61).
  - This is the clearest layout for an urgent handoff.
- **Weaknesses:**
  - It drops the reason for keeping artifacts: the source says they show whether a later mismatch came from source selection, cursor advancement or acknowledgement (lines 51 and 99). That reason appears in neither Deployment nor Rollback.
  - Deployment no longer says why the lease must be held ("a second worker could start from an unresolved cursor"). Rollback keeps "risks replaying or omitting a batch."
  - These count against F2 only as weaknesses. Each instruction is intact and carries its gate: "even if the deployment appears healthy," owner authorization, and "clean package rollback is not authorization." The reader can still act correctly, and nobody has to make a judgment that depends on the missing reason.

**control-2 (1,000): pass**
- **Strengths:**
  - It is the most complete control.
  - It keeps both artifact rationales (lines 36, 60) and the Deployment-side lease reason (line 38).
  - "The staffed window is still open" is added to the precondition checklist.
- **Weaknesses:**
  - It keeps both "Current position" and the separate "A reminder about the implementation" (line 52), so the cursor mechanism is explained twice, once far from Rollback.
  - Under interpretation boundary C, that is a minor residual redundancy, not a consequential burden: the section is short and accurate, and nothing breaks.
  - P2 applies to line 19.
  - It is the least compressed control.

**control-3 (791): pass**
- **Strengths:**
  - Status bullets make "**not yet recorded**" approval very visible (lines 5–9).
  - It has a checklist structure, numbered Rollback steps, and a "**Tonight:**" summary.
- **Weaknesses:**
  - Rollback drops "A clean package rollback is not authorization" (line 59). Retention is still gated on "until the incident owner authorizes their release after reconciliation," so the safeguard holds, but its explicit warning against the green-dashboard temptation is weaker.
  - It drops the "green dashboard isn't permission to discard comparison files" sentence. Deployment keeps "even if the deployment appears healthy."
  - It drops the artifact rationale entirely and the Deployment-side lease reason.
  - P3 applies.
  - Even so, F1 and F2 are met: every gate and authority is intact, and the losses are explanatory, not operational.

**control-4 (829): pass**
- **Strengths:**
  - It keeps the Deployment lease rationale (line 35) and the Rollback artifact rationale (line 59).
  - Health checks "cannot justify releasing an unresolved lease or discarding evidence" (line 44).
- **Precision notes:**
  - Step 3, "Keep the artifacts and lease token with the incident record until handoff is accepted," adds a storage location for artifacts that the source doesn't state. The next sentence sets the correct, longer retention gate, so this isn't consequential.
  - "Jo records" replaces the source's "Jo confirms" the observations, which is harmless.
- **Weakness:** The artifact rationale is absent from Deployment, but it is present in Rollback.

**control-5 (789): pass**
- **Strengths:**
  - It has a five-item precondition checklist, including "Rae and Jo are present" and "staffed window has not ended."
  - The five-step Rollback includes the escalation step.
  - "not approval … for a restart after an incident" (line 5) is supported by source line 102.
- **Weaknesses:**
  - It has no artifact rationale.
  - It has no Deployment-side lease reason.
  - The step-3 artifact-location precision note matches control-4.
  - It has no closing "tonight" summary. The opening section covers the decision, so this is acceptable.

### Original (skill)

**original-1 (860): pass**
- **Strengths:**
  - A one-line orientation says Deployment and Rollback "repeat critical controls so they stand alone."
  - Both entry points keep their causal reasons: artifacts (lines 23 and 43), lease and second worker (line 25), replay/omit (line 41).
  - The green dashboard is not permission to discard files (line 35).
  - It keeps the "Tonight" summary.
- **Weaknesses:**
  - The Rollback section has no in-section "responders may begin here." The top-of-document orientation covers this.
  - P1 and P3 apply.
  - It keeps a prose layout with no checklists, so preconditions are buried in one sentence (line 21). It is still easy to read.

**original-2 (974): pass**
- It is a light edit that keeps one sentence per line.
- It removes the source's padding: the generic intro, the duplicated row-count sentence, the "encouraging" sentence and the separate implementation reminder.
- It keeps every safeguard and both rationales.
- It is faithful throughout. Line 21 keeps the source's "Eighty staging exports completed…"
- **Weakness:** Compression is modest, and some sentence-level wording is unchanged. Neither is a burden.

**original-3 (997): pass**
- It is the lightest edit. It shortens the intro, merges the duplicate row-count sentences, drops "encouraging," removes the implementation reminder, and merges the dry-run sentences.
- "Current position" still has the source's slightly redundant three-sentence mechanism description (lines 9–11).
- It keeps "a missing explanation is not a cancellation."
- **F3 is met.** Removing the main padding blocks leaves the operational repetition, which serves the entry points. However, this run does little "tightening" beyond that.

**original-4 (1,000): pass**
- It is a light edit similar to original-2.
- The orientation now says why the sections repeat.
- It keeps all rationales and the green-dashboard discard warning.
- Line 22 drops "between batches," but line 21 states it.
- It is faithful, with modest compression.

**original-5 (825): pass**
- **Strengths:**
  - Evidence and limits are bullets, which makes the untested conditions especially clear (line 16).
  - Pre-enable steps are numbered.
  - Stop conditions are bullets.
  - All rationales are kept at both entry points.
- **Precision note:**
  - The handoff now reads "Before the outgoing shift leaves, the incoming shift explicitly accepts the record and keeps the lease token with the incident record" (line 63). This blurs the source's "until it accepts the handoff" timing.
  - Deployment line 27 keeps "until handoff is accepted," so the duration survives in the document.
- P1 and P3 apply.
- It is the most usable skill output, with structure comparable to the controls.

### Candidate-targeted-examples (skill)

**candidate-1 (954): pass**
- It removes the opening "How this handoff is used" entirely. The Rollback entry note survives (line 66), and Deployment stands alone.
- Deployment merges the lease reason and the health-check caveat into one sentence (line 40).
- It keeps all rationales and the "For tonight" summary.
- Sentence-per-line prose with little restructuring.
- Faithful.

**candidate-2 (889): pass**
- Its orientation says each operational section "includes the warnings needed to act safely."
- The precondition checklist includes approval.
- All rationales are present (lines 29, 31, 47, 49).
- P1 and P3 apply.
- It reads smoothly and is well balanced.

**candidate-3 (883): pass**
- It is close to candidate-2.
- Evidence is consolidated into one paragraph that keeps the "controlled interruptions did not test … during acknowledgement" qualification (line 13).
- All rationales are kept at both entry points.
- P1 and P3 apply.

**candidate-4 (1,011): pass**
- It is the longest output and the lightest edit.
- Line 22 keeps the source's "indicating that the implementation behaves as intended in staging." This is a slight strengthening of the source's "useful indication," but the limits that follow keep it bounded to staging, so it is not an unsupported claim.
- P2 applies to the same line.
- It keeps the line-per-sentence layout and all safeguards and rationales.
- F3 is met because the source's purposeless blocks (the generic intro and implementation reminder) are gone.
- Among the skill outputs, this run combines the least compression with one of the surviving source padding phrases.

**candidate-5 (970): pass**
- It is a light edit.
- It keeps the source's redundant mechanism sentences (lines 11–13).
- It drops the explicit "keep package availability and data recovery separate" line, but line 30 states the distinction directly ("installs… but not that reversal restores the correct cursor").
- P2 applies to line 23.
- All operational safeguards and rationales are present.

## Condition comparison

**Functional pass counts** (case: long-handoff; runtime: Codex CLI 0.163.0, `gpt-5.6-sol`, low effort; single stratum):

| Condition | Pass | Fail | Insufficient | F1 met | F2 met | F3 met | Mean words (range) |
|---|---|---|---|---|---|---|---|
| control (no CW) | 5/5 | 0 | 0 | 5 | 5 | 5 | 833 (757–1,000) |
| original | 5/5 | 0 | 0 | 5 | 5 | 5 | 931 (825–1,000) |
| candidate-targeted-examples | 5/5 | 0 | 0 | 5 | 5 | 5 | 941 (883–1,011) |

(There are no N3 cases in scope.)

**Quality differences behind the tied pass counts:**

1. **Causal explanations kept at each entry point (a recurring pattern, likely to recur).**
   - All 10 skill outputs keep the artifact-retention reason and the lease or second-worker reason within the sections where readers act.
   - Controls do this inconsistently. Control-1, control-3 and control-5 drop the artifact reason entirely and give the lease reason only in Rollback. Control-4 keeps the artifact reason only in Rollback. Only control-2 matches the skill outputs.
   - This is the clearest difference between conditions. It matches this case's stated risk: "indiscriminate deduplication can remove point-of-use safeguards."
   - It is a difference in explanatory quality, not a threshold failure, because every gate stayed intact.
2. **Restructuring for urgent use (recurring in controls).**
   - Four of five controls lead with a "Tonight's decision" or status block, use precondition checklists and give Rollback numbered steps.
   - Among skill outputs, only original-5 and partly candidate-2 restructure. The rest keep the source's prose and line-per-sentence layout.
   - For a reader with 20 minutes before handoff, the control layouts are faster to scan.
3. **Compression.**
   - Controls are about 100 words shorter on average.
   - Several skill runs are light edits (original-3, original-4, candidate-4, candidate-5; all 970 words or more) that keep minor source redundancy, such as the triple mechanism description and "indicating … as intended."
   - Length doesn't change any judgment.
4. **Precision slips** happen at similar, low rates across conditions. P2 appears once in the controls and twice in the candidates. Control-4 and control-5 add the artifact-location detail. Original-5 blurs the token timing. None is consequential.
5. **Differences between the two skill versions.**
   - None is meaningful. Both versions produce one more-restructured run or so and several light edits, and both preserve the rationales.
   - Candidate-4 is the weakest skill-bearing output on concision. Original-5 and candidate-2 are the strongest.

**Conclusions on CW contribution:**
- At the threshold level, CW shows no contribution: the controls pass 5/5.
- Descriptively, CW-bearing outputs more reliably keep the reasoning behind safeguards at each entry point. Controls more often produce the more scannable, more compressed layout, at the cost of some of that reasoning.
- So CW trades layout and compression gains for fidelity to the source's explanations. It is not a clear overall improvement.
- With n=5 per condition and one runtime stratum, I can't call either skill version reliably better than the control or than each other.
- Both drafts are equivalent in this sample. Neither is preferable to the original skill version.

---

Now reading the prior assessment.
