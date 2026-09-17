# Study document tooling proposal

Status: owner accepted the simplifications below for documentation; implementation scope/effort remains proposed, with no coding or model calls authorized by this document.
Authority: the [agreed framework's tooling requirements](2026-09-11-model-driven-skill-testing-framework.md#format-decisions-and-document-tooling) and [accepted format contracts](../../skill-studies/formats/companion-formats.md).
The [active plan](../2026-09-11-model-driven-skill-testing.md#document-tooling-after-baseline-collection) owns implementation progress; this proposal settles the tool interface, not the study workflow or scoring rules.

## Purpose and smallest useful scope

The baseline required repeated explicit checks of schemas, applicable criteria, Git retrieval, hashes, evidence links, planned/actual coverage and aggregate arithmetic.
Those checks currently combine the execution-result schema with session-specific scripts; the [format guide](../../skill-studies/formats/README.md) confirms that no batch validator or generator exists.
A reusable command makes the same mechanical checks available next session and in the next study without reconstructing them.
Generation saves template copying and makes the supported version explicit; validation supplies most of the value.

Recommend two subcommands in the existing non-shipped `skilltest` CLI, using shared versioned definitions for the six accepted artifact kinds: protocol, case, manifest, index, result and assessment.
Generate one unfinished artifact at a time; omit a whole-study scaffolder from this first implementation because the existing layout already supplies that guidance.
Keep Markdown narratives and JSON records in their accepted locations.
The alternative is continuing explicit session checks, which remains sufficient for the completed baseline but repeats mechanical work; a service, workflow engine or automatic assessor has no demonstrated need here.

## Proposed interface

These commands are proposals, not currently executable interfaces.

| Command | Effect |
|---|---|
| `skilltest docs new KIND --output PATH --format-version 1` | Create the accepted draft with unfinished content; fail if the output exists. No judgments, approvals or fabricated evidence. |
| `skilltest docs check PATH` | Read one artifact and its relevant references; report structural conformance and unresolved completion requirements. |
| `skilltest docs check PROTOCOL --ready-for collection` | Follow the protocol's declared scope and require identified cases/configurations, criteria/policy, frozen/retrievable sources and recorded scope/authority references. |
| `skilltest docs check PROTOCOL --ready-for assessment` | Follow the protocol's declared batch and require applicable execution results, reconciled attempts/coverage, evidence identities and correct aggregate counts. |

`--json` selects machine-readable diagnostics for either check mode; text is the default.
`--batch ID` selects a declared batch when readiness checking a study with several batches; ambiguous selection is an error, not a guessed scope.
Whole-study readiness checks start only from the protocol file, which already owns scope; this avoids multiple discovery paths and inferred scope.
Individual-file checks remain available but cannot certify a whole batch.
Diagnostics identify the file and field/line, failed rule and expected correction.
Exit 0 means the requested mechanical checks passed, 1 means a conformance/readiness failure, and 2 means invalid usage or a check could not be completed, including unsupported versions or representations.
Default checking may accept an explicitly unfinished draft structurally; readiness checking cannot accept unresolved required values.
Readiness never establishes actual owner consent, semantic correctness or readiness to adopt a skill.

## Checks and boundaries

Use the accepted definitions for sections/fields, types, enums, IDs, criterion applicability and functional rollup.
Resolve repository identities at their declared Git revision and external evidence by its recorded path/hash; report unavailable evidence instead of treating it as success.
Follow selected scope and explicit references, rather than counting every case directory or historical record as active evidence.
Reconcile planned repetitions with attempts, call charges, exclusions and criterion aggregates, including the baseline's separate runtime columns.
Check declared accounting arithmetic; recorded time and authority remain claims requiring human/session judgment.

The implementation must cover the actual version-1 Markdown tables/criterion cards and JSON records already in use, including the template's separate outcome columns and SSR's labelled M/N/U triples.
It must name any unsupported representation or unverified requirement; a successful parse of part of a document cannot silently establish whole-document readiness.
Parse only the agreed headings, fields, criterion cards and tables; do not infer obligations or approvals from arbitrary prose.
Free prose retains semantic review under the general spec's conformance rule.
Do not add duplicate metadata sidecars merely to simplify parsing; bring any necessary representation amendment back for explicit review before implementation depends on it.

Generation and validation share ordinary schemas, templates and a small set of structural rules; checked-in templates are generated/tested against those definitions rather than maintained as a second independent contract.
A new schema language, plugin system or configurable validation framework has no demonstrated need in this scope.
Reuse the execution-result schema and current configuration loader where appropriate; add `jsonschema` as a runtime dependency if the installed command uses it (currently it is development-only).
Keep the historical `worksheet` command outside this study path: it requires a legacy rubric and produces different sections, so it is not the implementation basis. Removing that command is separate scope.
Validation is read-only: it does not edit documents, run embedded commands, execute case checkers, invoke providers, migrate history or repair hashes automatically.
The active session still reads evidence, applies the criteria and writes judgments and interpretations. A validator would not resolve the Shiv negative-assertion category ambiguity.

## Verification, estimate and decision

Exercise the real CLI on disposable fixtures: generated drafts pass structural checks and fail required readiness; representative complete documents pass; missing criteria, wrong versions, broken Git/hash references, missing bundles and inconsistent counts produce actionable failures.
Verify refusal to overwrite, read-only checking and agreement between generated structure and validation definitions.
Apply the tool to the current SSR documents and their pinned historical references without rewriting frozen evidence; unsupported historical formats are reported explicitly.

Planning estimate: 120 active minutes for implementation and 60 for tests, actual CLI checks and applying it to SSR, including review.
Markdown checking is the main implementation uncertainty, so this estimate remains provisional.
Begin authorized implementation by checking the agreed structures against actual SSR documents, including scope and aggregate tables, before building the wider command; retain cross-document and arithmetic checks without duplicate metadata or silent format changes.
This replaces the earlier combined 120-minute placeholder allowance; the additional hour covers cross-document readiness and Git/evidence checks, beyond template copying and single-result schema validation.
The protocol owns the revised total forecast and remaining authorization; this estimate is not a promise or permission to extend the ceiling.

Decision requested: agree this small CLI scope and effort allowance before preparing its implementation steps. Skill editing and any further model collection remain separate decisions.
