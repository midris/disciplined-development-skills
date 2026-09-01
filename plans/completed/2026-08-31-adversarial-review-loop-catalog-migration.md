# Adversarial Review Loop Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** Use `superpowers:verification-before-completion`
> before completion claims. Stop at the owner approval gate before merge or
> cleanup.

**Goal:** Package all fifteen active `adversarial-review-loop` scenarios for the
schema `"0.2"` runner, prove that the runner can load and prepare every package,
and retain one completed representative smoke result.

**Architecture:** Each canonical scenario becomes one self-contained package.
Current repository skills remain live fixture sources, while the tester-selected
Superpowers dependency required by `OWN` is copied into that package. `OWN` is
the sole representative smoke because it is the catalog's only mixed live-skill
and packaged-dependency composition; the larger nine-live-skill `T2` package is
covered by package preparation.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](../specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](../2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../../skill-validation/scenarios/README.md).

## Global constraints

- Start from current `main` on branch
  `feature/adversarial-review-loop-schema-02` in
  `.worktrees/adversarial-review-loop-schema-02/`.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for scenario scope,
  prompt and rubric material, supplied-input representation, and scenario
  meaning.
- Package exactly the fifteen IDs `CS`, `T2` through `T7`, `NF`, `PW`, `XL`,
  `G3A` through `G3C`, `OWN`, and `CE` at
  `skill-validation/scenarios/adversarial-review-loop/<lowercase-id>/`.
- Give each `test.json` exactly the schema `"0.2"` keys `schema_version`, `id`,
  `prompt`, `fixtures`, and `execution`; use its lowercase scenario ID and
  `"prompt":"prompt.md"`.
- Give every `test.json` the execution declaration
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"high"}`.
- Use current repository `SKILL.md` files directly as live fixture sources. Do
  not copy them into packages or pin their hashes.
- Copy the tester-selected Superpowers 6.3.0 dependency into the `OWN` package
  and preserve its bytes exactly. Do not reference its absolute installation
  path from `test.json`.
- Apply only the prompt substitutions listed below. Do not otherwise rewrite,
  clarify, reflow, or improve prompts or rubrics.
- Keep every scenario response-only. Do not use `{{evidence_dir}}`, request file
  changes, inspect response meaning, score a response, or validate result
  contents beyond the runner's mechanical status.
- Add only the catalog-local acceptance test named below. Do not change runner,
  provider, schema, skills, shared helpers, or other catalogs.
- The owner's standing approval covers the single Codex smoke invocation. Run
  only `OWN`, once, with no retry.
- Skip external review. The controller owns the internal catalog review.
- Stop if a canonical source is unavailable or hash-mismatched, the pinned
  dependency is unavailable or hash-mismatched, an unlisted adaptation is
  required, the existing runner cannot represent a package, or the smoke does
  not finish with runner status `COMPLETED`.
- Do not merge or push implementation changes, archive this plan, update the
  roadmap, remove the feature branch or worktree, or create the next catalog
  plan before new explicit owner approval.

## Catalog definition

### Candidate inventory

| ID | Purpose | Supplied context |
|---|---|---|
| `CS` | Treat recurrence after a one-line fix as evidence of an incomplete class sweep before re-review. | Live loop skill only |
| `T2` | Keep a proven one-member class bounded and still require the safe reviewer re-run. | All nine live repository skills |
| `T3` | Take the memory-free cold-read escape after the third completed blocking cycle rather than starting a fourth cycle. | Live loop skill only |
| `T4` | Keep unrelated below-cap findings scattered and continue without inventing an umbrella axis. | Live loop skill only |
| `T5` | Treat a P3-only result as blocking-loop clean while disposing every P3 explicitly. | Live loop skill only |
| `T6` | Require the same-reviewer re-run after a complete self-sweep rather than self-certifying clean. | Live loop skill only |
| `T7` | Address a new blocking class rather than using class difference as a deferral or dismissal lever. | Live loop skill only |
| `NF` | Attack a visible below-cap error-contract invariant across its complete axis before re-review. | Live loop skill only |
| `PW` | Extend a shared-axis audit project-wide to uncited persistence components and paths. | Live loop skill only |
| `XL` | Translate one source-of-truth error invariant across all languages and code paths. | Live loop skill only |
| `G3A` | At cycle-3 entry, locate a shared pattern in governing text and record the verdict before fixing. | Live loop skill only |
| `G3B` | Permit a written no-shared-pattern cycle-3 verdict without over-firing a root attack. | Live loop skill only |
| `G3C` | Treat a cycle-3 re-raise as reviewer-side re-litigation, record a ruling, and dispose the P3 without appeasement. | Live loop skill only |
| `OWN` | Preserve individual-task and whole-branch owners, rules, and counters while grounding factual workflow claims. | Three live repository skills plus one packaged Superpowers dependency |
| `CE` | Route each cold-read outcome to its distinct stop, redo, or productive reset branch and record it. | Live loop skill only |

`OWN` is the sole smoke representative. It is the only package that combines
multiple live repository skills with a packaged external dependency, so it
exercises the catalog's distinctive provider-input shape. `T2` supplies more
live files, but the acceptance test loads and prepares that complete package
offline.

### Canonical prompts and rubrics

Hashes are SHA-256 over complete file bytes, including the trailing LF. Prompt
and rubric paths below are relative to `skill-validation/` at the canonical
source commit.

| ID | Canonical prompt SHA-256 | Canonical rubric SHA-256 | Adapted prompt SHA-256 |
|---|---|---|---|
| `CS` | `6bfbf05aa6a494295fe5e044f1ed8f45a38b0349c3fbafeeb5bc76df4877d788` | `587c543ecc82abdbde08123923e1c64aea77ca013d2a7a76ebe257f8c73989df` | `b96f0aaefa668aac0eee5f20201c63ebd8344a9203a6ab5c03585a19b96b1841` |
| `T2` | `157ab2e1d09d24e08c18ab4e826d847d00d96a322c4387769901480e0590a9be` | `5487fae2531b6153ee3f5d3d6fd399a5106326280f017d83accb14cd5eeaf2e9` | `14529087bab8b18168358b86084be236b5c13f2fd5fed696b7031c5f13dab891` |
| `T3` | `ef458a31071054126b7c6647a4f8859c71dc9416912c617b3f2d505fea5bea94` | `1c0f227ca974edc1a6c06e99a380f9a85c72c2b525fbb1d5c76330d23cd8a055` | `d66f70d475477c6e10da3b681425b0454f50b1c97129fcdb6cb65cf17b0c6a63` |
| `T4` | `d074f2aa8f0b156e0037feb5dc95e7c0b8598798fe4ec1e3fa5370c1a41808cb` | `4f329062dd03163cbbdcffc8cbf4e15fe695eceebe735183289e3609fa69cb76` | `2b6f8429b39b6f20699d765b9b9b0cf66b480d823431e18b9e40b1b8f28760b8` |
| `T5` | `179d134c24c22bd9dc8599ade9a3e6d5a625d3177a5596a7993a0275e5f9e739` | `469171a65d370542232776bc42ded0acf10e43f26375ec677d098cc3130b6749` | `53c86b99eeacc51312283b1de784cd040bcb3e7cc933fd3ef9a66a141335d457` |
| `T6` | `59177853e8e120996001a69366f022e703e89c52c1df50f0c766f0b40d878d47` | `36f660a1320fde68110f2b6c819d0adf52b032098d6b4eb69a2a3f8b1d009d62` | `f29ea03099bc61394149d31c3688b86961f305542ee529c8020a8e142fcb9c86` |
| `T7` | `3062673c9af2b2748007b44704347ff6a18058688be2f268d24cb326bb6f7179` | `21102b7487933fd8dce4a9f01579c083e38cef8cf57b0ac74749a950098420fe` | `d5b8352823ef6a17c163045ca2c9215bd3260f62aa4faca29ab45cd3347ce1ec` |
| `NF` | `6cb872779eb18d018ae9fb8d254e96c50c51a2a2a30540a16ade6220bdd333db` | `86756fd50bf95913fcab2e6234d71ec5189f3541bc20488461c072f2e4a183c8` | `088ecef309a869161c73eaa5eb0c9ed657e2b21b790b564d02e677eaccff7e02` |
| `PW` | `088e46a7453bd054439431ab42968dde77f0b5af669a557ab46bf6cb36f4de89` | `d4a20aa222ad5ddfd171516b8212b00f2709da86420f8e217479fd2a5bb93c27` | `9e98ba043948e5b1eb6a53afec816d6903901b0a50e080b905c6e9cb902755ea` |
| `XL` | `5fae476bd5596182aaffebb5311e8f67114ad9aa888edad4e9b101b564fd8e98` | `e3ccfc978b43ae2d04cb00e00ce8da165999417465d0dfe75db732186be2a315` | `c0dcb63ac3777310c828f1b9da2a4222b5c64d7c4e2dfc9365099e1a0fa91ac1` |
| `G3A` | `f881f1c7fba549ed96b87b6b4e8f691a5af790f590192c9e9186276bb86ee747` | `ee12c28eba3f3be9a282b3480569ce44af7e8bcc683132bf45fbc2eba5ea03e5` | `2a084b8833e69c8c149327fc3fa524123bb0de9f91078932ee0b9d6965e9d567` |
| `G3B` | `ead756c75cf32bff1ac8c5f21953649e90d9b537fe9a660364084f95f23b9190` | `3c743d848330299dec890f9230c5e86f4e107221c2494cdd146d79d01d144636` | `648fc438cb4c6b9db6a2e1f17cec02f40d45a8188cbbeb3976d864ec0b5d459b` |
| `G3C` | `03207727853600c8b122843e3014ba6af563e11f65d51098b70c8cb8a0fa87ad` | `6982f364c0314610496cfbbcfaeb370166707e0da014101ff1c7f24f6efa99cc` | `30ac0ea13ae6ef7b48a91358db3ef4407d084e821e5ec1d1e49119463e4791a6` |
| `OWN` | `97908401be96002414033827828d8bb10def56050b10e839f600a45a5462132a` | `a0cb5a88011a3ea8a5be2dd5ee5bf0f627e9e540cb414d105d78d9ef4592521c` | `5e6901b8b4a0c2b999876185d99276a6c1c5275132ff762acd36dfe375aab3c2` |
| `CE` | `886d7cf352938df43e7d24d0015759835d35b1b05361790270468f9dcb0a0ffb` | `02dc65ef6bba25d9f31a51e0f02aa4dda5bb6329b40871816ac580c556aab007` | `81c24bd0af157bffac55bbef325055dbb06e7b3c33fef87e31bdf30845eda69e` |

For each ID, source `prompt.md` from
`fixtures/adversarial-review-loop/prompts/<lowercase-id>.md` and `rubric.md`
from `fixtures/adversarial-review-loop/rubrics/<lowercase-id>.md`. The active
catalog links those files. The linked `OWN` bytes and hashes above are the
authoritative Task 18A epoch and supersede the fixture manifest's stale
top-level `OWN` row. This resolves provenance only and does not change the
scenario.

Catalog acceptance does not audit rubric contents. Rubric hashes guide exact
materialization and review only.

### Prompt adaptations

Start from the canonical prompt bytes and make only these literal substitutions.
Preserve every other byte and the trailing LF.

| IDs | Literal substitutions |
|---|---|
| `CS`, `T3`–`T7`, `NF`, `PW`, `XL`, `G3A`–`G3C`, `CE` | Replace `skills/adversarial-review-loop/SKILL.md` with `{{fixture_dir}}/skills/adversarial-review-loop/SKILL.md`. |
| `T2` | Replace the two-line text `All nine repository skills are available under \`skills/\`.` / `Use \`adversarial-review-loop\` directly to handle the already-surfaced finding below, and treat its \`SKILL.md\` as binding guidance.` with `All nine repository skills are available under \`{{fixture_dir}}/skills/\`.` / `Read \`{{fixture_dir}}/skills/adversarial-review-loop/SKILL.md\` completely to handle the already-surfaced finding below, and treat it as binding guidance.` |
| `OWN` | In its three-item skill list, root `skills/adversarial-review-loop/SKILL.md`, `skills/disciplined-development/SKILL.md`, and `skills/superpowers/subagent-driven-development/SKILL.md` at `{{fixture_dir}}/`. Do not add `disciplined-research` to the prompt; the canonical scenario supplies it through the parent composition without naming its path. |

These substitutions expose already-supplied inputs at schema `"0.2"` paths.
They do not add instructions, requirements, artifacts, or evaluation behavior.

### Fixture mappings

Declare every file separately. Live repository skills use source
`../../../../skills/<skill-id>/SKILL.md` and target
`skills/<skill-id>/SKILL.md`.

| IDs | Live skills |
|---|---|
| `CS`, `T3`–`T7`, `NF`, `PW`, `XL`, `G3A`–`G3C`, `CE` | `adversarial-review-loop` |
| `T2` | `adversarial-review-loop`; `adversarial-review`; `concise-writing`; `disciplined-development`; `disciplined-research`; `dispatching-development-subagents`; `lean-plan-writing`; `sweeping-stale-references`; `writing-explicit-rationale` |
| `OWN` | `adversarial-review-loop`; `disciplined-development`; `disciplined-research` |

`OWN` also packages the tester-selected Superpowers 6.3.0
`subagent-driven-development/SKILL.md` from
`/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/subagent-driven-development/SKILL.md`.
Copy it to
`fixture/skills/superpowers/subagent-driven-development/SKILL.md`, declare that
relative path as the fixture source, and target
`skills/superpowers/subagent-driven-development/SKILL.md`. Its required SHA-256
is `8dd1b8e698edec3700c6d89517dbe96febd3bacd3f6ea21c1a3569c62ea104b5`.

The canonical scenarios contain no other scenario-owned files. Do not create
code, project, evidence, hook, manifest, or bundle fixtures.

### Package records

Each package contains exactly `README.md`, `prompt.md`, `rubric.md`, `test.json`,
and its declared `fixture/` files, if any. Before the smoke, no package contains a
result. Each README records only the scenario purpose, input/provenance mapping,
and smoke status. After a successful smoke, only `OWN` links the exact retained
result and states the runner's mechanical status. Do not make a behavioral claim
or duplicate result contents.

## Catalog acceptance

Create
`skill-validation/runner/acceptance/test_adversarial_review_loop_catalog.py`.
Keep catalog data and any small local helpers in that file. It verifies only:

- exactly the fifteen planned scenario directories and their exact package
  files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- prompt bytes against the adapted hashes above;
- literal fixture source and target mappings against this plan;
- the packaged Superpowers dependency bytes against the pinned hash above;
- resolved prompt tokens and no stale `supplied-skills/` path;
- absence of rubric bytes from declared and prepared provider inputs; and
- an empty initial evidence directory.

Permit only `OWN` to add optional `smoke-result.json` after acceptance is
established. Redirect the runner's temporary root to pytest's `tmp_path` so
preparation leaves no run bundle outside the test directory.

Acceptance does not invoke a provider or validate README prose, rubric content,
execution choices, smoke results, response or result schemas, stdout, stderr,
provider artifacts, or behavioral outcomes. It does not reconstruct a result,
add a negative-test matrix, or add shared machinery. Those are accepted,
unexamined edges outside this migration.

## Verification

After package acceptance is implemented, run from `skill-validation/runner`:

```bash
uv run pytest -q acceptance/test_adversarial_review_loop_catalog.py
uv run pytest -q
```

After the smoke record and index update, rerun only the focused acceptance test
because those changes do not alter package preparation. If review repairs a
package or acceptance behavior, rerun both commands; otherwise rerun only the
affected check. Do not add another verifier or run unrelated skill test suites.

## Task 1: Package all fifteen scenarios

**Files:** Create all fifteen scenario packages and the one declared packaged
dependency.

**Boundary:** Stop on a missing source, hash mismatch, malformed configuration,
or required adaptation outside this plan.

- Materialize canonical prompts and rubrics; apply only the declared prompt
  substitutions.
- Copy only the pinned Superpowers dependency into `OWN`.
- Create the exact schema `"0.2"` configurations and minimal package READMEs.
- Do not carry forward schema `"0.1"` configuration, result-validation, bundle,
  or provenance machinery.

## Task 2: Add catalog acceptance and verify preparation

**Files:** Create
`skill-validation/runner/acceptance/test_adversarial_review_loop_catalog.py`.

**Boundary:** Provider behavior and result content remain accepted, unexamined
edges. Do not add output checks, result checks, mutations, negative-test
matrices, or shared helpers.

- Implement exactly the catalog-local acceptance contract above.
- Run the focused acceptance and the complete offline runner suite once.
- Review the test against the package-only boundary.

## Task 3: Run and record the representative smoke

**Files:** Create
`skill-validation/scenarios/adversarial-review-loop/own/smoke-result.json` only
if the runner publishes `result.json`. Modify the `OWN` README in every outcome;
modify the scenario migration index only after `COMPLETED`.

**Boundary:** Missing output or any status other than `COMPLETED` stops the
catalog without retry. Response meaning, rubric satisfaction, stdout/stderr,
artifact inventories, result schemas, and result reconstruction remain
unexamined.

- From `skill-validation/runner`, invoke exactly once:
  `uv run skilltest run ../scenarios/adversarial-review-loop/own/test.json`.
  Do not retry or run another scenario.
- If the runner publishes `result.json`, replace any prior
  `own/smoke-result.json` with its exact bytes. If it publishes no result, remove
  any prior retained result.
- Read only the runner-written mechanical status needed for disposition. Do not
  compare the retained file back to the bundle or validate any other result
  field.
- Record the runner's mechanical outcome in the `OWN` README and remove the
  owned temporary run directory in every outcome. Retain no other run artifact.
- If the retained result's runner status is `COMPLETED`, update the migration
  index, link all fifteen READMEs, identify `OWN` as representative, and update
  totals to 15/15 and 50/105 overall.
- If no result is retained or status is not `COMPLETED`, do not update the index;
  rerun focused acceptance and stop for owner direction.
- For `COMPLETED`, rerun focused acceptance and review the records.

## Controller review and approval gate

The controller performs this review directly and does not dispatch an external
review.

- Review the whole catalog against the governing design and this plan. Confirm
  the final diff is limited to the fifteen packages, their catalog-local
  acceptance test, and the migration index.
- Confirm that no response judgment, result validation, runner/provider/schema
  change, shared helper, lifecycle state, or unrelated bookkeeping entered the
  implementation.
- Address only verified in-scope findings and rerun only checks affected by
  repairs.
- Report the implementation commits, focused and full offline verification,
  smoke attempt and retained result status, and internal-review disposition.
- Stop and obtain explicit owner approval before merge, push, plan archive,
  roadmap update, feature worktree/branch removal, or next-catalog planning.

## Post-approval closeout

- Merge the feature branch into local `main`.
- On `main`, check the `adversarial-review-loop` roadmap item and move this plan
  to `plans/completed/`, adjusting its three header links for the new location,
  then commit the closeout.
- Push `main`, then remove this catalog's worktree and local feature branch.
  Do not create the next catalog plan without separate owner approval.

## Done when

- All fifteen packages pass catalog acceptance and the complete offline runner
  suite.
- One approved `OWN` invocation retains the exact runner-produced `COMPLETED`
  result.
- The migration index reports 15/15 for this catalog and 50/105 overall.
- Internal review passes without output or result judgment and without extra
  migration process or bookkeeping.
- After owner approval, the catalog is merged and pushed, the roadmap and plan
  are closed, and the feature worktree and branch are removed.
