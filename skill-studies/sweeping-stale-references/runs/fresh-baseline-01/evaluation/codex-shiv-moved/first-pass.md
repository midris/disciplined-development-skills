# First pass: independent F1–F3 review (Codex original, discovery-shiv and moved-guide)

I wrote this before locating or reading `prior-assessment.md`.

**Assessor context.** I'm Opus 5.5 reviewing in the active session, from a different model family than the Codex assessor. Labels were visible, and I make no claim of blinding. I used only native Read and Glob, with no code execution and no project edits.

**Policy and criteria.** SSR-assessment-3 (`policy.txt`). Fresh-baseline wrapper cards `criteria/discovery-shiv.md` and `criteria/moved-guide.md` (definition v3), their inherited cards (v2), and both `*-expected.json` files. I also read `INTERPRETATION.md`.

**Reads.** I read every required file in full before judging: policy, interpretation, all six criteria files, all ten facts files, objects 001–069 (including the `logo.png` image and the binary `test.zip`), and all ten delivered responses. The `.runtime` Click files were checked by hash only, as the index specifies. Every facts file reports `qualified_runtime_bytes_unchanged: true`.

**Structural fact.** Within each case, all five repetitions map to the same final-project objects:
- **discovery-shiv:** objects 062, 063, 064 and 065 replace 001, 010, 011 and 024. Everything else is the supplied object.
- **moved-guide:** objects 066, 067, 068 and 069 replace 053, 054, 056 and 058. Everything else is the supplied object.

So the artifact judgment is the same across repetitions. Each run's Git facts were still checked separately.

## Case discovery-shiv

### Evidence common to all five runs
**F1 (current consumers).** The four required consumers changed only the token `--output-file` to `--destination`; nothing else in those files changed:
- `README.md:28` (063)
- `scripts/build-example.sh:5` (065)
- `build-support/release/example.mk:4` (064)
- `.github/workflows/offline-example.yml:14` (062)

The canonical option is defined at `src/shiv/cli.py:96`: `"--destination", "-o", "output_file"`. Replay facts for each run:
- All four consumers exit 0 and produce `artifact_correct: true`, with matching payload and entry point.
- Every archive prints `discovery-fixture-ok\n`.
- `local_from_outside` runs the script from the parent directory with exit 0 and the correct artifact.
- The script's `cd "$(… dirname "$0")/.."` logic is unchanged, so it still works from both locations.
- The Makefile still includes `example.mk`.
- The CI evidence is a local replay of the build command only. That is the card's defined observation, so it is not an evidence gap.

**F2 (preservation).** All 46 other supplied files are byte-identical. That includes:
- `src/shiv/cli.py` and `constants.py`: the retired option was not restored.
- `docs/history/output-option.md`: the historical record.
- `docs/local-development.md` and `tools/inventory.py`: the independent tool, whose replay exits 0.
- `tests_local/test_offline.py`: the negative assertions at lines 46 and 55.

Runtime probes: `--destination` and `-o` both build working archives. The retired option exits 1 with no artifact, and stderr names `--destination/-o`. `changed_nonconsumer_files` is `[]`.

**F3 (committed repair).** In every run, porcelain status is empty, `uncommitted_diff` is empty, and the history is `fixture baseline` followed by one repair commit. All four edits are in HEAD.

One limit: the packet has no per-commit diffs. That the four edits sit in the repair commit rather than the baseline is inferred from ordering and the empty working diff. The F3 "met" condition (every repair present in retained history) is satisfied directly; commit grouping belongs to P2, which is outside this packet.

### Judgments
| Full run ID | F1 | F2 | F3 | Overall | Repair commit |
|---|---|---|---|---|---|
| 20261026T134721172Z-ssr-fresh-baseline-codex-discovery-shiv-b2bf1cab-ce90-43ab-bf0b-742deab69f41-fmmcjc30 | met | met | met | **met** | 7bb8daa |
| 20261026T143914253Z-ssr-fresh-baseline-codex-discovery-shiv-34bef055-5156-4912-b368-f30fd19f79ec-ezh96m4u | met | met | met | **met** | a0a6828 |
| 20261026T150353909Z-ssr-fresh-baseline-codex-discovery-shiv-8b7b2c1e-7ceb-4889-b85e-61e914680960-lmwtlkmw | met | met | met | **met** | f26bb06 |
| 20261026T153200730Z-ssr-fresh-baseline-codex-discovery-shiv-6aea74e1-b2ad-4844-96f1-8226ed7231aa-yc3bh5xi | met | met | met | **met** | 6c59262 |
| 20261026T160215005Z-ssr-fresh-baseline-codex-discovery-shiv-443053da-c094-4120-a779-90b810030140-5efwd34u | met | met | met | **met** | a62b67c |

## Case moved-guide

### Evidence common to all five runs
**F1 (current consumers).** Links resolve relative to their containing file:
- `README.md:3` → `docs/reference/setup.md` (066)
- `docs/index.md:3` → `reference/setup.md` (067), which resolves from `docs/`
- `docs/tutorials/quickstart.md:3` → `../reference/setup.md` (068), which resolves from `docs/tutorials/`
- `scripts/export-guide.sh:4` → `"$script_dir/../docs/reference/setup.md"` (069), with `script_dir` resolution unchanged

The checker reports `correct_target: true` for all three Markdown consumers. The export runs from the project root and from another directory both exit 0, and both produce output matching the guide's bytes (`# Orbit service setup … ORBIT_PORT=8042 …`).

**F2 (preservation).** These are byte-identical to the supplied files: `docs/reference/setup.md` (055), `plans/completed/docs-layout.md` (057, which still records `docs/setup.md` as history), `vendor/widget/README.md` (059) and `vendor/widget/setup.md` (060). The checker shows the vendor link resolving to its own guide. `old_path_present: false`, so the old path was neither restored nor duplicated, and the move stays intact.

**F3 (committed repair).** Clean worktree, empty uncommitted diff, and baseline followed by one repair commit in every run. The same per-commit-diff limit as discovery-shiv applies.

### Judgments
| Full run ID | F1 | F2 | F3 | Overall | Repair commit |
|---|---|---|---|---|---|
| 20261026T135423106Z-ssr-fresh-baseline-codex-moved-guide-3961fa8e-89bf-4c90-8499-5a3be88f3e6b-dhwjxka7 | met | met | met | **met** | 6cd49dc |
| 20261026T144158372Z-ssr-fresh-baseline-codex-moved-guide-1464c41d-e203-45b1-991f-7aafeb7a0826-w7945l8m | met | met | met | **met** | 3cd9c68 |
| 20261026T150725919Z-ssr-fresh-baseline-codex-moved-guide-6e927f28-a909-4be3-ad52-3f084793bc0a-34wbpaet | met | met | met | **met** | 105ac81 |
| 20261026T153437339Z-ssr-fresh-baseline-codex-moved-guide-158319e3-366b-4dbf-8e6d-1e014a67ac94-1lps5oor | met | met | met | **met** | 97deaba |
| 20261026T160541170Z-ssr-fresh-baseline-codex-moved-guide-eedfa38a-4422-4996-b67f-54a75b5a56c7-ndpar6uq | met | met | met | **met** | f205922 |

## Totals
- **Case discovery-shiv:** 5/5 overall met (15/15 factors met, 0 not met, 0 insufficient evidence).
- **Case moved-guide:** 5/5 overall met (15/15 factors met).
- **Provider Codex, condition original:** 10/10 overall met, 30/30 factors met. No failed or unknown factors, and no shared-cause failures to merge.

## Quality observations
- **No difference between passing artifacts.** Within each case, all five final projects are identical by content hash. Each is the minimal correct fix: exactly the four required consumers, with no extra files and no source or test changes. Ranking within a case can't come from the artifacts.
- **Shiv.** Every run kept the existing long-form command shape (`--destination`) rather than switching to `-o`, so the docs stay self-explanatory. The equal-length token swap left surrounding text and line structure untouched. Every run left the history note, the independent `--output-file` inventory tool, and the negative test assertions alone. These were the case's main traps, and none was taken.
- **Moved-guide.** Each consumer got the correct depth-specific relative path; none used a uniform string replacement. The same-name vendor guide and the historical plan were left alone.
- **Delivered responses (descriptive only, not evidence of correctness).**
  - All ten describe a baseline commit and a repair commit, and preservation of historical and independent references.
  - Their verification claims (for example "4 offline tests pass", "make example") can't be confirmed from this packet beyond the replay facts. I used only the replay facts.
  - Response 20261026T135423106Z…dhwjxka7 is the vaguest about which files changed ("README.md, documentation").
  - Responses 20261026T150725919Z…34wbpaet and 20261026T153437339Z…1lps5oor include absolute paths into the subject's workspace (to README and to SKILL.md). These links won't work outside that workspace, but they don't affect function.
  - Responses 20261026T153200730Z…yc3bh5xi and 20261026T160215005Z…5efwd34u, and the moved-guide runs, say the reference audit is in the commit body. The packet doesn't include commit bodies, so that claim, and anything about P3, isn't assessed here.
- **Out of scope here:** D1, P1–P3, and the negative and accounting cases.

---

Now locating the prior assessment for the separate comparison step.
