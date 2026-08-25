# Writing Explicit Rationale Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port the four remaining active `writing-explicit-rationale` scenarios into loadable, mechanically preflighted `skilltest` configurations.

**Architecture:** Preserve the canonical scenario-owned bytes and adapt only `skills/` references to the runner's `supplied-skills/` workspace path. Reference current project skill files explicitly, preflight without a provider, and update inventory only after all four configurations pass.

**Tech Stack:** Markdown, JSON schema `"0.1"`, Python 3.11+, pytest, `skilltest`.

**Spec:** [catalog migration design](specs/2026-08-25-catalog-migration-design.md), [scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and [core contracts](../skill-validation/charter/core-contracts.md).

## Global Constraints

- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
- Create only `WER-01`, `WER-02`, `WER-06`, and `WER-07`; do not modify `WER-05` or `WER-08`.
- Use schema `"0.1"`, explicit individual-file includes, and the existing ordinary skill-context root shape.
- Materialize only prompts and fixtures. Store each rubric unchanged as `expected_outcome`; never copy it into provider-visible input.
- Adapt only canonical `skills/<id>/SKILL.md` prompt paths to `supplied-skills/<id>/SKILL.md`.
- Use current project skill files. For the external `writing-plans` dependency, use the project-installed copy available at implementation time and record its path and hash.
- Execute the catalog in one isolated branch and worktree, with task review and final review before merge.
- Update each checkbox immediately when its step completes and include the active plan state in every task commit.
- Do not invoke a provider. Do not change runner code, providers, skills, methodology, validation, or already-ported scenarios.
- If any declared input is missing, ambiguous, hash-inconsistent, or unsupported by the current runner, stop and request owner approval.

---

### Task 1: Package the fixture-free scenarios

**Files:**

- Create `skill-validation/scenarios/writing-explicit-rationale/wer-01/prompt.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-01/test.json`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-02/prompt.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-02/test.json`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-06/prompt.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-06/test.json`.

**Produces:** Three loadable, fixture-free scenario packages consumed by Task 3.

- [ ] Verify the canonical and adapted prompt SHA-256 pairs: `WER-01` `bd0301ca240e287249de40d773fd2c6d37ca1f231b795beaf4f87bb003b68210` → `2260a7d08ade8737b504ebd1543996ec7a2977fe79b4936f3ffcdf1cf4ef9970`; `WER-02` `9b2621415525aab803ac01a234bc148746a0e9a437360c2eaa6da6aba7c2f7ab` → `bfbfc3d9dd30226dc7132c919778529868d000943f4920670835aa2b90ada51f`; `WER-06` `84fa4c432fdd47f0a9e1385c4721da55ef1fcfaf19e38963156ee2aede78ad64` → `f380cc324fe17a7be0b081c6a040edc78bfc5c8f2efd4d7fe1c9708e8fc37f26`. The arrow represents only the approved `skills/` → `supplied-skills/` path substitution.

- [ ] Extract each exact rubric from the active catalog table with one trailing LF. Verify rubric SHA-256 values `234e6cfca980392b2e5a44ec74bdd211bfcabee38cbed396ab2dbbe06dab350b` (`WER-01`), `753a412ed0bf2a36453aef4c08ab5a62e1783418978ace0a34bed99495bbbfd5` (`WER-02`), and `50b89b198c0b0fc471cd9c9aeca54f7006b518087b6b469ff619f1a0872a72bc` (`WER-06`).

- [ ] Materialize the three adapted prompts. Create each `test.json` with matching lowercase IDs, `fixture: null`, its exact rubric, and Codex `gpt-5.6-sol` at low effort.

- [ ] Configure `writing-explicit-rationale` as the primary skill with `source: "../../../../skills/writing-explicit-rationale"` and `include: ["SKILL.md"]`. Give `WER-02` and `WER-06` no dependencies. For `WER-01`, declare these eight dependencies in canonical bundle order, each from `../../../../skills/<id>` with only `SKILL.md`: `adversarial-review-loop`, `adversarial-review`, `concise-writing`, `disciplined-development`, `disciplined-research`, `dispatching-development-subagents`, `lean-plan-writing`, and `sweeping-stale-references`.

- [ ] Verify the included project skill hashes: `adversarial-review-loop` `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6`; `adversarial-review` `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c`; `concise-writing` `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`; `disciplined-development` `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`; `disciplined-research` `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`; `dispatching-development-subagents` `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500`; `lean-plan-writing` `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac`; `sweeping-stale-references` `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`; `writing-explicit-rationale` `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.

- [ ] Load all three configurations without invoking a provider. Prepare and remove disposable workspaces; require no fixture files, exactly the declared `supplied-skills/<id>/SKILL.md` files, the runner's exact ordinary-shape preamble followed by the adapted prompt bytes, and no rubric bytes in subject input or workspace.

- [ ] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, then commit these six scenario files with the current plan state.

### Task 2: Package the composition scenario

**Files:**

- Create `skill-validation/scenarios/writing-explicit-rationale/wer-07/prompt.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-07/fixture/project/wer-07/batch_import.py`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-07/fixture/project/wer-07/sources/ingest-architecture.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-07/fixture/project/wer-07/sources/quota-tokens.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-07/fixture/project/wer-07/sources/telemetry-comparison.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-07/test.json`.

**Produces:** One loadable composition scenario package consumed by Task 3.

- [ ] Verify canonical prompt SHA-256 `b4fbdd831bc8d569a4fe61fcb9898d112b44089779c9b4329c30e1df51ece92f`, adapted prompt SHA-256 `f6c5323018c9468f3b0686c7a5aa632a571eb560a749fcf2ac81b83a6506769b`, and active evaluator-withheld rubric file SHA-256 `2fc48c5a0c9c2aa06e5e20137fbfe0cc2c7f61d404b442b70a9b8c51da2063c5`. Ignore historical rubric epochs recorded elsewhere in the source document.

- [ ] Materialize the adapted prompt and the four canonical fixture files at the paths above. Verify fixture SHA-256 values: `batch_import.py` `2fbe0370868be60a4b8a96907c7404c65ae7b969bc5b63cfb0a6b521306beb20`; `ingest-architecture.md` `abc91b3248cae99aef1b3baa1418e5ea4eb0d943c99aa3460f75fd6fbec2f46a`; `quota-tokens.md` `0c06c4c7edc867de42105325eaccf30fb9112a7888a38eb812ec4b03945eeeef`; `telemetry-comparison.md` `34853c94fa465fc5ba2ef01b810419f2b3200b61a03b2111bdb2a150f31ba49a`.

- [ ] Create `test.json` with IDs `wer-07`, fixture `fixture`, the exact rubric as `expected_outcome`, and Codex `gpt-5.6-sol` at low effort. Use `writing-explicit-rationale` as primary. Declare dependencies in canonical supplied-context order: `disciplined-development`, `disciplined-research`, `writing-plans`, and `lean-plan-writing`; include only `SKILL.md` from each.

- [ ] Use repository sources `../../../../skills/disciplined-development`, `../../../../skills/disciplined-research`, `../../../../skills/lean-plan-writing`, and `../../../../skills/writing-explicit-rationale`. Verify their `SKILL.md` hashes are respectively `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`, `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`, `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac`, and `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`. At plan time, the installed `writing-plans` source is `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans` with `SKILL.md` SHA-256 `48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2`. If that installation moves before implementation, use the current installed project copy and update only the recorded source path and hash; stop if no copy is available.

- [ ] Load the configuration without invoking a provider. Prepare and remove a disposable workspace; require exactly the four fixture files and five declared `supplied-skills/<id>/SKILL.md` files, the exact ordinary-shape preamble followed by the adapted prompt bytes, and no rubric bytes in subject input or workspace.

- [ ] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, then commit the six `WER-07` scenario files with the current plan state.

### Task 3: Reconcile and complete the catalog

**Files:**

- Modify `skill-validation/scenarios/README.md`.
- Modify `plans/2026-08-24-scenario-porting-roadmap.md`.
- Complete and move this plan to `plans/completed/`.

**Consumes:** The four new packages from Tasks 1 and 2 and the two unchanged existing packages.

**Produces:** Reconciled inventory and roadmap state plus the archived completed plan.

- [ ] Mark `WER-01`, `WER-02`, `WER-06`, and `WER-07` ported. Update `writing-explicit-rationale` to 6 total / 6 ported / 0 not ported and overall totals to 105 total / 10 ported / 95 not ported.

- [ ] Add the completed catalog-plan link under the roadmap's catalog-migration phase. Do not select or plan the next catalog in this change.

- [ ] Run the full runner suite. Load and mechanically preflight all six `writing-explicit-rationale` configurations without invoking a provider; confirm the two existing packages are unchanged and all six preserve their declared packaging boundaries.

- [ ] Run the canonical local Markdown-link checker, `git diff --check`, and `git status --short`. Confirm no runner, provider, skill, methodology, raw-output, temporary-workspace, or already-ported scenario change entered the work.

- [ ] Confirm every checkbox reflects completed work, move this plan to `plans/completed/`, change its Spec links to `../specs/2026-08-25-catalog-migration-design.md`, `../2026-08-24-scenario-porting-roadmap.md`, and `../../skill-validation/charter/core-contracts.md`, then rerun the link and diff checks.

- [ ] Commit only the inventory, roadmap, and completed-plan bookkeeping.

## Done When

- [ ] All six active `writing-explicit-rationale` scenarios have loadable schema `"0.1"` configurations.
- [ ] The four new packages reproduce their canonical scenario-owned inputs with only approved path adaptation.
- [ ] No provider was invoked and no runner or skill code changed.
- [ ] Inventory, roadmap, and completed-plan state agree.
