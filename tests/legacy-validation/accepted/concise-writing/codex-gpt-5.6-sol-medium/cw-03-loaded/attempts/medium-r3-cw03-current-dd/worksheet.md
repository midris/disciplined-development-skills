# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-03/current-dd |
| Scenario ID | cw-03-current-dd-medium |
| Scenario purpose | CW-03 loaded cross-section deduplication, repetition 3. |
| Run ID | 20260908T122747888Z-cw-03-current-dd-medium-4b7c0031-c229-4a85-9fe0-e7840ca1d6c6-e7ldbai4 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T12:27:47.888Z |
| Finished | 2026-09-08T12:28:07.279Z |
| Duration seconds | 19.392 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 9d6b2a40ee991df8d7831724cca8387590fc60f283e91ab35adfb265b2b95a3f |
| Prompt template | prompt-template.txt | 8586e43b9ed114e27eabc3164cb1cc0aeb665ef1e61d64b798c831919484194b |
| Rendered prompt | prompt.txt | 7ea6109526e750f376d2593a73993decae4b8eae74b1928cfc1987c0e51b054a |
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

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-03/current-dd/rubric.md | 6384c0a06d7d2449fa026879a704afa520d74a74471a03f25827c5cacca7bf54 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I1/I2 | One definition | PASS | [final][final] | Single-use URL and 30-minute expiry each once, across sections; one sentence not required. |
| CW-I1 | Use/recovery | PASS | [final][final] | Intended recipient only; administrator issues new link after expiry. |
| CW-I1 | No unsupported fact | PASS | [final][final] | No added fact. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Loading | PASS | [trace][trace], item_0 | Full CW before revision. |
| Deliverable/boundaries | PASS | [trace][trace] | Revised guide only; fixture-local read, no narration or mutations. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: clear two-section guide. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | All semantic/fidelity rows pass; distributed definition facts are not duplicate definitions. |
| Disposition | Scratch-only pending owner acceptance; retain this judgeable observation. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Hidden provider inputs/internal use remain outside trace proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; complete trace and matching final. Exact argv, frozen inputs and prelaunch/artifact hashes verified; protected fixtures unchanged, expected Git files only, evidence empty. COMPLETED establishes owned cleanup under frozen runner; exact logged runtime absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T122747888Z-cw-03-current-dd-medium-4b7c0031-c229-4a85-9fe0-e7840ca1d6c6-e7ldbai4/final.txt
[trace]: ../../runs/skilltest-runs/20260908T122747888Z-cw-03-current-dd-medium-4b7c0031-c229-4a85-9fe0-e7840ca1d6c6-e7ldbai4/stdout.txt
