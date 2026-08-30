# Writing Explicit Rationale Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` to implement this plan task by task.
> Use `superpowers:verification-before-completion` before completion claims.
> Track progress with the checkboxes below.

**Goal:** Package all six active `writing-explicit-rationale` scenarios for the
schema `"0.2"` runner, retain one completed representative smoke result, and
finish this catalog before planning the next one.

**Architecture:** Each canonical scenario becomes one self-contained package.
`prompt.md` names supplied files beneath `{{fixture_dir}}`, `test.json` declares
each copied file, and `rubric.md` remains evaluator-withheld. Current repository
skills define the default input; `WER-07` also packages one pinned external
dependency and serves as the catalog's representative smoke.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../skill-validation/scenarios/README.md).

## Global constraints

- Implement on branch `feature/writing-explicit-rationale-schema-02` in
  `.worktrees/writing-explicit-rationale-schema-02/`.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for candidate scope,
  scenario meaning, prompt material, scenario-owned bytes, and rubrics.
- Package exactly `WER-01`, `WER-02`, `WER-05`, `WER-06`, `WER-07`, and
  `WER-08`. `WER-03` is historical and `WER-04` is intentionally unused.
- Put each package at
  `skill-validation/scenarios/writing-explicit-rationale/<lowercase-id>/`.
- Give each default configuration the execution declaration
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"low"}`.
- Use current repository `SKILL.md` files directly as fixture sources. Do not
  copy them into scenario packages or pin their hashes.
- Copy the pinned Superpowers 6.3.0 `writing-plans/SKILL.md` beneath the
  `WER-07` package. Do not replace it with another version or a live external
  path.
- Apply only the prompt substitutions listed below. Do not otherwise rewrite,
  normalize, reflow, clarify, or improve canonical prompts or rubrics.
- Keep every scenario response-only. Do not use `{{evidence_dir}}`, request file
  changes, add evaluator behavior, score responses, or inspect response meaning.
- Add only the catalog-local acceptance test named below. Do not change runner,
  provider, schema, skill, shared helper, or other catalog files.
- The smoke requires explicit owner approval. Run only `WER-07`, once.
- Do not merge or push without explicit owner approval. Do not create the next
  catalog plan before this catalog is merged and this plan is archived.
- Stop under the design's fail-closed conditions. In particular, stop if a
  canonical or pinned source is unavailable or differs, an unlisted prompt
  adaptation is needed, the runner cannot represent a scenario, or the smoke
  does not finish with runner status `COMPLETED`.

## Catalog decisions

### Candidate inventory and representative

| ID | Purpose | Default supplied context |
|---|---|---|
| `WER-01` | Apply a small direct plan descope while keeping selected scope, cause, accepted impact, and adjacent rationale intact. | Complete current nine-skill repository bundle plus inline task context |
| `WER-02` | Turn repeated review into a batched durable audit while distinguishing consequential choices from a consequence-free choice. | Current `writing-explicit-rationale` skill plus inline task context |
| `WER-05` | Reference an existing authoritative rationale instead of duplicating it under reviewer pressure. | Current `writing-explicit-rationale` skill plus one scenario-owned architecture document |
| `WER-06` | Retain only history that constrains current correctness or future decisions. | Current `writing-explicit-rationale` skill plus inline task context |
| `WER-07` | Exercise rationale, research, plan-writing, and parent-doctrine composition against multiple primary-source files. | Four current repository skills, one pinned external skill, four scenario-owned project files, and inline task context |
| `WER-08` | Apply the rationale policy outside software by placing a repeatedly requested cause in the durable nonprofit policy. | Current `writing-explicit-rationale` skill plus inline task context |

`WER-07` is the sole representative. It exercises multiple live skills, a
pinned dependency, nested scenario files, several prompt file references, and
the response-only path.

### Canonical prompt and rubric provenance

Hashes are SHA-256 over complete file bytes, including one trailing LF. The
first four prompts are fenced evaluator inputs beneath the named headings in the
canonical catalog. `WER-07` and `WER-08` use the canonical files shown below.

| ID | Canonical prompt source | Prompt SHA-256 | Rubric source | Rubric SHA-256 |
|---|---|---|---|---|
| `WER-01` | `skill-validation/writing-explicit-rationale.md`, `WER-01 — simple direct descope` fenced block | `bd0301ca240e287249de40d773fd2c6d37ca1f231b795beaf4f87bb003b68210` | Active catalog table `WER-01` evaluator-withheld rubric cell | `c4fbdbd8d730a762ec8050a4e5e48131a97a7acb44625d6e5fe53575c30fc8de` |
| `WER-02` | Same file, `WER-02 — repeated-review batch audit` fenced block | `9b2621415525aab803ac01a234bc148746a0e9a437360c2eaa6da6aba7c2f7ab` | Active catalog table `WER-02` evaluator-withheld rubric cell | `6babe6fa60fe3672617e4e2d61d59b7472c51d15e0ce78304b2bfa7f5e1e9181` |
| `WER-05` | Same file, `WER-05 — existing rationale reference` fenced block | `04e991da2e028d059a6fe5ec508b731b73e54ccb67696413be42c719087df6e8` | Active catalog table `WER-05` evaluator-withheld rubric cell | `2ea06ed57c8bbdf68a16c05d59a04b747ee14c7dc86e67c6d0e0072ca19bc18f` |
| `WER-06` | Same file, `WER-06 — relevant history only` fenced block | `84fa4c432fdd47f0a9e1385c4721da55ef1fcfaf19e38963156ee2aede78ad64` | Active catalog table `WER-06` evaluator-withheld rubric cell | `948fa0967f058ee482d617df04c3f146c711dde841e0a9f906304aed6be48e08` |
| `WER-07` | `skill-validation/fixtures/writing-explicit-rationale/prompts/wer-07.md` | `b4fbdd831bc8d569a4fe61fcb9898d112b44089779c9b4329c30e1df51ece92f` | `skill-validation/fixtures/writing-explicit-rationale/rubrics/wer-07.md` | `2fc48c5a0c9c2aa06e5e20137fbfe0cc2c7f61d404b442b70a9b8c51da2063c5` |
| `WER-08` | `skill-validation/fixtures/writing-explicit-rationale/prompts/wer-08.md` | `ad7fc0befc74d23accd09ac710a0fa1aa1111c3c48d218e6ca2672ac606c4c9a` | `skill-validation/fixtures/writing-explicit-rationale/rubrics/wer-08.md` | `98781f268c1b7f4d6052c896ca6bbc257377d2daff8a493ec9d9325121ef73ec` |

Materialize each rubric as `rubric.md`. For table-cell rubrics, use exactly the
cell text plus one trailing LF. These rubric hashes guide authoring and
provenance; catalog acceptance does not audit rubric contents.

### Prompt adaptations

Start from the canonical prompt bytes and make only these substitutions.
Preserve all other bytes and the trailing LF.

| ID | Literal substitutions | Resulting `prompt.md` SHA-256 |
|---|---|---|
| `WER-01` | Replace `The complete nine-skill local bundle is installed.` with `The complete nine-skill local bundle is supplied beneath \`{{fixture_dir}}/skills\`.`; replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`. | `1f6ea36007f027fef44dc12d60f1f33dff7fbde4b2cbd283f5e2399f8e6adf30` |
| `WER-02` | Replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`. | `743d95a448c6cd7d1a5cef4e839f6482ec989b7ebe219bdc9b0a360a696dd2a9` |
| `WER-05` | Replace canonical `docs/architecture/ingest.md` with `{{fixture_dir}}/docs/architecture/ingest.md`; replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`. | `dc35cfaa391e9f802a9b9de8c4fc21058ef61c1399381e26c4d836c0b5c6b01c` |
| `WER-06` | Replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`. | `e7ea734a0db797e828165fac6e45a042094880a4e215d20699f73a6c5b2db205` |
| `WER-07` | Replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`; root the four listed `project/wer-07/...` paths at `{{fixture_dir}}/`. | `a8da5c8b16a2c9cefbce2af41d0e1dc436ddac78d49795652f3a2fd45fd7e295` |
| `WER-08` | Replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`. | `0b5c3b220cd085cc01e1c06cab3156e838b8683a33c30034e9a96ed644189260` |

These are path and required-environment adaptations only. Do not add a wrapper
or reorganize prompts to mimic the sample anatomy.

### Live skill fixtures

For each live skill, use source `../../../../skills/<skill-id>/SKILL.md` and
target `skills/<skill-id>/SKILL.md`. Declare every used file separately.

| ID | Live skills |
|---|---|
| `WER-01` | `adversarial-review-loop`; `adversarial-review`; `concise-writing`; `disciplined-development`; `disciplined-research`; `dispatching-development-subagents`; `lean-plan-writing`; `sweeping-stale-references`; `writing-explicit-rationale` |
| `WER-02` | `writing-explicit-rationale` |
| `WER-05` | `writing-explicit-rationale` |
| `WER-06` | `writing-explicit-rationale` |
| `WER-07` | `disciplined-development`; `disciplined-research`; `lean-plan-writing`; `writing-explicit-rationale` |
| `WER-08` | `writing-explicit-rationale` |

### Packaged files

| ID | Provenance | Package source | Fixture target | SHA-256 |
|---|---|---|---|---|
| `WER-05` | Canonical fenced `WER-05 fixture` at the source commit | `fixture/docs/architecture/ingest.md` | `docs/architecture/ingest.md` | `5e25960ed19f0e046ecb263282d9244b9a5026695cc16a7ddb08663f422e4f7e` |
| `WER-07` | Superpowers 6.3.0 `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans/SKILL.md` | `fixture/skills/writing-plans/SKILL.md` | `skills/writing-plans/SKILL.md` | `48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2` |
| `WER-07` | Canonical `skill-validation/fixtures/writing-explicit-rationale/project/wer-07/batch_import.py` | `fixture/project/wer-07/batch_import.py` | `project/wer-07/batch_import.py` | `2fbe0370868be60a4b8a96907c7404c65ae7b969bc5b63cfb0a6b521306beb20` |
| `WER-07` | Canonical `skill-validation/fixtures/writing-explicit-rationale/project/wer-07/sources/ingest-architecture.md` | `fixture/project/wer-07/sources/ingest-architecture.md` | `project/wer-07/sources/ingest-architecture.md` | `abc91b3248cae99aef1b3baa1418e5ea4eb0d943c99aa3460f75fd6fbec2f46a` |
| `WER-07` | Canonical `skill-validation/fixtures/writing-explicit-rationale/project/wer-07/sources/quota-tokens.md` | `fixture/project/wer-07/sources/quota-tokens.md` | `project/wer-07/sources/quota-tokens.md` | `0c06c4c7edc867de42105325eaccf30fb9112a7888a38eb812ec4b03945eeeef` |
| `WER-07` | Canonical `skill-validation/fixtures/writing-explicit-rationale/project/wer-07/sources/telemetry-comparison.md` | `fixture/project/wer-07/sources/telemetry-comparison.md` | `project/wer-07/sources/telemetry-comparison.md` | `34853c94fa465fc5ba2ef01b810419f2b3200b61a03b2111bdb2a150f31ba49a` |

### Default configurations

Every `test.json` uses schema `"0.2"`, its lowercase scenario ID,
`"prompt":"prompt.md"`, the execution declaration in Global constraints, and
these fixture mappings:

| ID | Fixture mappings |
|---|---|
| `wer-01` | The nine live skills listed above |
| `wer-02` | Live `writing-explicit-rationale` |
| `wer-05` | Live `writing-explicit-rationale`; packaged `ingest.md` |
| `wer-06` | Live `writing-explicit-rationale` |
| `wer-07` | Four listed live skills; pinned `writing-plans`; four listed project files |
| `wer-08` | Live `writing-explicit-rationale` |

### README content

Each scenario README contains only `Purpose`, `Inputs`, and `Smoke` sections.
Use the candidate table for Purpose. Inputs compactly records prompt provenance
and adaptation, rubric provenance, and each supplied file's source and provider
location. Smoke initially states that no schema `"0.2"` result is retained.
After the representative run, only `WER-07` links the retained result and states
the runner's mechanical status. Do not duplicate the configuration or make a
behavioral claim.

## Catalog acceptance

Create
`skill-validation/runner/acceptance/test_writing_explicit_rationale_catalog.py`.
Keep all catalog data and small helpers in that file. It verifies only:

- exactly the six planned scenario directories and their required package files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- prompt bytes against the adapted prompt hashes above;
- fixture source and target mappings against this plan;
- packaged canonical and pinned file bytes against the hashes above;
- resolved prompt tokens and absence of stale `supplied-skills/` paths;
- absence of rubric bytes from declared and prepared provider inputs; and
- an empty initial evidence directory.

Redirect the runner's temporary root to pytest's `tmp_path`, following the
existing provider-smoke acceptance pattern, so preparation leaves no run bundle
outside the test's temporary directory.

It does not invoke a provider, validate README prose or rubric contents, compare
the configuration's ID, prompt, provider, model, or effort to this plan, inspect
smoke results, or add shared machinery.

## Verification

Catalog verification consists of these existing checks:

- From `skill-validation/runner`, run
  `uv run pytest -q acceptance/test_writing_explicit_rationale_catalog.py`.
- From `skill-validation/runner`, run `uv run pytest -q`.
- From the repository root, run
  `cd skills/disciplined-development/hooks && python3 -m pytest -q`.
- Run the repository's existing local Markdown-link check documented under
  `Verification commands` in
  `13599fb7d3127334b0d07bfe468767e586ec5f9c:skill-validation/README.md`.
- Run `git diff --check`.

Do not add another verifier. Run the focused acceptance and full offline runner
suite after Task 4. Run the full catalog verification after Tasks 5 and 6,
rerunning affected checks after verified review repairs.

## Task 1: Package `WER-01` and `WER-02`

**Files:**

- Create `README.md`, `prompt.md`, `rubric.md`, and `test.json` beneath
  `skill-validation/scenarios/writing-explicit-rationale/wer-01/` and
  `skill-validation/scenarios/writing-explicit-rationale/wer-02/`.
- Modify this plan only to mark completed steps.

- [ ] Create both packages from the catalog decisions above.
- [ ] Confirm the two prompts have their planned resulting hashes and each
  configuration loads with the runner.
- [ ] Review the package files against their canonical sources and commit the
  task changes.

## Task 2: Package `WER-05`, `WER-06`, and `WER-08`

**Files:**

- Create `README.md`, `prompt.md`, `rubric.md`, and `test.json` beneath each of
  `wer-05/`, `wer-06/`, and `wer-08/`.
- Create
  `skill-validation/scenarios/writing-explicit-rationale/wer-05/fixture/docs/architecture/ingest.md`.
- Modify this plan only to mark completed steps.

- [ ] Create all three packages and the `WER-05` scenario-owned fixture.
- [ ] Confirm the prompts and copied canonical file have their planned hashes
  and each configuration loads with the runner.
- [ ] Review the package files against their canonical sources and commit the
  task changes.

## Task 3: Package representative `WER-07`

**Files:**

- Create `README.md`, `prompt.md`, `rubric.md`, and `test.json` beneath
  `skill-validation/scenarios/writing-explicit-rationale/wer-07/`.
- Create each pinned and scenario-owned file at its package source path from the
  Packaged files table.
- Modify this plan only to mark completed steps.

- [ ] Verify the Superpowers 6.3.0 dependency is available with the planned
  hash; stop if it is not.
- [ ] Create the package, pinned dependency, and four canonical project files.
- [ ] Confirm the prompt and packaged files have their planned hashes and the
  configuration loads with the runner.
- [ ] Review the package files against their sources and commit the task
  changes.

## Task 4: Add catalog acceptance and verify preparation

**Files:**

- Create
  `skill-validation/runner/acceptance/test_writing_explicit_rationale_catalog.py`.
- Modify this plan only to mark completed steps.

- [ ] Implement the final six-scenario acceptance contract above using only
  catalog-local data and helpers.
- [ ] Run the focused acceptance and complete offline runner suite.
- [ ] Review the test for exact agreement with the spec's package-only boundary
  and commit the task changes.

## Task 5: Run and record the representative smoke

**Files:**

- Create
  `skill-validation/scenarios/writing-explicit-rationale/wer-07/smoke-result.json`
  only if the runner publishes `result.json`.
- Modify `skill-validation/scenarios/writing-explicit-rationale/wer-07/README.md`.
- Modify `skill-validation/scenarios/README.md` only after a `COMPLETED` result.
- Modify this plan only to mark completed steps.

- [ ] Present the `WER-07` configuration to the owner and obtain explicit
  approval for one Codex invocation.
- [ ] From `skill-validation/runner`, run exactly
  `uv run skilltest run ../scenarios/writing-explicit-rationale/wer-07/test.json`
  once. Do not retry or run another scenario.
- [ ] If the runner publishes `result.json`, copy its exact bytes to
  `wer-07/smoke-result.json`; otherwise remove any prior retained result.
- [ ] Record the runner status and result link, when present, in the `WER-07`
  README; remove the temporary run bundle and retain no other run artifact.
- [ ] If no result is retained or its status is not `COMPLETED`, run catalog
  verification, review and commit the smoke disposition, README, and plan
  tracking, then stop and request owner direction. Do not update the migration
  index.
- [ ] For a `COMPLETED` result, add the catalog to the migration index, link all
  six READMEs, identify `WER-07` as representative, and update totals to 6/6 for
  this catalog and 6/105 overall.
- [ ] Run catalog verification, review the smoke documentation and index update,
  and commit the task changes.

## Task 6: Final review, merge, and catalog bookkeeping

**Files:**

- Modify `plans/2026-08-24-scenario-porting-roadmap.md` after merge.
- Move this plan to
  `plans/completed/2026-08-29-writing-explicit-rationale-catalog-migration.md`
  after merge.

- [ ] Run catalog verification and complete a whole-catalog review against the
  governing design and this plan. Address verified findings and rerun affected
  checks.
- [ ] Confirm the final diff is limited to this catalog's packages, its local
  acceptance test, migration index, and plan tracking.
- [ ] Present the commits, verification results, retained smoke result, review
  disposition, and cleanup targets to the owner. Obtain explicit approval before
  merging or pushing.
- [ ] After approval, merge the feature branch into local `main`.
- [ ] On `main`, check the `writing-explicit-rationale` roadmap item and move
  this plan to `plans/completed/`, fixing relative links if needed. Run the
  Markdown-link check and `git diff --check`, then commit those bookkeeping
  changes.
- [ ] Run catalog verification on `main`, push `main`, then remove this catalog's
  worktree and local feature branch. Do not create the next catalog plan in this
  task.

## Done when

- [ ] All six packages pass the catalog acceptance test and offline runner suite.
- [ ] `WER-07` retains the latest runner-produced `COMPLETED`
  `smoke-result.json` from one approved attempt.
- [ ] The migration index reports 6/6 for this catalog and 6/105 overall.
- [ ] Final review and repository verification pass.
- [ ] With owner approval, the catalog is merged and pushed, the roadmap is
  checked, the plan is archived, and the worktree and feature branch are removed.
