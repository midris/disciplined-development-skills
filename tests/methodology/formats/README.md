# Study formats

The [field contracts](companion-formats.md) implement the [agreed spec](../framework.md#working-artifact-organization).
Current format set: `1`, with accepted result and assessment version `2` for unmeasured functional outcomes. Collection scope and dispatch require their own recorded authority.

| Artifact | Owns |
|---|---|
| [Protocol](protocol.template.md) | Study agreement, scope, policy, accounting and owner decisions. |
| [Case definition](case-definition.template.md) | Criterion boundaries and evidence rules; see the [filled criterion](semantic-delivery-criterion-example.md). |
| [Manifest](manifest.template.json) | Frozen input identities; configurations own mappings/settings. |
| [Attempt index](run-index.template.json) | Each actual attempt, authorization, call charge, retained bundle and execution-result link. |
| [Execution result](execution-result.template.json) | One execution's criterion outcomes, reasons, evidence and uncertainty. |
| [Batch assessment](assessment.template.md) | Aggregates, failure patterns, limits and any comparison using those same results. |

These are distinct responsibilities, not separate assessment processes.
A separate comparison report is unnecessary; study decisions remain in the protocol.
Keep detailed outputs/traces in the retained bundles and cite them from execution results.
The active agent or human inspects evidence supporting passes as well as failures; outcome labels do not replace evidence or reasoning.

## Execution results

Manifest authorities pin regular files in Git. The generated manifest uses `tests/runner/src/skilltest/_formats/execution-result.schema.json`. For version 2, pin `execution-result-v2.schema.json` in the same directory. The adjacent links are for browsing.

Use the [version-1 schema](execution-result.schema.json) and blank template for functional assessments, or the [version-2 schema](execution-result-v2.schema.json) and [template](execution-result-v2.template.json) when recording unmeasured functional outcomes.
The schema validates one execution and its functional rollup, not batch acceptance, evidence correctness or causal attribution.
`judgment` is `met`, `not met` or `insufficient evidence`; reasons explain the outcome, not a hidden graded score.
Shared rules and input identities resolve through the manifest; record per-execution evidence and exceptions locally.
An invalid setup limits the assessment even if a resulting artifact can be inspected.
Before accepting a result, verify schema conformance, identities, unique IDs, applicable criterion coverage and evidence references.
The [companion contract](companion-formats.md#execution-results-and-batch-assessment) defines aggregation and the separate batch assessment.

Run `tests/runner/.venv/bin/python -m unittest discover -s tests/methodology/formats` from the repository root.
For a completed result, load the schema selected by its version and pinned manifest with the runner environment's `jsonschema.Draft202012Validator` and validate the record.
The blank template intentionally fails completed-record validation.
The [document CLI](../../runner/README.md#study-documents) generates these six drafts and checks structures, identities, evidence, coverage and aggregate arithmetic. Use `skilltest docs check protocol.md --ready-for assessment --batch ID` for a selected batch; ordinary file checking does not certify the whole study. Supported Markdown representations and unsupported-version behavior are documented in that guide.

Use `docs manifest` to prepare/freeze the existing identities, `docs retain` to preserve and register a stopped attempt, and `docs tables` to derive tables from recorded judgments.
Run `docs check PROTOCOL --ready-for preparation --batch ID` before committing inputs, then use collection readiness after freezing.
These operations use the existing formats; see the [command guide](../../runner/README.md#mechanical-study-operations) for arguments and failure handling.

## Procedural-only diagnostics

Use `docs new result --format-version 2` and `docs new assessment --format-version 2` (each with `--output PATH`) for procedural-only evidence.
Version 2 adds `functional_result: "not measured"` and an explicit aggregate column; it does not add a criterion judgment or change functional scoring.
Validate version-2 records against `execution-result-v2.schema.json`.
Version-1 templates, schemas and existing records remain unchanged.
See the [companion contract](companion-formats.md#execution-results-and-batch-assessment) for inclusion and denominator rules.

## Historical example

The [historical example index](../examples/index.json) identifies the original worked assessment, schema and run index by full Git revision, path and SHA-256.
Fetch the archival tag from a main-only checkout and inspect the original bytes:

```sh
git fetch origin tag archive/study-foundation-sources
git show 3ba9169ee0de0db44e4014c31fbccb3abc921a94:skill-studies/sweeping-stale-references/assessments/pilot-02-original-policy-3-example.json | shasum -a 256
```

Compare the digest with the index before interpreting the record. Its original absolute evidence paths describe the operator's controlled store. The [offline walkthrough](../../README.md#walk-through-a-study-offline) supplies locally retrievable evidence for a new example.
