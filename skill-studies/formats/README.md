# Score records

The [schema](score-record.schema.json), [blank template](score-record.template.json) and [filled SSR example](../sweeping-stale-references/assessments/pilot-02-original-policy-3-example.json) are draft version `1-draft` for format review before the next scored collection.
They implement the [fixed scoring contract](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#fixed-scoring-rules-and-score-records); the remaining protocol, case, index, manifest and lifecycle formats are not frozen by this draft.

The active agent or human copies the template, reads the identified policy and case criteria, inspects the retained run, and completes one record.
The blank template deliberately fails completed-record validation: replace empty fields, list every applicable criterion and supply evidence before recording a result.
Use `null` for unavailable assessor model/session identity, an absent target skill in a control, or no superseded assessment; explain consequential limits in context or uncertainty.
Paths are repository-relative or absolute for private evidence; hashes identify file bytes, and selectors identify JSON fields, trace lines or other precise locations within them.
Evidence IDs must be unique, and criterion/setup/observation evidence lists refer to those IDs.
Keep trace payloads in their retained bundle; cite them rather than copying full transcripts into Git.

Record functional and procedural judgments separately under the case's agreed consequences.
The schema checks the three-state functional rollup, not semantic correctness or a skill's procedural severity.
A `met` audit-usefulness criterion can coexist with an explicit secondary accuracy defect when the registered criterion and policy permit that distinction, as in the example; it must not be presented as flawless compliance.
Control records describe observed procedure without imposing target instructions that were not supplied.
Setup is separate: an invalid or uncertain setup cannot substantiate a skill-effectiveness claim, even when the final artifact can be inspected.

Before accepting a completed record, check it against the schema, then verify all paths/hashes, unique criterion and evidence IDs, evidence-reference resolution, and coverage against the identified criteria.
Check that reasons support judgments and consequences follow the policy; the schema cannot do this judgment work.
Index the record's path/hash with its run identity; reassessments identify any record they supersede while preserving the prior bytes.
The example has a [separate index](../sweeping-stale-references/assessments/index.json), so the original pilot's run index and policy-2 assessment remain unchanged.

From the repository root, validate a completed record with the runner's existing environment:

```sh
skill-validation/runner/.venv/bin/python - <<'PY'
import json
from pathlib import Path
from jsonschema import Draft202012Validator
schema = json.loads(Path('skill-studies/formats/score-record.schema.json').read_text())
record = json.loads(Path('skill-studies/sweeping-stale-references/assessments/pilot-02-original-policy-3-example.json').read_text())
Draft202012Validator.check_schema(schema)
Draft202012Validator(schema).validate(record)
print('Record structure and functional rollup conform; inspect identities and judgments separately.')
PY
```

Run the format's contract checks with `skill-validation/runner/.venv/bin/python -m unittest discover -s skill-studies/formats`.
These use the runner's existing `jsonschema` dependency and invoke no models.
A template generator and integrated conformance CLI remain deferred until format agreement and baseline assessment, as the plan specifies.
