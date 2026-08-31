# Disciplined Research Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` to implement Tasks 1–4 task by task.
> After Task 4, leave the subagent-driven task loop and perform the controller
> closeout directly; do not dispatch that section as a task.
> Use `superpowers:verification-before-completion` before completion claims.
> Track progress with the checkboxes below.

**Goal:** Package all seven active `disciplined-research` scenarios for the
schema `"0.2"` runner, retain one completed representative smoke result, and
finish this catalog before planning the next one.

**Architecture:** Each canonical scenario becomes one self-contained package.
Current repository skills remain live fixture sources, while canonical
scenario-owned files are copied into their owning packages. `DR-01` is the sole
representative because it exercises the complete local skill bundle and two
scenario-owned files through one response-only run.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](../specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](../2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../../skill-validation/scenarios/README.md).

## Global constraints

- Implement on branch `feature/disciplined-research-schema-02` in
  `.worktrees/disciplined-research-schema-02/`.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for candidate scope,
  scenario meaning, prompt material, scenario-owned bytes, and rubrics.
- Package exactly `DR-01` through `DR-07` at
  `skill-validation/scenarios/disciplined-research/<lowercase-id>/`.
- Give each default configuration the execution declaration
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"high"}`.
- Use current repository `SKILL.md` files directly as fixture sources. Do not
  copy them into scenario packages or pin their hashes.
- Copy each canonical scenario-owned file only into its owning package and
  preserve its bytes exactly. Recover the bytes from the canonical source
  commit; do not reconstruct or regenerate them.
- Apply only the prompt substitutions listed below. Do not otherwise rewrite,
  normalize, reflow, clarify, or improve canonical prompts or rubrics.
- Keep every scenario response-only. Do not use `{{evidence_dir}}`, request file
  changes, add evaluator behavior, score responses, or inspect response meaning.
- Add only the catalog-local acceptance test named below. Do not change runner,
  provider, schema, skill, shared helper, or other catalog files.
- The owner's standing approval covers necessary Codex invocations for future
  test-scenario migrations. Run only `DR-01`, once, with no retry.
- Do not merge, push, archive this plan, or remove the feature branch or
  worktree without explicit owner approval. Do not create the next catalog plan
  before this catalog is merged and this plan is archived.
- Stop under the design's fail-closed conditions. In particular, stop if a
  canonical source is unavailable or differs, an unlisted prompt adaptation is
  needed, the runner cannot represent a scenario, or the smoke does not finish
  with runner status `COMPLETED`.
- Treat the whole catalog as one merge boundary: one feature branch and one
  final merge. Per-scenario branches would leave catalog acceptance and index
  state incomplete without making any package independently more useful.

## Catalog decisions

### Candidate inventory and representative

| ID | Purpose | Default supplied context |
|---|---|---|
| `DR-01` | Prefer current implementation over stale project documentation and correct a peer-fed retention claim with a source. | Complete current nine-skill repository bundle and the canonical retention project fixture |
| `DR-02` | Use a later controlling first-party addendum to disconfirm a supplied museum-procurement deadline. | Current `disciplined-research` and the canonical procurement sources |
| `DR-03` | Verify project and upstream version state separately and correct a cross-domain claim. | Current `disciplined-research` and the canonical project and upstream sources |
| `DR-04` | Apply acquire, verify, and source-disclosure rules to a private scratch note while mapping one source to multiple claims. | Current `disciplined-research` and the canonical retry-policy source |
| `DR-05` | Refuse to invent a datum missing from the only supplied source despite pressure for an uncaveated casual answer. | Current `disciplined-research` and the canonical support matrix |
| `DR-06` | Present an unsupported cause only as a stamped unverified investigation lead without attaching unrelated evidence as support. | Current `disciplined-research` and the canonical incident artifacts |
| `DR-07` | Correct a conversational premise and derive only the supported fifteen-minute result with source disclosure. | Current `disciplined-research` and the canonical hours source |

`DR-01` is the sole representative because it composes the catalog's broadest
provider input: all nine live repository skills and two canonical project files.
`DR-06` has the largest fixture, but catalog acceptance already exercises its
preparation; the smoke should cover the broadest live-skill input instead. The
older schema `"0.1"` plan selected `DR-05`, whose one-skill, one-file package is
narrower than the schema `"0.2"` catalog shape.

### Canonical prompt and rubric provenance

Hashes are SHA-256 over complete file bytes, including one trailing LF. For
`DR-01` through `DR-03`, each prompt is the fenced evaluator input beneath the
named heading in canonical `skill-validation/disciplined-research.md`, and each
rubric is the active catalog table's evaluator-withheld rubric cell plus one
trailing LF. For `DR-04` through `DR-07`, prompts and rubrics are the canonical
files linked from that record.

| ID | Canonical prompt source | Prompt SHA-256 | Canonical rubric source | Rubric SHA-256 |
|---|---|---|---|---|
| `DR-01` | `DR-01 — bundled project verification` | `4b79859709fa069aff54c03f71f712875ce419edbe01212d0b5b44cad8b45b74` | Active catalog rubric cell | `f9094161371b6aeeb63a84a5268c68f31376cab7e814afb52062fe0ddc830621` |
| `DR-02` | `DR-02 — isolated museum procurement deadline` | `61113a936de2f2b82a8aa04b9ea33b55f9bf017096b7f9ff4eda0c240ba13466` | Active catalog rubric cell | `b349513f2c134517d17831b6c8788ef011fca775f8335ad187fff8f97ebc1f85` |
| `DR-03` | `DR-03 — cross-domain version verification` | `01cbb20fdd6e0dd4a2d000e2599a897c4df17791a0e61675bd163354e7bcf5f1` | Active catalog rubric cell | `0f9a44c2690d1af8d68ed23ccb4b72bbf804ea0a2db6496431049563c1757fca` |
| `DR-04` | `fixtures/disciplined-research/prompts/dr-04.md` | `d6446bc6aee30bbb6534c18af706bfb6699f08a1b9383e070900de1ecdcc6362` | `fixtures/disciplined-research/rubrics/dr-04.md` | `5bcf27a85d8c055dfde82fe08bce8a25cac2b3850ca252652046d96500243132` |
| `DR-05` | `fixtures/disciplined-research/prompts/dr-05.md` | `c2b9901d48251d24dea35db1cda537b8fab95952615ea18fe4e97c57cd3055b6` | `fixtures/disciplined-research/rubrics/dr-05.md` | `f34530f4d3fcb87fb2e8097168f462bfc906843d4d793f0f4ab68e88b0920ed8` |
| `DR-06` | `fixtures/disciplined-research/prompts/dr-06.md` | `69ff7d3a620e03911313fcc76d28a2d813ff24648a266c9d994d554d2fbd5c0c` | `fixtures/disciplined-research/rubrics/dr-06.md` | `c479c2083bf950217e631b75db7b84a6166e81be4c05f9aaebacaec6981df7b1` |
| `DR-07` | `fixtures/disciplined-research/prompts/dr-07.md` | `54850a6aff5bb87f231cdf5b765c0437901a8a3e4debe9e064b36c0670219c4c` | `fixtures/disciplined-research/rubrics/dr-07.md` | `a29cde034d63ecfc229e3821435e92dfe6c33dc348f4b3cef03fb151db4a3bd3` |

Materialize each rubric as `rubric.md`. These hashes guide authoring and
provenance; catalog acceptance does not audit rubric contents.

### Prompt adaptations

Start from the canonical prompt bytes and make only the substitutions below.
For every scenario, replace the literal
`skills/disciplined-research/SKILL.md` with
`{{fixture_dir}}/skills/disciplined-research/SKILL.md`. Preserve all other bytes
and the trailing LF except for the scenario-specific adaptations listed here.

| ID | Additional literal adaptations | Resulting `prompt.md` SHA-256 |
|---|---|---|
| `DR-01` | Replace `The complete local skill bundle is installed.` with `The complete local skill bundle is supplied beneath \`{{fixture_dir}}/skills\`.`; replace task path `project/README.md` with `{{fixture_dir}}/project/README.md`; replace `Inspect the supplied project files and verify the current behavior before answering.` with `Inspect \`{{fixture_dir}}/project/README.md\` and \`{{fixture_dir}}/project/app/retention.py\`, and verify the current behavior before answering.` | `b011d522027b31696e4e6db6c3dfb61e59b5886f6c0ba153a3eca75d0ff0f644` |
| `DR-02` | Replace `Inspect the supplied sources, state explicitly if the premise is wrong, and identify the controlling authority.` with `Inspect \`{{fixture_dir}}/sources/city-museum-rfp.md\`, \`{{fixture_dir}}/sources/city-museum-addendum-2.md\`, and \`{{fixture_dir}}/sources/friends-newsletter.md\`; state explicitly if the premise is wrong and identify the controlling authority.` | `74dc6208dc12771c5754b8293efff7a632a11f2ad4a3082887e80d3dfb36faf0` |
| `DR-03` | Immediately before `Verify both the project's installed version and the authoritative upstream stable version.`, add `Read \`{{fixture_dir}}/project/package.json\`, \`{{fixture_dir}}/sources/orbital-release-notes.md\`, and \`{{fixture_dir}}/sources/orbital-maintainer-blog.md\`.` | `4a2ecdc36d1b647bfeac840c054c880958a0331457979cf416fe533348e7ec10` |
| `DR-04` | Immediately after the skill-read instruction, add `Read \`{{fixture_dir}}/project/payments/retry_policy.py\`.` | `73c675097aa4ef75a17f4ed7fcb9f56042f0a5bd374660c26217f28828fb84d7` |
| `DR-05` | Immediately after the skill-read instruction, add `Read \`{{fixture_dir}}/sources/nimbus-support-matrix.md\`.` | `25c63ad6fa002e671aa631ff96b52f2302f9bb58885cf2f918c4f89334aaf791` |
| `DR-06` | Replace `Inspect the supplied incident artifacts and prepare the next on-call engineer’s handoff.` with `Inspect \`{{fixture_dir}}/project/upload-403/evidence-index.md\`, \`{{fixture_dir}}/project/upload-403/runtime-config.json\`, and \`{{fixture_dir}}/project/upload-403/worker.log\`, and prepare the next on-call engineer’s handoff.` | `14c9968aae4616b3e19105d82e53b4b2a000bb7bb21027a5d8292705a409b1c2` |
| `DR-07` | Replace `Read \`sources/north-annex-hours.md\`.` with `Read \`{{fixture_dir}}/sources/north-annex-hours.md\`.` | `0a73303a85788bf3a23942d6be800a5f6162bc45526e14d05c7253c1482f6b0f` |

These adaptations expose supplied files through schema `"0.2"` paths without
changing the task or requested output. Do not add a wrapper or reorganize any
prompt.

### Live skill fixtures

For each live skill, use source `../../../../skills/<skill-id>/SKILL.md` and
target `skills/<skill-id>/SKILL.md`. Declare every used file separately.

| ID | Live skills |
|---|---|
| `DR-01` | `adversarial-review-loop`; `adversarial-review`; `concise-writing`; `disciplined-development`; `disciplined-research`; `dispatching-development-subagents`; `lean-plan-writing`; `sweeping-stale-references`; `writing-explicit-rationale` |
| `DR-02`, `DR-03`, `DR-04`, `DR-05`, `DR-06`, `DR-07` | `disciplined-research` |

### Packaged files

| ID | Canonical source or fixture path | Package source | Fixture target | SHA-256 |
|---|---|---|---|---|
| `DR-01` | Inline `project/app/retention.py` fixture | `fixture/project/app/retention.py` | `project/app/retention.py` | `900dd0268a517c797023f907ce3a14b6f66bc04b9c27787a153cd471dea6bec8` |
| `DR-01` | Inline `project/README.md` fixture | `fixture/project/README.md` | `project/README.md` | `49061feab313293d6a1b8f23cae43056c79eeee88a00745a741595f98d54f1db` |
| `DR-02` | Inline `sources/city-museum-rfp.md` fixture | `fixture/sources/city-museum-rfp.md` | `sources/city-museum-rfp.md` | `5b50cf2558ef9a73335487198f2fd44a30339df58741df312374e169951340ca` |
| `DR-02` | Inline `sources/city-museum-addendum-2.md` fixture | `fixture/sources/city-museum-addendum-2.md` | `sources/city-museum-addendum-2.md` | `a882f3e3753ca78357333238e5f808d65d251852df04e0506bf2582940bec64f` |
| `DR-02` | Inline `sources/friends-newsletter.md` fixture | `fixture/sources/friends-newsletter.md` | `sources/friends-newsletter.md` | `a8746ab03403c6143e8f65d0e249436b5bb8341c2ebe4c953eb21797787fad5f` |
| `DR-03` | Inline `project/package.json` fixture | `fixture/project/package.json` | `project/package.json` | `1c2bb8f53dce6c7a90c2411d53f177dbfcba8ace56861399dd4f55412e0fb262` |
| `DR-03` | Inline `sources/orbital-release-notes.md` fixture | `fixture/sources/orbital-release-notes.md` | `sources/orbital-release-notes.md` | `1592db31a0848116b082b2093704d80847f672b540633c00b0ea6c30ad03c3f4` |
| `DR-03` | Inline `sources/orbital-maintainer-blog.md` fixture | `fixture/sources/orbital-maintainer-blog.md` | `sources/orbital-maintainer-blog.md` | `3f6e47ed632fde9a22f94ec764ca2c98b5365a9db6190566e8efb29234347488` |
| `DR-04` | `fixtures/disciplined-research/project/payments/retry_policy.py` | `fixture/project/payments/retry_policy.py` | `project/payments/retry_policy.py` | `a7099716223bf4a0c67fc32bda4c6816e6743be3e72aff5f52f3acc953f9a9c4` |
| `DR-05` | `fixtures/disciplined-research/sources/nimbus-support-matrix.md` | `fixture/sources/nimbus-support-matrix.md` | `sources/nimbus-support-matrix.md` | `0abe5b18aaa9a6315fa982dba406a8bb6255dd9652674956426fb34fbd4c5843` |
| `DR-06` | `fixtures/disciplined-research/project/upload-403/evidence-index.md` | `fixture/project/upload-403/evidence-index.md` | `project/upload-403/evidence-index.md` | `5ce87478b5f41f46f10dbba5b329f6eae004ca9b4a6895a495fa75ec292bfb46` |
| `DR-06` | `fixtures/disciplined-research/project/upload-403/runtime-config.json` | `fixture/project/upload-403/runtime-config.json` | `project/upload-403/runtime-config.json` | `4ec39350c64e94229c7aaa59a719afc1c18c2c673d7d5215a8be38ee5307af13` |
| `DR-06` | `fixtures/disciplined-research/project/upload-403/worker.log` | `fixture/project/upload-403/worker.log` | `project/upload-403/worker.log` | `d381395b47ed8fb03ca12fc8c1ab9a1c17299d28149d591119319705aed39eba` |
| `DR-07` | `fixtures/disciplined-research/sources/north-annex-hours.md` | `fixture/sources/north-annex-hours.md` | `sources/north-annex-hours.md` | `876d614b194ace2d807a947223565f3fdc9a597be45c6c1b753a9252a65e45da` |

The canonical fixture directory no longer exists in the current tree. Extract
every row from the source commit and fail closed if a path is unavailable or its
SHA-256 differs. In particular, copy `worker.log` exactly; do not synthesize its
repeated content.

### Default configurations

Every `test.json` uses schema `"0.2"`, its lowercase scenario ID,
`"prompt":"prompt.md"`, the execution declaration in Global constraints, and
these fixture mappings:

| ID | Fixture mappings |
|---|---|
| `dr-01` | Nine live repository skills; packaged `retention.py`; packaged project `README.md` |
| `dr-02` | Live `disciplined-research`; three packaged procurement sources |
| `dr-03` | Live `disciplined-research`; packaged `package.json`; two packaged upstream sources |
| `dr-04` | Live `disciplined-research`; packaged `retry_policy.py` |
| `dr-05` | Live `disciplined-research`; packaged support matrix |
| `dr-06` | Live `disciplined-research`; three packaged incident artifacts |
| `dr-07` | Live `disciplined-research`; packaged hours source |

### README content

Each scenario README contains only `Purpose`, `Inputs`, and `Smoke` sections.
Use the candidate table for Purpose. Inputs compactly records prompt provenance
and adaptation, rubric provenance, every live skill source and provider target,
and every scenario-owned file's canonical source, package source, and provider
target. Smoke initially states that no schema `"0.2"` result is retained. After
the representative run, only `DR-01` links the retained result and states the
runner's mechanical status. Do not duplicate the configuration or make a
behavioral claim.

## Catalog acceptance

Create
`skill-validation/runner/acceptance/test_disciplined_research_catalog.py`. Keep
all catalog data and small helpers in that file. It verifies only:

- exactly the seven planned scenario directories and their required package
  files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- prompt bytes against the adapted prompt hashes above;
- fixture source and target mappings against this plan;
- packaged scenario-file bytes against the hashes above;
- resolved prompt tokens and absence of stale `supplied-skills/` paths;
- absence of rubric bytes from declared and prepared provider inputs; and
- an empty initial evidence directory.

Permit only `DR-01` to add an optional `smoke-result.json` after acceptance is
first established. Redirect the runner's temporary root to pytest's `tmp_path`,
following the existing catalog acceptance pattern, so preparation leaves no run
bundle outside the test's temporary directory.

Acceptance does not invoke a provider, validate README prose or rubric contents,
compare the configuration's ID, prompt, provider, model, or effort to this plan,
inspect smoke results, validate provider output, or add shared machinery. Those
omissions preserve the design's package-only boundary.

## Verification

After Task 3, run the focused catalog acceptance from
`skill-validation/runner` with
`uv run pytest -q acceptance/test_disciplined_research_catalog.py`, then run the
complete offline runner suite with `uv run pytest -q`. After Task 4, rerun only
the focused catalog acceptance because that task changes only the permitted
smoke result and documentation. If review repairs a package or its acceptance
test, rerun both runner commands; otherwise rerun only affected checks.

Before each commit, run the repository's existing local Markdown-link check
documented under `Verification commands` in
`13599fb7d3127334b0d07bfe468767e586ec5f9c:skill-validation/README.md`,
`git diff --check`, and `git diff --cached --check`. During controller closeout,
run the repository-required hook suite once with
`cd skills/disciplined-development/hooks && python3 -m pytest -q`. This hook
suite is repository sign-off, not catalog acceptance; do not repeat it after
Task 4 or on `main`. Do not add another verifier.

## Task 1: Package representative `DR-01`

**Files:**

- Create `README.md`, `prompt.md`, `rubric.md`, and `test.json` beneath
  `skill-validation/scenarios/disciplined-research/dr-01/`.
- Create `fixture/project/app/retention.py` and `fixture/project/README.md`
  beneath that package.
- Modify this plan only to mark completed steps.

**Boundary:** Stop if any canonical source is missing or hash-mismatched, or if
configuration loading requires an unlisted adaptation. Package size is bounded
by the declared files; no other input is accepted.

- [x] Create the self-contained package from the catalog decisions above.
- [x] Confirm the prompt and packaged files have their planned hashes and the
  configuration loads with the runner.
- [x] Review the package files against their sources and commit the task changes.

## Task 2: Package `DR-02` through `DR-07`

**Files:**

- Create `README.md`, `prompt.md`, `rubric.md`, and `test.json` beneath each
  remaining scenario package.
- Create the twelve listed canonical files beneath their owning packages.
- Modify this plan only to mark completed steps.

**Boundary:** Each package accepts exactly the canonical files declared above.
Stop on a missing source, hash mismatch, malformed configuration, or required
adaptation outside this plan. Do not reconstruct or normalize the large `DR-06`
worker log.

- [x] Create all six self-contained packages from the catalog decisions above.
- [x] Confirm the prompts and packaged files have their planned hashes and each
  configuration loads with the runner.
- [x] Review the package files against their sources and commit the task changes.

## Task 3: Add catalog acceptance and verify preparation

**Files:**

- Create
  `skill-validation/runner/acceptance/test_disciplined_research_catalog.py`.
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
  `skill-validation/scenarios/disciplined-research/dr-01/smoke-result.json` only
  if the runner publishes `result.json`.
- Modify `skill-validation/scenarios/disciplined-research/dr-01/README.md`.
- Modify `skill-validation/scenarios/README.md` only after a `COMPLETED` result.
- Modify this plan only to mark completed steps.

**Boundary:** A missing result or any runner status other than `COMPLETED` is
recorded mechanically and stops the catalog without a retry. Response meaning,
rubric satisfaction, provider stdout/stderr, result artifact inventories, and
result-file reconstruction are outside this migration and remain unexamined.

- [x] Under the owner's standing approval, run exactly
  `uv run skilltest run ../scenarios/disciplined-research/dr-01/test.json` once
  from `skill-validation/runner`. Do not retry or run another scenario.
- [x] If the runner publishes `result.json`, copy its exact bytes to
  `dr-01/smoke-result.json`; otherwise remove any prior retained result.
- [x] Record only the runner status and result link, when present, in the
  `DR-01` README; remove the temporary run bundle and retain no other run
  artifact.
- [ ] If no result is retained or its status is not `COMPLETED`, run catalog
  acceptance and the repository commit checks, review and commit the smoke
  disposition, README, and plan tracking, then stop and request owner direction.
  Do not update the migration index.
- [x] For a `COMPLETED` result, add the catalog to the migration index, link all
  seven READMEs, identify `DR-01` as representative, and update totals to 7/7
  for this catalog and 26/105 overall.
- [x] Run focused catalog acceptance and the repository commit checks, review
  the smoke documentation and index update, and commit the task changes.

## Controller closeout: Final review, merge, and catalog bookkeeping

**Files:**

- Modify `plans/2026-08-24-scenario-porting-roadmap.md` after merge.
- Move this plan to
  `plans/completed/2026-08-31-disciplined-research-catalog-migration.md` after
  merge.

**Ownership:** This section is outside the subagent-driven task loop. The
controller performs it directly under the repository's Gate 5 and
branch-finishing rules.

**Boundary:** A merge conflict, verification failure, or rejected push stops
completion with the feature worktree and branch preserved. Only the named
roadmap, plan, index, acceptance, and package paths belong to this catalog.

- [x] Complete a whole-catalog review against the governing design and this
  plan. Address verified findings, rerun only affected migration checks, and run
  the repository hook suite once before sign-off.
- [x] Confirm the final diff is limited to this catalog's packages, its local
  acceptance test, migration index, and plan tracking.
- [x] Present the commits, verification results, retained smoke result, review
  disposition, and cleanup targets to the owner. Obtain explicit approval before
  merging, pushing, archiving this plan, or removing the feature branch or
  worktree.
- [x] After approval, merge the feature branch into local `main`.
- [x] On `main`, check the `disciplined-research` roadmap item and move this plan
  to `plans/completed/`. Change its three header links to
  `../specs/2026-08-29-catalog-migration-design.md`,
  `../2026-08-24-scenario-porting-roadmap.md`, and
  `../../skill-validation/scenarios/README.md`; run the Markdown link check and
  `git diff --check`, then commit those bookkeeping changes.
- [x] Push `main`, then remove this catalog's worktree and local feature branch.
  Do not create the next catalog plan in this task.

## Done when

- [x] All seven packages pass the catalog acceptance test and offline runner
  suite.
- [x] `DR-01` retains the latest runner-produced `COMPLETED`
  `smoke-result.json` from one approved attempt.
- [x] The migration index reports 7/7 for this catalog and 26/105 overall.
- [x] Final review and repository verification pass.
- [x] With owner approval, the catalog is merged and pushed, the roadmap is
  checked, the plan is archived, and the worktree and feature branch are removed.
