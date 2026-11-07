# First pass: independent functional review (written before any access to prior-assessment.md)

**Policy and context.** I applied SSR-count-free-1, which inherits SSR-assessment-3 except its exact-count obligations, together with the `claim-full-1` case cards for `invocation-change` and `invocation-review` and the inherited controller facts (`invocation-change-expected.md`, `invocation-review-expected.json`). I'm an Opus reviewer, and the subjects are Claude Opus 5.5 runs from the same family. Condition labels were visible and nothing was blinded, so none of this counts as cross-family validation.

**What I read.** I read everything on the required list in full: the policy, the interpretation note, all six criteria files, all six facts files, objects 001–031 and all six delivered responses. I didn't read prior-assessment.md, any skill body or any traces, and I ran no code.

**Scope.** Only F1–F3 are judged here. D1 and the procedural P criteria stay with the active session.

## Lead result
In all six runs:
- every affected current reference was reconciled,
- protected material was kept intact,
- the required edits were committed, with a clean worktree and an empty uncommitted diff.

## invocation-change (task: rename `token_ttl_minutes` → `session_ttl_minutes`, use "session TTL", no alias required)

All three repetitions produced byte-identical final projects: objects 022–027, with 001/003/009/010 unchanged. The shared evidence below therefore applies to each run, but each repetition is still judged as its own execution.

- **F1 (complete useful change):**
  - The config (`023`: `{"session_ttl_minutes": 30}`), `src/session.py:4` (`026`), `scripts/show-session.py:8` (label and lookup, `025`) and `tests/test_session.py:17,21` (`027`) all use the new key.
  - The README line 4 (`022`) and `docs/session-policy.md:3,5` (`024`) say "session TTL" / `session_ttl_minutes`.
  - The replay ran 3 tests OK. The script printed `session_ttl_minutes=30; expires_at=1900` both from the fixture directory and from its parent, so it works from another working directory.
  - No current old name or old concept is left anywhere.
- **F2 (preservation):**
  - Value 30, minutes→seconds (`*60`) and the `minutes <= 0` → `ValueError` check are unchanged.
  - The partner limit and the refresh trade-off are kept in both `026:1-2` and `024:3-4`.
  - `archive/rollout-2024.md` (003) and both vendor files (009, 010 with value 15) are byte-identical.
- **F3 (committed completeness):** one repair commit follows the baseline. `complete_project_diff` contains all six edits, the porcelain status is empty and the uncommitted diff is empty.

| Run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261107T155747876Z-ssr-claim-full-claude-invocation-change-17ff30f0-4ddf-4c22-974c-fd321ca905a1-2_ovb7f3 | met | met | met (commit e7153f8) | **met** |
| 20261107T160915204Z-ssr-claim-full-claude-invocation-change-f61763fe-c3a0-452c-a54f-39b986768619-4r6mnbm6 | met | met | met (commit 8194b8e) | **met** |
| 20261107T162336222Z-ssr-claim-full-claude-invocation-change-07805bfc-9b0a-48f4-bcc8-a1ec680cf173-y9ye0ybu | met | met | met (commit c828de8) | **met** |

## invocation-review (task: README contradicts the four-attempt worker; fix and commit)

All three runs changed the same three documents with the same meaning. Run 3's README (`031`) differs from `028` only by a line wrap.

- **F1 (complete, useful documentation):**
  - **README (`028:8`/`031:8-9`):** "at most four delivery attempts … one initial attempt and up to three retries". Line 9 still says it stops on success.
  - **Operations (`029:6`):** "After the first failed send, the worker has three additional tries available." That is up to three further attempts after the first failure, so attempts and retries aren't confused. The success-stops line 7 is kept.
  - **Troubleshooting (`030:3`):** "the fourth consecutive failed send exhausts". The true-result guidance on lines 7–8 is kept.
  - Nothing implies four sends happen unconditionally, and no current claim is left stale.
- **F2 (preservation):**
  - `src/delivery.py` (018), `src/download.py` (019), the tests (020), `docs/download-helper.md` (014, still three attempts) and `plans/completed/delivery-policy.md` (017, still the historical three-attempt record) are byte-identical.
  - The replay ran 7 tests OK, covering delivery with 4/1/2/4 calls and download with 3/1/3 calls, which matches expected.json.
- **F3 (committed repair):** each run has one repair commit containing all three document edits, a clean porcelain status and an empty uncommitted diff.

| Run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261107T155957267Z-ssr-claim-full-claude-invocation-review-1ee37310-f232-4304-9730-c24515d89de0-scx_2ug_ | met | met | met (commit 4541852) | **met** |
| 20261107T161129832Z-ssr-claim-full-claude-invocation-review-e88cdadf-56e3-42f4-b138-4d980ab660fd-2t19yecv | met | met | met (commit 724871d) | **met** |
| 20261107T162530338Z-ssr-claim-full-claude-invocation-review-edb2ef77-2200-4b4a-a1ba-8f773b29781b-f1ad7wjl | met | met | met (commit b448036) | **met** |

## Totals
| Grouping | Runs met / total | Factors met / total |
|---|---|---|
| invocation-change | 3/3 | 9/9 |
| invocation-review | 3/3 | 9/9 |
| Provider: claude | 6/6 | 18/18 |
| Condition: finalist | 6/6 | 18/18 |

There are no failed factors and no insufficient-evidence factors, so there are no shared causes to separate.

## Quality observations among passing outputs
These don't affect F1–F3.

- **The change case is effectively one repair produced three times.** The final bytes are identical, so differences are only in reporting:
  - **Rep 1 and rep 2:** the commit messages give file:line locations for all updates, the archive (intentionally stale) and vendor (false positive), and say the partner rationale and trade-off were kept.
  - **Rep 3:** the commit message names only the "partner-rejects-longer-sessions rationale". Its response also leaves out the refresh trade-off, although the files still contain it. That makes rep 3's account of what was preserved a little less complete.
  - **Rep 2's response** usefully warns that any config still using the old name will now fail, which is the practical consequence of having no alias.
  - **Reps 1 and 2** list `TASK.md` as a "false positive". That's harmless, but it's outside the declared reference scope.
- **The review case:**
  - **Rep 1's response** openly admits that the re-search its commit message describes was actually run after committing. That's an honest correction, but it means the commit-message wording is slightly inaccurate about timing.
  - **Rep 2's commit account** is the most complete. It covers every required block, the optional independent helper, the already-current code and tests, and an incidental "third-party" match.
  - **Rep 3's commit message has no `References swept:` account at all**, only a subject line and a co-author line. Its delivered response does name the locations and outcomes, but the audit trail that reviewers use doesn't live in the commit. Under the policy this is an accounting/procedural defect, not a functional one.
  - **No run changed the code.** That's correct, because the worker already implemented the settled policy.

*End of first pass. Only now am I opening prior-assessment.md.*
