# Schema 0.2 Catalog Migration Design

**Status:** Owner-approved on 2026-08-29.

## Goal

Migrate all 105 active scenarios to the reusable prompt runner one catalog at
a time without changing scenario meaning, runner behavior, or testing
methodology. The first `writing-explicit-rationale` catalog establishes the
package, prompt, documentation, preflight, and smoke process used by later
catalogs.

## Program shape

Use source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c` as the
canonical scenario authority. Complete, review, and merge one catalog before
planning the next. Preserve the prior migration-wave order, then append the two
catalogs that had no prior catalog-wave position:

1. `writing-explicit-rationale`
2. `sweeping-stale-references`
3. `lean-plan-writing`
4. `disciplined-research`
5. `disciplined-development`
6. `adversarial-review-loop`
7. `skill-discovery`
8. `dispatching-development-subagents`
9. `concise-writing`
10. `adversarial-review`

The completed first catalog is the concrete template for later plans. Do not
write speculative plans for later catalogs or extract shared migration helpers
before a second catalog demonstrates the repeated shape. This accepts some
first-catalog repetition to avoid designing an abstraction from one example.

## Scenario identity and evaluation arms

A scenario consists of its purpose, prompt, evaluator-withheld rubric, and
scenario-owned fixture bytes. Skill and dependency versions are tester-selected
evaluation-arm inputs, not scenario identity.

Each checked-in `test.json` is the default smoke arm. During migration it selects
the live repository skill files. A tester may author another configuration that
copies different skill versions to the same fixture targets; no runner change is
needed. Alternate arms are not committed during catalog migration unless they
receive separate scope.

Required external dependencies are packaged beneath the scenario directory for
the first catalog and carry exact source, version, and hash provenance. Revisit
shared dependency storage only after multiple migrated scenarios require the
same pinned bytes.

## Scenario package

Each scenario directory contains:

- `README.md`: purpose, package inventory, arm context, provenance, and
  verification;
- `prompt.md`: the complete provider-facing prompt;
- `rubric.md`: the exact evaluator-withheld rubric;
- `test.json`: one loadable schema `"0.2"` default smoke configuration;
- `fixture/`: scenario-owned files and any locally pinned external dependency;
- optional `smoke-result.json`: the latest retained mechanical runner result for
  that scenario.

`README.md` uses these sections:

1. **Purpose** — the behavior, boundary, or pressure the scenario tests;
2. **Context** — required skill and dependency roles, including the sources
   selected by the default smoke arm;
3. **Package** — every packaged file, its role, and whether it is provider-visible;
4. **Provenance** — canonical commit, source record or section, original hashes,
   and permitted adaptations;
5. **Verification** — provider-free preflight and the latest live smoke, or an
   explicit statement that no live smoke has run.

The active inventory contains catalog totals plus a one-line purpose summary and
link for every scenario. The scenario README, not the global inventory, owns
detailed provenance and package facts.

## Prompt contract

Every `prompt.md` is independently readable and contains the complete execution
context. There is no shared wrapper, prompt generator, or runner-injected skill
context. Prompts use this anatomy in order:

1. evaluator boundary and permissions;
2. skill and dependency files to read;
3. scenario-owned files to read;
4. task context;
5. requested output;
6. mutation and process-narration restrictions.

`skill-validation/scenarios/README.md` documents the anatomy and includes a
small prompt that users can lift as a starting template. Its shape is:

```text
Act as a fresh evaluator and use only the supplied files.
Read {{fixture_dir}}/skills/example/SKILL.md completely and follow it.
Read {{fixture_dir}}/project/input.md.
Perform the supplied task and return the requested artifact.
Return only the artifact; do not modify files or narrate your process.
```

Real prompts replace the placeholders and state their exact task and output
contract. Every provider-visible path uses `{{fixture_dir}}`. Response-only
scenarios prohibit file mutation. A scenario that requires produced files must
name `{{evidence_dir}}` explicitly and remains separate from response-only
scenarios.

Canonical task meaning and output requirements remain unchanged. Adapt only
file paths, explicit read instructions, and environment wording required by the
schema `"0.2"` layout. Any other content adaptation requires owner approval.

## Fixture mapping

`test.json` declares every provider-visible file individually:

- tester-selected skills target `skills/<id>/SKILL.md`;
- packaged external dependencies target the same `skills/<id>/SKILL.md`
  namespace;
- scenario-owned files retain their canonical paths such as
  `project/wer-07/...` or `docs/architecture/...`.

The prompt and README are runner-owned inputs and documentation, not fixtures.
The rubric, README, and retained smoke result are never declared as fixtures.
The runner copies no directory implicitly and receives no new catalog-specific
behavior.

## Rubric isolation

Materialize each canonical evaluator-withheld rubric exactly as `rubric.md` with
recorded bytes and hash. It is repository-visible to testers but absent from the
configuration, rendered prompt, workspace fixture, evidence directory, and
provider invocation. Catalog migration does not apply the rubric, inspect the
semantic response, score behavior, or establish a baseline.

## Smoke evidence

Each scenario may retain only its latest mechanical smoke result as
`smoke-result.json`. Copy the runner's exact `result.json`; do not retain stdout,
stderr, final response, evidence contents, prompt render, configuration snapshot,
or the temporary bundle.

A new smoke replaces the prior result for that scenario. Its README records the
repository commit, configuration hash, provider, model, effort, and whether the
mechanical run completed. The result itself records the run ID, execution state,
artifact metadata, and copied fixture hashes. A failed owned run replaces the
prior result truthfully and stops the catalog; a configuration failure before run
allocation has no result to retain and is recorded in the plan.

During migration, run only the catalog's preselected representative. Other
scenario READMEs state that no live smoke has run. The active inventory links to
the representative scenario and its latest result.

## Catalog workflow

For each catalog:

1. Inventory every canonical scenario, prompt, rubric, fixture, required skill,
   dependency, and hash.
2. Package scenario-owned material and write the self-contained prompt and
   scenario README.
3. Create schema `"0.2"` default smoke configurations selecting the intended arm
   files and declaring every fixture individually.
4. Add catalog-specific provider-free acceptance coverage and preflight every
   configuration.
5. Obtain explicit owner approval, run the preselected scenario once through its
   configured provider, retain only its latest `smoke-result.json`, and inspect
   mechanics without scoring content.
6. Run repository verification, reconcile inventory and roadmap totals, archive
   the completed catalog plan, review the branch, and merge it before selecting
   the next catalog.

The first catalog uses a catalog-specific acceptance test. Do not introduce a
shared catalog-test helper until the next catalog exposes actual duplicated test
logic.

## First catalog

The `writing-explicit-rationale` catalog contains:

| Scenario | Purpose | Default arm | Scenario-owned files |
|---|---|---|---|
| `WER-01` | Preserve a descope, cause, and accepted impact beside the revised plan item. | All nine live repository skills. | None. |
| `WER-02` | Batch repeated-review rationale across decision sites while excluding a consequence-free choice. | Live `writing-explicit-rationale`. | None. |
| `WER-05` | Reference one authoritative rationale home without duplicating its explanation. | Live `writing-explicit-rationale`. | `docs/architecture/ingest.md`. |
| `WER-06` | Preserve correctness-relevant causality while removing irrelevant history. | Live `writing-explicit-rationale`. | None. |
| `WER-07` | Compose rationale, research, planning, and parent-development guidance across supplied primary sources. | Live `writing-explicit-rationale`, `disciplined-development`, `disciplined-research`, and `lean-plan-writing`; packaged `writing-plans`. | Four canonical `project/wer-07/...` files. |
| `WER-08` | Apply the rationale-home rule to a non-software policy decision. | Live `writing-explicit-rationale`. | None. |

All six default configurations use Codex `gpt-5.6-sol` at low effort. `WER-07`
is the representative live smoke because it exercises multiple selected skills,
one external dependency, multiple scenario files, explicit prompt paths, and a
response-only run whose evidence directory should remain empty. Its response is
not read or scored during migration.

Completing this catalog changes active inventory from 0/105 to 6/105.

## Provider-free acceptance

The first catalog's acceptance test verifies:

- exactly six expected packages, each with `README.md`, `prompt.md`, `rubric.md`,
  and schema `"0.2"` `test.json`;
- successful load and preparation of every configuration;
- exact declared fixture targets and bytes;
- resolved runner tokens and no stale `supplied-skills/` paths;
- absence of rubric bytes from all provider-visible input;
- fixed hashes for scenario-owned prompts, rubrics, fixtures, and pinned external
  dependencies, plus byte equality between each copied live skill and its current
  configuration source;
- no unexpected `smoke-result.json`, except the latest retained result for a
  scenario that has actually run.

This is mechanical packaging verification, not behavioral evaluation.

## Fail-closed conditions

Stop the catalog and request owner direction when canonical bytes or rubric
identity are missing or ambiguous, a required dependency is unavailable, a
scenario requires unsupported runner behavior, hashes do not reconcile, or
faithful packaging would require content adaptation beyond paths and environment
wording.

If the live smoke produces an infrastructure result, retain that latest result
and stop. Do not repeat the invocation, change the runner, weaken the scenario,
inspect the response semantically, skip the scenario, or mark the catalog
complete without new owner direction. These are plan rules, not new hooks,
validators, or runner behavior.

## Verification and boundaries

Each catalog runs the full runner suite, its provider-free catalog acceptance,
the mandatory repository hook suite, the local Markdown-link check, and
`git diff --check`. It receives task review and final whole-branch review before
merge.

Catalog migration does not change the runner, providers, skills, canonical
scenario meaning, validation methodology, behavioral scoring, baselines, or raw
provider artifacts. Runner changes, scenario redesign, alternate committed arms,
shared dependency storage, shared test helpers, and testing methodology require
separate approved scope.

Migration is complete when all 105 active scenarios have loadable schema `"0.2"`
packages with reconciled provenance and provider-free preflight, every catalog
has one retained representative smoke result, inventory reports none remaining,
and every catalog plan is archived.
