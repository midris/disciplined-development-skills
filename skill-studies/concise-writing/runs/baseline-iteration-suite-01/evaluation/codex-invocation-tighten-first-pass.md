I've read every source, criterion and output, plus the policy and controller files. `MECHANICAL-CHECKS.json` is empty (`{}`). Here is my first-pass assessment, written before I open `prior-assessment.md`.

---

# Part 1: Independent assessment (labels visible, so not blinded)

**Scope.** The case is `invocation-tighten`, a native tightening case. The source is `sources/report.md`, the task is `sources/TASK.md`, the policy is CW-expanded-1 / CW-assessment-4, and the card is `criteria.md`. The subject was codex / gpt-5.6-sol / CLI 0.163.0 / low effort, one stratum. There are 9 runs: original ×3, candidate-targeted ×3 and candidate-fuller ×3. There is no no-CW control. This is not N3, so F1–F3 apply. I did not assess D1 (invocation).

**Source meaning the reader needs** (the reader is the person deciding the next step for Cedar):
- **Evidence:** 50 staging exports all completed with matching row counts. In 3 injected upload failures the cursor stayed at the last uploaded batch and no rows were lost.
- **Limits:** this is staging evidence only. Production-sized data, production traffic and cross-region outages are untested.
- **Mechanism:** the change uploads a batch before advancing the cursor. The current production version advances first, so a failed upload can drop rows from the next export.
- **Status:** the change is not deployed; production still runs the current version.
- **Logistics:** Tuesday 10:00–11:00 is the staffed window. Maya runs the pilot, Leo watches row counts, and the pilot takes 30 minutes.
- **The ask:** approve a pilot on 10 internal accounts, not a general release. The reason is the untested items above.
- **On mismatch:** stop, keep both files and don't delete them before investigation. The files show whether the loss came from source selection or upload.
- **On match:** bring results back for a separate general-release decision, with no automatic expansion.

**Padding removed:** the intro, the communication digression and the second mechanism section repeat or add nothing.

**Word counts:** `report.md` is 625 words (`TASK.md`, 51 words, is the task, not the edited document). Every output is shorter.

## Per-output judgments

**1. original rep 1** (`…173601788Z…6fme7bdv`): 234 words (−391, shorter). F1 met · F2 met · F3 met → **Pass**
- **Evidence:** Leads with "Decision needed": the pilot-only ask, the 30-minute pilot in the 10:00–11:00 window, Maya and Leo. It states "not deployed", the 50 matching exports, the 3 failures with no loss, all three untested items, and the mechanism with the production-version contrast. On mismatch it says stop and retain both files, with the reason. On match it says a separate decision, no automatic expansion.
- **Weakness:** "Limiting the first exposure… addresses that uncertainty" slightly overstates. Limiting exposure contains the risk; it doesn't resolve the uncertainty. This isn't consequential, because the separate general-release step shows the uncertainty is still open.
- **Weakness:** It says "retain" but not "until investigated". Retention is implied by "needed to determine…".

**2. candidate-targeted rep 1** (`…173747677Z…35q33g2p`): 210 words (−415, shorter, the shortest). F1 met · F2 met · F3 met → **Pass**
- **Evidence:** Four compact bullets cover evidence, limits and deployment status. A clear "Pilot outcome" section gives both branches.
- **Weakness:** It never says the untested gaps are *why* this is pilot-only. The limits bullet sits right next to the pilot-only request, so the reader can make the link easily, but the source states it outright.
- **Weakness:** "Production traffic" is folded into "production-sized data". That's acceptable.

**3. candidate-fuller rep 1** (`…173833212Z…m9xsszar`): 244 words (−381, shorter). F1 met · F2 met · F3 met → **Pass**
- **Evidence:** Structured like original-1, but with a more faithful causal sentence: "That remaining uncertainty is why the recommended first exposure is limited to ten internal accounts." All facts, both branches and the evidence purpose of the files are present.
- **Strength:** The heading "What the change fixes" orients the reader well.

**4. candidate-targeted rep 2** (`…173924030Z…w2k6wkav`): 220 words (−405, shorter). F1 met · F2 met · F3 met → **Pass**
- **Evidence:** All facts are present, including "retain both export files until the issue is investigated" and the closing "Please confirm whether Maya should run the pilot on Tuesday."
- **Weakness:** It is the only output that puts evidence before the request. The decision sits in the second section, so a decision-focused reader reaches it a little later. At this length, with a clear heading, that's a small cost.
- **Weakness:** The causal link (limits → pilot-only) is implicit.
- **Weakness:** "If the counts mismatch" is slightly awkward.
- **Weakness:** "Approve…" and "Please confirm…" repeat the ask. That works as a closing call to action, not as padding.

**5. candidate-fuller rep 2** (`…174003161Z…r3jx9n5g`): 234 words (−391, shorter). F1 met · F2 met · F3 met → **Pass**
- **Evidence:** Complete. "Staging evidence supports limited exposure" plus the stated limits supplies the reasoning.
- **Weakness:** The mechanism paragraph sits under "Why a pilot". It explains why the change is needed, not why it should be a pilot, so the heading mislabels it a little.
- **Weakness:** The fact that the cursor stayed at the last uploaded batch appears once as design and once as test result. That's mild but defensible.

**6. original rep 2** (`…174044889Z…hgu21x2o`): 219 words (−406, shorter). F1 met · F2 met · F3 met → **Pass**
- **Evidence:** It has a separate "Remaining risk" section with an explicit link: "For that reason, the recommendation is a limited pilot." All three untested items are named. The section "Pilot stop condition and follow-up" gives both branches.
- **Weakness:** "Not deployed" is implied by "Production still uses the current version" rather than stated. That's fine.

**7. candidate-fuller rep 3** (`…174126499Z…r5f8no_p`): 230 words (−395, shorter). F1 met · F2 met · F3 met → **Pass**
- **Evidence:** Complete facts and both branches. "Missing rows came from source selection or upload" stays close to the source wording.
- **Weakness:** The causal link (limits → pilot-only) is implicit. It's carried only by the "remaining risk" heading and the pilot-only sentence.

**8. original rep 3** (`…174203757Z…mla6pnv2`): 228 words (−397, shorter). F1 met · F2 met · F3 met → **Pass**
- **Evidence:** "These gaps are why the recommendation is a limited pilot" makes the link explicit. "Retain both export files until the mismatch is investigated" keeps the retention condition.
- **Weakness:** The match branch is in "Decision needed" while the mismatch branch is in "Pilot safeguard". The two outcomes are split up, but each is easy to find.

**9. candidate-targeted rep 3** (`…174239923Z…odacpb_z`): 220 words (−405, shorter). F1 met · F2 met · F3 met → **Pass**
- **Evidence:** "So a general release is not yet recommended" makes the link explicit. It is the only output to keep the explicit "Do not delete either file". It says "Production is still using that version; the change has not been deployed."
- **Weakness:** As in original-3, the match and mismatch branches are in different sections.

No output added an unsupported claim of consequence, lost a condition or misstated a number or role.

## Condition comparison

| Case | Stratum | original | candidate-targeted | candidate-fuller |
|---|---|---|---|---|
| invocation-tighten (native) | codex / gpt-5.6-sol / low | 3/3 pass | 3/3 pass | 3/3 pass |

- **Shared behavior (9/9):** every output put the decision first except targeted-2. Every output removed the intro, the communication digression and the duplicate mechanism section, and kept all safeguards. Lengths were 210–244 words.
- **Explicit causal link (untested gaps → pilot only):**
  - original 3/3 (rep 1 is a little overstated)
  - fuller 2/3
  - targeted 1/3

  This is the most visible difference. With three runs per condition it's a weak tendency, and the gap is small, because the link is easy to infer in a ~220-word document.
- **Safeguard detail:** "until investigated" appears in original-3 and targeted-2; "do not delete" appears only in targeted-3. These are scattered single observations, not a pattern.
- **Layout:** targeted-2's evidence-first order is a single observation.
- **Contribution:** No no-CW control exists, so these results can't show what CW adds. All three versions produced equally passing, high-quality edits. Neither draft is preferable to the original on this evidence; the targeted draft is marginally weaker on the explicit causal link, and that is still unresolved at n=3.

## Criterion and card issues (kept separate from scoring)
- **Contradiction:** The "Limits" section says F1–F3 apply only to "original/candidate-comprehensive". The "Applies to" lines list original, candidate-targeted and candidate-fuller. I followed "Applies to"; "candidate-comprehensive" looks like a stale label.
- **Source identity:** The card says the case reuses source A verbatim with "no duplicate copy". Here a copy was supplied, and I can't confirm it matches A.
- **N3 instructions:** The prompt includes N3 instructions, which don't apply to this case.

---

Now reading the prior assessment.
