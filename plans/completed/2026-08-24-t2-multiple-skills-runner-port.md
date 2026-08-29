# Explicit Skill Files and T2 Runner Port Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Require explicit skill-file manifests in `skilltest`, migrate the two existing configurations, and smoke-run `T2` with exactly its nine canonical `SKILL.md` files.

**Architecture:** Replace whole-directory skill copying with required per-skill file lists under configuration schema `"0.1"`. After that runner change is green, port `T2` with `include: ["SKILL.md"]` on all nine skill declarations and run it once.

**Tech stack:** Python 3.11+, pytest, Markdown, JSON, `skilltest`, Codex CLI.

**Spec:** `plans/completed/specs/2026-08-24-explicit-skill-file-includes-design.md`, `plans/completed/2026-08-24-runner-shape-coverage.md`, `plans/2026-08-24-scenario-porting-roadmap.md`, and `skill-validation/charter/core-contracts.md`.

## Constraints

- Configuration schema version is the string `"0.1"`; the result schema remains integer version `1`.
- Every skill declaration requires a non-empty `include` list of unique relative regular-file paths and must explicitly include root-level `SKILL.md`.
- Reject directories, symlinks, absolute paths, empty paths, `.` or `..` components, duplicates, missing files, and missing `SKILL.md`.
- Copy only included files, preserving nested relative paths. Do not retain whole-directory copying or add globs, exclusions, directory includes, or fallback behavior.
- Change no provider, result, fixture, skill, or scenario behavior beyond migrating configuration packaging.
- For `T2`, use canonical source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`; adapt only `skills/` prompt paths to `supplied-skills/`.
- Run `T2` exactly once with Codex `gpt-5.6-sol` at low effort. Do not establish a baseline, change methodology, fix fallout, or commit raw provider output or the temporary bundle.
- Any runner change outside the approved explicit-file contract requires separate owner approval.

## Files

- Modify `skill-validation/runner/src/skilltest/config.py` and `workspace.py`.
- Modify focused runner tests and shared test configuration in `skill-validation/runner/tests/`.
- Modify `skill-validation/runner/README.md` and `plans/completed/specs/2026-08-23-single-run-skill-test-runner-design.md`.
- Modify the two existing WER `test.json` configurations.
- Create `skill-validation/scenarios/adversarial-review-loop/t2/prompt.md` and `test.json`.
- Update `skill-validation/scenarios/README.md`, this plan, and its link in `plans/2026-08-24-runner-shape-coverage.md` on completion.

---

### Task 1: Require explicit included files

- [x] Add `test_load_config_accepts_required_file_includes` using schema `"0.1"` with explicit root and nested files. Run only that test and confirm RED because the loader rejects the new schema or declaration shape.

- [x] Implement only valid declaration loading and retention, then rerun the acceptance test and require GREEN.

- [x] Add table-driven loader tests for every rejected form named in Constraints. Confirm RED on cases the acceptance implementation permits, then add the required validation and migrate existing configuration-test inputs to schema `"0.1"`. Run `uv run pytest -q tests/test_config.py` and require GREEN.

- [x] Add `test_prepare_workspace_copies_only_included_skill_files` and update its shared test configuration to explicit includes. Confirm RED because an unlisted source sibling is still copied.

- [x] Replace source-tree copying with copying only declared files into retained inputs, preserving nested paths; continue copying the already-filtered retained tree into the workspace. Update existing workspace expectations, run `uv run pytest -q tests/test_workspace.py`, then run the full suite and require GREEN.

- [x] Update the runner README and completed runner design to state the exact `"0.1"` contract and file-only copy behavior. Leave the result schema and result metadata unchanged.

- [x] Update `WER-05` and `WER-08` to schema `"0.1"` with `include: ["SKILL.md"]`. Load both configurations without invoking a provider, then run the full runner suite again.

### Task 2: Port and smoke-run `T2`

- [x] Verify the canonical `T2` manifest is prompt-contained with no fixture and exactly nine `SKILL.md` files. Confirm prompt SHA-256 `157ab2e1d09d24e08c18ab4e826d847d00d96a322c4387769901480e0590a9be` and rubric SHA-256 `5487fae2531b6153ee3f5d3d6fd399a5106326280f017d83accb14cd5eeaf2e9`.

- [x] Copy the prompt, changing only its sole `skills/` occurrence to `supplied-skills/`. Confirm adapted prompt SHA-256 `43acaf4c4651cb5a3b9020dfbd71b6196d739eea49a71e144d2667c636d01797`.

- [x] Create `test.json` with schema `"0.1"`; IDs `t2`; primary `adversarial-review-loop`; the other eight repository skills in canonical order; `include: ["SKILL.md"]` on every declaration; prompt `prompt.md`; fixture `null`; exact rubric as `expected_outcome`; and Codex `gpt-5.6-sol` at low effort.

- [x] Load the configuration without invoking a provider. Confirm the primary, dependency order, all nine include lists, fixture, prompt hash, skill hashes, and decoded rubric hash.

- [x] From `skill-validation/runner`, run exactly once:

  `uv run skilltest run ../scenarios/adversarial-review-loop/t2/test.json`

- [x] Inspect the retained result, inputs, subject input, workspace, provider record, output, and log. Confirm `COMPLETED`, `infrastructure_error: null`, exactly nine provider-visible skill files, canonical dependency order and hashes, and a withheld rubric.

- [x] Record whether the response is evaluable and, if so, compare it with the rubric as one observation only.

- [x] Mark `T2` ported in `skill-validation/scenarios/README.md`; update its catalog totals to 15 total / 1 ported / 14 not ported and overall totals to 105 / 3 / 102.

- [x] Append the run outcome and fallout. If the run is incomplete, record it and stop without archiving the plan.

- [x] From `skill-validation/runner`, run `uv run pytest -q`. From the repository root, run `git diff --check` and `git status --short`. Confirm no raw output, bundle, skill change, or unrelated file entered the change.

- [x] After the verification above passes, move this plan to `plans/completed/` and update the runner-shape plan's link. Run the canonical Markdown-link checker, `git diff --check`, and `git status --short` against that final layout.

## Done when

- [x] Schema `"0.1"` requires exact file includes and the runner copies no undeclared skill file.
- [x] Both existing configurations load under the new contract.
- [x] One successful `T2` run covers the multiple-supplied-skills shape with exactly nine canonical files.
- [x] The inventory and completed-plan link are reconciled, with no broader work.

## Run outcome — 2026-08-24

- **Run:** `20260824T205002418Z-t2-024df2b6-4030-4fd0-a1bb-106906f3155c-6ooohrkm`; bundle `/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/skilltest-runs/20260824T205002418Z-t2-024df2b6-4030-4fd0-a1bb-106906f3155c-6ooohrkm`.
- **Mechanical result:** `COMPLETED`; `infrastructure_error: null`; provider exit `0`; no timeout; duration `35.759s`.
- **Evidence:** configuration `ca58448723ba34d77c7783dbc7863afb26dfa4dbe2574907068545bcfa20a3c3`; adapted prompt `43acaf4c4651cb5a3b9020dfbd71b6196d739eea49a71e144d2667c636d01797`; decoded rubric `5487fae2531b6153ee3f5d3d6fd399a5106326280f017d83accb14cd5eeaf2e9`. The result records the canonical dependency order and exactly nine skill inputs whose hashes match the preflighted complete-control files; retained and workspace copies match. The rubric is absent from subject input and workspace, and the configuration snapshot was written after provider return.
- **Observed behavior:** evaluable. As one observation, the response satisfies all three rubric criteria: it accepts the complete one-member class, re-runs the same reviewer against the fixed HEAD, and applies the existing loop directly without restarting review or substituting another workflow.
- **Runner fallout:** none blocking. Explicit file manifests produced exactly the nine configured provider-visible files, and the retained evidence was sufficient for inspection.
- **Packaging fallout:** none. The sole prompt-path adaptation and all canonical prompt, rubric, dependency-order, and skill-file checks passed.
- **Provider fallout:** none blocking. Codex read all nine supplied files, returned `final.txt`, emitted empty stderr, and reported 130,225 input tokens, 99,072 cached input tokens, 1,214 output tokens, and 274 reasoning-output tokens in raw stdout.
- **Scenario fallout:** none blocking. The response was directly judgeable against the withheld rubric.
- **Skill-behavior fallout:** none from this observation. This is not a baseline or broader behavioral conclusion.
