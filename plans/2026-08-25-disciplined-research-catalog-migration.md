# Disciplined Research Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port all seven active `disciplined-research` scenarios into loadable, mechanically preflighted `skilltest` configurations and smoke-run one scenario end to end.

**Architecture:** Package the complete-bundle `DR-01` separately from the six single-skill scenarios, adapting only the declared `disciplined-research` skill path. After all seven packages pass provider-free preflight, smoke-run preselected `DR-05`, then reconcile the inventory and archive this plan.

**Tech Stack:** Markdown, JSON schema `"0.1"`, Python 3.11+, pytest, `skilltest`.

**Spec:** [catalog migration design](specs/2026-08-25-catalog-migration-design.md), [scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and [core contracts](../skill-validation/charter/core-contracts.md).

## Global Constraints

- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
- Create only `DR-01` through `DR-07`; none is already ported.
- Use schema `"0.1"`, the ordinary skill-context root shape, and explicit individual-file includes.
- Materialize only prompts and fixtures. Store each rubric unchanged as `expected_outcome`, including its one trailing LF; never expose rubric bytes to the provider.
- Adapt only `skills/disciplined-research/SKILL.md` to `supplied-skills/disciplined-research/SKILL.md` in prompts. Do not otherwise change prompt, rubric, or fixture bytes.
- Use current project skill files. Include only each declared skill's `SKILL.md`; add no dependency sourcing or version-pinning machinery.
- Package only the declared local fixtures.
- Use Codex `gpt-5.6-sol` at high effort for all seven configurations.
- Execute in one isolated branch and worktree with task review and final review; include current checkbox state in each task commit.
- Invoke a provider only for one `DR-05` smoke after all seven packages pass mechanical preflight. The owner-facing controller performs the invocation and may rely on the owner's standing approval in the owner-facing transcript; this plan is not execution authorization. Subagents must not invoke providers.
- Do not change runner code, providers, skills, methodology, validation, or existing scenarios. Do not score behavior or commit raw provider output or temporary bundles.
- If an input is missing, ambiguous, hash-inconsistent, or unsupported by the current runner, stop for owner direction.
- On completion, move this plan to `plans/completed/` and retain its Phase 3 roadmap link. Never delete it without explicit owner approval.

---

### Task 1: Package complete-bundle DR-01

**Files:**

- Create `skill-validation/scenarios/disciplined-research/dr-01/prompt.md`.
- Create `skill-validation/scenarios/disciplined-research/dr-01/test.json`.
- Create `skill-validation/scenarios/disciplined-research/dr-01/fixture/project/README.md`.
- Create `skill-validation/scenarios/disciplined-research/dr-01/fixture/project/app/retention.py`.

**Produces:** One loadable complete-bundle package consumed by Task 3.

- [x] Extract the canonical prompt and active-catalog rubric cell with one trailing LF. Verify canonical prompt SHA-256 `4b79859709fa069aff54c03f71f712875ce419edbe01212d0b5b44cad8b45b74`, adapted prompt `9c832ded818a452ce6254623e6e68b9e8b474ca6017f6d3cb04697146393336d`, and rubric `f9094161371b6aeeb63a84a5268c68f31376cab7e814afb52062fe0ddc830621`. The prompt change must be only the approved path substitution.
- [x] Materialize `project/README.md` at SHA-256 `49061feab313293d6a1b8f23cae43056c79eeee88a00745a741595f98d54f1db` and `project/app/retention.py` at `900dd0268a517c797023f907ce3a14b6f66bc04b9c27787a153cd471dea6bec8`.
- [x] Create `test.json` with matching lowercase IDs, fixture `fixture`, the exact rubric, and required execution settings. Configure primary `disciplined-research` from `../../../../skills/disciplined-research` with `include: ["SKILL.md"]`.
- [x] Declare dependencies in canonical bundle order, each from `../../../../skills/<id>` with `include: ["SKILL.md"]`: `adversarial-review-loop`, `adversarial-review`, `concise-writing`, `disciplined-development`, `dispatching-development-subagents`, `lean-plan-writing`, `sweeping-stale-references`, and `writing-explicit-rationale`.
- [x] Verify included hashes: `disciplined-research` `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`; `adversarial-review-loop` `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6`; `adversarial-review` `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c`; `concise-writing` `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`; `disciplined-development` `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`; `dispatching-development-subagents` `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500`; `lean-plan-writing` `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac`; `sweeping-stale-references` `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`; `writing-explicit-rationale` `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.
- [x] Load without a provider. Prepare and remove a disposable workspace; require exactly the two fixture files plus nine declared `supplied-skills/<id>/SKILL.md` files, the ordinary-shape preamble followed by the adapted prompt, and no rubric bytes in subject input or workspace.
- [x] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, update only Task 1 checkboxes, and commit.

### Task 2: Package single-skill DR-02 through DR-07

**Files:**

- Create `prompt.md` and `test.json` under `skill-validation/scenarios/disciplined-research/dr-02/` through `dr-07/`.
- Create the canonical fixture files under each scenario's `fixture/`: `DR-02` three `sources/` files; `DR-03` `project/package.json` plus two `sources/` files; `DR-04` `project/payments/retry_policy.py`; `DR-05` `sources/nimbus-support-matrix.md`; `DR-06` three `project/upload-403/` files; and `DR-07` `sources/north-annex-hours.md`.

**Produces:** Six loadable single-skill packages consumed by Task 3.

- [ ] Extract and path-adapt each prompt. Verify canonical → adapted prompt SHA-256 pairs: `DR-02` `61113a936de2f2b82a8aa04b9ea33b55f9bf017096b7f9ff4eda0c240ba13466` → `5619d2864fb8f0fce9b317efb585d7eafa5ae6ad61b32992fe9429d96883a4f1`; `DR-03` `01cbb20fdd6e0dd4a2d000e2599a897c4df17791a0e61675bd163354e7bcf5f1` → `e3a8bb42d7e2d526263e164e39a4dc55c282ce28e17dbf7ec99ce5392b429c76`; `DR-04` `d6446bc6aee30bbb6534c18af706bfb6699f08a1b9383e070900de1ecdcc6362` → `8ca0f2cc83792162f879c689a7b2ad32d2c1e49ee117f56b202d784913d25961`; `DR-05` `c2b9901d48251d24dea35db1cda537b8fab95952615ea18fe4e97c57cd3055b6` → `cd39feb11805db0e259565063b1e201bb7fe36d27d17db4bc32b6db3bb3d1598`; `DR-06` `69ff7d3a620e03911313fcc76d28a2d813ff24648a266c9d994d554d2fbd5c0c` → `eb7ca4d2d8ff23c7afa51097e0bc869a694c58555acba3b690725de8667d0672`; `DR-07` `54850a6aff5bb87f231cdf5b765c0437901a8a3e4debe9e064b36c0670219c4c` → `d544de83c040deb9e39f24ac4c00592be82e0174c4eaf4c3231ac08b3e8b3acb`. Each change must be only the approved path substitution.
- [ ] Preserve each rubric with one trailing LF. Verify SHA-256: `DR-02` `b349513f2c134517d17831b6c8788ef011fca775f8335ad187fff8f97ebc1f85`; `DR-03` `0f9a44c2690d1af8d68ed23ccb4b72bbf804ea0a2db6496431049563c1757fca`; `DR-04` `5bcf27a85d8c055dfde82fe08bce8a25cac2b3850ca252652046d96500243132`; `DR-05` `f34530f4d3fcb87fb2e8097168f462bfc906843d4d793f0f4ab68e88b0920ed8`; `DR-06` `c479c2083bf950217e631b75db7b84a6166e81be4c05f9aaebacaec6981df7b1`; `DR-07` `a29cde034d63ecfc229e3821435e92dfe6c33dc348f4b3cef03fb151db4a3bd3`.
- [ ] Materialize fixtures at these hashes: `DR-02` `sources/city-museum-rfp.md` `5b50cf2558ef9a73335487198f2fd44a30339df58741df312374e169951340ca`, `sources/city-museum-addendum-2.md` `a882f3e3753ca78357333238e5f808d65d251852df04e0506bf2582940bec64f`, `sources/friends-newsletter.md` `a8746ab03403c6143e8f65d0e249436b5bb8341c2ebe4c953eb21797787fad5f`; `DR-03` `project/package.json` `1c2bb8f53dce6c7a90c2411d53f177dbfcba8ace56861399dd4f55412e0fb262`, `sources/orbital-release-notes.md` `1592db31a0848116b082b2093704d80847f672b540633c00b0ea6c30ad03c3f4`, `sources/orbital-maintainer-blog.md` `3f6e47ed632fde9a22f94ec764ca2c98b5365a9db6190566e8efb29234347488`; `DR-04` `project/payments/retry_policy.py` `a7099716223bf4a0c67fc32bda4c6816e6743be3e72aff5f52f3acc953f9a9c4`; `DR-05` `sources/nimbus-support-matrix.md` `0abe5b18aaa9a6315fa982dba406a8bb6255dd9652674956426fb34fbd4c5843`; `DR-06` `project/upload-403/evidence-index.md` `5ce87478b5f41f46f10dbba5b329f6eae004ca9b4a6895a495fa75ec292bfb46`, `runtime-config.json` `4ec39350c64e94229c7aaa59a719afc1c18c2c673d7d5215a8be38ee5307af13`, `worker.log` `d381395b47ed8fb03ca12fc8c1ab9a1c17299d28149d591119319705aed39eba`; `DR-07` `sources/north-annex-hours.md` `876d614b194ace2d807a947223565f3fdc9a597be45c6c1b753a9252a65e45da`.
- [ ] Create each `test.json` with matching lowercase IDs, fixture `fixture`, exact rubric, and required execution settings. Configure only primary `disciplined-research` from `../../../../skills/disciplined-research` with `include: ["SKILL.md"]`, dependencies `[]`, and verify its included hash `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`.
- [ ] Load all six without a provider. Prepare and remove disposable workspaces; require exactly each declared fixture set plus `supplied-skills/disciplined-research/SKILL.md`, the ordinary-shape transport, and no rubric bytes in subject input or workspace.
- [ ] Run `uv run pytest -q`, run `git diff --check`, update only Task 2 checkboxes, and commit.

### Task 3: Smoke-run DR-05 end to end

**Files:**

- Modify this plan with Task 3 state and the dated run outcome.

**Consumes:** All seven mechanically preflighted packages.

**Produces:** One recorded real-provider smoke outcome consumed by Task 4.

- [ ] Run the full runner suite and mechanically preflight all seven configurations without a provider. Confirm declared files and hashes, exact subject transport, and rubric isolation.
- [ ] Confirm the owner-facing transcript contains approval for subsequent catalog-migration smoke runs. Have the controller run `uv run skilltest run ../scenarios/disciplined-research/dr-05/test.json` from `skill-validation/runner` exactly once, with an escalation description naming the adapted prompt, `sources/nimbus-support-matrix.md`, `disciplined-research/SKILL.md`, and configured Codex provider. Do not delegate or run another DR scenario.
- [ ] Validate `result.json` against `skill-validation/runner/result.schema.json`. Require `status: "COMPLETED"`, `infrastructure_error: null`, `invocation_started: true`, `timed_out: false`, provider exit `0`, required artifact records and on-disk paths, matching byte counts and hashes, and ordered invocation/return/configuration/completion log events. Allow `final.txt` exactly as the runner contract permits.
- [ ] Confirm retained inputs and workspace contain exactly the adapted prompt, the declared fixture, and supplied `disciplined-research/SKILL.md`; confirm ordinary transport and rubric isolation. Do not inspect or compare semantic provider output.
- [ ] Append a dated outcome with run ID, bundle path, mechanical result, relevant hashes, and runner/packaging/provider fallout. If incomplete, record it, commit only the plan outcome, and stop without rerunning or starting Task 4.
- [ ] Run `git diff --check`, update only Task 3 state/outcome, and commit.

### Task 4: Reconcile and complete the catalog

**Files:**

- Modify `skill-validation/scenarios/README.md`.
- Modify `plans/2026-08-24-scenario-porting-roadmap.md`.
- Move this plan to `plans/completed/`.

**Consumes:** Seven packages and the completed `DR-05` smoke outcome.

**Produces:** Reconciled inventory, roadmap state, and archived plan.

- [ ] Mark `DR-01` through `DR-07` ported. Update `disciplined-research` to 7 total / 7 ported / 0 not ported and overall totals to 105 total / 29 ported / 76 not ported.
- [ ] Confirm the full runner suite, seven-scenario preflight, and recorded `DR-05` smoke are complete before changing inventory state.
- [ ] Add a Phase 3 roadmap link to the completed plan without selecting the next catalog.
- [ ] Move this plan to `plans/completed/`; repair its Spec links to `../specs/2026-08-25-catalog-migration-design.md`, `../2026-08-24-scenario-porting-roadmap.md`, and `../../skill-validation/charter/core-contracts.md`.
- [ ] Run the canonical local Markdown-link checker, `git diff --check`, and `git status --short`. Confirm no runner, provider, skill, methodology, raw-output, temporary-workspace, or existing-scenario change entered the work.
- [ ] Confirm every checkbox is complete, then commit only inventory, roadmap, and archived-plan bookkeeping.

## Done When

- [ ] All seven active `disciplined-research` scenarios have loadable schema `"0.1"` configurations.
- [ ] Every package preserves canonical scenario-owned inputs with only the approved path substitution.
- [ ] Exactly one `DR-05` provider smoke completed; no other DR scenario ran and no runner or skill code changed.
- [ ] Inventory, roadmap, and archived plan agree.
