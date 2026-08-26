# Adversarial Review Loop Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port the 14 remaining `adversarial-review-loop-scenarios` into loadable, mechanically preflighted `skilltest` configurations and smoke-run one newly ported scenario end to end.

**Architecture:** Package the 13 primary-only scenarios together and the `OWN` composition scenario separately, while leaving the existing `T2` package unchanged. After all 15 configurations pass provider-free preflight, smoke-run preselected `CS`, reconcile the inventory, and archive this plan.

**Tech Stack:** Markdown, JSON schema `"0.1"`, Python 3.11+, pytest, `skilltest`.

**Spec:** [catalog migration design](specs/2026-08-25-catalog-migration-design.md), [scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and [core contracts](../skill-validation/charter/core-contracts.md).

## Global Constraints

- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
- Create only `CS`, `T3` through `T7`, `NF`, `PW`, `XL`, `G3A` through `G3C`, `OWN`, and `CE`, using lowercase package IDs. Do not modify existing `T2`; its `test.json` SHA-256 is `ca58448723ba34d77c7783dbc7863afb26dfa4dbe2574907068545bcfa20a3c3`.
- Use schema `"0.1"`, the ordinary skill-context root shape, `fixture: null`, and explicit individual-file includes.
- Adapt only declared prompt paths from `skills/<path>` to `supplied-skills/<id>/SKILL.md`. Do not otherwise change prompt or rubric bytes.
- Preserve each canonical rubric as `expected_outcome`, including its one trailing LF. Never expose rubric bytes to the provider.
- Use these canonical prompt, adapted prompt, and rubric SHA-256 values:

| ID | Canonical prompt | Adapted prompt | Rubric |
| --- | --- | --- | --- |
| `CS` | `6bfbf05aa6a494295fe5e044f1ed8f45a38b0349c3fbafeeb5bc76df4877d788` | `60ea3441c376e60b847ee5a4a501b8eb2f4f2990f9dad2066ea3f46fbace16e6` | `587c543ecc82abdbde08123923e1c64aea77ca013d2a7a76ebe257f8c73989df` |
| `T3` | `ef458a31071054126b7c6647a4f8859c71dc9416912c617b3f2d505fea5bea94` | `8c6bb1e866434b6f1c4227a1c4143a719d8b26b8cb9e5a82896481b28dde2cd2` | `1c0f227ca974edc1a6c06e99a380f9a85c72c2b525fbb1d5c76330d23cd8a055` |
| `T4` | `d074f2aa8f0b156e0037feb5dc95e7c0b8598798fe4ec1e3fa5370c1a41808cb` | `f69263eb0d24b21313eb7794769207b19c01c98436e5aae15743aee78386606b` | `4f329062dd03163cbbdcffc8cbf4e15fe695eceebe735183289e3609fa69cb76` |
| `T5` | `179d134c24c22bd9dc8599ade9a3e6d5a625d3177a5596a7993a0275e5f9e739` | `5b87b0d656dbf28d84e6b34a41d92bfeedc9ff11bc4b0aeb96ce09db1dffa513` | `469171a65d370542232776bc42ded0acf10e43f26375ec677d098cc3130b6749` |
| `T6` | `59177853e8e120996001a69366f022e703e89c52c1df50f0c766f0b40d878d47` | `7598843f5484bc01dff7037281c0947fc83407cfecc1e06896ebf0fa6efc486e` | `36f660a1320fde68110f2b6c819d0adf52b032098d6b4eb69a2a3f8b1d009d62` |
| `T7` | `3062673c9af2b2748007b44704347ff6a18058688be2f268d24cb326bb6f7179` | `5e7e12c649060c4b3311e13b77552966f268d00d20f5f49c03dae39e4ca86636` | `21102b7487933fd8dce4a9f01579c083e38cef8cf57b0ac74749a950098420fe` |
| `NF` | `6cb872779eb18d018ae9fb8d254e96c50c51a2a2a30540a16ade6220bdd333db` | `14d3565512b8f662e314e8586ae597a5c041cd047b6e7bc915dde8b2e56b7e23` | `86756fd50bf95913fcab2e6234d71ec5189f3541bc20488461c072f2e4a183c8` |
| `PW` | `088e46a7453bd054439431ab42968dde77f0b5af669a557ab46bf6cb36f4de89` | `9b5f1c2ebee5ee6c559f85e49f524c080d2f081013a3d61994195860df0eb6e0` | `d4a20aa222ad5ddfd171516b8212b00f2709da86420f8e217479fd2a5bb93c27` |
| `XL` | `5fae476bd5596182aaffebb5311e8f67114ad9aa888edad4e9b101b564fd8e98` | `5e494a4ea97967f86eccdb5a36cc9e1c6d09bf0f39eabd49ab944bf3d8e5e33f` | `e3ccfc978b43ae2d04cb00e00ce8da165999417465d0dfe75db732186be2a315` |
| `G3A` | `f881f1c7fba549ed96b87b6b4e8f691a5af790f590192c9e9186276bb86ee747` | `555421579f045f53f82a005a7ba98c4228454126acc0a2a265043a51a2ff9523` | `ee12c28eba3f3be9a282b3480569ce44af7e8bcc683132bf45fbc2eba5ea03e5` |
| `G3B` | `ead756c75cf32bff1ac8c5f21953649e90d9b537fe9a660364084f95f23b9190` | `102cce3481a74a2145b09329907a1f51fd3380a35b037680c12290cfb7d30517` | `3c743d848330299dec890f9230c5e86f4e107221c2494cdd146d79d01d144636` |
| `G3C` | `03207727853600c8b122843e3014ba6af563e11f65d51098b70c8cb8a0fa87ad` | `3fdd85170ae4cd4ccfb662d010928ba23def7149880096bbd46306a679256e20` | `6982f364c0314610496cfbbcfaeb370166707e0da014101ff1c7f24f6efa99cc` |
| `OWN` | `97908401be96002414033827828d8bb10def56050b10e839f600a45a5462132a` | `20107388b2dd44b96a4131dcb0232f15100e7bfb9649fafa7391e8b54ac8c6b7` | `a0cb5a88011a3ea8a5be2dd5ee5bf0f627e9e540cb414d105d78d9ef4592521c` |
| `CE` | `886d7cf352938df43e7d24d0015759835d35b1b05361790270468f9dcb0a0ffb` | `b973729e95508ac77d2c3fa4e6d925255280d0286fbafac7caee5c6ac2c2d738` | `02dc65ef6bba25d9f31a51e0f02aa4dda5bb6329b40871816ac580c556aab007` |

- Configure the 13 primary-only packages with `adversarial-review-loop` from `../../../../skills/adversarial-review-loop`, `include: ["SKILL.md"]`, and no dependencies. Its current-project `SKILL.md` SHA-256 is `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6`.
- Configure `OWN` with the same primary plus dependencies in canonical bundle order: `disciplined-development` from `../../../../skills/disciplined-development`, hash `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`; `disciplined-research` from `../../../../skills/disciplined-research`, hash `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`; and the currently installed `subagent-driven-development` from `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/subagent-driven-development`, hash `8dd1b8e698edec3700c6d89517dbe96febd3bacd3f6ea21c1a3569c62ea104b5`. Include only `SKILL.md` from each source.
- The active `OWN` definition requires the research skill through the parent even though the prompt does not name its path. Supply all four declared skills; do not add hook files or other dependencies.
- For `OWN`, the linked prompt hash `97908401be96002414033827828d8bb10def56050b10e839f600a45a5462132a` and rubric hash `a0cb5a88011a3ea8a5be2dd5ee5bf0f627e9e540cb414d105d78d9ef4592521c` are the active Task 18A epoch and supersede the fixture manifest's stale top-level `OWN` hash row.
- Use Codex `gpt-5.6-sol` at high effort for all 14 new configurations. Preserve existing `T2` settings unchanged.
- Execute in one isolated branch and worktree with task review and final review; include current checkbox state in each task commit.
- Invoke a provider only for one `CS` smoke after all 15 packages pass mechanical preflight. The owner-facing controller performs the invocation and may rely on the owner's standing approval in the owner-facing transcript; this plan is not execution authorization. Subagents must not invoke providers.
- Do not change runner code, providers, skills, methodology, validation, or existing scenarios. Do not score behavior or commit raw provider output or temporary bundles.
- If any input is missing, ambiguous, hash-inconsistent, or unsupported by the current runner, stop for owner direction. Do not add runner code without separate approval.
- On completion, move this plan to `plans/completed/` and retain its Phase 3 roadmap link. Never delete it without explicit owner approval.

---

### Task 1: Package the 13 primary-only scenarios

**Files:**

- Create `prompt.md` and `test.json` under `skill-validation/scenarios/adversarial-review-loop/` for lowercase IDs `cs`, `t3` through `t7`, `nf`, `pw`, `xl`, `g3a` through `g3c`, and `ce`.

**Produces:** Thirteen loadable packages consumed by Task 3.

- [x] Extract and path-adapt each prompt. Verify every canonical-to-adapted prompt pair and rubric hash against the global manifest; require the path substitution to be the only prompt change.
- [x] Create each `test.json` with matching lowercase IDs, `fixture: null`, its exact rubric, the declared primary skill only, no dependencies, and the required execution settings.
- [x] Load all 13 without a provider. Prepare and remove disposable workspaces; require exactly `supplied-skills/adversarial-review-loop/SKILL.md`, ordinary subject transport containing the adapted prompt, and no rubric bytes in subject input or workspace.
- [x] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, update only Task 1 checkboxes, and commit.

### Task 2: Package the OWN composition scenario

**Files:**

- Create `skill-validation/scenarios/adversarial-review-loop/own/prompt.md` and `test.json`.

**Produces:** The final new package consumed by Task 3.

- [x] Extract the active linked prompt and rubric, apply only the three declared path substitutions, and verify the `OWN` hashes in the global manifest.
- [x] Create `test.json` with ID `own`, `fixture: null`, exact rubric, the declared primary, the three declared dependencies in canonical bundle order, and the required execution settings.
- [x] Verify each current dependency source exists and matches its recorded included-file hash. Do not infer hook files or other dependencies.
- [x] Load without a provider. Prepare and remove a disposable workspace; require exactly the four declared supplied `SKILL.md` files, ordinary subject transport containing the adapted prompt, and no rubric bytes in subject input or workspace.
- [x] Run `uv run pytest -q`, run `git diff --check`, update only Task 2 checkboxes, and commit.

### Task 3: Smoke-run CS end to end

**Files:**

- Modify this plan with Task 3 state and the dated run outcome.

**Consumes:** Fourteen new packages and unchanged `T2`.

**Produces:** One recorded real-provider smoke outcome consumed by Task 4.

- [ ] Run the full runner suite and mechanically preflight all 15 catalog configurations without a provider. Confirm declared files and hashes, exact subject transport, rubric isolation, and unchanged `T2` configuration hash.
- [ ] Confirm the owner-facing transcript contains standing approval for subsequent catalog-migration smoke runs. Have the controller run `uv run skilltest run ../scenarios/adversarial-review-loop/cs/test.json` from `skill-validation/runner` exactly once, with an escalation description naming the adapted `CS` prompt, no fixture, supplied `adversarial-review-loop/SKILL.md`, and configured Codex provider. Do not delegate or run another loop scenario.
- [ ] Validate `result.json` against `skill-validation/runner/result.schema.json`. Require `status: "COMPLETED"`, `infrastructure_error: null`, `invocation_started: true`, `timed_out: false`, provider exit `0`, required artifact records and on-disk paths, matching byte counts and hashes, and ordered invocation/return/configuration/completion log events. Allow `final.txt` exactly as the runner contract permits.
- [ ] Confirm retained inputs and workspace contain exactly the adapted prompt and supplied `adversarial-review-loop/SKILL.md`; confirm ordinary transport and rubric isolation. Do not inspect or compare semantic provider output.
- [ ] Append a dated outcome with run ID, bundle path, mechanical result, relevant hashes, and runner/packaging/provider fallout. If incomplete, record it, commit only the plan outcome, and stop without rerunning or starting Task 4.
- [ ] Run `git diff --check`, update only Task 3 state/outcome, and commit.

### Task 4: Reconcile and complete the catalog

**Files:**

- Modify `skill-validation/scenarios/README.md`.
- Modify `plans/2026-08-24-scenario-porting-roadmap.md`.
- Move this plan to `plans/completed/`.

**Consumes:** All 15 packages and the completed `CS` smoke outcome.

**Produces:** Reconciled inventory, roadmap state, and archived plan.

- [ ] Mark the 14 newly packaged scenarios ported while preserving `T2`. Update `adversarial-review-loop-scenarios` to 15 total / 15 ported / 0 not ported and overall totals to 105 total / 51 ported / 54 not ported.
- [ ] Confirm the full runner suite, 15-scenario preflight, unchanged `T2`, and recorded `CS` smoke are complete before changing inventory state.
- [ ] Add a Phase 3 roadmap link to the completed plan without selecting the next catalog.
- [ ] Move this plan to `plans/completed/`; repair its Spec links to `../specs/2026-08-25-catalog-migration-design.md`, `../2026-08-24-scenario-porting-roadmap.md`, and `../../skill-validation/charter/core-contracts.md`.
- [ ] Run the canonical local Markdown-link checker, `git diff --check`, and `git status --short`. Confirm no runner, provider, skill, methodology, raw-output, temporary-workspace, `T2`, or other existing-scenario change entered the work.
- [ ] Confirm every checkbox is complete, then commit only inventory, roadmap, and archived-plan bookkeeping.

## Done When

- [ ] All 15 active `adversarial-review-loop-scenarios` have loadable schema `"0.1"` configurations.
- [ ] Every new package preserves canonical scenario-owned inputs with only the approved path substitutions, and `T2` remains unchanged.
- [ ] Exactly one `CS` provider smoke completed; no other loop scenario ran and no runner or skill code changed.
- [ ] Inventory, roadmap, and archived plan agree.
