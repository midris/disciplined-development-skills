# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-18/discovery |
| Scenario ID | cw-18-discovery-medium |
| Scenario purpose | CW-18 native durable-file discovery, repetition 3. |
| Run ID | 20260908T154046349Z-cw-18-discovery-medium-2ebccbe6-b0a2-47b9-843e-d0a0079ac142-w3i9819t |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T15:40:46.349Z |
| Finished | 2026-09-08T15:43:42.658Z |
| Duration seconds | 176.309 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | c16c0c0bc0ac86e9d9331014799a9a5140b094063aa4d4b057a93c1be6e4240c |
| Prompt template | prompt-template.txt | f65c78cdf2950877618f2fc14a10f3baa5c03a78f1aafef8c921fac477d0c52d |
| Rendered prompt | prompt.txt | 0f20b09afd7d9db428d65ee2da5f2aa5efb5f027b77f385ea613cd37d085b551 |
| Fixture | .agents/skills/adversarial-review-loop/SKILL.md | 46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6 |
| Fixture | .agents/skills/adversarial-review/SKILL.md | 9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c |
| Fixture | .agents/skills/concise-writing/SKILL.md | 4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72 |
| Fixture | .agents/skills/disciplined-development/SKILL.md | 1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec |
| Fixture | .agents/skills/disciplined-research/SKILL.md | a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50 |
| Fixture | .agents/skills/dispatching-development-subagents/SKILL.md | b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500 |
| Fixture | .agents/skills/lean-plan-writing/SKILL.md | 6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/sweeping-stale-references/SKILL.md | d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157 |
| Fixture | .agents/skills/writing-explicit-rationale/SKILL.md | 97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |
| Fixture | clothing-swap-guide.md | 91244a1103bb2b147d707c1700f9b1ac76911f1bfeafb7ee641437df63dc58ae |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-18/discovery/rubric.md | 24219beb57f1ec1cd90ab22b0b3e369ae15a85a5b57535c3c3723ebed95a0cd0 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I3 | Durable-file positive selection | PASS | [trace][trace], item_1 before item_4 | Full model-initiated CW read bundled with DD and DR before guide generation. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested guide | PASS | [guide][guide], independently read in full | Detailed planning, exchange rules, venue, volunteers, operations, accessibility, leftovers and follow-up. |
| Brief response only | FAIL | [trace][trace], items_0, 2, 5, 7 | Final notice is brief, but three extra narration messages violate response-only constraint. |
| Write boundary | PASS | [trace][trace]; audited inventory | Guide is sole added task file; protected fixtures intact, no Git mutation, outside-fixture inspection, network or dispatch. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: detailed, organized practical guide with navigable sections. | [guide][guide] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Native selection succeeds; prohibited narration is a separate fidelity failure. |
| Disposition | Scratch-only pending owner acceptance; retain this judgeable observation. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Bundled CW/DD/DR read disclosed; no claim of hidden method use or sole-CW attribution. The retained verification output contains actual guide previews; evaluator independently inspected all 192 lines, not just those previews. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; complete trace and matching final. Exact argv, frozen inputs and prelaunch/artifact hashes verified; protected fixtures unchanged, expected Git files plus sole allowed guide, evidence empty. COMPLETED establishes owned cleanup under frozen runner; exact logged runtime absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. Optional governing-document search found no matches (exit 1); no required control affected or retry. |

[final]: ../../runs/skilltest-runs/20260908T154046349Z-cw-18-discovery-medium-2ebccbe6-b0a2-47b9-843e-d0a0079ac142-w3i9819t/final.txt
[trace]: ../../runs/skilltest-runs/20260908T154046349Z-cw-18-discovery-medium-2ebccbe6-b0a2-47b9-843e-d0a0079ac142-w3i9819t/stdout.txt
[guide]: ../../runs/skilltest-runs/20260908T154046349Z-cw-18-discovery-medium-2ebccbe6-b0a2-47b9-843e-d0a0079ac142-w3i9819t/workspace/fixture/clothing-swap-guide.md
