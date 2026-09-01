# Skill Discovery Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** Use `superpowers:verification-before-completion`
> before completion claims. Stop at the owner approval gate before merge or
> cleanup.

**Goal:** Package all twelve active `skill-discovery` scenarios for the schema
`"0.2"` runner, prove that the runner can load and prepare every package, and
retain one completed representative smoke result.

**Architecture:** Each canonical target prompt becomes one self-contained,
prompt-only package with its evaluator-withheld rubric and an empty fixture
declaration. `DISC-12` is the sole representative smoke because it exercises
the catalog's non-development response/interaction boundary; offline acceptance
prepares all twelve packages, which otherwise share the same no-fixture runner
shape.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../skill-validation/scenarios/README.md).

## Global constraints

- Start from current `main` on branch `feature/skill-discovery-schema-02` in
  `.worktrees/skill-discovery-schema-02/`.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for scenario scope, prompt
  and rubric bytes, supplied-input representation, and scenario meaning.
- Package exactly `DISC-01` through `DISC-12` at
  `skill-validation/scenarios/skill-discovery/disc-01/` through
  `disc-12/`.
- Give each `test.json` exactly the schema `"0.2"` keys
  `schema_version`, `id`, `prompt`, `fixtures`, and `execution`; use
  `"schema_version":"0.2"`, its lowercase scenario ID,
  `"prompt":"prompt.md"`, and `"fixtures":[]`.
- Give every `test.json` the execution declaration
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"high"}`.
- Materialize each canonical target prompt and rubric without changing any
  byte. Do not adapt, clarify, reflow, or improve them.
- Do not supply repository skills, dependencies, scenario-owned files, or any
  other fixture. The complete nine-description context is already inline in
  each canonical target prompt.
- Keep every scenario response-only. Do not use `{{evidence_dir}}`, request
  file changes, inspect response meaning, score a response, or validate result
  contents beyond the runner's mechanical status.
- Add only the catalog-local acceptance test named below. Do not change runner,
  provider, schema, skills, shared helpers, or other catalogs.
- The owner's standing approval covers the single Codex smoke invocation. Run
  only `DISC-12`, once, with no retry.
- Skip external review. The controller owns the internal catalog review.
- Stop if a canonical source is unavailable or hash-mismatched, an adaptation
  or fixture is required, or the existing runner cannot represent an
  empty-fixture package. After recording and cleaning up the smoke attempt, stop
  if its runner status is not `COMPLETED`.
- Do not merge or push implementation changes, archive this plan, update the
  roadmap, remove the feature branch or worktree, or create the next catalog
  plan before new explicit owner approval.

## Catalog definition

### Candidate inventory

| ID | Purpose | Supplied context |
|---|---|---|
| `DISC-01` | Route internal logical review of supplied API text to review, parent-development, and research guidance. | Inline nine-skill descriptions only |
| `DISC-02` | Route remediation of already-reported findings to the review loop without starting a new review. | Inline nine-skill descriptions only |
| `DISC-03` | Route a purely stylistic sentence shortening through concise writing, parent development, and research. | Inline nine-skill descriptions only |
| `DISC-04` | Route resumed implementation through verification and commit with parent-development and research guidance. | Inline nine-skill descriptions only |
| `DISC-05` | Route a repository handler fact request through parent-development and research guidance. | Inline nine-skill descriptions only |
| `DISC-06` | Route a development-subagent request through parent-development, research, and dispatch guidance. | Inline nine-skill descriptions only |
| `DISC-07` | Route plan creation through parent-development, research, and lean-plan guidance. | Inline nine-skill descriptions only |
| `DISC-08` | Route a mechanical cross-code-and-documentation rename through parent-development, research, and stale-reference sweeping. | Inline nine-skill descriptions only |
| `DISC-09` | Route a temporary-shortcut record through parent-development, research, and explicit-rationale guidance. | Inline nine-skill descriptions only |
| `DISC-10` | Route a plan deferral with supplied rationale through parent-development, research, lean-plan, and explicit-rationale guidance. | Inline nine-skill descriptions only |
| `DISC-11` | Preserve research routing for a private, uncommitted factual software note. | Inline nine-skill descriptions only |
| `DISC-12` | Preserve research routing for a non-development, response-only factual interaction. | Inline nine-skill descriptions only |

`DISC-12` is the sole smoke representative. It protects the catalog's broadest
response/interaction boundary while using the same prompt-only, empty-fixture
runner composition as the other scenarios. Catalog acceptance loads and
prepares every package offline.

### Canonical prompts and rubrics

Hashes are SHA-256 over complete file bytes, including the trailing LF. Paths
below are relative to `skill-validation/` at the canonical source commit.

| ID | Target prompt SHA-256 | Rubric SHA-256 |
|---|---|---|
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

For each ID, source `prompt.md` from
`fixtures/skill-discovery/prompts/<lowercase-id>-target.md`. Source
`rubric.md` from
`fixtures/skill-discovery/rubrics/task-18a-disc-01-10.md` for `DISC-01`
through `DISC-10`,
`fixtures/skill-discovery/rubrics/disc-11.md` for `DISC-11`, and
`fixtures/skill-discovery/rubrics/disc-12.md` for `DISC-12`.

The target prompt hashes above identify the active Task 18A epoch. Control
prompts, historical rubrics, prior responses, scores, and replay records are not
package inputs and do not enter this migration.

Catalog acceptance does not audit rubric contents. Rubric hashes guide exact
materialization and review only.

### Prompt adaptations and fixture mappings

Apply no prompt adaptations. Preserve each target prompt byte-for-byte and
declare `fixtures: []` in every configuration.

The canonical scenarios contain no supplied files. Do not create `fixture/`,
skill, dependency, project, evidence, manifest, or bundle files.

### Package records

Before the smoke, each package contains exactly `README.md`, `prompt.md`,
`rubric.md`, and `test.json`. Each README records only the scenario purpose,
prompt and rubric provenance, the empty fixture mapping, and smoke status. After
the smoke, only `DISC-12` may contain and link the exact retained result; its
README states the runner's mechanical status. Do not make a behavioral claim or
duplicate result contents.

## Catalog acceptance

Create
`skill-validation/runner/acceptance/test_skill_discovery_catalog.py`. Keep
catalog data and any small local helpers in that file. It verifies only:

- exactly the twelve planned scenario directories and their exact package
  files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- prompt bytes against the hashes above;
- a literal empty fixture declaration for every package;
- resolved prompt tokens and no stale `supplied-skills/` path;
- absence of rubric bytes from declared and prepared provider inputs; and
- empty prepared fixture and initial evidence directories.

Permit only `DISC-12` to add optional `smoke-result.json` after acceptance is
established. Redirect the runner's temporary root to pytest's `tmp_path` so
preparation leaves no run bundle outside the test directory.

Acceptance does not invoke a provider or validate README prose, rubric content,
execution choices, smoke results, response or result schemas, stdout, stderr,
provider artifacts, or behavioral outcomes. It does not reconstruct a result,
add a negative-test matrix, or add shared machinery. Those are accepted,
unexamined edges outside this migration.

## Verification

After package acceptance is implemented, run from
`skill-validation/runner`:

```bash
uv run pytest -q acceptance/test_skill_discovery_catalog.py
uv run pytest -q
```

After the smoke record and index update, rerun only the focused acceptance test
because those changes do not alter package preparation. If review repairs a
package or acceptance behavior, rerun both commands; otherwise rerun only the
affected check. Do not add another verifier or run unrelated skill test suites.

## Task 1: Package all twelve scenarios

**Files:** Create all twelve scenario packages.

**Boundary:** Stop on a missing source, hash mismatch, malformed configuration,
required prompt adaptation or fixture, or an empty-fixture package the current
runner cannot represent.

- Materialize the canonical target prompts and rubrics unchanged.
- Create the exact schema `"0.2"` configurations with empty fixture arrays
  and minimal package READMEs.
- Do not carry forward schema `"0.1"` configuration, control arms, historical
  rubrics, result-validation, bundle, or replay machinery.

## Task 2: Add catalog acceptance and verify preparation

**Files:** Create
`skill-validation/runner/acceptance/test_skill_discovery_catalog.py`.

**Boundary:** Provider behavior and result content remain accepted, unexamined
edges. Do not add output checks, result checks, mutations, negative-test
matrices, or shared helpers.

- Implement exactly the catalog-local acceptance contract above.
- Run the focused acceptance and the complete offline runner suite once.
- Review the test against the package-only boundary.

## Task 3: Run and record the representative smoke

**Files:** Create
`skill-validation/scenarios/skill-discovery/disc-12/smoke-result.json` only if
the runner publishes `result.json`. Modify the `DISC-12` README in every
outcome; modify the scenario migration index only after `COMPLETED`.

**Boundary:** Missing output or any status other than `COMPLETED` stops the
catalog without retry. Response meaning, rubric satisfaction, stdout/stderr,
artifact inventories, result schemas, and result reconstruction remain
unexamined.

- From `skill-validation/runner`, invoke exactly once:
  `uv run skilltest run ../scenarios/skill-discovery/disc-12/test.json`.
  Do not retry or run another scenario.
- If the runner publishes `result.json`, replace any prior
  `disc-12/smoke-result.json` with its exact bytes. If it publishes no result,
  remove any prior retained result.
- Read only the runner-written mechanical status needed for disposition. Do not
  compare the retained file back to the bundle or validate any other result
  field.
- Record the runner's mechanical outcome in the `DISC-12` README and remove
  the owned temporary run directory in every outcome. Retain no other run
  artifact.
- If the retained result's runner status is `COMPLETED`, update the migration
  index, link all twelve READMEs, identify `DISC-12` as representative, and
  update totals to 12/12 for this catalog and 62/105 overall.
- If no result is retained or status is not `COMPLETED`, do not update the
  index; rerun focused acceptance and stop for owner direction.
- For `COMPLETED`, rerun focused acceptance and review the records.

## Controller review and approval gate

The controller performs this review directly and does not dispatch an external
review.

- Review the whole catalog against the governing design and this plan. Confirm
  the final diff is limited to the twelve packages, their catalog-local
  acceptance test, and the migration index.
- Confirm that no response judgment, result validation, runner/provider/schema
  change, shared helper, lifecycle state, historical control/replay material, or
  unrelated bookkeeping entered the implementation.
- Address only verified in-scope findings and rerun only checks affected by
  repairs.
- Report the implementation commits, focused and full offline verification,
  smoke attempt and retained result status, and internal-review disposition.
- Stop and obtain explicit owner approval before merge, push, plan archive,
  roadmap update, feature worktree/branch removal, or next-catalog planning.

## Post-approval closeout

- Merge the feature branch into local `main`.
- On `main`, check the `skill-discovery` roadmap item and move this plan to
  `plans/completed/`, adjusting its three header links for the new location,
  then commit the closeout.
- Push `main`, then remove this catalog's worktree and local feature branch.
  Do not create the next catalog plan without separate owner approval.

## Done when

- All twelve packages pass catalog acceptance and the complete offline runner
  suite.
- One approved `DISC-12` invocation retains the exact runner-produced
  `COMPLETED` result.
- The migration index reports 12/12 for this catalog and 62/105 overall.
- Internal review passes without output or result judgment and without extra
  migration process or bookkeeping.
- After owner approval, the catalog is merged and pushed, the roadmap and plan
  are closed, and the feature worktree and branch are removed.
