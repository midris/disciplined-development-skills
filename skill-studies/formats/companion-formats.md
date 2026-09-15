# Study formats for review

Format set: `1-draft`; status: proposed, pending owner agreement.
This completes the bounded format proposal alongside the existing [score format](README.md).
It applies the settled [general contract](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#working-artifact-organization); it introduces no scoring policy, run approval or tooling prerequisite.

## Representations and common identities

Use Markdown for the protocol, case rules and comparison: their substance requires human/model interpretation.
Use JSON for manifests, attempt indexes and scores: identities and relationships need deterministic checks.
This retains the existing SSR artifact roles without forcing semantic rules into a prose parser.
Only the score currently has a JSON Schema; the companion templates below are reviewable contracts, not implemented validators.

An artifact identity is `{path, sha256, version}`: nonempty path, lowercase 64-hex SHA-256 of exact file bytes, and declared version or `null` when the source has none.
Repository paths resolve from the repository root; external evidence uses canonical absolute paths.
Markdown links remain relative to their containing file as usual.
A citation adds a `selector` naming a heading, JSON pointer, line or other precise location; a selector is not part of the file hash.
Sources additionally record their repository revision or external provenance; hashes still identify the bytes used.
When freezing a mutable authority such as the live protocol, retain its bytes at a versioned snapshot path and cite that path; later accounting or decision edits must not break the frozen identity.
Do not embed a file's own hash or require reciprocal hashes: manifests identify inputs, indexes identify manifests/results/scores, and scores identify criteria/policy/evidence.
Scores may cite an earlier immutable evidence index, as the pilot example does; a current index must not acquire a hash cycle with a score it indexes.

IDs are nonempty strings, unique within their owning collection.
Case IDs are study-scoped; criterion IDs are case-scoped; attempt and assessment IDs are study-scoped; runner IDs retain their emitted values.
An identity mismatch stops use of that record until explained or corrected; it is not a behavioral failure.
Empty strings and `<...>` are unfinished template values, never readiness evidence.
`null` means genuinely absent/unavailable only where specified; record the consequence of unavailable evidence instead of inventing values.

## Protocol

Copy [protocol.template.md](protocol.template.md); retain its named sections in order.
The active plan remains the only task checklist.
The protocol carries study decisions and links to their evidence; case definitions carry case-specific rules; the manifest freezes their bytes for a selected scope.
Policy snapshots derive from the protocol's assessment-policy section and must match it verbatim.
Later protocol amendments do not alter frozen snapshots.

Every section is required.
For an inapplicable section or field, write `Not applicable — <reason>`; optional held-out and numerical-score material is explicitly conditional in the template.
Sources, contracts and policy may be incorporated by precise links when their authoritative content already exists; the linked artifacts must enter the freeze manifest.
Do not duplicate the plan's unchecked tasks or historical campaign forecasts into a new protocol.
At agreement, explicitly migrate the live SSR protocol to the agreed version and preserve prior Git identities; this draft does not relabel the existing protocol as conformant.

## Case and criterion definition

Copy [case-definition.template.md](case-definition.template.md).
Its required sections are Identity and purpose, Inputs and setup, Rules and evidence, Criteria, and Limits and amendments, in that order.
Repeat the criterion card for every criterion, preserving its field labels.
Setup is a separate validity check, never part of a skill's functional score.

| Criterion field | Required content |
|---|---|
| ID and name | Stable local ID and useful outcome/action being judged. |
| Basis | Source citation and whether it is explicit skill text, owner clarification or ordinary task requirement. |
| Coverage | Protocol obligation/facet citation; more than one is allowed. |
| Dimension | Exactly `functional` or `procedural`. |
| Applies to | Explicit condition IDs; other conditions may receive descriptive observations, never an undisclosed compliance obligation. |
| Judgment unit | Whole artifact, operation, action sequence or other unit and its scope. |
| Required evidence | Inspectable artifacts/actions, their priority, and applicable mechanical checks. |
| Met | What sufficient evidence establishes. |
| Not met | Observable violation; absence of evidence alone is not a violation. |
| Insufficient evidence | Missing/conflicting evidence that prevents a supported judgment. |
| Alternatives | Effective wording, structure, tools or implementations that remain valid; reference answers are not exclusive. |
| Consequence | Predeclared effect of failure and uncertainty, based on the policy and known consumers. |
| Overlap | Related criteria sharing a cause; `None` when none is known. |

Evidence precedence belongs to the rule, not to a universal source ranking: Git proves committed state, traces prove action order, and complete documents plus settled behavior support semantic judgment.
Self-reports cannot replace direct evidence of the claimed action or outcome.
Missing traces do not invalidate otherwise inspectable final artifacts; limit the specific unsupported judgment and any attribution claim.
Optional weights/mappings require a predeclared policy and cannot mask functional failure; SSR uses no numerical score.

The [semantic-delivery worked criterion](semantic-delivery-criterion-example.md) instantiates this card from the existing F1 rule.
It is a format example, not a replacement rule, new assessment or suite expansion.
Existing `expected.json` stays a skill-specific payload for facts, scope and alternatives; no universal prose-matching schema is proposed.

## Source and freeze manifest

Copy [manifest.template.json](manifest.template.json).
All displayed keys are required; repeat the condition/file entries as needed.

| Field | Type and relationship |
|---|---|
| `format_version`, `manifest_id`, `study_id`, `case_id` | Strings; format is `1-draft` until agreement. |
| `status`, `created_at`, `source_revision` | Status `draft` or `frozen`; ISO date/time; preparation Git revision. Frozen does not mean authorized. |
| `authorities` | Identities for `spec`, `protocol`, `format_contract`, `score_schema`, `policy`, plus nonempty `criteria` identity array. |
| `conditions` | Nonempty list of unique condition IDs; each has configuration identity, prompt identity and fixture mappings. |
| `fixtures` | Each entry has `source` identity and `target` relative path; reproduce the runner configuration's exact mapping. |
| `target_skill` | Frozen source identity or `null` for an absent target; when present it must match a supplied fixture. |
| `controller_only` | Array of remaining checkers, expected facts, qualification and source-provenance identities used for this case. Policy/criteria already appear in authorities. None may occur in subject inputs. |
| `supersedes`, `amendment` | Prior manifest identity or `null`; reason/affected scope, or `null` for the first version. Preserve the prior manifest when replacing a frozen one. |

`sources.json` remains the broader inspected-source inventory; it is not proof of supplied inputs.
The freeze manifest is the selected case's exact input inventory.
Configuration `0.2` remains unchanged: prompt and fixture sources resolve from the configuration directory, and each fixture source is one regular file.
Compare every mapping and byte identity with the real config loader before freezing.
Original conditions always identify the preserved original snapshot; later candidates use separate sources.
The existing SSR manifests remain under their current identities until explicit migration at format agreement.

## Execution and evidence index

Copy [run-index.template.json](run-index.template.json).
The top-level fields identify format, index, study and phase, and contain an `attempts` array.
An empty array records no attempts; template entries are placeholders, not scheduled calls.
All displayed attempt fields are required, with the following stage-dependent values.

| Fields | Meaning and checks |
|---|---|
| `attempt_id`, `case_id`, `condition`, `repetition`, `attempt_number`, `retry_of` | Stable logical identity; positive integer repetition/attempt, prior attempt ID or `null`. Unique tuple within phase; a retry never overwrites its earlier attempt. |
| `manifest`, `configuration` | Frozen manifest and submitted config identities; condition must resolve in that manifest. |
| `authorization` | Citation to recorded owner authority for this exact scope; present before invocation. A link cannot establish actual consent by itself. |
| `command`, `cwd`, `cli` | Exact command, absolute working directory and executable path/version/hash; recorded before invocation. |
| `state` | `prepared`, `stopped` or `preserved`; does not encode behavioral success. |
| `run_id`, `result`, `retained_configuration` | `null` before allocation or if unavailable with explanation; otherwise emitted ID and retained file identities. Result version remains `0.3`. |
| `allocation` | Pool `subject`, `evaluator`, `authoring` or `retry`; invocation started `true`, `false` or `null` if unresolved; charge `1`, `0` or `null` respectively. Every retry invocation charges retry, not subject. |
| `evidence` | Original run directory, absolute primary/backup directories, and complete inventory identity; `null` locations until available. Verification status is `pending`, `verified` or `failed`, with evidence/reason. |
| `metrics` | Duration from result; reported usage/cost with evidence citation, or `null` if unavailable. Unknown cost is never zero. |
| `scores` | Zero or more assessment ID/identity pairs. Empty is valid for an unassessed or unusable attempt. Worked examples remain separately identified. |
| `limitations` | Array explaining missing result, unresolved invocation state, preservation failure or assessment/attribution limits. |

Each `scores` entry is `{assessment_id, record}`, with `record` an artifact identity.
Non-null `result`, `retained_configuration` and evidence `inventory` values are artifact identities.
`metrics.duration_seconds` is a nonnegative number or `null`; `reported_usage_cost` is `null` or `{reported, evidence}`, retaining the provider's reported object and a citation rather than inventing a cross-provider cost conversion.
`evidence.verification.evidence_or_reason` is a nonempty string citing the comparison record/command outcome or explaining why verification is incomplete.

Record launch/configuration failures even when no runner ID or bundle exists.
An unknown invocation charge blocks a claim of reconciled remaining capacity and further dispatch until resolved; it does not create retry authority.
The protocol owns ceilings, current authorizations and cumulative active time; indexes own attempt charges, including legacy indexes linked by the protocol.
Derive totals over unique attempts across those indexes, excluding worked examples and avoiding double-counting retries.
Do not copy current remaining budgets into every attempt row.
Read settings, mechanical status, timestamps and duration from the retained result rather than maintaining another authoritative copy.
The result's `test.id` must equal the submitted configuration's `id`; that runner test ID is distinct from the study's case and condition IDs.
The runner retains submitted config bytes; their hash must match the indexed submitted configuration, while prompt rendering is verified against its template and allocated paths.
After writing stops, preserve the complete bundle and compare primary/backup inventories before the next dispatch.
The inventory includes every retained file (including Git history) by relative path, bytes and hash, and records directories/symlinks without following links.
Partial evidence remains indexed and limits the claim; it is never silently dropped.

## Scores, comparisons and lifecycle

Keep the [score schema/template/example](README.md) unchanged for this review.
For each condition, score exactly its applicable criterion IDs once, with matching dimensions; put target-only control procedure observations in `observations` and `procedural_summary`.
Evidence IDs resolve within the score; criteria and policy identities resolve to the frozen assessment inputs, or to an explicitly versioned reassessment amendment.
Functional rollup remains `not met` if any functional criterion fails, otherwise `insufficient evidence` if any is unknown, otherwise `met`.
Setup validity and procedural severity remain separately visible; a functional pass cannot establish attribution under invalid setup.

Copy [comparison.template.md](comparison.template.md) for a comparison report.
It identifies every included score and excluded attempt, the comparison question, case/condition/skill/settings/policy identities, criterion-level differences, overlapping causes, uncertainty, costs and decision status.
A standalone score does not require a comparison report.
Do not infer adoption, causal contribution or reliability from a worked example or single-condition success.

Canonical locations remain `protocol.md`, `cases/<case>/assessment.md`, `expected.json`, condition configs, `manifest.json`, phase run indexes/reports and `assessments/<id>.json` within a study.
Templates live here; raw bundles stay in the protocol's external stores.
The protocol's suite table explicitly distinguishes proposed, selected, deferred, historical and rejected cases; a directory's existence never selects it.
Exposure is recorded separately as development or reserved; reserved requires the specifically authorized and verified boundary.
Drafts may be edited; frozen inputs and recorded observations retain their identities.
Revised frozen inputs receive a new manifest; reassessments receive new score IDs and a `supersedes` reference when they replace a prior judgment.
An illustrative example never silently supersedes a measured assessment.
Superseded material remains discoverable for provenance, without authorizing its old workflow.

Structural review checks keys/sections, types, versions, unique IDs, links, hashes, applicable criterion coverage and allocation arithmetic.
Readiness additionally requires completed values, fixed scope and inputs, evidence availability for the declared stage, and recorded authority for any dispatch.
Semantic coverage, judgment correctness and actual owner consent remain model/human responsibilities.
Unknown format versions are unsupported, not implicitly migrated.
The future generator/validator will use shared definitions, generate without overwriting and validate read-only; its CLI and implementation remain later agreed work.
