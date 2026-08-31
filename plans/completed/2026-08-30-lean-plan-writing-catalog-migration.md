# Lean Plan Writing Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` to implement Tasks 1–4 task by task.
> After Task 4, leave the subagent-driven task loop and perform the controller
> closeout directly; do not dispatch that section as a task.
> Use `superpowers:verification-before-completion` before completion claims.
> Track progress with the checkboxes below.

**Goal:** Package all seven active `lean-plan-writing` scenarios for the schema
`"0.2"` runner, retain one completed representative smoke result, and finish
this catalog before planning the next one.

**Architecture:** Each canonical scenario becomes one self-contained package.
Current repository skills remain live fixture sources, while the required
Superpowers 6.3.0 `writing-plans` dependency and canonical scenario files are
copied into every package that uses them. `LP-01` is the sole representative
because it exercises the complete local skill bundle, the pinned external
dependency, and a scenario-owned file through one response-only run.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](../specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](../2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../../skill-validation/scenarios/README.md).

## Global constraints

- Implement on branch `feature/lean-plan-writing-schema-02` in
  `.worktrees/lean-plan-writing-schema-02/`.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for candidate scope,
  scenario meaning, prompt material, scenario-owned bytes, and rubrics.
- Package exactly `LP-01`, `LP-02`, `LP-03`, `LP-05`, `LP-06`, `LP-07`, and
  `LP-08`. `LP-04` is retired and remains excluded.
- Put each package at
  `skill-validation/scenarios/lean-plan-writing/<lowercase-id>/`.
- Give each default configuration the execution declaration
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"high"}`.
- Use current repository `SKILL.md` files directly as fixture sources. Do not
  copy them into scenario packages or pin their hashes.
- Copy Superpowers 6.3.0
  `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans/SKILL.md`
  separately into every package. The duplication is the accepted cost of
  keeping each package self-contained; do not introduce shared dependency
  storage or an absolute runtime source.
- Copy each canonical scenario-owned file only into its owning package and
  preserve its bytes exactly.
- Apply only the prompt substitutions listed below. Do not otherwise rewrite,
  normalize, reflow, clarify, or improve canonical prompts or rubrics.
- Keep every scenario response-only. Do not use `{{evidence_dir}}`, request file
  changes, add evaluator behavior, score responses, or inspect response meaning.
- Add only the catalog-local acceptance test named below. Do not change runner,
  provider, schema, skill, shared helper, or other catalog files.
- The owner's 2026-08-30 standing approval covers necessary Codex invocations
  for future test-scenario migrations. Run only `LP-01`, once, with no retry.
- Do not merge, push, archive this plan, or remove the feature branch or
  worktree without explicit owner approval. Do not create the next catalog plan
  before this catalog is merged and this plan is archived.
- Stop under the design's fail-closed conditions. In particular, stop if a
  canonical or pinned source is unavailable or differs, an unlisted prompt
  adaptation is needed, the runner cannot represent a scenario, or the smoke
  does not finish with runner status `COMPLETED`.
- Treat the whole catalog as one merge boundary: one feature branch and one
  final merge. Per-scenario branches would leave catalog acceptance and index
  state incomplete without making any package independently more useful.

## Catalog decisions

### Candidate inventory and representative

| ID | Purpose | Default supplied context |
|---|---|---|
| `LP-01` | Preserve the upstream plan scaffold, TDD order, concrete files, rigor, and commit cadence while applying lean prose density. | Complete current nine-skill repository bundle, pinned `writing-plans`, and the canonical JSON CLI brief |
| `LP-02` | Keep implementation bodies and copyable templates out of a detailed parser task while preserving exact behavior through a complete tricky-case table. | Current `lean-plan-writing`, pinned `writing-plans`, and fixed parser semantics inline |
| `LP-03` | Permit exactly one bounded illustrative snippet when prose alone cannot specify an exact four-line artifact. | Current `lean-plan-writing`, pinned `writing-plans`, and the artifact contract inline |
| `LP-05` | Name and disposition absent, malformed, out-of-scale, uniqueness, atomicity, and actionable-error cases without embedding implementation bodies. | Current `lean-plan-writing`, pinned `writing-plans`, and the canonical membership-import brief |
| `LP-06` | Name and disposition quiet failure, scale, overlap, idempotency, quota, isolation, and timezone cases. | Current `lean-plan-writing`, pinned `writing-plans`, and the canonical nightly-digest brief |
| `LP-07` | Split oversized independently deployable work at qualitative review boundaries while preserving dependency order. | Current `lean-plan-writing`, pinned `writing-plans`, and the canonical oversized-program brief |
| `LP-08` | Keep a small genuinely coupled rename in one atomic branch and merge. | Current `lean-plan-writing`, pinned `writing-plans`, and the canonical coupled-rename brief |

`LP-01` is the sole representative because it composes the catalog's broadest
runner input: nine live repository skills, one pinned external dependency, and
one scenario-owned file. The older schema `"0.1"` `LP-05` smoke covered a
narrower two-skill package; retaining it as representative would not exercise
the complete schema `"0.2"` catalog shape.

### Canonical prompt and rubric provenance

Hashes are SHA-256 over complete file bytes, including one trailing LF. Every
prompt is the fenced evaluator input beneath the named heading in canonical
`skill-validation/lean-plan-writing.md`. Every rubric is the active catalog
table's evaluator-withheld rubric cell plus one trailing LF.

| ID | Canonical prompt heading | Prompt SHA-256 | Rubric SHA-256 |
|---|---|---|---|
| `LP-01` | `LP-01 — full-bundle JSON report plan` | `d0d2daf8c9da4bb8d417bb064c5fc50a30cc756dcc287c15540d0c19ffed25f5` | `6f9e42155d26e1a779d54c7987893207847ed18cfa34981d07dc5bd19a3c0585` |
| `LP-02` | `LP-02 — parser table without implementation` | `bc17742401c5d9fe6ed0e55d9e63bdaabd544a67d0925ff563c234b1a865c2f1` | `25c652e447ebf6b792ab85e2e6bafc684e908ecc6e2e55e457a89dc216d2fa4a` |
| `LP-03` | `LP-03 — necessary four-line artifact shape` | `6dc439c916aea496915f3e92163653f0eebf8526bd68ecd41c5c84ebc43d39ae` | `8e9f86e8532792799aeb94c0ad258f61f0692618dc07436f79c43017469714af` |
| `LP-05` | `LP-05 — loud CSV edge inventory` | `297d0f357f7ed7d2fff44c15d4b7e8fffebb8a7b91b58cfea09e2c7651feb1f8` | `237f61c94a6e3ec5be12afe4e8d5a2d78482651a43c217ab65c5aa9ea9bf27ac` |
| `LP-06` | `LP-06 — quiet digest edge inventory` | `a86f494b79defb37f6685312043ea7110c719f185fad0544079c974e97625d05` | `51bd263fe590b21e84c46cbbaa237866755b89081fa6c75e60beac79aeb58474` |
| `LP-07` | `LP-07 — oversized program boundary` | `737bf8052c76033b74010eb4516b904f42f9cc894d62503a1c630363cb593c9b` | `5f1c9773e6e9f13de86dffea04d4cbc22dd01a9390e7403ff6f24461d1548894` |
| `LP-08` | `LP-08 — coupled change boundary` | `ab34f34a06d4961d5dc6f1b52175f39517342c9cf9908a796f4afb01d81b18f5` | `698bfc496f0da6f1f3d78510f785f0d81b75c55176db97f29b307fbabfd25648` |

Materialize each rubric as `rubric.md`. These hashes guide authoring and
provenance; catalog acceptance does not audit rubric contents.

### Prompt adaptations

Start from the canonical prompt bytes and make only the substitutions below.
Preserve all other bytes and the trailing LF.

For every scenario, replace each `skills/` prefix in a canonical skill path
with `{{fixture_dir}}/skills/`. Apply these additional substitutions:

| ID | Additional literal substitutions | Resulting `prompt.md` SHA-256 |
|---|---|---|
| `LP-01` | Replace `The complete nine-skill local bundle and external \`superpowers:writing-plans\` are installed.` with `The complete nine-skill local bundle and external \`superpowers:writing-plans\` are supplied beneath \`{{fixture_dir}}/skills\`.`; replace `context/task.md` with `{{fixture_dir}}/context/task.md`. | `88b82609319594001c6c5737eacef0114930012169b656e4647cb6bb719bfc2d` |
| `LP-02` | None. | `52dc170f02d4d055456982381adba708b7be011ca7896da2a9ebf2a75b8356a3` |
| `LP-03` | None. | `41a94175c01f78325bce620c6a30ee6f600ed8a8ebd6fce051710cdafc2e00e9` |
| `LP-05` | Replace `context/import-brief.md` with `{{fixture_dir}}/context/import-brief.md`. | `914f8831a62da2c3811895ce0f426c02e7307edc8440e35154dd51768d20417b` |
| `LP-06` | Replace `context/digest-brief.md` with `{{fixture_dir}}/context/digest-brief.md`. | `e00cf13f429928a48129058a7391e4c5adeb07bce24c494047157e3b2d855902` |
| `LP-07` | Replace `context/oversized-spec.md` with `{{fixture_dir}}/context/oversized-spec.md`. | `4e825ffbe57cb7bb3352bfccbcbe6ba399c2ae37977bc73978da8596bbd1839c` |
| `LP-08` | Replace `context/coupled-spec.md` with `{{fixture_dir}}/context/coupled-spec.md`. | `0eb903aeb088ebacb45dd1d90e6c2364c949a60f6c337f3c8ca35a017f1d6e12` |

These substitutions expose supplied files through schema `"0.2"` paths without
changing the task or requested output. Do not add a wrapper or reorganize any
prompt.

### Live skill fixtures

For each live skill, use source `../../../../skills/<skill-id>/SKILL.md` and
target `skills/<skill-id>/SKILL.md`. Declare every used file separately.

| ID | Live skills |
|---|---|
| `LP-01` | `adversarial-review-loop`; `adversarial-review`; `concise-writing`; `disciplined-development`; `disciplined-research`; `dispatching-development-subagents`; `lean-plan-writing`; `sweeping-stale-references`; `writing-explicit-rationale` |
| `LP-02`, `LP-03`, `LP-05`, `LP-06`, `LP-07`, `LP-08` | `lean-plan-writing` |

### Packaged files

| IDs | Provenance | Package source | Fixture target | SHA-256 |
|---|---|---|---|---|
| All seven active IDs | Superpowers 6.3.0 `writing-plans/SKILL.md` at the absolute source named in Global constraints | `fixture/skills/writing-plans/SKILL.md` | `skills/writing-plans/SKILL.md` | `48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2` |
| `LP-01` | Canonical fenced `LP-01 fixture` at the source commit | `fixture/context/task.md` | `context/task.md` | `c1de457ec9789a1345c72d3bf638486f5362d582bbb9917949eef8e00de5cabd` |
| `LP-05` | Canonical repaired fenced `LP-05 fixture` at the source commit | `fixture/context/import-brief.md` | `context/import-brief.md` | `8789920dd0f54b1804e2a0aab65adfbcc728d525598d1d30a1d13b28c901c128` |
| `LP-06` | Canonical fenced `LP-06 fixture` at the source commit | `fixture/context/digest-brief.md` | `context/digest-brief.md` | `4df040c40f8888fb406265b3643e1c51e1eeaa91ad469d859dec0fd6f92dc792` |
| `LP-07` | Canonical fenced `LP-07 fixture` at the source commit | `fixture/context/oversized-spec.md` | `context/oversized-spec.md` | `e2a2a54472f37e5ad830ec1016f66fe3b280463c5c400a84697b508d22713685` |
| `LP-08` | Canonical fenced `LP-08 fixture` at the source commit | `fixture/context/coupled-spec.md` | `context/coupled-spec.md` | `05734fbdd024ff4db8404e46b995688ce30da1bacc9efc82b4bbbb5cd5a93ca1` |

The `writing-plans` row requires a separate identical copy beneath every active
package. `LP-02` and `LP-03` have no scenario-owned file because their fixed
inputs remain inline in their canonical prompts.

Superpowers 6.3.0 is the current locally available `writing-plans` dependency
and is selected as the migration's tester-chosen default input. The canonical
scenario does not make its dependency version part of scenario identity.

### Default configurations

Every `test.json` uses schema `"0.2"`, its lowercase scenario ID,
`"prompt":"prompt.md"`, the execution declaration in Global constraints, and
these fixture mappings:

| ID | Fixture mappings |
|---|---|
| `lp-01` | Nine live repository skills; packaged `writing-plans`; packaged `task.md` |
| `lp-02` | Live `lean-plan-writing`; packaged `writing-plans` |
| `lp-03` | Live `lean-plan-writing`; packaged `writing-plans` |
| `lp-05` | Live `lean-plan-writing`; packaged `writing-plans`; packaged `import-brief.md` |
| `lp-06` | Live `lean-plan-writing`; packaged `writing-plans`; packaged `digest-brief.md` |
| `lp-07` | Live `lean-plan-writing`; packaged `writing-plans`; packaged `oversized-spec.md` |
| `lp-08` | Live `lean-plan-writing`; packaged `writing-plans`; packaged `coupled-spec.md` |

### README content

Each scenario README contains only `Purpose`, `Inputs`, and `Smoke` sections.
Use the candidate table for Purpose. Inputs compactly records prompt provenance
and adaptation, rubric provenance, every live skill source and provider target,
the pinned `writing-plans` source and provider target, and any scenario-owned
file's source and provider target. Smoke initially states that no schema `"0.2"`
result is retained. After the representative run, only `LP-01` links the
retained result and states the runner's mechanical status. Do not duplicate the
configuration or make a behavioral claim.

## Catalog acceptance

Create
`skill-validation/runner/acceptance/test_lean_plan_writing_catalog.py`. Keep all
catalog data and small helpers in that file. It verifies only:

- exactly the seven planned scenario directories and their required package
  files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- prompt bytes against the adapted prompt hashes above;
- fixture source and target mappings against this plan;
- packaged `writing-plans` and canonical scenario-file bytes against the hashes
  above;
- resolved prompt tokens and absence of stale `supplied-skills/` paths;
- absence of rubric bytes from declared and prepared provider inputs; and
- an empty initial evidence directory.

Permit only `LP-01` to add an optional `smoke-result.json` after acceptance is
first established. Redirect the runner's temporary root to pytest's `tmp_path`,
following the existing catalog acceptance pattern, so preparation leaves no run
bundle outside the test's temporary directory.

Acceptance does not invoke a provider, validate README prose or rubric contents,
compare the configuration's ID, prompt, provider, model, or effort to this plan,
inspect smoke results, validate provider output, or add shared machinery. Those
omissions preserve the design's package-only boundary.

## Verification

Catalog verification consists of these existing checks:

- From `skill-validation/runner`, run
  `uv run pytest -q acceptance/test_lean_plan_writing_catalog.py`.
- From `skill-validation/runner`, run `uv run pytest -q`.
- From the repository root, run
  `cd skills/disciplined-development/hooks && python3 -m pytest -q`.
- Run the repository's existing local Markdown-link check documented under
  `Verification commands` in
  `13599fb7d3127334b0d07bfe468767e586ec5f9c:skill-validation/README.md`.
- Run `git diff --check`.

Do not add another verifier. Run the focused acceptance and full offline runner
suite after Task 3. Run the full catalog verification after Task 4 and again
during controller closeout, rerunning affected checks after verified review
repairs.

## Task 1: Package representative `LP-01`

**Files:**

- Create `README.md`, `prompt.md`, `rubric.md`, and `test.json` beneath
  `skill-validation/scenarios/lean-plan-writing/lp-01/`.
- Create `fixture/skills/writing-plans/SKILL.md` and
  `fixture/context/task.md` beneath that package.
- Modify this plan only to mark completed steps.

**Boundary:** Stop if any canonical or pinned source is missing or hash-mismatched,
or if configuration loading requires an unlisted adaptation. Package size is
bounded by the declared files; no other input is accepted.

- [x] Create the self-contained package from the catalog decisions above.
- [x] Confirm the prompt and packaged files have their planned hashes and the
  configuration loads with the runner.
- [x] Review the package files against their sources and commit the task changes.

## Task 2: Package `LP-02`, `LP-03`, `LP-05`, `LP-06`, `LP-07`, and `LP-08`

**Files:**

- Create `README.md`, `prompt.md`, `rubric.md`, and `test.json` beneath each
  remaining active scenario package.
- Create a separate `fixture/skills/writing-plans/SKILL.md` beneath every
  package.
- Create the four listed canonical context files beneath their owning packages.
- Modify this plan only to mark completed steps.

**Boundary:** `LP-02` and `LP-03` accept no scenario-owned file. The other four
accept exactly one canonical context file. Stop on a missing source, hash
mismatch, malformed configuration, or required adaptation outside this plan.

- [x] Create all six self-contained packages from the catalog decisions above.
- [x] Confirm the prompts and packaged files have their planned hashes and each
  configuration loads with the runner.
- [x] Review the package files against their sources and commit the task changes.

## Task 3: Add catalog acceptance and verify preparation

**Files:**

- Create
  `skill-validation/runner/acceptance/test_lean_plan_writing_catalog.py`.
- Modify this plan only to mark completed steps.

**Boundary:** Invalid or undeclared package inputs fail acceptance through the
existing loader/preparation path. Provider behavior and result content are
outside this test and remain accepted, unexamined edges.

- [x] Implement the final seven-scenario acceptance contract above using only
  catalog-local data and helpers.
- [x] Run the focused acceptance and complete offline runner suite.
- [x] Review the test for exact agreement with the spec's package-only boundary
  and commit the task changes.

## Task 4: Run and record the representative smoke

**Files:**

- Create
  `skill-validation/scenarios/lean-plan-writing/lp-01/smoke-result.json` only if
  the runner publishes `result.json`.
- Modify `skill-validation/scenarios/lean-plan-writing/lp-01/README.md`.
- Modify `skill-validation/scenarios/README.md` only after a `COMPLETED` result.
- Modify this plan only to mark completed steps.

**Boundary:** A missing result or any runner status other than `COMPLETED` is
recorded mechanically and stops the catalog without a retry. Response meaning,
rubric satisfaction, provider stdout/stderr, result artifact inventories, and
result-file reconstruction are outside this migration and remain unexamined.

- [x] Under the owner's standing approval, run exactly
  `uv run skilltest run ../scenarios/lean-plan-writing/lp-01/test.json` once from
  `skill-validation/runner`. Do not retry or run another scenario.
- [x] If the runner publishes `result.json`, copy its exact bytes to
  `lp-01/smoke-result.json`; otherwise remove any prior retained result.
- [x] Record only the runner status and result link, when present, in the
  `LP-01` README; remove the temporary run bundle and retain no other run
  artifact.
- [ ] If no result is retained or its status is not `COMPLETED`, run catalog
  verification, review and commit the smoke disposition, README, and plan
  tracking, then stop and request owner direction. Do not update the migration
  index.
- [x] For a `COMPLETED` result, add the catalog to the migration index, link all
  seven READMEs, identify `LP-01` as representative, and update totals to 7/7
  for this catalog and 19/105 overall.
- [x] Run catalog verification, review the smoke documentation and index update,
  and commit the task changes.

## Controller closeout: Final review, merge, and catalog bookkeeping

**Files:**

- Modify `plans/2026-08-24-scenario-porting-roadmap.md` after merge.
- Move this plan to
  `plans/completed/2026-08-30-lean-plan-writing-catalog-migration.md` after
  merge.

**Ownership:** This section is outside the subagent-driven task loop. The
controller performs it directly under the repository's Gate 5 and branch-finishing
rules.

**Boundary:** A merge conflict, verification failure, or rejected push stops
completion with the feature worktree and branch preserved. Only the named
roadmap, plan, index, acceptance, and package paths belong to this catalog.

- [x] Run catalog verification and complete a whole-catalog review against the
  governing design and this plan. Address verified findings and rerun affected
  checks.
- [x] Confirm the final diff is limited to this catalog's packages, its local
  acceptance test, migration index, and plan tracking.
- [x] Present the commits, verification results, retained smoke result, review
  disposition, and cleanup targets to the owner. Obtain explicit approval before
  merging, pushing, archiving this plan, or removing the feature branch or
  worktree.
- [x] After approval, merge the feature branch into local `main`.
- [x] On `main`, check the `lean-plan-writing` roadmap item and move this plan to
  `plans/completed/`. Change its three header links to
  `../specs/2026-08-29-catalog-migration-design.md`,
  `../2026-08-24-scenario-porting-roadmap.md`, and
  `../../skill-validation/scenarios/README.md`; run the Markdown link check and
  `git diff --check`, then commit those bookkeeping changes.
- [ ] Run catalog verification on `main`, push `main`, then remove this catalog's
  worktree and local feature branch. Do not create the next catalog plan in this
  task.

## Done when

- [x] All seven packages pass the catalog acceptance test and offline runner
  suite.
- [x] `LP-01` retains the latest runner-produced `COMPLETED`
  `smoke-result.json` from one approved attempt.
- [x] The migration index reports 7/7 for this catalog and 19/105 overall.
- [x] Final review and repository verification pass.
- [ ] With owner approval, the catalog is merged and pushed, the roadmap is
  checked, the plan is archived, and the worktree and feature branch are removed.
