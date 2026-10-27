# Independent first pass: invocation-change and invocation-review, Codex native-positive repair outputs

**Reviewer:** Opus 5.5 (`claude-opus-5-5`), a fresh Opus reviewer. I'm not from the active Codex assessor's model family, but I share a family with the Opus subjects. Condition labels were visible, so nothing here was blinded and I don't claim cross-family subject validation. I used Read/Glob only, with no code execution and no project edits. I have not located or read `prior-assessment.md`.

**Inputs read in full:** `EVALUATION-INDEX.json`, `policy.txt` (SSR-assessment-3), `INTERPRETATION.md`, all six criteria files, all 22 fact files, all 22 delivered responses, and all 34 unique objects (001–034).

**Packet discrepancies (no effect on scoring):**
- The index scope text mentions "original/comprehensive/compact labels", an "unchanged .runtime Click dependency" and a "PNG asset". None of these are in this packet. Both cases have `qualified_runtime_dependency: []`, the object list has no PNG, and the runs are labelled `original` / `candidate` / `finalist`.
- I did not assume which of candidate/finalist corresponds to comprehensive or compact.

**Scope:** Only F1–F3 are judged. D1, the P criteria, P3 accounting and loading/trace questions are left to the active session. The responses' self-reports of using SSR ("Applied the `sweeping-stale-references` skill…") are not evidence for anything here.

## Result

**All 66 functional factors are met. All 22 outputs are overall met. There are no failures and no unknowns.** In every run, every affected current reference was reconciled, protected material was preserved, and the required edits were committed in a single commit after the neutral baseline, with no uncommitted changes.

## Case invocation-change (11 runs)

**Shared evidence.** All 11 runs map to the same final objects: README 022, config 023, policy 024, script 025, session.py 026, tests 027. Archive 003 and vendor 009/010 are unchanged. Each fact file shows the same diff, one task commit after `fixture baseline`, an empty porcelain status and an empty uncommitted diff.

- **F1:**
  - `src/session.py` (026) reads `settings['session_ttl_minutes']`, and its comment now says "session TTL".
  - `config/defaults.json` is `{"session_ttl_minutes": 30}`.
  - The script reads and prints `session_ttl_minutes`. Runtime shows `session_ttl_minutes=30; expires_at=1900` both from the repository and from another directory.
  - The tests use the new key, as do README line 4 and policy lines 3 and 5.
  - No current file still contains `token_ttl_minutes` or "token TTL". No alias was added, which the task allows.
- **F2:**
  - Values (30, 12→820, 100→1900), minute and second units, and the `<= 0` check that raises `ValueError` are unchanged. The candidate/finalist probe also shows zero and negative values raise `ValueError`.
  - The partner limit and the refresh trade-off are kept in both the code comment (026 lines 1–2) and the policy (024 lines 3–4).
  - `archive/rollout-2024.md` and the vendor README/JSON are byte-unchanged. That is correct, because they are historical or independent settings.
- **F3:** There is one commit after the baseline and the working tree is clean.

| Full run ID | Condition | Rep | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| 20261026T134245334Z-ssr-fresh-baseline-codex-invocation-change-f0f0a9ee-37d0-466b-abf4-4ba50bb9030e-8joxuexg | original | 1 | met | met | met | met (commit `2fe72d9`) |
| 20261026T143618995Z-ssr-fresh-baseline-codex-invocation-change-8e62c8d0-fd1b-476d-9bce-ad7d42e475df-x9tj5hw9 | original | 2 | met | met | met | met (`04cd1d0`) |
| 20261026T150117283Z-ssr-fresh-baseline-codex-invocation-change-dbb48864-3418-4976-8f5f-8e1dac46c320-1hlsr6yu | original | 3 | met | met | met | met (`264b6d6`) |
| 20261026T152934740Z-ssr-fresh-baseline-codex-invocation-change-851ff07c-9b8e-48ae-900d-01569aa001d2-m67mwqvl | original | 4 | met | met | met | met (`9a65925`) |
| 20261026T155930969Z-ssr-fresh-baseline-codex-invocation-change-badd3adf-2c86-44de-8ec8-10e60e2a784b-juvar6m0 | original | 5 | met | met | met | met (`1c42dcb`) |
| 20261026T205305311Z-ssr-screen-codex-invocation-change-candidate-4867cd89-09bd-4bbb-81e0-c070a1b4236d-co2yij6t | candidate | 1 | met | met | met | met (`8e2b7c6`) |
| 20261026T213601032Z-ssr-screen-codex-invocation-change-candidate-ab35c656-b6e3-4835-b42f-db825d4c44f5-v0s8shsd | candidate | 2 | met | met | met | met (`4b05018`) |
| 20261026T231928229Z-ssr-screen-codex-invocation-change-candidate-b6bf6463-4beb-4875-851d-e1e136638e96-m_75cpxs | candidate | 3 | met | met | met | met (`c53d0a4`) |
| 20261026T205200723Z-ssr-screen-codex-invocation-change-finalist-898af4f8-c6a8-4072-b2cf-a8abf8bd899c-0yq8fgda | finalist | 1 | met | met | met | met (`dddf2d3`) |
| 20261026T213725688Z-ssr-screen-codex-invocation-change-finalist-18fbe788-21dd-4291-bf85-d2ca87ee4e1e-ah208ag9 | finalist | 2 | met | met | met | met (`300288d`) |
| 20261026T231831214Z-ssr-screen-codex-invocation-change-finalist-330da997-eca5-491b-85ff-0b8a9bde10b0-p5bmfqf0 | finalist | 3 | met | met | met | met (`0ea8672`) |

## Case invocation-review (11 runs)

**Shared evidence.**
- Code (018/019), tests (020), the download-helper doc (014) and the historical plan (017) are byte-unchanged in every run.
- Troubleshooting is 030 in every run: "the fourth consecutive failed send exhausts".
- Operations is 029 ("three additional tries available") or 033 ("up to three additional tries available"). In both, the next line says success ends processing immediately.
- The runtime probe matches `expected.json` exactly: delivery 4/1/2/4 calls and download 3/1/3 calls.
- Each run has one commit after the baseline, a clean working tree and no uncommitted diff.

**How the README variants were judged.** The judgment unit is the whole current documentation set. 028, 031 and 032 state both "one initial … up to three retries" and "at most four attempts". 034 says only "one initial delivery attempt and up to three retries" and doesn't state the total. That still means at most four sends, ending on success. It doesn't confuse attempts with retries, and the operations and troubleshooting docs agree with it, so F1 is met.

| Full run ID | Condition | Rep | README / ops | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|---|
| 20261026T135904152Z-ssr-fresh-baseline-codex-invocation-review-31649107-f152-4b8b-8e2c-a16167e02426-3ywc8wq4 | original | 1 | 028 / 029 | met | met | met | met (`a105148`) |
| 20261026T144440056Z-ssr-fresh-baseline-codex-invocation-review-b52a9798-cc51-40b4-a3ff-6449616186ec-0u6xy1kc | original | 2 | 031 / 029 | met | met | met | met (`80b8d59`) |
| 20261026T151006832Z-ssr-fresh-baseline-codex-invocation-review-8b77a4cc-a528-4553-98bc-77150e8feb14-yxaiykrt | original | 3 | 032 / 029 | met | met | met | met (`bc201a4`) |
| 20261026T153813745Z-ssr-fresh-baseline-codex-invocation-review-b193f5c0-6ae0-4a5a-ad1e-3d0131b94cc8-070pzqtm | original | 4 | 032 / 029 | met | met | met | met (`9d276a3`) |
| 20261026T161052183Z-ssr-fresh-baseline-codex-invocation-review-6a00071d-9d44-495d-9ed6-c3d29526328e-s2cddd8y | original | 5 | 031 / 033 | met | met | met | met (`340ae7b`) |
| 20261026T205445588Z-ssr-screen-codex-invocation-review-candidate-56f0913f-2065-45f7-9c01-5571f82f45a1-cwx_fjag | candidate | 1 | 031 / 029 | met | met | met | met (`6fde84a`) |
| 20261026T214138608Z-ssr-screen-codex-invocation-review-candidate-4b1e465c-057f-44a7-85b8-d5b7cfbf8757-6nvm1z5a | candidate | 2 | 034 / 029 | met | met | met | met (`dfc3629`) |
| 20261026T232030161Z-ssr-screen-codex-invocation-review-candidate-867f196b-f414-41e6-9d1b-804574cb91e7-9xmbm_t3 | candidate | 3 | 031 / 033 | met | met | met | met (`3099dc7`) |
| 20261026T205622496Z-ssr-screen-codex-invocation-review-finalist-fd0dc116-b15d-47cc-bdd4-08408b4a89a8-l8ag_o9y | finalist | 1 | 032 / 029 | met | met | met | met (`30041d0`) |
| 20261026T214011854Z-ssr-screen-codex-invocation-review-finalist-bb2abd2b-f0f7-460f-82db-66c573d88c50-nmkx8_0e | finalist | 2 | 032 / 029 | met | met | met | met (`8e99f2a`) |
| 20261026T232201546Z-ssr-screen-codex-invocation-review-finalist-f9847ff2-6a8a-45d0-8011-c27c1bc48d65-f251m57q | finalist | 3 | 031 / 029 | met | met | met | met (`9bb4042`) |

## Totals (provider: Codex only)

| Case | Condition | Runs | F met / judged | Overall met | Not met | Insufficient evidence |
|---|---|---|---|---|---|---|
| invocation-change | original | 5 | 15/15 | 5 | 0 | 0 |
| invocation-change | candidate | 3 | 9/9 | 3 | 0 | 0 |
| invocation-change | finalist | 3 | 9/9 | 3 | 0 | 0 |
| invocation-review | original | 5 | 15/15 | 5 | 0 | 0 |
| invocation-review | candidate | 3 | 9/9 | 3 | 0 | 0 |
| invocation-review | finalist | 3 | 9/9 | 3 | 0 | 0 |
| **All** | | **22** | **66/66** | **22** | **0** | **0** |

## Quality observations

1. **invocation-change: the artifacts can't separate the conditions.** All 11 final projects are byte-identical: minimal token→session substitutions with the rationale left in place. Any difference between versions here would have to come from procedure or tracing, not from the outcome.
2. **invocation-review: small wording differences, none consequential.**
   - Ops 033 ("up to three additional tries") is slightly more precise than 029 ("three additional tries"). It appears in original rep 5 and candidate rep 3.
   - README 034 (candidate rep 2) is the least explicit for an overview reader, because the total of four has to be inferred. It's still correct and consistent, so I don't count it as a consequential regression.
   - 034's delivered response says the docs "state four maximum attempts", but the README doesn't literally say that. This is a minor inaccuracy in the self-report, not a defect in the artifact.
3. **No output did unrequested work.** None touched code, tests, the helper or the historical plan, and none added a compatibility alias in invocation-change. The final trees contain only supplied files: no stray files, and `TASK.md` was not committed.
4. **Limits on what I could check:**
   - Commit bodies aren't supplied; I only have one-line subjects. So claims like "documented dispositions in the commit" (candidate rep 1, invocation-change) or "record the sweep in the commit body" (original rep 5, invocation-review) can't be checked here. They only matter for P3, which is out of scope.
   - Several responses say they "created" the baseline commit or set the Git identity "as requested". Without the subject prompt I can't tell whether that was setup or task work. It doesn't affect F3, which judges the committed result after the baseline.
   - The original-condition runs in invocation-change have no separate probe for negative durations. But `src/session.py` (026) is identical to the probed candidate/finalist code and still contains `if minutes <= 0: raise ValueError`, so F2 rests on reading the code directly.

This first pass is complete. I'll read `prior-assessment.md` next and compare it in a separate message, leaving these judgments unchanged.
