# First-pass independent review, before reading the prior assessment

**Reviewer:** a fresh Opus 5.5 session (`claude-opus-5-5`), the same model family as the Opus subjects. The labels were visible. This review is not blinded and it does not validate across model families. I used only Read and Glob, ran no code and edited nothing.

**Policy and cards applied:** SSR-assessment-3 (`policy.txt`) and `INTERPRETATION.md`. For `initiating-change` I used the candidate-screen card v4, the inherited card v2 and `initiating-change-expected.md`. For `local-change` I used the candidate-screen card v6, the inherited card v4 and `local-change-expected.md`.

**What I read in full before judging:** all required files in the index — policy, interpretation, the six criteria files, all 22 fact files, objects 001–026 and all 22 delivered responses.

**Access disclosure:** my first Glob of the fixture directory listed the filename `prior-assessment.md`. I have not opened it and did not search for it.

## Packet problems (none of these change a verdict)
- The index's `packaging` note mentions a ".runtime Click dependency" and a "PNG asset" that must be read. Neither exists here: both `qualified_runtime_dependency` arrays are empty and there is no PNG object. This looks like leftover text from another packet. Nothing indexed was missing.
- Your instructions call the labels original/comprehensive/compact. The index uses `original` / `candidate` / `finalist`. Line 6 of `INTERPRETATION.md` says comprehensive and compact both follow the Candidate branch, but nothing in the packet maps candidate→comprehensive or finalist→compact. I report the labels exactly as the index gives them.
- `INTERPRETATION.md` describes 180 outputs and Opus observations. This packet has only 22 Codex outputs, so every total below is Codex only.
- Commit bodies are not supplied, so P3 can't be judged from this packet. P3 is out of scope here anyway.

## Evidence shared by all runs

**initiating-change**
- **Expected behaviour:** baseline `objects/007` reads `settings['token_ttl_minutes']`. Every final `src/session.py` is `objects/023`, which reads `session_ttl_minutes`.
  - The `<= 0` → `ValueError` guard and the `minutes * 60` calculation are unchanged.
  - The comment now says "session TTL". It keeps the reason (the partner rejects longer sessions) and the trade-off (more frequent refreshes).
- **Current consumers all updated:**
  - config `objects/020` is `{"session_ttl_minutes": 30}`
  - the script `objects/022` changes both the label and the lookup
  - tests `objects/024` change both the custom (12 → 820) and invalid (0) configurations
  - policy `objects/021` uses "session TTL" and the new key, and keeps the partner/refresh rationale and the units line
  - README `objects/019` (or `objects/025`) uses the new key
- **Runtime checks:**
  - All 11 runs: 3 tests OK.
  - The script prints `session_ttl_minutes=30; expires_at=1900` both from the project directory and from another directory.
  - The candidate and finalist runs also have an independent probe: default 1900, custom 820, zero and negative both raise ValueError.
- **Preservation:** `archive/rollout-2024.md` (003) and `vendor/partner/*` (009, 010) are byte-identical to the source in every final tree. The facts confirm this with `supplied_project_bytes_unchanged: true`.
- **What the README still says:** "a duration in minutes" and "configured duration" remain in `objects/019`. I don't count these as stale: they are generic wording and the expected facts put them outside the accounting scope. The only other surviving wording is the error string `'duration must be positive'`, which is unchanged behaviour.

**local-change**
- Every final glossary is `objects/026`. The only change from `objects/016` is `## Member ship` → `## Membership`. The membership definition and the billing-pause sentence are intact.
- `README` (012), `billing` (015), `shipping` (017, the unrelated "member shipping" near-match), `archive` (013) and `config/account.json` (014) are byte-identical in all runs.
- The fact files confirm both README link targets exist, and the JSON values are unchanged (`membership_required: true`, `billing_pause_revokes_access: false`). No supplied link targets the heading anchor.

**F3 for all 22 runs:** each `commit_history` shows exactly one task commit after `fixture baseline`. `working_status_porcelain` and `uncommitted_diff` are empty. `complete_project_diff` matches the final objects. So every required change is committed in HEAD, and a clean tree means HEAD equals the inspected final project.

## Per-run judgments (F1 / F2 / F3 → overall)

### initiating-change · codex

| Full run ID | Condition, rep | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|
| 20261026T140546843Z-ssr-fresh-baseline-codex-initiating-change-83467fd1-3781-446b-a164-bed6c7c0117f-9jmeyyww | original 1 | met | met | met (`ae01ee4`) | **met** |
| 20261026T144704352Z-ssr-fresh-baseline-codex-initiating-change-f8840c93-a991-4a72-82a0-5fb037a4ed73-cm8_tcbo | original 2 | met | met | met (`608f7bb`) | **met** |
| 20261026T151239770Z-ssr-fresh-baseline-codex-initiating-change-67127b6d-a501-47b6-bba8-4de2fcea9540-sskrnwu7 | original 3 | met | met | met (`4e8a5e0`) | **met** |
| 20261026T154139635Z-ssr-fresh-baseline-codex-initiating-change-17dded1d-3d32-4cb6-9651-23fb952a72a4-54rv74mt | original 4 | met | met | met (`18737a9`) | **met** |
| 20261026T161406484Z-ssr-fresh-baseline-codex-initiating-change-45fab7dc-3c94-49af-a64d-56a3f803812e-4qwsbxeq | original 5 | met | met | met (`51ba505`) | **met** |
| 20261026T204553292Z-ssr-screen-codex-initiating-change-candidate-2989e459-1e03-42a1-966c-221dbe18da15-8ucpa5he | candidate 1 | met | met | met (`c993010`) | **met** |
| 20261026T213417777Z-ssr-screen-codex-initiating-change-candidate-4a4076cb-355d-4117-84f0-7acd7b5bf0cd-_ub7kiio | candidate 2 | met | met | met (`eaff81a`) | **met** |
| 20261026T231131752Z-ssr-screen-codex-initiating-change-candidate-6e138563-25c8-4bf3-a39d-6d6a2226ef79-8ggtyg4_ | candidate 3 | met | met | met (`845e956`) | **met** |
| 20261026T204730849Z-ssr-screen-codex-initiating-change-finalist-16f26925-b90f-4860-8fb2-2fbb5e3da71e-skboyzjx | finalist 1 | met | met | met (`f8ed314`) | **met** |
| 20261026T213244285Z-ssr-screen-codex-initiating-change-finalist-12c3d16a-5721-4dfa-baf2-662bbcd1e9aa-o64sbbbk | finalist 2 | met | met | met (`a6ee8de`) | **met** |
| 20261026T231326259Z-ssr-screen-codex-initiating-change-finalist-7fca2c8e-eac7-48b9-a113-eebf7111875a-bqwthsxj | finalist 3 | met | met | met (`9df1f57`) | **met** |

The first ten final trees are byte-identical (objects 019–024). Finalist 3 differs only in its README (`objects/025`): it also rewrites line 3 to "a session TTL in minutes". That is consistent, accurate and harmless to meaning.

### local-change · codex

| Full run ID | Condition, rep | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|
| 20261026T141313656Z-ssr-fresh-baseline-codex-local-change-cd1737e2-9ab1-49c9-8393-3eb5e58bc5c5-7z505eid | original 1 | met | met | met (`ac1ffc1`) | **met** |
| 20261026T144939668Z-ssr-fresh-baseline-codex-local-change-a9b768e9-f6f6-4792-a2cd-bd9a389b817e-wfkiwz3e | original 2 | met | met | met (`1d03992`) | **met** |
| 20261026T151525768Z-ssr-fresh-baseline-codex-local-change-0cddf436-ece9-4d65-80b6-f909a2e7e7f3-d94fwzcg | original 3 | met | met | met (`7ac0478`) | **met** |
| 20261026T154509781Z-ssr-fresh-baseline-codex-local-change-5b3ffadf-990e-439c-ac3e-82536a8080e7-31srg3i5 | original 4 | met | met | met (`d1e9539`) | **met** |
| 20261026T161700582Z-ssr-fresh-baseline-codex-local-change-8a29c68f-378f-44d8-bf6d-c659714a1836-tq2dseko | original 5 | met | met | met (`689bd7a`) | **met** |
| 20261026T210321206Z-ssr-screen-codex-local-change-candidate-27ab5d13-b63f-4541-87cf-d583178cbc67-v42k2z3i | candidate 1 | met | met | met (`27f6cde`) | **met** |
| 20261026T224804855Z-ssr-screen-codex-local-change-candidate-a21fc716-a4d6-4e94-bcde-59c34d519928-r9sqzaxm | candidate 2 | met | met | met (`9afa850`) | **met** |
| 20261026T233018082Z-ssr-screen-codex-local-change-candidate-9285a883-62b7-497d-9551-2925f6a9ea36-t5lt6l9m | candidate 3 | met | met | met (`25c279f`) | **met** |
| 20261026T210448065Z-ssr-screen-codex-local-change-finalist-fd8ef6e4-16fd-4b4b-a8b1-6c5c762df5e9-2qavq8_x | finalist 1 | met | met | met (`9a55e65`) | **met** |
| 20261026T224700541Z-ssr-screen-codex-local-change-finalist-00975e7a-d19a-495c-86dc-671688192f4f-39206r7q | finalist 2 | met | met | met (`d8e2c5a`) | **met** |
| 20261026T233145120Z-ssr-screen-codex-local-change-finalist-ab10b389-0871-44ff-b532-958882147076-4_699gy0 | finalist 3 | met | met | met (`b496bd0`) | **met** |

All 11 final trees are byte-identical, and each diff is a single-line heading fix.

## Totals (Codex only)

| Case | Condition | Runs | F met / not met / insufficient | Overall met |
|---|---|---|---|---|
| initiating-change | original | 5 | 15 / 0 / 0 | 5/5 |
| initiating-change | candidate | 3 | 9 / 0 / 0 | 3/3 |
| initiating-change | finalist | 3 | 9 / 0 / 0 | 3/3 |
| local-change | original | 5 | 15 / 0 / 0 | 5/5 |
| local-change | candidate | 3 | 9 / 0 / 0 | 3/3 |
| local-change | finalist | 3 | 9 / 0 / 0 | 3/3 |
| **All** | | **22** | **66 / 0 / 0** | **22/22** |

## Quality observations
- **No functional difference between conditions.** In both cases the original, candidate and finalist outputs reach the same correct, minimal, committed result. In 21 of 22 runs the final trees are byte-identical. These are small, easy cases, so this packet can't show the conditions differ, and equal totals don't establish that they're equivalent in effectiveness or quality.
- **Finalist rep 3 (`…bqwthsxj`) is the only variation.** It also replaces "duration" with "session TTL" in the README's description, which slightly extends the requested terminology. That edit wasn't required, and leaving "duration" in place isn't a defect. This is a slight improvement, not a separate criterion.
- **Delivered responses:**
  - **Accurate claims:** all are short and correct about the commits, the clean tree, the passing tests and CLI output, and the untouched archive/vendor or shipping files.
  - **Claims I can't check:** several responses say the commit body records a complete inventory or disposition. Examples are original reps 2 and 3 of the initiating case, candidate 3 / `…8ggtyg4_`, finalist 2 / `…o64sbbbk`, and local original rep 3 / `…d94fwzcg`. The commit bodies aren't supplied, so these are unverified and belong to P3. They don't affect F1–F3.
  - **Extra checks:** finalist 1 initiating (`…skboyzjx`) says it confirmed the retired key is rejected. Candidate 3 local (`…t5lt6l9m`) correctly notes that the only leftover old spelling is in the ignored, unchanged `TASK.md`.
- **Out of scope for this packet:** D1, the P criteria, invocation and loading timeliness. The negative cases and the accounting diagnostic were left out and were not judged.

---

The first pass is complete. Next I'll read the prior assessment.
