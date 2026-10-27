# First-pass independent review: discovery-shiv, Codex, 11 repair outputs

**Bottom line:** All 11 runs are **met** on F1, F2 and F3, so 33 of 33 functional factors are met. Every run reconciled all four current consumers, preserved the protected material and committed the repair with a clean working tree. The 11 final projects are identical, byte for byte. No run has a functional failure or an evidence gap.

**What I read (Read/Glob/Grep only, no code run, no project edits):**
- `policy.txt` (SSR-assessment-3), `INTERPRETATION.md`, and the three criteria files (`discovery-shiv-expected.json`, `discovery-shiv-inherited.md`, `discovery-shiv.md`). The card in `discovery-shiv.md` is definition v4 and wraps the inherited card, which is v2.
- All 11 facts files and all 11 delivered responses.
- Every object, 001–055, in full, including `022.png` (the snake logo) and `051.txt` (TASK).
- I did not read `prior-assessment.md` or search for it.

## Shared artifact evidence

Every run's `complete_final_project` maps to the same objects. Only four paths differ from the supplied source: 052, 053, 054 and 055. Each of those four changes exactly one `--output-file` to `--destination` in a Shiv invocation:

| Consumer | Source → final |
|---|---|
| `.github/workflows/offline-example.yml:14` | 001 → 052: `... --destination build/ci.pyz` |
| `README.md:28` | 010 → 053: `... --destination build/readme.pyz` |
| `build-support/release/example.mk:4` | 011 → 054: `... --destination build/release.pyz` |
| `scripts/build-example.sh:5` | 024 → 055: `... --destination build/local.pyz` |

Nothing else in those files changed. The CI workflow's other steps, the README prose ("Run it with … prints `discovery-fixture-ok`"), the Make target and the script's `cd "$(CDPATH= cd …)"` root logic are all intact.

**F1 (current consumers):** Every facts file shows all four consumers with `exit_code: 0`, `payload_matches: true`, `entry_point_matches: true`, and the archive printing `discovery-fixture-ok\n`.
- The script also works from outside the project (`local_from_outside`, run from the parent directory).
- My own reading agrees. `src/shiv/cli.py:96` declares `--destination`/`-o`. `tools/shiv-local.py` loads `.runtime` and `src`. Each command builds `examples/greeting` with `greeting:main`.
- The workflow's local-replay limit is the card's own: the build step is replayed locally, but the workflow is not run on hosted CI. This is not an evidence gap for F1.

**F2 (preservation):** The following are unchanged (`supplied_project_bytes_unchanged: true`, confirmed by identical object IDs):
- the CLI and constants (`cli.py` 034, `constants.py` 035), so the retired option was not restored;
- the historical note `docs/history/output-option.md` (016, still says `--output-file`);
- the independent tool `tools/inventory.py` (048) and its doc `docs/local-development.md` (019);
- the negative tests `tests_local/test_offline.py:46,55` (047);
- `examples/greeting/greeting.py` (021), all other source, tests and docs, `TASK.md`, and the qualified `.runtime` (`qualified_runtime_bytes_unchanged: true`).

The runtime probes agree:
- `--destination` and `-o` both build a correct runnable archive.
- `--output-file` exits 1 with `NO_OUTFILE` and leaves no artifact.
- The inventory command exits 0.
- `changed_nonconsumer_files: []`.

**F3 (committed repair):** Every run has exactly one commit after `fixture baseline`, `uncommitted_diff: ""` and empty porcelain status. So every required edit is in the retained history.

One nuance does not change the verdict. Each response says the subject created the baseline commit itself. The packet doesn't include separate per-commit diffs. However, the final tree equals HEAD, the working tree is clean, and the old-side blob hashes (`7f49891`, `0109059`, `67533a9`, `df864d6`) are the same in every run. That is consistent with a pristine baseline and a single repair commit. Commit grouping (P2) belongs to the active session, not this review.

## Per-run judgments

| Full run ID | Condition, rep | F1 | F2 | F3 | Overall | Repair commit |
|---|---|---|---|---|---|---|
| 20261026T134721172Z-ssr-fresh-baseline-codex-discovery-shiv-b2bf1cab-ce90-43ab-bf0b-742deab69f41-fmmcjc30 | original 1 | met | met | met | **met** | `7bb8daa` docs: repair offline example after option rename |
| 20261026T143914253Z-ssr-fresh-baseline-codex-discovery-shiv-34bef055-5156-4912-b368-f30fd19f79ec-ezh96m4u | original 2 | met | met | met | **met** | `a0a6828` fix stale long output option references |
| 20261026T150353909Z-ssr-fresh-baseline-codex-discovery-shiv-8b7b2c1e-7ceb-4889-b85e-61e914680960-lmwtlkmw | original 3 | met | met | met | **met** | `f26bb06` fix offline examples for destination option |
| 20261026T153200730Z-ssr-fresh-baseline-codex-discovery-shiv-6aea74e1-b2ad-4844-96f1-8226ed7231aa-yc3bh5xi | original 4 | met | met | met | **met** | `6c59262` Fix offline examples for destination option |
| 20261026T160215005Z-ssr-fresh-baseline-codex-discovery-shiv-443053da-c094-4120-a779-90b810030140-5efwd34u | original 5 | met | met | met | **met** | `a62b67c` Fix destination option in offline examples |
| 20261026T204406120Z-ssr-screen-codex-discovery-shiv-candidate-c0f73722-17eb-43fb-afef-8b52be9165b3-gta01too | candidate 1 | met | met | met | **met** | `e3cb878` Fix stale output option references |
| 20261026T212521143Z-ssr-screen-codex-discovery-shiv-candidate-d74ab21a-21cc-4e9a-b091-1f44bd0b31f3-b5l16_um | candidate 2 | met | met | met | **met** | `5b1d777` Update offline examples for destination option |
| 20261026T230951628Z-ssr-screen-codex-discovery-shiv-candidate-67852c02-e91f-44a6-861e-3008a8812cc0-r9i4j1y0 | candidate 3 | met | met | met | **met** | `fd0e9f4` Update offline examples for destination option |
| 20261026T204231699Z-ssr-screen-codex-discovery-shiv-finalist-e4f82415-5d91-47f3-8181-3b63e27eb6c4-gjlbbssd | finalist 1 | met | met | met | **met** | `aea5e97` Update stale output option examples |
| 20261026T212724634Z-ssr-screen-codex-discovery-shiv-finalist-6a0e6721-98f8-4f2c-8aaf-6d047450d96c-25yadmcm | finalist 2 | met | met | met | **met** | `6d62d95` Update offline examples for destination option |
| 20261026T230812245Z-ssr-screen-codex-discovery-shiv-finalist-f1797bba-ca58-445d-98bd-bbbc85d5d5e3-silpin_9 | finalist 3 | met | met | met | **met** | `abe49f6` Fix stale destination option examples |

## Totals

| Group | Runs | F1 / F2 / F3 met | Overall met | Not met | Insufficient evidence |
|---|---|---|---|---|---|
| discovery-shiv / codex / original | 5 | 5 / 5 / 5 | 5 | 0 | 0 |
| discovery-shiv / codex / candidate | 3 | 3 / 3 / 3 | 3 | 0 | 0 |
| discovery-shiv / codex / finalist | 3 | 3 / 3 / 3 | 3 | 0 | 0 |
| **Case/provider total** | **11** | **11 / 11 / 11 (33 of 33 factors)** | **11** | **0** | **0** |

There are no failures, so shared causes need no deduplication.

## Quality observations

- **No difference in the artifacts.** The final projects are identical across all 11 runs, so their consequential quality is identical too. Each run made the minimal edit to the canonical option rather than switching to `-o`. That keeps the docs, script, Make target and CI in line with the settled long-option name the task names. These identical, passing results can't separate the conditions. Equal totals here do not show that the conditions are equally effective in general (INTERPRETATION l.16).
- **Responses differ only in wording and what they claim.** None of the response claims contradicts the facts.
  - Run `r9i4j1y0` says "all three example archives". That is accurate: CI wasn't run locally by the subject, and it didn't overclaim.
  - Run `silpin_9` says "clean *tracked* working tree", a narrower claim. The facts show empty porcelain anyway.
  - The subject line of `silpin_9`, "Fix stale destination option examples", is slightly misleading because `--destination` is the current option. This is cosmetic.
  - Runs `yc3bh5xi`, `5efwd34u`, `gta01too`, `b5l16_um`, `r9i4j1y0` and `silpin_9` say a commit-body audit or classification exists. The packet has commit subjects only, not bodies, so I can't verify those claims. P3 is outside this packet in any case.
- **Packet discrepancy (no effect on verdicts).** The index `scope` string says "original/comprehensive/compact labels", but the runs are labelled `original`/`candidate`/`finalist`. The inherited card maps `candidate` to the comprehensive snapshot. The wrapper card says `finalist` uses "the accepted Candidate branch" but doesn't name it compact. I've reported each run under its declared label and inferred no mapping beyond what the cards say.
- **Kept separate from these judgments.** Invocation and loading, search order and triage (P1), commit grouping (P2), the account (P3) and D1 remain judgments for the active session. Nothing here assesses them, and the identical artifacts carry no evidence about procedure.

This message is the complete first pass. I'll read `prior-assessment.md` only in a later step, and I'll report any changed factor or evidence by full run ID without changing these judgments.
