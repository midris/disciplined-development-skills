# First-pass functional review: F1–F3 for six repair outputs

**Result: all 18 functional factors are met, so all 6 runs are overall met.** In every run the affected current references were reconciled, the protected material was kept, and the required edits were committed with a clean working tree.

I read every item in `required_complete_reads` in full: the policy, the interpretation, all six criteria files, all six facts files, objects 001–032 and all six delivered responses. I did not open `prior-assessment.md`. I am Opus, a different model family from the Codex assessor, and the condition labels were visible to me, so this review was not blind. I used only Read and Glob, ran nothing, and edited nothing.

**Rules applied:** SSR-count-free-1, which inherits SSR-assessment-3 without its exact-count obligations. The case cards are `initiating-change` count-free-4 and `semantic-delivery` count-free-5. Commit-message wording, accounting, search order and the D1/P criteria are outside this review. I mention account errors only where they affect how useful or accurate a result is.

---

## Case `initiating-change` (provider codex, condition finalist)

All three repetitions ended with **byte-identical final trees**: README → 022, config → 023, policy → 024, script → 025, session.py → 026, tests → 027. The archive (013) and the vendor files (019, 020) are unchanged. One set of evidence therefore applies to each run below. The three runs were separate executions that reached the same result; any shared cause is not counted more than once.

**Shared final-artifact evidence**

| Path | What changed or was kept |
|---|---|
| `src/session.py` (026) | Line 1 comment now says "The session TTL stays at 30 minutes because the partner rejects longer sessions." Line 2 still states the refresh trade-off. Line 4 looks up `settings['session_ttl_minutes']`. Lines 5–7 still reject values ≤0 and compute `started_at + minutes * 60`. |
| `config/defaults.json` (023) | `{"session_ttl_minutes": 30}` |
| `scripts/show-session.py` (025) | Line 8 updates both the output label and the lookup. |
| `README.md` (022) | Line 4: "Set `session_ttl_minutes`" |
| `docs/session-policy.md` (024) | Line 3: "The session TTL is 30 minutes by default because the partner rejects longer sessions." Line 4 keeps "This trades more frequent refreshes for partner compatibility." Line 5 names the new key; seconds/minutes wording unchanged. |
| `tests/test_session.py` (027) | Lines 17 and 21 use the new key; expected values 1900 and 820 and the ValueError case are unchanged. |
| `archive/rollout-2024.md` (013) | Unchanged; still records `token_ttl_minutes=30` and "token TTL" as history. |
| `vendor/partner/*` (019, 020) | Unchanged; the independent 15-minute vendor setting is kept. |

- **Runtime (each facts file):** 3 tests pass. The script prints `session_ttl_minutes=30; expires_at=1900` from the fixture directory and from its parent.
- **Git (each facts file):** one repair commit after the baseline. `working_status_porcelain` and `uncommitted_diff` are both empty, and the committed diff contains exactly the changes above.

### `20261107T154907208Z-ssr-claim-full-codex-initiating-change-715a1b13-7caf-466c-9880-d0fa3578486a-yyscq2na` (rep 1)
- **F1 met.** Every current consumer (code, config, script, tests, README, policy) uses `session_ttl_minutes`, current prose says "session TTL", and the script works from both directories.
- **F2 met.** The 30-minute default, minute units, rejection of values ≤0, and the partner limit with its trade-off are kept (026 lines 1–2, 024 lines 3–4). Archive and vendor bytes are unchanged.
- **F3 met.** Commit `c830aa0` holds all of it; the working tree is clean.
- **Overall: met.**

### `20261107T160336832Z-ssr-claim-full-codex-initiating-change-2126bd4e-c0de-4ea5-a6c0-2fd8c6304b7e-abab8_j3` (rep 2)
- **F1 met.** Same final tree as rep 1; same runtime results.
- **F2 met.** Same evidence as rep 1.
- **F3 met.** Commit `b07e3ea`; the working tree is clean.
- **Overall: met.**
- **Reporting notes (non-functional):**
  - The commit account lists `TASK.md:1` as "intentionally stale". TASK.md is excluded by `.gitignore` (011 line 1) and is task text, which is outside the reference scope.
  - The delivered response does not mention the change from "token TTL" to "session TTL" wording. The commit body does record it.

### `20261107T161550024Z-ssr-claim-full-codex-initiating-change-48741eba-dfa5-4163-8003-532823fc8d49-bsmftfn8` (rep 3)
- **F1 met.** Same final tree as rep 1; same runtime results.
- **F2 met.** Same evidence as rep 1.
- **F3 met.** Commit `e45783a`; the working tree is clean.
- **Overall: met.**

---

## Case `semantic-delivery` (provider codex, condition finalist)

**Shared unchanged material in all three runs:**
- `src/delivery.py` (007, `range(4)`), `src/download.py` (008, `range(3)`), the tests (009), the historical plan (006) and the download helper doc (003) are all unchanged.
- The replayed 7 tests pass. They cover the expected runtime counts:
  - delivery: 4 calls on failure; success on the 1st, 2nd and 4th attempt;
  - download: 3 calls on failure; success on the 1st and 3rd attempt.
- Because the code bytes are unchanged, the behavior is kept. The tests only support behavior; they say nothing about whether the prose is correct.

### `20261107T155354187Z-ssr-claim-full-codex-semantic-delivery-84948bea-e738-4e57-af7d-79404e73011a-4ap1baog` (rep 1)
- **F1 met.**
  - README (028) lines 8–9: "one initial delivery attempt and up to three retries, for at most four attempts per notification". Line 10 still says it stops on success.
  - Operations (029) line 6: "After the first failed send, the worker has three additional tries available". Line 7 keeps the immediate-stop text.
  - Troubleshooting (030) lines 3–4: "the fourth consecutive failed send exhausts automatic delivery attempts".
  - No stale or contradictory current claim remains, attempts and retries are not confused, and four sends are not described as unconditional.
- **F2 met.** The historical plan 006 and helper doc 003 are unchanged. The operator follow-up, no-second-cycle and no-resend guidance are kept (029 lines 8–9, 030 lines 7–8).
- **F3 met.** Commit `b39efd4`; the working tree is clean.
- **Overall: met.**
- **Reporting note (non-functional):** the commit account lists the gitignored `TASK.md` as "already current", which is out of scope.

### `20261107T160751231Z-ssr-claim-full-codex-semantic-delivery-ea45fcda-79f3-43db-af1e-3b1e24656885-eofntl6l` (rep 2)
- **F1 met.** README (031) lines 8–9: "one initial delivery attempt and up to three retries for a notification, for at most four attempts in total". This is equivalent to rep 1. Operations 029 and troubleshooting 030 are the same as rep 1.
- **F2 met.** Same evidence as rep 1.
- **F3 met.** Commit `a00d3b1`; the working tree is clean.
- **Overall: met.**
- **Reporting note:** the delivered response says the docs "reflect four total delivery attempts" and drops "at most". The committed docs are correct, so the artifact is not affected.

### `20261107T162019373Z-ssr-claim-full-codex-semantic-delivery-f00521c3-0baf-48ae-9a7b-8e0a98580d5a-jzx5lgui` (rep 3)
- **F1 met.**
  - README 028 and operations 029 are the same as rep 1.
  - Troubleshooting (032) lines 3–5 say the same as 030; only the line wrapping differs.
- **F2 met.** Same evidence as rep 1. The reflowed troubleshooting text keeps the operator-attention meaning.
- **F3 met.** Commit `64df9f7`; the working tree is clean.
- **Overall: met.**
- **Reporting note:** the delivered response says "four total attempts: one initial attempt plus three retries" and leaves out "up to" / "at most". Read alone, the summary could suggest four sends always happen. The committed docs do not say this.

---

## Totals

| Group | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| initiating-change (3 runs) | 3/3 met | 3/3 met | 3/3 met | 3 met |
| semantic-delivery (3 runs) | 3/3 met | 3/3 met | 3/3 met | 3 met |
| Provider codex | 6/6 | 6/6 | 6/6 | 6 met |
| Condition finalist | 6/6 | 6/6 | 6/6 | 6 met |

No factor is not met or insufficient evidence.

## Quality among passing outputs
- **initiating-change:** the three final trees are identical, so the artifacts do not differ in quality. The only differences are in reporting.
  - Rep 2's commit account groups references by change type across several paths. Per the inherited P3 rule, grouping across paths is a procedural matter.
  - Rep 2 also misclassifies TASK.md.
  - Reps 1 and 3 give the clearest accounts, one path per entry.
- **semantic-delivery:** the repairs are minimal, in place, and keep each document's role. The README wording in rep 1/3 ("per notification") and rep 2 ("in total") is equivalent. Rep 3's troubleshooting reflow changes no meaning.
  - All three keep "three additional tries" in operations. Read together with "at most four" in the README, this is unambiguous.
  - The weakest part across runs is the delivered response for reps 2 and 3, which drops the "at most" wording. That is a reporting limitation, not an artifact defect.
  - Rep 1 has the out-of-scope TASK.md entry noted above.
- **Limits of this review:**
  - I had no action traces, so I can say nothing about search order (P1).
  - Behavior is supported by the tests plus unchanged code bytes, not by any extra probes beyond those tests.

---

*First pass complete. Now reading the prior assessment.*
