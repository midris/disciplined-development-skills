# Scenario migration index

Canonical source commit: `13599fb7d3127334b0d07bfe468767e586ec5f9c`.

Active packaging schema: `"0.2"`.

This index tracks schema `"0.2"` migration output. The canonical commit above is
the scenario and scope authority; the single plan for each catalog enumerates its
exact active scenarios from that source before migration.

As each package migrates, add its one-line purpose summary and scenario README
link beneath its catalog. Keep detailed package, provenance, and smoke facts in
the scenario README rather than duplicating them here.

## writing-explicit-rationale

Representative smoke: [`WER-07`](writing-explicit-rationale/wer-07/README.md)

- [`WER-01`](writing-explicit-rationale/wer-01/README.md) — Apply a small direct plan descope while retaining its selected scope, cause, accepted impact, and adjacent rationale.
- [`WER-02`](writing-explicit-rationale/wer-02/README.md) — Turn repeated review into a batched durable audit while distinguishing consequential choices from a consequence-free choice.
- [`WER-05`](writing-explicit-rationale/wer-05/README.md) — Reference an existing authoritative rationale instead of duplicating it under reviewer pressure.
- [`WER-06`](writing-explicit-rationale/wer-06/README.md) — Retain only history that constrains current correctness or future decisions.
- [`WER-07`](writing-explicit-rationale/wer-07/README.md) — Exercise rationale, research, plan-writing, and parent-doctrine composition against multiple primary-source files.
- [`WER-08`](writing-explicit-rationale/wer-08/README.md) — Apply the rationale policy outside software by placing a repeatedly requested cause in a durable nonprofit policy.

## sweeping-stale-references

Representative smoke: [`SSR-01`](sweeping-stale-references/ssr-01/README.md)

- [`SSR-01`](sweeping-stale-references/ssr-01/README.md) — Exercise an end-to-end load-bearing rename with complete discovery, rationale-preserving reconciliation, durable sweep evidence, and verification.
- [`SSR-02`](sweeping-stale-references/ssr-02/README.md) — Treat one reviewer hit as a sample and reconcile a complete cross-category search inventory.
- [`SSR-03`](sweeping-stale-references/ssr-03/README.md) — Group a large sweep only by path and outcome while retaining precise locations, counts, and complete evidence.
- [`SSR-05`](sweeping-stale-references/ssr-05/README.md) — Record the required truthful negative sweep form for a single-file change with no sibling matches.
- [`SSR-06`](sweeping-stale-references/ssr-06/README.md) — Identify exactly the symbol, attached-rationale, and documentation updates required by the session rename.
- [`SSR-07`](sweeping-stale-references/ssr-07/README.md) — Preserve the partner constraint and accepted refresh cost while renaming the session-setting rationale.

## lean-plan-writing

Representative smoke: [`LP-01`](lean-plan-writing/lp-01/README.md)

- [`LP-01`](lean-plan-writing/lp-01/README.md) — Preserve the upstream plan scaffold, TDD order, concrete files, rigor, and commit cadence while applying lean prose density.
- [`LP-02`](lean-plan-writing/lp-02/README.md) — Keep implementation bodies and copyable templates out of a detailed parser task while preserving exact behavior through a complete tricky-case table.
- [`LP-03`](lean-plan-writing/lp-03/README.md) — Permit exactly one bounded illustrative snippet when prose alone cannot specify an exact four-line artifact.
- [`LP-05`](lean-plan-writing/lp-05/README.md) — Name and disposition absent, malformed, out-of-scale, uniqueness, atomicity, and actionable-error cases without embedding implementation bodies.
- [`LP-06`](lean-plan-writing/lp-06/README.md) — Name and disposition quiet failure, scale, overlap, idempotency, quota, isolation, and timezone cases.
- [`LP-07`](lean-plan-writing/lp-07/README.md) — Split oversized independently deployable work at qualitative review boundaries while preserving dependency order.
- [`LP-08`](lean-plan-writing/lp-08/README.md) — Keep a small genuinely coupled rename in one atomic branch and merge.

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
additional file-reading instructions for files declared by `test.json`. Do not
expose the evaluator-withheld rubric.

## Totals

- `adversarial-review`: 15 total, 0 migrated, 15 not migrated
- `adversarial-review-loop`: 15 total, 0 migrated, 15 not migrated
- `concise-writing`: 17 total, 0 migrated, 17 not migrated
- `disciplined-development`: 9 total, 0 migrated, 9 not migrated
- `disciplined-research`: 7 total, 0 migrated, 7 not migrated
- `dispatching-development-subagents`: 11 total, 0 migrated, 11 not migrated
- `lean-plan-writing`: 7 total, 7 migrated, 0 not migrated
- `skill-discovery`: 12 total, 0 migrated, 12 not migrated
- `sweeping-stale-references`: 6 total, 6 migrated, 0 not migrated
- `writing-explicit-rationale`: 6 total, 6 migrated, 0 not migrated
- Overall: 105 total, 19 migrated, 86 not migrated
