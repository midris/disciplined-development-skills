# Disciplined Development Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port the eight remaining `disciplined-development` scenarios into loadable, mechanically preflighted `skilltest` configurations and smoke-run one newly ported scenario end to end.

**Architecture:** Package `DD-01` through `DD-03` separately from the five atomic `DD-05` through `DD-09` scenarios, while leaving the existing `DD-04` package unchanged. After all nine configurations pass provider-free preflight, smoke-run preselected `DD-07`, then reconcile the inventory and archive this plan.

**Tech Stack:** Markdown, JSON schema `"0.1"`, Python 3.11+, pytest, `skilltest`.

**Spec:** [catalog migration design](specs/2026-08-25-catalog-migration-design.md), [scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and [core contracts](../../skill-validation/charter/core-contracts.md).

## Global Constraints

- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
- Create only `DD-01`, `DD-02`, `DD-03`, and `DD-05` through `DD-09`. Do not modify the existing `DD-04` package; its `test.json` SHA-256 is `6e697a02b1c58528fbd9130f50528cb699333f95360d6240a99a170caf12c878`.
- For `DD-01`, use the linked prompt file at the canonical source commit, SHA-256 `b3ec84e300d5070ab14beb1786493abc2648d70c4b9b3e0a3a6ffdd416b6cf47`. The owner ruled on 2026-08-26 that these bytes supersede the stale historical-table hash `b41c2835573b645e101280c2928c97f5363f519d73c769568924c3ded8f658ce`.
- Use schema `"0.1"`, the ordinary skill-context root shape, and explicit individual-file includes.
- Preserve every canonical prompt byte unchanged; no path adaptation is required. Materialize only prompts and declared fixtures.
- Store each rubric unchanged as `expected_outcome`, including its one trailing LF; never expose rubric bytes to the provider.
- Configure every new package with primary `disciplined-development` from `../../../../skills/disciplined-development`, `include: ["SKILL.md"]`, and `dependencies: []`. Verify the included current-project `SKILL.md` SHA-256 `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`.
- Use Codex `gpt-5.6-sol` at high effort for the eight new configurations. Preserve the existing `DD-04` execution settings unchanged.
- Execute in one isolated branch and worktree with task review and final review; include current checkbox state in each task commit.
- Invoke a provider only for one `DD-07` smoke after all nine packages pass mechanical preflight. The owner-facing controller performs the invocation and may rely on the owner's standing approval in the owner-facing transcript; this plan is not execution authorization. Subagents must not invoke providers.
- Do not change runner code, providers, skills, methodology, validation, or existing scenarios. Do not score behavior or commit raw provider output or temporary bundles.
- If any other input is missing, ambiguous, hash-inconsistent, or unsupported by the current runner, stop for owner direction.
- On completion, move this plan to `plans/completed/` and retain its Phase 3 roadmap link. Never delete it without explicit owner approval.

---

### Task 1: Package DD-01 through DD-03

**Files:**

- Create `prompt.md` and `test.json` under `skill-validation/scenarios/disciplined-development/dd-01/` through `dd-03/`.
- Create the seven declared `DD-02` fixture files under `dd-02/fixture/project/dd-02/` and the two declared `DD-03` fixture files under `dd-03/fixture/project/dd-03/sources/`.

**Produces:** Three loadable packages consumed by Task 3.

- [x] Extract each canonical prompt unchanged. Verify SHA-256: `DD-01` `b3ec84e300d5070ab14beb1786493abc2648d70c4b9b3e0a3a6ffdd416b6cf47`; `DD-02` `95deb13830eea682f06086c406dedb1a537b22f1bbf60598c4e1c231256ee706`; `DD-03` `e329586445f56ca213fc20557109c874b650219daf3860f079ce909b534c7f07`.
- [x] Preserve each rubric with one trailing LF. Verify SHA-256: `DD-01` `bb994c3b2e4adfc4feead9220ab9df89d53f5a74d1efa0e6bffbf733c7c0c9bb`; `DD-02` `801a1e8192a632c5aacee1ad63234af0987e73a498ad41dcba90610843181742`; `DD-03` `8daf6068c6546a1de19a77172513c7c6c74456df09193ed1b0722c46720e7cd4`.
- [x] Materialize `DD-02` fixtures at these hashes: `CLAUDE.md` `cc1f87826147c2799de88f208edbb798b24d6beb955bbadd5295e04fa1514d69`; `plans/export.md` `fd6dec456856f4aeb78cd4926a40ddf26c2f86da836e9559e91bff8f4b5d7daa`; `plans/specs/export.md` `77a8ad0cfa3ea65b02047968f412712d2b7723e4b943277ffdecfa3fd7ba735e`; `sources/cli-schema.md` `d31a0cf950c631454c0c3bb4e3a732e7e360776f7157cd81aa0921f8be3f42fd`; `sources/library-api.md` `253fb27d2587dd1ae1da9c6ff96c27a3c6c5c622301c661dc2e2a82a4452e1a4`; `sources/vendor-schema-status.md` `e696074e7b3c344a9e61601013af88036620ad981744cebc8acecca3964dffe5`; `sources/git-history.md` `a870dab35c878752f1b8c38538c08769df1ec21a2575fea0e723e484b7fd42bf`. Do not include `sources/operator-note.md`.
- [x] Materialize `DD-03` fixtures at these hashes: `sources/accepted-object-contract.md` `a7dd65af335e4d25626a543e42d61e78761155906b3cc42ef2c362cf81d8bdb5`; `sources/parser-capabilities.md` `717b21cb61d87637ca241791407d9c57594e29c122cd0ef6c35e3476b5c1bee1`.
- [x] Create each `test.json` with matching lowercase IDs, the exact rubric, and required execution settings. Use `fixture: null` for `DD-01` and fixture `fixture` for `DD-02` and `DD-03`; configure only the declared primary skill and no dependencies.
- [x] Load all three without a provider. Prepare and remove disposable workspaces; require exactly each declared fixture set plus `supplied-skills/disciplined-development/SKILL.md`, ordinary-shape subject transport, and no rubric bytes in subject input or workspace.
- [x] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, update only Task 1 checkboxes, and commit.

### Task 2: Package DD-05 through DD-09

**Files:**

- Create `prompt.md` and `test.json` under `skill-validation/scenarios/disciplined-development/dd-05/` through `dd-09/`.
- Create the declared fixture files under each scenario's `fixture/`: the seven `project/dd-02/` files for both `DD-05` and `DD-06`; `project/dd-07/signed-scope.md`; two `project/dd-08/` files; and three `project/dd-09/` files.

**Produces:** Five loadable packages consumed by Task 3.

- [x] Extract each canonical prompt unchanged. Verify SHA-256: `DD-05` `250300e505f05a6e1b139a352f1887e5116ac90ef99c18ac4b1c6d0139458ee4`; `DD-06` `0c296fd4f2a4245643e4ad17e746c06499e8ee920797721f654a6cf0aa74dda5`; `DD-07` `c79eb2bc14d0d9860a808c8875defc1f21bfaa7ec6a2ab356a08fe2c2cf88fd1`; `DD-08` `fc5e306045d9a6ff3e49913320ea48cff6fada7eb637d9aa0e0463c52dd6ced9`; `DD-09` `d0d0234d9688666656862f6a874e7ca491bd9b0d32b16ea1cdaad083f229a67d`.
- [x] Preserve each rubric with one trailing LF. Verify SHA-256: `DD-05` `cc900e882777acac4bb63f516861fa230ebb2ca33581ed463985062c91c8bd8c`; `DD-06` `701ce6503df5e72fe2617b391caea8a66a19533f4c8054aa1f1d6bc7d064b1b2`; `DD-07` `f8d47d834f1e29b5f3f61e3f1bb0e52cef7fea11d4fb20eef3626ca4a6d1889d`; `DD-08` `7dfb9766ffb31271028c1a4c97b1199b5251ab32e0bae79b73881ed828ee7283`; `DD-09` `a2e99c0a3cab2e3968d3e300489e1f6de484239ff442db49b8aec8ad02b26d3c`.
- [x] Materialize these seven `project/dd-02/` files for both `DD-05` and `DD-06`: `CLAUDE.md` `cc1f87826147c2799de88f208edbb798b24d6beb955bbadd5295e04fa1514d69`; `plans/export.md` `fd6dec456856f4aeb78cd4926a40ddf26c2f86da836e9559e91bff8f4b5d7daa`; `plans/specs/export.md` `77a8ad0cfa3ea65b02047968f412712d2b7723e4b943277ffdecfa3fd7ba735e`; `sources/cli-schema.md` `d31a0cf950c631454c0c3bb4e3a732e7e360776f7157cd81aa0921f8be3f42fd`; `sources/library-api.md` `253fb27d2587dd1ae1da9c6ff96c27a3c6c5c622301c661dc2e2a82a4452e1a4`; `sources/vendor-schema-status.md` `e696074e7b3c344a9e61601013af88036620ad981744cebc8acecca3964dffe5`; `sources/git-history.md` `a870dab35c878752f1b8c38538c08769df1ec21a2575fea0e723e484b7fd42bf`. Exclude `sources/operator-note.md` from both packages.
- [x] Materialize remaining fixtures at these hashes: `DD-07` `project/dd-07/signed-scope.md` `c9004c24d44bc4284fef9541ea3ff7912790227f288ac0c722a41df5a868cb25`; `DD-08` `project/dd-08/cli-schema.md` `dbfbe479f69212a39d1dc671aca5213fa6aa4e605fb769b1a1391b5d5abc5d05` and `project/dd-08/signed-scope.md` `8840eda21e4a8d4ec4771b1d46c7652c36729065075f9f971153d70a83e0a974`; `DD-09` `project/dd-09/active-plan.md` `c09b6c4727776e8871af3ac358656dba48b60566899b883527728cc35761199f`, `project/dd-09/git-history.md` `9a29b8528528d47840e0525cc96b4a8e7639875896543efd97ccb35fef03fdff`, and `project/dd-09/signed-change-scope.md` `071f0d9c1d5778f63c475a8c3a7299f5124f92386e648e9f293cf0209f2323ed`.
- [x] Create each `test.json` with matching lowercase IDs, fixture `fixture`, the exact rubric, required execution settings, only the declared primary skill, and no dependencies.
- [x] Load all five without a provider. Prepare and remove disposable workspaces; require exactly each declared fixture set plus `supplied-skills/disciplined-development/SKILL.md`, ordinary-shape subject transport, and no rubric bytes in subject input or workspace.
- [x] Run `uv run pytest -q`, run `git diff --check`, update only Task 2 checkboxes, and commit.

### Task 3: Smoke-run DD-07 end to end

**Files:**

- Modify this plan with Task 3 state and the dated run outcome.

**Consumes:** Eight new packages and unchanged `DD-04`.

**Produces:** One recorded real-provider smoke outcome consumed by Task 4.

- [x] Run the full runner suite and mechanically preflight `DD-01` through `DD-09` without a provider. Confirm declared files and hashes, exact subject transport, rubric isolation, and unchanged `DD-04` configuration hash.
- [x] Confirm the owner-facing transcript contains standing approval for subsequent catalog-migration smoke runs. Have the controller run `uv run skilltest run ../scenarios/disciplined-development/dd-07/test.json` from `skill-validation/runner` exactly once, with an escalation description naming the canonical prompt, `project/dd-07/signed-scope.md`, `disciplined-development/SKILL.md`, and configured Codex provider. Do not delegate or run another DD scenario.
- [x] Validate `result.json` against `skill-validation/runner/result.schema.json`. Require `status: "COMPLETED"`, `infrastructure_error: null`, `invocation_started: true`, `timed_out: false`, provider exit `0`, required artifact records and on-disk paths, matching byte counts and hashes, and ordered invocation/return/configuration/completion log events. Allow `final.txt` exactly as the runner contract permits.
- [x] Confirm retained inputs and workspace contain exactly the canonical prompt, declared fixture, and supplied `disciplined-development/SKILL.md`; confirm ordinary transport and rubric isolation. Do not inspect or compare semantic provider output.
- [x] Append a dated outcome with run ID, bundle path, mechanical result, relevant hashes, and runner/packaging/provider fallout. If incomplete, record it, commit only the plan outcome, and stop without rerunning or starting Task 4.
- [x] Run `git diff --check`, update only Task 3 state/outcome, and commit.

#### 2026-08-26 DD-07 smoke outcome

- The owner-facing controller performed the one authorized `DD-07` Codex smoke. Run ID: `20260826T145523018Z-dd-07-20f7e086-8d89-4e0b-9c92-40dc2247f63f-jso1ur9k`; retained bundle: `/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/skilltest-runs/20260826T145523018Z-dd-07-20f7e086-8d89-4e0b-9c92-40dc2247f63f-jso1ur9k`.
- Mechanical validation passed: `result.json` satisfies `result.schema.json`; it records `COMPLETED`, `infrastructure_error: null`, Codex `gpt-5.6-sol` at `high`, invocation started, no timeout, and provider exit `0`. Required artifact records point to on-disk files with matching byte counts and SHA-256 values; `final.txt` is present as permitted. Runner-log events appear in order: allocation, workspace preparation, provider arguments and invocation, provider return, raw-artifact persistence, configuration snapshot, then `COMPLETED`.
- Retained inputs and workspace contain only the canonical DD-07 prompt (`c79eb2bc14d0d9860a808c8875defc1f21bfaa7ec6a2ab356a08fe2c2cf88fd1`), `project/dd-07/signed-scope.md` (`c9004c24d44bc4284fef9541ea3ff7912790227f288ac0c722a41df5a868cb25`), and supplied `disciplined-development/SKILL.md` (`1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`). The retained configuration hashes to `99515b51b29d3142ef8e34ad36736f8115b343a08793a5d0ef46fe4d4505580a`; the exact ordinary subject transport hashes to `b5d8cb14dc336d8f915f497fe94c371760d1d1af28a9d280ca7462fba0184512`; withheld-rubric bytes are absent from provider-visible subject input and workspace.
- No runner, packaging, or provider fallout was observed mechanically. Provider response semantics were not inspected or compared. No additional scenario was run.

### Task 4: Reconcile and complete the catalog

**Files:**

- Modify `skill-validation/scenarios/README.md`.
- Modify `plans/2026-08-24-scenario-porting-roadmap.md`.
- Move this plan to `plans/completed/`.

**Consumes:** All nine packages and the completed `DD-07` smoke outcome.

**Produces:** Reconciled inventory, roadmap state, and archived plan.

- [x] Mark the eight newly packaged scenarios ported while preserving `DD-04`. Update `disciplined-development` to 9 total / 9 ported / 0 not ported and overall totals to 105 total / 37 ported / 68 not ported.
- [x] Confirm the full runner suite, nine-scenario preflight, unchanged `DD-04`, and recorded `DD-07` smoke are complete before changing inventory state.
- [x] Add a Phase 3 roadmap link to the completed plan without selecting the next catalog.
- [x] Move this plan to `plans/completed/`; repair its Spec links to `../specs/2026-08-25-catalog-migration-design.md`, `../2026-08-24-scenario-porting-roadmap.md`, and `../../skill-validation/charter/core-contracts.md`.
- [x] Run the canonical local Markdown-link checker, `git diff --check`, and `git status --short`. Confirm no runner, provider, skill, methodology, raw-output, temporary-workspace, `DD-04`, or other existing-scenario change entered the work.
- [x] Confirm every checkbox is complete, then commit only inventory, roadmap, and archived-plan bookkeeping.

## Done When

- [x] All nine active `disciplined-development` scenarios have loadable schema `"0.1"` configurations.
- [x] Every new package preserves canonical scenario-owned inputs without prompt adaptation, and `DD-04` remains unchanged.
- [x] Exactly one `DD-07` provider smoke completed; no other DD scenario ran and no runner or skill code changed.
- [x] Inventory, roadmap, and archived plan agree.
