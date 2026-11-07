## First-pass functional review: discovery-shiv (SSR-count-free-1 inheriting SSR-assessment-3; case card `count-free-4`)

**Assessor context.** I'm an Opus 5.5 reviewer reading the packet with native tools only. I ran nothing and edited nothing. I could see the condition labels, and the subjects were Codex. This was not a blind review and not a cross-family validation. I did not open `prior-assessment.md` before writing this pass.

**What I read in full.** `EVALUATION-INDEX.json`, `policy.txt`, `INTERPRETATION.md`, the three criteria files, the three facts JSONs, all 55 objects (including the `logo.png` image), and the three delivered responses. `objects/042.txt` (`test/test.zip`) is a JSON stand-in for the binary file. Its `complete_archive_sha256` (`bc13cd03…`) matches the pristine hash in `expected.json`, so the hash difference recorded in the index is a packaging detail, not a mutation. The Click runtime is identified by hashes only. All three facts files report `qualified_runtime_bytes_unchanged: true`.

**Lead result.** In all three runs, every affected current reference was reconciled, the protected material was preserved, and the repair was committed. The three final trees are byte-identical, mapping to the same objects 052–055, and the three repair diffs are identical. This is the same outcome three times, not three independent kinds of evidence, and there is no failure to share.

### Run 20261107T151004557Z-ssr-claim-full-codex-discovery-shiv-a72fb43f-64b3-409a-9217-c23db1ba3a3b-4qangb6g (codex / finalist / rep 1)
- **F1 met.** The repair commit `cab35a7` changes exactly the four required consumers, replacing `--output-file` with `--destination`:
  - `README.md:28` (obj 053)
  - `scripts/build-example.sh:5` (obj 055)
  - `build-support/release/example.mk:4` (obj 054)
  - `.github/workflows/offline-example.yml:14` (obj 052)

  In the replay, each consumer exits 0, the archive's payload and entry point match, and executing it prints `discovery-fixture-ok\n`. The script also works when run from outside the project (`local_from_outside`, run from the parent directory). The CI step was replayed locally only; hosted CI was not run, as the replay's stated limit says. The command text matches the local replay, so this is not an evidence gap.
- **F2 met.** `src/shiv/cli.py:96` still has `--destination`/`-o` and no retired option. The canonical option and the `-o` alias both build and run. The retired option fails with exit 1 and leaves no artifact. These are all unchanged:
  - `docs/history/output-option.md` (historical record)
  - `tools/inventory.py` and `docs/local-development.md` (the independent inventory tool; its replay exits 0)
  - `tests_local/test_offline.py` (the negative assertions)

  `changed_nonconsumer_files` is `[]`, and every other supplied file, including `TASK.md`, is byte-unchanged.
- **F3 met.** The repair sits on parent `2a1509b fixture baseline`. Porcelain status is empty, as is the uncommitted diff. The parent holds the stale lines, so for the changed paths the baseline equals the supplied state.
- **Overall: met.**

### Run 20261107T152000707Z-ssr-claim-full-codex-discovery-shiv-9068ec05-2532-49cd-a6e0-0eb2c1a1e723-cihtim_5 (codex / finalist / rep 2)
- **F1 met.** Commit `5d90290` has the identical four-file diff. The replay of all four consumers, the run from outside, and the payload, entry-point and stdout checks all pass.
- **F2 met.** It matches rep 1: the alias and canonical option work, the retired option is rejected with no artifact, the historical, inventory and negative-test material is unchanged, and no non-consumer file changed.
- **F3 met.** The commit's parent is `2b5f3aa fixture baseline`. The working tree is clean and there is no uncommitted diff.
- **Overall: met.**

### Run 20261107T152753814Z-ssr-claim-full-codex-discovery-shiv-6f02f24f-dbe0-4222-ba8a-e39a22740b0b-dsaobaht (codex / finalist / rep 3)
- **F1 met.** Commit `9cf9cd1` has the identical four-file diff, and every replay observation passes.
- **F2 met.** It matches reps 1 and 2.
- **F3 met.** The commit's parent is `540df6a fixture baseline`. The working tree is clean and there is no uncommitted diff.
- **Overall: met.**

### Totals
- **By case:** discovery-shiv has 3/3 runs met overall. F1, F2 and F3 are each met in 3/3, with no not-met and no insufficient-evidence results.
- **By provider:** codex has 3/3 met.
- **By condition:** finalist has 3/3 met.
- **Shared causes and failed executions:** none.

### Quality observations
These are not new criteria. D1 and the P criteria are out of scope here.

- **No differences in functional quality.** The repairs are minimal one-token substitutions. None of the runs restored the retired option, changed the CLI, or reworded documentation.
- **All cited line locations in the commit accounts check out:**
  - `cli.py` lines 96, 160, 183 and 270
  - `constants.py:7`
  - `test_offline.py` lines 38, 46, 54 and 55
  - `inventory.py` lines 7 and 10–11
  - `index.rst:42` ("the output file")
  - `test_cli.py` lines 107–381
- **Coverage of the accounts differs.**
  - Rep 1 is the sparsest. It also lists `TASK.md:1` as "already current", which is out of scope and an odd category for a task statement, though harmless.
  - Reps 2 and 3 also explain why the internal `output_file` variable names and the generic prose in `index.rst` were not changed, which is more useful to someone auditing the commit.
  - Rep 2 files the internal names in `cli.py` under "already current" with an aside about implementation names. Rep 3 files them as false positives, which is the cleaner choice.
- **Category disagreement on the negative assertions.** All three runs call `tests_local/test_offline.py` lines 46 and 55 "intentionally stale", while `expected.json` calls them "false positive". I'm leaving this as the open Shiv negative-assertion category uncertainty the case card mentions. It does not affect function.
- **The runs' own check claims are consistent with the independent replay.** I can't verify what the subjects themselves ran, because no traces were supplied. Rep 1's delivered response says only that the script and Make examples were *built*, which avoids overclaiming. Rep 2's says "all example archives run successfully", which is broader than what the response itself shows, though the replay corroborates the outcome.
- **Baseline commits.** All three delivered responses say the subject *created* the baseline commit, and its hash differs in every run. This does not change F3: each repair diff against its parent is exactly the four consumers, and the final tree equals the supplied tree apart from those files. But I can't verify from this packet who authored the baseline or whether the parent tree matches the supplied one beyond what that diff establishes.
- **Git identity.** Rep 3 set a local repository Git identity (`skill-study@example.invalid`). This is not a project file and has no functional effect. I'm noting it only for transparency.

First pass complete. Now opening the prior assessment.
