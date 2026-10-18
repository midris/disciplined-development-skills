## First-pass independent assessment (written before opening prior-assessment.md)

**Scope and disclosure.** Case `long-handoff`. Subject: codex / gpt-5.6-sol, low effort, one runtime stratum. 12 executions: 4 conditions × 3 repetitions. This review is independent but **not blinded**, because condition labels were visible. I read all of TASK.md, report.md, policy.txt (CW-expanded-1 / CW-assessment-4), criteria.md and all 12 outputs. MECHANICAL-CHECKS.json is `{}`, so the controller recorded no mechanical observations. Word counts come from WORD-COUNTS.json.

**Evidence gaps:**
- The boundary-checks file linked from criteria.md is not in the fixture.
- The subjects' completion messages are not supplied. They are outside this F1–F3 scope.

**Source anchors checked in every output:**
- Pilot approval is needed and none is recorded.
- Green checks are not approval.
- 12 internal accounts, the 01:00–02:00 UTC window and the 40-minute pilot.
- No batch may be estimated to finish after 02:00; finishing exactly at 02:00 is allowed.
- One mismatch stops new batches, and a later match doesn't cancel it.
- Latency must exceed 90 s on three consecutive batches; exactly 90 s doesn't count, and a faster batch resets the count.
- The lease is held while an acknowledgement is outstanding, and health checks don't change that.
- Cursor reconciliation with the destination operator before releasing the lease.
- Snapshot and comparison files are kept until the incident owner authorizes release.
- The 12 accounts stay on the existing policy after a rollback.
- Handoff record and acceptance, and the token rule with its unexplained rationale.
- Untested conditions remain; wider release is a separate decision.
- The Deployment and Rollback sections each work as an entry point on their own.

Source word count: report.md 1207, TASK.md 68.

### Per-output judgments

| Run (suffix) | Condition | Rep | Words (Δ vs 1207) | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|---|
| …2bst2qua | candidate-targeted | 1 | 842 (−365) | met | met | met | **pass** |
| …fv_q4hrh | candidate-targeted | 2 | 910 (−297) | met | met | met | **pass** |
| …p2fw66_f | candidate-targeted | 3 | 883 (−324) | met | met | met | **pass** |
| …iakgyzp9 | candidate-fuller | 1 | 900 (−307) | met | met | met | **pass** |
| …a_oxgdfq | candidate-fuller | 2 | 845 (−362) | met | met | met | **pass** |
| …70c316l7 | candidate-fuller | 3 | 820 (−387) | met | met | met | **pass** |
| …ung8wj8o | control | 1 | 868 (−339) | met | met | met | **pass** |
| …2coijqb9 | control | 2 | 842 (−365) | met | **not met** | met | **fail** |
| …ve_9uhip | control | 3 | 815 (−392) | met | met | met | **pass** |
| …s_ra2gs2 | original | 1 | 900 (−307) | met | met | met | **pass** |
| …azax1cym | original | 2 | 864 (−343) | met | met | met | **pass** |
| …wafs66vv | original | 3 | 878 (−329) | met | met | met | **pass** |

All outputs are shorter than the source. Shorter length is recorded, not scored.

**Original 1–3 (pass).** These keep the source's section order almost exactly and remove its padding:
- The "several aspects" intro.
- The duplicated row-count sentence.
- The "encouraging" sentence.
- The separate "reminder about the implementation" section. Its mechanism is already in Current position.

Every Deployment section contains the full go/no-go gate: approval, both people present, channel staffed, accounts, window. It also keeps the reasons for artifacts and lease (e.g. original-1:23–25). Every Rollback section restates the lease, reconciliation, "replay or omit" and artifact rules on its own (original-1:41–47). All boundary values are exact (original-2:27, 33).

Small simplifications:
- "The team has not tested a destination outage during acknowledgement" turns "these interruptions were not an acknowledgement outage" into a general "not tested". This is harmless.
- Original 1–2 drop the literal "do not begin" but keep "arrange another staffed window", so the meaning is unchanged.

Original-1:3 adds a short orientation line ("Those sections repeat critical safeguards…"). It's useful framing. Readability is good: familiar structure and short paragraphs.

**Candidate-targeted 1–3 (pass).** These are structurally close to the originals and equally faithful:
- Targeted-1 drops the navigation intro entirely. Rollback still says "Incident responders may enter here directly" (line 38), and the headings are self-evident, so nothing practical is lost.
- Targeted-2 keeps every causal sentence, including the "worker that has sent a batch… remains outstanding" clarification (line 23).
- Targeted-3 keeps "do not begin" (line 21) and the source's "passing it supplies no evidence" (line 53).

No regressions against the originals. Quality differences between targeted and original are negligible.

**Candidate-fuller 1–3 (pass).**
- Fuller-1 turns the Deployment preconditions into a checklist that puts approval first (lines 20–26). This makes the most important gate more visible, which is a slight improvement.
- Fuller-2 numbers the pre-enable steps and keeps every reason in Deployment.
- Fuller-3 uses an untitled lead-in and bulleted stop conditions.

Fuller-3 weaknesses:
- It adds the interpretive "These results support the limited pilot" (line 14). This is consistent with the team's recommendation and not consequential.
- Its Rollback drops the reason for keeping the artifacts. The reason survives in Deployment (line 22), and the retention rule plus "clean rollback is not authorization" remain in Rollback.

Fuller-1's Rollback lacks its own "enter here" note, but the intro supplies it.

**Control-1 (pass).** It reorganizes into bullets, a checklist and numbered rollback steps. The Deployment gate includes approval (lines 24–30), and all boundaries are exact.

Weakness: Deployment drops the causal reasons for keeping the artifacts and the lease ("second worker from unresolved cursor"). Both reasons survive in Rollback (lines 61, 63), and the Deployment rules themselves remain, with "even if healthy" and "even after the window ends". I count this as a lost explanation, not a lost safeguard, so F2 is met with reservation.

**Control-2 (fail, F2 not met).**
- *Source meaning:* "Release operators normally open the Deployment section immediately before the window… the operational sections must also work for those readers at the moment they act." Source Deployment lines 44–47 put the go/no-go gate there: approval, both people, staffed channel, approved accounts, window not ended.
- *Output:* control-2 moves the whole gate into "Tonight's decision" (lines 3–17). Its Deployment section (lines 37–47) starts at "1. Save the current cursor snapshot" and never mentions approval, Rae's and Jo's presence, the staffed channel or the end of the window. The navigation note telling release operators to enter at Deployment is also gone.
- *Consequence:* an operator who enters at Deployment under green-check pressure, which is exactly the scenario the case targets, gets a procedure with no approval stop. The approval gate is the document's central safeguard.

Secondary issues:
- Rollback (lines 68–71) drops the "replaying or omitting a batch" reason for holding the lease.
- The added precondition "the pilot can run within the staffed window" (line 15) is not stated in the source. It is conservative and arguably implied by "40-minute pilot in the 01:00–02:00 window".

F1 is met, because every fact appears somewhere and nothing is falsified. F3 is met, because the document is well organized. **This is an interpretive judgment.** A reviewer who treats the opening section as sufficient navigation could score F2 met.

**Control-3 (pass).** It puts the decision first and still repeats the full gate in Deployment (lines 23–29). Boundaries are exact, and "any single row-count comparison" (line 47) keeps the single-mismatch rule.

Weaknesses:
- Rollback drops the reason for keeping the artifacts (it survives in Deployment, line 37).
- Deployment drops the lease reason (it survives in Rollback, line 65).
- The "report results / no automatic account addition" rule moves to the opening and loses its "if counts agree throughout" condition. That is harmless, because a mismatch triggers a stop anyway.

### Comparison

**Measured functional passes (codex / gpt-5.6-sol, long-handoff):**

| Condition | Pass | Fail | Insufficient evidence |
|---|---|---|---|
| control | 2/3 | 1 (rep 2, F2) | 0 |
| original | 3/3 | 0 | 0 |
| candidate-targeted | 3/3 | 0 | 0 |
| candidate-fuller | 3/3 | 0 | 0 |

**Differences between passing outputs:**
- All nine skill-bearing outputs keep the source's section skeleton, including a self-contained Deployment gate and Rollback restatement. They place both the rules and their reasons at each point of use, which preserves the entry-point redundancy the case tests.
- The controls restructure more aggressively (decision-first sections, bullets, numbered steps). This sometimes reads faster, but it repeatedly strips causal reasons from one of the two operational sections (controls 1, 2 and 3), and once strips the gate itself (control-2).

So the recurring control behavior is that **dedup removes point-of-use explanations** (3/3 controls). The **gate loss** happened once. The skill-bearing outputs' recurring behavior is conservative compression that leaves structure intact.

Regressions in skill outputs are minor and one-off: fuller-3 drops the artifact reason in Rollback and adds an interpretive line, and targeted-1 drops the navigation intro.

**Draft versus original:**
- Targeted is essentially indistinguishable from the original.
- Fuller-1's approval checklist is a small usability gain, while fuller-3 is slightly weaker at point of use.
- Neither draft is shown to be preferable to the original.

**CW contribution:** the evidence weakly suggests CW helps keep entry-point safeguards and their reasons in place during deduplication. That rests on 9/9 skill outputs against 2/3 controls, plus the control-only pattern of lost reasons. With n=3 per condition, one runtime and an unblinded assessor, a reliable contribution is unresolved. The control pass rate is still high, so the margin depends on a single run.

Now reading prior-assessment.md for comparison.
