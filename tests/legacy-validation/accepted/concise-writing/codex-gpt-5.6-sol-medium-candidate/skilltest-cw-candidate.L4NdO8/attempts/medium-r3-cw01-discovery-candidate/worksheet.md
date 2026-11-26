# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-01/discovery |
| Scenario ID | cw-01-discovery-candidate-medium |
| Scenario purpose | Native positive CW discovery for prose shortening, separate from compression effectiveness. |
| Run ID | 20260909T014307216Z-cw-01-discovery-candidate-medium-95b40f3b-96d2-4c3c-8945-a04fc4a60893-_olrxqf7 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T01:43:07.216Z |
| Finished | 2026-09-09T01:43:30.775Z |
| Duration seconds | 23.56 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | f59c202ca70d877b861b8c2311af3f084604afa7958ff17e95bea2e6603aaffc |
| Prompt template | prompt-template.txt | 56a9c1f62782b81ed01801acaeef034534abb21ec55963863e941f4d1c10de86 |
| Rendered prompt | prompt.txt | 56a9c1f62782b81ed01801acaeef034534abb21ec55963863e941f4d1c10de86 |
| Fixture | .agents/skills/adversarial-review-loop/SKILL.md | 46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6 |
| Fixture | .agents/skills/adversarial-review/SKILL.md | 9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c |
| Fixture | .agents/skills/concise-writing/SKILL.md | f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba |
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
| Rubric | skill-validation/pilot/cw-01/discovery/rubric.md | 11b5b229ba0f05cbffaaa19942b1d1b838ee354703870f40f7e40fdd1628eb8b |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I3 / native selection | Full CW body before revision | PASS | [trace][trace], item_0 | Model initiated a direct read returning the entire 73-line CW body; no other bodies loaded. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested output | PASS | [final][final] | Revised export section only, no routing answer or extra narration. |
| Boundaries | PASS | [trace][trace] | Only fixture-local read; no edits, Git mutation, outside reads, network or dispatch. |

## Readability

| Observation | Evidence |
|---|---|
| PASS — clear and easy to scan. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Unprompted full body access precedes the requested revision; exposure is established, not inferred from prose quality. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; exact argv, frozen inputs, artifact/prelaunch hashes, protected fixtures and owned cleanup verified. Complete visible trace, empty provider/command stderr; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T014307216Z-cw-01-discovery-candidate-medium-95b40f3b-96d2-4c3c-8945-a04fc4a60893-_olrxqf7/final.txt
[trace]: ../../runs/skilltest-runs/20260909T014307216Z-cw-01-discovery-candidate-medium-95b40f3b-96d2-4c3c-8945-a04fc4a60893-_olrxqf7/stdout.txt
