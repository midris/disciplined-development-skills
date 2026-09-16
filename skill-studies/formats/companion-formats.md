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
For repository evidence, keep one canonical file and preserve accepted versions in Git before replacing them.
Record a full Git commit ID with a path/hash citation when it must resolve historical bytes; retrieve those bytes from that commit rather than requiring the current file to match an old hash.
Do not embed a file's own hash or require reciprocal hashes: manifests identify inputs, indexes identify manifests/results/scores, and scores identify criteria/policy/evidence.
Scores may cite an earlier immutable evidence index; a current index must not acquire a hash cycle with a score it indexes.
The pilot example's original run-index citation resolves through `git_revision` in its [assessment index](../sweeping-stale-references/assessments/index.json), as described in the [score instructions](README.md#score-records).

IDs are nonempty strings, unique within their owning collection.
Case IDs are study-scoped; criterion IDs are case-scoped; attempt and assessment IDs are study-scoped; runner IDs retain their emitted values.
An identity mismatch stops use of that record until explained or corrected; it is not a behavioral failure.
Empty strings and `<...>` are unfinished template values, never readiness evidence.
`null` means genuinely absent/unavailable only where specified; record the consequence of unavailable evidence instead of inventing values.

## Protocol

Copy [protocol.template.md](protocol.template.md); retain its named sections in order.
Its seven sections describe the current study agreement; place decisions, authority and brief rationale beside the subject they govern, with Git preserving earlier versions.
Do not maintain a separate decisions/amendments ledger: it duplicates current section content and Git history.
The active plan remains the only task checklist.
The protocol carries study decisions and links to their evidence; case definitions carry case-specific rules; the manifest freezes their bytes for a selected scope.
Policy snapshots derive from the protocol's assessment-policy section and must match it verbatim.
Later protocol amendments preserve accepted policy bytes in Git; controller policy copies serve execution inputs, not a separate historical archive.

Every section is required.
For an inapplicable section or field, write `Not applicable — <reason>`; optional held-out and numerical-score material is explicitly conditional in the template.
Sources, contracts and policy may be incorporated by precise links when their authoritative content already exists; the linked artifacts must enter the freeze manifest.
Do not duplicate the plan's unchecked tasks or historical campaign forecasts into a new protocol.
At agreement, explicitly migrate the live SSR protocol to the agreed version and preserve prior Git identities; this draft does not relabel the existing protocol as conformant.

## Case and criterion definition

Copy [case-definition.template.md](case-definition.template.md).
Its required sections are Identity and purpose, Inputs and setup, Rules and evidence, Criteria, and Limits and amendments, in that order.
Repeat the criterion card for every criterion, preserving its field labels.
Keep field values brief; where a rule is shared, cite its precise location in the case or policy instead of repeating it in every card.
The fields make consequential distinctions inspectable; they do not require a separate essay or example for each entry.
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
| `supersedes`, `amendment` | Prior manifest citation or `null`; concise reason/affected scope, or `null` for the first version. Earlier accepted versions live in Git. |

`sources.json` remains the broader inspected-source inventory; it is not proof of supplied inputs.
The freeze manifest is the selected case's exact input inventory.
Configuration `0.2` remains unchanged: prompt and fixture sources resolve from the configuration directory, and each fixture source is one regular file.
Compare every mapping and byte identity with the real config loader before freezing.
Original conditions always identify the preserved original snapshot; later candidates use separate sources.
The existing SSR manifests remain under their current identities until explicit migration at format agreement.

## Execution and evidence index

Copy [run-index.template.json](run-index.template.json).
The top-level fields identify format, index, study and phase, and contain an `attempts` array.
Each actual attempt has one entry; no attempts means an empty array.

| Fields | Meaning and checks |
|---|---|
| `attempt_id`, `case_id`, `condition`, `repetition`, `attempt_number`, `retry_of` | Stable identity; positive repetition/attempt numbers, prior attempt ID or `null`. Distinct attempts remain separately accounted for. |
| `manifest` | Frozen input manifest identity; condition resolves there. Use its configuration identity instead of repeating it. |
| `authorization` | Citation to owner authority for this scope, recorded before invocation. The citation alone cannot establish actual consent. |
| `run_id` | Emitted runner ID, or `null` if no run directory was allocated. |
| `allocation` | Pool `subject`, `evaluator`, `authoring` or `retry`; charge `1` for an invocation, `0` when none occurred, or `null` if unresolved. Every retry invocation charges retry. |
| `bundle` | Absolute durable `path`, one complete `inventory` identity, and boolean `verified`. Path/inventory may be `null` before preservation or when unavailable, with the reason in limitations. |
| `score` | One canonical `{assessment_id, record}` entry, with `record` an artifact identity; `null` until assessed or for an unusable attempt. |
| `limitations` | Reasons for missing evidence, unresolved invocation state, failed preservation or limits on assessment/attribution. |

Use the runner's fixed bundle layout to locate `result.json`, `config.json`, prompts and logs.
Read settings, execution status, timestamps and duration from those artifacts; report unavailable cost as unavailable rather than zero.
The result's `test.id` must match the manifest's configuration ID; it is distinct from the study's case and condition IDs.
Record exact commands/cwd and CLI qualification in the execution scope, without duplicating them in every index entry.
The index supplies study relationships the runner does not know; it is not a second copy of runner metadata.

Retain one complete durable bundle per actual run, including unsuccessful attempts, and use one inventory to verify preservation after writing stops.
The inventory includes all retained files (including Git history) by relative path, size and hash, plus directory/symlink entries without following links.
Verify the retained bytes against that inventory before further dispatch; preservation failure stops progression.
Use ordinary backup arrangements when configured; no second study-managed copy or per-run backup-verification gate is required.
The protocol records the actual arrangement, unverified coverage or explicitly accepted single-host retention; do not infer recoverability from a durable path alone.
Existing historical copies stay in place; this rule does not authorize deletion.

Record configuration/launch failures even when no bundle exists.
Unknown invocation charge blocks a reconciled remaining-capacity claim and further dispatch until resolved; it grants no retry authority.
The protocol owns ceilings and active time; derive invocation totals over distinct index entries, without counting a correction or worked example as another attempt.

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
Drafts may be edited; accepted inputs and records are committed before replacement.
Update the canonical manifest or score for a correction, retaining its run identity and a concise reason; Git supplies prior versions, without requiring duplicate files or a separate amendment ledger.
Distinct actual attempts remain separately accounted for; correcting a record is not another attempt.
An illustrative example never silently supersedes a measured assessment.
Superseded material remains discoverable for provenance, without authorizing its old workflow.

Structural review checks keys/sections, types, versions, unique IDs, links, hashes, applicable criterion coverage and allocation arithmetic.
Readiness additionally requires completed values, fixed scope and inputs, evidence availability for the declared stage, and recorded authority for any dispatch.
Semantic coverage, judgment correctness and actual owner consent remain model/human responsibilities.
Unknown format versions are unsupported, not implicitly migrated.
The future generator/validator will use shared definitions, generate without overwriting and validate read-only; its CLI and implementation remain later agreed work.
