# Skill Discovery Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port all 12 `skill-discovery` scenarios into loadable, mechanically preflighted `skilltest` configurations and smoke-run one scenario end to end.

**Architecture:** Package the active Task 18A target prompts as prompt-only, no-skill-context scenarios with no fixture. After all 12 configurations pass provider-free preflight, smoke-run preselected `DISC-12`, reconcile the inventory, and archive this plan.

**Tech Stack:** Markdown, JSON schema `"0.1"`, Python 3.11+, pytest, `skilltest`.

**Spec:** [catalog migration design](specs/2026-08-25-catalog-migration-design.md), [scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and [core contracts](../skill-validation/charter/core-contracts.md).

## Global Constraints

- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
- Create only `DISC-01` through `DISC-12`, using lowercase package IDs `disc-01` through `disc-12`.
- Use schema `"0.1"`, `skill_context: "none"`, and `fixture: null`. Do not declare a skill or dependencies.
- Copy each active `skill-validation/fixtures/skill-discovery/prompts/disc-XX-target.md` unchanged to its package's `prompt.md`. The prompts already embed the complete nine-description context; do not create fixture or supplied-skill files and do not adapt prompt bytes. The canonical supplied-file manifest is empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Preserve the canonical evaluator-withheld rubric unchanged as `expected_outcome`, including its trailing LF. Under `skill-validation/fixtures/skill-discovery/rubrics/`, use `task-18a-disc-01-10.md` for `DISC-01` through `DISC-10`, `disc-11.md` for `DISC-11`, and `disc-12.md` for `DISC-12`. Never expose rubric bytes to the provider.
- Use these canonical prompt and rubric SHA-256 values:

| ID | Prompt | Rubric |
| --- | --- | --- |
| `DISC-01` | `2f175787e2a45f998f44fbe4f13d3801425e82cca26537f504bac820dba60012` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-02` | `16506525e0f9ec43e2d5099aa411564492880a9ed8c5230c1407a20be7bc7682` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-03` | `dfa7e97c41e92c4583ae3efe9e79160eef984518f94e7bee09a75d59c786348c` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-04` | `aa9f3db4df0f178be34092c8b9b8d5968f73966f0aba9f0eb9d92c7502e56560` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-05` | `d5c5f4be0b5c646b7a6f93785a013fc0d23b104e296eca6e1edcc4287f8dfdbe` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-06` | `9b8fcb5893499e0a6de6cba0b39c121195231c5f393f9aba74c9f0c6718047c3` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-07` | `35d770d897461b3a2d5040da74436d8ea3f96465575e17a60c31631b85d9a04e` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-08` | `bcd2cf2514404899f202177273af766271652688b41dcef44db7e7462177aecc` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-09` | `3c31604d3575e4c9310f13c69f32bfadc27d91d1d0ed19995f8d7a17cfb02395` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-10` | `a265e73f8c3043e06c35a6d67eb11cf3d04495f5e7a96826f67e0855caf40ec6` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` |
| `DISC-11` | `f91713e4b75334486ceb6b625f6fdb432963659d8d8302042cb71e2c8a6d3f5f` | `200b06fcd313fc0f911a24f11c0a78be7696e8e5ad9c03c7c05070e81001c866` |
| `DISC-12` | `5a3c869dcf3307459fb548effeb4d4d015188fbd3a358a9f2fe312a800484b1c` | `a17e7937d27723947239247831e08f6064cfb4b7cb35159dc38bc3014c18c066` |

- Use Codex `gpt-5.6-sol` at high effort for all 12 configurations.
- Execute in one isolated branch and worktree with task review and final review; include current checkbox state in each task commit.
- Invoke a provider only for one `DISC-12` smoke after all 12 packages pass mechanical preflight. The owner-facing controller performs the invocation and may rely on the owner's standing approval for catalog-migration smoke runs. Subagents must not invoke providers.
- Do not change runner code, providers, skills, methodology, validation, or existing scenarios. Do not score behavior or commit raw provider output or temporary bundles.
- If any input is missing, ambiguous, hash-inconsistent, or unsupported by the current runner, stop for owner direction. Do not add runner code without separate approval.
- On completion, move this plan to `plans/completed/` and retain its Phase 3 roadmap link. Never delete it without explicit owner approval.

---

### Task 1: Package all 12 skill-discovery scenarios

**Files:**

- Create `prompt.md` and `test.json` under `skill-validation/scenarios/skill-discovery/disc-01/` through `disc-12/`.

**Produces:** Twelve loadable packages consumed by Task 2.

- [x] Copy each active target prompt exactly and verify its hash against the global manifest.
- [x] Create each `test.json` with its matching lowercase ID, `skill_context: "none"`, `fixture: null`, exact canonical rubric, and required execution settings.
- [x] Load all 12 without a provider. Prepare and remove disposable workspaces; require retained prompt input only, an empty provider-visible workspace, subject input exactly equal to `prompt.md`, and no rubric bytes in subject input or workspace.
- [x] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, update only Task 1 checkboxes, and commit.

### Task 2: Smoke-run DISC-12 end to end

**Files:**

- Modify this plan with Task 2 state and the dated run outcome.

**Consumes:** All 12 packaged scenarios.

**Produces:** One recorded real-provider smoke outcome consumed by Task 3.

- [ ] Run the full runner suite and mechanically preflight all 12 configurations without a provider. Confirm prompt/rubric hashes, exact no-skill subject transport, empty workspaces, and rubric isolation.
- [ ] Confirm the owner-facing transcript contains standing approval for catalog-migration smoke runs. Have the controller run `uv run skilltest run ../scenarios/skill-discovery/disc-12/test.json` from `skill-validation/runner` exactly once, with an escalation description naming the embedded-description `DISC-12` prompt, no fixture, no supplied skills or dependencies, and configured Codex provider. Do not delegate or run another skill-discovery scenario.
- [ ] Validate `result.json` against `skill-validation/runner/result.schema.json`. Require `status: "COMPLETED"`, `infrastructure_error: null`, `invocation_started: true`, `timed_out: false`, provider exit `0`, required artifact records and on-disk paths, matching byte counts and hashes, and ordered invocation/return/configuration/completion log events.
- [ ] Confirm retained inputs contain only the canonical prompt, the workspace contains no files, subject input equals the prompt bytes, and rubric bytes remain isolated. Do not inspect or compare semantic provider output.
- [ ] Append a dated outcome with run ID, bundle path, mechanical result, relevant hashes, and runner/packaging/provider fallout. If incomplete, record it, commit only the plan outcome, and stop without rerunning or starting Task 3.
- [ ] Run `git diff --check`, update only Task 2 state/outcome, and commit.

### Task 3: Reconcile and complete the catalog

**Files:**

- Modify `skill-validation/scenarios/README.md`.
- Modify `plans/2026-08-24-scenario-porting-roadmap.md`.
- Move this plan to `plans/completed/`.

**Consumes:** All 12 packages and the completed `DISC-12` smoke outcome.

**Produces:** Reconciled inventory, roadmap state, and archived plan.

- [ ] Mark all 12 scenarios ported. Update `skill-discovery` to 12 total / 12 ported / 0 not ported and overall totals to 105 total / 63 ported / 42 not ported.
- [ ] Confirm the full runner suite, 12-scenario preflight, and recorded `DISC-12` smoke are complete before changing inventory state.
- [ ] Add a Phase 3 roadmap link to the completed plan without selecting the next catalog.
- [ ] Move this plan to `plans/completed/`; repair its Spec links to `../specs/2026-08-25-catalog-migration-design.md`, `../2026-08-24-scenario-porting-roadmap.md`, and `../../skill-validation/charter/core-contracts.md`.
- [ ] Run the canonical local Markdown-link checker, `git diff --check`, and `git status --short`. Confirm no runner, provider, skill, methodology, raw-output, temporary-workspace, or existing-scenario change entered the work.
- [ ] Confirm every checkbox is complete, then commit only inventory, roadmap, and archived-plan bookkeeping.

## Done When

- [ ] All 12 active `skill-discovery` scenarios have loadable schema `"0.1"` configurations.
- [ ] Every package preserves the active target prompt and canonical rubric exactly, with no fixture or supplied skill context.
- [ ] Exactly one `DISC-12` provider smoke completed; no other skill-discovery scenario ran and no runner or skill code changed.
- [ ] Inventory, roadmap, and archived plan agree.
