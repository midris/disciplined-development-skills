## First pass: independent review of moved-guide F1–F3 (policy SSR-count-free-1 inheriting SSR-assessment-3; card `moved-guide` count-free-4)

**Reviewer:** Opus 5.5 in the same session, read-only, with native Read/Glob only. This is not blind: condition labels are visible. The subjects are Codex, not my model family, but I make no cross-family validation claim. I had not read prior-assessment.md when I wrote this pass.

**What I read in full before judging:** policy.txt, INTERPRETATION.md, `criteria/moved-guide-expected.json`, `moved-guide-inherited.md`, `moved-guide.md`, all three facts files, objects 001–014 and all three outputs. The source has no image and no qualified runtime dependency.

**Shared evidence.** All three runs map to exactly the same final objects:
- `README.md` → 011
- `docs/index.md` → 012
- `docs/tutorials/quickstart.md` → 013
- `scripts/export-guide.sh` → 014
- Everything else stays at its source object: 001, 004, 006, 008, 009.

Because the artifacts are identical, the functional verdicts share one cause. They still count as three separate executions with three separate Git histories.

### Per-run judgments

**`20261031T113258321Z-ssr-count-free-codex-moved-guide-a8795779-7aea-4d64-a58f-91b687f54105-egwrylq7`** (codex / finalist / rep 1)
- **F1 met.**
  - Each link resolves correctly from its own file:
    - README:3 `docs/reference/setup.md` (object 011)
    - docs/index.md:3 `reference/setup.md` (012)
    - quickstart:3 `../reference/setup.md` (013)
  - All three resolve to `docs/reference/setup.md`.
  - The export script now runs `cat "$script_dir/../docs/reference/setup.md"` (014). Because `script_dir` is the script's own directory, this works from any working directory.
  - The disposable replay of check_paths.py reported `correct_target: true` for all three links. It ran the export from both the fixture root and its parent directory: exit 0 each time, `exact_guide_content: true`, and the output matches object 004.
- **F2 met.**
  - The service guide (004), the historical plan (006) and the vendor README/guide (008/009) are byte-identical to the source.
  - The vendor link `setup.md` still resolves to `vendor/widget/setup.md` (checker role `independent`, `correct_target: true`).
  - `old_path_present: false`: no restored or duplicated `docs/setup.md`. The move is intact, and TASK.md and .gitignore are unchanged.
- **F3 met.** Commit `1e6072d` comes after the baseline `5a9757e` and contains all four consumer edits (the full diff matches F1). The porcelain status is empty and the uncommitted diff is empty.
- **Overall: met.**

**`20261031T114417130Z-ssr-count-free-codex-moved-guide-89f533e5-b661-4275-a65f-52def915298f-kbxmbdwl`** (codex / finalist / rep 2)
- **F1 met.** Same final objects (011–014) and the same replay result: all three links correct, and the export ran from both directories with exact guide content.
- **F2 met.** Protected objects 004/006/008/009 are unchanged, the vendor link works, and `old_path_present: false`.
- **F3 met.** Repair commit `16515762` comes after baseline `e5848b7` and contains all four edits. The working tree is clean and nothing is uncommitted.
- **Overall: met.**

**`20261031T115634295Z-ssr-count-free-codex-moved-guide-f416e6dd-c5bd-416c-80e8-be0faae6d32b-sxzrwx7_`** (codex / finalist / rep 3)
- **F1 met.** Same final objects and replay result: all three links correct, both export runs exact.
- **F2 met.** Protected bytes are unchanged, the vendor link works, and the old path is absent.
- **F3 met.** Repair commit `27343718` comes after baseline `3172896` and contains all four edits. The working tree is clean.
- **Overall: met.**

### Totals
| Scope | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| moved-guide | 3/3 met | 3/3 met | 3/3 met | 3 met, 0 not met, 0 insufficient |
| codex | 3/3 | 3/3 | 3/3 | 3 met |
| finalist | 3/3 | 3/3 | 3/3 | 3 met |

No functional factor failed and none is insufficient evidence. Each run made exactly one repair commit after the baseline. I note that as an observation only; grouping (P2) is a procedural question outside this functional packet.

### Quality observations
The functional repair is identical across all three runs, so the only quality differences are in the reporting. These are not F-criteria, and P1–P3 and D1 stay active-session judgments.

- **Every account covers the full required scope correctly:** the four updates with faithful old → new encodings and correct line numbers, plus the historical plan at line 3 with a reason based on its dated-record meaning. All three also explain why the vendor link was left alone, which is useful because a same-name file makes "the path exists" an unreliable check here.
- **Rep 1 and rep 3** also list `docs/reference/setup.md` as already current and `TASK.md:1,3` as intentionally stale. These extra entries are allowed but not required (`accounting_scope`).
- **Rep 2** leaves those extras out and is still complete for the required scope.
- **Rep 2's verification line** says only the historical record and the vendor link "retain old-form matches". That ignores TASK.md, which still contains `docs/setup.md`, though TASK.md is git-ignored and arguably outside the "mutable tree". This is a small precision gap in the account, not a functional issue.
- **Rep 3** justifies keeping TASK.md by saying it "was required to remain unchanged". The task text (010) doesn't say that; it may come from the prompt, which isn't in this packet. I can't verify it from the evidence I have.
- **Self-reported checks:**
  - Rep 1's message claims only an outside-checkout export run.
  - Rep 3 claims both an inside and an outside run.
  - The independent replay covers both directories for all three runs, so these differences don't affect F1.
  - Search-breadth claims ("repository-wide sweep", "hidden, ignored, vendor…") can't be verified without the traces. They give no support to P1 here.
- **Delivered responses:** all three are short, accurate summaries that match Git (commit SHAs/prefixes match the facts). Rep 2's "four stale setup-guide references" is an optional count and is correct.
- **Ranking:** I don't rank any run higher on consequential quality, since the artifacts are identical. Rep 1's and rep 3's accounts are slightly more complete as audit records, and rep 2 has the small TASK.md precision gap.

---

First pass complete. Now locating prior-assessment.md.
