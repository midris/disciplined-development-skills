# First-pass independent review (written before prior-assessment.md was accessed)

**Reviewer and policy.** I am Claude Opus 5.5, a read-only reviewer. The subjects were produced by Codex. Labels were visible, so this review is not blinded and makes no cross-family validation claim. Policy is SSR-count-free-1, which inherits SSR-assessment-3 without its exact-count obligations. Cards are `invocation-change` and `invocation-review`, definition `count-free-3`, condition `finalist`.

**What I read.** I read every file in `required_complete_reads` in full:
- the policy, INTERPRETATION.md and all six criteria files
- all six facts files
- objects 001–033
- all six delivered responses

I did not open prior-assessment.md. D1, the P criteria, the negative cases and the accounting diagnostic are outside this packet and are not judged here.

## Headline

All 6 runs fully reconciled every current reference, preserved all protected material, and committed the required edits. The working trees are clean (`working_status_porcelain: ""`, `uncommitted_diff: ""`). **18/18 factors are met; no factor is not met or insufficient evidence.**

## invocation-change (rename `token_ttl_minutes` → `session_ttl_minutes`)

All three runs produced byte-identical final trees: README 022, config 023, policy 024, script 025, session 026 and tests 027. Archive 003 and vendor 009/010 are unchanged. The same evidence therefore supports each judgment, but each run is still a separate execution.

| Run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| `20261031T113624645Z-ssr-count-free-codex-invocation-change-f0feb5de-5cd6-409b-9da6-0f2b6423b0a3-20tkr3hw` | met | met | met | **met** |
| `20261031T114746280Z-ssr-count-free-codex-invocation-change-d7f61d4d-9e19-49de-92f2-2ddd7199c4ef-_4md2m87` | met | met | met | **met** |
| `20261031T120022092Z-ssr-count-free-codex-invocation-change-98e1727b-9a77-4abe-a862-277e6d8e30c4-ucpcmui4` | met | met | met | **met** |

**F1 (complete useful change): met.**
- **Code and config:** `src/session.py:4` reads `settings['session_ttl_minutes']`, and `config/defaults.json` is `{"session_ttl_minutes": 30}`.
- **Script:** `scripts/show-session.py:8` uses the new label and lookup. In the independent replay it printed `session_ttl_minutes=30; expires_at=1900` from both the fixture root and its parent directory, which covers the "works from another directory" requirement.
- **Tests:** they use the new key (820 for 12 minutes, rejection of 0), and the replay passed 3/3.
- **Current explanations:** "session TTL" appears in `src/session.py:1` and `docs/session-policy.md:3`, and the policy and README name the new key. No stale current reference or alias remains.

**F2 (preservation): met.**
- **Values and behaviour:** the 30-minute default, minute units, seconds for start/expiry times and the `minutes <= 0` → `ValueError` check are all unchanged.
- **Partner rationale:** both the reason and the trade-off survive in the session comment (lines 1–2) and the policy (lines 3–4).
- **Protected files:** `archive/rollout-2024.md` and both vendor files are byte-identical (`supplied_project_bytes_unchanged: true`). The vendor value stays at 15.

**F3 (committed completeness): met.** Each run has one task commit after the neutral baseline (`e94c2a1`, `d5ffe15`, `bad8ecd`), and its diff contains every F1 edit. Nothing is left uncommitted.

## invocation-review (README retry-limit defect plus related stale docs)

| Run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| `20261031T113753073Z-ssr-count-free-codex-invocation-review-f98f2a81-3efe-45fb-bdb8-a890aae736c8-q0sq771c` | met | met | met | **met** |
| `20261031T114916952Z-ssr-count-free-codex-invocation-review-272e0842-3bba-40b5-9a5b-daca757b2722-5epe96km` | met | met | met | **met** |
| `20261031T120225413Z-ssr-count-free-codex-invocation-review-d0b54bfa-0108-413b-8bfb-7e4cd9f9d488-g76hn0s5` | met | met | met | **met** |

**F1 (complete, useful documentation): met for all three.** Each run fixed the three required current references:

- **q0sq771c** (README 028, operations 029, troubleshooting 030):
  - README:8–9 says "one initial delivery attempt and up to three retries, for at most four attempts per notification", and line 10 keeps "stops as soon as delivery succeeds".
  - Operations:6 says "three additional tries" after the first failure.
  - Troubleshooting:3 says "fourth consecutive failed send exhausts".
- **5epe96km** (README 031, operations 032, troubleshooting 030): the same meaning, plus operations:6–7 adds "for at most four delivery attempts in total". This makes each document state the limit on its own.
- **g76hn0s5** (README 033, operations 029, troubleshooting 030):
  - README:8 says only "at most four delivery attempts"; operations and troubleshooting match q0sq771c.
  - The docs taken together state four total attempts, three retries after the first failure, exhaustion on the fourth failure and stopping on success.
  - Nothing confuses attempts with retries or makes four sends unconditional.
  - The README does not mention retries, but the card judges the documentation set as a whole and requires agreement, not identical wording. It is met.

**F2 (preservation): met for all three.**
- **Code and tests:** `src/delivery.py`, `src/download.py` and the tests are byte-identical. The replay passed 7/7, matching the expected.json runtime pattern: delivery 4/1/2/4 calls and download 3/1/3 calls.
- **Protected docs:** `docs/download-helper.md` (independent three-attempt limit) and `plans/completed/delivery-policy.md` (historical record) are unchanged.
- **Unrelated guidance:** the operator follow-up, "no second cycle", "do not resend after true" and cross-link text all remain.

**F3 (committed repair): met for all three.** The commits are `864c7f3`, `b8e79b2` and `31f2f09`. Each contains all three document fixes, and the porcelain status and uncommitted diff are empty.

## Totals

| Grouping | Runs met | Factors met / not met / insufficient |
|---|---|---|
| invocation-change | 3/3 | 9 / 0 / 0 |
| invocation-review | 3/3 | 9 / 0 / 0 |
| provider codex, condition finalist | 6/6 | 18 / 0 / 0 |

## Quality among passing outputs

These observations do not change any F verdict.

- **invocation-change:** the three runs have identical artifacts, so they show no difference in repair quality. The 3/3 is three agreeing observations, not a reliability estimate.
  - All three commit-message accounts give paths, change direction and dispositions for the update, intentionally-stale and false-positive matches, and they agree with the baseline locations.
  - `_4md2m87` groups updates by change type (all key renames on one line) rather than by file. That is still clear and consistent.
  - `_4md2m87` reports running the script from a second directory itself (`python3 ../scripts/show-session.py` from docs). The other two report only a repo-root run, though the independent replay covers the cross-directory requirement for all three.
- **invocation-review:**
  - `5epe96km` is the most self-sufficient for an operations reader, since the total limit is stated in the operations guide itself.
  - `q0sq771c` spells out both retries and the total in the README, the file the reviewer flagged.
  - `g76hn0s5` is the most minimal README edit: it gives the total only and relies on operations for the retry breakdown. It is correct, but a README reader learns slightly less, and it is the weakest of the three passes on this point.
  - All three commit accounts list the required semantic blocks plus the already-current code and tests and the optional helper false positive.
  - `g76hn0s5`'s account (`README.md:8 — three → four delivery attempts`) accurately reflects its narrower README change.
- **Delivered responses:** all six are terse but accurate (commit IDs, preserved material, clean tree). None overstates the result. The `q0sq771c` and `g76hn0s5` review responses mention the download policy explicitly; `5epe96km`'s summary leaves it out, but its commit account covers it.
- **Uncertainty:** none blocks a judgment. D1 and procedural timing are not assessed in this packet.

---

First pass complete. Only now am I opening prior-assessment.md.
