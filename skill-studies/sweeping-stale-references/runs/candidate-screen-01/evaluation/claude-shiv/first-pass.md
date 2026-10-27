## First pass: independent functional review of discovery-shiv (prior assessment not yet opened)

**Scope.** I applied policy SSR-assessment-3, the candidate-screen card for discovery-shiv (v4) and the inherited card (v2). I covered 11 repair outputs (Claude provider; 5 original, 3 candidate, 3 finalist) and judged F1–F3 for each, 33 factors in total. D1, the P criteria, the negative cases and the accounting diagnostic are outside this packet and I did not score them. I am an Opus 5.5 reviewer from the same model family as the Opus subjects, and I could see the condition labels. I make no claim of blinding or of cross-family validation.

**Reads completed before judging.** I read policy.txt, INTERPRETATION.md, all three criteria files, all 11 facts files, objects 001–055 including the PNG (a snake logo), and all 11 delivered responses. Following the packaging note, I treated the `.runtime` Click dependency as identified by its hashes, and every facts file reports `qualified_runtime_bytes_unchanged: true`.

### What the source requires
- **Task (051).** The rename to `--destination` is settled, `-o` stays valid, the README Offline example is broken, and the work must be committed. Behaviour and documentation meaning must be kept apart from the rename.
- **Four stale current consumers (all use `--output-file`):**
  - `README.md:28`
  - `scripts/build-example.sh:5`
  - `build-support/release/example.mk:4` (included by `Makefile:2`)
  - `.github/workflows/offline-example.yml:14`
- **Protected material:**
  - `docs/history/output-option.md` (historical record)
  - `tools/inventory.py` and `docs/local-development.md` (an independent tool with its own `--output-file`)
  - `tests_local/test_offline.py:46,55` (negative assertions that deliberately name the retired option)
  - `src/shiv/cli.py:96` (`--destination`/`-o`) and `constants.py:7`

### Key finding: all 11 final projects are byte-identical
Every run maps to the same final objects: 052 (workflow), 053 (README), 054 (example.mk) and 055 (build script). All 47 other paths map to the unchanged supplied objects. I read each pair in full. The only change is the single token `--output-file` → `--destination` on the four expected lines. Nothing else changed.

So the functional evidence is the same for every run. These are 11 independent executions that reached the same edit, not one shared result counted 11 times. They give no artifact-level way to tell the conditions apart.

### Evidence common to every run
**F1 (current consumers)**
- In every facts file, all four consumers are `observed` with exit 0, and each builds an artifact with `payload_matches`, `entry_point_matches` and execution stdout `discovery-fixture-ok\n`.
- The build script also works when run from outside the project (`local_from_outside`, cwd = parent directory, exit 0, correct artifact).
- `make release-example` ran through `Makefile`'s include and exited 0.
- Limit: the CI check replays only the build command locally. The card qualifies exactly that observation, so this is not an evidence gap.

**F2 (preservation)**
- `src/shiv/cli.py`, `constants.py`, `tools/inventory.py`, `docs/history/output-option.md`, `docs/local-development.md`, `tests_local/test_offline.py`, `examples/greeting/greeting.py` and every other non-consumer file are byte-unchanged.
- Runtime probes:
  - `--destination` and `-o` both build correct, runnable archives.
  - The retired `--output-file` exits 1 and creates no artifact, so the old option was not restored.
  - The inventory tool's `--output-file` exits 0.
- The facts flag `changed_nonconsumer_files: [".gitignore"]` is not a subject change. `supplied_project_bytes_unchanged[".gitignore"]` is true, and supplied = final = object 003. Object 003 is the subject-facing ignore file that adds `.runtime/`, `.claude/` and `TASK.md`, while expected.json's pristine hash (`e9542…`) is a different reference. This is a fixture/reference difference, not damage.

**F3 (committed repair)**
- Each run's history is `fixture baseline` plus one fix commit.
- The baseline→HEAD git diff (blob-indexed, e.g. `7f49891..4ead845`) contains all four repairs.
- `working_status_porcelain` and `uncommitted_diff` are empty.

### Per-run judgments

| Full run ID | Condition / rep | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|
| 20261026T135122580Z-ssr-fresh-baseline-claude-discovery-shiv-57a33052-c40a-4da6-86bb-f7ef26471f1c-2sr8cacs | original 1 | met | met | met (`8cf1dfd`) | met |
| 20261026T143736299Z-ssr-fresh-baseline-claude-discovery-shiv-4c9a1ff7-d139-47cf-a149-3e3610e8846e-2_jd8aly | original 2 | met | met | met (`170135e`) | met |
| 20261026T150542611Z-ssr-fresh-baseline-claude-discovery-shiv-12060293-68fc-4aad-b179-1167dd86712b-d9tpcdl7 | original 3 | met | met | met (`d5a6bf5`) | met |
| 20261026T153052393Z-ssr-fresh-baseline-claude-discovery-shiv-154d57c7-7497-4c7f-a3e2-bfd98dbf9e86-6ym5l74b | original 4 | met | met | met (`1274d47`) | met |
| 20261026T160403275Z-ssr-fresh-baseline-claude-discovery-shiv-68f079bc-6b6e-474e-a153-b43c5b2f6d4c-_5a6h6x8 | original 5 | met | met | met (`f8a945d`) | met |
| 20261026T204127212Z-ssr-screen-claude-discovery-shiv-candidate-8f4c85e4-164b-42ef-9a08-60fe7bc95d5d-zk8fmhqf | candidate 1 | met | met | met (`5f7f666`) | met |
| 20261026T212914632Z-ssr-screen-claude-discovery-shiv-candidate-ed7600a9-51ba-4d83-98b3-1cee8edb44ba-pj3sz9sy | candidate 2 | met | met | met (`a6a1947`) | met |
| 20261026T230655225Z-ssr-screen-claude-discovery-shiv-candidate-3472ee4d-b123-4717-ba13-586473c13fb9-v8cl04u0 | candidate 3 | met | met | met (`53ed6b1`) | met |
| 20261026T204016551Z-ssr-screen-claude-discovery-shiv-finalist-93228af4-e87b-4c35-8754-23a27b0efbda-ewo2bg3z | finalist 1 | met | met | met (`5033288`) | met |
| 20261026T213023342Z-ssr-screen-claude-discovery-shiv-finalist-d6dc90bc-c6d2-403c-b562-5fffbe10856f-mmflvt1a | finalist 2 | met | met | met (`264d7bd`) | met |
| 20261026T230547583Z-ssr-screen-claude-discovery-shiv-finalist-b32f67ae-4de1-4656-b360-7c2ae06b40e3-bgmgjotl | finalist 3 | met | met | met (`9362f76`) | met |

### Totals
- **Case discovery-shiv:** 33/33 factors met, 11/11 overall met. No not met, no insufficient evidence.
- **Provider claude:** 11/11 overall met.
- **By condition:** original 5/5 (15/15 factors), candidate 3/3 (9/9), finalist 3/3 (9/9).

### Quality observations
The artifacts are identical, so the only differences that matter are in the delivered responses: how accurate their verification claims are and how candid they are. None of these affects F1–F3.

1. **Self-correction of a false claim:** candidate 2 (`…pj3sz9sy`, line 18) says its first commit message falsely claimed it had run the archive and seen the expected output, and that it amended the message. The final history still has a single fix commit, so F3 is unaffected. The original false claim is an integrity concern, partly offset by the correction; it belongs to the procedural/account review.
2. **Known, unfixed miscount in the commit message:** original 4 (`…6ym5l74b`, line 25) admits the count line "11 matches across 9 paths" doesn't match its itemised list, and left it unamended. That is a P3/accounting matter and non-blocking here. I can't check commit bodies because they are not in the packet.
3. **Weaker self-verification, made up for by independent replay:**
   - Original 5 (`…_5a6h6x8`) says it could not run the archives end to end.
   - Candidate 2 says the same.
   - Candidate 3 (`…v8cl04u0`) could not run `make`.
   - Finalist 2 (`…mmflvt1a`) checked the script only with `bash -n`.

   All four disclose these limits accurately, and the controller's replay supplies the missing behavioural evidence.
4. **Accuracy of triage claims:**
   - Every response correctly classifies the history note, the inventory tool and its document, and the negative tests.
   - Original 3 (`…d9tpcdl7`) correctly notes that the "output file" prose at `docs/index.rst:42` refers to the still-valid `-o` example.
   - Candidate 3 (line 8) says "as the skill asks". This is a reference to its instructions, not an artifact issue.
5. **No discriminating signal:** no condition did better or worse at the artifact level. All 11 runs made the same minimal, correct, committed four-line change. Equal totals here do not establish wider effectiveness equivalence; this case only gives each condition a chance to fail on discovery, and none did.

**Remaining uncertainty:**
- Hosted CI was not executed (bounded by the card).
- I did not recompute hashes myself, so I rely on the index mapping, which agrees with my full reads and the facts diffs.
- Commit bodies are not supplied.
- The mapping of the "finalist" label to the comprehensive or compact rewrite is not stated in my packet. The inherited card only ties `candidate` to the comprehensive snapshot.

---

The first pass above is complete. Now I'll find and read the prior assessment.
