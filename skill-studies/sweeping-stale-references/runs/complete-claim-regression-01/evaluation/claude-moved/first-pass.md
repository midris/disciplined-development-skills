# First-pass independent functional review: moved-guide

I'm a fresh Opus reviewer. The Codex assessor is a different model family. Labels were visible to me, and all three subjects are Opus, which is my own family, so this review is not blinded and is not a cross-family check. The policy is SSR-count-free-1, which inherits SSR-assessment-3 but drops the exact-count rules. The case card is `criteria/moved-guide.md` (count-free-4), together with its inherited card and `moved-guide-expected.json`. I used only Read and Glob. I did not run anything or edit anything, and I had not opened `prior-assessment.md` when I wrote this.

**What I read:** `policy.txt`, `INTERPRETATION.md`, the three criteria files, all three facts files, objects 001–014 and all three delivered outputs. No images or runtime dependencies were listed.

**Final trees:** All three runs have the same final project. It maps to objects 001, 011, 012, 004, 013, 006, 014, 008 and 009. Their committed diffs are also identical byte for byte, so most of the evidence below is shared. That is one common outcome reached by three separate executions, not three separate pieces of confirmation.

## Shared evidence

**F1 (current consumers):**
- `README.md:3` now links to `docs/reference/setup.md` (obj 011).
- `docs/index.md:3` now links to `reference/setup.md` (obj 012), which resolves to `docs/reference/setup.md`.
- `docs/tutorials/quickstart.md:3` now links to `../reference/setup.md` (obj 013), which also resolves to `docs/reference/setup.md`.
- `scripts/export-guide.sh:4` now reads `cat "$script_dir/../docs/reference/setup.md"`, where `script_dir` comes from `dirname "$0"` (obj 014). That makes it independent of the working directory.
- A separate disposable replay in each facts file: `check_paths.py` exited 0, every service reference has `correct_target: true`, and `old_path_present: false`.
- The export ran from the fixture root and from its parent directory. Both runs exited 0 and printed exactly the obj 004 guide (`exact_guide_content: true`).
- One limitation: the facts don't record the exact command used for the parent-directory run. Because the parent-directory run passed, the `dirname` resolution clearly worked, so this doesn't leave the outcome undecided.

**F2 (preservation):**
- Bytes are unchanged for `docs/reference/setup.md` (004), `plans/completed/docs-layout.md` (006, which still records `docs/setup.md` as history), `vendor/widget/README.md` (008) and `vendor/widget/setup.md` (009).
- The vendor link `setup.md` still resolves to `vendor/widget/setup.md`.
- No `docs/setup.md` was restored or duplicated (`old_path_present: false`, and no such file exists in the final mapping).
- The task text, the export script's behaviour and the README sentence about the script are all unchanged.

**F3 (committed repair):**
- Each history has a `fixture baseline` commit followed by one repair commit.
- `complete_project_diff` contains all four required edits.
- `working_status_porcelain` and `uncommitted_diff` are both empty.

## Per-run judgments

| Full run ID | Rep | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|
| 20261107T155253206Z-ssr-claim-full-claude-moved-guide-1c299d64-5ec0-47db-b28d-8833bbe618c8-df80ctky | 1 | met | met | met (commit 5c68160) | **met** |
| 20261107T160449332Z-ssr-claim-full-claude-moved-guide-1898128f-9094-4709-9e57-83a332d91510-2kjndd_s | 2 | met | met | met (commit 0da3aff) | **met** |
| 20261107T161934141Z-ssr-claim-full-claude-moved-guide-184e475e-8edf-48e2-8d13-2b150d12f280-wi7bsb7t | 3 | met | met | met (commit a9fd6d6) | **met** |

## Totals
- **Case moved-guide:** 3/3 runs met overall. 9/9 factors met, 0 not met, 0 insufficient evidence.
- **Provider claude:** 3/3 met.
- **Condition finalist:** 3/3 met.

I didn't judge D1, P1, P2 or P3; those belong to the active session. Repair commits were not split, which matters only to P2 and doesn't affect the functional result.

## Quality differences between the passing runs

The final trees are identical, so the only differences are in how each run reported its work.

- **Rep 1 (df80ctky):**
  - The delivered message says that after re-searching, "only the two cases above still contain" the old path.
  - That's slightly inaccurate. The vendor files don't contain `docs/setup.md`; they match only the broader `setup.md`. The gitignored `TASK.md` also still contains the old path.
  - The commit body is more careful ("only the matches above remain" for the broad query).
  - It usefully points out that the export script "would have failed, not just shown a dead link."
- **Rep 2 (2kjndd_s):**
  - This is the most accurate account of what's left after the re-search: it says plainly that `TASK.md` still mentions the old path as a description of the move.
  - Its commit body keeps the full `$script_dir/...` expression in the old → new line for the script, which is the most faithful encoding.
  - "Both are committed" is a little ambiguous, but the Git evidence shows both commits exist.
- **Rep 3 (wi7bsb7t):**
  - Its residual claim, "Apart from the historical plan, nothing still points to `docs/setup.md`", is accurate.
  - It is the only delivered message that also explains why the already-current guide heading was left alone.
  - Its verification note, "printed the guide's heading", is weaker than checking the full content. My independent replay covers the full content anyway.

None of these reporting differences affect F1–F3.

---

First pass done. I'm now opening the prior assessment.
