# First-pass independent review: moved-guide, 11 repair outputs (no prior assessment read)

**Result: all 33 functional factors are met, so all 11 runs are met overall.** In every run, all four current consumers reach the moved guide, the protected material is unchanged, and every required repair is committed. None is not met and none is insufficient evidence.

**Basis.** I read the following in full before judging:
- Policy SSR-assessment-3.
- `INTERPRETATION.md`.
- Case card `criteria/moved-guide.md` (definition version 4) and the inherited card (definition version 2).
- `moved-guide-expected.json`.
- All 11 facts files, objects 001–014 and all 11 delivered responses.

I used native Read and Glob only. I ran nothing and edited nothing. The runtime evidence comes from the neutral disposable-copy observations in each facts file. I did not run the checker or the export script myself.

**Packet discrepancies.**
- The index's `packaging` text mentions an unchanged Click runtime dependency and a PNG asset that must be read. Neither exists in this packet: every object is text and `qualified_runtime_dependency` is `[]`. This looks like copied boilerplate, and no evidence is missing.
- Condition names map like this: `original` is the original skill; `candidate` is the comprehensive rewrite (inherited card, line 16); `finalist` is the compact rewrite (run IDs `compact-regression`; INTERPRETATION line 6).

## Shared evidence

All 11 `complete_final_project` mappings point to the same objects: 001, 011, 012, 004, 013, 006, 014, 008 and 009. Checked against the source (objects 002, 003, 005 and 007):

| Consumer | Source → final | Resolves to |
|---|---|---|
| `README.md:3` | `docs/setup.md` → `docs/reference/setup.md` | docs/reference/setup.md |
| `docs/index.md:3` | `setup.md` → `reference/setup.md` | docs/reference/setup.md |
| `docs/tutorials/quickstart.md:3` | `../setup.md` → `../reference/setup.md` | docs/reference/setup.md |
| `scripts/export-guide.sh:4` | `$script_dir/../docs/setup.md` → `$script_dir/../docs/reference/setup.md` | the `script_dir` anchor is unchanged, so it works from any working directory |

- **Protected files are byte-identical to the source.** That covers `docs/reference/setup.md` (004), `plans/completed/docs-layout.md` (006, old path kept as history), `vendor/widget/README.md` (008) and `vendor/widget/setup.md` (009). `.gitignore` and TASK.md are also unchanged.
- **No old path was restored.** No `docs/setup.md` file exists in any final mapping, and the facts report `old_path_present: false`.
- **Per-run facts are the same for every run.** Checker exit is 0. All three service links show `correct_target: true`, and the vendor link resolves to `vendor/widget/setup.md` with `intended: true`. Both export runs (from the project root and from another directory) exit 0 with `matches_supplied_guide_bytes: true`. The history is exactly `<repair> ← fixture baseline`, porcelain status is `""` and `uncommitted_diff` is `""`. Each run's committed diff contains exactly the four consumer edits.

Because the artifacts are identical, the verdicts share one cause. Each run is still its own recorded execution with its own Git and runtime facts.

## Per-run judgments

Each run below is F1 met · F2 met · F3 met, so overall met. The commit shown is that run's single repair commit after `fixture baseline`, and each has a clean tree.

**original (5 runs)**
1. `20261026T135650028Z-ssr-fresh-baseline-claude-moved-guide-da811995-0ecf-4bdf-89a8-f997b6f9cd40-o89dadrq`: commit `78c458b`.
2. `20261026T144052901Z-ssr-fresh-baseline-claude-moved-guide-87640d7a-aa26-4bfb-a16d-8dd22bd36898-a87ygsrv`: commit `7628be4`.
3. `20261026T150908932Z-ssr-fresh-baseline-claude-moved-guide-091246d0-6355-4742-8d11-60c79a334d60-xqh45qhl`: commit `2d6a6df`.
4. `20261026T153330184Z-ssr-fresh-baseline-claude-moved-guide-45aa004a-7e30-4fe8-b3a1-08d265a7f9fd-rx7pg01j`: commit `d96db8a`.
5. `20261026T160936719Z-ssr-fresh-baseline-claude-moved-guide-6f8fe2b0-7064-417d-9011-c12f818448ea-glsel8dw`: commit `9d7f5d0`.

**candidate / comprehensive (3 runs)**
1. `20261026T210717432Z-ssr-screen-claude-moved-guide-candidate-453057f2-80f6-4223-8725-a22b765a393c-2y10g1ex`: commit `df75e7c`.
2. `20261026T225142332Z-ssr-screen-claude-moved-guide-candidate-0de99024-fcdf-4dc7-85f0-f12cf4096b96-fcx9kq13`: commit `08eea56`.
3. `20261026T233550330Z-ssr-screen-claude-moved-guide-candidate-93d8ad88-d374-4eca-8b95-39ab02562f74-1pol0unm`: commit `6a772ce`.

**finalist / compact (3 runs)**
1. `20261024T060738969Z-ssr-compact-regression-moved-guide-3a8241d0-eb67-4a24-8f49-1f1b24b72db7-9shudgzv`: commit `670ed50`.
2. `20261024T061703945Z-ssr-compact-regression-moved-guide-42f97295-92c5-41e5-bf7b-2c644ab42d1c-0scb5n1v`: commit `2c799cb`.
3. `20261026T233505666Z-ssr-screen-claude-moved-guide-finalist-5ff74720-3628-48e5-85d6-55081529871d-p79mfhnw`: commit `9ca931c`.

## Totals (case moved-guide, provider claude)

| Condition | Runs | F1 | F2 | F3 | Overall met / not met / insufficient |
|---|---|---|---|---|---|
| original | 5 | 5/5 | 5/5 | 5/5 | 5 / 0 / 0 |
| candidate (comprehensive) | 3 | 3/3 | 3/3 | 3/3 | 3 / 0 / 0 |
| finalist (compact) | 3 | 3/3 | 3/3 | 3/3 | 3 / 0 / 0 |
| **All** | 11 | 11 | 11 | 11 | **11 / 0 / 0** (33/33 factors met) |

## Quality among passing outputs

- **The committed artifacts can't be told apart.** All 11 final trees are byte-identical, so the conditions show no difference in artifact quality. Equal totals here say nothing about relative skill effectiveness elsewhere; this case does not separate the three versions on outcome.
- **The difference is the shared same-name vendor guide.** Every response correctly told the independent vendor `setup.md` apart from the service guide, kept the completed plan as history, and recognised the export script as a runtime consumer rather than just another link.
- **Some delivered responses describe the evidence imprecisely.** None of this affects the artifacts.
  - Original rep 3 (`…xqh45qhl`) lists `vendor/widget/setup.md` among the remaining "references to the old path". That file contains no path reference.
  - Original rep 2 (`…a87ygsrv`) says a search for the "old path" finds the vendor README. It only matches the basename `setup.md`.
  - Finalist rep 1 (`…9shudgzv`) says a `setup.md` search finds "the moved guide itself". The guide's content contains no `setup.md` string, and that sentence leaves out the four updated paths.
  - Original rep 5 (`…glsel8dw`) openly says it did not check that the links resolve. That is honest, but it verified less. The neutral checker confirms the links resolve anyway.
  - Finalist rep 3 (`…p79mfhnw`) gives exact `file:line` locations (README:3, index:3, quickstart:3, export:4). All four are correct, which makes it the most auditable response.
- **The commit-message claims can't be checked here.** Many responses claim a `References swept:` section or "every match" in the commit message, but the facts include only commit subject lines. That belongs to P3, which is outside this packet and is the active session's job. It does not affect F1–F3.

## Not judged here

D1 and P1–P3, skill loading and search order belong to the active session. The two negative cases and the accounting diagnostic are not in this packet.

---

This first pass is complete. I haven't searched for or read `prior-assessment.md`. Once you confirm, I'll read it and report any changed factors or evidence by full run ID, without changing the judgments above.
