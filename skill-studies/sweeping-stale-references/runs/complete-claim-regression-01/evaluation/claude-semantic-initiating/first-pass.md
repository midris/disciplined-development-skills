# Independent first pass: F1–F3 functional review

**Bottom line:** All six repair outputs meet F1, F2 and F3, so all six are met overall (18/18 factors). In every run, all the references that needed changing were changed, the material that had to stay was kept, and the fix was committed with nothing left uncommitted.

**Basis and limits:** I judged these under SSR-count-free-1, which inherits SSR-assessment-3 except for its exact-count rules. The case cards were `initiating-change` count-free-4 and `semantic-delivery` count-free-5, with their inherited cards and expected files. I read every file listed in `required_complete_reads` in full: policy, interpretation, all six criteria files, all six facts files, objects 001–030 and all six outputs. I used only Read and Glob, ran no code and edited nothing. I did not open `prior-assessment.md`.

I am an Opus reviewer and the subjects are labelled Claude/Opus, so this is the same model family. The review is not blinded and is not a cross-family check. No subject traces were supplied, so I made no D1 or P1–P3 judgments. The commit-message quality notes below are descriptive only and do not affect F1–F3.

All three runs in each case produced byte-identical final projects (the same object hashes). The F1–F3 judgments within a case therefore rest on the same artifact evidence. Each run is still its own execution with its own Git history and its own replay, and I checked each one separately.

---

## Case `initiating-change` (claude / finalist)

These three runs share final objects 022–027. Objects 011, 013, 019 and 020 are byte-identical to the source.

**F1 evidence (shared final artifacts):**
- **Code:** `src/session.py` (obj 026) reads `settings['session_ttl_minutes']`, and its comment now says "The session TTL".
- **Config:** `config/defaults.json` (obj 023) is `{"session_ttl_minutes": 30}`.
- **Script:** `scripts/show-session.py` (obj 025) uses the new key for both the label and the lookup.
- **Tests:** `tests/test_session.py` (obj 027) uses the new key in the custom (12) and invalid (0) cases.
- **Docs:** `docs/session-policy.md` (obj 024) says "session TTL" and `session_ttl_minutes`. `README.md` (obj 022) line 4 uses the new key.
- **Leftovers:** No current file still contains `token_ttl_minutes` or "token TTL". No alias was added, as the task allowed.
- **Replay:** Each facts file shows 3 tests passing. The script prints `session_ttl_minutes=30; expires_at=1900` from both the fixture directory and its parent. That matches the expected results (30 → 1900, 12 → 820, nonpositive values rejected).

**F2 evidence:**
- **Values and behaviour:** The value 30, minutes as the unit, the `minutes * 60` calculation and the `<= 0` → `ValueError` check are all unchanged.
- **Rationale:** The partner-limit reason and the refresh trade-off are kept in both the code comment (obj 026, lines 1–2) and the policy doc (obj 024, lines 3–4).
- **Protected files:** `archive/rollout-2024.md` (obj 013) and the two `vendor/partner/*` files (obj 019, obj 020, still 15) are byte-unchanged, per `supplied_project_bytes_unchanged`.

**F3 evidence:** Each run has a baseline commit plus one rename commit. In each, `working_status_porcelain` and `uncommitted_diff` are empty, and `complete_project_diff` contains all six required file edits.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| `20261107T155033291Z-ssr-claim-full-claude-initiating-change-360e156e-61b3-4906-877f-0ee914a0b41b-bb427l37` | met | met | met (commit `c3d19a3`, clean tree) | **met** |
| `20261107T160247744Z-ssr-claim-full-claude-initiating-change-76124df8-085a-41b9-8f0d-837a8be847cb-pmsfkfnk` | met | met | met (commit `926c4c8`, clean tree) | **met** |
| `20261107T161719043Z-ssr-claim-full-claude-initiating-change-48bc1bdf-4ce8-46d2-9010-c03396e4ead4-tv5iqs3h` | met | met | met (commit `a974f0e`, clean tree) | **met** |

## Case `semantic-delivery` (claude / finalist)

These three runs share final objects 028–030. Objects 001, 003 and 006–009 are byte-identical to the source.

**F1 evidence (shared final artifacts):**
- **`README.md:8` (obj 028):** "at most four delivery attempts (one initial attempt and up to three retries)". Line 9 still says it stops on success.
- **`docs/operations.md:6` (obj 029):** "After the first failed send, the worker has three additional tries available." This correctly counts retries after the first failure, and line 7 still says success stops processing at once.
- **`docs/troubleshooting.md:3` (obj 030):** "the fourth consecutive failed send exhausts".
- **Agreement:** All three docs now agree on at most four sends, up to three retries, exhaustion after four failures and stopping on success. None of them says four sends always happen, and none mixes up attempts with retries. The operator guidance (record the notification for follow-up, don't start a second delivery cycle, don't resend after `true`) is unchanged.
- **Replay:** Each run passes 7/7 tests. That matches the expected runtime, but it does not by itself prove the prose is correct.

**F2 evidence:** `src/delivery.py` (`range(4)`), `src/download.py` (`range(3)`), `docs/download-helper.md`, the historical `plans/completed/delivery-policy.md` and the tests are all byte-unchanged.

**F3 evidence:** Each run has a baseline commit plus one fix commit containing all three doc edits. The working tree and uncommitted diff are empty.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| `20261107T155510438Z-ssr-claim-full-claude-semantic-delivery-f2f5a015-705b-46be-8ca2-fbc2c4d9f81a-1in2tke7` | met | met | met (commit `433ec13`, clean tree) | **met** |
| `20261107T160651983Z-ssr-claim-full-claude-semantic-delivery-a9581887-c2a4-48aa-a2d0-5911bd921998-_wfu0ng3` | met | met | met (commit `74c15b0`, clean tree) | **met** |
| `20261107T162136476Z-ssr-claim-full-claude-semantic-delivery-34d1179f-7604-467f-8480-bd54488348ae-x9kbnnlf` | met | met | met (commit `d986388`, clean tree) | **met** |

## Totals

| Grouping | Runs met / total | Factors met |
|---|---|---|
| `initiating-change`, claude, finalist | 3/3 | 9/9 |
| `semantic-delivery`, claude, finalist | 3/3 | 9/9 |
| **claude, finalist (all)** | **6/6** | **18/18** |

No run failed and none was rated insufficient evidence. There were no shared-cause failures to merge.

## Quality differences among passing outputs

The final artifacts are identical within each case, so the outputs differ only in how they report the work. None of these points changes F1–F3.

1. **Same fix within each case:** Every run made the same minimal edits that keep the meaning intact. For `semantic-delivery`, all three went past the one file the reviewer named and also fixed the operations and troubleshooting docs, which the case required. For `initiating-change`, all three kept the rationale rather than just renaming things.

2. **`_wfu0ng3` has imprecise locations:** Its commit body cites `src/download.py:1` as a false positive, but line 1 is the module docstring and the three-attempt limit is `range(3)` on line 6. It cites only `tests/test_retry_behavior.py:40`, though the download tests span lines 34–40. It also groups three different files on one line. These are commit-message accuracy and grouping issues only. On the plus side, it is the only run that recorded the unchanged success and false-result wording as "already current".

3. **`x9kbnnlf` overstates its search result:** Its final message says a re-search of the delivery docs for "three", "two" and "third" left "third-party package" as the only hit. That cannot be literally true: the fixed `README.md:8` ("up to three retries") and `docs/operations.md:6` ("three additional tries") now contain "three". Its commit body ("no stale limit remains") is accurate. The code-level claim is right, but the self-report is less trustworthy. Its range `tests/test_retry_behavior.py:22-31` also stops one line short of the fourth-attempt test, which ends at line 32.

4. **`1in2tke7`'s account is accurate:** Its locations check out against the source. It correctly lists `README.md:17` "third-party" as an unrelated match.

5. **`initiating-change` accounts:** All three accurately map the supplied line locations and outcomes. All three group the two `vendor/partner/*` files on one line. `bb427l37` and `pmsfkfnk` give practically the same account. `tv5iqs3h` adds harmless detail (the repo-local Git identity, deleting `__pycache__`, which `.gitignore` excludes anyway) and explains each update most clearly for a reader.

---

I have now finished the independent first pass and deliberately stopped before opening `prior-assessment.md`. If you'd like the comparison, tell me in your next message. I'll then read it, leave this first pass as it stands, and list any factors or evidence that differ, by full run ID.
