## First-pass independent assessment (written before opening prior-assessment.md)

**Disclosure:** I did this review independently, but it was not blinded, because condition labels were visible in the filenames. I worked read-only and ran nothing.

**Scope and evidence.** The case is `document-addition` (E). There are 15 executions in one runtime stratum: Claude provider, `claude-sonnet-5`, CLI 2.1.305, effort low. That is 5 repetitions each of `control` (no CW), `original` and `candidate-targeted-examples`. I read every file the review depends on in full:
- all three source files (`report.md`, `TASK.md`, `NEW-NOTES.md`)
- `policy.txt`, `criteria.md`, `INTERPRETATION.md`
- all 15 outputs

`MECHANICAL-CHECKS.json` is `{}`, so the controller supplied no mechanical observations. Word counts come from `WORD-COUNTS.json`.

**What I checked.** These are the points from the source and the new notes that each output needs to keep or add:
- **Opt-in scope:** six teams continue, it is not the default, and the decision is about four more teams.
- **Evidence limits:**
  - 120 searches, 2 timeouts that both succeeded on retry
  - no evidence of lost documents, but nothing over 50,000 documents tested
  - a quiet support queue does not prove the results are correct
  - the four new teams each have under 20,000 documents, so adding them does not validate large collections
- **Strict >5% threshold:** a timeout rate over 5% in the preceding 24 hours means postpone and investigate.
- **Approval gates:** consent, ability to switch back, and Thursday approval.
- **New fallback contact:** Nia records a named fallback contact before each invitation is sent.
- **Pause:** a potentially incorrect result pauses only the affected team, and the query and returned result go into the restricted incident record.
- **Not confirmed:** the pause does not mean the report is a confirmed defect.
- **Other teams:** they continue unless the investigation finds a broader problem.
- **Resumption:** only after Omar investigates and Nia approves.
- **Review:** the seven-day review includes pauses and their outcomes.
- **Separate decision:** further expansion still needs its own decision, and the review does not authorize making the preview the default.

All 15 outputs leave the existing report content word for word except where the additions are merged in. Every output adds the fallback contact, the incident branch and the review evidence in sensible places, with no conflicting addendum left over. The "separate decision / not default" requirement is carried by "does not automatically authorize a wider rollout", "before deciding whether to expand again" and "The broader default-setting decision remains open" in every output.

### Per-output judgments

Word count changes are measured against `report.md` (279 words). `NEW-NOTES.md` is 166 words and `TASK.md` is 58. Every output is longer than the report. The growth is justified by the required additions, and E has no preference for shorter output.

| Run ID (suffix) | Condition / rep | F1 | F2 | F3 | Overall | Words (Δ vs report) |
|---|---|---|---|---|---|---|
| …958f0762-qynih0cm | control 1 | met | met | met | **pass** | 396 (+117) |
| …e02cc7c1-ojlca6q6 | control 2 | met | met | met | **pass** | 382 (+103) |
| …20a87609-obisloam | control 3 | met | met | met | **pass** | 386 (+107) |
| …48e12213-ymp1tvn8 | control 4 | met | met | met | **pass** | 381 (+102) |
| …adf17fd1-ilshpj0w | control 5 | met | met | met | **pass** | 398 (+119) |
| …a8846f6d-e0sydcqd | original 1 | met | met | met | **pass** | 363 (+84) |
| …c2dc552a-4qsik9ds | original 2 | met | met | met | **pass** | 358 (+79) |
| …a37977bc-iok3mzq6 | original 3 | met | met | met | **pass** | 361 (+82) |
| …570cf339-wb_j3a78 | original 4 | met | met | met | **pass** | 356 (+77) |
| …da466de9-9h21hw0e | original 5 | met | met | met | **pass** | 357 (+78) |
| …a40d58d4-syt0zh4e | candidate 1 | met | met | met | **pass** | 360 (+81) |
| …f8a82482-y9gjm7qw | candidate 2 | met | met | met | **pass** | 355 (+76) |
| …9a84cb78-r3ovtke0 | candidate 3 | met | met | met | **pass** | 362 (+83) |
| …c76dcb47-nf7ozblz | candidate 4 | met | met | met | **pass** | 359 (+80) |
| …68a9bcbb-tmmx2zc1 | candidate 5 | met | met | met | **pass** | 353 (+74) |

### Evidence by condition

**Controls (all 5).** The controls add the new material with nearly the notes' own wording, so they are the most precise.

- **Fallback contact (F1/F2):** The contact is a separate gate sentence, for example control-1:13 "Nia must also record a named fallback contact for each team before sending its invitation." This keeps both "record" and the before-sending timing. "If those checks pass" then covers it.
- **Incident branch:** Each control has its own incident section (control-1:17–19, control-2/3:17–19, control-4:17–19, control-5:17–19). All five keep the restricted record, the "does not imply… confirmed as a defect" qualification, the conditional continuation for other teams, and the Omar-then-Nia resumption gate.
- **Review and separate decision:** All five add pauses and their outcomes to the review. Control-1:23 and control-5:23 also spell out "separate decision"; control-5 adds "does not authorize enabling the preview by default."
- **Readability (F3):** One minor point: Nia's two pre-invitation duties are split across two sentences with Omar's timeout check between them (control-1:13). This is a small loss of grouping, not a real reading burden. Close repetition of the notes' wording is the reason the controls run 20–40 words longer than the skill outputs. None of that text is padding that gets in the way.

**Original (all 5).** The originals fold the fallback contact into Nia's confirmation list: "has agreed…, can switch back…, and has a named fallback contact on record" (orig-1/2/4:13). Orig-3/5:13 say "has a named fallback contact," without "on record".

- **Fallback contact (F1):** The CW-E-contact interpretation says confirming a named fallback before the invitation is enough, and treats explicit recording as a precision point. Because the confirmation sits under "Before inviting anyone" and is followed by "If those checks pass… Nia can send," the timing gate is kept. For orig-3/5, losing "record" is a precision observation, not an F1 failure.
- **Incident branch:** The sections are compact and correct. Orig-2:19 says "even before the report is confirmed as a defect." That keeps the point that the pause comes before confirmation. Its tone is a little weaker than "does not imply", but the meaning holds. Orig-1:19 keeps "does not mean the report is confirmed as a defect."
- **Resumption gate:** Every original keeps "resumes only after Omar investigates and Nia approves."
- **Readability (F3):** Grouping Nia's checks into one sentence reads slightly better than the controls.

**Candidate-targeted-examples (all 5).** These are structurally almost identical to the originals.

- **Fallback contact:** It is folded into Nia's list. "On record" appears in cand-3/4; cand-1/2/5 omit "record". This is the same precision observation as for the originals.
- **Candidate-1:19, the weakest wording in the sample.** It says the pause and retention happen "regardless of whether the report is later confirmed as a defect" instead of saying the pause does not imply confirmation.
  - **What survives:** In context, "potentially incorrect" plus "later confirmed" still tells the reader that the report is unconfirmed when the pause happens. The separate resumption gate stops anyone reading it as "the pause continues regardless".
  - **What is lost:** the explicit "precaution, not a finding" framing.
  - **Verdict:** I judge this a precision observation, not an introduced inaccuracy, so F1 is met. There is some uncertainty here, and a stricter reader might call it a shift in meaning.
- **Candidate-4:19, "This is a precaution, not a confirmed defect."** This is slightly loose grammatically, since the pause is the precaution and the report is what is unconfirmed. It still keeps the source's "precaution" framing.
- **Candidate-2/5:** These use a direct instruction ("Pause the preview for… that team"), which works well for action.
- **"Other teams":** Cand-2:19 has "Other teams may keep using the preview," where the source says "other participating teams". The meaning is the same.

### Condition comparison

**Functional pass counts** (E, Claude / sonnet-5 / CLI 2.1.305 / low effort):
- control: **5/5**
- original: **5/5**
- candidate-targeted-examples: **5/5**

There were no failures and no insufficient-evidence results in any factor.

**Quality differences among passing outputs:**
- **Precision favors the controls**, consistently across all five reps. They keep "record" and "before sending its invitation," "does not imply… already been confirmed," and, in 2 of 5, an explicit "separate decision".
- **The skill conditions trade some precision for brevity.** They consistently produce a tighter consolidated checklist and about 25–40 fewer words. This repeats across all ten skill outputs.
  - **Wording drift:** "Record" is dropped in 2/5 originals and 3/5 candidates. The "not confirmed" phrasing drifts once in each condition (orig-2 "even before", cand-1 "regardless of whether… later confirmed").
  - **Is it a regression?** None of these reaches F1 failure, so I count them as small precision regressions against the control, not functional regressions.
- **Readability:** The skill outputs have a small, recurring readability edge from grouping Nia's checks in one place. The incident sections are equally clear in all three conditions.
- **Original vs. candidate:** They are practically the same: same structure, same contact consolidation, similar word counts (356–363 vs 353–362). Neither draft is better in this sample. The one candidate wording issue (cand-1) and the one original wording softening (orig-2) are single observations, not patterns.

**Does CW contribute?** These results do not support a useful CW quality contribution for this case:
- The no-CW control already passes 5/5 and is slightly more faithful.
- The skill outputs are only modestly more concise (about 7–10% fewer words), and the case prefers neither shorter nor longer output.
- The sample is small and from development cases, so no reliable difference can be claimed in either direction.

Now reading prior-assessment.md.
