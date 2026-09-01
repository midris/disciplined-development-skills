# Schema 0.2 Catalog Migration Design

**Status:** Completed and archived 2026-09-01.

## Goal

Package all 105 active canonical scenarios for reusable prompt runner schema
`"0.2"`, one catalog at a time, without changing scenario meaning, runner
behavior, or testing methodology.

Use canonical source commit
`13599fb7d3127334b0d07bfe468767e586ec5f9c` for candidate scope, scenario
meaning, evaluator instructions, task, requested output, supplied-input
representation, scenario-owned bytes, and evaluator-withheld rubrics. Use the
schema `"0.2"` runner and its documentation for configuration, fixture copying,
prompt rendering, execution, and result behavior.

The canonical source commit defines the content to migrate. It is not smoke-run
provenance, and a smoke does not need to be tied to repository state.

## Phase boundary

This migration answers one question: can the minimal schema `"0.2"` runner
configuration represent and prepare every canonical scenario? One representative
invocation per catalog confirms the end-to-end runner path. Work proceeds catalog
by catalog so each catalog establishes those mechanical results before the next
catalog begins.

The migration verifies that checked-in prompts and fixture mappings match the
catalog plan and that every configuration loads and prepares with the runner. It
does not independently audit author-selected configuration choices beyond those
mechanical checks. That is test-design validation, alongside test correctness,
rubric correctness, response quality, behavioral results, evaluator parity, and
the runner's effectiveness as an evaluation harness. Content selected or written
incorrectly despite being mechanically representable is an authoring error, not a
runner capability gap.

Do not add runner functionality, configuration options, validation beyond the
package checks below, or safeguards to prevent possible authoring errors or
anticipate later evaluation needs. After all scenarios are mechanically migrated,
a separately scoped evaluation phase may assess the minimal harness and use
observed evidence to justify any changes.

## Minimality rule

Catalog migration has exactly five responsibilities:

1. package each canonical scenario;
2. verify that every package loads and prepares correctly;
3. run one approved representative smoke for the catalog;
4. retain and document the latest smoke result; and
5. update the catalog records and merge the completed catalog.

> If work does not directly serve one of those responsibilities, it is outside
> this migration.

In particular, do not add:

- runner, provider, schema, or testing-methodology changes;
- smoke-run Git-commit provenance, clean-commit smoke requirements, Git
  snapshots, or synchronization rules;
- a second result validator or reconstruction of checks already performed by
  the runner;
- prescribed authoring order, lifecycle state machines, or plan-status
  transitions;
- shared migration helpers, shared catalog-test helpers, or shared dependency
  storage;
- behavioral scoring, response judgment, baseline claims, or evaluator
  transport enforcement; or
- validation and bookkeeping unrelated to packaging, running, documenting, and
  merging the catalog.

Normal repository review, commit, merge, and push practices remain ordinary
development workflow. They are not part of the runner or scenario contract. Do
not merge or push a catalog without explicit owner approval.

## Catalog sequence and ownership

Follow the order in the
[scenario porting roadmap](../2026-08-24-scenario-porting-roadmap.md). Create one
catalog-specific plan at a time. Complete, merge, and archive that catalog before
creating the next catalog plan.

This design owns the shared migration rules. Each catalog plan owns only that
catalog's candidates, exact package mappings, permitted prompt adaptations,
default executions, representative scenario, acceptance test, and implementation
steps. Scenario READMEs document the finished packages and current smoke status.
The [scenario migration index](../../../skill-validation/scenarios/README.md) owns
catalog totals, scenario links and summaries, representative markers, and the
liftable sample prompt.

Catalog-specific details do not become general rules automatically. A reusable
change requires separate owner approval and a change to this design.

## Scenario package

Every scenario uses this layout:

```text
skill-validation/scenarios/<catalog>/<scenario-id>/
  README.md
  prompt.md
  rubric.md
  test.json
  fixture/                 # optional
  smoke-result.json        # optional
```

`<catalog>` is the lowercase catalog name. `<scenario-id>` and `test.json.id`
are the lowercase canonical ID: `EXAMPLE-01` becomes `example-01`.

- `README.md` explains the scenario, its supplied inputs, their provenance, any
  adaptations, and the current smoke status.
- `prompt.md` is the complete self-contained provider-facing prompt template.
- `rubric.md` is the exact evaluator-withheld canonical rubric.
- `test.json` is one loadable schema `"0.2"` default configuration.
- `fixture/` contains only files that must be stored with the scenario.
- `smoke-result.json`, when present, is the exact latest `result.json` retained
  for that scenario.

Each scenario README has three sections:

1. **Purpose** — what the scenario is built to test;
2. **Inputs** — a compact inventory of the prompt and every supplied file,
   including source or provenance and provider location, plus rubric provenance
   and any prompt adaptations; and
3. **Smoke** — the current result link and mechanical status, or a statement
   that no schema `"0.2"` result is retained.

The README is documentation, not another executable configuration. `test.json`
owns fixture source and target declarations. Do not require a machine-validated
README schema or duplicate every `test.json` field in prose.

## Scenario inputs

A scenario consists of its evaluator instructions, task, requested output,
evaluator-withheld rubric, and scenario-owned bytes. Skill and dependency versions
are tester-selected inputs, not scenario identity.

The checked-in `prompt.md` and `test.json` define the migration's default smoke
input. For this migration, use current live repository skill files directly when
the canonical input is the complete skill file. Record their source paths, but do
not pin their hashes as catalog requirements. The retained runner result records
the files actually copied for a representative smoke.

Store scenario-owned files, derived files, and required external dependencies
beneath the scenario's `fixture/` directory. Preserve scenario-owned bytes
exactly. Record the source, version, and SHA-256 for pinned external dependencies
and other copied canonical files.

Testers may create other prompts or configurations using different skill or
dependency versions. Those alternate inputs are outside catalog migration unless
separately approved.

Preserve the canonical representation of every provider-visible input:

- inline canonical material remains in `prompt.md`;
- canonical files remain individual files at their canonical bundle-relative
  paths;
- an extraction remains that extraction rather than becoming a complete source
  file;
- nested support files retain their canonical paths;
- every supplied file is declared individually in `test.json`; and
- files not visible to the canonical evaluator are not supplied.

Stop if candidate scope, canonical representation, canonical bytes, rubric
identity, or required provenance cannot be determined; a required dependency is
unavailable; the runner cannot represent the scenario; or faithful packaging
requires an unapproved adaptation.

## Prompt and rubric

Every `prompt.md` is independently readable and preserves the canonical ordering,
task meaning, and output requirements. It follows the
[documented prompt anatomy](../../../skill-validation/scenarios/README.md#prompt-anatomy)
without adding a generic wrapper.

When the prompt directly names a supplied file or directory, root that reference
at `{{fixture_dir}}`. Adapt canonical prompt text only for required paths,
explicit read instructions, and environment wording. Any other content change
requires owner approval.

All scenarios are response-only. Prompts prohibit file mutation, do not name
`{{evidence_dir}}`, and require no produced evidence.

Materialize the exact canonical rubric as `rubric.md`. Do not include the rubric
in `test.json`, `prompt.md`, fixtures, provider arguments, or provider standard
input. Catalog migration does not apply the rubric or inspect or score the
response.

## Catalog acceptance

Each catalog has one catalog-local provider-free acceptance test. Keep its data
and small helpers local to that test.

Acceptance verifies only the package:

- the exact expected scenario directories and required package files exist;
- every `test.json` loads and prepares successfully;
- prompts, copied canonical files, pinned dependencies, fixture sources, and
  fixture targets match the catalog plan;
- prompt tokens resolve and no stale `supplied-skills/` paths remain;
- rubric bytes are absent from declared and prepared provider input; and
- initial evidence is empty.

Acceptance does not invoke a provider, score a response, validate README prose,
or independently validate runner result mechanics. Do not add shared migration
or catalog-test machinery. It intentionally does not audit `rubric.md` contents:
the rubric is retained for later evaluation, and incorrect rubric text is an
authoring error rather than a runner capability failure.

Loading and preparation are the complete configuration acceptance check. Do not
separately compare `id`, `prompt`, `execution.provider`, `execution.model`, or
`execution.effort` with the catalog plan. The plan supplies those authoring
choices; validating whether they are the right test-design choices belongs to the
later testing-methodology phase.

## Representative smoke

Each catalog plan selects one representative scenario and specifies its exact
`test.json` execution declaration. Obtain explicit owner approval for one attempt,
then run that configuration once.

If the runner publishes `result.json`, replace any prior result for that scenario
with its exact bytes as `smoke-result.json`. If it publishes no result, remove any
prior smoke result. In either case, update the representative README with the
mechanical outcome and remove the temporary run bundle. Retain no stdout, stderr,
final response, rendered prompt, configuration snapshot, evidence contents, or
other run artifact.

Use the status written by the runner. Do not compare the retained file back to
the bundle, reconstruct its artifact inventory, tie it to a Git commit, or add a
second result-validation procedure. The smoke satisfies catalog completion only
when the retained result has status `COMPLETED`. Otherwise record the outcome and
stop. Do not retry, modify the runner, weaken the scenario, or inspect the response
without new owner direction.

`COMPLETED` means that the runner completed the invocation mechanically. It does
not mean that the response passed the scenario or that the harness is effective.

Other scenario READMEs state that no schema `"0.2"` result is retained. The
migration index identifies the catalog representative.

## Catalog workflow

For each catalog:

1. Create the sole catalog plan. Enumerate the canonical candidates; define the
   exact prompt, rubric, and file mappings; record each default configuration;
   select the representative; and define the catalog-local acceptance test.
2. Create every scenario package and README.
3. Run catalog acceptance and the complete offline runner suite.
4. Obtain approval, run the representative once, retain its latest result, and
   update its README.
5. Update the migration index, review the catalog, obtain merge and push
   approval, merge it, update the roadmap, archive the plan, push `main`, and
   remove the local worktree and feature branch.

Do not create the next catalog plan before the current catalog is merged and its
plan archived.

## Completion

A catalog is complete when:

- every planned scenario has a loadable schema `"0.2"` package that passes its
  catalog acceptance test;
- its representative has one retained `COMPLETED` smoke result;
- the migration index reports the catalog complete;
- final catalog review passes; and
- the catalog is merged, its roadmap item is checked, and its plan is archived.

The migration is complete when all 105 scenarios meet these package requirements,
all catalog representatives have a retained `COMPLETED` smoke result, the index
reports 105/105, and every catalog plan is archived and merged.
