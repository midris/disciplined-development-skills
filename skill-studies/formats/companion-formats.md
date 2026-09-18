# Study format contracts

Format set: `1`, accepted by the owner; collection authorization is separate.
These contracts implement the [spec's artifact ownership and units](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#architecture-seven-responsibilities).
They define document representations, not another workflow or authorization gate.
The [document CLI](../../skill-validation/runner/README.md#study-documents) checks these contracts using shared templates and structural rules; execution results retain their checked-in JSON Schema. Its guide names supported Markdown representations and the remaining semantic review boundary.

## Representations and common identities

Use Markdown for study agreements, case rules and batch assessments; JSON for manifests, attempt indexes and execution results.
An artifact identity is `{path, sha256, version}`, with optional `git_revision`: nonempty path, lowercase 64-hex SHA-256, declared version or `null`, and a full 40-hex commit ID when supplied.
Repository paths resolve from the repository root; external evidence uses canonical absolute paths.
A repository identity resolves at its own `git_revision`, or at the enclosing manifest's `source_revision` when present.
Require a revision for citations to mutable repository records whose accepted bytes must remain retrievable; a hash alone is not a retrieval address.
External retained files use path/hash; Git does not recover external bundles.
Markdown links are relative to their containing document; an accepted report records the full Git revision for the repository evidence it cites.
A citation adds a `selector` for a heading, JSON pointer, trace line or other precise location.

Keep references directional: manifests identify inputs; indexes identify attempts/manifests/bundles/results; batch assessments cite an accepted index version.
Execution results identify their manifest and direct evidence. Avoid citing the current index that hashes the result; use direct bundle evidence or an earlier Git version if an index citation is needed.
Do not embed a file's own hash, require reciprocal hashes or repeat input identities already resolvable through a manifest.

IDs are nonempty and unique within their owning collection: cases within a study, criteria within a case, attempts/results/batches/assessments within a study.
Runner IDs retain their emitted values. Empty strings and `<...>` are unfinished template values.
`null` means absent/unavailable only where permitted; an unresolved identity or missing evidence is not a behavioral failure.

## Protocol

Copy [protocol.template.md](protocol.template.md), retaining its seven sections in order.
The protocol owns current study decisions, their authority and brief rationale; the active plan alone owns progress/checklists.
Link case-specific rules, configuration settings, manifests, attempt indexes and assessments rather than recopying their contents.
Omit unselected optional provisions, such as reserved-evidence boundaries or a graded numeric mapping; material limits on actual claims remain explicit.
Use Git for earlier versions and place a correction's reason beside the current decision; no decision ledger is required.
The live SSR protocol and the Shiv and semantic-delivery case definitions/manifests use this layout. Historical observed-case inputs retain their recorded formats.

The protocol's policy section owns the study's assessment rules.
Controller policy copies derive verbatim from its designated policy body; identify the copy outside that body to avoid self-reference.
Keep observed-run policy bytes unchanged. A general batch interpretation rule may be incorporated by a precise spec citation; freeze all relied-on authorities before collection.

## Case and criterion definition

Copy [case-definition.template.md](case-definition.template.md): Identity and purpose, Inputs and setup, Rules and evidence, Criteria, Limits.
Repeat the brief criterion card for each criterion; cite shared rules instead of repeating explanations.

| Field | Required content |
|---|---|
| ID and name | Stable local ID and useful outcome/action. |
| Basis and coverage | Source citation/classification and the protocol obligation exercised. |
| Dimension | `functional` or `procedural`. |
| Applies to | Explicit condition IDs; other conditions receive observations, not undisclosed compliance obligations. |
| Judgment unit | Whole artifact, operation or action sequence and its scope. |
| Required evidence | Inspectable artifacts/actions, precedence and applicable checks. |
| Met / not met / insufficient evidence | Sufficient evidence, observable violation, and the gap/conflict preventing a supported outcome. |
| Alternatives | Valid wording, structure, tools or implementations; references are not exclusive answers. |
| Consequence | Effect of failure/uncertainty under the policy and known consumer requirements. |
| Overlap | Related criteria sharing a cause, or none. |

Keep whole-artifact criteria; do not split them into replacement counts to make assessment look mechanical.
Git proves committed state, traces can establish action order, and document meaning must be inspected against settled behavior.
Missing traces limit the relevant claim without invalidating otherwise inspectable artifacts; self-reports do not replace direct evidence.
`expected.json` remains the case-specific source of facts/scope/alternatives; no universal prose-matching schema is needed.
The [filled semantic criterion](../sweeping-stale-references/cases/semantic-delivery/assessment.md#f1-complete-useful-documentation) applies this layout to the existing F1 without adding obligations or reassessing evidence.

## Source and freeze manifest

Copy [manifest.template.json](manifest.template.json); all displayed keys are required.

| Field | Meaning |
|---|---|
| `format_version`, `manifest_id`, `study_id`, `case_id` | Format `1` and stable identities. |
| `status`, `created_at`, `source_revision` | `draft` or `frozen`, ISO date/time, and full Git commit containing identified repository bytes. A preparation base with different bytes is insufficient; frozen is not authorized. |
| `authorities` | Spec, protocol, format contract, execution-result schema, policy and nonempty criteria identity list. |
| `conditions` | Unique IDs, each with configuration identity and target-skill source path or `null`. |
| `subject_sources` | Exact deduplicated union of prompt and fixture files resolved from all condition configurations. Config files themselves are identified in `conditions`. |
| `controller_only` | Remaining checker/expected-fact/qualification/provenance identities; policy/criteria are already in authorities. These must not appear in subject inputs. |

Configuration `0.2` owns prompt/fixture paths, destination mappings and settings; sources resolve from its directory and each fixture source is one regular file.
Use the actual config loader to verify source membership, hashes, mappings and target-skill membership in the appropriate condition.
Reject missing/extra sources and controller-input overlap; this does not prove that unrelated prose contains no leaked guidance.
Commit input changes before freezing the manifest and exclude the manifest from its own inventory.
Original conditions use the preserved original snapshot; candidates use separate sources.
`sources.json` is an inspected-source inventory, not proof of supplied inputs.
Prepared unrun manifests use this format and identify committed input bytes. Historical observed-case manifests retain their identities.

## Execution and evidence index

Copy [run-index.template.json](run-index.template.json).
Each index covers one declared batch; top-level fields identify format, index, study and batch. `attempts` contains every actual attempt, or is empty before any attempt.

| Field | Meaning |
|---|---|
| `attempt_id`, `case_id`, `condition`, `repetition`, `attempt_number`, `retry_of` | Stable identities, positive repetition/attempt numbers, prior attempt ID or `null`. |
| `manifest` | Frozen input identity; condition resolves within it. |
| `authorization` | Citation to owner authority for this attempt's scope. Recording a citation cannot establish consent by itself. |
| `run_id` | Emitted runner ID, or `null` when no run directory was allocated. |
| `allocation` | Pool `subject`, `evaluator`, `authoring` or `retry`; charge `1`, `0` if no invocation, or `null` if unresolved. Every retry invocation charges retry. |
| `bundle` | Durable absolute path, one complete inventory identity and boolean `verified`; unavailable path/inventory may be `null` with the reason in limitations. |
| `result` | One canonical `{result_id, record}` execution-result entry, or `null` until assessed or when unusable; state which in limitations. |
| `limitations` | Missing evidence, unresolved invocation charge, preservation failure or assessment/attribution limits. |

Read settings, status, timestamps and duration from the bundle's `result.json` and `config.json`; missing cost is unavailable, not zero.
The runner result's `test.id` must match the `id` inside the manifest-identified configuration, not the case or condition ID.
The protocol owns commands/cwd, scope, ceilings and active-time accounting. Derive call totals from distinct attempts, not result revisions or worked examples.
Unknown charge must be resolved before further dispatch or a reconciled remaining-capacity claim.

Retain each actual attempt's complete bundle, including failures, in the protocol's durable store.
After writes stop, inventory all files including Git history by relative path, size and hash, plus directory/symlink entries without following links; verify preservation before further dispatch.
Keep historical copies. The actual backup/recovery arrangement belongs in the protocol; no second study-managed copy or new backup gate is required.

## Execution results and batch assessment

Complete [execution-result.template.json](execution-result.template.json) under its [schema](execution-result.schema.json) for each assessable execution.
The result identifies `result_id`, `run_id`, `condition`, a manifest, assessor context, direct evidence, setup validity, applicable criterion outcomes and uncertainty.
The manifest resolves case/study, subject inputs and assessment rules; do not repeat those identities.
For reassessment, a newly identified manifest may change rules while preserving the actual subject-input identities; explain the correction and verify those inputs against the attempt's frozen manifest. Never relabel the supplied subject context. Aggregate criterion coverage follows the result-pinned assessment rules; collection definitions do not add superseded criteria to a reassessed group. Groups without recorded attempts use the protocol’s declared definitions.

Record each applicable criterion exactly once, with dimension, `judgment`, concise `reason`, actual `consequence` and evidence IDs.
`judgment` is categorical, not a quality grade. Keep relevant secondary defects and descriptive control procedure in `observations`/`procedural_summary`.
Derive `functional_result` within this execution: any functional failure gives `not met`, otherwise any unknown gives `insufficient evidence`, otherwise `met`.
Procedural severity and setup validity remain separate. The schema enforces this rollup; criterion completeness, reference resolution and semantic correctness still need inspection.
Keep one canonical result per assessed execution. Historical `1-draft` scores and their worked example remain valid under their pinned historical schema; do not silently migrate them.

Copy [assessment.template.md](assessment.template.md) for the full declared test batch.
It owns the aggregate assessment required by [spec section 6](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#6-assess-observations-and-establish-the-baseline): coverage, counts by case/condition/criterion, recurring failures, uncertainty and acceptance under the declared rule.
Identify its accepted attempt-index version and reconcile every planned repetition and actual attempt, including unknown, invalid, unfinished and retried observations.
Follow the spec's denominator and inclusion rules; never select favorable repetitions, count a worked example/reassessment as another execution, or average overlapping criteria into independent successes/failures.
An optional comparison section uses these same aggregate results; no separate comparison record is required.
The protocol records the owner's decision, citing this assessment. Resource figures stay in accounting unless relevant to the comparison.

## Lifecycle and conformance

Current locations: `protocol.md`, case definitions/inputs/manifests, batch attempt indexes, `results/<run-id>.json` execution results and `<batch>-assessment.md` batch assessments.
Existing pilot reports and `assessments/` examples keep their historical locations. Raw bundles remain external.
Commit accepted records before correction; preserve the actual run identity and give a concise reason where the correction occurs. Git provides earlier versions without mandatory history fields or duplicate snapshots.
Label worked examples explicitly and keep them out of measured aggregates.
The protocol identifies suite membership and actual exposure; a case directory alone does not select it or establish reserved evidence.

Review the whole set against the [spec's conformance rule](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#document-conformance).
Check required sections/fields, IDs, references, versions/hashes, criterion coverage and allocation arithmetic; readiness additionally requires fixed scope, available evidence and authority for the actual dispatch.
Do not equate schema validity with study completeness, semantic correctness or owner consent.
Unknown versions are unsupported. The generator/validator shares definitions, generates without overwriting and validates read-only. Its mechanical checks support this conformance review; they do not replace interpretation or authorize collection.
