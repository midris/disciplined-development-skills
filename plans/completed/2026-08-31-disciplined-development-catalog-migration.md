# Disciplined Development Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** Use `superpowers:verification-before-completion`
> before completion claims. Stop at the owner approval gate before merge or
> cleanup.

**Goal:** Package all nine active `disciplined-development` scenarios for the
schema `"0.2"` runner, prove that the runner can load and prepare every package,
and retain one completed representative smoke result.

**Architecture:** Each canonical scenario becomes one self-contained package.
Current repository skills remain live fixture sources, while canonical
scenario-owned files are copied byte-for-byte into each owning package. `DD-04`
is the sole representative smoke because it is the catalog's only two-live-skill
composition; the larger file sets are covered by package preparation.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](../specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](../2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../../skill-validation/scenarios/README.md).

## Global constraints

- Start from current `main` on branch
  `feature/disciplined-development-schema-02` in
  `.worktrees/disciplined-development-schema-02/`.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for scenario scope,
  prompt and rubric material, and scenario-owned file bytes.
- Package exactly `DD-01` through `DD-09` at
  `skill-validation/scenarios/disciplined-development/<lowercase-id>/`.
- Give each `test.json` exactly the schema `"0.2"` keys `schema_version`, `id`,
  `prompt`, `fixtures`, and `execution`; use its lowercase scenario ID and
  `"prompt":"prompt.md"`.
- Give every `test.json` the execution declaration
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"high"}`.
- Use current repository `SKILL.md` files directly as fixture sources. Do not
  copy them into packages or pin their hashes.
- Copy canonical scenario-owned files into every package that owns them and
  preserve their bytes exactly. Do not reconstruct, normalize, or share them
  between packages.
- Apply only the prompt substitutions listed below. Do not otherwise rewrite,
  clarify, reflow, or improve prompts or rubrics.
- Keep every scenario response-only. Do not use `{{evidence_dir}}`, request file
  changes, inspect response meaning, score a response, or validate result
  contents beyond the runner's mechanical status.
- Add only the catalog-local acceptance test named below. Do not change runner,
  provider, schema, skills, shared helpers, or other catalogs.
- The owner's standing approval covers the single Codex smoke invocation. Run
  only `DD-04`, once, with no retry.
- Skip external review. If the owner later requests one, use Claude rather than
  Codex.
- Stop if a canonical source is unavailable or hash-mismatched, an unlisted
  adaptation is required, the existing runner cannot represent a package, or
  the smoke does not finish with runner status `COMPLETED`.
- Do not merge or push implementation changes, archive this plan, remove the
  feature branch or worktree, or create the next catalog plan before new
  explicit owner approval.

## Catalog definition

### Candidate inventory

| ID | Purpose | Supplied context |
|---|---|---|
| `DD-01` | Select the due parent modes, gates, principles, artifacts, outcomes, blocked transitions, and owner seams across eight independent vignettes. | Live parent skill only |
| `DD-02` | Preserve Gate 1–5 timing and order, parent artifacts and destinations, fail-closed transitions, and owner boundaries through one fixed sequence. | Live parent plus the seven-file `DD-02` project set |
| `DD-03` | Apply Principle 7 only for contract, reachable accepted input, observed use, or robust invariants rather than speculative scale. | Live parent plus two parser-contract sources |
| `DD-04` | Ground a factual deployment premise before action, keep action blocked, and leave research procedure to the companion skill. | Live parent, live research companion, and deployment-target source |
| `DD-05` | Read governing sources, surface a plan/spec conflict, verify a recalled capability, and block planning and implementation. | Live parent plus the seven-file `DD-02` project set |
| `DD-06` | Require signed written scope to preserve a chosen spelling and an intentional deferral before delegation, planning, or coding. | Live parent plus the seven-file `DD-02` project set |
| `DD-07` | Keep delegation inside signed scope, require directly observed RED before production edits, and retain parent acceptance authority. | Live parent plus signed scope |
| `DD-08` | Dispose of unauthorized work before direct CLI evidence, reference reconciliation, truthful bookkeeping, and one coherent green commit. | Live parent plus signed scope and schema contract |
| `DD-09` | Require whole-tree review, scope resolution, refreshed evidence, clean review and smoke, and finishing before PR creation. | Live parent plus signed scope, plan, and history |

`DD-04` is the sole smoke representative. It is the only package that composes
two live skills, so it exercises the catalog's distinctive provider-input shape.
`DD-02`, `DD-05`, and `DD-06` contain more files, but the acceptance test loads
and prepares those complete packages offline.

### Canonical prompts and rubrics

Hashes are SHA-256 over complete file bytes, including the trailing LF. Prompt
and rubric paths below are relative to `skill-validation/` at the canonical
source commit.

| ID | Canonical prompt SHA-256 | Canonical rubric SHA-256 |
|---|---|---|
| `DD-01` | `b3ec84e300d5070ab14beb1786493abc2648d70c4b9b3e0a3a6ffdd416b6cf47` | `bb994c3b2e4adfc4feead9220ab9df89d53f5a74d1efa0e6bffbf733c7c0c9bb` |
| `DD-02` | `95deb13830eea682f06086c406dedb1a537b22f1bbf60598c4e1c231256ee706` | `801a1e8192a632c5aacee1ad63234af0987e73a498ad41dcba90610843181742` |
| `DD-03` | `e329586445f56ca213fc20557109c874b650219daf3860f079ce909b534c7f07` | `8daf6068c6546a1de19a77172513c7c6c74456df09193ed1b0722c46720e7cd4` |
| `DD-04` | `939a40cfe8fe27025ad8c83230830f000c8db0a67c440af0f42cf21925c9183f` | `275eb747335ff0f5d4b7933d43958332e33215db4a04dd8695c7e3e8327e8466` |
| `DD-05` | `250300e505f05a6e1b139a352f1887e5116ac90ef99c18ac4b1c6d0139458ee4` | `cc900e882777acac4bb63f516861fa230ebb2ca33581ed463985062c91c8bd8c` |
| `DD-06` | `0c296fd4f2a4245643e4ad17e746c06499e8ee920797721f654a6cf0aa74dda5` | `701ce6503df5e72fe2617b391caea8a66a19533f4c8054aa1f1d6bc7d064b1b2` |
| `DD-07` | `c79eb2bc14d0d9860a808c8875defc1f21bfaa7ec6a2ab356a08fe2c2cf88fd1` | `f8d47d834f1e29b5f3f61e3f1bb0e52cef7fea11d4fb20eef3626ca4a6d1889d` |
| `DD-08` | `fc5e306045d9a6ff3e49913320ea48cff6fada7eb637d9aa0e0463c52dd6ced9` | `7dfb9766ffb31271028c1a4c97b1199b5251ab32e0bae79b73881ed828ee7283` |
| `DD-09` | `d0d0234d9688666656862f6a874e7ca491bd9b0d32b16ea1cdaad083f229a67d` | `a2e99c0a3cab2e3968d3e300489e1f6de484239ff442db49b8aec8ad02b26d3c` |

For each ID, source `prompt.md` from
`fixtures/disciplined-development/prompts/<lowercase-id>.md` and `rubric.md`
from `fixtures/disciplined-development/rubrics/<lowercase-id>.md`. The active
catalog links those files. Its `DD-01` table metadata contains a stale prompt
hash; the linked file bytes and the hash above are authoritative, consistent
with the existing schema `"0.1"` provenance ruling. This resolves provenance
only and does not change the scenario.

Catalog acceptance does not audit rubric contents. Rubric hashes guide exact
materialization and review only.

### Prompt adaptations

Start from the canonical prompt bytes and make only these literal substitutions.
Preserve every other byte and the trailing LF.

| ID | Literal substitutions | Resulting `prompt.md` SHA-256 |
|---|---|---|
| `DD-01` | Replace `Invoke it directly, read it completely, and follow its applicable guidance as binding.` with `Read \`{{fixture_dir}}/skills/disciplined-development/SKILL.md\` completely and follow its applicable guidance as binding.` | `e13a4d90df7360f3a8b949e7b7b5208dc22f1a942294271f4de53898ff6bb0a2` |
| `DD-02` | Replace the two-line sentence `Invoke the parent directly, read it completely, and follow its` / `applicable guidance as binding.` with `Read \`{{fixture_dir}}/skills/disciplined-development/SKILL.md\` completely and follow its` / `applicable guidance as binding.`; replace every `project/dd-02/` with `{{fixture_dir}}/project/dd-02/`. | `5455c56e3fdfe2f390240680b2a7b52bb1f2f1af5fd027d3cc7a7b544081b45c` |
| `DD-03` | Replace `Read the parent completely and follow its applicable guidance as binding.` with `Read \`{{fixture_dir}}/skills/disciplined-development/SKILL.md\` completely and follow its applicable guidance as binding.`; replace every `project/dd-03/` with `{{fixture_dir}}/project/dd-03/`. | `8804abc9cd643a9e54e96c0409d01cda4243ee2226f3abbdcc25ae62d1866680` |
| `DD-04` | Replace `Read both skills and \`project/dd-04/sources/deployment-targets.md\` completely and follow their applicable guidance as binding.` with `Read \`{{fixture_dir}}/skills/disciplined-development/SKILL.md\`, \`{{fixture_dir}}/skills/disciplined-research/SKILL.md\`, and \`{{fixture_dir}}/project/dd-04/sources/deployment-targets.md\` completely and follow their applicable guidance as binding.` | `a5e789ac85f39038eb089fbc123221157e2f888807c37a747b23df7bd8140720` |
| `DD-05` | Apply the `DD-02` skill-read substitution; replace every `project/dd-02/` with `{{fixture_dir}}/project/dd-02/`. | `892267b05ac96d381ff18f072073c9d73aeb9ce1966cc9dc0c9a0cbb0058d5e7` |
| `DD-06` | Replace the two-line sentence `Invoke \`disciplined-development\`, read it completely, and follow its applicable` / `parent guidance as binding.` with `Read \`{{fixture_dir}}/skills/disciplined-development/SKILL.md\` completely and follow its applicable` / `parent guidance as binding.`; replace the literal backticked path `project/dd-02` with `{{fixture_dir}}/project/dd-02`. | `1f49a903af98ab130aba3b8a189cb1dd08d586e0376e0f08ab6e11a0d811f004` |
| `DD-07` | Apply the `DD-06` skill-read substitution; replace the literal backticked path `project/dd-07/signed-scope.md` with `{{fixture_dir}}/project/dd-07/signed-scope.md`. | `44701c450532a737cb3ff197a7ee80bb81bc98c4e4c43278b6631f84add989fd` |
| `DD-08` | Apply the `DD-06` skill-read substitution; replace the literal backticked path `project/dd-08` with `{{fixture_dir}}/project/dd-08`. | `69b7fa3d7a2c3793d5e3563396813cef8f7dd6f951c066c17bfb743a5c12e2af` |
| `DD-09` | Apply the `DD-06` skill-read substitution; replace the literal backticked path `project/dd-09` with `{{fixture_dir}}/project/dd-09`. | `919f41e20c38e7b971480b16b50ca134db41e1f807890076514f9fabb58156ac` |

These substitutions expose already-supplied inputs at schema `"0.2"` paths.
They do not add instructions, requirements, artifacts, or evaluation behavior.

### Live skill fixture mappings

Declare every skill file separately. Use source
`../../../../skills/<skill-id>/SKILL.md` and target
`skills/<skill-id>/SKILL.md`.

| IDs | Live skills |
|---|---|
| `DD-01`, `DD-02`, `DD-03`, `DD-05`, `DD-06`, `DD-07`, `DD-08`, `DD-09` | `disciplined-development` |
| `DD-04` | `disciplined-development`; `disciplined-research` |

### Scenario-owned fixture mappings

Canonical paths are relative to
`skill-validation/fixtures/disciplined-development/` at the canonical commit.
Package sources and targets are literal configuration values relative to each
owning package. `DD-02`, `DD-05`, and `DD-06` each receive their own copy of all
seven `DD-02` rows. Do not include `project/dd-02/sources/operator-note.md`.

| Owners | Canonical path | Package source | Fixture target | SHA-256 |
|---|---|---|---|---|
| `DD-02`, `DD-05`, `DD-06` | `project/dd-02/CLAUDE.md` | `fixture/project/dd-02/CLAUDE.md` | `project/dd-02/CLAUDE.md` | `cc1f87826147c2799de88f208edbb798b24d6beb955bbadd5295e04fa1514d69` |
| `DD-02`, `DD-05`, `DD-06` | `project/dd-02/plans/export.md` | `fixture/project/dd-02/plans/export.md` | `project/dd-02/plans/export.md` | `fd6dec456856f4aeb78cd4926a40ddf26c2f86da836e9559e91bff8f4b5d7daa` |
| `DD-02`, `DD-05`, `DD-06` | `project/dd-02/plans/specs/export.md` | `fixture/project/dd-02/plans/specs/export.md` | `project/dd-02/plans/specs/export.md` | `77a8ad0cfa3ea65b02047968f412712d2b7723e4b943277ffdecfa3fd7ba735e` |
| `DD-02`, `DD-05`, `DD-06` | `project/dd-02/sources/cli-schema.md` | `fixture/project/dd-02/sources/cli-schema.md` | `project/dd-02/sources/cli-schema.md` | `d31a0cf950c631454c0c3bb4e3a732e7e360776f7157cd81aa0921f8be3f42fd` |
| `DD-02`, `DD-05`, `DD-06` | `project/dd-02/sources/git-history.md` | `fixture/project/dd-02/sources/git-history.md` | `project/dd-02/sources/git-history.md` | `a870dab35c878752f1b8c38538c08769df1ec21a2575fea0e723e484b7fd42bf` |
| `DD-02`, `DD-05`, `DD-06` | `project/dd-02/sources/library-api.md` | `fixture/project/dd-02/sources/library-api.md` | `project/dd-02/sources/library-api.md` | `253fb27d2587dd1ae1da9c6ff96c27a3c6c5c622301c661dc2e2a82a4452e1a4` |
| `DD-02`, `DD-05`, `DD-06` | `project/dd-02/sources/vendor-schema-status.md` | `fixture/project/dd-02/sources/vendor-schema-status.md` | `project/dd-02/sources/vendor-schema-status.md` | `e696074e7b3c344a9e61601013af88036620ad981744cebc8acecca3964dffe5` |
| `DD-03` | `project/dd-03/sources/accepted-object-contract.md` | `fixture/project/dd-03/sources/accepted-object-contract.md` | `project/dd-03/sources/accepted-object-contract.md` | `a7dd65af335e4d25626a543e42d61e78761155906b3cc42ef2c362cf81d8bdb5` |
| `DD-03` | `project/dd-03/sources/parser-capabilities.md` | `fixture/project/dd-03/sources/parser-capabilities.md` | `project/dd-03/sources/parser-capabilities.md` | `717b21cb61d87637ca241791407d9c57594e29c122cd0ef6c35e3476b5c1bee1` |
| `DD-04` | `project/dd-04/sources/deployment-targets.md` | `fixture/project/dd-04/sources/deployment-targets.md` | `project/dd-04/sources/deployment-targets.md` | `90e874878dd0380aca4517b53eedb1f58436f6f3500fb2397517716aa15b986d` |
| `DD-07` | `project/dd-07/signed-scope.md` | `fixture/project/dd-07/signed-scope.md` | `project/dd-07/signed-scope.md` | `c9004c24d44bc4284fef9541ea3ff7912790227f288ac0c722a41df5a868cb25` |
| `DD-08` | `project/dd-08/cli-schema.md` | `fixture/project/dd-08/cli-schema.md` | `project/dd-08/cli-schema.md` | `dbfbe479f69212a39d1dc671aca5213fa6aa4e605fb769b1a1391b5d5abc5d05` |
| `DD-08` | `project/dd-08/signed-scope.md` | `fixture/project/dd-08/signed-scope.md` | `project/dd-08/signed-scope.md` | `8840eda21e4a8d4ec4771b1d46c7652c36729065075f9f971153d70a83e0a974` |
| `DD-09` | `project/dd-09/active-plan.md` | `fixture/project/dd-09/active-plan.md` | `project/dd-09/active-plan.md` | `c09b6c4727776e8871af3ac358656dba48b60566899b883527728cc35761199f` |
| `DD-09` | `project/dd-09/git-history.md` | `fixture/project/dd-09/git-history.md` | `project/dd-09/git-history.md` | `9a29b8528528d47840e0525cc96b4a8e7639875896543efd97ccb35fef03fdff` |
| `DD-09` | `project/dd-09/signed-change-scope.md` | `fixture/project/dd-09/signed-change-scope.md` | `project/dd-09/signed-change-scope.md` | `071f0d9c1d5778f63c475a8c3a7299f5124f92386e648e9f293cf0209f2323ed` |

`DD-01` has no scenario-owned fixture. Empty scenario-owned input is supported;
its live parent skill remains its sole declared fixture.

### Package records

Each package contains exactly `README.md`, `prompt.md`, `rubric.md`, `test.json`,
and its declared `fixture/` files. Before the smoke, no package contains a
result. Each README records only the scenario purpose, input/provenance mapping,
and smoke status. After a successful smoke, only `DD-04` links the exact retained
result and states the runner's mechanical status. Do not make a behavioral claim
or duplicate result contents.

## Catalog acceptance

Create
`skill-validation/runner/acceptance/test_disciplined_development_catalog.py`.
Keep catalog data and any small local helpers in that file. It verifies only:

- exactly the nine planned scenario directories and their exact package files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- prompt bytes against the adapted hashes above;
- literal fixture source and target mappings against this plan;
- packaged scenario-owned file bytes against the hashes above;
- resolved prompt tokens and no stale `supplied-skills/` path;
- absence of rubric bytes from declared and prepared provider inputs; and
- an empty initial evidence directory.

Permit only `DD-04` to add optional `smoke-result.json` after acceptance is
established. Redirect the runner's temporary root to pytest's `tmp_path` so
preparation leaves no run bundle outside the test directory.

Acceptance does not invoke a provider or validate README prose, rubric content,
execution choices, smoke results, response or result schemas, or provider
artifacts. It does not reconstruct a result or add shared machinery. Those are
accepted, unexamined edges outside this migration.

## Verification

After package acceptance is implemented, run from `skill-validation/runner`:

```bash
uv run pytest -q acceptance/test_disciplined_development_catalog.py
uv run pytest -q
```

After the smoke record and any index update, rerun only the focused acceptance
test because those changes do not alter package preparation. If review repairs
a package or acceptance behavior, rerun both commands; otherwise rerun only the
affected check. Do not add another verifier or run unrelated skill test suites.

## Task 1: Package `DD-01` through `DD-09`

**Files:** Create all nine scenario packages and their declared fixture files.

**Boundary:** Stop on a missing source, hash mismatch, malformed configuration,
or required adaptation outside this plan.

- Materialize canonical prompts, rubrics, and owned fixtures; apply only the
  declared prompt substitutions.
- Create the exact schema `"0.2"` configurations and minimal package READMEs.
- Exclude `operator-note.md` from all three copies of the `DD-02` set.

## Task 2: Add catalog acceptance and verify preparation

**Files:** Create
`skill-validation/runner/acceptance/test_disciplined_development_catalog.py`.

**Boundary:** Provider behavior and result content remain accepted, unexamined
edges. Do not add output checks, mutations, negative-test matrices, or shared
helpers.

- Implement exactly the catalog-local acceptance contract above.
- Run the focused acceptance and the complete offline runner suite once.
- Review the test against the package-only boundary.

## Task 3: Run and record the representative smoke

**Files:** Create
`skill-validation/scenarios/disciplined-development/dd-04/smoke-result.json`
only if the runner publishes `result.json`. Modify the `DD-04` README, the
scenario migration index only after `COMPLETED`.

**Boundary:** Missing output or any status other than `COMPLETED` stops the
catalog without retry. Response meaning, rubric satisfaction, stdout/stderr,
artifact inventories, and result reconstruction remain unexamined.

- From `skill-validation/runner`, invoke exactly once:
  `uv run skilltest run ../scenarios/disciplined-development/dd-04/test.json`.
  Do not retry or run another scenario.
- If the runner publishes `result.json`, replace any prior
  `dd-04/smoke-result.json` with its exact bytes. If it publishes no result,
  remove any prior retained result.
- Record the runner's mechanical outcome in the `DD-04` README and remove the
  owned temporary run directory in every outcome. Retain no other run artifact.
- If the retained result's runner status is `COMPLETED`, update the migration
  index, link all nine READMEs, identify `DD-04` as representative, and update
  totals to 9/9 and 35/105 overall.
- If no result is retained or status is not `COMPLETED`, do not update the
  index; rerun focused acceptance and stop for owner direction.
- For `COMPLETED`, rerun focused acceptance and review the records.

## Controller review and approval gate

The controller performs this review directly and does not dispatch an external
review unless the owner requests one.

- Review the whole catalog against the governing design and this plan.
  Confirm the final diff is limited to the nine packages, their catalog-local
  acceptance test, and the migration index.
- Address only verified in-scope findings and rerun only checks affected by
  repairs.
- Report the implementation commits, focused and full offline verification,
  smoke attempt and retained result status, and internal-review disposition.
- Stop and obtain explicit owner approval before merge, push, plan archive,
  roadmap update, feature worktree/branch removal, or next-catalog planning.

## Post-approval closeout

- Merge the feature branch into local `main`.
- On `main`, check the `disciplined-development` roadmap item and move this
  plan to `plans/completed/`, adjusting its three header links for the new
  location, then commit the closeout.
- Push `main`, then remove this catalog's worktree and local feature branch.
  Do not create the next catalog plan without separate owner approval.

## Done when

- All nine packages pass catalog acceptance and the complete offline runner
  suite.
- One approved `DD-04` invocation retains the exact runner-produced
  `COMPLETED` result.
- The migration index reports 9/9 for this catalog and 35/105 overall.
- Internal review passes without output or result judgment.
- After owner approval, the catalog is merged and pushed, the roadmap and
  plan are closed, and the feature worktree and branch are removed.
