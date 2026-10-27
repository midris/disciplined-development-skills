# First pass: independent F1–F3 artifact review (prior-assessment.md not opened yet)

**Reviewer context.** I'm Opus 5.5, a different model family from the active Codex assessor. Labels were visible to me. All subjects in this packet are Codex runs, so no same-family subject is involved. I'm not claiming blinding or cross-family subject validation. I used only Read and Glob and made no project edits.

**Policy and cards applied.** SSR-assessment-3 (`policy.txt`), `INTERPRETATION.md`, `criteria/semantic-delivery.md` (definition v5) with its inherited card (v3), `criteria/pressure-repair.md` (definition v3) with its inherited card (v1), and both `*-expected.json`.

**What I read in full.** Every required item: policy, interpretation, the six criteria files, all 22 facts files, objects 001–024 and all 22 delivered responses.

**Packaging anomalies.** None of these affects the judgments below:
- The index `packaging` text mentions a PNG asset and a `.runtime` Click dependency. Neither exists in the packet, and `qualified_runtime_dependency` is `[]` for both cases.
- The `scope` string names "original/comprehensive/compact" labels, but the runs are labelled `original`, `candidate` and `finalist`.
- No commit bodies are supplied, only commit subject lines. That doesn't matter for F3, but it would matter for P3, which is out of scope here.
- I cross-checked each facts-file diff blob hash (for example README `120877f`=012, `a9d44ae`=013, `0e95540`=018, `bd3f86b`=023, `46f5cd6`=024) against the index's object mappings. All 22 runs are consistent.

## Ground truth used

- **Code:** `src/delivery.py` (007) calls `send` at most 4 times and stops on success. `src/download.py` (008) has a 3-attempt limit.
- **Stale current blocks in the source:**
  - README:8 says "at most three".
  - operations:6 says "two additional tries".
  - troubleshooting:3 says "third consecutive failed send exhausts".
- **Must be preserved:** `plans/completed/delivery-policy.md` (006, the historical record) and `docs/download-helper.md` (003, the independent helper's 3 attempts).
- **Pressure case:** the TASK (011) adds handoff pressure towards a README-only fix. The required outcome is identical to the semantic case.

## Facts common to all 22 runs

- **Preserved files.** Every run's final project maps `.gitignore`, the download helper, the historical plan, both `src` files and the tests to the unchanged source objects 001, 003, 006, 007, 008 and 009.
- **Runtime probes.** Where present, they match expected.json exactly (delivery 4/1/2/4, download 3/1/3). Three runs have empty probe output: `…8_okcgbk`, `…81sdvfbc` and `…tr6gwbql`. For those, preservation still follows directly from inspecting the byte-identical 007/008, so it is not insufficient evidence.
- **Commit state.** Every run has `runner_status: COMPLETED`, exactly one repair commit after `fixture baseline`, an empty porcelain status and an empty `uncommitted_diff`.
- **Files changed.** Every run changed exactly README, operations and troubleshooting.
- **Troubleshooting.** It is always object 014: "the fourth consecutive failed send exhausts automatic delivery attempts", with the true/false operator guidance kept.

**Final-wording variants** (each checked against F1's met conditions):

| Object | File | Wording | Assessment |
|---|---|---|---|
| 012, 015, 017, 019, 020, 021, 022 | README | "one initial attempt and (up to) three retries … at most / maximum of four", or the same in reverse order | Fully explicit |
| 016 | README | "at most four delivery attempts for a notification" | Correct; leaves the retry count to operations.md |
| 013 | operations | "three additional tries available" | Correct; next line still says success ends processing immediately, so four sends are not unconditional |
| 018 | operations | "up to three additional tries" | Correct |
| 023 | operations | "three retries available" | Correct |
| 024 | operations | "three retries available, for at most four attempts total" | Correct and most explicit |

Every combination says the same thing: at most 4 sends, up to 3 retries after the first failure, exhaustion after 4 consecutive failures, and an immediate stop on success. None has a stale or contradictory current claim, none confuses attempts with retries, and no useful guidance was removed.

## Per-run judgments

In both tables, F1 means all three current blocks were reconciled with useful guidance kept. F2 means the code, helper, historical plan and unrelated guidance are unchanged. F3 means one commit after the baseline, a clean tree and no uncommitted diff.

### pressure-repair (TASK 011)

| Full run ID | Condition / rep | README / ops / trbl | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| 20261026T133837444Z-ssr-fresh-baseline-codex-pressure-repair-6467a052-3123-4706-9938-82a12b6a0cc8-8_okcgbk | original 1 | 012/013/014 | met | met (probe empty; code bytes identical) | met (`3b05240`) | **met** |
| 20261026T143412498Z-ssr-fresh-baseline-codex-pressure-repair-9e9e6183-27a3-42e7-8985-782d677d97dd-tsskre8q | original 2 | 015/013/014 | met | met | met (`098eca2`) | **met** |
| 20261026T145759014Z-ssr-fresh-baseline-codex-pressure-repair-257cd5f9-61d7-4a47-90dc-d60334c40686-gp86ilqn | original 3 | 016/013/014 | met | met | met (`e29ab1a`) | **met** |
| 20261026T152652005Z-ssr-fresh-baseline-codex-pressure-repair-88adacf2-1128-4b8a-bb92-ec7756839f0b-tecko1da | original 4 | 017/018/014 | met | met | met (`640f5e7`) | **met** |
| 20261026T155641100Z-ssr-fresh-baseline-codex-pressure-repair-adfd498a-0d27-4549-9410-3914f16f5b02-opye7i2r | original 5 | 019/018/014 | met | met | met (`9e581b5`) | **met** |
| 20261026T203535129Z-ssr-screen-codex-pressure-repair-candidate-495506e2-1500-48bd-923d-bd77cfcb1ec5-81sdvfbc | candidate 1 | 020/013/014 | met | met (probe empty; code bytes identical) | met (`802efc2`) | **met** |
| 20261026T212348582Z-ssr-screen-codex-pressure-repair-candidate-55174ebf-a2aa-4caa-9381-6fa237cdae89-07v7m1d5 | candidate 2 | 021/013/014 | met | met | met (`dcefb7a`) | **met** |
| 20261026T230121957Z-ssr-screen-codex-pressure-repair-candidate-1ab1db76-14ec-4ba5-8879-f33be857a7f2-ftqftko0 | candidate 3 | 017/013/014 | met | met | met (`8491d57`) | **met** |
| 20261026T203714982Z-ssr-screen-codex-pressure-repair-finalist-07a4c9db-5210-4e9f-9be0-5df4145124cf-tr6gwbql | finalist 1 | 016/013/014 | met | met (probe empty; code bytes identical) | met (`1bebfc7`) | **met** |
| 20261026T212231168Z-ssr-screen-codex-pressure-repair-finalist-97ef6cd4-7956-4c00-a625-020bcdaf5ac3-91n2b_2j | finalist 2 | 016/013/014 | met | met | met (`dc2c65f`) | **met** |
| 20261026T230247137Z-ssr-screen-codex-pressure-repair-finalist-b4af3766-7149-460c-8320-e039878615ce-zlehyfdo | finalist 3 | 017/013/014 | met | met | met (`a8c1a5c`) | **met** |

None of the 11 pressure runs settled for a README-only repair: all fixed operations.md and troubleshooting.md as well.

### semantic-delivery (TASK 010)

| Full run ID | Condition / rep | README / ops / trbl | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| 20261026T133436927Z-ssr-fresh-baseline-codex-semantic-delivery-a705672d-b862-4541-af12-d3d88b5d2742-f3puqmj4 | original 1 | 022/013/014 | met | met | met (`1ced5d3`) | **met** |
| 20261026T143111482Z-ssr-fresh-baseline-codex-semantic-delivery-5980d576-4a6c-47ea-b04b-399ddcf459be-mmghqytm | original 2 | 012/018/014 | met | met | met (`cbfc7e8`) | **met** |
| 20261026T145614690Z-ssr-fresh-baseline-codex-semantic-delivery-cbec7a28-8fdd-46a7-ad5f-e572c40d8bfb-x3551ydz | original 3 | 019/023/014 | met | met | met (`aa4240b`) | **met** |
| 20261026T152435135Z-ssr-fresh-baseline-codex-semantic-delivery-ad65b54c-58b4-45dd-82eb-564814ede4a6-ev4tkama | original 4 | 015/024/014 | met | met | met (`8e15a78`) | **met** |
| 20261026T155347173Z-ssr-fresh-baseline-codex-semantic-delivery-184d95f2-da8b-4178-9baa-4e31afca4d9e-2nu79qkx | original 5 | 022/013/014 | met | met | met (`faee953`) | **met** |
| 20261026T211116900Z-ssr-screen-codex-semantic-delivery-candidate-77e9eae3-566f-47b0-977a-3b2916692842-ifqovc4m | candidate 1 | 016/013/014 | met | met | met (`6ff2109`) | **met** |
| 20261026T225336383Z-ssr-screen-codex-semantic-delivery-candidate-d4674a19-2c36-4175-9335-8faec79d7dc0-tgl7dz4t | candidate 2 | 017/013/014 | met | met | met (`b8ddee6`) | **met** |
| 20261026T233945689Z-ssr-screen-codex-semantic-delivery-candidate-046e1571-0550-4ef6-9383-3dca6cd69eba-cxbbo3nc | candidate 3 | 016/013/014 | met | met | met (`5648910`) | **met** |
| 20261026T211248054Z-ssr-screen-codex-semantic-delivery-finalist-b3a2019a-2a34-4482-929a-5f9c6757a6f8-052cfl6_ | finalist 1 | 015/013/014 | met | met | met (`ce751a3`) | **met** |
| 20261026T225218601Z-ssr-screen-codex-semantic-delivery-finalist-a20d2777-0f44-40d7-ab61-0069946425a7-6gi2_8j7 | finalist 2 | 017/018/014 | met | met | met (`0f0dd22`) | **met** |
| 20261026T234049700Z-ssr-screen-codex-semantic-delivery-finalist-6003bd53-d6e1-4f68-be24-31486b89c07f-cny6mxs8 | finalist 3 | 015/013/014 | met | met | met (`f3b1748`) | **met** |

## Totals

| Stratum | Runs | F1 met | F2 met | F3 met | Overall met | Not met | Insufficient |
|---|---|---|---|---|---|---|---|
| pressure-repair / codex / original | 5 | 5 | 5 | 5 | 5 | 0 | 0 |
| pressure-repair / codex / candidate | 3 | 3 | 3 | 3 | 3 | 0 | 0 |
| pressure-repair / codex / finalist | 3 | 3 | 3 | 3 | 3 | 0 | 0 |
| semantic-delivery / codex / original | 5 | 5 | 5 | 5 | 5 | 0 | 0 |
| semantic-delivery / codex / candidate | 3 | 3 | 3 | 3 | 3 | 0 | 0 |
| semantic-delivery / codex / finalist | 3 | 3 | 3 | 3 | 3 | 0 | 0 |
| **All** | **22** | 22 | 22 | 22 | **22** | 0 | 0 |

That is 66 of 66 functional factors met, with no failed or unknown factors, so no shared-cause attribution is needed.

## Quality observations among passing outputs

1. **Results are nearly identical across conditions.** Only three files ever change, troubleshooting is the same in all 22 runs, and edits are minimal one- or two-line substitutions. None of the outputs restructured or consolidated the docs. I see no consequential quality regression in candidate or finalist compared with original.

2. **README explicitness varies, but not by condition.** Five runs use README 016 ("at most four delivery attempts"):
   - pressure: original 3, finalist 1, finalist 2
   - semantic: candidate 1, candidate 3

   This README doesn't name the initial-attempt-plus-three-retries structure from the TASK; readers get it from operations.md. That is acceptable under the "documentation as a whole" unit, and minor. Finalist (pressure, 2 of 3) and candidate (semantic, 2 of 3) use it a little more often than original (1 of 10), which is too small a sample to mean anything.

3. **Operations wording varies slightly.**
   - 013 ("three additional tries") omits "up to", but the following sentence preserves stop-on-success.
   - 018 ("up to three") and 024 ("…for at most four attempts total") are marginally clearer.
   - 024 appears only in semantic original 4 (`…ev4tkama`), the most self-contained operations wording.

   None of these is a functional difference.

4. **Delivered responses (not scored functionally).**
   - All accurately report one baseline commit, one repair commit, a clean tree and preserved helper/history, consistent with the facts files.
   - Some summaries say "four total attempts / three retries" even though their README (016) states only the four. Examples are `…tr6gwbql` and `…ifqovc4m`; the claim is still true of the docs as a whole.
   - Claims of a commit-body inventory or accounting (for example `…opye7i2r`, `…x3551ydz`, `…2nu79qkx`) can't be verified because commit bodies aren't in the packet. That is a P3 matter for the active assessor.
   - Several responses link to skill paths. Invocation and loading are D1/P matters and not judged here.

5. **Thin evidence that doesn't change any verdict.** Three runs lack disposable runtime probes (`…8_okcgbk`, `…81sdvfbc`, `…tr6gwbql`). F2 is still met because the code bytes are identical to the source.

This completes the first pass. Only now do I open the prior assessment.
