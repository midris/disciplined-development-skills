# Study formats

The [field contracts](companion-formats.md) implement the [agreed spec](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#working-artifact-organization).
Current format set: `2-draft`; final version-1 acceptance and collection freeze remain pending.

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

Use the [schema](execution-result.schema.json) and blank template for new records.
The schema validates one execution and its functional rollup, not batch acceptance, evidence correctness or causal attribution.
`judgment` is `met`, `not met` or `insufficient evidence`; reasons explain the outcome, not a hidden graded score.
Shared rules and input identities resolve through the manifest; record per-execution evidence and exceptions locally.
An invalid setup limits the assessment even if a resulting artifact can be inspected.
Before accepting a result, verify schema conformance, identities, unique IDs, applicable criterion coverage and evidence references.
The [companion contract](companion-formats.md#execution-results-and-batch-assessment) defines aggregation and the separate batch assessment.

Run `skill-validation/runner/.venv/bin/python -m unittest discover -s skill-studies/formats` from the repository root.
For a completed result, load `execution-result.schema.json` with the runner environment's `jsonschema.Draft202012Validator` and validate the record.
The blank template intentionally fails completed-record validation.
No batch validator or generator is implemented; explicit contract checks suffice until the planned document tooling after baseline assessment.

## Historical example

The [policy-3 pilot-02 example](../sweeping-stale-references/assessments/pilot-02-original-policy-3-example.json) remains byte-for-byte unchanged in format `1-draft`.
It illustrates evidence and criterion reasoning from one retained execution, not batch reliability or a replacement pilot assessment.
Its [index](../sweeping-stale-references/assessments/index.json) pins the original schema and the cited historical run index by full Git revision, path and SHA-256.
Retrieve those bytes with `git show <git_revision>:<path>` and verify the hash before validation; do not apply the current schema to that historical record.
The old schema lives in Git rather than a duplicate archive or compatibility branch in the current schema.
