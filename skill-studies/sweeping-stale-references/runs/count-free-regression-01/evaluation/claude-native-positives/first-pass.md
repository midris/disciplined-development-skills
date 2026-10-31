# First-pass functional review: count-free finalist, Claude native positives

**Result: all 6 runs are overall met, and all 18 functional factors (F1–F3 for each run) are met. All affected current references were reconciled, the material that had to be protected was preserved, and every required edit is committed with a clean working tree.**

**Basis:** policy SSR-count-free-1, which inherits SSR-assessment-3 without its exact-count rules. Case cards: `invocation-change` count-free-3 and `invocation-review` count-free-3, plus the inherited cards and the controller reference files (`invocation-change-expected.md`, `invocation-review-expected.json`). I am a fresh Opus reviewer from a different family than the Codex assessor. The labels were visible and the subjects are Opus, the same family as me, so I make no claim of blinding or cross-family validation. I used only Read and Glob and ran nothing. Runtime results below come from the runner's facts files, not from my own replay.

**What I read:** every file in `required_complete_reads`, in full, before judging. That covers the policy, the interpretation file, all six criteria files, all six facts files, objects 001–032 and all six delivered responses. I have not located or opened `prior-assessment.md`. D1, the procedural P criteria, both negative cases and the accounting diagnostic are not in this packet and are not judged here.

## Case `invocation-change` (rename `token_ttl_minutes` → `session_ttl_minutes`)

All three runs end with the same final tree, byte for byte: objects 022–027, with 001, 003, 009 and 010 unchanged. The functional verdicts therefore share one cause, and the outcome counts below are not independent evidence.

**Evidence shared by all three runs:**
- **F1 (complete useful change):** every place that reads or documents the setting now uses the new name:
  - `src/session.py:4` reads `settings['session_ttl_minutes']`.
  - `config/defaults.json` is `{"session_ttl_minutes": 30}`.
  - `scripts/show-session.py:8` uses the new key and prints the new label.
  - Both test fixtures use the new key.
  - `README.md:4` uses the new key.
  - `docs/session-policy.md:3,5` says "session TTL" and uses the new key.
  - The comment in `src/session.py:1` says "session TTL".
  - The runner's replay passed 3 tests. The script printed `session_ttl_minutes=30; expires_at=1900` when run from the fixture directory and from its parent. No current text keeps the old meaning or contradicts the new one.
- **F2 (preservation):**
  - The 30-minute default, minute units, `<= 0` rejection and `* 60` arithmetic are unchanged.
  - The partner-rejection reason and the accepted cost of more frequent refreshes are kept in both `src/session.py:1-2` and `docs/session-policy.md:3-4`.
  - `archive/rollout-2024.md` (object 003) and both vendor files (objects 009 and 010) are byte-identical to the source.
- **F3 (committed completeness):** there is one task commit after `fixture baseline`, the porcelain status is empty and the uncommitted diff is empty. The committed diff contains the complete F1 change set.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261031T113715839Z-ssr-count-free-claude-invocation-change-9d518b56-d641-4635-833d-47f586dc7808-7us5rvqn | met | met | met (commit `edf12c3`) | **met** |
| 20261031T114655830Z-ssr-count-free-claude-invocation-change-74b1fd77-f097-4e69-9569-e62c962772bf-m_p7fuwh | met | met | met (commit `ce8534f`) | **met** |
| 20261031T120137970Z-ssr-count-free-claude-invocation-change-51ede39f-bbb1-4d90-b5fb-43c0dcff1276-lv7k7lj3 | met | met | met (commit `45e7000`) | **met** |

## Case `invocation-review` (document the four-attempt delivery limit)

All three runs end with the same `docs/operations.md` (object 029) and `docs/troubleshooting.md` (object 030). Their READMEs differ only in wording and line wrapping: objects 028, 031 and 032. `src/`, `tests/`, `plans/` and `docs/download-helper.md` are unchanged in every run.

**Evidence shared by all three runs:**
- **F1 (complete useful documentation):** all three stale current claims are corrected.
  - **README:** "at most four delivery attempts" and "one initial attempt and up to three retries". Line 9 keeps "stops as soon as delivery succeeds", so four sends are never described as unconditional.
  - **Operations guide:** "After the first failed send, the worker has three additional tries available." The next line still says success ends processing immediately.
  - **Troubleshooting guide:** "the fourth consecutive failed send exhausts automatic delivery attempts".
  - Attempts and retries are never confused, and all operator guidance stays in place.
- **F2 (preservation):**
  - `src/delivery.py` (`range(4)`) and `src/download.py` (`range(3)`) are unchanged.
  - The runner's replay passed 7 tests, matching the controller's expected runtime results for both delivery and download.
  - The historical policy file (object 017) and the download-helper doc (object 014) are byte-identical, so the former three-attempt meaning and the helper's three-attempt limit survive.
- **F3 (committed repair):** there is one task commit after the baseline. The status and uncommitted diff are both empty, and the committed diff covers all three documents.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261031T113842998Z-ssr-count-free-claude-invocation-review-c9dea6b7-28a3-408d-a2c9-0f4282048245-7blieivv | met (README 028) | met | met (commit `8d1db53`) | **met** |
| 20261031T114839183Z-ssr-count-free-claude-invocation-review-5c82f072-f91f-485f-b6ee-8dfc857b14f8-25cwrlt0 | met (README 031, parenthetical wording) | met | met (commit `da30cbb`) | **met** |
| 20261031T120336629Z-ssr-count-free-claude-invocation-review-fd514768-bf19-4b10-8a2f-c58d576151c9-2010ts_p | met (README 032, wrapped line; renders the same in Markdown) | met | met (commit `ba37a2c`) | **met** |

## Totals

| Group | Runs overall met | Factors met | Not met | Insufficient evidence |
|---|---|---|---|---|
| Case `invocation-change` | 3/3 | 9/9 | 0 | 0 |
| Case `invocation-review` | 3/3 | 9/9 | 0 | 0 |
| Provider `claude` | 6/6 | 18/18 | 0 | 0 |
| Condition `finalist` | 6/6 | 18/18 | 0 | 0 |

Each case's three repetitions produced the same functional artifact, so 3/3 is one outcome repeated three times. It is not three independent confirmations, and it says nothing about reliability.

## Quality observations among the passing runs

The functional artifacts are equivalent within each case, so the differences are only in the reporting. They are reporting matters, not functional criteria.

**`invocation-change`:**
- **7us5rvqn:** the commit message is just a subject line with no `References swept:` section. The delivered response still covers the updates, the archive and vendor exclusions, and the verification.
  - Saying the script prints "the same result as before" is true of the values, but the printed label changed.
  - The audit account is weaker than in the other two runs because it isn't in the commit.
- **m_p7fuwh:** the commit has a full path, line and change account, which matches the reference scope.
  - Two small inaccuracies:
    - It lists `TASK.md:1` as a "false positive". Task text is outside the declared reference scope, so the label is off, though nothing was harmed.
    - The response says `TASK.md` was left unchanged "as you asked". The task never asked for that.
  - Neither affects the repair or preservation status.
- **lv7k7lj3:** the commit and response accounts are both complete and accurate, and the account stays inside the declared scope. It is the cleanest report of the three.

**`invocation-review`:**
- **7blieivv:** the commit has a full `References swept:` account covering the four required blocks, the optional download-helper block, and code and tests that were already current.
  - The entry `README.md:17 — false positive: "third-party package"` is a trivial match that adds noise without harm.
  - This is the most auditable commit of the three.
- **25cwrlt0:** the commit message is just a subject line. The response accurately lists the three updates and the two items deliberately left alone, and correctly explains that `TASK.md` was excluded from the baseline by `.gitignore`.
- **2010ts_p:** the commit message is just a subject line. The response is accurate and complete, and gives the commit by subject rather than hash.

None of these reporting differences makes the essential repair or preservation status untrustworthy. Every response agrees with the Git facts and final trees.

## Limits

- No traces were supplied, so this pass cannot say anything about search order, skill loading or timing (D1/P).
- The byte-unchanged flags and runtime results come from the runner. I checked them against the complete object contents but did not run anything myself.

I have not yet opened `prior-assessment.md`. In a follow-up turn I can read it and report, by full run ID, any factor or evidence that differs from this pass, without changing what is recorded here.
