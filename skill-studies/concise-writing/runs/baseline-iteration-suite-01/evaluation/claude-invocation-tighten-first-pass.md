## First-pass independent assessment (written before opening prior-assessment.md)

**Disclosure:** This review is independent but not blinded. The condition labels were visible. I read the following files completely: the index, `sources/report.md`, `sources/TASK.md`, `criteria.md`, `policy.txt`, `MECHANICAL-CHECKS.json` (`{}`, so no controller observations), `WORD-COUNTS.json` and all 9 outputs.

**Case:** invocation-tighten is a native case (N1-type) for tightening a decision update. Subject: claude / claude-sonnet-5, CLI 2.1.301, low effort. There is no no-CW control, so this case cannot show an incremental CW contribution. Invocation (D1) is outside this review.

**Facts each output needs to keep:**
- How the change works and the production risk: the new version moves the cursor only after upload, so a failed batch can be retried; the current production version moves it first, so rows can be lost.
- Test results: 50 staging exports with matching row counts, and 3 injected failures where the cursor held and no rows were lost.
- Limits: staging only, with no cross-region outage and no production-sized dataset, so the results prove nothing about production traffic or cross-region safety.
- Recommendation: a ten-internal-account pilot, not a general release. Approval is sought for the pilot only, because production-sized data and cross-region behaviour are untested.
- Logistics: Tuesday 10:00–11:00 staffed window. Maya runs the pilot, Leo compares row counts, and the pilot takes 30 minutes.
- Status: production still runs the current version; nothing is deployed.
- If counts don't match: stop, keep both files and don't delete them before investigation. The files show whether the missing rows came from source selection or from the upload.
- If counts match: return for a separate general-release decision; don't expand automatically.
- The request: confirm whether Maya should run the pilot.

| Run (short ID) | Condition / rep | Words (src 625) | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| …175838304Z…dehuzd_4 | candidate-fuller 1 | 231 (−394) | Met | Met (borderline) | Met | Pass |
| …175925732Z…3kwnyfkh | original 1 | 231 (−394) | Met | Met | Met | Pass |
| …175958573Z…88t7ioua | candidate-targeted 1 | 297 (−328) | Met | Met | Met | Pass |
| …180039294Z…endzbwm1 | original 2 | 275 (−350) | **Not met** | Met | Met | **Fail** |
| …180122941Z…yic96ly2 | candidate-targeted 2 | 279 (−346) | Met | Met | Met | Pass |
| …180157809Z…5fsa7z31 | candidate-fuller 2 | 269 (−356) | Met | Met | Met | Pass |
| …180232257Z…k_37fu_p | candidate-targeted 3 | 244 (−381) | Met | Met | Met | Pass |
| …180310852Z…rtxztq0x | candidate-fuller 3 | 265 (−360) | Met | Met | Met | Pass |
| …180343660Z…iogbjip3 | original 3 | 289 (−336) | Met | Met | Met | Pass |

All outputs are shorter than the source. TASK.md is 51 words.

**Evidence by output**
- **fuller-1:**
  - **Kept:** every fact, condition and action. Test results are bulleted. "Approval is requested for this pilot only." Match and mismatch branches are kept, with "do not delete either file."
  - **Weakness:** it is the only output that drops why the files matter (they show whether rows were lost in source selection or upload). It also doesn't explicitly say the pilot is limited *because* production-sized and cross-region behaviour are untested.
  - **Why F2 still passes:** the limits paragraph sits directly above the Recommendation, so the reader can make that link. The safeguard itself is intact and unconditional. So this is a weaker explanation, not lost safe action. This is a borderline call.
- **original-1:** Complete and well connected. The limitation reason is attached to the recommendation, and the reason for keeping the files is kept. It is the same length as fuller-1 but drops nothing consequential. It is the strongest of the shortest outputs. Approval for the pilot only is implied by "not a general release" plus the separate release decision.
- **targeted-1:** Complete, including the rationales and the separate approval scope.
  - "Don't delete either until the mismatch is resolved" is slightly stricter than the source's "investigated", which is harmless.
  - The staging/cross-region limit is stated in both "Staging checks" and "What this does and does not establish." This is mild leftover repetition that stops short of a real reading burden.
  - The recommendation comes late but is easy to find under its heading.
- **original-2 — F1 not met:**
  - **What changed:** it adds "(the only staffed window available)". The source says only "Tuesday from 10:00 to 11:00 is the staffed change window" and says nothing about other windows.
  - **Why it matters:** this unsupported scarcity claim bears directly on the decision. It tells the approver that declining or delaying means losing the only staffed slot, which puts pressure on the decision that the source doesn't justify.
  - **Caveat:** this is the borderline judgment in the set. Another assessor might read the source's definite article "the" as support. I don't, because "only … available" makes a new claim about the absence of alternatives.
  - **Otherwise complete:** both rationales are kept. The match branch sits under Next action and the mismatch branch under Recommendation, which splits the branches but stays readable. F2 and F3 are met apart from this shared defect.
- **targeted-2:** Complete, including "not to approve a general release" and both rationales. There is a small slip: "during the 30-minute window", when the window is 60 minutes and the pilot is 30. This is unlikely to mislead because 10:00–11:00 is stated just before it.
- **fuller-2:**
  - **Kept:** everything. Next action ends with clear match/mismatch bullets.
  - **Repetition:** the mismatch instruction appears in both Recommendation and Next action. I count this as useful reinforcement of a safeguard, as in the source, not padding.
  - **Navigation:** Maya, Leo and the 30-minute duration are split between sections, a slight cost.
- **targeted-3:** Complete. The labelled bullets (Window / If counts mismatch / If counts match) are the easiest to act on. Like fuller-1, the limit-reason link is only implied by the adjacent "does not establish" section, but here the reason for keeping the files is kept. There is no explicit "approval for pilot only" sentence; Next action plus the separate release decision cover it.
- **fuller-3:** Complete. It is the only output that puts the Recommendation and Next action first, which suits a decision reader. The final paragraph says the cross-region limit twice in adjacent sentences, a minor redundancy.
- **original-3:**
  - Complete. "Approving the pilot is not approval of a general release" is the clearest statement of approval scope in the set.
  - It keeps the source's separate Timing section. As a result, Leo's role appears twice, and the logistics, recommendation and actions are spread across three sections. This adds some navigation cost but stays easy to read.
  - It drops the explicit "don't delete", but "keep both export files" covers it.

**Comparison (native case, claude-sonnet-5 stratum only)**

| Condition | Functional passes |
|---|---|
| original | 2/3 |
| candidate-targeted | 3/3 |
| candidate-fuller | 3/3 |

- **Shared result:** every output removed the padding (the meta intro, the communication digression and the duplicate implementation section) and kept the decision, limits and safeguards. That behaviour recurs across all conditions.
- **Single observations, not patterns:**
  - The only failure (original-2) is an unsupported addition.
  - fuller-1 is the weakest pass on explanation.
  - targeted-3's bullets and fuller-3's decision-first order are notable improvements in usability.
- **Contribution:** with no control and n=3 per condition, these results cannot establish a CW contribution. The 2/3 vs 3/3 gap rests on one borderline judgment. Neither draft is shown to be preferable to the original. The quality differences between passing outputs vary within each condition more than between conditions.

**Criterion defect:** the criteria card's Limits line says F1–F3 apply to "original/candidate-comprehensive", but the Applies-to fields and the index name `candidate-targeted` and `candidate-fuller`. I applied the Applies-to fields.

Now reading the prior assessment.
