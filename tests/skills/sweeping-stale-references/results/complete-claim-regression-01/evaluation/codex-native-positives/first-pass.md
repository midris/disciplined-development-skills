# First-pass functional review: six repair outputs (codex, `finalist`)

**Overall: all six runs met F1, F2 and F3.** In every run, all affected current references were reconciled, the protected material was kept, and the required edits were committed. Each run has a single repair commit after the neutral baseline, with an empty working status and no uncommitted diff.

**Basis:**
- **Policy:** SSR-count-free-1 (2026-10-31), which inherits SSR-assessment-3 except for exact-count obligations.
- **Case cards:** `invocation-change` and `invocation-review`, both definition `claim-full-1`. Their inherited cards and expected-facts files were read in full.
- **Evidence read:** everything the index lists. That covers `policy.txt`, `INTERPRETATION.md`, all six criteria files, all six facts files, objects 001–032 (each unique object once) and all six delivered responses.
- **Not judged here:** D1, P criteria, the negative cases and the accounting diagnostic. They are outside this packet.

**Evidence limits:**
- I could not run code. I relied on the supplied hashes and object mappings, the `supplied_project_bytes_unchanged` flags and the runner's disposable replay records.
- For `invocation-review`, the replay records only the overall unittest result (7 tests OK), not separate call counts per scenario. `tests/test_retry_behavior.py` (object 020, unchanged) asserts exactly the call counts that `expected.json` requires, and `src/delivery.py` and `src/download.py` are byte-identical to the source. I judged that sufficient, not a gap.
- Who reviewed this: Opus, which is not the Codex assessor's family. The run labels were visible, so this review was not blinded.

---

## Case `invocation-change` (codex / finalist)

All three runs end with **the same final project tree**: objects 022–027 plus unchanged 001, 003, 009 and 010. They differ only in commit messages and delivered responses. Because the tree is shared, any defect would have been a single shared cause; there were none.

**What every run shows:**
- **F1 (complete useful change): met.**
  - The setting is renamed in `config/defaults.json` (023: `{"session_ttl_minutes": 30}`), in `src/session.py:4` (026, the lookup), in the script's label and lookup at `scripts/show-session.py:8` (025), and in `tests/test_session.py:17,21` (027).
  - The README (`README.md:4`, 022) and the policy doc (`docs/session-policy.md:3,5`, 024) now use the new key and the term "session TTL". The source comment at `src/session.py:1` also says "session TTL".
  - The replay shows tests OK (3) and the script printing `session_ttl_minutes=30; expires_at=1900` from both the repository and its parent directory.
  - No alias was kept, which the task allows.
- **F2 (preservation): met.**
  - The value 30, the minute units and the `minutes <= 0` → `ValueError` check are unchanged (026:5–7).
  - The partner limit and the refresh trade-off are kept in both the comment (026:1–2) and the policy doc (024:3–4).
  - `archive/rollout-2024.md` (003), `vendor/partner/README.md` (009) and `vendor/partner/example.json` (010, value 15) are byte-identical to the source.
  - `TASK.md` and `.gitignore` are unchanged.
- **F3 (committed completeness): met.** There is one commit after the baseline. Its diff contains all six required file changes, `working_status_porcelain` is empty and `uncommitted_diff` is empty.

| Full run ID | F1 | F2 | F3 | Overall | Run-specific evidence |
|---|---|---|---|---|---|
| `20261107T155609869Z-ssr-claim-full-codex-invocation-change-104366d5-2289-4f79-bf09-540b36afacbc-aaymv_xt` | met | met | met | **met** | Commit `b227b37` on top of baseline `8148ee5`; clean tree |
| `20261107T161002278Z-ssr-claim-full-codex-invocation-change-99de356c-490c-4ce1-9d6f-1101aacfaf95-gibfjrgn` | met | met | met | **met** | Commit `bde59b1` on top of baseline `37bc547`; clean tree |
| `20261107T162218587Z-ssr-claim-full-codex-invocation-change-c5b8aa84-860b-4706-8e57-f984d3b67133-x5zyxal9` | met | met | met | **met** | Commit `ea1c441` on top of baseline `5a6d1fa`; clean tree |

**Quality and reporting differences (none change a functional verdict):**
- The artifacts are identical, so there is no difference in what was built.
- **`…aaymv_xt`:**
  - Its account lists each file with the specific change made.
  - Its verification also reports that the legacy key is rejected with `KeyError`, which matches the code.
- **`…gibfjrgn`:**
  - Its account merges every update into one line. That is sparser, but the locations are complete.
  - Its delivered response says "CLI behavior remains unchanged", but the script's output label did change, from `token_ttl_minutes=` to `session_ttl_minutes=`. Only the values are unchanged, so that wording is slightly loose.
- **`…x5zyxal9`:** its response says "unchanged behaviorally", which is the more accurate phrasing. Its own verification ran the script only from the repository, but the independent replay covers the second working directory.
- **All three:** they correctly say the archive was left unchanged on purpose because it is historical, and that the vendor matches were false positives because they belong to an independent third-party setting.

## Case `invocation-review` (codex / finalist)

**What every run shows:**
- **Unchanged in all three:**
  - `src/delivery.py` (018), `src/download.py` (019) and `tests/test_retry_behavior.py` (020) are byte-identical to the source.
  - `docs/download-helper.md` (014) and `plans/completed/delivery-policy.md` (017) are unchanged.
  - `docs/troubleshooting.md` is object 030 in every run: "the fourth consecutive failed send exhausts", with the advice not to resend after a true result kept.
- **Replay:** 7 tests OK. Those tests cover delivery taking 4, 1, 2 and 4 calls and download taking 3, 1 and 3 calls, matching `expected.json`.

| Full run ID | Final files | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|
| `20261107T155837950Z-ssr-claim-full-codex-invocation-review-7a5f091c-b102-4679-95e3-28f87de266af-ggp6ttmv` | README 028, operations 029, troubleshooting 030 | met | met | met | **met** |
| `20261107T161213875Z-ssr-claim-full-codex-invocation-review-20b6c3ef-3814-45f6-8004-6dfb165d2c1d-20nx5cxi` | README 031, operations 032, troubleshooting 030 | met | met | met | **met** |
| `20261107T162419515Z-ssr-claim-full-codex-invocation-review-01277da4-6e2b-4956-97ee-dffa6c83d493-1rcq0k7t` | README 031, operations 029, troubleshooting 030 | met | met | met | **met** |

**F1 (complete, useful documentation): met for each run.**
- **README:**
  - 028 says "one initial delivery attempt and up to three retries, for at most four attempts per notification".
  - 031 says "…up to three retries for a notification, for at most four attempts in total".
  - Both keep "It stops as soon as delivery succeeds".
- **Operations:**
  - 029 says "three additional tries available". The next line, "Successful delivery ends processing immediately", stops this from reading as four unconditional sends.
  - 032 says "up to three additional tries available, for at most four attempts in total".
- **Troubleshooting:** 030 says four consecutive failures exhaust delivery.
- **No stale current claims remain**, attempts and retries are kept distinct, and the follow-up, no-second-cycle and no-resend guidance is all kept.

**F2 (preservation): met for each run.**
- The worker and helper code are unchanged, so both settled behaviors are kept.
- The historical plan, which records three attempts in total under the former policy, is unchanged.
- The download helper keeps its three-attempt limit.

**F3 (committed repair): met for each run.** Each has one repair commit (`b442d49`, `931ac63`, `bb2ec61`) whose diff contains all three document changes, with an empty working status and no uncommitted diff.

**Quality and reporting differences (none change a functional verdict):**
- **Clarity of the operations guide:** `…20nx5cxi` (object 032) is the most explicit, because it puts "up to" and "at most four in total" in the same sentence. `…ggp6ttmv` and `…1rcq0k7t` (object 029) leave the conditional reading to the next sentence. That is acceptable, but slightly weaker for an operator skimming one line.
- **README wording:** "per notification" (028) and "in total" (031) mean the same thing.
- **`…ggp6ttmv`'s account:**
  - It goes beyond the declared scope. It lists `TASK.md` as already current, and it lists `.agents/skills/…/SKILL.md:32-84` as a false positive, which is an ignored file outside the project.
  - Its line ranges (`docs/operations.md:6-9`, `docs/troubleshooting.md:3-8`) are wider than the text that changed.
  - None of this is functional.
- **`…20nx5cxi` and `…1rcq0k7t`:** their accounts stay closer to the declared reference scope.
- **Delivered responses:**
  - All three summarize the change as "four maximum attempts" without restating early stopping; the documents themselves keep it.
  - `…20nx5cxi` includes an absolute link into its own workspace path.
  - `…1rcq0k7t` says "Completed and committed both stages", which counts the neutral baseline as part of its work. The baseline is setup, so this is a framing point only.

## Totals

| Grouping | Runs | F1 met | F2 met | F3 met | Overall met / not met / insufficient evidence |
|---|---|---|---|---|---|
| `invocation-change` (codex, finalist) | 3 | 3 | 3 | 3 | 3 / 0 / 0 |
| `invocation-review` (codex, finalist) | 3 | 3 | 3 | 3 | 3 / 0 / 0 |
| Provider: codex | 6 | 6 | 6 | 6 | 6 / 0 / 0 |
| Condition: finalist | 6 | 6 | 6 | 6 | 6 / 0 / 0 |

That is 18 of 18 functional factors met and no failed executions. These are three descriptive attempts per case, not a reliability estimate, and they say nothing about invocation (D1) or procedure.

---

This message is the complete independent first pass. I have not searched for or read `prior-assessment.md`. Comparing against it is the next step: I would keep this first pass as it stands and list any changed factors or evidence separately by full run ID.
