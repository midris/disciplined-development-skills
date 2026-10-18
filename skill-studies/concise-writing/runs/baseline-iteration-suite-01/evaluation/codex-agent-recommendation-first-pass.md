## First-pass independent assessment (written before opening prior-assessment.md)

**Disclosure:** This review is independent but not blinded, because the condition labels were visible. I read every file I needed in full: EVALUATION-INDEX.json, both source_files (`sources/report.md` and `sources/TASK.md`), `criteria.md`, `policy.txt`, MECHANICAL-CHECKS.json (`{}`, so it records no controller observations), WORD-COUNTS.json and all 12 outputs. Nothing was left partly read. The case is A-type editing (agent-recommendation), run on Codex gpt-5.6-sol at low effort, all in one stratum. It is measured under F1–F3; N3 rules do not apply.

**What the reader needs from the source (625 words):** whether to approve a 30-minute pilot on ten internal accounts on Tuesday, 10:00–11:00. Maya runs it and Leo compares row counts. It is not a general release.

Supporting evidence:
- 50 staging exports all matched.
- In 3 injected upload failures, the cursor held and no rows were lost.
- How the fix works: the cursor advances only after upload. Production's current version advances it before upload, so a failure can drop rows.

Limits:
- Staging only. Production traffic, production-sized data and a cross-region outage were not tested, and this is the stated reason for limiting the pilot.
- The change has not been deployed.

Actions:
- On a mismatch, stop and keep both files, and don't delete them before investigation. The files show whether the rows were lost at source selection or at upload.
- On a match, return for a separate general-release decision rather than expanding automatically.

### Per-output judgments

| Run ID (prefix) | Condition / rep | F1 | F2 | F3 | Overall | Words (Δ vs 625) |
|---|---|---|---|---|---|---|
| 20261018T163332960Z…807003c3 | control / 1 | met | met | met | **pass** | 224 (−401) |
| 20261018T163848522Z…28615740 | control / 2 | met | met | met | **pass** | 234 (−391) |
| 20261018T164029409Z…99d110c9 | control / 3 | met | met | met | **pass** | 196 (−429) |
| 20261018T163426022Z…80bed02a | original / 1 | met | met | met | **pass** | 243 (−382) |
| 20261018T163648790Z…78d44923 | original / 2 | met | met | met | **pass** | 228 (−397) |
| 20261018T164107612Z…c7ae56cd | original / 3 | met | met | met | **pass** | 221 (−404) |
| 20261018T163528329Z…ca997521 | targeted / 1 | met | met | met | **pass** | 219 (−406) |
| 20261018T163728325Z…aea01fda | targeted / 2 | met | met | met | **pass** | 195 (−430) |
| 20261018T163919129Z…961233ed | targeted / 3 | met | met | met | **pass** | 233 (−392) |
| 20261018T163611129Z…95a6b0cb | fuller / 1 | met | met | met | **pass** | 218 (−407) |
| 20261018T163807986Z…ae0309f5 | fuller / 2 | met | met | met | **pass** | 244 (−381) |
| 20261018T163957463Z…23959f90 | fuller / 3 | met | met | met | **pass** | 237 (−388) |

**Points common to all 12 outputs:**
- **F3 met:** each one deletes the communication digression and the duplicate mechanism section, and puts the decision first.
- **F1 met:** none adds an unsupported conclusion. Each keeps the ten-account scope, the time window, Maya and Leo's roles, and both outcome branches.
- **Length:** all are about 63–69% shorter than the source.

**Evidence and notes by output:**

- **control-1**
  - **Kept:** "This is not a request to approve a general release." It states the reason for the limit ("production-sized data and cross-region failure behavior remain untested"), says "has not been deployed", keeps the explicit "Do not delete either file", says "Do not expand the rollout automatically" and keeps the closing confirm action.
  - **Weaknesses:**
    - It drops the reason for keeping the files (source selection vs upload). The instruction itself stays, so the reader can still act safely.
    - "production-scale traffic" merges the source's separate "production traffic" and "production-sized dataset". The meaning still gets through.
- **control-2**
  - **Kept:** all evidence, the limits ("do not establish production performance or cross-region safety"), a numbered mismatch procedure, the match branch and the confirm action.
  - **Weaknesses:**
    - It never states that the untested conditions are *why* the pilot is limited. Limits and safeguards sit together under one heading, so the reader has to infer the link. It is easy to infer, so I don't count it as a lost decision input, but it is a real weakening.
    - It turns the files' purpose into a pilot step ("Determine whether the discrepancy came from source selection or upload"). That reframes evidence as a task and assigns it to no one.
    - "Production remains on the current version until the pilot results are reviewed and a separate general-release decision is made" is a slight forward inference. It is consistent with the source.
- **control-3**
  - **Strengths:** the heading "Why a limited pilot" makes the causal link, and it keeps "production still uses the current version", both branches and the confirm action.
  - **Weaknesses:**
    - It drops the reason for keeping the files and the explicit don't-delete warning. "Retain … for investigation" carries the instruction.
    - "Production-traffic performance" folds into "production-sized data", which is acceptable.
- **original-1:** the most complete of the 12.
  - **Kept:** all three untested conditions, plus "They do not establish production-traffic performance or cross-region safety". It ties the limit to the limits ("so the first production exposure should be limited"), includes not-deployed, gives the reason for keeping the files and closes with a confirm.
  - **Weakness:** none material.
- **original-2:** complete, with the reason for keeping the files.
  - **Weakness:** "Limiting the first production exposure … addresses this uncertainty" overstates slightly. A limited pilot contains the risk; it does not resolve it. In context this is not misleading.
- **original-3:** complete, with the causal link ("These gaps are why…"), numbered mismatch steps and the reason for keeping the files.
  - **Weaknesses:**
    - There is no closing "confirm" line, but the opening "Please approve a pilot…" carries the request.
    - It says "had matching row counts" instead of "completed". Neither gap matters.
- **targeted-1**
  - **Strengths:** both outcome branches sit right under the decision, which works well for someone about to act. It includes the causal link ("This uncertainty is why…"), the reason for keeping the files and not-deployed.
  - **Weakness:** the mechanism comes last under "What changes", after the evidence it explains. This is a valid layout.
- **targeted-2:** the shortest output.
  - **Weaknesses:**
    - It merges the retry mechanism into the evidence sentence ("allowing the failed batch to be retried without losing rows"). That is faithful.
    - Like control-2, it lacks an explicit sentence saying the untested conditions are why the pilot is limited. The "Evidence and remaining risk" heading puts them side by side.
    - "has not been deployed" is implied by "Production still uses the current version".
    - There is no confirm line; "Decision needed" carries the request.
  - **Judgment:** passes, but it is the thinnest skill output on the decision rationale.
- **targeted-3:** complete, with the causal link, not-deployed and the reason for keeping the files.
  - **Weakness:** it splits the outcome branches. The match branch sits in the decision section and the mismatch branch in a final "Stop condition" section. This partly recreates the source's scattered instructions, but each branch is clearly labelled, so I don't count it as an F3 failure.
- **fuller-1:** complete, with the causal link, both branches together, the reason for keeping the files, not-deployed and the confirm line.
  - **Weakness:** the "Recommendation" heading sits over an "Approve…" request. That is a cosmetic quibble.
- **fuller-2:** complete, with the reason for keeping the files.
  - **Weaknesses:**
    - It restates the limits twice in one paragraph ("do not establish…" then "Neither … was tested, which is why…"). That is mild repetition but it delivers the causal link.
    - It splits the branches the same way targeted-3 does.
    - It has no explicit not-deployed or confirm line. Both are carried by "Production still uses the current version" and "Approve…".
- **fuller-3:** complete, with the causal link, branches together, the reason for keeping the files, not-deployed and the confirm line.
  - **Weakness:** none material.

### Condition comparison

**Measured functional passes** (one stratum: Codex gpt-5.6-sol, low effort; no N3 in scope):

| Condition | Pass | Fail | Insufficient |
|---|---|---|---|
| control (no CW) | 3/3 | 0 | 0 |
| original | 3/3 | 0 | 0 |
| candidate-targeted | 3/3 | 0 | 0 |
| candidate-fuller | 3/3 | 0 | 0 |

Average words: control 218, original 231, targeted 216, fuller 233. These differences are small and are not a quality signal.

**Quality differences among passing outputs:**
- **Reason for keeping the files.** All 9 skill-bearing outputs keep it as the reason for retention ("needed to determine whether rows were lost during source selection or upload"). No control keeps it in that form: control-1 and control-3 drop it, and control-2 turns it into an unassigned step. This held across all repetitions, but it is a small fidelity and safeguard gain. Control-1 makes up for part of it with an explicit "Do not delete either file".
- **Why the pilot is limited.** Control-1 and control-3, all three originals, targeted-1, targeted-3 and all three fullers state it. Control-2 and targeted-2 leave it implicit. So this weakness appears once in a control and once in a skill output; it is not tied to a condition.
- **Layout.** Targeted-3 and fuller-2 split the outcome branches. The originals and fuller-1/3 are the most complete and well ordered. Targeted-1 puts the action branches first, which is the most action-oriented layout.

**Conclusion:** the controls already pass 3/3, so the pass counts show no CW contribution. On quality, the skill-bearing outputs are slightly better on one recurring point: they keep the reason for retaining the files. Neither draft beats the original. The original and fuller look marginally more consistent than targeted, but n=3 cannot settle that. Any CW contribution here is at most marginal and is unresolved.

Now opening the prior assessment.
