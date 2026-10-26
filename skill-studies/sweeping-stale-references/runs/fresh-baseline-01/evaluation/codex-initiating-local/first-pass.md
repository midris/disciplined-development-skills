# Independent first pass: SSR fresh original, Codex, initiating-change and local-change

**Bottom line:** I judged F1, F2 and F3 met for all 10 runs, so all 30 factors are met and all 10 runs are met overall. Every affected reference was reconciled, the protected material was preserved, and all required edits were committed with clean worktrees.

**Basis:** policy SSR-assessment-3 (`policy.txt`) and the prospective `INTERPRETATION.md`. For initiating-change I used card v3 (`criteria/initiating-change.md`), the inherited v2 card and its expected facts. For local-change I used card v5 (`criteria/local-change.md`), the inherited v4 card and its expected facts.

**Reviewer context:** I am Opus 5.5 and the labels were visible, so this review is not blinded and is not a cross-family validation. I used only Read and Glob, executed no code and edited nothing.

**Read audit:** Before judging, I read all 50 required files in full: policy, interpretation, all 6 criteria files, all 10 facts files, objects 001–025 and all 10 outputs. I have not searched for or opened `prior-assessment.md`.

**Packet gap:** The index's packaging note mentions a PNG asset and an unchanged `.runtime` Click dependency. Neither appears in `objects`, and both cases declare `qualified_runtime_dependency: []`. I treated that note as boilerplate rather than missing evidence, because no indexed case depends on those items. None of the judgments below rests on it.

**Runtime evidence:** I executed nothing myself. Runtime claims come from the controller's disposable observations in each facts file. Those observations match my own reading of the final code.

---

## Case: initiating-change (codex, original). All 5 runs have identical final trees.

All five runs map to the same final objects (019–024), and the supplied objects 001, 003, 009 and 010 are unchanged. Each run's `complete_project_diff` is the same six-file diff, but each comes from a separate execution with its own commit hashes. The shared final content is one observed outcome repeated, not one cause shared across runs, so I judged each run on its own evidence.

**Evidence that applies to every run:**

- **F1, the rename works across every consumer:**
  - **Config:** `config/defaults.json` is `{"session_ttl_minutes": 30}` (020).
  - **Service:** `src/session.py:4` looks up `settings['session_ttl_minutes']` (023).
  - **Script:** `scripts/show-session.py:8` renames both the output label and the lookup (022). The runtime observations give `session_ttl_minutes=30; expires_at=1900` from both the fixture directory and its parent directory.
  - **Tests:** `tests/test_session.py:17,21` use the new key; 12 gives 820 and 0 is rejected (024). The observations record 3 tests run, OK.
  - **Current explanations:** `README.md:4` uses the new key (019). `docs/session-policy.md:3` says "The session TTL…" and line 5 uses `session_ttl_minutes` (021). The `src/session.py:1` comment says "The session TTL stays at 30 minutes…".
  - **No leftovers:** none of the 10 required update occurrences keeps the old name in current material.
- **F2, protected meanings are preserved:**
  - **Behaviour:** the value 30, `minutes * 60`, and `if minutes <= 0: raise ValueError` are unchanged.
  - **Rationale:** the partner constraint and the refresh trade-off survive in both places: `src/session.py:1–2` and `docs/session-policy.md:3–4`.
  - **History and vendor:** `archive/rollout-2024.md` is byte-identical (003), so the historical `token_ttl_minutes=30` / "token TTL" stays stale on purpose. `vendor/partner/README.md` and `example.json` (`15`) are byte-identical (009/010), so the independent vendor setting is untouched.
  - **Other material:** `README.md:7`, which describes the archive and vendor folders, is unchanged.
  - **No damage:** there is no alias, and no blanket replacement into archive or vendor.
- **F3, all work is committed:** each run has exactly one commit after `fixture baseline`, `working_status_porcelain` is empty, `uncommitted_diff` is empty, and the committed diff contains every F1 edit. The committed tree is the final tree.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| `20261026T140546843Z-ssr-fresh-baseline-codex-initiating-change-83467fd1-3781-446b-a164-bed6c7c0117f-9jmeyyww` | met | met | met (`ae01ee4` after `a6b7787`, clean) | **met** |
| `20261026T144704352Z-ssr-fresh-baseline-codex-initiating-change-f8840c93-a991-4a72-82a0-5fb037a4ed73-cm8_tcbo` | met | met | met (`608f7bb` after `cf899c3`, clean) | **met** |
| `20261026T151239770Z-ssr-fresh-baseline-codex-initiating-change-67127b6d-a501-47b6-bba8-4de2fcea9540-sskrnwu7` | met | met | met (`4e8a5e0` after `f407ae4`, clean) | **met** |
| `20261026T154139635Z-ssr-fresh-baseline-codex-initiating-change-17dded1d-3d32-4cb6-9651-23fb952a72a4-54rv74mt` | met | met | met (`18737a9` after `4ec3c21`, clean) | **met** |
| `20261026T161406484Z-ssr-fresh-baseline-codex-initiating-change-45fab7dc-3c94-49af-a64d-56a3f803812e-4qwsbxeq` | met | met | met (`51ba505` after `0e3eac7`, clean) | **met** |

## Case: local-change (codex, original). All 5 runs have identical final trees.

All five runs map to the same final `docs/glossary.md` (025). Every other supplied file is byte-identical to the source; `supplied_project_bytes_unchanged` is true for every file except the glossary.

**Evidence that applies to every run:**

- **F1, the heading is fixed:** `docs/glossary.md:3` reads `## Membership`. The body lines that follow (5–6) and the Workspace section are unchanged, so the heading stays useful in context.
- **F2, meanings and links are preserved:**
  - **Docs:** `docs/billing.md` (015) and `docs/shipping.md` (017) are unchanged. The near-match "member shipping address" was not normalized.
  - **Archive and config:** the archive (013) is unchanged. `config/account.json` keeps `membership_required: true` and `billing_pause_revokes_access: false`.
  - **Links:** both `README.md` link targets exist. The heading anchor changes from `#member-ship` to `#membership`, but no supplied file links to that anchor; `README.md` (012) links only to the file.
- **F3, the fix is committed:** each run has one commit after the baseline, with an empty porcelain status and an empty uncommitted diff.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| `20261026T141313656Z-ssr-fresh-baseline-codex-local-change-cd1737e2-9ab1-49c9-8393-3eb5e58bc5c5-7z505eid` | met | met | met (`ac1ffc1` after `9d413de`, clean) | **met** |
| `20261026T144939668Z-ssr-fresh-baseline-codex-local-change-a9b768e9-f6f6-4792-a2cd-bd9a389b817e-wfkiwz3e` | met | met | met (`1d03992` after `2f2760c`, clean) | **met** |
| `20261026T151525768Z-ssr-fresh-baseline-codex-local-change-0cddf436-ece9-4d65-80b6-f909a2e7e7f3-d94fwzcg` | met | met | met (`7ac0478` after `752f633`, clean) | **met** |
| `20261026T154509781Z-ssr-fresh-baseline-codex-local-change-5b3ffadf-990e-439c-ac3e-82536a8080e7-31srg3i5` | met | met | met (`d1e9539` after `a494f6c`, clean) | **met** |
| `20261026T161700582Z-ssr-fresh-baseline-codex-local-change-8a29c68f-378f-44d8-bf6d-c659714a1836-tq2dseko` | met | met | met (`689bd7a` after `3de179c`, clean) | **met** |

## Totals

| Grouping | Runs | F met / not met / insufficient | Overall met / not met / insufficient |
|---|---|---|---|
| initiating-change · codex · original | 5 | 15 / 0 / 0 | 5 / 0 / 0 |
| local-change · codex · original | 5 | 15 / 0 / 0 | 5 / 0 / 0 |
| **Provider codex** | 10 | 30 / 0 / 0 | 10 / 0 / 0 |
| **Condition original** | 10 | 30 / 0 / 0 | 10 / 0 / 0 |

## Quality observations among the passing outputs

1. **The repairs cannot be ranked against each other.** Within each case, all five final trees are byte-identical. Each one is the minimal repair, and each keeps the rationale by editing in place rather than consolidating it. Differences between runs exist only in the delivered messages and commit subjects, and those are not functional.
2. **The initiating-change repair is good beyond mere completeness.** It updates the script's output label as well as its lookup, which is easy to miss because both sit on one line. It changes "token TTL" to "session TTL" in both the comment and the policy prose without losing the "because the partner rejects longer sessions" / "frequent refreshes" explanation. It also keeps the archive and vendor triage separate.
3. **Some self-reports cannot be checked here and do not count as evidence:**
   - **Unseen commit bodies:** run `…sskrnwu7` says the reference sweep is "documented in the commit's reference sweep". Run `…cm8_tcbo` says it "recorded the complete reference inventory in the repair commit body". Run `…d94fwzcg` says it "swept all related membership references and documented their disposition in the commit body". The packet gives commit subjects only, not bodies.
   - **Skill-guided procedure:** runs `…9jmeyyww`, `…4qwsbxeq` and `…31srg3i5` say they followed the skill's search procedure. There are no traces to confirm that.
   - **Where these claims belong:** they bear on P1 and P3, which stay active-session judgments outside this packet. They have no bearing on F1–F3, which rest on the trees and Git facts.
4. **An unexplained line in one response:** run `…54rv74mt` says "Configured repository-local identity as requested", but the TASK does not request that. It presumably refers to runner instructions I wasn't given. It does not affect the functional outcome.
5. **One accurate verification claim:** run `…wfkiwz3e`'s "No stale typo or old-anchor references remain" is consistent with the final tree; there were never any links to that anchor.

## Kept separate and outside this pass

- **Not judged here:** D1, P1, P2 and P3, which remain active-session judgments; the negative cases; and the accounting diagnostic.
- **Commit grouping (P2) is not inferred:** each run happens to have a single repair commit, but I did not score grouping.
- **Limits of the evidence:** passing tests and counts were treated only as supporting evidence, not as proof of meaning. Five identical repetitions describe what was observed and say nothing about reliability.

---

This message is the complete first pass. I have not located or read `prior-assessment.md`. As the instructions require, comparing against it comes only after this message. In the next turn I can read it and list, by full run ID, any factors or evidence that differ, without changing the judgments above.
