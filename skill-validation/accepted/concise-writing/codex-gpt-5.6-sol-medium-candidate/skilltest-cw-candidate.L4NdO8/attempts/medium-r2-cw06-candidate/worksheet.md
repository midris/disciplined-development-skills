# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-06/current-dd |
| Scenario ID | cw-06-candidate-medium |
| Scenario purpose | Loaded CW effectiveness: remove inflated emphasis without weakening the API-key requirement. |
| Run ID | 20260909T011922901Z-cw-06-candidate-medium-fae668a9-8374-4eb7-aec9-7c844b7abc18-2ubuxmr0 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T01:19:22.901Z |
| Finished | 2026-09-09T01:19:51.177Z |
| Duration seconds | 28.276 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 7d9083384092fe913a602bb7f8a8dfe7beffb0263b4678a2e11f750775869808 |
| Prompt template | prompt-template.txt | bb72c140218df2ca53f6b254f7a7c780418eb3a0b4a05e94f505f58d4913bcbd |
| Rendered prompt | prompt.txt | 58e4e06ff9ddd921ca837e20ebf1134649d2aaa99a4f4b9f839e5d0c3d2c4462 |
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
| Rubric | skill-validation/pilot/cw-06/current-dd/rubric.md | bb7ec8f73d7398e61e88ec5a95f1a2efa22b734dcd5f9871f6472058c93d1f89 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I1 | Required key and rejection | PASS | [final][final] | Every request must supply API key in Authorization; absence rejected. |
| CW-I2 | Remove inflated padding | PASS | [final][final] | Requirement and rejection each once, no bold/doubled universals or descriptors. The single Every request must is permitted. |
| CW-I1 | No unsupported rule | PASS | [final][final] | No new condition. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Full body read | PASS | [trace][trace] | Complete CW before revised prose. |
| Revision-only response | FAIL | [trace][trace], item_0 | Extra I’ll apply the supplied writing guidance and keep the fixture unchanged announcement. |
| Boundaries | PASS | [trace][trace] | Fixture read only, no outside reads/network/dispatch/mutation. |

## Readability

| Observation | Evidence |
|---|---|
| PASS — clear compact requirement; header literal is easy to identify. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Meaning and de-inflation pass; independent extra narration fails fidelity. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; exact argv, frozen inputs, artifact/prelaunch hashes, protected fixtures and owned cleanup verified. Complete visible trace, empty provider/command stderr; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T011922901Z-cw-06-candidate-medium-fae668a9-8374-4eb7-aec9-7c844b7abc18-2ubuxmr0/final.txt
[trace]: ../../runs/skilltest-runs/20260909T011922901Z-cw-06-candidate-medium-fae668a9-8374-4eb7-aec9-7c844b7abc18-2ubuxmr0/stdout.txt
