## First pass: discovery-shiv, Codex, `finalist` (3 repair outputs, 9 functional factors)

**Lead result: all three runs met F1, F2 and F3.** Each run updated all four affected references, left protected material unchanged and committed every required edit. The working tree was clean at the end of each run.

**Policy and criteria:** SSR-count-free-1, which inherits SSR-assessment-3 apart from the exact-count rules, applied with the `discovery-count-free-4` case card, whose F1–F3 text matches the inherited `discovery-shiv` v2 card.

**Reviewer context:** fresh Opus 5.5 session, read-only, using only native Read/Glob. I made no edits and ran no code. The run labels were visible, so this review is not blinded and is not a cross-family validation.

**What I read:** every object listed in the index, including the PNG (the shiv snake logo), plus the policy, the interpretation, all three criteria files, all three facts files and all three delivered responses. I did not open `prior-assessment.md`.

**Shared evidence across the runs.** All three runs map to the same final objects (`052`–`055` plus unchanged `002`–`050`). That means three independent executions arrived at byte-identical final projects. It is not a single shared cause. Comparing the final objects with the source objects shows exactly four edits, one line each, all `--output-file` → `--destination`:
- `README.md:28` (`010`→`053`)
- `scripts/build-example.sh:5` (`024`→`055`)
- `build-support/release/example.mk:4` (`011`→`054`)
- `.github/workflows/offline-example.yml:14` (`001`→`052`)

These match the `complete_project_diff` in each facts file. The edits target the canonical option defined at `src/shiv/cli.py:96` (`"--destination", "-o", "output_file"`), which is unchanged.

The index lists `test/test.zip` (`042`) under a different hash from the one in `expected.json`. Reading the object resolves this: `042` is a JSON description of the archive whose `complete_archive_sha256` (`bc13cd…`) matches the expected pristine hash. The facts also record `test/test.zip` as unchanged, so this is a packaging representation, not damage.

### 20261031T104306410Z-ssr-count-free-codex-discovery-shiv-cc717fd4-6e4e-4dff-a482-9b92d1437e2b-e6fkardo
- **F1 met.** The replay observed all four required consumers with `artifact_correct: true`. Each payload and entry point matched, and each archive ran with exit 0 and printed `discovery-fixture-ok\n`. The script also worked from outside the repo (`local_from_outside`, cwd = parent directory). By inspection, each command now passes `--destination` to `tools/shiv-local.py`, which loads the unchanged `cli.py`.
- **F2 met.**
  - Only the four consumer files changed (`changed_nonconsumer_files: []`). The Click runtime and `TASK.md`/`.gitignore` bytes are unchanged.
  - The retired option was not restored: the `--output-file` probe exits 1 with `NO_OUTFILE` and creates no artifact. The `-o` alias and canonical builds both produce correct archives.
  - The history note (`016`), the inventory tool and its docs (`048`/`019`; the independent-tool probe exits 0), and the negative assertions at `test_offline.py:46,55` (`047`) are all unchanged.
- **F3 met.** History is `679efae fixture baseline` followed by one repair commit, `e9b15b9`. Porcelain status and the uncommitted diff are both empty, so all four edits are in the history.
- **Overall: met.**

### 20261031T105251378Z-ssr-count-free-codex-discovery-shiv-c2fdfad1-0e0e-4cb8-8cc6-438c0506969e-0sak5_do
- **F1 met.** Same final consumer objects as the first run. Its own replay (`count-free-replay-hhqyjcrq`) shows all four consumers, the script from outside, payload/entry-point matches and correct output.
- **F2 met.** Same preservation facts: the retired option is rejected with no artifact, the alias and canonical builds are correct, the inventory probe exits 0, and no non-consumer file changed.
- **F3 met.** History is `d52fb15` baseline followed by one repair commit, `c8613d2`. The tree is clean and nothing is left uncommitted.
- **Overall: met.**

### 20261031T110220442Z-ssr-count-free-codex-discovery-shiv-5f67dfae-97bb-4724-8320-ccfe296a3a89-wb1iesq1
- **F1 met.** Same final objects. Its replay (`count-free-replay-hdl7ocgq`) shows all four consumers and the script from outside producing correct, runnable archives.
- **F2 met.** The retired option is rejected with no artifact, the alias and canonical builds are correct, the inventory probe exits 0, and no protected file changed.
- **F3 met.** History is `400745a` baseline followed by one repair commit, `a0c4a04`. The tree is clean.
- **Overall: met.**

**Evidence limits that apply to all three runs:**
- The CI workflow was checked by replaying only its build command locally; hosted CI was not executed (this is the stated replay limit).
- The facts do not name the base of `complete_project_diff`. Because the tree is clean and the final content differs from the source, the edits are in the retained history, which is all the F3 "Met" rule requires.
- Each subject created its own baseline commit, so I can't independently show that the baseline tree was exactly pristine. Each run has a single repair commit whose message describes exactly these four edits, and the shared final tree is the source plus those four lines.

None of this changes a verdict.

### Totals
| Grouping | Runs | F1 | F2 | F3 | Overall met / not met / insufficient |
|---|---|---|---|---|---|
| Case discovery-shiv | 3 | 3/3 met | 3/3 met | 3/3 met | 3 / 0 / 0 |
| Provider codex | 3 | 3/3 | 3/3 | 3/3 | 3 / 0 / 0 |
| Condition finalist | 3 | 3/3 | 3/3 | 3/3 | 3 / 0 / 0 |

### Quality among the passing outputs
These are observations only; P1–P3 and D1 remain judgments for the active session.

1. **Repairs:** identical across the runs. The functional result gives no basis for ranking them.
2. **First run (`…e6fkardo`), commit account:**
   - It groups `tests_local/test_offline.py:38,46,54-55` under one mixed label, "intentionally stale/current". That merges the already-current lines (38, 54) with the negative assertions (46, 55).
   - It adds supplementary entries for `src/shiv/cli.py` and for `test/test_cli.py:107-381` (`output_file` variable names). These are accurate but outside the required scope.
   - Its verification list is honest: it does not claim to have run the CI command.
3. **Second run (`…0sak5_do`), commit account:**
   - The content is accurate. It separates tests 38/54 (already current) from 46/55 (stale).
   - **The commit body contains literal `\n` escape sequences instead of line breaks.** In the facts, the body after the summary line is one physical line with backslash-n text, so the `References swept:` list does not show as a list in `git log`. That is a real readability and audit defect in the artifact people inspect, though it does not affect any F criterion.
   - It also lists `TASK.md:1`, an ignored input that the fixed scope excludes. This is harmless.
   - It puts all four updated paths in one bullet.
4. **Third run (`…wb1iesq1`), commit account:**
   - It is the clearest. Each update path has its own line, and current and stale test lines are split.
   - Its preservation reasons are correct, and its verification claims are honest: it names README, local and release builds, not CI, and it checked the inventory tool.
   - It still pairs `cli.py`/`constants.py` and `local-development.md`/`inventory.py` in shared bullets.
5. **Negative assertions (`test_offline.py:46,55`):**
   - All three runs call them "intentionally stale" (the first run with the mixed label above); `expected.json` calls them "false positive".
   - I am leaving that inherited category uncertainty unresolved, as the card requires.
6. **Delivered chat responses:**
   - All three are short and accurate about committed state, the clean tree, and what was verified. None claims a CI run.
   - The second run's mention of "Configured repository Git identity as requested" refers to setup, not the repair.

---

That completes the independent first pass. Next I'll open the prior assessment.
