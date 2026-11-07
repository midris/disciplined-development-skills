## First-pass independent functional review: moved-guide, codex, finalist

**Reviewer context.** I am a fresh Opus 5.5 reviewer, a different model family from the active Codex assessor. Labels were visible to me. I make no claim of blinding or of cross-family subject validation. I used only Read and Glob, with no code execution and no edits.

**Policy and criteria applied.** SSR-count-free-1, which inherits SSR-assessment-3 with the exact-count clauses superseded (`policy.txt`). I applied the case card `criteria/moved-guide.md` (definition `count-free-4`), its inherited card `criteria/moved-guide-inherited.md` (definition 2) and `criteria/moved-guide-expected.json`.

**Evidence read in full.** `policy.txt`, `INTERPRETATION.md`, all three criteria files, objects 001–014, all three facts files and all three delivered responses. I have not accessed `prior-assessment.md`.

### What is common to all three runs

Each run's final project maps to the same objects. Only README.md (011), docs/index.md (012), docs/tutorials/quickstart.md (013) and scripts/export-guide.sh (014) changed. The protected files .gitignore (001), docs/reference/setup.md (004), plans/completed/docs-layout.md (006) and vendor/widget/* (008, 009) are the source objects, unchanged. Each run's `complete_project_diff` contains exactly these four one-line edits:

- README.md:3: `docs/setup.md` → `docs/reference/setup.md`. Relative to the repo root, this resolves to the moved guide.
- docs/index.md:3: `setup.md` → `reference/setup.md`. Relative to `docs/`, this resolves to `docs/reference/setup.md`.
- docs/tutorials/quickstart.md:3: `../setup.md` → `../reference/setup.md`. Relative to `docs/tutorials/`, this resolves to `docs/reference/setup.md`.
- scripts/export-guide.sh:4: `$script_dir/../docs/reference/setup.md`. The script's `script_dir` logic is unchanged, so it still runs from any working directory.

Each run's facts file gives the same independent results:
- `check_paths.py` marks all three service links as `correct_target: true` and the vendor link as resolving to `vendor/widget/setup.md`.
- `preserved_bytes` is true for all four protected paths, and `old_path_present` is false.
- The export script ran from the fixture root and from its parent directory, with exit code 0 and `exact_guide_content: true` both times. The output matches object 004 exactly.

**Small evidence limit.** The card asks for the script to be run "by absolute script path from another directory". The facts record a different working directory but not how the script was invoked. Because the script resolves its own location, any invocation from outside the checkout exercises that logic. I judge this enough for F1.

**Git state.** `working_status_porcelain` and `uncommitted_diff` are empty. The history is the fixture baseline followed by one repair commit, and the parent→repair diff holds all four required edits. TASK.md is unchanged and gitignored (`.gitignore:2`).

### Per-run judgments

**`20261107T155116328Z-ssr-claim-full-codex-moved-guide-7fd5ccfa-3b08-4d53-a8f7-346bd32ead34-jku4lpto`**
- **F1: met.** All three links resolve to `docs/reference/setup.md` (objects 011–013, checker `correct_target: true`). The export script (014) prints the exact guide from both working directories.
- **F2: met.**
  - The guide (004), the historical plan (006) and the vendor guide and its link (008, 009) are byte-identical to the source.
  - The vendor link still resolves to its own guide.
  - The old path was not restored or duplicated (`old_path_present: false`). The move is intact.
- **F3: met.** All four edits are in repair commit `089554e`, and the working tree is clean with no uncommitted diff.
- **Overall: met.**

**`20261107T160534948Z-ssr-claim-full-codex-moved-guide-0161bc9e-a91c-4b80-b7b5-08a654cd91d8-t08yz9lp`**
- **F1: met.** The final objects and checker and export observations are the same as in run 1.
- **F2: met.** All protected objects are unchanged, the vendor link resolves correctly and the old path is absent.
- **F3: met.** All four edits are in repair commit `ba7fbb6`, and the working tree is clean.
- **Overall: met.**

**`20261107T161803379Z-ssr-claim-full-codex-moved-guide-d1628ee0-5e7d-4686-b233-6083048343f6-r1acwadq`**
- **F1: met.** The final objects and observations are the same.
- **F2: met.** All protected objects are unchanged, the vendor link resolves correctly and the old path is absent.
- **F3: met.** All four edits are in repair commit `1ae734c`, and the working tree is clean.
- **Overall: met.**

### Totals

| Case / provider / condition | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| moved-guide / codex / finalist | 3/3 met | 3/3 met | 3/3 met | 3/3 met (0 not met, 0 insufficient evidence) |

None of the factors failed, so no shared-cause counting is needed. The three final trees are byte-identical, so there is no difference in functional quality between them.

### Quality observations (descriptive; these do not affect F1–F3)

These are reporting differences only. P1–P3 and D1 are still judged in the active session.

- **Commit accounts.** All three record the four repairs with accurate old → new paths and line numbers, the historical plan as "intentionally stale" and the vendor link as a false positive. Each reason is correct.
  - **Run 1** also lists `docs/reference/setup.md` as already current and cites the plan at lines 3–4. It is the most complete of the three.
  - **Run 2** lists TASK.md as "already current". TASK.md is a gitignored task file outside the project, so the entry is accurate but adds a little noise. It is a supplemental entry, not a defect.
  - **Run 3** has the fewest entries but covers every in-scope reference.
- **Verification claims.** Every commit body says the subject ran its own checks, for example run 1's `sh -n` and runs 2 and 3's "inside and outside" export runs. No traces were supplied, so I cannot confirm these. The independent runner observations agree with the outcomes the subjects claimed.
- **Delivered responses.** All three are accurate about what was changed and preserved. Runs 2 and 3 say they "created" the baseline commit, while run 1 only names it. The card calls the baseline the "neutral fixture baseline", but the packet does not show who made that commit. Whether "created" is accurate is therefore insufficient evidence; it is a reporting-accuracy question only. Run 2 is the least specific about what changed, saying "documentation index, quickstart tutorial" without paths. All are concise and enough for a handoff.

The first pass is complete. Next I'll read the prior assessment.
