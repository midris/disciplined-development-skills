# Dispatching Development Subagents Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** Use `superpowers:verification-before-completion`
> before completion claims. Stop at each owner approval gate named below.

**Goal:** Package all eleven active `dispatching-development-subagents`
scenarios for the schema `"0.2"` runner, prove that the runner can load and
prepare every package, and retain one completed representative smoke result.

**Architecture:** Each canonical prompt becomes one response-only package with
its evaluator-withheld rubric and exact supplied files. Current repository
skills are declared directly; canonical project files and the required pinned
Superpowers dependency are stored per package. `DSD-03` is the sole smoke
because it is the established minimal end-to-end catalog representative;
provider-free acceptance covers every package and fixture shape.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../skill-validation/scenarios/README.md).

## Global constraints

- Start from clean current `main` on branch
  `feature/dispatching-development-subagents-schema-02` in
  `.worktrees/dispatching-development-subagents-schema-02/`.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for scenario scope, prompt
  and rubric bytes, supplied-input representation, scenario-owned bytes, and
  scenario meaning.
- Package exactly `DSD-01` through `DSD-11` at
  `skill-validation/scenarios/dispatching-development-subagents/dsd-01/`
  through `dsd-11/`.
- Give each `test.json` exactly the schema `"0.2"` keys
  `schema_version`, `id`, `prompt`, `fixtures`, and `execution`; use its
  lowercase scenario ID and `"prompt":"prompt.md"`.
- Give every configuration
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"high"}`.
- Use current live repository skill files directly. Do not copy them into a
  package or pin their hashes as catalog requirements.
- Store canonical project files and each required external dependency beneath
  the owning package's `fixture/` directory. Do not create shared dependency
  storage.
- Apply only the literal path and read-instruction adaptations listed below.
  Preserve every other prompt byte and every rubric byte.
- Keep every scenario response-only. Do not use `{{evidence_dir}}`, request
  file changes, inspect response meaning, apply a rubric, or score a response.
- Add only the catalog-local acceptance test named below. Do not change the
  runner, provider, schema, skills, shared helpers, or another catalog.
- Do not invoke a provider until the owner explicitly approves one `DSD-03`
  attempt. After approval, invoke it once with no retry.
- Skip external review. The controller owns one internal catalog review.
- Stop if canonical scope, bytes, representation, or provenance is unavailable;
  the pinned dependency is unavailable or hash-mismatched; an unlisted prompt
  adaptation is required; or the current runner cannot load or prepare a
  package. Do not change the runner to accommodate the catalog.
- Do not merge or push implementation changes, archive this plan, update the
  roadmap, remove the feature branch or worktree, or create the next catalog
  plan before explicit owner approval at the final gate.

## Catalog definition

### Candidate inventory

| ID | Purpose | Supplied context |
|---|---|---|
| `DSD-01` | Produce one bounded development-subagent prompt with grounded scope, identity, authority, disclosure, and handoff requirements. | All nine repository skills and the `dsd-01` project files |
| `DSD-02` | Preserve subagent identity and verification duties under pressure to assume orchestrator gates and nested dispatch. | Dispatch, parent, research, hook, and upstream execution skills |
| `DSD-03` | Require commit-by-commit inspection and disposition of an out-of-scope commit before integration. | Dispatch skill |
| `DSD-04` | Partition mixed findings without paraphrasing, unsafe batching, or invented rationale. | Dispatch skill |
| `DSD-05` | Reconcile a development handoff and landed prose while keeping a no-commit research report outside the development boundary. | Dispatch skill and the `dsd-05` project files |
| `DSD-06` | Ground the factual finding, scope, constraints, and governing rereads in supplied project sources. | Dispatch skill and the `dsd-01` project files |
| `DSD-07` | State bounded subagent identity, authority, no-widening, and disclosure clauses. | Dispatch skill |
| `DSD-08` | Define returned-work verification and omit unsupported landed rationale. | Dispatch skill and the `dsd-05` project files |
| `DSD-09` | Resist promotion to orchestrator authority, nested reviewers, and parent-gate action. | Dispatch, parent, hook, and upstream execution skills |
| `DSD-10` | Order the subagent's own running-system verification before reporting the parent-owned review gate and stopping. | Dispatch, parent, and hook files |
| `DSD-11` | Require research and precise source mapping for dispatch and post-hook factual claims. | Dispatch, parent, hook, and upstream execution skills |

`DSD-03` is the sole smoke representative. It preserves the catalog's prior
representative choice and proves the end-to-end runner path with the smallest
fixture set. Provider-free acceptance prepares the fixture-bearing and
multi-skill packages; the smoke does not duplicate those package checks.

### Canonical prompts, adapted prompts, and rubrics

Hashes are SHA-256 over complete file bytes, including the trailing LF. Source
each prompt and rubric from
`skill-validation/fixtures/dispatching-development-subagents/prompts/` and
`rubrics/` at the canonical commit.

| ID | Canonical prompt | Adapted `prompt.md` | `rubric.md` |
|---|---|---|---|
| `DSD-01` | `b0d2273f25c29266f2e8aa1b75f6cc760aa6dc79d78f84f6fa8c3a7f82824ccb` | `6eedfdb6b17fce5af790c0fe9cd7dc967426ea6f911c4086a9ed1ade718bce09` | `acf3ade4ab145d91709ccbce6315fbb301bcb86cc8c5648932d839e0d98b13d0` |
| `DSD-02` | `750b43ea0d12d109c70e996578618da5d79717c2716b6878db0e4812a5226c4c` | `d4c03e13a68a7c25a480d07dfb075e7b23d2bbda79d330ce00a3d52b92054cca` | `ac3e61476eca2010dd37143b3ac942f392fa333c695fa98c1a68330a08237bb5` |
| `DSD-03` | `6e99e94ce865c2102799474225fa8ee500440d013d30b9a853951663b3ee0d70` | `e0e07f5e26930a58a6741c3f1e3ad900f2bcc362ff4c688ff554b8ccbd040e7b` | `c7b3fbf6eb092f8919cd8ec1eaa278af7f736f4fa1522bbb8e56bc536aab6570` |
| `DSD-04` | `31a5cbe423d9bd9531cc2706de2f9372d13af5bb142db5320e8887cb75ab2dfe` | `9637da4d3e05acf47034ff063c5e41193ccb0192fc2f31ed6bfbe2705ed8993c` | `dc29adc91e29ca32bae2fe3a8df3ba1a7cac3293add9eec2e77b7aeecaebd25b` |
| `DSD-05` | `5917fa9a572dd8ecce515b4728b946754bd00233655ebf0d505ef26b5ea98f33` | `4b0f1c15850a20e191dd060396153adf24492d791a67f2cd68aad2e29322f74a` | `fc5d43057ffdb3055d2fbd20dba98f594ac3a654807132e5b768e8651f8b0d6b` |
| `DSD-06` | `dce91ca050fb7e1cc3cad40d53b2df65c37c9184dc06fb0cb38a97190d672171` | `6a182459ece79f7696e18b43a891b9441c548a992814f9862729ea3bb96f7469` | `72246ee567b9c0353817a58d85f8ec632dd6bf89c59dbcffcc14e1fe12699769` |
| `DSD-07` | `366f109c8570927dec22908def32f52ff3f2119c116913666a7386d021b817a2` | `cd4b9b14c2deea0ea019bd3ce8ed5e85948fbbc97bcdf7f346e794b32106464b` | `50e6f2c823ff942820f99c659d2f660230359d380edc9ffa99048c6c05243d86` |
| `DSD-08` | `a08ec853a3a904b198c66667a8df8f85e5b3c60526d217878758d01b1ceb3cda` | `43ac03009dd981bcc6633d75d21921fe496fb8d69c57629711a341ac666aae6c` | `9a320803e86b35e3c0b8ab339714803e227a9da0c9529f2d453068928a2ed135` |
| `DSD-09` | `c46e94834202e37346cf031b9ed320c719d4e3b57e005a538cc055e0acff4653` | `81beafb72ff9e9e89bdb76a1c9a24b3e1cdf5a26ab84b7ae80c16113749f4b87` | `87af699d793adfda35cf2a74114e632893bd668cc66aa4c5c14018469da5481c` |
| `DSD-10` | `cc6f0089b32768684ac28d15d41ee73f786a46f15953d48ce8719ad5bd05e69c` | `f56340c6ba819155105644881da386e04ff09f80178bf953d338a1dee06e7a2e` | `a4420e154601b7f6f53741165680cfafc4a9e6add569fbdd703537b1c9d3ff3e` |
| `DSD-11` | `10ddcdc963eae9cc10c5445acd61fe93d0618341141000cc76ee41f94c36fb52` | `2d1ad2701ed71a224e10a4ebdb9aba4ef1c65e8e999212290f06558c055a34a1` | `eaa14d182248e0267bef934c3307a782a14836848b453a7690df1b4a11e615df` |

Catalog acceptance does not audit rubric contents. Rubric hashes guide exact
materialization and review only.

### Prompt adaptations

Start from the canonical prompt bytes and make only these literal
substitutions. Preserve all other bytes and the trailing LF.

| IDs | Literal substitutions |
|---|---|
| `DSD-01` | Prefix every backticked `skills/` and `project/dsd-01` path with `{{fixture_dir}}/`. |
| `DSD-02` | Prefix each of the four backticked skill and hook paths in the supplied-file list with `{{fixture_dir}}/`. |
| `DSD-03`, `DSD-04` | Prefix the backticked dispatch `SKILL.md` path with `{{fixture_dir}}/`. |
| `DSD-05` | Prefix the backticked dispatch `SKILL.md` and `project/dsd-05/` paths with `{{fixture_dir}}/`. |
| `DSD-06` | Replace `Invoke \`dispatching-development-subagents\` directly and read it completely.` with `Read \`{{fixture_dir}}/skills/dispatching-development-subagents/SKILL.md\` completely.`; prefix the backticked `project/dsd-01/AGENTS.md` path with `{{fixture_dir}}/`. |
| `DSD-07` | Apply the `DSD-06` dispatch-read substitution. |
| `DSD-08` | Apply the `DSD-06` dispatch-read substitution; prefix the backticked `project/dsd-05` directory with `{{fixture_dir}}/`. |
| `DSD-09`, `DSD-10` | Apply the `DSD-06` dispatch-read substitution and the exact parent-and-hook substitution below. |
| `DSD-11` | Apply the `DSD-06` dispatch-read substitution and the exact parent-hook-and-upstream substitution below. |

For the `DSD-09` and `DSD-10` parent-and-hook substitution, replace these
exact two lines:

```text
Read the
supplied parent and hook files.
```

with these exact two lines:

```text
Read `{{fixture_dir}}/skills/disciplined-development/SKILL.md` and
`{{fixture_dir}}/skills/disciplined-development/hooks/review_nudge.py` completely.
```

For the `DSD-11` parent-hook-and-upstream substitution, replace these exact
two lines:

```text
Read the
supplied parent, hook, and upstream subagent files.
```

with these exact three lines:

```text
Read `{{fixture_dir}}/skills/disciplined-development/SKILL.md`,
`{{fixture_dir}}/skills/disciplined-development/hooks/review_nudge.py`, and
`{{fixture_dir}}/skills/superpowers/subagent-driven-development/SKILL.md` completely.
```

These substitutions expose already-supplied inputs at schema `"0.2"` paths.
They add no task, output, artifact, or evaluation requirement.

### Fixture mappings

Use these live repository mappings where the scenario table below names them:

| Label | Source relative to the scenario package | Provider target |
|---|---|---|
| `dispatch` | `../../../../skills/dispatching-development-subagents/SKILL.md` | `skills/dispatching-development-subagents/SKILL.md` |
| `review-loop` | `../../../../skills/adversarial-review-loop/SKILL.md` | `skills/adversarial-review-loop/SKILL.md` |
| `review` | `../../../../skills/adversarial-review/SKILL.md` | `skills/adversarial-review/SKILL.md` |
| `concise` | `../../../../skills/concise-writing/SKILL.md` | `skills/concise-writing/SKILL.md` |
| `parent` | `../../../../skills/disciplined-development/SKILL.md` | `skills/disciplined-development/SKILL.md` |
| `hook` | `../../../../skills/disciplined-development/hooks/review_nudge.py` | `skills/disciplined-development/hooks/review_nudge.py` |
| `research` | `../../../../skills/disciplined-research/SKILL.md` | `skills/disciplined-research/SKILL.md` |
| `lean-plan` | `../../../../skills/lean-plan-writing/SKILL.md` | `skills/lean-plan-writing/SKILL.md` |
| `sweep` | `../../../../skills/sweeping-stale-references/SKILL.md` | `skills/sweeping-stale-references/SKILL.md` |
| `rationale` | `../../../../skills/writing-explicit-rationale/SKILL.md` | `skills/writing-explicit-rationale/SKILL.md` |

Materialize these package-owned mappings only in scenarios that name them.
Copy each `p01-*` and `p05-*` origin from the canonical commit. Copy `upstream`
from the installed Superpowers `6.3.0` path shown below. Stop on any hash
mismatch.

| Label | Origin | Package source -> provider target | SHA-256 |
|---|---|---|---|
| `p01-agents` | `skill-validation/fixtures/dispatching-development-subagents/project/dsd-01/AGENTS.md` | `fixture/project/dsd-01/AGENTS.md` -> `project/dsd-01/AGENTS.md` | `567ded3276c9ecaabbfea7f34229a528652476cf2cfe1f7a81573b4577c866fe` |
| `p01-plan` | `skill-validation/fixtures/dispatching-development-subagents/project/dsd-01/plans/pagination.md` | `fixture/project/dsd-01/plans/pagination.md` -> `project/dsd-01/plans/pagination.md` | `e18ce80cae7233db26ed903116fee411162433d2ef82cfbcfa574835efcf35c4` |
| `p01-review` | `skill-validation/fixtures/dispatching-development-subagents/project/dsd-01/reviews/pagination.md` | `fixture/project/dsd-01/reviews/pagination.md` -> `project/dsd-01/reviews/pagination.md` | `884e1ee1a6c7109134144ff3ab1cddf6bd9bd522a249373e4ce7e1571b77a80a` |
| `p05-prose` | `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/landed-prose.md` | `fixture/project/dsd-05/landed-prose.md` -> `project/dsd-05/landed-prose.md` | `dc1c4a0881580f5a883d126ddcbc00b70dfd3e226129e44aa6ed06381fbc4aae` |
| `p05-research` | `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/research-report.md` | `fixture/project/dsd-05/research-report.md` -> `project/dsd-05/research-report.md` | `0d7d31036a68767b0a586b7aad0c228999316c6463dfd39009f8d7e7131360d5` |
| `p05-handoff` | `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/returned-handoff.md` | `fixture/project/dsd-05/returned-handoff.md` -> `project/dsd-05/returned-handoff.md` | `1c9f3979e4a123c584f3ddd072f6869df6a241adca1c4da4cc484b8f6815ecab` |
| `p05-source` | `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/src/request_config.py` | `fixture/project/dsd-05/src/request_config.py` -> `project/dsd-05/src/request_config.py` | `f0ff7ba51f0b758aea2f9b248c754f832dd57c6d2110036a80f886690ecdee6c` |
| `p05-tests` | `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/test-output.txt` | `fixture/project/dsd-05/test-output.txt` -> `project/dsd-05/test-output.txt` | `dbff34df084976e0006cd15b2bd1cf6e3b5419b626c19f0030544a1c174ec3d7` |
| `upstream` | `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/subagent-driven-development/SKILL.md` | `fixture/skills/superpowers/subagent-driven-development/SKILL.md` -> `skills/superpowers/subagent-driven-development/SKILL.md` | `8dd1b8e698edec3700c6d89517dbe96febd3bacd3f6ea21c1a3569c62ea104b5` |

Declare mappings in the listed order:

| IDs | Ordered fixture labels |
|---|---|
| `DSD-01` | `dispatch`, `review-loop`, `review`, `concise`, `parent`, `research`, `lean-plan`, `sweep`, `rationale`, `p01-agents`, `p01-plan`, `p01-review` |
| `DSD-02` | `dispatch`, `parent`, `hook`, `research`, `upstream` |
| `DSD-03`, `DSD-04`, `DSD-07` | `dispatch` |
| `DSD-05`, `DSD-08` | `dispatch`, `p05-prose`, `p05-research`, `p05-handoff`, `p05-source`, `p05-tests` |
| `DSD-06` | `dispatch`, `p01-agents`, `p01-plan`, `p01-review` |
| `DSD-09`, `DSD-11` | `dispatch`, `parent`, `hook`, `upstream` |
| `DSD-10` | `dispatch`, `parent`, `hook` |

`DSD-02`, `DSD-09`, and `DSD-11` each store their own exact `upstream`
copy. Duplication is deliberate because the migration design prohibits shared
dependency storage and requires external dependencies beneath each owning
package.

### Package records

Before the smoke, every package contains `README.md`, `prompt.md`, `rubric.md`,
and `test.json`, plus only its declared `fixture/` files. Each README records
the scenario purpose, input provenance and mappings, prompt adaptations, and
that no schema `"0.2"` result is retained. After the smoke, only `DSD-03` may
contain and link `smoke-result.json`; its README reports only the runner's
mechanical status.

## Catalog acceptance

Create
`skill-validation/runner/acceptance/test_dispatching_development_subagents_catalog.py`.
Keep catalog data and any small local helpers in that file. It verifies only:

- exactly the eleven planned scenario directories and their exact package
  files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- adapted prompt bytes against the hashes above;
- exact fixture sources, targets, copied canonical bytes, and pinned dependency
  bytes;
- resolved prompt tokens and no stale `supplied-skills/` path;
- absence of rubric bytes from declared and prepared provider input; and
- an empty initial evidence directory.

Permit only `DSD-03` to add optional `smoke-result.json` after acceptance is
established. Redirect the runner's temporary root to pytest's `tmp_path` so
preparation leaves no run bundle outside the test directory.

Acceptance does not invoke a provider or validate README prose, rubric content,
configuration authoring choices, smoke results, response or result schemas,
stdout, stderr, provider artifacts, evaluator behavior, or behavioral outcomes.
It does not reconstruct a result, add a negative-test matrix, or add shared
machinery. These are accepted, unexamined edges outside this migration.

## Verification

After package acceptance is implemented, run from
`skill-validation/runner`:

```bash
uv run pytest -q acceptance/test_dispatching_development_subagents_catalog.py
uv run pytest -q
```

After the smoke record and index update, rerun only the focused acceptance test
because those changes do not alter package preparation. If internal-review
repairs change a package or acceptance behavior, rerun both commands; otherwise
rerun only the affected check. Do not add another verifier or run unrelated
skill test suites.

## Task 1: Package all eleven scenarios

**Files:** Create the eleven packages and their package-owned fixtures.

**Boundary:** Stop on a missing source, hash mismatch, malformed
configuration, required unlisted adaptation, or unsupported package shape.

- Materialize every adapted prompt, exact rubric, canonical project file,
  and package-local upstream dependency from the sources above.
- Create every schema `"0.2"` configuration and minimal scenario README
  with exactly the declared mappings.
- Confirm the package diff contains no runner, provider, schema, skill,
  shared-helper, other-catalog, or historical replay material.
- Commit only the eleven scenario packages.

## Task 2: Add catalog acceptance and verify preparation

**Files:** Create
`skill-validation/runner/acceptance/test_dispatching_development_subagents_catalog.py`.

**Boundary:** Provider behavior and result content remain accepted, unexamined
edges. Do not add output checks, result checks, mutations, negative matrices,
or shared helpers.

- Implement exactly the catalog-local acceptance contract above.
- Run the focused acceptance test and complete offline runner suite once.
- Review the test against the package-only boundary and commit it.

## Smoke approval gate

- Report the package and acceptance commits plus focused and full offline
  verification.
- Obtain explicit owner approval for exactly one Codex `DSD-03` invocation.
  Do not treat plan approval or implementation approval as smoke approval.

## Task 3: Run and record the representative smoke

**Files:** Create
`skill-validation/scenarios/dispatching-development-subagents/dsd-03/smoke-result.json`
only if the runner publishes `result.json`. Modify the `DSD-03` README in every
outcome; modify the scenario migration index only after `COMPLETED`.

**Boundary:** Missing output or any status other than `COMPLETED` stops the
catalog without retry. Response meaning, rubric satisfaction, stdout/stderr,
artifact inventories, result schemas, and result reconstruction remain
unexamined.

- From `skill-validation/runner`, invoke exactly once:
  `uv run skilltest run ../scenarios/dispatching-development-subagents/dsd-03/test.json`.
  Do not retry or run another scenario.
- If the runner publishes `result.json`, retain its exact bytes as
  `dsd-03/smoke-result.json`. If no result is published, remove any prior
  retained result.
- Read only the runner-written mechanical status needed for disposition.
  Do not compare the retained file with the run bundle or validate another
  result field.
- Record the mechanical outcome in the `DSD-03` README and remove the
  owned temporary run directory. Retain no other run artifact.
- If status is `COMPLETED`, add the catalog's eleven README links and
  `DSD-03` representative marker to the migration index; update this catalog to
  11/11 and overall totals to 73/105. Otherwise leave the index unchanged and
  stop for owner direction.
- Rerun focused acceptance and commit the smoke record, README, and index
  update.

## Controller review and final approval gate

- Review the complete catalog against the governing design and this plan.
  Confirm the final implementation diff is limited to the eleven packages,
  their catalog-local acceptance test, and the migration index.
- Confirm that no response judgment, result validation,
  runner/provider/schema/skill change, shared helper, lifecycle machinery,
  historical replay material, or unrelated bookkeeping entered the work.
- Address only verified in-scope findings and rerun only checks affected by
  repairs.
- Report implementation commits, focused and full offline verification,
  the one smoke attempt and retained mechanical status, and internal-review
  disposition.
- Stop and obtain explicit owner approval before merge, push, plan archive,
  roadmap update, worktree/branch removal, or next-catalog planning.

## Post-approval closeout

- Merge the feature branch into local `main`.
- On `main`, check the `dispatching-development-subagents` roadmap item and
  move this plan to `plans/completed/`, adjusting its three header links for
  the new location, then commit the closeout.
- Push `main`, then remove this catalog's worktree and local feature branch.
  Do not create the next catalog plan without separate owner approval.

## Done when

- All eleven packages pass catalog acceptance and the complete offline runner
  suite.
- One owner-approved `DSD-03` invocation retains the exact runner-produced
  `COMPLETED` result.
- The migration index reports 11/11 for this catalog and 73/105 overall.
- Internal review passes without output or result judgment and without extra
  migration process or bookkeeping.
- After owner approval, the catalog is merged and pushed, the roadmap and plan
  are closed, and the feature worktree and branch are removed.
