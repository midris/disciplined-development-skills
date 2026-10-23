# Independent review: Aster long-handoff, Codex subjects (gpt-5.6-sol, low effort)

**How this review was done.** I'm a fresh-context Opus reviewer. That's a different model family from the active assessor (Codex) and the same family as the Claude subjects. The review is independent but not blinded: I could see the condition labels. I worked read-only.

**What I read before judging.** EVALUATION-INDEX.json, SETUP.md, sources/TASK.md, sources/report.md, policy.txt, criteria.md, INTERPRETATION.md, WORD-COUNTS.json, MECHANICAL-CHECKS.json (which is empty, `{}`) and all six outputs in full. I have not opened or searched prior-assessment.md yet.

**Word counts.** The source report.md is 1207 words. Every output is shorter:

| Output | Words | Change |
|---|---|---|
| original-body-1 | 825 | −382 |
| original-body-2 | 1020 | −187 |
| original-body-3 | 826 | −381 |
| original-examples-1 | 1018 | −189 |
| original-examples-2 | 852 | −355 |
| original-examples-3 | 876 | −331 |

**Source anchors I checked in every output:**
- **Approval and scope:** pilot-only approval, none recorded yet; green checks don't count as approval.
- **Pilot limits:** twelve internal accounts, the staffed 01:00–02:00 UTC window, forty minutes.
- **Time rule:** don't start a batch estimated to finish after 02:00; exactly 02:00 is allowed; keep the lease past the window's end.
- **Mismatch stop:** one mismatch stops new batches, and a later match doesn't cancel it.
- **Latency stop:** over 90 s for three consecutive batches; exactly 90 s doesn't count; a faster batch resets the count; independent of the mismatch stop.
- **Health checks:** a passing check isn't proof of acknowledgement or matching counts.
- **Lease and acknowledgement:** keep the lease while an acknowledgement is outstanding; confirm status, reconcile the cursor, then release; escalate if the status can't be established.
- **Rollback limits:** reverting the package doesn't restore the cursor.
- **Evidence retention:** keep artifacts until the incident owner authorizes release; a clean rollback isn't that authorization.
- **Restart:** stay on the existing policy and an earlier approval doesn't cover a restart.
- **Shift handoff:** the handoff record, explicit acceptance, and keeping the token until acceptance even though no reason is given.
- **Untested areas:** cross-region and production-sized data.
- **Staging evidence limits:** the interruptions were between batches, not during acknowledgement; the dry run proved the packages install and start, not that data can be recovered.

---

## First-pass assessment

### 1. `20261023T010028571Z-cw-examples-codex-long-handoff-original-body-84254956-1131-49f3-ac79-2b22abb6ddfb-r87lmamj` — original-body, repetition 1 (`outputs/original-body-1.md`, 825 words)

- **F1: met.** All the anchors are kept:
  - Time rule: "Do not start a batch estimated to finish after 02:00 UTC; an estimate of exactly 02:00 is permitted… even after the window ends."
  - Latency: "Exactly 90 seconds does not meet the threshold, and a faster intervening batch resets the count."
  - Staging evidence: "These tests did not cover a destination outage during acknowledgement." This scoping is precise.
  - Rollback limit: "package rollback alone neither restores the cursor nor resolves an outstanding acknowledgement."
  - Restart: "any earlier pilot approval does not authorize a restart after the incident."
  - Token: "The source notes do not explain why… but the requirement remains in force."

  Precision observations, none consequential:
  - "If any condition is unmet … arrange another staffed window" stretches the source's remedy (which applied to approval, staffing and window) to cover the incident-channel and account checks. The effect is cautious and nothing gets started.
  - Rollback steps 1–4 are framed under "If an acknowledgement is outstanding." The source places those steps in the outstanding-acknowledgement paragraph, so this is a reasonable reading.
- **F2: met.**
  - Deployment works on its own. It has a checklist of start conditions, the lease and its token, and "even if the worker health check passes."
  - Rollback works as an entry point: "Incident responders may begin here," numbered keep/confirm/reconcile/release steps, escalation, artifact retention, and "A clean package rollback is not authorization."
  - The "For tonight" summary is kept.
  - The detached "reminder about the implementation" was folded into the opening paragraph, which removes needless reconstruction.
- **F3: met.** The headings are compact and the preconditions and rollback steps are lists, which makes it the most scannable of the six. I found no purposeless restatement.
- **Overall: pass.**

### 2. `20261023T010443848Z-cw-examples-codex-long-handoff-original-body-e915d642-3cfe-4d94-834f-0c24da928d38-_s9iqagw` — original-body, repetition 2 (`outputs/original-body-2.md`, 1020 words)

- **F1: met.** Most source sentences are kept word for word. The edits are faithful:
  - "The dry run establishes package availability, not data recovery."
  - "Releasing it could let a second worker start from an unresolved cursor."
  - "A sent batch without acknowledgement remains outstanding even when its health check passes." The "its" is slightly ambiguous because the source refers to the worker's health check, but the meaning survives.
- **F2: met.**
  - The new opening says "The operational sections therefore repeat critical safety instructions needed by readers who enter there directly," which tells readers how the document is meant to be used.
  - Deployment and Rollback each keep every safeguard, and Rollback keeps "Incident responders may enter this section directly from an alert."
- **F3: met.**
  - Removed: the source's empty opening paragraph, the duplicated row-count sentence, the "encouraging" sentence and the detached implementation reminder.
  - What's left is the source's one-sentence-per-line layout and some minor overlap, such as "remain untested…" followed by "Passing the pilot does not supply evidence for those untested cases." That's a quality observation, not an obscured action or a consequential burden.
  - It's the least tightened body output, which is a weakness in quality rather than a failure.
- **Overall: pass.**

### 3. `20261023T010542011Z-cw-examples-codex-long-handoff-original-body-642bd1f1-d21d-41ce-aa42-7f68113fb5ea-tfemnilb` — original-body, repetition 3 (`outputs/original-body-3.md`, 826 words)

- **F1: met.**
  - Evidence: "Four controlled interruptions between batches… These were not destination outages during acknowledgement."
  - Untested areas, the 02:00 rule, the latency rules, rollback, retention, restart and token are all kept accurately.
  - Precision note: "the twelve accounts must be the approved internal pilot accounts" no longer says Rae is the one who confirms this. The requirement stays and Rae still records the account list at handoff.
- **F2: met, with one quality weakness.**
  - Deployment no longer explains why the artifacts are kept (to tell a source-selection problem from a cursor or acknowledgement problem). That reason now appears only in Rollback: "The files distinguish a source-selection problem from a version-change or acknowledgement problem."
  - The instruction itself and "even if the deployment looks healthy" remain in Deployment, so the action is intact. The reader just has to find the reason in another section.
  - Rollback no longer says "responders may enter here," but the opening line ("incident responders can enter at Rollback") makes up for that, and every Rollback safeguard is present.
- **F3: met.** The prose is compact and the sections connect well.
- **Overall: pass.**

### 4. `20261023T010236240Z-cw-examples-codex-long-handoff-original-examples-8c2a869c-de9a-4e8c-a9f0-a11055daa840-xts9ff2u` — original-examples, repetition 1 (`outputs/original-examples-1.md`, 1018 words)

- **F1: met, with a precision note.**
  - It reads "All eighty completed staging exports had matching source and destination row counts, indicating that the implementation behaves as intended in staging." The source's "useful indication… encouraging" is hedged, so this is slightly firmer.
  - It stays limited to staging, and the very next lines say cross-region and production-sized data are untested and that staging "do[es] not establish safety under either condition." It doesn't communicate a consequential overclaim.
  - Everything else is the source's wording.
- **F2: met.**
  - The "How this handoff is used" section was removed completely. It was meta-orientation, and the operational sections don't depend on it.
  - Rollback keeps "Incident responders may enter this section directly from an alert" and all its safeguards. Deployment is unchanged.
- **F3: met.** It has the same residual line-per-sentence verbosity as body-2, and keeps "a missing explanation is not a cancellation." There's no consequential burden.
- **Overall: pass.**

### 5. `20261023T010330688Z-cw-examples-codex-long-handoff-original-examples-886c9281-ccc8-49a1-ab7c-d3cf7face16d-z4_l5di3` — original-examples, repetition 2 (`outputs/original-examples-2.md`, 852 words)

- **F1: met, with a precision note.**
  - It says "The team has not tested an outage during acknowledgement, a cross-region outage, or a production-sized dataset. Staging results therefore do not establish safety under those conditions." The source says more narrowly that the four interruptions were "not a destination outage during acknowledgement." It explicitly lists only cross-region and production-sized data as unexercised.
  - The listed evidence (80 exports, 4 between-batch interruptions, the package dry run) doesn't include an acknowledgement outage, so the reader comes away with the source's point: staging doesn't cover that case.
  - Adding it to the "do not establish safety" sentence fits the source's reasoning. It isn't a consequential inaccuracy.
- **F2: met.**
  - The opening says "Release operators may enter at Deployment and incident responders at Rollback, so those sections repeat critical constraints where needed."
  - Deployment keeps the artifact rationale, the lease and token, the health-check caveat and the 02:00 rule.
  - Rollback keeps every safeguard.
- **F3: met.** The paragraphs are compact and the logic is connected.
- **Overall: pass.**

### 6. `20261023T010707460Z-cw-examples-codex-long-handoff-original-examples-beb4f08f-e1b3-4357-9760-ccaadd6d16e4-2_zi0zli` — original-examples, repetition 3 (`outputs/original-examples-3.md`, 876 words)

- **F1: met, with three precision notes.**
  1. It generalizes the acknowledgement-outage point the same way as examples-2: "has not tested a destination outage during acknowledgement…"
  2. Rollback says "reverting the package does not restore the cursor" without the source's "by itself." This is the more cautious reading, and the next instruction is to reconcile the cursor.
  3. The Handoff section says "Before the outgoing shift leaves, the incoming shift explicitly accepts the record and keeps the write lease token with the incident record." That merged sentence loses the source's "until it accepts" endpoint locally. Deployment still says "keep its token with the incident record until handoff is accepted," so the whole document keeps the boundary. The handoff reader's action (keep the token with the record and accept explicitly) is still safe.
- **F2: met.**
  - The opening explains the entry points.
  - The mismatch stop is consolidated: "At the first mismatch, stop new batches, retain both comparison files, and investigate before resuming; a later match does not cancel the discrepancy."
  - Rollback keeps every safeguard.
- **F3: met.** The prose reads smoothly.
- **Overall: pass.**

---

## First-pass condition comparison (Codex only)

| Condition | Pass | Fail | Insufficient | F1 / F2 / F3 met |
|---|---|---|---|---|
| original-body (reps 1, 2, 3) | 3 | 0 | 0 | 3 / 3 / 3 |
| original-examples (reps 1, 2, 3) | 3 | 0 | 0 | 3 / 3 / 3 |

**Behaviour seen in both conditions**
- One output in each condition kept the source almost word for word and cut only about 15% (body-2 at 1020 words, examples-1 at 1018). Neither condition is distinctive here: both show one conservative edit with the obvious padding removed.
- All six fold the detached "reminder about the implementation" into the opening position text. All six keep every Deployment and Rollback safeguard, the exact-02:00 and exactly-90 s boundaries, the latency count reset, and the "token requirement remains in force" note.

**Repeated within one condition**
- Two of three examples outputs (examples-2 and examples-3) turn "these interruptions were not an acknowledgement outage" into "the team has not tested an outage during acknowledgement." That's a small widening of the staging-evidence limits, though it doesn't cause a failure.
- Body-1 and body-3 keep the narrower scoping ("These tests did not cover…" / "These were not destination outages during acknowledgement"). Body-2 keeps it word for word.

**Single-output observations**
- Body-1 is the strongest for operational use. Its lists for start preconditions and rollback steps make it the quickest to scan at the moment of action. It slightly stretches "arrange another staffed window."
- Body-3 leaves the artifact rationale out of Deployment, so the reader has to find it in Rollback, and it no longer names who confirms the accounts.
- Examples-1 has slightly firmer staging-evidence wording ("indicating that the implementation behaves as intended in staging").
- Examples-3 blurs the token endpoint in the Handoff section; Deployment still states it.

**Conclusion.** The threshold outcomes are equal: 3 out of 3 passes in each condition. On quality, the most compressed outputs in each condition (body-1 and body-3; examples-2 and examples-3) are roughly comparable. Body-1 has a slight edge in scannability, and the body outputs are slightly more precise about staging evidence. The examples outputs have more consistent entry-point framing; examples-1 has none. Three repetitions are diagnostic only, and with no no-CW control nothing here supports a claim about how much the skill contributed.

---

First pass is complete. Now I'll read the prior assessment.
