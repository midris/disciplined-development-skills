## First-pass independent assessment (written before opening prior-assessment.md)

**Disclosure:** This review is independent but not blinded. Condition labels were visible. I am a Claude-family model (Opus 5.5) assessing outputs from a Claude-family subject (claude-sonnet-5, CLI 2.1.301, effort low). Everything is in one stratum: provider claude.

**Evidence read in full:** EVALUATION-INDEX.json, sources/report.md, sources/TASK.md, policy.txt (CW-expanded-1 / CW-assessment-4), criteria.md (agent-recommendation, definition 6), WORD-COUNTS.json, MECHANICAL-CHECKS.json (`{}`, so the controller recorded no mechanical observations), and all 12 outputs. There are no evidence gaps.

**Case and reader:** This is case A-type explicit-load editing. The reader has to decide whether to approve a limited Cedar export pilot. They need the evidence, its limits, the execution arrangements and what to do with each result. The source is 625 words. The consequential items are:
- the 50 matching exports and the 3 injected failures
- staging only: no production-sized data and no cross-region outage tested
- the mechanism contrast between the new and current versions
- not yet deployed
- the Tuesday 10:00–11:00 staffed window, with Maya running the pilot, Leo comparing row counts, and a 30-minute duration
- the pilot is limited to 10 internal accounts, not a general release, *because* production-sized data and cross-region behaviour are untested
- on a mismatch: stop, keep both files and don't delete them, because they show whether the rows were lost in source selection or upload
- on a match: return for a separate general-release decision, with no automatic expansion

### Per-output judgments

| Order | Run ID (suffix) | Condition / rep | F1 | F2 | F3 | Overall | Words (Δ vs 625) |
|---|---|---|---|---|---|---|---|
| 3 | …control-78c1dbef…mwxcm_6h | control 1 | met | met | met | **pass** | 230 (−395) |
| 6 | …control-77572985…14sncics | control 2 | **not met** | met | met | **fail** | 240 (−385) |
| 9 | …control-1bbc97d0…9q55rlub | control 3 | **not met** | met | met | **fail** | 257 (−368) |
| 4 | …original-d3077d2e…iz0mxf7u | original 1 | met | met | met | **pass** | 304 (−321) |
| 7 | …original-c4b5d3cb…u_s1su0m | original 2 | met | met | met | **pass** | 308 (−317) |
| 10 | …original-dda59c49…55yqlemj | original 3 | met | met | met | **pass** | 317 (−308) |
| 1 | …candidate-targeted-b2c93c2c…fz3scwk4 | targeted 1 | met | met | met | **pass** | 270 (−355) |
| 8 | …candidate-targeted-94d0de42…s8wu1e6e | targeted 2 | met | met | met | **pass** | 261 (−364) |
| 11 | …candidate-targeted-fd6164e3…du4j6iot | targeted 3 | met | met | met | **pass** | 322 (−303) |
| 2 | …candidate-fuller-fb7d7805…n0vsuhra | fuller 1 | met | met | met | **pass** | 241 (−384) |
| 5 | …candidate-fuller-8f010012…1mlzkko4 | fuller 2 | met | met | met | **pass** | 239 (−386) |
| 12 | …candidate-fuller-69c7c473…csb8f3g5 | fuller 3 | met | met | met | **pass** | 285 (−340) |

All outputs are shorter than the source and none is flagged for length. Length was not used as a quality score.

#### Control 1: pass
- **F1 met.** Every fact in the source is present:
  - status: not deployed
  - the mechanism contrast
  - 50 exports and 3 failures, with no rows lost
  - the staging-only limits, including "production-sized data has not been exercised"
  - the 10 internal accounts, not a general release
  - Tuesday 10:00–11:00, Maya, Leo and the 30-minute run
  - both result branches, including "Do not expand the rollout automatically"
  - "This is not a request to approve general release"
- **Weaknesses:**
  - It drops the reason for keeping the files (they show whether the rows were lost in source selection or upload). The action itself ("keep both… do not delete either file") and its purpose ("for investigation") remain, so the safeguard still works.
  - The recommendation has no explicit "because untested". The limits sit in the bullet directly above it, so the reader can make the connection without effort.
- **F2/F3 met.** The match/mismatch bullets and the separate "Decision needed" section make the decision and the actions easy to find.

#### Control 2: fail (F1)
- **Source meaning:** The pilot is limited *because* production-sized data and cross-region behaviour "remain untested". This is risk containment. The source stresses that the evidence "do[es] not establish" these things.
- **Output:** "Run a pilot on 10 internal accounts — not a general release — **to test production-sized behavior**."
  - This presents a 10-account pilot as the test of production-sized behaviour. The source never claims that.
  - The containment rationale is gone, and cross-region drops out of the reasoning.
- **Consequence:** If the pilot matches, the reader could treat it as having addressed the production-size gap at the general-release decision. That is the overstatement the source warns against.
- **Smaller issue:** The mechanism sentence adds "and no rows are lost" as a design property. In the source, that was a test result.
- **Otherwise strong:** The approval section is complete, it includes the reason for keeping the files, and the branches are clear. F2/F3 met.
- **Uncertainty:** This is borderline. A lenient reading would take "production-sized" loosely to mean "production". I judge it unsupported because the source's central caution is precisely about this scope.

#### Control 3: fail (F1)
- **Output:** "Run a pilot on 10 internal accounts, not a general release, **to test the untested conditions above (production-sized data, cross-region failure behavior)**."
- **Why it fails:** This is stronger than control 2. It explicitly says the pilot will test cross-region failure behaviour. Nothing in the source suggests a staffed 30-minute, 10-account pilot will exercise a cross-region outage.
- **Consequence:** After a successful pilot, the reader may believe cross-region safety has been checked.
- **Otherwise excellent:** The Logistics bullets bring together the window, the duration, the roles, both branches and the reason for keeping the files. F2/F3 met.

#### Original 1: pass
- **F1 met.** Every item is present, and the rationale ("because production-sized data and cross-region failure behavior remain untested") is preserved.
- **F2 met.** It is better than the source: the padding, the communication digression and the duplicated mechanism section are gone. The Next action section brings together Maya, Leo, the 30-minute duration and both branches.
- **F3 met, with weaknesses:**
  - It keeps the source's scattered order: checks, mechanism, limits, timing, mismatch, recommendation, next action.
  - The staging limits are stated in "Checks" and then immediately restated in "What this does and does not establish".
  - The mismatch instruction appears twice. That has some safety-reinforcement value.
  - The overall reading burden is small.

#### Original 2: pass
- **F1 met.** "Checks" mentions only the cross-region gap, but "production-sized traffic" appears in the limits section and in the recommendation rationale.
- **Minor gap:** Leo's role appears only under Timing.
- **Structure:** It follows the same source order as original 1. F2/F3 met, with the same fragmentation weakness.

#### Original 3: pass
- **Complete.** The rationale is preserved and "not to approve a general release" is kept.
- **Order:** The limits section comes after Timing and Mismatch, away from the evidence it qualifies. This is a mild coherence cost, not a failure. F2/F3 met.

#### Targeted 1: pass
- **Consolidation:** Approval, window, roles, duration, both branches and the reason for keeping the files are all in one Recommendation section, which is very usable.
- **Fidelity:** The "because untested" rationale is kept.
- **Minor gap:** "Keep both export files" drops the explicit "do not delete". Keeping the files and the reason for keeping them are both present, so the safeguard is intact.
- **Placement:** "Production is still running…" sits a little oddly under the limits section.

#### Targeted 2: pass
- **Complete.** The rationale and the 30-minute duration are present, and "don't delete the evidence" is kept.
- **Gap:** Like control 1, it drops the source-selection-vs-upload reason for keeping the files. The safeguard remains.
- **Minor repetition:** "Staging only" is stated twice. Clean overall.

#### Targeted 3: pass
- **Structure:** It is almost identical in structure and length to original 1/3 and keeps the source's section order (322 words, the least reduction).
- **Fidelity:** Complete and faithful. F3 met, with the same fragmentation weakness as the originals.

#### Fuller 1: pass
- **Layout:** It puts the recommendation first: the decision, approval, window, roles, duration and the match branch. Then come "Why", the evidence and limits, and the mismatch handling. This is the most decision-oriented layout in the set.
- **Weaknesses:**
  - It adds "(the only staffed window)". The source says "the staffed change window", so this is a mild, low-consequence extrapolation that could add urgency. I flag it but do not treat it as a failure.
  - The recommendation has no explicit "because untested". The limits follow two sections later.
  - The mismatch branch is separated from the match branch, although it has its own heading.
- **F1/F2/F3 met.**

#### Fuller 2: pass
- **Labelling:** The "Status" heading covers the mechanism and the evidence, which is a slightly inaccurate label.
- **Content:** The "given that… untested" rationale is kept. The mismatch handling is complete with its reason.
- **Minor gap:** The match branch omits "rather than expanding automatically". "Separate general-release decision" still carries that meaning. Pass.

#### Fuller 3: pass
- **Complete.** The Next action bullets give both branches, with the reason for keeping the files.
- **Minor repetition:** Cross-region is mentioned twice in one paragraph.
- **Placement:** "Not deployed" is a trailing orphan line. Pass.

### Condition comparison (claude / claude-sonnet-5 / low effort)

| Condition | Pass | Fail | Insufficient |
|---|---|---|---|
| control | 1/3 | 2/3 (F1) | 0 |
| original | 3/3 | 0 | 0 |
| candidate-targeted | 3/3 | 0 | 0 |
| candidate-fuller | 3/3 | 0 | 0 |

**Quality differences beyond pass/fail:**
- **Controls restructure the most.** They are the shortest and use bullets and conditional branches. Two of the three rewrite the pilot's rationale into "the pilot will test the untested conditions". This is a recurring control behaviour (2/3), not a single observation.
- **All 9 skill-bearing outputs keep the source's risk-containment reasoning.** It is explicit in 8 of them and implicit in fuller 1.
- **Original-condition outputs stay closest to the source** in wording and section order. They are faithful but keep the scattered layout and some adjacent restatement. Targeted 3 behaves the same way.
- **Fuller outputs are the most reader-oriented on average.** Fuller 1 leads with the recommendation, and fuller 3 has branch bullets in Next action. Fuller 1 also has the one minor unsupported addition.
- **Targeted 1 and 2 consolidate well.** Targeted 3 does not.

**Contribution:**
- In this sample, the skill-bearing conditions avoided a correctness regression that 2 of 3 controls made, and they still removed the source's padding (all 46–51% of source length).
- That suggests CW helped preserve reasoning fidelity here, possibly by keeping outputs closer to the source wording.
- However, n=3 per condition, the deciding defect is borderline, and the control that avoided it (control 1) is arguably the most usable document overall. A reliable contribution claim is not established.
- Neither draft is clearly preferable to the original on outcomes (3/3 each). On quality, fuller is modestly preferable for decision-oriented structure. Targeted is mixed. Both are unresolved at this sample size.

Now reading the prior assessment.
