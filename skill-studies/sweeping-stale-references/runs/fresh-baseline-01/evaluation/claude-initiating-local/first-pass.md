# First-pass independent review: SSR fresh original baseline (Claude, initiating-change and local-change)

All 10 runs pass all three functional factors (30 of 30 judgments met), and every run's overall result is met. The five initiating-change runs ended with byte-identical projects, and so did the five local-change runs.

**About this review**
- **Reviewer:** Opus 5.5 (`claude-opus-5-5`), a fresh session using only Read, Glob and Grep. I ran no code and edited nothing.
- **Same family as the subjects:** the subject labels are visible and the subjects are Opus, the same family as me. This is not blinded and not a cross-family check.
- **Rules applied:** policy SSR-assessment-3, the two case cards (initiating-change v3 on top of the inherited v2 card; local-change v5 on top of the inherited v4 card), both expected-facts files, and the prospective interpretation. Only F1–F3 are judged here. D1, P1–P3, the negative cases and the accounting diagnostic are left to the active session.
- **Reads done before judging:** everything listed in `required_complete_reads`, each read in full once. That is `policy.txt`, `INTERPRETATION.md`, the 6 criteria files, the 10 facts files, objects 001–025 and the 10 delivered responses. I have not looked for or opened `prior-assessment.md`.
- **Gaps in the packet:**
  - The index's packaging note mentions a PNG asset and a `.runtime` Click dependency. Neither appears in any mapping, both `qualified_runtime_dependency` lists are empty, and a search for `**/*.png` found nothing. I'm treating that note as leftover template text. It doesn't affect any judgment, because both projects are fully mapped.
  - The facts give only commit subject lines, not commit bodies. That only matters for P3, which is out of scope here.

## initiating-change (Claude, original): 5 runs

All five runs ended with the same project: objects 019–024 for the six changed files, and objects 001, 003, 009 and 010 unchanged. So the evidence below applies to every run. Each run's own facts confirm the same diff, a clean working tree and an empty uncommitted diff.

**F1 Complete useful change: met**
- `config/defaults.json` is now `{"session_ttl_minutes": 30}` (020).
- `src/session.py:4` looks up `settings['session_ttl_minutes']`, and the comment on line 1 says "session TTL" (023).
- `scripts/show-session.py:8` uses the new name for both the printed label and the lookup (022). The facts show it run from the repo and from the parent directory. Both runs print `session_ttl_minutes=30; expires_at=1900`.
- Both test cases (custom value and invalid value) use the new key (024), and the facts show 3 tests passing. I didn't rely on the tests for meaning; I read the code.
- `README.md:4` uses the new key (019).
- `docs/session-policy.md` uses "session TTL" on line 3 and `session_ttl_minutes` on line 5 (021).
- All 10 required updates are present. There is no alias, which the task allows, and no current material contradicts the change.

**F2 Preservation: met**
- **Values and behaviour:** the default is still 30, and `minutes * 60` still produces 1900 and 820. The `<= 0` check still raises `ValueError`.
- **Partner rationale:** in the comment, line 1 keeps "partner rejects longer sessions" and line 2 is unchanged ("accepts more frequent refreshes…"). In the policy doc, line 3 keeps the constraint and line 4 is unchanged ("trades more frequent refreshes for partner compatibility").
- **Units:** the line saying start and expiry times are in seconds is unchanged in the policy doc.
- **History and vendor files:** `archive/rollout-2024.md` and both `vendor/partner/*` files are byte-identical to the supplied versions (`supplied_project_bytes_unchanged` is true, and the mappings point to the same objects 003, 009 and 010).

**F3 Committed completeness: met**
- Each run has exactly one task commit after the `fixture baseline` commit. The working tree is clean and the uncommitted diff is empty, so the final workspace matches HEAD. `TASK.md` is gitignored and unchanged.

| Full run ID | Task commit | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|
| 20261026T140954711Z-ssr-fresh-baseline-claude-initiating-change-76018b57-f195-4dbf-b4b7-fbdc4d84b06a-stxp0q_m | d868ebe | met | met | met | **met** |
| 20261026T144604004Z-ssr-fresh-baseline-claude-initiating-change-57d57b6e-3c98-438e-8315-e688adf36a65-ht9yzxgt | acf8300 | met | met | met | **met** |
| 20261026T151431129Z-ssr-fresh-baseline-claude-initiating-change-3c7e4f2c-8af5-4423-910b-db05a116f204-d4zzzylp | c25a1fd | met | met | met | **met** |
| 20261026T154039670Z-ssr-fresh-baseline-claude-initiating-change-12316756-3c3c-4aa3-9ead-36e703708698-g32nx_jz | 8cb892c | met | met | met | **met** |
| 20261026T161553232Z-ssr-fresh-baseline-claude-initiating-change-56f75d7a-28d0-44e7-9e1b-3d0090855e8b-o3h6qn0l | a2fe0b9 | met | met | met | **met** |

## local-change (Claude, original): 5 runs

All five runs ended with the same project. The only changed file is `docs/glossary.md`, which became object 025; every other file keeps its supplied object.

**F1 Complete useful change: met**
- Line 3 changed from `## Member ship` to `## Membership`. The definition under it still reads naturally with the corrected heading.

**F2 Preservation: met**
- `billing.md`, `shipping.md` (including the unrelated "member shipping address" phrase), the archive, `README.md` and `config/account.json` are all byte-unchanged.
- The facts confirm the JSON values are still `membership_required: true` and `billing_pause_revokes_access: false`.
- README's links point to `docs/glossary.md` and `docs/billing.md`, and both files exist. No link in the project targets the heading anchor.
- The rest of the glossary, including the Workspace section, is unchanged.

**F3 Committed completeness: met**
- Each run has one commit after the baseline, with a clean tree and an empty uncommitted diff.

| Full run ID | Task commit | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|
| 20261026T141544649Z-ssr-fresh-baseline-claude-local-change-1446339f-f220-4b14-8081-7ef1898edc80-_axsjchk | 8e1386b | met | met | met | **met** |
| 20261026T144838218Z-ssr-fresh-baseline-claude-local-change-75fe23e2-ab3c-4f3c-8a08-c8a822fa6c91-k7phrp5n | da5f0ef | met | met | met | **met** |
| 20261026T151757646Z-ssr-fresh-baseline-claude-local-change-4c599697-2687-401b-93eb-3e0fbc6a975a-79v3yqvp | dec27ec | met | met | met | **met** |
| 20261026T154411925Z-ssr-fresh-baseline-claude-local-change-4e61e909-5fe9-4f58-95a7-336646bc7e04-_d0w7c_0 | 3b2f3bb | met | met | met | **met** |
| 20261026T161848074Z-ssr-fresh-baseline-claude-local-change-98477fce-360b-4ca2-849d-103f6e71019b-k68ok8r7 | adeefd3 | met | met | met | **met** |

## Totals

| Case / provider / condition | Runs met overall | F1 | F2 | F3 | Not met | Insufficient evidence |
|---|---|---|---|---|---|---|
| initiating-change / claude / original | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 0 | 0 |
| local-change / claude / original | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 0 | 0 |
| **Claude original, all** | **10 of 10** | 10 | 10 | 10 | 0 | 0 |

## Quality observations

**Project changes**
- Within each case all five runs produced byte-identical projects, so no repetition did better or worse than another.
- The initiating-change result is the minimal fix: it reuses the existing rationale wording and changes only the terms. Nothing was over-edited.
- Five identical results are a descriptive observation about these runs, not a reliability claim.

**Delivered responses.** These differ only in what they tell the reader; none of this affects F1–F3.
- **20261026T154039670Z…g32nx_jz** is the only response that spells out the practical effect of having no alias: a config file that still uses the old key will now fail with a missing-key error. That is accurate per `src/session.py:4` and useful to someone running the service.
- The other initiating responses report the archive and vendor reasons correctly and give the same checks.

**Accounting claims, recorded for the active session's P3 review and not scored here**
- **20261026T144604004Z…ht9yzxgt** and **20261026T161553232Z…o3h6qn0l** claim "15 matches". The expected facts give 14 occurrences or 12 matching lines.
- **20261026T154039670Z…g32nx_jz** claims 12 matches across 9 files, with 3 deliberately kept afterwards. That matches the 12-line count (the archive has 1 line and vendor has 2).
- **20261026T141544649Z…_axsjchk** describes its `References swept:` section as listing other matches as false positives, which may not be the original's required `n/a — <reason>` form. The other four local runs say `References swept: n/a`.
- None of these claims can be checked here, because commit bodies aren't in the packet.

**Other scope notes**
- Each run's facts show one task commit, so I saw no split-commit issue. Commit grouping (P2) and search order (P1) still belong to the active session.

---

This is my complete first pass. I haven't located or read `prior-assessment.md`. If you want the comparison, I'll read it next and report, by full run ID, any factor or evidence where it differs from this pass, keeping this first pass unchanged.
