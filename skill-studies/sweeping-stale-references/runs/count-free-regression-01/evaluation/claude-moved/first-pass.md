# First-pass independent review: moved-guide, provider claude, condition `finalist`

**Reviewer and policy.** I'm Opus 5.5, reviewing read-only in this session. I applied policy SSR-count-free-1 (which inherits SSR-assessment-3) and case card `moved-guide` `count-free-4`, whose F1–F3 match the inherited card word for word. The condition labels were visible to me. The subjects are the same model family as me, and I make no claim of blinding or cross-family validation. I have not opened `prior-assessment.md`.

**Material read in full before judging:**
- `EVALUATION-INDEX.json`, `policy.txt`, `INTERPRETATION.md`
- `criteria/moved-guide-expected.json`, `criteria/moved-guide-inherited.md`, `criteria/moved-guide.md`
- all three `facts/*.json`, objects `001`–`014`, and all three `outputs/*.md`

No image or runtime dependency is listed, and none was assumed.

## Headline

**All three runs fully meet F1–F3:**
- **Reconciliation:** every affected current reference was correctly updated.
- **Preservation:** the service guide, the historical plan and the vendor guide and its link are unchanged and still work.
- **Commit:** every required edit is committed and the working tree is clean.

All three runs produced the same final project, mapped to the same objects (`011`/`012`/`013`/`014` for the four changed files; every other file has the same bytes as the supplied project).

## Evidence common to all three runs

The facts files report identical project diffs and runtime observations for all three runs.

**F1 evidence (current consumers):**

| Consumer | Before | After | Resolves to |
|---|---|---|---|
| `README.md:3` | `docs/setup.md` | `docs/reference/setup.md` (object `011`) | `docs/reference/setup.md` |
| `docs/index.md:3` | `setup.md` | `reference/setup.md` (object `012`) | `docs/reference/setup.md` |
| `docs/tutorials/quickstart.md:3` | `../setup.md` | `../reference/setup.md` (object `013`) | `docs/reference/setup.md` |
| `scripts/export-guide.sh:4` | `cat "$script_dir/../docs/setup.md"` | `cat "$script_dir/../docs/reference/setup.md"` (object `014`) | — |

- I resolved each Markdown link relative to the file that contains it, and each one reaches the intended guide.
- The script finds its own directory through `dirname "$0"`, so its path doesn't depend on where it is run from.
- The disposable-copy run of `check_paths.py` reports `correct_target: true` for all three Markdown links.
- `export_execution` ran the script from the project root and from the parent directory. Both runs exited 0, and both printed exactly the text of object `004` (`exact_guide_content: true`).

**F2 evidence (preservation):**
- The bytes are unchanged for `docs/reference/setup.md`, `plans/completed/docs-layout.md` (still records `docs/setup.md` as the historical location), `vendor/widget/README.md` and `vendor/widget/setup.md`.
- The vendor link `setup.md` still resolves to `vendor/widget/setup.md`, and the checker marks it `intended: true`.
- `old_path_present: false`: no file was recreated at `docs/setup.md` to cover up broken links.
- `README.md` lines 5–6 are unchanged, including the export-script instruction and its "works from outside this checkout" promise. That promise is still true after the script fix.
- `TASK.md` and `.gitignore` are unchanged.

**F3 evidence (committed repair):**
- Git history is the `fixture baseline` commit followed by one repair commit.
- `complete_project_diff` contains exactly the four required edits.
- Both `uncommitted_diff` and `working_status_porcelain` are empty.

## Per-run judgments

### `20261031T113403602Z-ssr-count-free-claude-moved-guide-be123e9c-6233-4b12-81d4-3523dafebe0d-slnwkuqw` (repetition 1)

| Factor | Judgment | Evidence |
|---|---|---|
| F1 | met | All four consumer edits listed above. Checker and both export runs passed on the disposable copy. |
| F2 | met | All four protected files unchanged, vendor link works, old path absent. |
| F3 | met | Repair commit `891403dd`, made after baseline `3f9e8895`. Working tree clean. |
| **Overall** | **met** | |

### `20261031T114318384Z-ssr-count-free-claude-moved-guide-fe0a134e-98d9-43f0-8aea-bde87d691ab9-yggij97o` (repetition 2)

| Factor | Judgment | Evidence |
|---|---|---|
| F1 | met | Same final objects and same passing checker and export observations (replay `ty57att0`). |
| F2 | met | Same preservation facts. |
| F3 | met | Repair commit `5757b564`, made after baseline `bad18e76`. Working tree clean. |
| **Overall** | **met** | |

### `20261031T115749039Z-ssr-count-free-claude-moved-guide-c2594dd9-b8ea-46b6-9bdb-760f052e452f-2sp150ok` (repetition 3)

| Factor | Judgment | Evidence |
|---|---|---|
| F1 | met | Same final objects and same passing observations (replay `rwmpe7u0`). |
| F2 | met | Same preservation facts. |
| F3 | met | Repair commit `490015c3`, made after baseline `ea5aba1a`. Working tree clean. |
| **Overall** | **met** | |

## Totals

| Case / provider / condition | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| moved-guide / claude / finalist | 3/3 met | 3/3 met | 3/3 met | 3 met, 0 not met, 0 insufficient evidence |

There were no failures, so there are no shared causes to merge. The three runs are separate executions that happened to produce the same tree. That is a descriptive observation, not evidence of reliability.

## Quality observations

These are not scored. P1–P3 and D1 belong to the active session.

- **No functional difference between runs.** The final trees are byte-identical, so neither output repaired or preserved anything better than another.
- **All three commit accounts are complete.** Each lists the four repairs with faithful old → new paths and line numbers. Each also explains why `plans/completed/docs-layout.md:3` was kept, groups the vendor files as an independent false positive, and adds an "already current" line for the moved guide itself.
- **Script entry in repetition 3 is shortened.** Its account writes `../docs/setup.md` → `../docs/reference/setup.md` and drops the `$script_dir/` prefix. It is still an accurate substring of the actual change, just less exact than repetitions 1 and 2, which quote the full expression.
- **Repetition 2 gives the most specific historical reason** ("where the guide shipped at completion"), which matches the wording of object `006`. The other two say "historical record of (the) completed plan". All three are adequate.
- **Repetition 2's response wording is slightly loose.** It says the script "now reads `docs/reference/setup.md`"; the actual path is `$script_dir/../docs/reference/setup.md`. This does not mislead about the repair.
- **Verification claims are partly unconfirmed.** Every run's claim that the export script works and prints the guide is borne out by the independent export runs. Repetition 2 also claims it "checked each updated relative link resolves". The final state agrees with that, but no trace was supplied, so I can't confirm the check was actually performed. The same applies to the "re-ran grep" claims in all three runs. This does not affect F1–F3.
- **The runs, not the harness, made the baseline commit.** All three responses say "I committed the project as `fixture baseline`". The diffs' removed lines match the supplied bytes, which suggests the baseline commit is the supplied project. `.gitignore` excludes `TASK.md`. This is consistent with F3, which only asks whether the repairs were committed after the baseline. Whether the runs were supposed to make that baseline commit themselves is a question for the active session.
- **All three delivered responses are accurate.** Each states truthfully what was changed, kept and checked. None claims the README was the only problem, and each explains why the other three references were also fixed.

---

My first pass ends here. I haven't located or read `prior-assessment.md`. If you'd like the comparison, I'll read it next and report any factor or piece of evidence that differs by full run ID, keeping this first pass unchanged and treating any agreement as agreement, not as a second independent review.
