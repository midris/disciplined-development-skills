# First-pass independent functional review: invocation-review (functional repair outputs only)

**Policy and criteria:** SSR-count-free-1 (inherits SSR-assessment-3; exact-count obligations superseded). Case card `criteria/invocation-review.md` (definition `claim-1`) with inherited card `criteria/invocation-review-inherited.md`. Reference facts are in `criteria/invocation-review-expected.json`.

**Assessor context:** Opus 5.5, active session. Labels were visible. This is not blinded, and it is not a cross-family check of the Opus subjects. D1 and P criteria are not judged here.

**What I read:** every required item in the index. That covers policy.txt, INTERPRETATION.md, the 3 criteria files, the 4 facts files, objects 001–016 and the 4 delivered responses. I did not open prior-assessment.md.

**Packet notes:**
- The index's `packaging` text mentions a `.runtime` Click dependency and a PNG asset. Neither appears in this index, and `qualified_runtime_dependency` is `[]`. This looks like template wording and does not affect any judgment.
- `TASK.md` is missing from every final mapping. That is expected: `.gitignore` (object 001) ignores it, and the facts record `TASK.md: true` (unchanged).

## Shared source baseline
- **Code:** `src/delivery.py` (007) runs `range(4)` and stops on success. `src/download.py` (008) runs `range(3)`.
- **Tests:** the tests (009) cover exhaustion and early success for both operations.
- **Stale current claims in the source:**
  - README:8 says "at most three delivery attempts".
  - operations:6 says "two additional tries".
  - troubleshooting:3 says "third consecutive failed send exhausts".
- **Must be preserved:** the historical plan (006) and the independent helper doc (003).

## Shared final state (all 4 runs)
- **Same edits in every run:** `docs/operations.md` becomes object 012 and `docs/troubleshooting.md` becomes object 013.
  - Operations:6 now says "three additional tries". The early-stop line, the operator follow-up line and the "no second cycle" line are unchanged.
  - Troubleshooting:3 now says "fourth consecutive failed send exhausts". The true/false guidance in lines 4–8 is unchanged.
- **Untouched in every run:** objects 001, 003, 006, 007, 008 and 009 are byte-identical to the source. The facts confirm this: helper doc, historical plan, both source files and tests all show `true`.
- **Only README differs between runs.**
- **Runtime:** a disposable replay passed 7 tests in every run. This only confirms that the worker (4 calls) and helper (3 calls) behave as expected. It says nothing about whether the prose is correct.
- **Git:** every run shows a two-commit history (baseline, then repair), an empty `working_status_porcelain` and an empty `uncommitted_diff`.
- **Shared F3 caveat:** in every response the subject says it created the "fixture baseline" commit itself. No per-commit diff is supplied. So the conclusion that the edits sit in the repair commit rests on three things: the commit messages, the identical supplied-blob pre-images (`ce67c5d`, `1ae2955`, `dd8fc17`) in the full diff, and the clean tree. Every required edit is committed in every run either way. Which commit holds them is a grouping/attribution question (P2), not a gap in committed completeness.

## Per-run judgments

### `20261101T011811762Z-ssr-claim-codex-invocation-review-current-1f699f48-1abb-46cb-a359-31ba16902938-5i0m38v6` (codex / current / rep 1)
- **F1 met.**
  - README (011:8–10) says "one initial delivery attempt and up to three retries … for at most four attempts total" and keeps "stops as soon as delivery succeeds".
  - Operations (012:6) says "three additional tries". Troubleshooting (013:3) says "fourth consecutive failed send".
  - No current contradictions remain, attempts and retries are not confused, and four sends are not stated as unconditional. The cross-links in README:12–14 still resolve.
- **F2 met.**
  - Code and tests are unchanged, and the runtime observations match `expected.json`.
  - The historical plan (006) and helper doc (003) are byte-identical. All other operator guidance survives.
- **F3 met.** Repair commit `1861bfe` exists, and the working tree and uncommitted diff are both empty.
- **Overall: met.**

### `20261101T011907031Z-ssr-claim-codex-invocation-review-candidate-d567aa17-dbf5-4a6c-88ec-ceb38c4887b5-a02kgvgz` (codex / candidate / rep 1)
- **F1 met.**
  - README (014:8) says only "at most four delivery attempts for a notification", plus the unchanged success/exhaustion line.
  - This is accurate. It uses "at most", so four sends are not unconditional.
  - The README does not mention retries. Read as a whole, though, the docs agree: operations (012:6) supplies the "three additional tries after the first failure" framing, and troubleshooting (013:3) gives four-failure exhaustion. No guidance was removed.
- **F2 met.** Same preservation evidence as above: 003, 006, 007, 008 and 009 are unchanged, and the runtime replay matches.
- **F3 met.** Repair commit `c8c5618` exists, and the tree is clean.
- **Overall: met.**

### `20261101T012244680Z-ssr-claim-codex-invocation-review-candidate-6dbb1a63-1b27-46c4-8523-61e80ef10cf8-hlwzcaze` (codex / candidate / rep 2)
- **F1 met.**
  - README (015:8–9) says "one initial delivery attempt and up to three retries, for at most four attempts per notification". The early-stop line is kept.
  - Operations and troubleshooting are the same as in the other runs.
- **F2 met.** Same preservation evidence: all protected objects are unchanged, and the runtime replay matches.
- **F3 met.** Repair commit `b6915e6` exists, and the tree is clean.
- **Overall: met.**

### `20261101T012337490Z-ssr-claim-codex-invocation-review-current-21cf95da-857b-4247-a4f3-42798319304d-024hnwyt` (codex / current / rep 2)
- **F1 met.**
  - README (016:8–9) says "one initial delivery attempt and up to three retries for a notification, for at most four attempts in total". The early-stop line is kept.
  - Operations and troubleshooting are the same as in the other runs.
- **F2 met.** Same preservation evidence: all protected objects are unchanged, and the runtime replay matches.
- **F3 met.** Repair commit `b2c5f94` exists, and the tree is clean.
- **Overall: met.**

## Totals
| Slice | F1 | F2 | F3 | Overall met |
|---|---|---|---|---|
| invocation-review (4 runs) | 4/4 | 4/4 | 4/4 | 4/4 |
| codex | 4/4 | 4/4 | 4/4 | 4/4 |
| current (rep 1, rep 2) | 2/2 | 2/2 | 2/2 | 2/2 |
| candidate (rep 1, rep 2) | 2/2 | 2/2 | 2/2 | 2/2 |

- No failures and no insufficient-evidence results.
- No shared-cause failures need deduplicating.
- Four runs on one small exposed case support no reliability or condition-difference claim.

## Quality observations among passing outputs
- **README wording:**
  - Three runs (current rep 1, current rep 2, candidate rep 2) state both forms in the README: one initial attempt plus up to three retries, and at most four in total. That matches the task's own wording, heads off attempt-versus-retry confusion for overview readers, and lines up with the "additional tries" wording in operations.
  - Candidate rep 1's "at most four delivery attempts" is correct and the smallest possible fix. It is a little less self-contained for overview readers but is not deficient.
  - This is a minor difference in consequence, not a pass/fail split, and it does not line up with condition: one candidate run took each approach, and both current runs took the fuller one.
- **Breadth of the sweep:**
  - All four runs went beyond the single README defect the reviewer named and fixed the two other stale current claims, which is the substantive outcome being tested.
  - None touched the historical plan or the helper. None restructured docs unnecessarily.
- **Commit accounts:** every `References swept:` block correctly covers all four required blocks (three updates, plus the historical plan marked intentionally stale). Every block also includes the optional helper false positive and the already-current code/tests.
  - Candidate rep 2 adds the useful note that early-stop and operator handling were already current.
  - Current rep 2 does not record a repeated-search verification, unlike the other three. That is only an accounting/procedure note.
- **Delivered responses:** all are short and accurate about commits and checks.
  - Current rep 2 says it "Preserved … worker behavior". That is true, since the code is unchanged.
  - None of the responses spells out which three docs got which change, beyond naming the files. The commit messages carry that detail.

---

The first pass is complete. Now reading the prior assessment.
