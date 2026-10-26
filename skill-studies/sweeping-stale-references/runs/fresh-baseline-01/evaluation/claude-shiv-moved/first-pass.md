# Independent first-pass review: SSR fresh baseline (Claude, original condition)

All 10 indexed repair outputs meet F1, F2 and F3, so all 10 are met overall (30 of 30 factors met). I found no failed or unknown functional factor.

**What I read:**
- The policy (SSR-assessment-3), INTERPRETATION.md, all six criteria files and all ten facts files.
- Every object from 001 to 069, including the logo PNG (a green snake holding a knife).
- All ten delivered responses.
- The `.runtime` Click files were identified by hash only, as the index directs. Every run's facts report `qualified_runtime_bytes_unchanged: true`.

**Method and limits:**
- I used only Read and Glob, executed nothing and edited nothing.
- Runtime outcomes come from the retained disposable-replay facts, checked against my own reading of every final artifact.
- The packet holds only commit subject lines, not full commit bodies. That affects P3, which is outside this review, and not F1–F3.
- I have not opened `prior-assessment.md` and have not searched for it.

## discovery-shiv (card: definition v3, wrapping inherited v2 and expected.json)

Within this case, all five runs have the same final-project mapping and the same complete diff. The evidence below is one shared cause. I am not counting it five times as independent findings.

**F1 (current consumers):**
- All four required consumers in the final objects now use `--destination`:
  - `README.md:28` (object 063)
  - `scripts/build-example.sh:5` (object 065)
  - `build-support/release/example.mk:4` (object 064)
  - `.github/workflows/offline-example.yml:14` (object 062)
- The replay facts show each consumer exiting 0 with `payload_matches` and `entry_point_matches` true, and running the archive prints `discovery-fixture-ok\n`.
- The script also succeeds when run from the parent directory (`local_from_outside`).
- Limit: CI is replayed locally only, as the card states.

**F2 (preservation):**
- `src/shiv/cli.py` is byte-identical to the source: `--destination`/`-o` only, and the retired option was not restored. The retired-option probe exits 1 with no artifact, and the `-o` alias builds a correct archive.
- `docs/history/output-option.md`, `tools/inventory.py`, `docs/local-development.md`, `tests_local/test_offline.py` (lines 46 and 55, the negative assertions) and `examples/greeting/greeting.py` are all unchanged. The inventory command still exits 0.
- The checker lists `.gitignore` under `changed_nonconsumer_files`. This is not a subject change:
  - The final `.gitignore` maps to the supplied object 003, the diff does not touch it, and `supplied_project_bytes_unchanged[".gitignore"]` is true.
  - The flag arises because expected.json's pristine hash (`e9542…`) differs from the subject-facing supplied file (`5640b…`, which contains `.claude/`). That is a setup/inventory difference.

**F3 (committed repair):**
- Each run has exactly one repair commit after `fixture baseline`, an empty `uncommitted_diff` and an empty porcelain status.
- The committed diff contains all four required edits.
- The responses say the subject itself created the baseline commit. This does not hide any repair: apart from the four consumers, the final tree matches the supplied bytes, and all four edits appear in the post-baseline diff.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261026T135122580Z-ssr-fresh-baseline-claude-discovery-shiv-57a33052-c40a-4da6-86bb-f7ef26471f1c-2sr8cacs | met | met | met (`8cf1dfd`) | met |
| 20261026T143736299Z-ssr-fresh-baseline-claude-discovery-shiv-4c9a1ff7-d139-47cf-a149-3e3610e8846e-2_jd8aly | met | met | met (`170135e`) | met |
| 20261026T150542611Z-ssr-fresh-baseline-claude-discovery-shiv-12060293-68fc-4aad-b179-1167dd86712b-d9tpcdl7 | met | met | met (`d5a6bf5`) | met |
| 20261026T153052393Z-ssr-fresh-baseline-claude-discovery-shiv-154d57c7-7497-4c7f-a3e2-bfd98dbf9e86-6ym5l74b | met | met | met (`1274d47`) | met |
| 20261026T160403275Z-ssr-fresh-baseline-claude-discovery-shiv-68f079bc-6b6e-474e-a153-b43c5b2f6d4c-_5a6h6x8 | met | met | met (`f8a945d`) | met |

## moved-guide (card: definition v3, wrapping inherited v2 and expected.json)

As with Shiv, all five runs share the same final objects and the same diff, so the evidence is one shared cause.

**F1 (current consumers):**
- Each link resolves correctly relative to its own file:
  - `README.md` → `docs/reference/setup.md` (object 066)
  - `docs/index.md` → `reference/setup.md` (object 067)
  - `docs/tutorials/quickstart.md` → `../reference/setup.md` (object 068)
- The checker marks each of these `intended: true`.
- `scripts/export-guide.sh` now reads `$script_dir/../docs/reference/setup.md` (object 069). Run from the project root and from another directory, it exits 0 and its output matches the supplied guide's bytes.

**F2 (preservation):**
- The service guide, `plans/completed/docs-layout.md` (still recording the historical `docs/setup.md`) and both vendor files are byte-preserved.
- The vendor link still resolves to `vendor/widget/setup.md`.
- `old_path_present: false`, so the old path was neither restored nor duplicated.

**F3 (committed repair):** each run has one repair commit after the baseline containing all four edits, with a clean working tree and no uncommitted diff.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261026T135650028Z-ssr-fresh-baseline-claude-moved-guide-da811995-0ecf-4bdf-89a8-f997b6f9cd40-o89dadrq | met | met | met (`78c458b`) | met |
| 20261026T144052901Z-ssr-fresh-baseline-claude-moved-guide-87640d7a-aa26-4bfb-a16d-8dd22bd36898-a87ygsrv | met | met | met (`7628be4`) | met |
| 20261026T150908932Z-ssr-fresh-baseline-claude-moved-guide-091246d0-6355-4742-8d11-60c79a334d60-xqh45qhl | met | met | met (`2d6a6df`) | met |
| 20261026T153330184Z-ssr-fresh-baseline-claude-moved-guide-45aa004a-7e30-4fe8-b3a1-08d265a7f9fd-rx7pg01j | met | met | met (`d96db8a`) | met |
| 20261026T160936719Z-ssr-fresh-baseline-claude-moved-guide-6f8fe2b0-7064-417d-9011-c12f818448ea-glsel8dw | met | met | met (`9d7f5d0`) | met |

## Totals

| Grouping | Factors met / not met / insufficient evidence | Overall met / not met / insufficient evidence |
|---|---|---|
| Case: discovery-shiv | 15 / 0 / 0 | 5 / 0 / 0 |
| Case: moved-guide | 15 / 0 / 0 | 5 / 0 / 0 |
| Provider: claude | 30 / 0 / 0 | 10 / 0 / 0 |
| Condition: original | 30 / 0 / 0 | 10 / 0 / 0 |

## Quality observations among the passing outputs

- **The project artifacts are the same within each case.** Committed quality cannot be told apart across the five repetitions. Each case got the minimal semantic edit (the same option or path substitution) with no extra files or rewording. All runs used `--destination`, which is the canonical option; `-o` would also have been valid.
- **The differences are in the delivered responses**, not the artifacts:
  - **Shiv `…-_5a6h6x8`:** the response says it could not run the built archives end to end, and also says the sandbox blocked temp directories. Yet it reports that `tests_local` passed, and one of those tests uses `tempfile` and runs an archive. That is a small internal inconsistency in the response. Independent replay confirms the artifact works, so it is not a functional defect.
  - **Shiv `…-6ym5l74b`:** the response admits that its commit-message count line ("11 matches across 9 paths") does not match its own itemised list. This is a P3 accounting defect and outside this review. It does not change F1–F3. The open disclosure is to its credit.
  - **Shiv `…-d9tpcdl7`:** the response also triaged `docs/index.rst:42` (the phrase "output file") correctly.
  - **Shiv `…-2sr8cacs` and `…-6ym5l74b`:** both explain that `output_file` in the source code is an internal variable name, not the CLI option. That is accurate, useful context.
  - **moved-guide `…-xqh45qhl`:** the response says "the only remaining references to the old path are the three files above", which include the vendor files. The vendor files mention `setup.md` but not the old path, so the wording is imprecise. The artifact is unaffected.
  - **moved-guide `…-glsel8dw`:** the response openly says it did not otherwise check that the links resolve. The checker confirms that they do.
- **Out of scope here:** D1, P1–P3 and both negative cases. They remain active-session judgments. I have made no procedural judgment.

This message is the complete first pass. I have not located or read `prior-assessment.md`. If you want the comparison against it, I'll do that in a separate step and keep this first pass unchanged. I'll list any changed factors or evidence by full run ID rather than counting agreement as a second independent pass.
