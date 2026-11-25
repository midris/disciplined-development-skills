# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-12/contract |
| Scenario ID | cw-12-contract-candidate-medium |
| Scenario purpose | Loaded CW contract diagnostic for supporting-reference authoring ownership. |
| Run ID | 20260909T015111217Z-cw-12-contract-candidate-medium-7fcad019-23c7-4b6c-a84e-8951086f6af2-bgxa2_gw |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T01:51:11.217Z |
| Finished | 2026-09-09T01:51:34.048Z |
| Duration seconds | 22.831 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 29769a52c5db73321cf4c1ac790a19cb96bb6242f7266b1b96d49743c8e65edf |
| Prompt template | prompt-template.txt | 10fe1ea50b5bfba895b82515a88d4ed460395e0471cd7c68f443d3c7d3f6d648 |
| Rendered prompt | prompt.txt | bac00bf8135c3e7dee253fa05855f9d9f6934a3f31254e4bfaebe534d02506d5 |
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
| Rubric | skill-validation/pilot/cw-12/contract/rubric.md | f9fc90a33f7f2e607e40470e510b303559a25c64feaab69fd0bab81e893bd8d3 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Authoring contract | writing-skills owns authoring decisions | PASS | [final][final] and [trace][trace] | Canonical owner plus exact explicit source sentence. |
| Validation contract | writing-skills owns validation | PASS | [final][final] and [trace][trace] | Same explicit ownership sentence supports validation_owner. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Complete CW and faithful extraction | PASS | [trace][trace] | All 73 CW lines returned; exact complete ownership sentence supports both canonical owners. |
| JSON only | FAIL | [trace][trace], item_0 | Extra I’m reading the specified guidance and supplied contract announcement. |
| Boundaries | PASS | [trace][trace] | Fixture read/search only; no mutation, outside access, network or dispatch. |

## Readability

| Observation | Evidence |
|---|---|
| PASS — owners and supporting sentence unambiguous. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Explicit ownership contract passes and extraction is faithful; extra announcement fails output-only fidelity. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; mechanical checks and cleanup passed. A compound CW read/search exited 1 because rg omitted hidden paths and found no listed files, but the complete CW body was returned. Judgeable result, not INFRA_RETRY. Empty provider/command stderr; version-only PATH warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T015111217Z-cw-12-contract-candidate-medium-7fcad019-23c7-4b6c-a84e-8951086f6af2-bgxa2_gw/final.txt
[trace]: ../../runs/skilltest-runs/20260909T015111217Z-cw-12-contract-candidate-medium-7fcad019-23c7-4b6c-a84e-8951086f6af2-bgxa2_gw/stdout.txt
