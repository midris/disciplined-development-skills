# Scenario migration index

Canonical source commit: `13599fb7d3127334b0d07bfe468767e586ec5f9c`.

Active packaging schema: `"0.2"`.

This index tracks schema `"0.2"` migration output. The canonical commit above is
the scenario and scope authority; the single plan for each catalog enumerates its
exact active scenarios from that source before migration.

No scenario packages have migrated under schema `"0.2"`. As each package
migrates, add its one-line purpose summary and scenario README link beneath its
catalog. Keep detailed package, provenance, and smoke facts in the scenario
README rather than duplicating them here.

## Entry format

Use the identities defined by the migration design. A migrated catalog has one
representative line followed by its scenario entries:

```text
## catalog-name

Representative smoke: [`SCENARIO-ID`](README.md)

- [`SCENARIO-ID`](README.md) — One-line purpose summary.
```

Replace each example `README.md` target with that scenario package's relative
README path. The representative line identifies the catalog's sole representative
scenario for schema `"0.2"` migration smoke attempts. Scenario READMEs own the
current retained-result or no-result status.

## Prompt anatomy

Every `prompt.md` is independently readable and accounts for each applicable
semantic element:

1. evaluator boundary and permissions;
2. arm-selected context, inline or through supplied files;
3. scenario-owned files;
4. task context;
5. requested output;
6. mutation and process-narration restrictions.

This is a common file-based starting template, not a mandatory ordering rule.
Preserve the canonical relative ordering of scenario material, then replace
every angle-bracket placeholder:

```text
Act as a fresh evaluator. Use only this prompt and the supplied files.
Read {{fixture_dir}}/skills/example/SKILL.md completely and follow it.
Read {{fixture_dir}}/project/input.md.

Task:
<Perform the canonical scenario task.>

Return:
<State the canonical output contract.>

Do not modify files, dispatch agents, or narrate your process. Return only the requested artifact.
```

Omit file-reading lines a scenario does not need. Add canonical inline context or
additional declared-file instructions where its provider-input manifest requires
them. Do not expose the evaluator-withheld rubric.

## Totals

- `adversarial-review`: 15 total, 0 migrated, 15 not migrated
- `adversarial-review-loop`: 15 total, 0 migrated, 15 not migrated
- `concise-writing`: 17 total, 0 migrated, 17 not migrated
- `disciplined-development`: 9 total, 0 migrated, 9 not migrated
- `disciplined-research`: 7 total, 0 migrated, 7 not migrated
- `dispatching-development-subagents`: 11 total, 0 migrated, 11 not migrated
- `lean-plan-writing`: 7 total, 0 migrated, 7 not migrated
- `skill-discovery`: 12 total, 0 migrated, 12 not migrated
- `sweeping-stale-references`: 6 total, 0 migrated, 6 not migrated
- `writing-explicit-rationale`: 6 total, 0 migrated, 6 not migrated
- Overall: 105 total, 0 migrated, 105 not migrated
