# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/lean-plan-writing/lp-05 |
| Scenario ID | lp-05 |
| Scenario purpose | Name and disposition absent, malformed, out-of-scale, uniqueness, atomicity, and actionable-error cases without embedding implementation bodies. |
| Run ID | 20260904T202119383Z-lp-05-76bc50be-373e-4661-8cc7-d7114e92284e-g_n6njd_ |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T20:21:19.383Z |
| Finished | 2026-09-04T20:22:51.733Z |
| Duration seconds | 92.35 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | f5d420b0531218dba00006bd70f108be7037e040de2ddbbc6d34421b9c4f7144 |
| Prompt template | prompt-template.txt | 914f8831a62da2c3811895ce0f426c02e7307edc8440e35154dd51768d20417b |
| Rendered prompt | prompt.txt | b2436c4360fe92c4f7e03a1283ef5d44cbc199670c5fc40c22fb5186898e61d4 |
| Fixture | context/import-brief.md | 8789920dd0f54b1804e2a0aab65adfbcc728d525598d1d30a1d13b28c901c128 |
| Fixture | skills/lean-plan-writing/SKILL.md | 6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac |
| Fixture | skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/lean-plan-writing/lp-05/rubric.md | 237f61c94a6e3ec5be12afe4e8d5a2d78482651a43c217ab65c5aa9ea9bf27ac |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| LP-I1 | Specify implementation and tests in prose rather than embedding implementation bodies, test bodies, or copyable templates. | PASS | final.txt:28-83 | The response contains no fenced code, heredoc, implementation body, or test body. It uses behavioral rows, prose implementation requirements, runnable test commands, and a plaintext commit message. |
| LP-I2 | Name concrete files and explicitly disposition absent/empty, malformed, out-of-scale, uniqueness, atomic-visibility, and actionable-error behavior. | PASS | final.txt:5-26,32-43,61-79 | Both owning files are named. The plan separately rejects absent and empty inputs, defines malformed cases, accepts exactly 2,000,000 rows and rejects record 2,000,001 without activation, rejects candidate duplicates, preserves the old roster through every failure, and requires one reason/record/corrective-action report. |
| LP-I3 | Replace tricky streaming, validation, scale, and atomicity implementation with a dense behavioral test contract rather than embedded code. | PASS | final.txt:17-26,28-43,61-73 | The behavior table pins the principal input and failure cases, including old-roster identity overlap, multiple defects, staging/activation failure, and reader visibility. Separate generated-stream tests pin the exact size boundary and late-failure rollback without prescribing implementation code. |
| LP-I4 | Keep the tightly coupled importer and focused tests in one independently reviewable merge unit. | PASS | final.txt:1-8,81-83 | The plan declares one branch and one PR, keeps the two existing files in one task, and finishes with one concrete commit. Splitting the tests from implementation would leave an incomplete intermediate state. |

## Composition-owner behavior

| Owner | Criterion | Verdict | Evidence | Notes |
|---|---|---|---|---|
| superpowers:writing-plans | Preserve concrete files and interfaces, checkbox steps, runnable focused verification, and a concrete commit. | PASS | final.txt:3-15,28-83 | The focused task names its merge boundary, files, interface constraints, behavioral test work, three runnable pytest commands with expected outcomes, and the final commit. |
| superpowers:writing-plans TDD order | Do not independently rescore ordering in this scenario. | N/A | rubric.md | LP-05's rubric explicitly reserves upstream TDD-order scoring for LP-01. The response happens to use failing-test, prose-implementation, passing-test order, but that does not create another campaign score for the same upstream behavior. |
| Composition-owner verdict | Retain useful upstream execution scaffolding while applying lean prose density. | PASS | final.txt:1-83 | Every upstream element in scope for this focused task is actionable, while the lean owner correctly removes code and test bodies. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The plan is interpreted by an implementer. File names, table rows, checkbox steps, and pytest commands are human-facing semantic and task-fidelity constraints rather than an authenticated parser protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only the focused membership-roster implementation-plan task with behavioral tests, runnable verification, concrete files, prose implementation, and no placeholders. | PASS | final.txt:1-83 | The response contains one task, names only the two supplied files, provides concrete test and implementation work, and contains no TODO, TBD, fixture path, unrelated narration, or deferred placeholder. |

## Readability

| Observation | Evidence |
|---|---|
| The invariant list and input-to-result table make a large edge inventory easy to audit. Additional decisions about BOMs, header order, case sensitivity, and email normalization are concise dispositions of otherwise silent boundaries rather than distracting implementation detail. | final.txt:17-43 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. LP-I1 through LP-I4 and task fidelity pass: the plan is prose-first, names both concrete files, explicitly dispositions every required edge category, supplies a dense test contract for tricky streaming and atomicity behavior, and keeps the coupled work in one merge unit. The separate composition-owner ledger passes for the upstream scaffolding in scope, while TDD ordering is correctly not rescored. No deterministic protocol applies. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `PASS` baseline, with a separate composition-owner `PASS`. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting judgment. The brief's phrase “unique within the file and active roster” could be misread as forbidding an identity carried from the old roster into its replacement; the response resolves this consistently with replacement semantics by enforcing uniqueness within the candidate while allowing one old-roster match. The rubric requires an explicit uniqueness disposition, which this provides. |
| Scenario defects | None affecting execution or judgment. The fixture makes every scored edge observable, its packaged bytes match the catalog hash, and the rubric explicitly prevents duplicate scoring of upstream TDD ordering. As elsewhere in this catalog, the README retains the source validation document's former pre-archive path; that wording should be corrected consistently at catalog scope. |
| Proposed methodology changes | Continue scoring required edge categories independently and distinguish merely naming an edge from giving it an implementable disposition. Preserve the rubric's explicit deduplication of behaviors already scored in another scenario. |
