# Sweeping Stale References Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` to implement this plan task by task.
> Use `superpowers:verification-before-completion` before completion claims.
> Track progress with the checkboxes below.

**Goal:** Package all six active `sweeping-stale-references` scenarios for the
schema `"0.2"` runner, retain one completed representative smoke result, and
finish this catalog before planning the next one.

**Architecture:** Each canonical scenario becomes one self-contained package.
`prompt.md` names supplied files beneath `{{fixture_dir}}`, `test.json` declares
each copied file, and `rubric.md` remains evaluator-withheld. Current repository
skills define the default skill inputs; canonical scenario-owned files are
copied into each package that uses them, and `SSR-01` serves as the catalog's
representative smoke.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../skill-validation/scenarios/README.md).

## Global constraints

- Implement on branch `feature/sweeping-stale-references-schema-02` in
  `.worktrees/sweeping-stale-references-schema-02/`.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for candidate scope,
  scenario meaning, prompt material, scenario-owned bytes, and rubrics.
- Package exactly `SSR-01`, `SSR-02`, `SSR-03`, `SSR-05`, `SSR-06`, and
  `SSR-07`. `SSR-04` is retired and remains excluded.
- Put each package at
  `skill-validation/scenarios/sweeping-stale-references/<lowercase-id>/`.
- Give each default configuration the execution declaration
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"high"}`.
- Use current repository `SKILL.md` files directly as fixture sources. Do not
  copy them into scenario packages or pin their hashes.
- Duplicate canonical scenario-owned files into each self-contained package
  that uses them. Do not introduce shared fixture storage.
- Apply only the prompt substitutions listed below. Do not otherwise rewrite,
  normalize, reflow, clarify, or improve canonical prompts or rubrics.
- Keep every scenario response-only. Do not use `{{evidence_dir}}`, request file
  changes, add evaluator behavior, score responses, or inspect response meaning.
- Add only the catalog-local acceptance test named below. Do not change runner,
  provider, schema, skill, shared helper, or other catalog files.
- The smoke requires explicit owner approval. Run only `SSR-01`, once.
- Do not merge or push without explicit owner approval. Do not create the next
  catalog plan before this catalog is merged and this plan is archived.
- Stop under the design's fail-closed conditions. In particular, stop if a
  canonical source is unavailable or differs, an unlisted prompt adaptation is
  needed, the runner cannot represent a scenario, or the smoke does not finish
  with runner status `COMPLETED`.

## Catalog decisions

### Candidate inventory and representative

| ID | Purpose | Default supplied context |
|---|---|---|
| `SSR-01` | Exercise an end-to-end load-bearing rename with complete discovery, rationale-preserving reconciliation, durable sweep evidence, and verification. | Complete current nine-skill repository bundle plus the two-file session project |
| `SSR-02` | Treat one reviewer hit as a sample and reconcile a complete cross-category search inventory. | Current `sweeping-stale-references` skill plus the canonical 13-match inventory |
| `SSR-03` | Group a large sweep only by path and outcome while retaining precise locations, counts, and complete evidence. | Current `sweeping-stale-references` skill plus the canonical 126-match inventory |
| `SSR-05` | Record the required truthful negative sweep form for a single-file change with no sibling matches. | Current `sweeping-stale-references` skill plus the canonical zero-sibling search report |
| `SSR-06` | Identify exactly the symbol, attached-rationale, and documentation updates required by the session rename. | Complete current nine-skill repository bundle plus the two-file session project |
| `SSR-07` | Preserve the partner constraint and accepted refresh cost while renaming the session-setting rationale. | Complete current nine-skill repository bundle plus the two-file session project |

`SSR-01` is the sole representative because it composes the catalog's complete
discovery, rationale-preservation, reconciliation, evidence, and verification
path while exercising the full live skill bundle and scenario-owned files.

### Canonical prompt and rubric provenance

Hashes are SHA-256 over complete file bytes, including one trailing LF. The
first four prompts are fenced evaluator inputs beneath the named headings in the
canonical catalog. `SSR-06` and `SSR-07` use the canonical files shown below.

| ID | Canonical prompt source | Prompt SHA-256 | Rubric source | Rubric SHA-256 |
|---|---|---|---|---|
| `SSR-01` | `skill-validation/sweeping-stale-references.md`, `SSR-01 — simple direct rename` fenced block | `a4f377770c2811470504dc72350220e002e064248cdb22eb5942f53cf6416768` | Active catalog table `SSR-01` evaluator-withheld rubric cell | `ce3ee9983a4ab647b11010c0d2760ec62cff47f85e0e7fab1ad502044fb95ac2` |
| `SSR-02` | Same file, `SSR-02 — reviewer one-hit completeness` fenced block | `79637843faf83489c19d07fa5cd99e5c8725c2931b8974d284713695d3b6ddd8` | Active catalog table `SSR-02` evaluator-withheld rubric cell | `85e031214c456eab383b00e8a18d16e384d15902ace99491d2acbf2785a739bb` |
| `SSR-03` | Same file, `SSR-03 — 126-match grouped sweep` fenced block | `109ba0f3c5ee7afc94649b59624ca42683088f13a1cfca034540be83b0e963dc` | Active catalog table `SSR-03` evaluator-withheld rubric cell | `803b8d4133d4b833f1c1c805ec82ba859c6aa9989c68038c3d10f1d1b178325d` |
| `SSR-05` | Same file, `SSR-05 — required negative form` fenced block | `1e01a57689204f0647bfd4cbd952d8973d4a64c23f3ca5e844e56f7e1fa5832a` | Active catalog table `SSR-05` evaluator-withheld rubric cell | `5a4cc77d65a97111082c168434028062de8fe5ac62b9a094eb43b1f331e3dfe5` |
| `SSR-06` | `skill-validation/fixtures/sweeping-stale-references/prompts/ssr-06.md` | `d9de7958ba1a54e0b36288e16f9d854b9418e41ec26656173a28bb8f8799ffb8` | `skill-validation/fixtures/sweeping-stale-references/rubrics/ssr-06.md` | `286a3a8eab4c9aac655454036fa1b590856f230bf11f0db97841a6d2d0040ccb` |
| `SSR-07` | `skill-validation/fixtures/sweeping-stale-references/prompts/ssr-07.md` | `41d26783e7b85d33164bd5f3983e52b607aa716e90464768e808ae40f35b2646` | `skill-validation/fixtures/sweeping-stale-references/rubrics/ssr-07.md` | `cf1d686418a9791137c14f539494041b91f32e855c3858ca757dc1f432ce24b7` |

Materialize each rubric as `rubric.md`. For table-cell rubrics, use exactly the
cell text plus one trailing LF. These rubric hashes guide authoring and
provenance; catalog acceptance does not audit rubric contents.

### Prompt adaptations

Start from the canonical prompt bytes and make only these substitutions.
Preserve all other bytes and the trailing LF.

| ID | Literal substitutions | Resulting `prompt.md` SHA-256 |
|---|---|---|
| `SSR-01` | Replace `The complete nine-skill local bundle is installed.` with `The complete nine-skill local bundle is supplied beneath \`{{fixture_dir}}/skills\`.`; replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`; replace `Inspect the supplied project files, then` with `Inspect \`{{fixture_dir}}/project/src/session.py\` and \`{{fixture_dir}}/project/docs/session-policy.md\`, then`. | `b87520036c0f72d5eadeb9d43f1cc50ed2ff144f604e5ca7b9277f1fb51390c3` |
| `SSR-02` | Replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`; replace canonical `context/match-inventory.md` with `{{fixture_dir}}/context/match-inventory.md`. | `a6113dc283c5dd61c79698f96d4d0a5a09a327619c64969e4bd25178975be93d` |
| `SSR-03` | Replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`; replace canonical `context/grouping-inventory.md` with `{{fixture_dir}}/context/grouping-inventory.md`. | `5e1a1fa2f60db6cf2aeceaed4a85b869366e4e6a8b20cfe8bf0e4398de46f39e` |
| `SSR-05` | Replace every `skills/` prefix in a canonical skill path with `{{fixture_dir}}/skills/`; replace canonical `context/single-file-search.md` with `{{fixture_dir}}/context/single-file-search.md`. | `8d9f3a242802100fbe7ded2b7ace37f0647030502c9b5c3dd0b1efd9c268477c` |
| `SSR-06` | Apply the exact shared insertion and replacement below. | `a39d26e62ad7ec6070e51655b0282ac8072547349f12ae39e0642f541dc1c401` |
| `SSR-07` | Apply the exact shared insertion and replacement below. | `86a40957dad5091eac5f650ad44f8a71ab85aa318038f77e982952fa7294187f` |

For both `SSR-06` and `SSR-07`, insert
`The complete nine-skill local bundle is supplied beneath \`{{fixture_dir}}/skills\`.`
immediately after the first line. Then replace this exact canonical text:

```text
Invoke `sweeping-stale-references`, read it completely, and follow it as
binding guidance.
```

with:

```text
Invoke `sweeping-stale-references`: read `{{fixture_dir}}/skills/sweeping-stale-references/SKILL.md` completely and follow it as
binding guidance.

Read `{{fixture_dir}}/project/src/session.py` and `{{fixture_dir}}/project/docs/session-policy.md`.
```

These additions expose canonical supplied context that the schema `"0.2"`
runner otherwise copies without describing; they do not change the task or
requested output. No other wrapper or prompt reorganization is permitted.

### Live skill fixtures

For each live skill, use source `../../../../skills/<skill-id>/SKILL.md` and
target `skills/<skill-id>/SKILL.md`. Declare every used file separately.

| ID | Live skills |
|---|---|
| `SSR-01` | `adversarial-review-loop`; `adversarial-review`; `concise-writing`; `disciplined-development`; `disciplined-research`; `dispatching-development-subagents`; `lean-plan-writing`; `sweeping-stale-references`; `writing-explicit-rationale` |
| `SSR-02` | `sweeping-stale-references` |
| `SSR-03` | `sweeping-stale-references` |
| `SSR-05` | `sweeping-stale-references` |
| `SSR-06` | Same nine-skill bundle as `SSR-01` |
| `SSR-07` | Same nine-skill bundle as `SSR-01` |

### Packaged files

| IDs | Provenance | Package source | Fixture target | SHA-256 |
|---|---|---|---|---|
| `SSR-01`, `SSR-06`, `SSR-07` | Canonical fenced `SSR-01 fixture` at the source commit | `fixture/project/src/session.py` | `project/src/session.py` | `a975fc6bef67344143832d89a6b24b12a8b59da4682236c842f8639eb9378cd2` |
| `SSR-01`, `SSR-06`, `SSR-07` | Canonical fenced `SSR-01 fixture` at the source commit | `fixture/project/docs/session-policy.md` | `project/docs/session-policy.md` | `a925897761b094ba37bf8f7825ceab7fac62a48beeea310dbb5f412ef74d1d0c` |
| `SSR-02` | Canonical fenced `SSR-02 fixture` at the source commit | `fixture/context/match-inventory.md` | `context/match-inventory.md` | `43b3f8819da7b85ccff406f64a4d0c438ebc4cea35e5628ac4e0919a64e7dcf6` |
| `SSR-03` | Canonical fenced `SSR-03 fixture` at the source commit | `fixture/context/grouping-inventory.md` | `context/grouping-inventory.md` | `0916a116c5d0d98089b000a65bcfe1b73ec26951b4659b6279e7f6df0c1e1b02` |
| `SSR-05` | Canonical fenced `SSR-05 fixture` at the source commit | `fixture/context/single-file-search.md` | `context/single-file-search.md` | `48f863afc5e164a3d74f19271656f98f88e00c87c48d10d6995318a7aaece85f` |

Each grouped `SSR-01`/`SSR-06`/`SSR-07` row requires a separate copy beneath
every named package. Shared storage is excluded because each scenario package
must remain self-contained; the accepted cost is three identical canonical
copies of each small project file.

### Default configurations

Every `test.json` uses schema `"0.2"`, its lowercase scenario ID,
`"prompt":"prompt.md"`, the execution declaration in Global constraints, and
these fixture mappings:

| ID | Fixture mappings |
|---|---|
| `ssr-01` | The nine live skills listed above; packaged `session.py`; packaged `session-policy.md` |
| `ssr-02` | Live `sweeping-stale-references`; packaged `match-inventory.md` |
| `ssr-03` | Live `sweeping-stale-references`; packaged `grouping-inventory.md` |
| `ssr-05` | Live `sweeping-stale-references`; packaged `single-file-search.md` |
| `ssr-06` | The nine live skills listed above; packaged `session.py`; packaged `session-policy.md` |
| `ssr-07` | The nine live skills listed above; packaged `session.py`; packaged `session-policy.md` |

### README content

Each scenario README contains only `Purpose`, `Inputs`, and `Smoke` sections.
Use the candidate table for Purpose. Inputs compactly records prompt provenance
and adaptation, rubric provenance, and each supplied file's source and provider
location. Smoke initially states that no schema `"0.2"` result is retained.
After the representative run, only `SSR-01` links the retained result and states
the runner's mechanical status. Do not duplicate the configuration or make a
behavioral claim.

## Catalog acceptance

Create
`skill-validation/runner/acceptance/test_sweeping_stale_references_catalog.py`.
Keep all catalog data and small helpers in that file. It verifies only:

- exactly the six planned scenario directories and their required package files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- prompt bytes against the adapted prompt hashes above;
- fixture source and target mappings against this plan;
- packaged canonical file bytes against the hashes above;
- resolved prompt tokens and absence of stale `supplied-skills/` paths;
- absence of rubric bytes from declared and prepared provider inputs; and
- an empty initial evidence directory.

Permit only `SSR-01` to add an optional `smoke-result.json` after acceptance is
first established. Redirect the runner's temporary root to pytest's `tmp_path`,
following the existing catalog acceptance pattern, so preparation leaves no run
bundle outside the test's temporary directory.

Acceptance does not invoke a provider, validate README prose or rubric contents,
compare the configuration's ID, prompt, provider, model, or effort to this plan,
inspect smoke results, or add shared machinery. Those omissions preserve the
shared design's package-only boundary.

## Verification

Catalog verification consists of these existing checks:

- From `skill-validation/runner`, run
  `uv run pytest -q acceptance/test_sweeping_stale_references_catalog.py`.
- From `skill-validation/runner`, run `uv run pytest -q`.
- From the repository root, run
  `cd skills/disciplined-development/hooks && python3 -m pytest -q`.
- Run the repository's existing local Markdown-link check documented under
  `Verification commands` in
  `13599fb7d3127334b0d07bfe468767e586ec5f9c:skill-validation/README.md`.
- Run `git diff --check`.

Do not add another verifier. Run the focused acceptance and full offline runner
suite after Task 3. Run the full catalog verification after Tasks 4 and 5,
rerunning affected checks after verified review repairs.

## Task 1: Package `SSR-01`, `SSR-06`, and `SSR-07`

**Files:**

- Create `README.md`, `prompt.md`, `rubric.md`, and `test.json` beneath each of
  `skill-validation/scenarios/sweeping-stale-references/ssr-01/`, `ssr-06/`,
  and `ssr-07/`.
- Create both listed project files beneath each package at its Packaged files
  source path.
- Modify this plan only to mark completed steps.

- [x] Create all three packages and their separate canonical project-file
  copies from the catalog decisions above.
- [x] Confirm the prompts and copied files have their planned hashes and each
  configuration loads with the runner.
- [x] Review the package files against their canonical sources and commit the
  task changes.

## Task 2: Package `SSR-02`, `SSR-03`, and `SSR-05`

**Files:**

- Create `README.md`, `prompt.md`, `rubric.md`, and `test.json` beneath each of
  `skill-validation/scenarios/sweeping-stale-references/ssr-02/`, `ssr-03/`,
  and `ssr-05/`.
- Create each scenario's listed inventory file at its package source path.
- Modify this plan only to mark completed steps.

- [ ] Create all three packages and their canonical inventory files from the
  catalog decisions above.
- [ ] Confirm the prompts and copied files have their planned hashes and each
  configuration loads with the runner.
- [ ] Review the package files against their canonical sources and commit the
  task changes.

## Task 3: Add catalog acceptance and verify preparation

**Files:**

- Create
  `skill-validation/runner/acceptance/test_sweeping_stale_references_catalog.py`.
- Modify this plan only to mark completed steps.

- [ ] Implement the final six-scenario acceptance contract above using only
  catalog-local data and helpers.
- [ ] Run the focused acceptance and complete offline runner suite.
- [ ] Review the test for exact agreement with the spec's package-only boundary
  and commit the task changes.

## Task 4: Run and record the representative smoke

**Files:**

- Create
  `skill-validation/scenarios/sweeping-stale-references/ssr-01/smoke-result.json`
  only if the runner publishes `result.json`.
- Modify `skill-validation/scenarios/sweeping-stale-references/ssr-01/README.md`.
- Modify `skill-validation/scenarios/README.md` only after a `COMPLETED` result.
- Modify this plan only to mark completed steps.

- [ ] Present the `SSR-01` configuration to the owner and obtain explicit
  approval for one Codex invocation.
- [ ] From `skill-validation/runner`, run exactly
  `uv run skilltest run ../scenarios/sweeping-stale-references/ssr-01/test.json`
  once. Do not retry or run another scenario.
- [ ] If the runner publishes `result.json`, copy its exact bytes to
  `ssr-01/smoke-result.json`; otherwise remove any prior retained result.
- [ ] Record the runner status and result link, when present, in the `SSR-01`
  README; remove the temporary run bundle and retain no other run artifact.
- [ ] If no result is retained or its status is not `COMPLETED`, run catalog
  verification, review and commit the smoke disposition, README, and plan
  tracking, then stop and request owner direction. Do not update the migration
  index.
- [ ] For a `COMPLETED` result, add the catalog to the migration index, link all
  six READMEs, identify `SSR-01` as representative, and update totals to 6/6 for
  this catalog and 12/105 overall.
- [ ] Run catalog verification, review the smoke documentation and index update,
  and commit the task changes.

## Task 5: Final review, merge, and catalog bookkeeping

**Files:**

- Modify `plans/2026-08-24-scenario-porting-roadmap.md` after merge.
- Move this plan to
  `plans/completed/2026-08-30-sweeping-stale-references-catalog-migration.md`
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
- [ ] On `main`, check the `sweeping-stale-references` roadmap item and move this
  plan to `plans/completed/`. Change its three header links to
  `../specs/2026-08-29-catalog-migration-design.md`,
  `../2026-08-24-scenario-porting-roadmap.md`, and
  `../../skill-validation/scenarios/README.md`; run the Markdown link check and
  `git diff --check`, then commit those bookkeeping changes.
- [ ] Run catalog verification on `main`, push `main`, then remove this catalog's
  worktree and local feature branch. Do not create the next catalog plan in this
  task.

## Done when

- [ ] All six packages pass the catalog acceptance test and offline runner suite.
- [ ] `SSR-01` retains the latest runner-produced `COMPLETED`
  `smoke-result.json` from one approved attempt.
- [ ] The migration index reports 6/6 for this catalog and 12/105 overall.
- [ ] Final review and repository verification pass.
- [ ] With owner approval, the catalog is merged and pushed, the roadmap is
  checked, the plan is archived, and the worktree and feature branch are removed.
