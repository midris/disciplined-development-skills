# First-pass independent review: moved-guide, Codex, 11 repair outputs

All 11 outputs meet F1, F2 and F3, so all 11 are overall **met** (33 of 33 factors met, none not met, none insufficient evidence).

**Basis:** SSR-assessment-3 (`policy.txt`) and the moved-guide card (`criteria/moved-guide.md` v4, inheriting `criteria/moved-guide-inherited.md` v2), with `criteria/moved-guide-expected.json` and `INTERPRETATION.md`. The reviewer is a fresh Opus 5.5 session, from a different model family than the active Codex assessor. This was not blinded: condition labels were visible, and no cross-family subject validation is claimed. No skill bodies, descriptions, hypotheses or traces were supplied, and I read none.

**What I read:** every file in `required_complete_reads`, each in full: the policy, the interpretation, the three criteria files, all 11 facts files, objects 001–014 and all 11 delivered responses. I did not read `prior-assessment.md` or search for it.

**Gaps in the packet itself:**
- The index's `packaging` and `scope` text mentions a PNG asset, a Click runtime dependency and "comprehensive/compact" labels. None of these are in this packet. Its sources declare `qualified_runtime_dependency: []`, and the run conditions are labelled `original`, `candidate` and `finalist`.
- The cards suggest which rewrite each label means (inherited v2 maps `candidate` to the comprehensive snapshot, and v4 says "finalist uses the accepted Candidate branch"). Nothing supplied here confirms that mapping, so I only use the labels as given.

**What I did not do:**
- I did not run anything myself; only Read/Glob/Grep were allowed. Runtime behaviour comes from each facts file's `independent_disposable_runtime_observations`, checked against my own reading of the script and links.
- Commit bodies were not supplied, only commit subjects, so the `References swept:` account (P3) can't be judged here. P1–P3 and D1 belong to the active session anyway.

## Shared evidence (the same for all 11 runs)

Every run's `complete_final_project` points to the same objects: 001, 011, 012, 004, 013, 006, 014, 008, 009. The `complete_project_diff` in every facts file is byte-identical.

### F1: the four current consumers now reach the moved guide
- **`README.md` (object 011):** links to `docs/reference/setup.md`, which resolves from the repo root to the moved guide.
- **`docs/index.md` (object 012):** links to `reference/setup.md`, which resolves from `docs/` to `docs/reference/setup.md`.
- **`docs/tutorials/quickstart.md` (object 013):** links to `../reference/setup.md`, which resolves from `docs/tutorials/` to `docs/reference/setup.md`. Each path was rewritten correctly for its own directory, not by blanket string replacement.
- **`scripts/export-guide.sh` (object 014):** `cat "$script_dir/../docs/reference/setup.md"`. `script_dir` comes from `dirname "$0"`, so the script doesn't depend on the current directory.
  - Runtime observations for every run: `export_from_project` and `export_from_other_directory` both exit 0 with `matches_supplied_guide_bytes: true`. The output is the Orbit guide (`ORBIT_PORT=8042`), not the Widget guide.
- **Checker:** reports `correct_target: true` / `intended: true` for all three Markdown consumers in every run.

### F2: protected material is preserved
- The service guide (004) is unchanged, so its instructions are intact.
- `plans/completed/docs-layout.md` (006) is unchanged and still records the historical `docs/setup.md` location, so its historical meaning survives.
- `vendor/widget/README.md` (008) and `vendor/widget/setup.md` (009) are unchanged, and the checker resolves the vendor link to `vendor/widget/setup.md` as intended.
- `old_path_present: false`, and no final project mapping contains `docs/setup.md`. The old path was not restored or duplicated to hide broken links.
- `.gitignore` (001) and TASK.md are unchanged. No unrelated edits: the diff touches only the four consumer files.

### F3: all repairs are committed
- Each history is exactly `fixture baseline` followed by one repair commit.
- `working_status_porcelain` and `uncommitted_diff` are both empty, so every edit in `complete_project_diff` (all four consumers) is in committed history.
- This is based on the Git facts, not on what the responses say.

## Judgments by run

| Full run ID | Condition / rep | Repair commit | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| 20261026T135423106Z-ssr-fresh-baseline-codex-moved-guide-3961fa8e-89bf-4c90-8499-5a3be88f3e6b-dhwjxka7 | original / 1 | 6cd49dc | met | met | met | met |
| 20261026T144158372Z-ssr-fresh-baseline-codex-moved-guide-1464c41d-e203-45b1-991f-7aafeb7a0826-w7945l8m | original / 2 | 3cd9c68 | met | met | met | met |
| 20261026T150725919Z-ssr-fresh-baseline-codex-moved-guide-6e927f28-a909-4be3-ad52-3f084793bc0a-34wbpaet | original / 3 | 105ac81 | met | met | met | met |
| 20261026T153437339Z-ssr-fresh-baseline-codex-moved-guide-158319e3-366b-4dbf-8e6d-1e014a67ac94-1lps5oor | original / 4 | 97deaba | met | met | met | met |
| 20261026T160541170Z-ssr-fresh-baseline-codex-moved-guide-eedfa38a-4422-4996-b67f-54a75b5a56c7-ndpar6uq | original / 5 | f205922 | met | met | met | met |
| 20261026T211013125Z-ssr-screen-codex-moved-guide-candidate-f4c5289a-8fda-4b56-b1a0-c16373c8b857-bghdfn9u | candidate / 1 | 4ca5c9a | met | met | met | met |
| 20261026T224906809Z-ssr-screen-codex-moved-guide-candidate-c520fa3e-080f-467b-a691-15ecc031ae63-dsdftik_ | candidate / 2 | 0ddb8ab | met | met | met | met |
| 20261026T233821780Z-ssr-screen-codex-moved-guide-candidate-5a037c43-695e-49e4-ba10-687ea95d23fe-hzzh_xpk | candidate / 3 | aeaf19d | met | met | met | met |
| 20261026T210827783Z-ssr-screen-codex-moved-guide-finalist-65f840b2-16a1-4e42-97c3-17b0be66d851-4y4ke0bj | finalist / 1 | 16a3ba0 | met | met | met | met |
| 20261026T225022624Z-ssr-screen-codex-moved-guide-finalist-0977eac1-7444-4ae4-a683-3c4457777f39-ga7g1kpd | finalist / 2 | 9b694e9 | met | met | met | met |
| 20261026T233655094Z-ssr-screen-codex-moved-guide-finalist-46f1de0e-9e8a-4ab7-ba7d-3b2da175380a-c54g42ku | finalist / 3 | ba460f0 | met | met | met | met |

All original runs are marked `reused: true` (earlier baseline observations); the candidate and finalist runs are new (`reused: false`).

## Totals

| Case / provider / condition | Runs | Factors met / not met / insufficient | Overall met |
|---|---|---|---|
| moved-guide / codex / original | 5 | 15 / 0 / 0 | 5/5 |
| moved-guide / codex / candidate | 3 | 9 / 0 / 0 | 3/3 |
| moved-guide / codex / finalist | 3 | 9 / 0 / 0 | 3/3 |
| **All** | **11** | **33 / 0 / 0** | **11/11** |

There are no failures, so no shared failure causes to collapse.

## Quality among the passing outputs

- **The final projects are identical.** All 11 runs produced the same bytes in every final file, so the delivered project shows no difference at all between original, candidate and finalist. Each is the minimal correct repair: four one-line edits, each relative to its own file, with no extra changes. Equal scores here come from identical artifacts, not just from equal criterion counts.
- **These runs can't tell the conditions apart.** With identical artifacts, this case on Codex gives no artifact evidence either way about whether a rewrite is effective or equivalent, and it doesn't speak to skill size.
- **The responses differ only in reporting, which isn't a functional criterion:**
  - Finalist/1 (…4y4ke0bj) and original/2 (…w7945l8m) name all four repaired files. Original/1, original/3, original/5 and finalist/3 (…dhwjxka7, …34wbpaet, …ndpar6uq, …c54g42ku) say "documentation" or "the docs index/tutorial", which is a little less precise.
  - Original/3 (…34wbpaet) says the preservations were "documented in the commit sweep", and original/4 (…1lps5oor) mentions a "commit-body audit". I can't check either claim because the commit bodies weren't supplied.
  - No response claims something that the Git or runtime facts contradict.
- **Possible checker gap (not a defect):** some responses say "shell syntax" was checked. The card's checker covers only inline Markdown links. The export script was separately run on disposable copies (from the project root and from another directory), so F1 doesn't rest on the checker for the script.

This completes the independent first pass. I have not opened `prior-assessment.md`. Comparing against it, run by run, comes in a separate step, and these first-pass judgments stay as they are.
