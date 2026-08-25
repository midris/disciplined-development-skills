# Lean Plan Writing Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port the six remaining active `lean-plan-writing` scenarios into loadable, mechanically preflighted `skilltest` configurations and smoke-run one scenario end to end.

**Architecture:** Preserve the canonical prompts, rubrics, and fixtures, adapting only the two declared skill paths to the runner's `supplied-skills/` layout. Package the complete-bundle `LP-01` separately from the five lean-plus-writing-plans scenarios, smoke-run preselected `LP-05` after all packages pass preflight, then reconcile the inventory and archive this plan.

**Tech Stack:** Markdown, JSON schema `"0.1"`, Python 3.11+, pytest, `skilltest`.

**Spec:** [catalog migration design](specs/2026-08-25-catalog-migration-design.md), [scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and [core contracts](../skill-validation/charter/core-contracts.md).

## Global Constraints

- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
- Create only `LP-01`, `LP-03`, `LP-05`, `LP-06`, `LP-07`, and `LP-08`. Do not create retired `LP-04` or modify already-ported `LP-02`.
- Use schema `"0.1"`, the existing ordinary skill-context root shape, and explicit individual-file includes.
- Materialize only prompts and fixtures. Store each rubric unchanged as `expected_outcome`; never copy it into provider-visible input.
- Adapt only canonical `skills/lean-plan-writing/SKILL.md` and `skills/writing-plans/SKILL.md` prompt paths to their `supplied-skills/` equivalents. Do not otherwise change prompt, rubric, or fixture bytes.
- Use the current project skill files and the currently installed external `writing-plans` skill at `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans`. Include only each declared skill's `SKILL.md`; do not add sourcing or version-pinning machinery.
- Use Codex `gpt-5.6-sol` at high effort for all six configurations.
- Execute the catalog in one isolated branch and worktree, with task review and final review before merge.
- Update each checkbox immediately when its step completes and include the active plan state in every task commit.
- Invoke a provider only for one `LP-05` smoke run after all six new packages pass mechanical preflight. The owner-facing controller must obtain explicit owner approval and perform the invocation. Subagents may preflight and mechanically validate the retained bundle, but must not initiate the provider call.
- Do not change runner code, providers, skills, methodology, validation, or already-ported scenarios. Do not score behavior or commit raw provider output or temporary run bundles.
- If any declared input is missing, ambiguous, hash-inconsistent, or unsupported by the current runner, stop and request owner approval.
- On completion, move this plan to `plans/completed/` and retain its roadmap link. Never delete the plan without explicit owner approval.

---

### Task 1: Package the complete-bundle LP-01 scenario

**Files:**

- Create `skill-validation/scenarios/lean-plan-writing/lp-01/prompt.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-01/test.json`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-01/fixture/context/task.md`.

**Produces:** One loadable complete-bundle package consumed by Task 3.

- [x] Extract the canonical `LP-01` prompt and active-catalog rubric table cell with one trailing LF. Verify canonical prompt SHA-256 `d0d2daf8c9da4bb8d417bb064c5fc50a30cc756dcc287c15540d0c19ffed25f5`, adapted prompt SHA-256 `9e540a380e26858af73e1b4712a2b846237b6edb0a90a5d73f34e197c372effc`, and rubric SHA-256 `6f9e42155d26e1a779d54c7987893207847ed18cfa34981d07dc5bd19a3c0585`. The prompt hash change must contain only the two approved path substitutions.

- [x] Materialize `context/task.md` byte-for-byte at SHA-256 `c1de457ec9789a1345c72d3bf638486f5362d582bbb9917949eef8e00de5cabd`.

- [x] Create `test.json` with matching lowercase IDs, fixture `fixture`, the exact rubric, and the required execution settings. Configure `lean-plan-writing` as primary from `../../../../skills/lean-plan-writing`.

- [x] Declare these dependencies in order, each with `include: ["SKILL.md"]`: `adversarial-review-loop`, `adversarial-review`, `concise-writing`, `disciplined-development`, `disciplined-research`, `dispatching-development-subagents`, `sweeping-stale-references`, and `writing-explicit-rationale` from `../../../../skills/<id>`, followed by external `writing-plans` from `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans`.

- [x] Verify included `SKILL.md` hashes: `lean-plan-writing` `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac`; `adversarial-review-loop` `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6`; `adversarial-review` `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c`; `concise-writing` `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`; `disciplined-development` `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`; `disciplined-research` `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`; `dispatching-development-subagents` `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500`; `sweeping-stale-references` `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`; `writing-explicit-rationale` `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`; external `writing-plans` `48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2`.

- [x] Load the configuration without invoking a provider. Prepare and remove a disposable workspace; require exactly `context/task.md` plus ten declared `supplied-skills/<id>/SKILL.md` files, the exact ordinary-shape preamble followed by the adapted prompt bytes, and no rubric bytes in subject input or workspace.

- [x] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, then commit the scenario files with the current plan state.

### Task 2: Package the lean-plus-writing-plans scenarios

**Files:**

- Create `skill-validation/scenarios/lean-plan-writing/lp-03/prompt.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-03/test.json`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-05/prompt.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-05/test.json`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-05/fixture/context/import-brief.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-06/prompt.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-06/test.json`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-06/fixture/context/digest-brief.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-07/prompt.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-07/test.json`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-07/fixture/context/oversized-spec.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-08/prompt.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-08/test.json`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-08/fixture/context/coupled-spec.md`.

**Produces:** Five loadable lean-plus-writing-plans packages consumed by Task 3.

- [ ] Extract each canonical prompt and active-catalog rubric table cell with one trailing LF. Verify prompt SHA-256 pairs and rubric SHA-256 values: `LP-03` `6dc439c916aea496915f3e92163653f0eebf8526bd68ecd41c5c84ebc43d39ae` → `a21f556a0cf28dfb0dbfce4487e7855abf71cdf373ce0bc773e037126af7115e`, rubric `8e9f86e8532792799aeb94c0ad258f61f0692618dc07436f79c43017469714af`; `LP-05` `297d0f357f7ed7d2fff44c15d4b7e8fffebb8a7b91b58cfea09e2c7651feb1f8` → `de9c4a6f15a5dba2bc23c94936d69c6bdcfe254f9f655c0444150bbc847613e4`, rubric `237f61c94a6e3ec5be12afe4e8d5a2d78482651a43c217ab65c5aa9ea9bf27ac`; `LP-06` `a86f494b79defb37f6685312043ea7110c719f185fad0544079c974e97625d05` → `980908ce78faa35066de06aa7c9030e94c8d731622f92ea8f9cbba6c4367962e`, rubric `51bd263fe590b21e84c46cbbaa237866755b89081fa6c75e60beac79aeb58474`; `LP-07` `737bf8052c76033b74010eb4516b904f42f9cc894d62503a1c630363cb593c9b` → `f16b26b25e69537c00555520a002681be14e4d5b835053f71fcd700be8fda6ee`, rubric `5f1c9773e6e9f13de86dffea04d4cbc22dd01a9390e7403ff6f24461d1548894`; `LP-08` `ab34f34a06d4961d5dc6f1b52175f39517342c9cf9908a796f4afb01d81b18f5` → `0e9c6048427e03ca2e84c2fae545edfb1a84ecbdc6fb04631b069558fd62ed29`, rubric `698bfc496f0da6f1f3d78510f785f0d81b75c55176db97f29b307fbabfd25648`. Each prompt hash change must contain only the two approved path substitutions.

- [ ] Materialize the canonical fixtures: `LP-05` `context/import-brief.md` at SHA-256 `8789920dd0f54b1804e2a0aab65adfbcc728d525598d1d30a1d13b28c901c128`; `LP-06` `context/digest-brief.md` at `4df040c40f8888fb406265b3643e1c51e1eeaa91ad469d859dec0fd6f92dc792`; `LP-07` `context/oversized-spec.md` at `e2a2a54472f37e5ad830ec1016f66fe3b280463c5c400a84697b508d22713685`; `LP-08` `context/coupled-spec.md` at `05734fbdd024ff4db8404e46b995688ce30da1bacc9efc82b4bbbb5cd5a93ca1`. `LP-03` has fixture `null` and no fixture directory.

- [ ] Create each `test.json` with matching lowercase IDs, the exact rubric, and the required execution settings. Configure primary `lean-plan-writing` from `../../../../skills/lean-plan-writing` and dependency `writing-plans` from `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans`, each with `include: ["SKILL.md"]`. Use fixture `null` for `LP-03` and fixture `fixture` for `LP-05` through `LP-08`. Verify the two included hashes are `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac` and `48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2`.

- [ ] Load all five configurations without invoking a provider. Prepare and remove disposable workspaces; require only two declared supplied `SKILL.md` files per scenario, no fixture file for `LP-03`, exactly one declared fixture file for each of `LP-05` through `LP-08`, the exact ordinary-shape preamble followed by the adapted prompt bytes, and no rubric bytes in subject input or workspace.

- [ ] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, then commit the scenario files with the current plan state.

### Task 3: Smoke-run LP-05 end to end

**Files:**

- Modify `plans/2026-08-25-lean-plan-writing-catalog-migration.md` with checkbox state and the run outcome.

**Consumes:** All six mechanically preflighted packages from Tasks 1 and 2.

**Produces:** One recorded real-provider smoke outcome consumed by Task 4.

- [ ] Run the full runner suite and mechanically preflight all six new configurations without invoking a provider. Confirm each package preserves its declared files, hashes, subject input, and rubric boundary before starting the smoke run.

- [ ] After explicit owner approval in the owner-facing session, have the controller run `uv run skilltest run ../scenarios/lean-plan-writing/lp-05/test.json` from `skill-validation/runner` exactly once. Do not delegate this command, invoke another LP scenario, or repeat a completed run.

- [ ] Validate `result.json` against `skill-validation/runner/result.schema.json`. Require `status: "COMPLETED"`, `infrastructure_error: null`, `invocation_started: true`, `timed_out: false`, and provider exit `0`. Confirm the required `config`, `subject_input`, `stdout`, `stderr`, `final`, and `workspace` artifact records exist; require the config, subject-input, stdout, stderr, workspace, runner log, and result artifacts to exist on disk; allow `final.txt` to be present, absent, empty, or non-empty as the runner contract permits. Require every recorded byte count and SHA-256 to match its retained file, and require the runner log to record provider invocation, provider return, configuration snapshot, and terminal completion in order.

- [ ] Confirm retained inputs contain exactly the adapted prompt, `context/import-brief.md`, and the two declared `SKILL.md` files with the preflighted hashes; confirm the workspace contains exactly the fixture and two declared supplied-skill files; confirm subject input uses the ordinary-shape transport and the rubric is absent from subject input and workspace. Do not inspect or compare the semantic content of `final.txt`, stdout, or stderr against the rubric.

- [ ] Append a dated run outcome covering the run ID and bundle path, mechanical result, relevant hashes, and runner, packaging, and provider fallout. Do not describe or score response semantics, establish a behavioral result, or copy raw output or the temporary run bundle into the repository. If the run is incomplete, record it and proceed only to the plan-state check and commit below; do not change code, rerun, or begin Task 4.

- [ ] Run `git diff --check`, then commit only the updated plan state and recorded smoke outcome. If the run was incomplete, stop after this commit for owner direction.

### Task 4: Reconcile and complete the catalog

**Files:**

- Modify `skill-validation/scenarios/README.md`.
- Modify `plans/2026-08-24-scenario-porting-roadmap.md`.
- Move this plan to `plans/completed/`.

**Consumes:** The six packages from Tasks 1 and 2 and the completed smoke outcome from Task 3.

**Produces:** Reconciled inventory and roadmap state plus the archived completed plan.

- [ ] Mark `LP-01`, `LP-03`, `LP-05`, `LP-06`, `LP-07`, and `LP-08` ported without changing the existing `LP-02` entry. Update `lean-plan-writing` to 7 total / 7 ported / 0 not ported and overall totals to 105 total / 22 ported / 83 not ported.

- [ ] Confirm the full runner suite, six-scenario mechanical preflight, and recorded `LP-05` smoke outcome are complete before changing inventory state.

- [ ] Update Phase 3 of the roadmap with a link to the completed catalog plan. Do not select or plan the next catalog in this change.

- [ ] Move this plan to `plans/completed/`; do not delete it. Change its Spec links to `../specs/2026-08-25-catalog-migration-design.md`, `../2026-08-24-scenario-porting-roadmap.md`, and `../../skill-validation/charter/core-contracts.md`.

- [ ] Run the canonical local Markdown-link checker, `git diff --check`, and `git status --short`. Confirm no runner, provider, skill, methodology, raw-output, temporary-workspace, or already-ported scenario change entered the work.

- [ ] Confirm every checkbox reflects completed work, then commit only the inventory, roadmap, and completed-plan bookkeeping.

## Done When

- [ ] All seven active `lean-plan-writing` scenarios have loadable schema `"0.1"` configurations.
- [ ] Every new package reproduces its canonical scenario-owned inputs with only approved path adaptation.
- [ ] Exactly one `LP-05` provider smoke run completed, no other new LP scenario was invoked, and no runner or skill code changed.
- [ ] Inventory, roadmap, and archived-plan state agree.
