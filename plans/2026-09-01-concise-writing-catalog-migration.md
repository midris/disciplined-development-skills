# Concise Writing Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** Use `superpowers:verification-before-completion`
> before completion claims. Stop at each owner approval gate named below.

**Goal:** Package all seventeen active `concise-writing` scenarios for the
schema `"0.2"` runner, prove that the runner can load and prepare every package,
and retain one completed representative smoke result.

**Architecture:** Each active canonical prompt becomes one response-only package
with its evaluator-withheld rubric and exact supplied files. Current complete
repository skills are declared directly; canonical description extractions and
the required pinned Superpowers files are stored beneath each owning package.
`CW-09` is the sole smoke because it is the catalog's established runner
representative; provider-free acceptance covers every package and fixture shape.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../skill-validation/scenarios/README.md).

## Global constraints

- Start from clean current `main` on branch `feature/concise-writing-schema-02`
  in `.worktrees/concise-writing-schema-02/`.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for active scenario scope,
  prompt and rubric bytes, supplied-input representation, and scenario meaning.
- Package exactly `CW-01` through `CW-14`, `CW-17`, `CW-18`, and `CW-19` at
  `skill-validation/scenarios/concise-writing/cw-01/` through `cw-14/` and
  `cw-17/` through `cw-19/`. `CW-15` and `CW-16` are reserved, not active, and
  receive no package.
- Give each `test.json` exactly the schema `"0.2"` keys `schema_version`, `id`,
  `prompt`, `fixtures`, and `execution`; use its lowercase scenario ID and
  `"prompt":"prompt.md"`.
- Give every configuration
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"high"}`.
- Use current complete repository skill files directly. Do not copy them into a
  package or pin their hashes as catalog requirements.
- Store each description extraction and required external dependency beneath
  every package that owns a copy. Do not create shared dependency storage.
- Apply only the literal path, read-instruction, and environment adaptations
  listed below. Preserve every other prompt byte and every rubric byte.
- Keep every scenario response-only. Do not use `{{evidence_dir}}`, request a
  mutation, inspect response meaning, apply a rubric, or score a response.
  `CW-18` remains response-only: the file-writing request is quoted subject text;
  the evaluator prohibits edits and requests only JSON.
- Add only the catalog-local acceptance test named below. Do not change the
  runner, provider, schema, skills, shared helpers, or another catalog.
- Do not invoke a provider until the owner explicitly approves one `CW-09`
  attempt. After approval, invoke it once with no retry.
- Skip external review. The controller owns one internal catalog review.
- Stop if active scope, canonical bytes, representation, or provenance is
  unavailable; a pinned input is unavailable or hash-mismatched; an unlisted
  prompt adaptation is required; or the current runner cannot load or prepare a
  package. Do not change the runner to accommodate the catalog.
- Do not merge or push implementation changes, archive this plan, update the
  roadmap, remove the feature branch or worktree, or create the next catalog
  plan before explicit owner approval at the final gate.

## Catalog definition

### Candidate inventory

| ID | Purpose | Supplied context |
|---|---|---|
| `CW-01` | Remove simple padding while preserving four states and their distinct completion and failure details. | Concise-writing skill |
| `CW-02` | Compress duplicate retry prose while preserving framing, causality, navigation, and the final failure rule. | Concise-writing skill |
| `CW-03` | Remove cross-section duplication without losing recipient or reissue requirements. | Concise-writing skill |
| `CW-04` | Collapse unnecessary one-sentence sections while preserving timeout, warning, activity, and recovery facts. | Concise-writing skill |
| `CW-05` | Remove unsupported elaboration while preserving the authoritative archive facts. | Concise-writing skill |
| `CW-06` | Remove emphasis and hedge inflation without weakening the API-key rule. | Concise-writing skill |
| `CW-07` | Complete a direct concise-writing task with the complete repository skill bundle and no project state. | All nine repository skills |
| `CW-08` | Apply concise writing to policy prose while preserving every protected eligibility, deadline, accommodation, appeal, and navigation fact. | Concise-writing skill |
| `CW-09` | Co-select concise writing and writing-skills for skill-description prose while excluding an unrelated candidate. | Three description extractions |
| `CW-10` | Extract the skill-authoring ownership and validation sentence from the concise-writing contract. | Concise-writing skill |
| `CW-11` | Co-select concise writing and writing-skills for reference prose while excluding an unrelated candidate. | Three description extractions |
| `CW-12` | Extract the reference-authoring ownership and validation sentence from the concise-writing contract. | Concise-writing skill |
| `CW-13` | Route a pressured discipline-skill edit through the skill-authoring lifecycle and its required validation. | Concise-writing skill and pinned writing-skills bundle |
| `CW-14` | Route a pressured supporting-reference edit through the reference-authoring lifecycle and its required validation. | Concise-writing skill and pinned writing-skills bundle |
| `CW-17` | Preserve the response-only detailed-explanation exemption at discovery and contract-application boundaries. | Three description extractions and concise-writing skill |
| `CW-18` | Keep detailed project-file prose in scope despite an accompanying brief response. | Three description extractions and concise-writing skill |
| `CW-19` | Tighten a coupled cutover runbook without losing actors, exact thresholds and complements, ordering, boundaries, or rationales. | Concise-writing skill |

`CW-09` is the sole smoke representative. It preserves the prior runner-shape
representative choice and exercises the descriptions-only package end to end.
Provider-free acceptance prepares the complete-skill, full-bundle, composition,
and mixed description-plus-skill packages; the smoke does not duplicate those
package checks.

### Canonical prompts, adapted prompts, and rubrics

Hashes are SHA-256 over complete file bytes, including the trailing LF. Source
the active prompt and rubric bytes from `skill-validation/concise-writing.md` at
the canonical commit. For `CW-08`, use only the active repaired fixture. For
`CW-19`, use only the active threshold-exact prompt and active whole-artifact
rubric. Do not package either scenario's superseded arms or historical results.

| ID | Canonical prompt | Adapted `prompt.md` | `rubric.md` |
|---|---|---|---|
| `CW-01` | `4e7792ea8ac4263d16b3f1146ced377aa9e20449e39682ba52d33f08a1c0130d` | `cf7b9fdcd21a35856f1c7a038a6fbd21a85af76258fd476910c2b512fed47c46` | `e47a1f2fd9b764ab14d2932e6dbb90d6f7980aedc21221e89b887c3534c62023` |
| `CW-02` | `ccafa89503b43d4b942e99b21980b03a4d2c715bbd7489c9752e95055161095c` | `6c6580ec1557f10443d33ed09a7497cebce72195ee74bb303901d98ef48db58b` | `c06e93ca8405b8b4b23b2202d1701500b390f5d4dd08e3e4695158e05533a15f` |
| `CW-03` | `a1b1f041a90a8a354641af0dbf023932627d2a0082ced1ca806c828420174b2b` | `55bc07ef88d4c5e0a1e1fd23f12958ad5982d4424caaaf5c8d68bc17528e1067` | `1169ca9f3da8ddd7d38eb0d19b49efa1871e278a0e018e91b0d684a8b27f4209` |
| `CW-04` | `4b2d388630a8bbace61cbd7ff21d59c7a0169a32e639580333e7fd53000325cd` | `eb27f4a55d0ad55776f9394a606f5b08eb9be13b97df6ec1070d26faea28f288` | `b4984fce2d5f3c64e42dec68eb3c91ef03f4fb34a78bb387772581f88d4d8d8f` |
| `CW-05` | `7c160d51e4a7beb631eb3b7bdbf03450fde3c7ed5b43daac4334f2f7d400aad2` | `05393026ca0f4f79d7b96b57bb657fd6d16d947f3a98f612c0f329d93b80fe2e` | `7bf4622337380149543e332d847581d03fc9ac6f9b813c0cb1dd42f8b3109f0a` |
| `CW-06` | `fb5a28a627984da23515ba7e8e285ff0e6c6c930238e8764d5ec51c0b92f04e6` | `ec25b3eeb1e4f165f86cb43c558096ec7291f584d11b771442bf93f9a48edd85` | `6f1efa16316f4ba1a3bd8fb986e87564457d6a941216388fa307e33d37a1e7ed` |
| `CW-07` | `a4b3e375413cc29e72e4453a0893c1b837146c1fb75e116171ed481a74b6eea0` | `82cd1c8bcce6b726ab9e6d180d94879527c8b80fa304ff66547fa7fc1184faa5` | `650c766f5943c63f17d64c3accb985400f635573347d74a52f6a6ff3b7f3d913` |
| `CW-08` | `4b6ab5d5c4ed1ebd32a79709d6bf501b5c3f20486fbff2528a8adae72fd7aa24` | `91db2173ab9bb9a8251c3571fdf26bf485e4d527ce92987d89e2c369a5b3b29b` | `8247b6191ecda18cbeff074b59a530552355cb5ed3096e3b5cc0f24bd431d965` |
| `CW-09` | `e7adf2a882598587029a14ba737da4a4aa87c1c5f57106f767f04c6e78584bf9` | `169a425529c0cfb5f0c77bcc99ef63e41244b94b46b068c83d48e491d9c17f16` | `efbc83413fa8b192f39b2716ab5985d1bb8fd3664c8de54679fcc5406dab4dcd` |
| `CW-10` | `f00b3425ec1588155069f04962f22afe92f862568160979ad2c85f85f41a9544` | `d89691bec1d5ee09531e65c1e2a5785e409196c118ce9ae76b708627e4852b35` | `de115b7fd44df81f6b30885d463cbc31103ab263e919d3ae824e10187ab034ac` |
| `CW-11` | `b89cf931f0d75c1022d6b874c5c3e3e34a82b1ee9b34396528fa5a1e8454d54a` | `e902d1c5395512c068a77f5fcbb405a23a0cfdcb55ef63887e8c0741acd9312f` | `efbc83413fa8b192f39b2716ab5985d1bb8fd3664c8de54679fcc5406dab4dcd` |
| `CW-12` | `33b1302cd5bf10156ddc3b1c6259f59106fe869721812a6ebecfc83f6e208381` | `f492f92ceb4a00753557f9d7365715694bd56deea9a45d320f48fdf1844cf7b6` | `de115b7fd44df81f6b30885d463cbc31103ab263e919d3ae824e10187ab034ac` |
| `CW-13` | `a57330a86402aeb6e944f366b6acc5c5587ec8d06b04ffdc3d34544118f838c5` | `192c46c6f4650f42458aa93782f5aebbec422d9aa520e78d8f66adb2050983f7` | `d11f9d58c025f3dbd510c525ed3ab6989e54e3fe8ab6e0b99b4ab43c6990ede1` |
| `CW-14` | `d17569ae7715122477757c3127eadde6f4fa1cdea47fa59b4f708826b54b7378` | `8ccb4f0d0aa82c2c06d3c861c153e93161e32f4580dd41706273010acd9339d9` | `d11f9d58c025f3dbd510c525ed3ab6989e54e3fe8ab6e0b99b4ab43c6990ede1` |
| `CW-17` | `104bec538e19042df446ee64f25bc8bc67c2c8275485226b146dcfd5cdef99b8` | `041117e026c2b823db8c21beb482f91da91822c4552e03c084be54e912ca180c` | `2e4adaaa5385e133ef49fc6ebf7e19f1da03b43b6573a339c4bf2728ee7af3dd` |
| `CW-18` | `1ce35dc1fb3b5aa041c13597b26819509220d07bba4305e21bbfbb0f254c3d5b` | `b7fb1df8a6a8343004b0f5ccf5460a2abe94a26e058be5fb3ab3c6344a597376` | `6fd04eec5bb22a2a61fe031a0d59edfb85de109fda1a366a096afb40995a6d9e` |
| `CW-19` | `e05ab6e083289579573eb08c51213acdc9c81e7a189c1c10841b0b331742ae14` | `df33a3add2dc4ad6445076a381e35be307c35fdfbc50426fd0db4072a10b26b3` | `8c7ae23faa8adaa35090b9f78e8b40eaf245687982378b19fd8873b2aa646c07` |

Catalog acceptance does not audit rubric contents. Rubric hashes guide exact
materialization and review only.

### Prompt adaptations

Start from the active canonical prompt bytes and make only these literal
substitutions. Preserve all other bytes and the trailing LF.

| IDs | Literal substitutions |
|---|---|
| `CW-01`–`CW-06`, `CW-08`, `CW-10`, `CW-12`, `CW-19` | Prefix the backticked `skills/concise-writing/SKILL.md` path with `{{fixture_dir}}/`. |
| `CW-07` | Prefix the backticked concise-writing path with `{{fixture_dir}}/`; replace `The complete local skill bundle is installed,` with `The complete local skill bundle is supplied beneath \`{{fixture_dir}}/skills\`,`. |
| `CW-09`, `CW-11` | Prefix each of the three backticked `descriptions/` paths with `{{fixture_dir}}/`. |
| `CW-13`, `CW-14` | Replace `Read every supplied file completely.` with `Read every file beneath \`{{fixture_dir}}\` completely.`; prefix the backticked writing-skills and test-driven-development paths with `{{fixture_dir}}/`. |
| `CW-17`, `CW-18` | Prefix the three backticked `descriptions/` paths and the backticked concise-writing path with `{{fixture_dir}}/`. |

These substitutions expose already-supplied inputs at schema `"0.2"` paths.
They add no task, output, artifact, or evaluation requirement.

### Fixture mappings

Use these current live repository mappings where the package table names them:

| Label | Source relative to the scenario package | Provider target |
|---|---|---|
| `review-loop` | `../../../../skills/adversarial-review-loop/SKILL.md` | `skills/adversarial-review-loop/SKILL.md` |
| `review` | `../../../../skills/adversarial-review/SKILL.md` | `skills/adversarial-review/SKILL.md` |
| `concise` | `../../../../skills/concise-writing/SKILL.md` | `skills/concise-writing/SKILL.md` |
| `parent` | `../../../../skills/disciplined-development/SKILL.md` | `skills/disciplined-development/SKILL.md` |
| `research` | `../../../../skills/disciplined-research/SKILL.md` | `skills/disciplined-research/SKILL.md` |
| `dispatch` | `../../../../skills/dispatching-development-subagents/SKILL.md` | `skills/dispatching-development-subagents/SKILL.md` |
| `lean-plan` | `../../../../skills/lean-plan-writing/SKILL.md` | `skills/lean-plan-writing/SKILL.md` |
| `sweep` | `../../../../skills/sweeping-stale-references/SKILL.md` | `skills/sweeping-stale-references/SKILL.md` |
| `rationale` | `../../../../skills/writing-explicit-rationale/SKILL.md` | `skills/writing-explicit-rationale/SKILL.md` |

Materialize only the following package-owned inputs in each scenario that names
them. The description files are the one-line frontmatter description extraction,
including its final LF. `desc-review-loop` and `desc-concise` derive from the
named live repository sources; `desc-writing` and the complete external files
derive from the installed Superpowers `6.3.0` paths. Stop on any hash mismatch.

| Label | Origin | Package source -> provider target | SHA-256 |
|---|---|---|---|
| `desc-review-loop` | `skills/adversarial-review-loop/SKILL.md` frontmatter | `fixture/descriptions/adversarial-review-loop.txt` -> `descriptions/adversarial-review-loop.txt` | `38843f7718501f52116bfd4f95a6640cb16b560851767df540c808a1ed18cefa` |
| `desc-concise` | `skills/concise-writing/SKILL.md` frontmatter | `fixture/descriptions/concise-writing.txt` -> `descriptions/concise-writing.txt` | `586a741a9cb28746078ca1b5f7aa570a4e621a5d2cdecac16e31bd6d2c82fd62` |
| `desc-writing` | `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-skills/SKILL.md` frontmatter | `fixture/descriptions/superpowers-writing-skills.txt` -> `descriptions/superpowers-writing-skills.txt` | `5504b0825ec458aa8c20e9a55c6a932b36849e261a97aaf98af366e19a937154` |
| `writing-skills` | `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-skills/SKILL.md` | `fixture/skills/writing-skills/SKILL.md` -> `skills/writing-skills/SKILL.md` | `d34db5c8aed6a4e0440132bd0613aace70a693ec7819d5637ad77481d8e10d1b` |
| `writing-tests` | `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-skills/testing-skills-with-subagents.md` | `fixture/skills/writing-skills/testing-skills-with-subagents.md` -> `skills/writing-skills/testing-skills-with-subagents.md` | `c711346852c911b24a84aa161e0cff06a4cd7f4e2fa9e9c0a266cead5afcbade` |
| `tdd` | `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/test-driven-development/SKILL.md` | `fixture/skills/test-driven-development/SKILL.md` -> `skills/test-driven-development/SKILL.md` | `bf1b8216e523851a411e91d429a7c1c2a173e79d88957bc78e348218d50edd54` |

Declare mappings in the listed order:

| IDs | Ordered fixture labels |
|---|---|
| `CW-01`–`CW-06`, `CW-08`, `CW-10`, `CW-12`, `CW-19` | `concise` |
| `CW-07` | `concise`, `review-loop`, `review`, `parent`, `research`, `dispatch`, `lean-plan`, `sweep`, `rationale` |
| `CW-09`, `CW-11` | `desc-review-loop`, `desc-concise`, `desc-writing` |
| `CW-13`, `CW-14` | `concise`, `writing-skills`, `writing-tests`, `tdd` |
| `CW-17`, `CW-18` | `desc-review-loop`, `desc-concise`, `desc-writing`, `concise` |

Each descriptions package stores its own three exact extraction files, and
`CW-13` and `CW-14` each store their own three complete Superpowers files.
Duplication is deliberate because the migration design prohibits shared storage
and requires package-owned inputs beneath each owning package.

### Package records

Before the smoke, every package contains `README.md`, `prompt.md`, `rubric.md`,
and `test.json`, plus only its declared `fixture/` files. Each README records the
scenario purpose, input provenance and mappings, prompt adaptations, and that no
schema `"0.2"` result is retained. After the smoke, only `CW-09` may contain and
link `smoke-result.json`; its README reports only the runner's mechanical status.

## Catalog acceptance

Create `skill-validation/runner/acceptance/test_concise_writing_catalog.py`.
Keep catalog data and any small local helpers in that file. It verifies only:

- exactly the seventeen planned scenario directories and their exact package
  files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- adapted prompt bytes against the hashes above;
- exact fixture sources, targets, derived description bytes, and pinned external
  dependency bytes;
- resolved prompt tokens and no stale `supplied-skills/` path;
- absence of rubric bytes from declared and prepared provider input; and
- an empty initial evidence directory.

Permit only `CW-09` to add optional `smoke-result.json` after acceptance is
established. Redirect the runner's temporary root to pytest's `tmp_path` so
preparation leaves no run bundle outside the test directory.

Acceptance does not invoke a provider or validate README prose, rubric content,
configuration authoring choices, smoke results, response or result schemas,
stdout, stderr, provider artifacts, evaluator behavior, or behavioral outcomes.
It does not reconstruct a result, add a negative-test matrix, or add shared
machinery. These are accepted, unexamined edges outside this migration.

## Verification

After package acceptance is implemented, run from `skill-validation/runner`:

```bash
uv run pytest -q acceptance/test_concise_writing_catalog.py
uv run pytest -q
```

After the smoke record and index update, rerun only the focused acceptance test
because those changes do not alter package preparation. If internal-review
repairs change a package or acceptance behavior, rerun both commands; otherwise
rerun only the affected check. Do not add another verifier or run unrelated skill
test suites.

## Task 1: Package all seventeen scenarios

**Files:** Create the seventeen packages and only their declared package-owned
fixtures.

**Boundary:** Stop on a missing source, hash mismatch, malformed configuration,
required unlisted adaptation, or unsupported package shape.

- Materialize every adapted prompt, exact rubric, description extraction, and
  package-local external dependency from the sources above.
- Create every schema `"0.2"` configuration and minimal scenario README with
  exactly the declared mappings.
- Confirm the package diff contains no runner, provider, schema, skill,
  shared-helper, other-catalog, superseded-arm, or historical-result material.

## Task 2: Add catalog acceptance and verify preparation

**Files:** Create
`skill-validation/runner/acceptance/test_concise_writing_catalog.py`.

**Boundary:** Provider behavior and result content remain accepted, unexamined
edges. Do not add output checks, result checks, mutations, negative matrices, or
shared helpers.

- Implement exactly the catalog-local acceptance contract above.
- Run the focused acceptance test and complete offline runner suite once.
- Review the test against the package-only boundary.

## Smoke approval gate

- Report package state plus focused and full offline verification.
- Obtain explicit owner approval for exactly one Codex `CW-09` invocation. Do
  not treat plan approval or implementation approval as smoke approval.

## Task 3: Run and record the representative smoke

**Files:** Create
`skill-validation/scenarios/concise-writing/cw-09/smoke-result.json` only if the
runner publishes `result.json`. Modify the `CW-09` README in every outcome;
modify the scenario migration index only after `COMPLETED`.

**Boundary:** Missing output or any status other than `COMPLETED` stops the
catalog without retry. Response meaning, rubric satisfaction, stdout/stderr,
artifact inventories, result schemas, and result reconstruction remain
unexamined.

- From `skill-validation/runner`, invoke exactly once:
  `uv run skilltest run ../scenarios/concise-writing/cw-09/test.json`. Do not
  retry or run another scenario.
- If the runner publishes `result.json`, retain its exact bytes as
  `cw-09/smoke-result.json`. If no result is published, remove any prior retained
  result.
- Read only the runner-written mechanical status needed for disposition. Do not
  compare the retained file with the run bundle or validate another result field.
- Record the mechanical outcome in the `CW-09` README and remove the owned
  temporary run directory. Retain no other run artifact.
- If status is `COMPLETED`, add the catalog's seventeen README links and `CW-09`
  representative marker to the migration index; update this catalog to 17/17 and
  overall totals to 90/105.
- If no result is retained or status is not `COMPLETED`, leave the index
  unchanged; rerun focused acceptance and stop for owner direction.
- For `COMPLETED`, rerun focused acceptance and review only the smoke record,
  README, and index update.

## Controller review and final approval gate

- Review the complete catalog against the governing design and this plan.
  Confirm the final implementation diff is limited to the seventeen packages,
  their catalog-local acceptance test, and the migration index.
- Confirm that no response judgment, output or result validation,
  runner/provider/schema/skill change, shared helper, lifecycle machinery,
  superseded or historical material, or unrelated bookkeeping entered the work.
- Address only verified in-scope findings and rerun only checks affected by
  repairs.
- Report implementation commits, focused and full offline verification, the one
  smoke attempt and retained mechanical status, and internal-review disposition.
- Stop and obtain explicit owner approval before merge, push, plan archive,
  roadmap update, worktree/branch removal, or next-catalog planning.

## Post-approval closeout

- Merge the feature branch into local `main`.
- On `main`, check the `concise-writing` roadmap item and move this plan to
  `plans/completed/`, adjusting its three header links for the new location,
  then commit the closeout.
- Push `main`, then remove this catalog's worktree and local feature branch. Do
  not create the next catalog plan without separate owner approval.

## Done when

- All seventeen packages pass catalog acceptance and the complete offline runner
  suite.
- One owner-approved `CW-09` invocation retains the exact runner-produced
  `COMPLETED` result.
- The migration index reports 17/17 for this catalog and 90/105 overall.
- Internal review passes without output or result judgment and without extra
  migration scope.
- The owner approves closeout, local `main` contains the merged implementation
  and closeout commit, the plan is archived, the roadmap is checked, `main` is
  pushed, and the feature worktree and local branch are removed.
