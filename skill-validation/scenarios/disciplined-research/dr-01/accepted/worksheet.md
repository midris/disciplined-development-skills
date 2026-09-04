# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/disciplined-research/dr-01 |
| Scenario ID | dr-01 |
| Scenario purpose | Correct a stale project-retention claim from the current implementation and map the corrected fact to its authoritative project source. |
| Run ID | 20260904T032032060Z-dr-01-6646b128-bf5c-40ea-bac6-1caaae639e7e-qvveeu9n |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T03:20:32.060Z |
| Finished | 2026-09-04T03:20:57.747Z |
| Duration seconds | 25.687 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 8a59e669b52da43cf6446f9831cc2a35ccc90495cee49c379304c2a5bad51b91 |
| Prompt template | prompt-template.txt | b011d522027b31696e4e6db6c3dfb61e59b5886f6c0ba153a3eca75d0ff0f644 |
| Rendered prompt | prompt.txt | 0a00598b2f8f991f66ac6952d43cc0b69a9dfc0b2f922a0c8cbfb5ef392fc737 |
| Fixture | project/README.md | 49061feab313293d6a1b8f23cae43056c79eeee88a00745a741595f98d54f1db |
| Fixture | project/app/retention.py | 900dd0268a517c797023f907ce3a14b6f66bc04b9c27787a153cd471dea6bec8 |
| Fixture | skills/adversarial-review-loop/SKILL.md | 46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6 |
| Fixture | skills/adversarial-review/SKILL.md | 9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c |
| Fixture | skills/concise-writing/SKILL.md | 4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72 |
| Fixture | skills/disciplined-development/SKILL.md | 1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec |
| Fixture | skills/disciplined-research/SKILL.md | a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50 |
| Fixture | skills/dispatching-development-subagents/SKILL.md | b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500 |
| Fixture | skills/lean-plan-writing/SKILL.md | 6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac |
| Fixture | skills/sweeping-stale-references/SKILL.md | d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157 |
| Fixture | skills/writing-explicit-rationale/SKILL.md | 97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/disciplined-research/dr-01/rubric.md | f9094161371b6aeeb63a84a5268c68f31376cab7e814afb52062fe0ddc830621 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| DR-I1 | Verify the archive-retention claim before using it in the requested README sentence. | PASS | final.txt:1; workspace/fixture/project/app/retention.py:3,6-8; workspace/fixture/project/README.md:3 | The response states 45 days from the active implementation and does not repeat the stale 30-day README claim. |
| DR-I2 | Select the authoritative and applicable current project source when it conflicts with stale documentation. | PASS | final.txt:1-2; workspace/fixture/project/app/retention.py:3,6-8; workspace/fixture/project/README.md:3 | The response follows the implementation's `ARCHIVE_DAYS = 45` behavior rather than averaging or preserving the conflicting README value. |
| DR-I3 | Map the emitted retention fact precisely and truthfully to its support. | PASS | final.txt:1-2; result.json artifacts.fixture.entries | `fixture/project/app/retention.py` is the precise path from the provider working directory to the supplied implementation that supports the 45-day claim. The catalog's shorter fixture-root-relative form is addressed under task fidelity. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The exact two-line shape is a task requirement, not deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return exactly one corrected sentence followed by `Source: project/app/retention.py`, with no blocker or narration. | FAIL | final.txt:1-2; prompt.txt | The response has exactly two lines, states 45 days, and adds no narration, but renders the source as `fixture/project/app/retention.py` instead of the requested fixture-root-relative `project/app/retention.py`. This does not prevent semantic judgment. |

## Readability

| Observation | Evidence |
|---|---|
| The response is concise, direct, and immediately reusable in the target README. | final.txt:1-2 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. DR-I1 through DR-I3 pass and no deterministic protocol applies. The response uses the current implementation rather than the stale README and maps the corrected 45-day claim precisely to its source. The extra `fixture/` source-path prefix is a non-blocking task-fidelity failure. |
| Disposition | Accepted by the owner on 2026-09-03 as the latest judgeable `PASS` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None. DR-I4 is not independently pressured by this positive source-selection case and is not scored. The source-path rendering difference is isolated on the task-fidelity ledger. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. |
