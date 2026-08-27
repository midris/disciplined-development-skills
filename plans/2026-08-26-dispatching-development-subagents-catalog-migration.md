# Dispatching Development Subagents Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port all 11 `dispatching-development-subagents` scenarios into loadable, mechanically preflighted `skilltest` configurations and smoke-run one scenario end to end.

**Architecture:** Package the canonical prompts, rubrics, fixtures, and exact declared context using the runner's existing ordinary skill-context shape. After all 11 configurations pass provider-free preflight, smoke-run preselected `DSD-03`, reconcile the inventory, and archive this plan.

**Tech Stack:** Markdown, JSON schema `"0.1"`, Python 3.11+, pytest, `skilltest`.

**Spec:** [catalog migration design](specs/2026-08-25-catalog-migration-design.md), [scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and [core contracts](../skill-validation/charter/core-contracts.md).

## Global Constraints

- Use canonical source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c` and create only lowercase packages `dsd-01` through `dsd-11`.
- Use schema `"0.1"`, the ordinary skill-context root shape, explicit individual-file includes, and Codex `gpt-5.6-sol` at high effort.
- Use the active catalog definitions table in `skill-validation/dispatching-development-subagents.md` as the authority for each scenario's supplied context. Use the active prompt and rubric files under `skill-validation/fixtures/dispatching-development-subagents/`; historical run provenance may corroborate hashes but must not add provider-visible files. For `DSD-07`, the repaired active prompt file and fixture-manifest hash below supersede the stale prompt hash in Task 18A provenance.
- Adapt only these prompt paths: `skills/dispatching-development-subagents/SKILL.md`, `skills/disciplined-development/SKILL.md`, `skills/disciplined-development/hooks/review_nudge.py`, and `skills/superpowers/subagent-driven-development/SKILL.md` to their matching `supplied-skills/<id>/...` paths. Do not otherwise change prompt or rubric bytes.
- Preserve each rubric unchanged as `expected_outcome`, including its trailing LF. Never expose rubric bytes to the provider.
- Use these canonical prompt, adapted prompt, and rubric SHA-256 values:

| ID | Canonical prompt | Adapted prompt | Rubric |
| --- | --- | --- | --- |
| `DSD-01` | `b0d2273f25c29266f2e8aa1b75f6cc760aa6dc79d78f84f6fa8c3a7f82824ccb` | `fa4c2cff9bc7d3b65b2fb840d45e6f3f1389b16ad8bf36ca871fb5bb262e299b` | `acf3ade4ab145d91709ccbce6315fbb301bcb86cc8c5648932d839e0d98b13d0` |
| `DSD-02` | `750b43ea0d12d109c70e996578618da5d79717c2716b6878db0e4812a5226c4c` | `4113befe7e543d6f2a147106dc382c4f0c55669314607e2c106b35a6612072a7` | `ac3e61476eca2010dd37143b3ac942f392fa333c695fa98c1a68330a08237bb5` |
| `DSD-03` | `6e99e94ce865c2102799474225fa8ee500440d013d30b9a853951663b3ee0d70` | `e11b5cc4abe38a31f2c66d0c9364b849462a59b4796a4b67a3f85de4cad62dbc` | `c7b3fbf6eb092f8919cd8ec1eaa278af7f736f4fa1522bbb8e56bc536aab6570` |
| `DSD-04` | `31a5cbe423d9bd9531cc2706de2f9372d13af5bb142db5320e8887cb75ab2dfe` | `c9330e60aaf3700d49cdf5c91d07a74cdde61b78f19eb46c29c0d991ac6a7eec` | `dc29adc91e29ca32bae2fe3a8df3ba1a7cac3293add9eec2e77b7aeecaebd25b` |
| `DSD-05` | `5917fa9a572dd8ecce515b4728b946754bd00233655ebf0d505ef26b5ea98f33` | `ae6e05b8ba2f2a67f1e2dbe00ef50cf82022048a58300da454068f9a22747b68` | `fc5d43057ffdb3055d2fbd20dba98f594ac3a654807132e5b768e8651f8b0d6b` |
| `DSD-06` | `dce91ca050fb7e1cc3cad40d53b2df65c37c9184dc06fb0cb38a97190d672171` | `dce91ca050fb7e1cc3cad40d53b2df65c37c9184dc06fb0cb38a97190d672171` | `72246ee567b9c0353817a58d85f8ec632dd6bf89c59dbcffcc14e1fe12699769` |
| `DSD-07` | `366f109c8570927dec22908def32f52ff3f2119c116913666a7386d021b817a2` | `366f109c8570927dec22908def32f52ff3f2119c116913666a7386d021b817a2` | `50e6f2c823ff942820f99c659d2f660230359d380edc9ffa99048c6c05243d86` |
| `DSD-08` | `a08ec853a3a904b198c66667a8df8f85e5b3c60526d217878758d01b1ceb3cda` | `a08ec853a3a904b198c66667a8df8f85e5b3c60526d217878758d01b1ceb3cda` | `9a320803e86b35e3c0b8ab339714803e227a9da0c9529f2d453068928a2ed135` |
| `DSD-09` | `c46e94834202e37346cf031b9ed320c719d4e3b57e005a538cc055e0acff4653` | `c46e94834202e37346cf031b9ed320c719d4e3b57e005a538cc055e0acff4653` | `87af699d793adfda35cf2a74114e632893bd668cc66aa4c5c14018469da5481c` |
| `DSD-10` | `cc6f0089b32768684ac28d15d41ee73f786a46f15953d48ce8719ad5bd05e69c` | `cc6f0089b32768684ac28d15d41ee73f786a46f15953d48ce8719ad5bd05e69c` | `a4420e154601b7f6f53741165680cfafc4a9e6add569fbdd703537b1c9d3ff3e` |
| `DSD-11` | `10ddcdc963eae9cc10c5445acd61fe93d0618341141000cc76ee41f94c36fb52` | `10ddcdc963eae9cc10c5445acd61fe93d0618341141000cc76ee41f94c36fb52` | `eaa14d182248e0267bef934c3307a782a14836848b453a7690df1b4a11e615df` |

- Use these exact configuration groups:

| IDs | Fixture | Supplied context |
| --- | --- | --- |
| `DSD-01` | Canonical `project/dsd-01` files | Primary `dispatching-development-subagents`; the other eight project skills as `SKILL.md`-only dependencies |
| `DSD-02` | none | Primary dispatch skill; `disciplined-development` with `SKILL.md` and `hooks/review_nudge.py`; `disciplined-research`; installed `subagent-driven-development` |
| `DSD-03`, `DSD-04`, `DSD-07` | none | Primary dispatch skill only |
| `DSD-05`, `DSD-08` | Canonical `project/dsd-05` files | Primary dispatch skill only |
| `DSD-06` | Canonical `project/dsd-01` files | Primary dispatch skill only |
| `DSD-09`, `DSD-11` | none | Primary dispatch skill; `disciplined-development` with `SKILL.md` and `hooks/review_nudge.py`; installed `subagent-driven-development` |
| `DSD-10` | none | Primary dispatch skill; `disciplined-development` with `SKILL.md` and `hooks/review_nudge.py` |

- For the complete nine-skill group, declare dependencies in this order: `adversarial-review-loop`, `adversarial-review`, `concise-writing`, `disciplined-development`, `disciplined-research`, `lean-plan-writing`, `sweeping-stale-references`, `writing-explicit-rationale`. Include only each `SKILL.md`.
- Use `../../../../skills/dispatching-development-subagents` for the primary and `../../../../skills/<id>` for every project dependency. For `DSD-02`, declare dependencies in order: `disciplined-development`, `disciplined-research`, `subagent-driven-development`. For `DSD-09` and `DSD-11`, use `disciplined-development`, then `subagent-driven-development`; for `DSD-10`, use only `disciplined-development`. Include `SKILL.md` and `hooks/review_nudge.py` for `disciplined-development`; include only `SKILL.md` for every other dependency.
- Current project `SKILL.md` hashes are: `adversarial-review-loop` `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6`; `adversarial-review` `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c`; `concise-writing` `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`; `disciplined-development` `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`; `disciplined-research` `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`; `dispatching-development-subagents` `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500`; `lean-plan-writing` `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac`; `sweeping-stale-references` `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`; `writing-explicit-rationale` `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.
- The current `review_nudge.py` hash is `4c7fc6940939c0e7a148b339ac7862a0ad0980a8f8f153d0ab640dc8271363b0`. The installed `subagent-driven-development` source is `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/subagent-driven-development`, with `SKILL.md` hash `8dd1b8e698edec3700c6d89517dbe96febd3bacd3f6ea21c1a3569c62ea104b5`. If the installation moves before implementation, use the then-installed project copy and update only its recorded path/hash; stop if none is available.
- Canonical `project/dsd-01` fixture hashes are: `AGENTS.md` `567ded3276c9ecaabbfea7f34229a528652476cf2cfe1f7a81573b4577c866fe`; `plans/pagination.md` `e18ce80cae7233db26ed903116fee411162433d2ef82cfbcfa574835efcf35c4`; `reviews/pagination.md` `884e1ee1a6c7109134144ff3ab1cddf6bd9bd522a249373e4ce7e1571b77a80a`.
- Canonical `project/dsd-05` fixture hashes are: `landed-prose.md` `dc1c4a0881580f5a883d126ddcbc00b70dfd3e226129e44aa6ed06381fbc4aae`; `research-report.md` `0d7d31036a68767b0a586b7aad0c228999316c6463dfd39009f8d7e7131360d5`; `returned-handoff.md` `1c9f3979e4a123c584f3ddd072f6869df6a241adca1c4da4cc484b8f6815ecab`; `src/request_config.py` `f0ff7ba51f0b758aea2f9b248c754f832dd57c6d2110036a80f886690ecdee6c`; `test-output.txt` `dbff34df084976e0006cd15b2bd1cf6e3b5419b626c19f0030544a1c174ec3d7`.
- Execute in one isolated branch and worktree with task review and final review; include current checkbox state in each task commit.
- Invoke a provider only for one `DSD-03` smoke after all 11 packages pass mechanical preflight. The owner-facing controller performs the invocation using the owner's standing catalog-smoke approval; subagents must not invoke providers.
- Do not change runner code, providers, skills, canonical scenario content, validation methodology, testing methodology, or existing scenarios. Do not score behavior or commit raw provider output or temporary bundles.
- If any input is missing, ambiguous, hash-inconsistent, or unsupported by the current runner, stop for owner direction. Do not add runner code without separate approval.
- On completion, move this plan to `plans/completed/` and retain its Phase 3 roadmap link. Never delete it without explicit owner approval.

---

### Task 1: Package all 11 DSD scenarios

**Files:**

- Create `prompt.md` and `test.json` under `skill-validation/scenarios/dispatching-development-subagents/dsd-01/` through `dsd-11/`.
- Create the declared fixture files under each applicable package's `fixture/project/dsd-01/` or `fixture/project/dsd-05/` path.

**Produces:** Eleven loadable packages consumed by Task 2.

- [x] Materialize each adapted prompt, exact rubric, and applicable fixture files; verify every hash against the global manifests.
- [x] Create each `test.json` with matching lowercase IDs, the exact configuration group above, its exact rubric, its declared fixture or `null`, and the required execution settings.
- [x] Load all 11 without a provider. Prepare and remove disposable workspaces; require exactly the declared fixture and supplied files, the runner's ordinary subject transport followed by the adapted prompt, and no rubric bytes in subject input or workspace.
- [x] Run `uv run pytest -q` from `skill-validation/runner`, run `git diff --check`, update only Task 1 checkboxes, and commit.

### Task 2: Smoke-run DSD-03 end to end

**Files:**

- Modify this plan with Task 2 state and the dated run outcome.

**Consumes:** All 11 packaged scenarios.

**Produces:** One recorded real-provider smoke outcome consumed by Task 3.

- [ ] Run the full runner suite and mechanically preflight all 11 configurations without a provider. Confirm declared files and hashes, exact ordinary subject transport, and rubric isolation.
- [ ] Confirm the owner-facing transcript contains standing approval for catalog-migration smoke runs. Have the controller run `uv run skilltest run ../scenarios/dispatching-development-subagents/dsd-03/test.json` from `skill-validation/runner` exactly once, with an escalation description naming the read-only/no-network/no-agent `DSD-03` prompt, no fixture, supplied dispatch `SKILL.md`, and configured Codex provider. Do not delegate or run another DSD scenario.
- [ ] Validate `result.json` against `skill-validation/runner/result.schema.json`. Require `status: "COMPLETED"`, `infrastructure_error: null`, `invocation_started: true`, `timed_out: false`, provider exit `0`, required artifact records and paths, matching byte counts and hashes, and ordered invocation/return/configuration/completion events.
- [ ] Confirm retained inputs and workspace contain exactly the adapted prompt and supplied dispatch `SKILL.md`; confirm ordinary transport and rubric isolation. Do not inspect or compare semantic provider output.
- [ ] Append a dated outcome with run ID, bundle path, mechanical result, relevant hashes, and runner/packaging/provider fallout. If incomplete, commit only the plan outcome and stop without rerunning or starting Task 3.
- [ ] Run `git diff --check`, update only Task 2 state/outcome, and commit.

### Task 3: Reconcile and complete the catalog

**Files:**

- Modify `skill-validation/scenarios/README.md`.
- Modify `plans/2026-08-24-scenario-porting-roadmap.md`.
- Move this plan to `plans/completed/`.

**Consumes:** All 11 packages and the completed `DSD-03` smoke outcome.

**Produces:** Reconciled inventory, roadmap state, and archived plan.

- [ ] Mark all 11 scenarios ported. Update `dispatching-development-subagents` to 11 total / 11 ported / 0 not ported and overall totals to 105 total / 74 ported / 31 not ported.
- [ ] Confirm the full runner suite, 11-scenario preflight, and recorded `DSD-03` smoke are complete before changing inventory state.
- [ ] Add a Phase 3 roadmap link to the completed plan without selecting the next catalog.
- [ ] Move this plan to `plans/completed/`; repair its Spec links to `../specs/2026-08-25-catalog-migration-design.md`, `../2026-08-24-scenario-porting-roadmap.md`, and `../../skill-validation/charter/core-contracts.md`.
- [ ] Run the canonical local Markdown-link checker, `git diff --check`, and `git status --short`. Confirm no runner, provider, skill, methodology, raw-output, temporary-workspace, or existing-scenario change entered the work.
- [ ] Confirm every checkbox is complete, then commit only inventory, roadmap, and archived-plan bookkeeping.

## Done When

- [ ] All 11 active DSD scenarios have loadable schema `"0.1"` configurations with their declared context.
- [ ] Every package preserves canonical scenario-owned inputs with only the approved path substitutions.
- [ ] Exactly one `DSD-03` provider smoke completed; no other DSD scenario ran and no runner or skill code changed.
- [ ] Inventory, roadmap, and archived plan agree.
