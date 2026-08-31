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

## disciplined-research

Representative smoke: [`DR-01`](disciplined-research/dr-01/README.md)

- [`DR-01`](disciplined-research/dr-01/README.md) — Prefer current implementation over stale project documentation and correct a peer-fed retention claim with a source.
- [`DR-02`](disciplined-research/dr-02/README.md) — Use a later controlling first-party addendum to disconfirm a supplied museum-procurement deadline.
- [`DR-03`](disciplined-research/dr-03/README.md) — Verify project and upstream version state separately and correct a cross-domain claim.
- [`DR-04`](disciplined-research/dr-04/README.md) — Apply acquire, verify, and source-disclosure rules to a private scratch note while mapping one source to multiple claims.
- [`DR-05`](disciplined-research/dr-05/README.md) — Refuse to invent a datum missing from the only supplied source despite pressure for an uncaveated casual answer.
- [`DR-06`](disciplined-research/dr-06/README.md) — Present an unsupported cause only as a stamped unverified investigation lead without attaching unrelated evidence as support.
- [`DR-07`](disciplined-research/dr-07/README.md) — Correct a conversational premise and derive only the supported fifteen-minute result with source disclosure.

## disciplined-development

Representative smoke: [`DD-04`](disciplined-development/dd-04/README.md)

- [`DD-01`](disciplined-development/dd-01/README.md) — Select the due parent modes, gates, principles, artifacts, outcomes, blocked transitions, and owner seams across eight independent vignettes.
- [`DD-02`](disciplined-development/dd-02/README.md) — Preserve Gate 1–5 timing and order, parent artifacts and destinations, fail-closed transitions, and owner boundaries through one fixed sequence.
- [`DD-03`](disciplined-development/dd-03/README.md) — Apply Principle 7 only for contract, reachable accepted input, observed use, or robust invariants rather than speculative scale.
- [`DD-04`](disciplined-development/dd-04/README.md) — Ground a factual deployment premise before action, keep action blocked, and leave research procedure to the companion skill.
- [`DD-05`](disciplined-development/dd-05/README.md) — Read governing sources, surface a plan/spec conflict, verify a recalled capability, and block planning and implementation.
- [`DD-06`](disciplined-development/dd-06/README.md) — Require signed written scope to preserve a chosen spelling and an intentional deferral before delegation, planning, or coding.
- [`DD-07`](disciplined-development/dd-07/README.md) — Keep delegation inside signed scope, require directly observed RED before production edits, and retain parent acceptance authority.
- [`DD-08`](disciplined-development/dd-08/README.md) — Dispose of unauthorized work before direct CLI evidence, reference reconciliation, truthful bookkeeping, and one coherent green commit.
- [`DD-09`](disciplined-development/dd-09/README.md) — Require whole-tree review, scope resolution, refreshed evidence, clean review and smoke, and finishing before PR creation.

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
- `disciplined-development`: 9 total, 9 migrated, 0 not migrated
- `disciplined-research`: 7 total, 7 migrated, 0 not migrated
- `dispatching-development-subagents`: 11 total, 0 migrated, 11 not migrated
- `lean-plan-writing`: 7 total, 7 migrated, 0 not migrated
- `skill-discovery`: 12 total, 0 migrated, 12 not migrated
- `sweeping-stale-references`: 6 total, 6 migrated, 0 not migrated
- `writing-explicit-rationale`: 6 total, 6 migrated, 0 not migrated
- Overall: 105 total, 35 migrated, 70 not migrated
