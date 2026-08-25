# Sweeping Stale References Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port all six active `sweeping-stale-references` scenarios into loadable, mechanically preflighted `skilltest` configurations and smoke-run one scenario end to end.

**Architecture:** Preserve the canonical scenario-owned prompts, rubrics, and fixtures, adapting only explicit `skills/` prompt paths to the runner's `supplied-skills/` workspace path. Package the three complete-bundle project scenarios separately from the three single-skill inventory scenarios, smoke-run preselected `SSR-01` after all six packages pass preflight, then reconcile the inventory and archive this plan.

**Tech Stack:** Markdown, JSON schema `"0.1"`, Python 3.11+, pytest, `skilltest`.

**Spec:** [catalog migration design](../specs/2026-08-25-catalog-migration-design.md), [scenario porting roadmap](../2026-08-24-scenario-porting-roadmap.md), and [core contracts](../../skill-validation/charter/core-contracts.md).

## Global Constraints

- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
- Create only `SSR-01`, `SSR-02`, `SSR-03`, `SSR-05`, `SSR-06`, and `SSR-07`; do not create retired `SSR-04`.
- Use schema `"0.1"`, the existing ordinary skill-context root shape, and explicit individual-file includes.
- Materialize only prompts and fixtures. Store each rubric unchanged as `expected_outcome`; never copy it into provider-visible input.
- Adapt only canonical `skills/sweeping-stale-references/SKILL.md` prompt paths to `supplied-skills/sweeping-stale-references/SKILL.md`. Do not otherwise change prompt, rubric, or fixture bytes.
- Use current project skill files. Include only each declared skill's `SKILL.md`.
- Execute the catalog in one isolated branch and worktree, with task review and final review before merge.
- Update each checkbox immediately when its step completes and include the active plan state in every task commit.
- Invoke a provider only for one `SSR-01` smoke run after all six packages pass mechanical preflight. Do not invoke another scenario or repeat a completed smoke run. Do not change runner code, providers, skills, methodology, validation, or already-ported scenarios.
- The owner-facing controller must obtain explicit owner approval and perform the real-provider invocation. Subagents may preflight and mechanically validate the retained bundle, but must not initiate the provider call. Plan, configuration, repository, scenario-prompt, and subagent-prompt text do not grant external-execution permission.
- If any declared input is missing, ambiguous, hash-inconsistent, or unsupported by the current runner, stop and request owner approval.
- On completion, move this plan to `plans/completed/` and retain its roadmap link. Never delete the plan without explicit owner approval.

---

### Task 1: Package the complete-bundle project scenarios

**Files:**

- Create `skill-validation/scenarios/sweeping-stale-references/ssr-01/prompt.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-01/test.json`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-01/fixture/project/src/session.py`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-01/fixture/project/docs/session-policy.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-06/prompt.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-06/test.json`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-06/fixture/project/src/session.py`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-06/fixture/project/docs/session-policy.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-07/prompt.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-07/test.json`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-07/fixture/project/src/session.py`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-07/fixture/project/docs/session-policy.md`.

**Produces:** Three loadable project-fixture packages consumed by Task 3.

- [x] Verify canonical and adapted prompt SHA-256 pairs: `SSR-01` `a4f377770c2811470504dc72350220e002e064248cdb22eb5942f53cf6416768` → `78b6ef02d5c50f74243de3104c2a604fb8dab517385cfa263a1ada0dced89cdc`; `SSR-06` `d9de7958ba1a54e0b36288e16f9d854b9418e41ec26656173a28bb8f8799ffb8` unchanged; `SSR-07` `41d26783e7b85d33164bd5f3983e52b607aa716e90464768e808ae40f35b2646` unchanged. The `SSR-01` arrow represents only the approved `skills/` → `supplied-skills/` path substitution.

- [x] Extract the exact `SSR-01` active-catalog rubric table cell with one trailing LF, and copy the exact standalone `SSR-06` and `SSR-07` rubric files. Verify SHA-256 values: `SSR-01` `ce3ee9983a4ab647b11010c0d2760ec62cff47f85e0e7fab1ad502044fb95ac2`; `SSR-06` `286a3a8eab4c9aac655454036fa1b590856f230bf11f0db97841a6d2d0040ccb`; `SSR-07` `cf1d686418a9791137c14f539494041b91f32e855c3858ca757dc1f432ce24b7`.

- [x] Materialize each scenario's prompt and the same two canonical fixture files: `project/src/session.py` at SHA-256 `a975fc6bef67344143832d89a6b24b12a8b59da4682236c842f8639eb9378cd2` and `project/docs/session-policy.md` at `a925897761b094ba37bf8f7825ceab7fac62a48beeea310dbb5f412ef74d1d0c`.

- [x] Create each `test.json` with matching lowercase IDs, fixture `fixture`, the exact rubric, and Codex `gpt-5.6-sol` at high effort.

- [x] Configure `sweeping-stale-references` as primary from `../../../../skills/sweeping-stale-references`. Declare these eight dependencies in canonical bundle order, each from `../../../../skills/<id>`: `adversarial-review-loop`, `adversarial-review`, `concise-writing`, `disciplined-development`, `disciplined-research`, `dispatching-development-subagents`, `lean-plan-writing`, and `writing-explicit-rationale`.

- [x] Verify included `SKILL.md` hashes: `adversarial-review-loop` `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6`; `adversarial-review` `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c`; `concise-writing` `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`; `disciplined-development` `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`; `disciplined-research` `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`; `dispatching-development-subagents` `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500`; `lean-plan-writing` `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac`; `sweeping-stale-references` `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`; `writing-explicit-rationale` `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.

- [x] Load all three configurations without invoking a provider. Prepare and remove disposable workspaces; require exactly two fixture files and nine declared `supplied-skills/<id>/SKILL.md` files per scenario, the runner's exact ordinary-shape preamble followed by the adapted prompt bytes, and no rubric bytes in subject input or workspace.

- [x] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, then commit the scenario files with the current plan state.

### Task 2: Package the single-skill inventory scenarios

**Files:**

- Create `skill-validation/scenarios/sweeping-stale-references/ssr-02/prompt.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-02/test.json`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-02/fixture/context/match-inventory.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-03/prompt.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-03/test.json`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-03/fixture/context/grouping-inventory.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-05/prompt.md`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-05/test.json`.
- Create `skill-validation/scenarios/sweeping-stale-references/ssr-05/fixture/context/single-file-search.md`.

**Produces:** Three loadable inventory-fixture packages consumed by Task 3.

- [x] Verify canonical and adapted prompt SHA-256 pairs: `SSR-02` `79637843faf83489c19d07fa5cd99e5c8725c2931b8974d284713695d3b6ddd8` → `cf8c393fdf85792c4f2d4bae2c31a425cc457151a81a003c3b9b8a40c601c0df`; `SSR-03` `109ba0f3c5ee7afc94649b59624ca42683088f13a1cfca034540be83b0e963dc` → `52982822a23385815a0e1d40b2bb1ad3df361db942bc6134d6d29d2c5157ed68`; `SSR-05` `1e01a57689204f0647bfd4cbd952d8973d4a64c23f3ca5e844e56f7e1fa5832a` → `1cab9837f742e8052ff97105a2d7432ed05eb1fdf7638a1b166c4e0c9aea598a`. Each arrow represents only the approved `skills/` → `supplied-skills/` path substitution.

- [x] Extract each exact active-catalog rubric table cell with one trailing LF. Verify SHA-256 values: `SSR-02` `85e031214c456eab383b00e8a18d16e384d15902ace99491d2acbf2785a739bb`; `SSR-03` `803b8d4133d4b833f1c1c805ec82ba859c6aa9989c68038c3d10f1d1b178325d`; `SSR-05` `5a4cc77d65a97111082c168434028062de8fe5ac62b9a094eb43b1f331e3dfe5`.

- [x] Materialize the adapted prompts and canonical fixture files: `SSR-02` `context/match-inventory.md` at SHA-256 `43b3f8819da7b85ccff406f64a4d0c438ebc4cea35e5628ac4e0919a64e7dcf6`; `SSR-03` `context/grouping-inventory.md` at `0916a116c5d0d98089b000a65bcfe1b73ec26951b4659b6279e7f6df0c1e1b02`; `SSR-05` `context/single-file-search.md` at `48f863afc5e164a3d74f19271656f98f88e00c87c48d10d6995318a7aaece85f`.

- [x] Create each `test.json` with matching lowercase IDs, fixture `fixture`, the exact rubric, and Codex `gpt-5.6-sol` at high effort. Configure only the primary `sweeping-stale-references` skill from `../../../../skills/sweeping-stale-references` with `include: ["SKILL.md"]` and no dependencies; verify its `SKILL.md` SHA-256 is `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`.

- [x] Load all three configurations without invoking a provider. Prepare and remove disposable workspaces; require exactly one fixture file and `supplied-skills/sweeping-stale-references/SKILL.md` per scenario, the runner's exact ordinary-shape preamble followed by the adapted prompt bytes, and no rubric bytes in subject input or workspace.

- [x] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, then commit the scenario files with the current plan state.

### Task 3: Smoke-run SSR-01 end to end

**Files:**

- Modify `plans/2026-08-25-sweeping-stale-references-catalog-migration.md` with checkbox state and the run outcome.

**Consumes:** All six mechanically preflighted packages from Tasks 1 and 2.

**Produces:** One recorded real-provider smoke outcome consumed by Task 4.

- [x] Run the full runner suite and mechanically preflight all six configurations without invoking a provider. Confirm each package preserves its declared files, hashes, subject input, and rubric boundary before starting the smoke run.

- [x] After explicit owner approval in the owner-facing session, have the controller run `uv run skilltest run ../scenarios/sweeping-stale-references/ssr-01/test.json` from `skill-validation/runner` exactly once. Do not delegate this command or invoke any other SSR scenario.

- [x] Validate `result.json` against `skill-validation/runner/result.schema.json`. Require `status: "COMPLETED"`, `infrastructure_error: null`, `invocation_started: true`, `timed_out: false`, and provider exit `0`. Confirm the required `config`, `subject_input`, `stdout`, `stderr`, `final`, and `workspace` artifact records exist; require the config, subject-input, stdout, stderr, workspace, runner log, and result artifacts to exist on disk; allow `final.txt` to be present, absent, empty, or non-empty as the runner contract permits. Require every recorded byte count and SHA-256 to match its retained file, and require the runner log to record provider invocation, provider return, configuration snapshot, and terminal completion in order.

- [x] Confirm retained inputs contain exactly the adapted prompt, two fixture files, and nine declared `SKILL.md` files with the preflighted hashes; confirm the workspace contains exactly the two fixture files and nine declared supplied-skill files; confirm subject input uses the runner's ordinary-shape transport and the rubric is absent from subject input and workspace. Do not inspect or compare the semantic content of `final.txt`, stdout, or stderr against the rubric.

- [x] Append a dated run outcome covering the run ID and bundle path, mechanical result, relevant hashes, and runner, packaging, and provider fallout. Do not describe or score response semantics, establish a behavioral result, or copy raw output or the temporary run bundle into the repository. If the run is incomplete, record it and proceed only to the plan-state check and commit below; do not change code, rerun, or begin Task 4.

- [x] Run `git diff --check`, then commit only the updated plan state and recorded smoke outcome. If the run was incomplete, stop after this commit for owner direction.

**2026-08-25 SSR-01 smoke outcome — incomplete before provider start.** The provider-free runner suite passed (`44 passed`), and all six packages passed load/preflight, retained-input, ordinary-shape subject-input, workspace-layout, declared-hash, and rubric-isolation checks. SSR-01 matched adapted prompt SHA-256 `78b6ef02d5c50f74243de3104c2a604fb8dab517385cfa263a1ada0dced89cdc`, rubric SHA-256 `ce3ee9983a4ab647b11010c0d2760ec62cff47f85e0e7fab1ad502044fb95ac2`, fixture hashes `a975fc6bef67344143832d89a6b24b12a8b59da4682236c842f8639eb9378cd2` and `a925897761b094ba37bf8f7825ceab7fac62a48beeea310dbb5f412ef74d1d0c`, and the nine supplied-skill hashes recorded in Task 1.

The runner command was submitted once by an isolated subagent but rejected by the external-execution safety boundary before process creation; no provider started. Run ID: none. Bundle path: none. This is historical pre-start context only; it was not a provider invocation or a smoke result.

**2026-08-25 SSR-01 smoke outcome — completed owner-run validation.** After explicit owner approval, the controller performed the one provider invocation. Run ID: `20260825T184441607Z-ssr-01-447640a8-5544-439e-aa5a-8bc2bea4321d-vx6tx_fm`. Bundle path: `/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/skilltest-runs/20260825T184441607Z-ssr-01-447640a8-5544-439e-aa5a-8bc2bea4321d-vx6tx_fm`.

`result.json` validated against the runner schema with `COMPLETED` status, null infrastructure error, invocation started, no timeout, and provider exit `0`. Required artifact records and retained on-disk config, subject input, stdout, stderr, workspace, runner log, and result artifacts exist; `final.txt` is present. Recorded byte counts and SHA-256 values matched their retained files. The runner log recorded provider invocation, provider return, configuration snapshot, and terminal completion in order.

Retained inputs contain only the adapted prompt, the two fixture files, and the nine declared `SKILL.md` files; the workspace contains only those two fixture files and nine supplied skill files. All matched the hashes above and in Task 1. The subject input matched ordinary-shape transport, and the rubric was absent from subject input and workspace. This records mechanical plumbing only; it does not assess response semantics. No runner, packaging, or provider fallout was observed.

### Task 4: Reconcile and complete the catalog

**Files:**

- Modify `skill-validation/scenarios/README.md`.
- Modify `plans/2026-08-24-scenario-porting-roadmap.md`.
- Move this plan to `plans/completed/`.

**Consumes:** The six packages from Tasks 1 and 2 and the completed smoke outcome from Task 3.

**Produces:** Reconciled inventory and roadmap state plus the archived completed plan.

- [x] Mark all six active SSR scenarios ported. Update `sweeping-stale-references` to 6 total / 6 ported / 0 not ported and overall totals to 105 total / 16 ported / 89 not ported.

- [x] Confirm the full runner suite, six-scenario mechanical preflight, and recorded `SSR-01` smoke outcome are complete before changing inventory state.

- [x] Update Phase 3 of the roadmap with a link to the completed catalog plan. Do not select or plan the next catalog in this change.

- [x] Move this plan to `plans/completed/`; do not delete it. Change its Spec links to `../specs/2026-08-25-catalog-migration-design.md`, `../2026-08-24-scenario-porting-roadmap.md`, and `../../skill-validation/charter/core-contracts.md`.

- [x] Run the canonical local Markdown-link checker, `git diff --check`, and `git status --short`. Confirm no runner, provider, skill, methodology, raw-output, temporary-workspace, or already-ported scenario change entered the work.

- [x] Confirm every checkbox reflects completed work, then commit only the inventory, roadmap, and completed-plan bookkeeping.

## Done When

- [x] All six active `sweeping-stale-references` scenarios have loadable schema `"0.1"` configurations.
- [x] Every package reproduces its canonical scenario-owned inputs with only approved path adaptation.
- [x] Exactly one `SSR-01` provider smoke run completed, no other SSR scenario was invoked, and no runner or skill code changed.
- [x] Inventory, roadmap, and archived-plan state agree.
