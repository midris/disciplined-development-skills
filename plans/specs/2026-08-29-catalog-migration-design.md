# Schema 0.2 Catalog Migration Design

**Status:** Owner-approved on 2026-08-29.

## Goal

Package all 105 active canonical scenarios for reusable prompt runner schema
`"0.2"`, one catalog at a time, without changing scenario meaning, runner
behavior, or testing methodology. The first catalog establishes the migration
process used by later catalogs.

## Authorities and ownership

Use source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c` as the
authority for candidate scope, scenario meaning, evaluator instructions, task,
requested output, supplied-input representation, scenario-owned bytes, and
evaluator-withheld rubric. Use the schema `"0.2"` runner and its documentation as
the authority for configuration, fixture-copy, prompt-rendering, execution, and
result mechanics.

Each migration fact has one durable operational owner:

| Artifact | Owns |
|---|---|
| This design | Shared considerations, package rules, workflow, smoke contract, and completion rules for every catalog |
| Catalog plan | All intended work and decisions specific to one catalog, including its candidates, scenario packages, representative, default executions, acceptance, and migration-time smoke record |
| Scenario `README.md` | Implemented scenario purpose, provider-input manifest and provenance, adaptations actually applied, and current schema `"0.2"` smoke status |
| Scenario migration index | Catalog totals, scenario links and summaries, representative marker, and liftable prompt template |
| Roadmap | Migration order and phase status |

While work is active, the catalog plan is the authority for catalog-specific
instructions and decisions. After implementation, scenario READMEs and the index
own the resulting current package and status facts; the archived plan links to
them and retains the historical execution record.

## Program shape

Follow the catalog order in the roadmap. Create exactly one catalog-specific plan
for the current catalog, complete and archive that plan, and merge the catalog
before creating the plan for the next catalog. Keep only one active catalog plan
at a time.

This design remains the general migration method. Each catalog plan applies it to
one catalog and defines all catalog-specific work. A completed catalog may expose
a reusable consideration that warrants a separately approved design amendment,
but its input shape or implementation details do not become general rules by
default. Do not introduce shared migration or catalog-test helpers during this
migration.

## Scenario identity and evaluation arms

A scenario contract consists of its purpose, evaluator instructions, task,
requested output, evaluator-withheld rubric, and scenario-owned bytes. Skill and
dependency versions are tester-selected evaluation-arm inputs, not scenario
identity.

The checked-in `prompt.md` and `test.json` together define the default smoke arm.
During migration, that arm selects current live repository skill text where the
canonical representation permits a live file or an extraction from it. Required
external dependency bytes are pinned beneath the scenario package with exact
source, version, and hash provenance.

A tester may create another prompt and configuration that select different arm
bytes. Alternate arms may change prompt material, fixture sources, or both
without a runner change. They are not committed during catalog migration unless
separately approved. Revisit shared dependency storage only after multiple
migrated scenarios require the same pinned bytes.

## Package layout and identity

Every scenario uses this exact layout:

```text
skill-validation/scenarios/<catalog>/<scenario-id>/
  README.md
  prompt.md
  rubric.md
  test.json
  fixture/                 # optional
  smoke-result.json        # optional
```

`<catalog>` is the lowercase catalog name. `<scenario-id>` and `test.json`'s
`id` are the lowercase form of the canonical scenario ID: `EXAMPLE-01` becomes
`example-01`, and `EXAMPLE` becomes `example`. The canonical uppercase ID
remains the documentation identity.

Package files have these roles:

- `README.md`: purpose, package provenance, adaptations actually applied, and
  verification;
- `prompt.md`: self-contained provider-facing prompt template;
- `rubric.md`: exact evaluator-withheld rubric;
- `test.json`: one loadable schema `"0.2"` default-arm configuration;
- `fixture/`: packaged provider-visible files, present only when needed;
- `smoke-result.json`: exact latest schema `"0.2"` mechanical result retained
  for that scenario, present only after a result-producing attempt.

Each scenario README uses three sections:

1. **Purpose** — behavior, boundary, or pressure tested;
2. **Package and provenance** — the provider-input manifest, canonical and
   default-arm provenance, and adaptations actually applied;
3. **Verification** — provider-free preflight and either the current schema
   `"0.2"` smoke commit and result link or an explicit statement that no current
   schema `"0.2"` result is retained.

## Provider-input manifest

The catalog plan first defines each scenario's intended provider-visible inputs,
mapping, provenance, and permitted adaptations. Before authoring the prompt,
configuration, or fixtures, create the scenario README and transcribe those
decisions into its initial manifest. After authoring those files, finalize the
manifest's sources, targets, and hashes and reconcile its rows with `test.json`.
Each manifest row records:

| Field | Meaning |
|---|---|
| Provider input | `prompt.md` or a stable label for one supplied file |
| Ownership | `scenario`, `arm`, or both |
| Representation | `prompt` or `file`, matching the canonical evaluator input |
| Canonical and default-arm provenance | Canonical provenance and, when different, the exact origin of selected default-arm bytes; include paths, sections, revisions or external versions, and recorded canonical hashes as applicable |
| Default-arm source | `prompt.md` or the regular file named by `test.json` |
| Provider location | Rendered prompt or exact fixture target path |
| Default-arm source SHA-256 | Complete `prompt.md` template bytes or exact declared source-file bytes before runner rendering or copying |

Each manifest has exactly one `prompt.md` row and one supplied-file row per
`test.json.fixtures` entry. The prompt row records all canonical prompt sources
and the provenance of any inline arm-selected material, plus the complete template
hash; it does not divide the prompt into independently hashed fragments.

The manifest is the migration invariant:

> Preserve the canonical representation of every provider-visible input.
> Preserve scenario-owned bytes exactly, record and reproduce the selected arm
> bytes exactly, and adapt scenario prompt content only for paths, explicit read
> instructions, and environment wording required by schema `"0.2"`.

Apply it mechanically:

- canonical inline material remains in `prompt.md`;
- canonical file material remains an individually declared file at its canonical
  bundle-relative path;
- a canonical extraction, such as a description file, is materialized as that
  exact file rather than replaced with a full source file or inline text;
- nested skill references and support files retain their canonical paths;
- scenario-owned files retain their canonical paths;
- every file is declared individually in `test.json`; the runner infers and
  copies no directory;
- current repository files may be direct configuration sources when their whole
  bytes are the selected arm input;
- derived arm files, scenario-owned files, and pinned external files live under
  the scenario's `fixture/` directory;
- files not visible to the canonical evaluator are not declared as fixtures.

Do not transform prompt material into a file, a file into prompt material, an
extraction into a complete source file, or a complete source file into an
extraction without owner approval. Stop if the canonical representation or bytes
cannot be determined.

## Prompt contract

Every `prompt.md` is independently readable, preserves the canonical relative
ordering of its material, and accounts for each applicable semantic element in the
[scenario migration index](../../skill-validation/scenarios/README.md#prompt-anatomy).
The runner injects no wrapper, skill text, dependency text, or behavioral
instructions.

When a prompt directly names a canonical bundle-relative file or directory, it
roots that reference at `{{fixture_dir}}`. Canonical support files loaded
indirectly from an already rooted supplied file need not be listed redundantly
in the prompt. All 105 canonical scenarios are response-only: prompts prohibit
file mutation, do not name `{{evidence_dir}}`, and require no produced evidence.

The scenario migration index owns the liftable sample `prompt.md`. Real prompts
replace its placeholders and preserve the canonical task meaning and output
requirements. Content adaptations beyond paths, explicit read instructions, and
environment wording required by schema `"0.2"` require owner approval.

## Rubric isolation

Materialize the exact canonical evaluator-withheld rubric as `rubric.md` and
record its source and hash in the scenario README. The runner must not supply it
through `test.json`, the rendered prompt, declared fixtures, evidence setup,
provider arguments, or provider standard input.

This requirement does not claim filesystem isolation beyond existing runner
permissions. Migration does not apply the rubric, inspect the response
semantically, score behavior, or establish a baseline.

## Evaluator transport boundary

Schema `"0.2"` does not reproduce the canonical behavioral-evaluation transport.
The canonical protocol uses a read-only sandbox, ignores user configuration and
rules, and disables nested agents. The runner uses its fixed writable provider
workspace and installed configuration. Prompt restrictions and post-run
inventories do not make those transports equivalent.

Representative smokes are mechanical packaging checks, not canonical replays or
behavioral results. The later testing-methodology phase must approve enforcement
of the canonical evaluator boundary before establishing a baseline. This
migration does not change the runner or providers.

## Smoke evidence

Each explicit owner approval authorizes one attempt of the catalog plan's
representative scenario from a named commit with clean tracked state. Every
prompt, configuration, declared source, and other arm-defining file must be
tracked and match that commit.

Retain at most one `smoke-result.json` per scenario. It is the runner's exact
`result.json`; do not retain stdout, stderr, final response, rendered prompt,
configuration snapshot, evidence contents, or the temporary bundle.

Apply this disposition to the approved attempt:

| Outcome | Retained state | Catalog disposition |
|---|---|---|
| Published `COMPLETED` result with null infrastructure error | Replace any prior result with the exact new file | Validate completed-state mechanics; satisfy the smoke requirement only when validation passes, otherwise record and stop |
| Published `INFRA_ERROR` result | Replace any prior result with the exact new file | Validate it as the latest blocked-state evidence, record, and stop |
| No published result | Remove any prior result; retain none | Record in the scenario README and catalog plan; stop |

Before discarding a result-producing attempt's bundle, compare the retained file
byte-for-byte with its `result.json` and record the successful comparison in the
catalog plan. For every published result, validate its schema, scenario ID,
configured execution, status/error pairing, and recorded artifacts against the
retained bundle and clean commit. For a `COMPLETED` result, also require the final
fixture inventory to contain exactly the regular files declared by
`test.json.fixtures` at their manifest-recorded targets, bytes, and hashes, plus
only their target-implied parent directories. Require the evidence inventory to
be empty. This comparison is required because the result records post-provider
state.

The representative scenario README links its current result when one exists. If
the attempt publishes no result, it records the explicit no-result failure
instead. Other scenario READMEs state that no current schema `"0.2"` result is
retained. The migration index marks the representative using its documented
entry format.

## Catalog workflow

For each catalog:

1. Create the catalog's sole plan. Make it the complete executable checklist for
   that catalog: enumerate every canonical candidate; define each scenario's
   package, input mapping, provenance, and permitted adaptations; select the
   representative; specify every default configuration's exact provider, model,
   and effort; define catalog-specific acceptance; and include implementation,
   smoke, verification, archive, and merge work.
2. For each candidate, create the scenario README and initial manifest, package
   its prompt, rubric, declared files, and schema `"0.2"` configuration, then
   finalize and reconcile the manifest.
3. Add catalog-specific provider-free acceptance and preflight every
   configuration against its manifest.
4. Commit a clean provider-free catalog state, obtain explicit owner approval,
   and run the approved representative attempt under the smoke contract.
5. Verify the repository, reconcile index totals and roadmap catalog status,
   archive the completed catalog plan, review the branch, and merge it before
   planning the next catalog.

Each catalog uses catalog-specific acceptance. Shared catalog-test helpers remain
outside this migration's scope.

## Provider-free acceptance

Catalog acceptance verifies:

- exact expected scenario directories, canonical-to-runner ID mapping, and
  required package files;
- successful load and preparation of every `test.json`;
- exact prompt, declared-source, target, byte, and hash agreement with each
  provider-input manifest, plus exact rubric agreement with its recorded
  provenance;
- absence of rubric bytes from runner-declared provider input and the prepared
  workspace;
- resolved runner tokens, no stale `supplied-skills/` paths, and empty initial
  evidence;
- no unexpected `smoke-result.json`; when one is present, its schema, identity,
  configured execution, recorded artifacts, and status/error pairing agree with
  the smoke disposition. A `COMPLETED` result additionally satisfies the
  completed-state fixture and evidence requirements above. A retained
  `INFRA_ERROR` is valid blocked evidence but does not satisfy catalog completion.

This is mechanical packaging verification, not behavioral evaluation.

## Fail-closed conditions

Stop and request owner direction when candidate scope, canonical representation,
canonical bytes, rubric identity, or provenance is missing or ambiguous; a
required dependency is unavailable; a scenario requires unsupported runner
behavior; hashes do not reconcile; or faithful packaging requires an unapproved
adaptation.

Do not start a smoke when an arm-defining file is untracked or differs from the
named commit. After an attempt, apply the smoke disposition above and stop unless
the result is `COMPLETED` with null infrastructure error and all completed-state
mechanics validate. Do not repeat the invocation, change the runner, weaken the
scenario, inspect the response semantically, skip the scenario, or mark the
catalog complete without new owner direction. Owner direction may authorize
another invocation or a separately scoped contract change; it cannot make an
incomplete run satisfy the current rule.

These are catalog-plan and acceptance rules, not new hooks, runner validators,
or provider behavior.

## Verification and completion

Each catalog runs the full runner suite, catalog-specific provider-free
acceptance, mandatory repository hook suite, local Markdown-link check, and
`git diff --check`. It receives task review and final whole-branch review before
merge.

Catalog migration does not change the runner, providers, skills, canonical
scenario meaning or input representation, validation methodology, behavioral
scoring, baselines, or raw provider artifacts. Runner changes, scenario redesign,
alternate committed arms, shared dependency storage, shared test helpers,
evaluator-transport enforcement, and testing methodology require separate
approved scope.

Migration is complete when all 105 scenarios have loadable schema `"0.2"`
packages whose manifests, provenance, and provider-free preflight reconcile;
every catalog's representative scenario has one current `COMPLETED` smoke result
matching its clean smoke commit; the index reports none remaining; and every
catalog plan is archived and its catalog is merged.
