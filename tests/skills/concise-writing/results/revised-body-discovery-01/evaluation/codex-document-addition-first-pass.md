I've read every source, policy, criterion card, the interpretation supplement, the controller files and all 15 outputs. Below is my independent first-pass assessment. I'll read prior-assessment.md only after this.

---

# First-pass assessment (independent, not blinded)

**Disclosure:** The condition labels were visible in the filenames and the index, so this review is independent but not blinded. MECHANICAL-CHECKS.json is `{}`, so it records no controller observations. INTERPRETATION.md refers to `contact-reassessment-01/policy.txt` and other external records that are not in the packet. I applied the contact rule as summarised in INTERPRETATION.md: confirming a named fallback contact before invitation is enough, and explicitly recording it is a precision point. Not having the full contact policy is an evidence gap, but it doesn't change any result here.

**Case:** E, document addition. Subject: Codex `gpt-5.6-sol`, effort low, one runtime/provider stratum. Conditions: `original`, `candidate-targeted-examples`, `control` (no CW), 5 repetitions each.

**What I checked against.** In the existing report: opt-in scope; the decision is four invitations, not the default; the evidence limits (120 searches, 2 timeouts that succeeded on retry, untested above 50k documents, quiet support queue ≠ correctness, new teams under 20k documents don't validate large collections); consent and switch-back checks; the strict >5%/24h timeout check with postpone-and-investigate; Thursday approval; invitation is permission, not a default change; the 7-day review; and the default decision stays open.
In NEW-NOTES: a named fallback contact before invitation; pause the affected team only; retain the query and result in the restricted incident record; a report is not a confirmed defect; other teams continue unless the problem is broader; resume only after Omar has investigated **and** Nia approves; the review includes pauses and their outcomes; a successful review needs a separate expansion decision and doesn't authorise default enablement.

**Length:** Source report 279 words; NEW-NOTES 166 words (TASK 58). Case E has no shortening preference, and growth is justified by the required additions.

## Per-output judgments

### original-1 (`…original-ef378298…`), rep 1: **PASS** (F1 met, F2 met, F3 met). 359 words (+80 vs report)
- Fallback contact is added to Nia's pre-invite checks. Under the contact rule, "confirm… has a named fallback contact" is adequate. All existing evidence limits and gates are kept word for word.
- A new "If a result may be incorrect" section covers: affected team only, restricted incident record, "precaution trigger, not confirmation of a defect", others continue unless broader, and resume only after Omar investigates and Nia approves.
- The review now includes "any pauses, and their investigation outcomes", plus the separate-decision and no-default rules. The closing recap is kept.
- Strength: each branch is clear and easy to find. Weakness: none of consequence.

### original-2 (`…original-9c76e112…`), rep 2: **PASS** (met / met / met). 348 words (+69)
- Same structure as original-1. "The report is not a confirmed defect" keeps the qualification. The review sentence drops "before deciding whether to expand again" but keeps "separate decision before further expansion", so the meaning is preserved. Recap kept.

### original-3 (`…original-e1d909fb…`), rep 3: **PASS** (met / met / met). 359 words (+80)
- Resumption is in its own paragraph with both gates. "A successful review does not authorize further expansion or enabling the preview by default; either requires a separate decision" matches the source and the "default decision remains open" line. Recap kept.

### original-4 (`…original-f1c1dcb3…`), rep 4: **PASS** (met / met / met). 347 words (+68)
- "has a named fallback contact recorded" is more precise than most outputs.
- It lightly edits existing text: "This matters because an invitation is permission…" becomes "an invitation permits a team to try the preview but does not enable it". The permission-versus-default distinction survives. "only the invited teams choose to enable it" is dropped, but "off by default" plus "permits a team to try" carries it.
- "A report is not, by itself, confirmation of a defect" is good. Recap kept (without "broader", which doesn't matter).

### original-5 (`…original-90aa3c52…`), rep 5: **PASS** (met / met / met). 321 words (+42), the shortest output
- The most precise fallback handling: "For each proposed team, Nia must confirm consent and the ability to switch back…, then record a named fallback contact." It also keeps "under the existing policy" for other teams. Both resumption gates are present.
- **Weakness (quality, not failure):** the closing "For Thursday:" recap is removed, including "The broader default-setting decision remains open." I checked whether the meaning survives elsewhere:
  - The opening still says the decision is "whether to invite four more teams, not whether to make the preview the default" and that the evidence doesn't support enabling for everyone.
  - The timeout postponement is still in "Before inviting anyone".
  - The final section says a review "does not authorize enabling the preview by default."
  
  So no fact or condition is lost. The cost is that the manager loses the end-of-document action summary. It's a meaningful regression from the source's orientation, but not enough to fail F2 for a short document that leads with the decision.

### candidate-targeted-examples-1 (`…69f41413…`), rep 1: **PASS** (met / met / met). 350 words (+71)
- All additions are present and correct; both resumption gates are kept.
- **Layout weakness:** the incident branch has no heading of its own. It sits inside "What happens next", ahead of the 7-day review. The incident rule applies throughout the preview, not as a next step, so a reader looking for incident handling has to scan. The document is short, so the burden is small. This is a quality observation only.
- **Precision note:** "If a team reports…" narrows the trigger. The source triggers on "a report of a potentially incorrect search result", whoever reports it. In practice the reporter will usually be the team or its users, so I don't count it as a consequential distortion. All five controls share this wording.

### candidate-targeted-examples-2 (`…a34f4dd2…`), rep 2: **PASS** (met / met / met). 357 words (+78)
- Separate incident section; "The report is not confirmation of a defect"; both gates present. "A successful review does not authorize another expansion or enable the preview by default; each requires a separate decision." Recap kept. The existing text is unchanged apart from the fallback clause.

### candidate-targeted-examples-3 (`…9863d953…`), rep 3: **PASS** (met / met / met). 364 words (+85)
- "A report triggers this precaution but is not, by itself, a confirmed defect" states the qualification well. Resumption is in its own paragraph with both gates. Recap kept.

### candidate-targeted-examples-4 (`…4e3917bd…`), rep 4: **PASS** (met / met / met). 361 words (+82)
- Fallback is "recorded", which is more precise. "precautionary trigger, not confirmation of a defect"; both gates present; recap kept.

### candidate-targeted-examples-5 (`…5f3b0db1…`), rep 5: **PASS** (met / met / met). 353 words (+74)
- Very close to candidate-2 and candidate-4. All anchors present.

### control-1 (`…control-c71d2084…`), rep 1: **PASS** (met / met / met). 381 words (+102)
- Keeps the source wording most closely: "recorded", "while using the preview", "Other participating teams may continue under the existing policy", "resume only after Omar has investigated and Nia approves resumption." Also has the "If a team reports" trigger narrowing (precision note).
- Slightly heavier phrasing ("the outcomes of their investigations", "does not automatically authorize… either step requires a separate decision"). This adds no real reading burden.

### control-2 (`…control-b0d0083c…`), rep 2: **PASS** (met / met / met). 389 words (+110)
- Same as control-1, with resumption in its own paragraph with both gates. "The pause is a precaution and does not mean the report has been confirmed as a defect."

### control-3 (`…control-508d0e0c…`), rep 3: **PASS** (met / met / met). 384 words (+105)
- "If a participating team reports…" Both gates present. Recap kept.

### control-4 (`…control-0b64f082…`), rep 4: **PASS** (met / met / met). 389 words (+110)
- Both gates: "may resume only after Omar has investigated and Nia approves resumption." Recap kept.

### control-5 (`…control-27669602…`), rep 5: **FAIL** (F1 not met; F2 met, with the same defect noted; F3 met). 382 words (+103)
- **F1 failure:**
  - **Source:** "The affected team can resume only after Omar has investigated and Nia approves resumption." That is two conditions, both required before resumption.
  - **Output (line 21):** "Omar must investigate the report, and the affected team may resume the preview only after Nia approves resumption." Investigation becomes a duty running alongside the gate. Only Nia's approval is the precondition.
  - **What the document communicates:** nothing in it prevents resumption while Omar's investigation is still open. I checked the rest of the document and the condition isn't restored anywhere.
  - **Why it counts:** the case card names "investigation/resumption conditions" as an anchor, and INTERPRETATION.md says missing incident/resumption conditions can still fail.
  - **Uncertainty:** this is the closest call in the packet. A charitable reader would assume Nia approves after the investigation. But the text doesn't say so, and in every other output the "only after" gate covers both steps.
- Everything else is faithful and well organised: a dedicated "While teams use the preview" heading, fallback "recorded", "under the existing policy", review with pauses and outcomes, recap kept. Under the overlap rule I score the defect once (F1). F2 and F3 are otherwise met.

## Condition comparison

**Measured functional pass counts (case E; Codex gpt-5.6-sol, low effort; one stratum):**

| Condition | Pass | Fail | Insufficient | F1 met | F2 met | F3 met |
|---|---|---|---|---|---|---|
| original | 5/5 | 0 | 0 | 5 | 5 | 5 |
| candidate-targeted-examples | 5/5 | 0 | 0 | 5 | 5 | 5 |
| control (no CW) | 4/5 | 1 | 0 | 4 | 5 | 5 |

**Word counts (report 279 / notes 166):**

| Condition | Words per rep (1–5) | Range vs report |
|---|---|---|
| original | 359, 348, 359, 347, 321 | +42 to +80 |
| candidate | 350, 357, 364, 361, 353 | +71 to +85 |
| control | 381, 389, 384, 389, 382 | +102 to +110 |

Lengths are descriptive only. Shorter isn't preferred for case E.

**Quality differences beyond pass/fail:**
- **All 15 outputs integrate the new material well.** None appends an unconnected addendum, and none weakens the existing evidence limits or the >5% threshold. The case was not hard for this model even without CW.
- **Controls** (recurring, 5/5) stay close to the source wording, which keeps precision ("recorded", "under the existing policy", "while using the preview"). They are about 25–35 words longer than the skill outputs, with mildly wordier phrasing. That isn't a readability burden. Their recurring trigger wording "If a team reports" (5/5) narrows the trigger slightly; it is a precision note only.
- **Candidate** (5/5) produces near-identical, conservative edits: the existing text is unchanged and the new text is compact. One layout weakness, in candidate-1 (incident branch under "What happens next"), is a single observation. Only candidate-1 uses the narrowed "a team reports" trigger.
- **Original** (5/5) varies more. Reps 4 and 5 also tightened existing source sentences, and the edits were faithful. Original-5 removed the closing decision recap, a single observed regression in orientation for the deciding manager. It also had the most precise fallback wording.
- **The one F1 failure** (control-5's lost resumption precondition) is a single observation. It is not a pattern in the controls: the other four state both gates.

**CW contribution:** These results don't support a useful CW contribution in this case. The 5/5/4 split comes down to one borderline control defect, and the controls otherwise match or beat the skill outputs on precision. The skill conditions give modestly tighter documents with no loss of meaning (apart from original-5's lost recap). Neither skill version is clearly better than the other. Candidate was a little more consistent (no recap loss) and original a little more precise in places. The difference is within what you'd expect from 5 samples.

---

Now reading the prior assessment for comparison.
