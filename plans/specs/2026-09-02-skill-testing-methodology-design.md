# Skill Testing Methodology Design

## Status

Live design started 2026-09-02.
This document records owner-approved methodology decisions as they are made.
It does not authorize a provider run, activate a complete test suite, or authorize
implementation.
The only new tool specified by this design is the mechanical worksheet generator.

## Purpose

Define a repeatable way to use the reusable prompt runner and validation charter to evaluate skill behavior.
The methodology must distinguish semantic behavior from deterministic protocol, preserve enough evidence for independent review, and avoid failing skills for arbitrary formatting differences.

## Authorities

- The [validation charter](../../skill-validation/charter/core-contracts.md) defines skill invariants, evaluation ledgers, and acceptance ownership.
- The [runner contract](../../skill-validation/runner/README.md) defines scenario preparation, model invocation, and mechanical evidence collection.
- The [scenario catalog](../../skill-validation/scenarios/README.md) indexes the migrated prompts, rubrics, configurations, and supplied files.
- The [retired comprehensive cleanup plan](../completed/2026-08-01-comprehensive-skill-cleanup.md) and [design](../completed/specs/2026-08-01-comprehensive-skill-cleanup-design.md) are historical context, not current methodology.

## Responsibility boundary

The runner prepares declared files, renders a prompt, invokes one configured provider, and retains mechanical evidence.
It does not understand skills, apply rubrics, score responses, or assign behavioral verdicts.

The methodology determines whether scenario inputs are valid, maps observable results to charter invariants, records separate ledger scores, and assigns an overall scenario verdict.
The orchestrator reads the raw retained run evidence and owns the final ledger assignments and verdict.

Do not add test tooling until an observed testing need can be simplified by a deterministic program.
Prompting may guide model behavior, but it does not establish determinism.

## Evaluation ledgers

Every scored requirement belongs to exactly one ledger.

| Ledger | Score | Effect |
|---|---|---|
| Semantic behavior | `PASS`, `FAIL`, or `NOT_JUDGEABLE` per applicable charter invariant | Blocks the scenario verdict. |
| Deterministic protocol | `PASS`, `FAIL`, or `NOT_JUDGEABLE` per applicable requirement; one ledger-level `N/A` row when no requirement applies | Blocks when a real authenticated renderer, validator, parser, or production consumer applies. |
| Task or fixture fidelity | `PASS`, `FAIL`, or `NOT_JUDGEABLE` | Does not block unless the defect prevents semantic or protocol judgment. |
| Readability | Recorded separately when the scenario is designed to evaluate it | Never substituted for semantic or protocol evidence. |
| Infrastructure | `COMPLETED` or an infrastructure failure | An infrastructure failure is not a scored result and remains scratch-only. |

Do not combine ledger results into a numeric score, percentage, weighted total, or average.
The worksheet preserves the cause of each result so the orchestrator can assign the scenario verdict directly.

## Scenario verdict

The orchestrator applies these rules in order so no result matches two verdicts:

| Priority | Condition | Scenario disposition or verdict |
|---|---|---|
| 1 | The runner reports an infrastructure failure. | `INFRA_RETRY`; scratch-only and not scored. |
| 2 | Any applicable semantic or deterministic-protocol row is `NOT_JUDGEABLE`, or a task/fixture-fidelity defect prevents semantic or protocol judgment. | `SCENARIO_INVALID`; scratch-only. |
| 3 | The remaining judgeable semantic or applicable deterministic-protocol rows contain any `FAIL`. | `FAIL`. |
| 4 | Every semantic row and every applicable deterministic-protocol row is `PASS`, or no deterministic protocol applies and the ledger contains one explicit `N/A` row with its rationale. | `PASS`. |

`FAIL` is a valid accepted result when the scenario and evidence are judgeable.
The semantic and protocol rows record whether the failure was semantic, deterministic, or both.
`SCENARIO_INVALID`, row-level `NOT_JUDGEABLE`, and infrastructure failures are not accepted test results.

Task-fidelity differences remain visible but do not change a semantic pass into a failure unless they prevent judgment.
Equivalent wording, punctuation, capitalization, ordering, and rendering pass unless an applicable deterministic consumer requires them.

## Determinism and skill rewrites

For every skill rule or output requirement, determine whether it is semantic judgment, deterministic protocol, or task fidelity.

- Skills own judgment, sequencing, boundaries, tool selection, and handling of tool failure.
- Justified deterministic tools own syntax, rendering, parsing, validation, and mechanical evidence.
- A real consumer requirement or observed reliability failure must justify deterministic tooling.
- If no deterministic consumer or need exists, relax or remove exact formatting requirements rather than inventing a validator.
- A prompt-based checker may provide advisory judgment, but it does not satisfy the deterministic-protocol ledger.

Later skill rewrites use this classification consistently.
Format-heavy prose should move to a small authenticated tool when exactness is necessary and observed evidence shows that the move improves reliability or simplifies the skill.

## Evidence lifecycle

All attempts remain in scratch space during the active evaluation cycle.
Rejected attempts, invalid scenarios, infrastructure failures, logs, duplicated stdout or stderr, and temporary rendered paths are discarded after that cycle.

Each scenario maintains one replaceable accepted record for its latest valid test result at
`skill-validation/scenarios/<catalog>/<scenario-id>/accepted/`:

```text
accepted/
  worksheet.md
  result.json
  final.txt
  evidence/       # only when produced evidence is used for judgment
```

- `worksheet.md` records run identity, input and skill hashes, charter mappings, evidence references, ledger judgments, and the orchestrator verdict.
- `result.json` is the runner's exact mechanical result and artifact digest record.
- `final.txt` is the exact response that was evaluated.
- `evidence/` contains only model-produced files used for judgment.
- The scenario's checked-in prompt, rubric, configuration, and fixtures remain the single source for inputs and are not duplicated in the accepted record.

A later accepted run replaces these files in place.
Earlier accepted records remain recoverable through Git history alongside the corresponding skill and scenario versions.
Unaccepted scratch attempts are intentionally not historical records.

Acceptance means the run completed mechanically, the scenario was valid, the evidence was sufficient, and the worksheet received orchestrator review.
Acceptance does not mean the skill passed: both `PASS` and judgeable `FAIL` results may become the latest accepted record.

## Worksheet

The worksheet records:

1. scenario package path and ID, plus a blank purpose field for the orchestrator;
2. supplied skill paths and content hashes as ordinary executed fixture entries;
3. prompt, rubric, configuration, and remaining fixture hashes;
4. provider, model, effort, and run ID;
5. infrastructure outcome;
6. one row per applicable charter invariant with `PASS`, `FAIL`, or `NOT_JUDGEABLE`, plus a precise evidence reference;
7. deterministic-protocol rows or an explicit `N/A` rationale;
8. task or fixture fidelity observations;
9. readability observations when applicable;
10. overall orchestrator verdict;
11. ambiguities, scenario defects, and methodology changes revealed by the run; and
12. acceptance or scratch-only disposition.

### Deterministic worksheet generation

A small deterministic tool generates the fixed `worksheet.md` representation.
The tool owns the Markdown layout, mechanically derived run metadata and hashes,
and only the structural checks necessary to produce output that adheres to the
worksheet specification.
It reads the scenario package and one retained runner bundle, prefills only the
mechanical fields available from those inputs, and leaves every assessment field
blank for the orchestrator.
It does not require a structured judgment input.

The command interface is:

```text
skilltest worksheet SCENARIO RUN_BUNDLE --output PATH
```

`SCENARIO` is the scenario package directory, `RUN_BUNDLE` is one retained runner
bundle, and `PATH` is an explicit scratch output path.
The command never selects or writes a scenario's `accepted/` location implicitly.
The orchestrator invokes the command from the repository root and passes `SCENARIO`
as a repository-relative path so a later accepted worksheet remains portable.
The generator records that argument as supplied and does not discover or validate a
repository root.

The minimal command contract is:

- `SCENARIO` must be a readable directory containing readable `rubric.md`.
- `RUN_BUNDLE` must be a readable directory containing a parseable `result.json`
  with the fields used by the fixed worksheet.
- `PATH` must not exist, and its parent directory must already exist.
- Success writes the worksheet, exits `0`, prints the resolved output path followed
  by one LF to standard output, and writes nothing to standard error.
- Command-line misuse or an unreadable, malformed, or incomplete input exits `2`,
  writes one `skilltest:` diagnostic to standard error, writes nothing to standard
  output, and does not create `PATH`.
- An output collision or write failure exits `1`, writes one `skilltest:` diagnostic
  to standard error, writes nothing to standard output, and never overwrites an
  existing file.

The generator parses only the existing fields it must render.
It does not validate `result.json` against its schema, compare scenario and run
identities, inspect response or evidence content, or create output directories.

The implementation scope is limited to the new CLI subcommand and the rendering
code needed to read the existing scenario and runner-bundle records, hash the
withheld rubric, and write the specified blank worksheet.
Focused tests and the runner README cover that command.
Do not change `skilltest run`, provider adapters, configuration or result schemas,
scenario packages, or skills; add a dependency or schema; validate or calculate an
assessment; copy an accepted record; or add lifecycle, scoring, or suite machinery.

### Evaluation workflow

1. The orchestrator audits and selects one scenario.
2. The orchestrator obtains any required authorization for the exact provider
   invocation.
3. The orchestrator executes `skilltest run` for that scenario configuration.
4. The runner performs one model invocation and retains its mechanical run bundle.
5. The orchestrator executes `skilltest worksheet` against the scenario package and
   retained run bundle.
6. The worksheet tool writes an unscored scratch worksheet with only mechanical
   fields populated.
7. The orchestrator examines `final.txt`, `result.json`, produced evidence, the
   withheld rubric, and the applicable charter invariants.
8. The orchestrator fills the assessment fields and assigns the scenario verdict.
9. After the required review, a judgeable `PASS` or `FAIL` result may replace the
   scenario's `accepted/` record.

The orchestrator invokes worksheet generation explicitly.
The runner does not invoke it automatically, score the response, or decide whether
a completed bundle is worth evaluating.

The orchestrator continues to own the substantive inputs: applicable invariant
mapping, each ledger judgment, precise evidence references, observations, overall
verdict, and acceptance decision.
The generator must not infer a judgment from the rubric or response, invoke a
model, calculate or reconcile a verdict, evaluate evidence references, or turn
task-fidelity observations into blocking failures.
It renders only the mechanical inputs and blank assessment structure; conformance
to the worksheet output specification is not verification that a later assessment
is coherent or correct.

Generation occurs in scratch first.
Producing a structurally valid worksheet does not accept a run or write the
scenario's `accepted/` record without the required orchestrator review.

### First-cut worksheet layout

The generated worksheet uses these sections in order:

1. **Run identity:** scenario path and ID, run ID, provider, model, effort, and
   timestamps.
2. **Infrastructure:** runner status and any recorded infrastructure error.
3. **Executed inputs:** retained configuration, prompt-template, rendered-prompt,
   fixture, and supplied-skill paths and hashes.
4. **Withheld evaluation input:** scenario rubric path and hash.
5. **Semantic behavior:** blank rows for invariant, criterion, score, evidence, and
   notes.
6. **Deterministic protocol:** blank rows for requirement, score, evidence, and
   notes.
7. **Task fidelity:** blank rows for requirement, score, evidence, and notes.
8. **Readability:** blank observation and evidence fields.
9. **Verdict:** blank verdict, rationale, and accepted-or-scratch disposition.
10. **Methodology notes:** blank fields for ambiguities, scenario defects, and
    proposed methodology changes.

The generator prefills the mechanical slots in sections 1 through 4 from explicit
paths and retained records without interpreting scenario prose; the scenario-purpose
cell remains blank.
Supplied skills remain ordinary fixture rows; the generator does not classify or
handle them separately.
It renders sections 5 through 10 as blank scoring structure for the orchestrator.
When completing the worksheet, the orchestrator preserves every generated heading,
column, row label, and mechanical value.
It fills the empty cells and duplicates only the blank assessment rows when a ledger
needs additional entries, preserving the existing column order.
If no deterministic protocol applies, it uses the single generated protocol row,
enters `N/A` in `Score`, and records the rationale in `Notes`.
Applicable protocol requirements use separate rows and never use `N/A`.
The orchestrator applies the same table-cell escaping rule defined below to every
value it enters.
No post-edit validator is required.

The first-cut output is UTF-8 Markdown with LF line endings and one trailing LF.
It uses these literal headings, fields, and table columns:

```text
# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | <SCENARIO argument> |
| Scenario ID | <result test ID> |
| Scenario purpose |  |
| Run ID | <run ID> |
| Provider | <provider> |
| Model | <model> |
| Effort | <effort> |
| Started | <started timestamp> |
| Finished | <finished timestamp> |
| Duration seconds | <duration> |

## Infrastructure

| Field | Value |
|---|---|
| Status | <runner status> |
| Error code | <error code or empty> |
| Error message | <error message or empty> |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | <retained config path> | <digest> |
| Prompt template | <retained prompt-template path> | <digest> |
| Rendered prompt | <retained prompt path> | <digest> |
| Fixture | <retained fixture-entry path> | <fixture-entry digest> |
<repeat the preceding Fixture row once per additional regular file>

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | <scenario rubric path> | <digest> |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
|  |  |  |  |  |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
|  |  |  |  |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
|  |  |  |  |

## Readability

| Observation | Evidence |
|---|---|
|  |  |

## Verdict

| Field | Value |
|---|---|
| Overall verdict |  |
| Rationale |  |
| Disposition |  |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities |  |
| Scenario defects |  |
| Proposed methodology changes |  |
```

Angle-bracketed text above identifies mechanical substitution slots and is not
emitted literally.
The scenario rubric path is the supplied `SCENARIO` text followed by `/rubric.md`;
when `SCENARIO` already ends in `/`, append `rubric.md` without adding another slash.
Fixture rows retain the lexicographic order already recorded in `result.json`.
When the fixture inventory has no regular files, emit no Fixture row.
Render a JSON `null` digest or infrastructure-error value as an empty cell.
Render `duration_seconds` with Python's `str()` representation of the parsed JSON
number.
For inserted table values, normalize CRLF and bare carriage return to line feed,
then replace `\` with `\\`, `|` with `\|`, and line feed with `<br>` in that order.
All assessment cells are emitted empty exactly as shown.

The first cut may be revised from pilot evidence; speculative fields are not added
before then.

## Initial manual pilot

The first pilot uses [`DR-02`](../../skill-validation/scenarios/disciplined-research/dr-02/README.md).
It validates the low-level methodology before introducing test-operator subagents,
scorer agents, repetitions, control arms, suite automation, or tooling beyond the
worksheet generator.

The orchestrator:

1. audits the scenario package and charter mapping;
2. presents the pre-run audit to the owner;
3. obtains explicit approval for the exact provider invocation;
4. runs the existing configuration once;
5. inspects the complete retained response and evidence;
6. completes the worksheet;
7. decides whether the scenario is judgeable; and
8. records methodology defects before attempting another scenario.

The subject model receives the prompt and declared fixtures but never the rubric.
Historical `DR-02` results inform methodology risks but do not count as pilot evidence.

### `DR-02` pre-run audit

The packaged prompt and three source files match their recorded canonical provenance.
The live `disciplined-research` skill is the only supplied skill.
The rubric is absent from declared and prepared provider input.
The existing provider-free catalog acceptance check prepares the package successfully and begins with empty evidence.

| Ledger | Pilot criterion |
|---|---|
| Semantic `DR-I1` | State September 22, 2026 as the corrected calendar date, do not accept September 15 as controlling, and support every deadline fact actually stated. |
| Semantic `DR-I2` | Resolve the conflict in favor of Official Addendum 2. |
| Semantic `DR-I3` | Map the conclusion precisely to `sources/city-museum-addendum-2.md`. |
| Semantic `DR-I4` | Add no unsupported factual claims. |
| Deterministic protocol | `N/A`; no authenticated consumer parses this response. |
| Task fidelity | Provide the complete corrected deadline, including time zone, in the requested two-line form without blocker, preface, postscript, or process narration. |
| Readability | Not independently scored in this pilot. |
| Infrastructure | The runner result must be mechanically `COMPLETED`. |

Semantic equivalence passes.
For example, `September 22, 2026 at 5 PM Eastern` is equivalent to the fixture wording.
Omitting the time, time zone, or requested two-line rendering is a task-fidelity
failure, not a semantic failure.
Omitting the corrected calendar date, repeating September 15 as controlling,
inventing another date, selecting the wrong authority, or falsely mapping support
is a semantic failure.

## Decisions still open

- The exact provider, model, effort, and owner-authorized invocation for the first pilot.
- The review required before an accepted record replaces its predecessor.
- When repeated runs, comparison arms, or advisory scorers become justified.
- When the manual workflow is stable enough to hand execution and draft scoring to a bounded test subagent.
- How scenario-level accepted results roll up to skill-level and suite-level status.
