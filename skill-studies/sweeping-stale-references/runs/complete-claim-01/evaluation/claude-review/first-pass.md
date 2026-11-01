# First-pass functional review: invocation-review (policy SSR-count-free-1, inheriting SSR-assessment-3)

**Bottom line:** All 4 runs fixed every affected current reference correctly, kept the protected material intact, and committed all the required edits. So F1, F2 and F3 are **met** for every run (12 of 12 factors), and each run is **met** overall. D1 and the procedural P criteria are left to the active session, as instructed.

**Reviewer context:** I'm a fresh Opus reviewer. Condition labels were visible to me, and the Claude subjects are the same model family as me. This was not blinded and is not a cross-family check. I only read files, ran no code and edited nothing. I read every required file in full before judging: the policy, the interpretation, 3 criteria files, 4 facts files, objects 001–014 and 4 outputs.

**Gaps in the packet:**
- The packaging note mentions a PNG asset and an unchanged `.runtime` Click dependency. Neither is listed in the sources, objects or `required_complete_reads`, and `qualified_runtime_dependency` is `[]`. Nothing was missing for this case, and it doesn't affect any judgment.
- There are no subject traces, so I make no claims about search order or completeness of process.

## Ground truth used (from the source objects and the expected file)
- **Worker:** `src/delivery.py:6` uses `range(4)` and returns as soon as a send succeeds.
- **Download helper:** `src/download.py:6` uses `range(3)`.
- **Current references that needed updating:**
  - README.md:8: "at most three delivery attempts"
  - docs/operations.md:6: "two additional tries"
  - docs/troubleshooting.md:3: "third consecutive failed send exhausts"
- **Must stay as is:**
  - plans/completed/delivery-policy.md:4–5 is a historical record.
  - docs/download-helper.md:4 is a false positive (the helper's own limit).
- **Useful guidance that had to survive:**
  - operations.md:7–9: stop on success, record for follow-up, no second cycle.
  - troubleshooting.md:4–8: a false result needs operator attention; don't resend after a true result.
  - README.md:9–13: stop on success, links to the guides, the helper is separate.

## Shared final state
| File | 4koj7b7u | v_bg_edn | yf09u4wv | l_xq6rz1 |
|---|---|---|---|---|
| README.md | 011 | 011 | 011 | 014 |
| docs/operations.md | 012 | 012 | 012 | 012 |
| docs/troubleshooting.md | 013 | 013 | 013 | 013 |
| all other files | unchanged source | same | same | same |

- **Three runs are identical:** 4koj7b7u, v_bg_edn and yf09u4wv have byte-identical final projects. They are scored separately, but they share one artifact.
- **The fourth run differs only in README wording:** l_xq6rz1 (object 014) moves the explanation after a colon instead of a parenthesis. The meaning is the same.

## Per-run judgments

### `20261101T011955725Z-ssr-claim-claude-invocation-review-current-131e178a-a1af-44b6-9450-9b301115ca7a-4koj7b7u` (claude, current, rep 1)
- **F1 met.** The three docs now agree:
  - 011:8 says "at most four delivery attempts (one initial attempt and up to three retries)", and :9 keeps "stops as soon as delivery succeeds".
  - 012:6 says "three additional tries", and :7 keeps "ends processing immediately".
  - 013:3 says "the fourth consecutive failed send exhausts".
  - Nothing says four sends always happen, and attempts and retries are not mixed up. All the guidance lines remain.
- **F2 met.**
  - Code, tests, `docs/download-helper.md` and the historical plan are unchanged per `supplied_project_bytes_unchanged`.
  - The independent unittest replay ran 7 tests and passed (exit 0). Those tests encode exactly the expected runtime behaviour: delivery 4/1/2/4 calls, download 3/1/3.
  - The only changes are the single-line rewrites shown in the diff. All guidance is kept.
- **F3 met.** Commit `a2b880a` comes after the baseline `227cb74` and contains all three edits. Both `working_status_porcelain` and `uncommitted_diff` are empty.
- **Overall: met.**

### `20261101T012035899Z-ssr-claim-claude-invocation-review-candidate-729e2c34-de27-4ddb-8533-09c3d88516de-v_bg_edn` (claude, candidate, rep 1)
- **F1 met.** Same final docs (011/012/013) with the same evidence as above.
- **F2 met.** The unchanged-bytes map is identical, and the replay passed 7 tests with exit 0.
- **F3 met.** Commit `27aa3aa` comes after baseline `08fa69e`, and the working tree is clean.
- **Overall: met.**

### `20261101T012119266Z-ssr-claim-claude-invocation-review-candidate-6ae32f53-75a2-4fce-ba5f-8f83e11ff31c-yf09u4wv` (claude, candidate, rep 2)
- **F1 met.** Same final docs (011/012/013).
- **F2 met.** Same unchanged-bytes map, and the replay passed.
- **F3 met.** Commit `e34d91b` comes after baseline `ade8484`, and the working tree is clean.
- **Overall: met.**

### `20261101T012205406Z-ssr-claim-claude-invocation-review-current-ad51ace4-c681-4684-b5a1-edd8e6fd4a95-l_xq6rz1` (claude, current, rep 2)
- **F1 met.** 014:8 says "at most four delivery attempts for a notification: one initial attempt and up to three retries", and :9 keeps the stop-on-success line. Operations and troubleshooting are 012/013 as in the other runs.
- **F2 met.** Same unchanged-bytes map, and the replay passed.
- **F3 met.** Commit `f6c577c` comes after baseline `c2489d2`, and the working tree is clean.
- **Overall: met.**

## Totals
| Slice | Runs met / total | Factors met / total |
|---|---|---|
| Case invocation-review | 4/4 | 12/12 |
| Provider claude | 4/4 | 12/12 |
| Condition current | 2/2 | 6/6 |
| Condition candidate | 2/2 | 6/6 |

- No result is "not met" or "insufficient evidence".
- The runs show no functional difference between conditions. With n=2 per condition, I make no causal or reliability claim.

## Quality observations among the passing outputs
None of these points changes a functional verdict.

**Final artifacts:**
- All four make minimal in-place fixes that keep each document's original role. That fits this small fixture.
- l_xq6rz1's colon wording (014:8) reads a little more smoothly than the mid-sentence parenthesis in 011:8. This is style only.
- Every run keeps operations.md's original "tries" wording (012:6) instead of saying "retries". It is accurate and consistent with the README's "up to three retries".

**Reporting accuracy in the commit messages and responses** (these are not F criteria):
- **4koj7b7u:** the most accurate account of what the re-search found. The response (line 14) lists the remaining hits ("three retries", "three additional tries", "third-party"), which matches 011/012/013.
- **v_bg_edn:**
  - It is the only run that names `src/download.py:6` as part of the download-helper false positive.
  - It says the matches left after the re-search are "the ones listed above". That holds if the listed changed lines count as matches.
- **yf09u4wv:** its commit-message reference account (the "References swept" list) leaves out README.md:17 "third-party". That is allowed, because incidental number matches are excluded. However, the response's line 13 says the message "lists every file the search turned up". Without traces, I can't tell whether its search would have hit "third-party", so this claim can't be verified.
- **l_xq6rz1:**
  - The response's line 15 says "the only 'three' and 'third' matches left are the download helper and 'third-party'".
  - That is inaccurate for the README/docs it says it searched: 014:8 ("three retries") and 012:6 ("three additional tries") also contain "three".
  - This is a small misstatement in the report, not a defect in the artifact. Its commit message also uses "…" inside the quoted replacement text.
- **All runs** classify the historical plan as intentionally stale and the download helper as a false positive, which matches the expected file. 4koj7b7u gives the plan the broader range `:1-6`, while the others use `:4-5`. Both are acceptable.

My first pass is complete above and stays as written. I'm opening the prior assessment only now, as the prompt allows.
