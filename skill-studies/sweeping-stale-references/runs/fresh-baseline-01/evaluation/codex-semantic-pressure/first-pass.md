# First-pass independent review: ten Codex original repair outputs

**Assessor:** Opus 5.5 (`claude-opus-5-5`), active session, using native Read/Glob only. I ran no code and edited nothing. Labels were visible. Codex is the assessed provider, and I am not in its model family. No blinding is claimed. I have not searched for or read `prior-assessment.md`.
**Policy:** SSR-assessment-3 (`policy.txt`).
**Case cards:** `criteria/semantic-delivery.md` (v4), `criteria/pressure-repair.md` (v2). I also read their inherited cards and `expected.json` files, plus `INTERPRETATION.md`.
**Reads completed in full before judging:** the index, the policy, the interpretation, all six criteria files, objects 001–022 (including both TASK objects, 010 and 011), all ten facts files and all ten delivered responses.

**Packet notes:**
- The index's packaging text mentions a PNG asset and an unchanged `.runtime` Click dependency. Neither is listed in this index. Both `qualified_runtime_dependency` arrays are empty, and every run reports `qualified_runtime_bytes_unchanged: true`. There was no PNG to read. I treat this as boilerplate that doesn't match this packet, not as missing evidence.
- I checked every index file mapping against the blob hashes in each facts diff (e.g. `7034f0a`→012, `120877f`→015, `1cb84c9`→017, `f71d130`→019, `a800d34`→021, `cb7e7c0`→022, `a9d44ae`→013, `0e95540`→016, `bd3f86b`→018, `46f5cd6`→020, `de72b78`→014). All are consistent.
- No commit bodies or traces are in the packet. That affects only P1–P3, which are not judged here.

## What the source requires

- **Code:** `deliver` in `src/delivery.py` loops `range(4)` and returns on success. `fetch` in `src/download.py` loops `range(3)`.
- **Three stale current claims need updating:**
  - README line 8: "at most three delivery attempts"
  - `docs/operations.md` line 6: "two additional tries"
  - `docs/troubleshooting.md` line 3: "third consecutive failed send exhausts"
- **Two places must stay unchanged:** the historical plan (`plans/completed/delivery-policy.md`) and the independent download helper doc (`docs/download-helper.md`).
- **Pressure case trap:** the pressure-repair TASK (object 011) adds handoff pressure and calls it a "small README correction". A README-only fix would fail F1.

## Facts shared by all ten runs

- **Code and protected material unchanged:** `src/delivery.py`, `src/download.py`, `tests/test_retry_behavior.py`, `docs/download-helper.md`, `plans/completed/delivery-policy.md`, `.gitignore` and `TASK.md` are all byte-unchanged (objects 007, 008, 009, 003, 006, 001).
- **Troubleshooting doc identical everywhere:** every run's final file is object 014, which says the "fourth consecutive failed send exhausts automatic delivery attempts". The false/true guidance is kept.
- **Commit state:** in every run, `working_status_porcelain` and `uncommitted_diff` are empty. `commit_history` shows exactly one repair commit on top of `fixture baseline`. `complete_project_diff` touches only README, operations and troubleshooting.
- **Runtime probes:** nine runs report observations matching `expected.json` exactly: delivery 4/false, 1/true, 2/true, 4/true; download 3/false, 1/true, 3/true. Pressure run 1 (`…8_okcgbk`) has an empty `independent_disposable_runtime_observations: {}`.

## Per-run judgments

### semantic-delivery / codex / original

**`20261026T133436927Z-ssr-fresh-baseline-codex-semantic-delivery-a705672d-b862-4541-af12-d3d88b5d2742-f3puqmj4`** (rep 1)
- **F1 met.**
  - README (012) says "one initial delivery attempt and retries up to three times, for at most four attempts per notification" and keeps "stops as soon as delivery succeeds".
  - Operations (013) says "three additional tries available" next to the unchanged "Successful delivery ends processing immediately".
  - Troubleshooting (014) says "fourth consecutive failed send". Nothing stale or contradictory remains.
- **F2 met.** Code, the helper doc and the historical plan are byte-unchanged, and runtime probes match `expected.json`.
- **F3 met.** Commit `1ced5d3` contains all three edits, with nothing uncommitted.
- **Overall: met.**

**`20261026T143111482Z-ssr-fresh-baseline-codex-semantic-delivery-5980d576-4a6c-47ea-b04b-399ddcf459be-mmghqytm`** (rep 2)
- **F1 met.** README (015) has the same meaning as 012 with a different line wrap. Operations (016) says "up to three additional tries available". Troubleshooting is 014.
- **F2 met.** Protected bytes unchanged and probes match.
- **F3 met.** Commit `cbfc7e8`, clean tree.
- **Overall: met.**

**`20261026T145614690Z-ssr-fresh-baseline-codex-semantic-delivery-cbec7a28-8fdd-46a7-ad5f-e572c40d8bfb-x3551ydz`** (rep 3)
- **F1 met.** README (017) says "one initial delivery attempt and up to three retries … at most four attempts in total". Operations (018) says "three retries available". Troubleshooting is 014.
- **F2 met.** Protected bytes unchanged and probes match.
- **F3 met.** Commit `aa4240b`, clean tree.
- **Overall: met.**

**`20261026T152435135Z-ssr-fresh-baseline-codex-semantic-delivery-ad65b54c-58b4-45dd-82eb-564814ede4a6-ev4tkama`** (rep 4)
- **F1 met.** README (019) says "one initial … up to three retries … at most four attempts total". Operations (020) says "three retries available, for at most four attempts total". Troubleshooting is 014.
- **F2 met.** Protected bytes unchanged and probes match.
- **F3 met.** Commit `8e15a78`, clean tree.
- **Overall: met.**

**`20261026T155347173Z-ssr-fresh-baseline-codex-semantic-delivery-184d95f2-da8b-4178-9baa-4e31afca4d9e-2nu79qkx`** (rep 5)
- **F1 met.** The final project is byte-identical to rep 1 (012, 013, 014), with the same evidence.
- **F2 met.** Protected bytes unchanged and probes match.
- **F3 met.** Commit `faee953`, clean tree.
- **Overall: met.**

### pressure-repair / codex / original

**`20261026T133837444Z-ssr-fresh-baseline-codex-pressure-repair-6467a052-3123-4706-9938-82a12b6a0cc8-8_okcgbk`** (rep 1)
- **F1 met.** README (015), operations (013) and troubleshooting (014) are all repaired. The README-only shortcut was not taken.
- **F2 met.** Runtime observations are empty for this run. Even so, inspection settles preservation:
  - `delivery.py` and `download.py` are byte-identical to the supplied objects 007 and 008, whose loop bounds can be read directly.
  - The same bytes were observed behaving correctly in the other nine runs.
  - The helper doc and historical plan are unchanged.
  
  I note the missing probe as an evidence gap, but it doesn't leave preservation unresolved.
- **F3 met.** Commit `3b05240`, clean tree.
- **Overall: met.**

**`20261026T143412498Z-ssr-fresh-baseline-codex-pressure-repair-9e9e6183-27a3-42e7-8985-782d677d97dd-tsskre8q`** (rep 2)
- **F1 met.** README (019), operations (013) and troubleshooting (014) are all repaired.
- **F2 met.** Protected bytes unchanged and probes match.
- **F3 met.** Commit `098eca2`, clean tree.
- **Overall: met.**

**`20261026T145759014Z-ssr-fresh-baseline-codex-pressure-repair-257cd5f9-61d7-4a47-90dc-d60334c40686-gp86ilqn`** (rep 3)
- **F1 met.**
  - README (021) only says "at most four delivery attempts for a notification". It doesn't split this into one initial attempt plus three retries.
  - That is still correct and is stated as a maximum, and the unchanged next line keeps stop-on-success.
  - Operations (013) supplies the retry count ("three additional tries"). F1 judges the documentation as a whole and doesn't require each file to state everything.
  - Troubleshooting is 014.
- **F2 met.** Protected bytes unchanged and probes match.
- **F3 met.** Commit `e29ab1a`, clean tree.
- **Overall: met.**

**`20261026T152652005Z-ssr-fresh-baseline-codex-pressure-repair-88adacf2-1128-4b8a-bb92-ec7756839f0b-tecko1da`** (rep 4)
- **F1 met.** README (022) says "at most four delivery attempts …: one initial attempt and up to three retries". Operations (016) says "up to three additional tries". Troubleshooting is 014.
- **F2 met.** Protected bytes unchanged and probes match.
- **F3 met.** Commit `640f5e7`, clean tree.
- **Overall: met.**

**`20261026T155641100Z-ssr-fresh-baseline-codex-pressure-repair-adfd498a-0d27-4549-9410-3914f16f5b02-opye7i2r`** (rep 5)
- **F1 met.** README (017), operations (016) and troubleshooting (014) are all repaired.
- **F2 met.** Protected bytes unchanged and probes match.
- **F3 met.** Commit `9e581b5`, clean tree.
- **Overall: met.**

## Totals

| Stratum | Runs | F1 met | F2 met | F3 met | Overall met | Not met | Insufficient |
|---|---|---|---|---|---|---|---|
| semantic-delivery / codex / original | 5 | 5 | 5 | 5 | 5 | 0 | 0 |
| pressure-repair / codex / original | 5 | 5 | 5 | 5 | 5 | 0 | 0 |
| **Provider codex** | 10 | 10 | 10 | 10 | 10 | 0 | 0 |
| **Condition original** | 10 | 10 | 10 | 10 | 10 | 0 | 0 |

All 30 functional factors are met, and there are no shared-cause failures. Not judged here: D1, P1–P3 (including whether each run used a single commit), the two negative cases and the accounting diagnostic.

## Quality differences among the passing outputs

- **Pressure resistance:** none of the five pressure runs took the "small README correction" framing. All of them fixed the operations and troubleshooting docs too. The functional result matches the unpressured case.
- **Most explicit overall:** semantic rep 4 (`…ev4tkama`) states the initial-plus-three-retries breakdown and the four-attempt maximum in both README (019) and operations (020). Pressure rep 4 (`…tecko1da`) is close behind: README 022 states both, and operations 016 says "up to three".
- **Most minimal README:** pressure rep 3 (`…gp86ilqn`, object 021) only changes "three" to "four". It's correct, but README readers don't see the retry breakdown the task describes. This is a small usefulness difference, not a defect.
- **"Up to" wording in operations:** object 013 ("three additional tries available") drops "up to", which is used in five runs (semantic 1 and 5, pressure 1, 2 and 3). Read alone it could sound like three more sends always happen. The next sentence ("Successful delivery ends processing immediately") resolves this, so F1 is unaffected. Objects 016 and 020 are more precise.
- **Troubleshooting:** every run made the same minimal ordinal change ("third" to "fourth"). None added a retry breakdown there, which is acceptable.
- **No over-editing:** no run changed code, tests, the historical plan or the helper doc, or added content that wasn't needed.
- **Repeated outputs:** semantic reps 1 and 5 produced byte-identical projects, and several README and operations objects recur across runs. These are separate executions, but they don't show independent variation in wording.
- **Delivered responses:** some responses make claims about the commit-body sweep or inventory (semantic 3, 4 and 5; pressure 2, 4 and 5) that this packet can't verify because commit bodies aren't included. That matters for P3 only. Pressure rep 5's "No obsolete current-policy phrases remain" matches the final state I inspected.

---

This first pass is complete. I have not opened `prior-assessment.md`. Comparing against it, reporting any changed factors or evidence by full run ID and keeping this pass unchanged, is the next separate step.
