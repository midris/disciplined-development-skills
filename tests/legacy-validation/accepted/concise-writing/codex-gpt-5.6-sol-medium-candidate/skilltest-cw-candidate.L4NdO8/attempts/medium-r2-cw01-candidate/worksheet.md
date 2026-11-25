# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-01/current-dd |
| Scenario ID | cw-01-candidate-medium |
| Scenario purpose | Loaded CW prose effectiveness: export-status meta-framing and duplication. |
| Run ID | 20260909T011423134Z-cw-01-candidate-medium-70533ceb-87b8-44d6-9f9e-74d4595476ef-daf4y8in |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T01:14:23.134Z |
| Finished | 2026-09-09T01:14:41.541Z |
| Duration seconds | 18.407 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 23587b3bdd2bd7c84a17d7be960da17271658a43698e692ec02b6061620e8d24 |
| Prompt template | prompt-template.txt | ee17c7de4730f7dd0190e75e4d76292bf914f202dfdb6bc7ee160b5a65877e3e |
| Rendered prompt | prompt.txt | 4b2999d6d464225a0a78f486e4392ef69597976f45b8714535f977841ae2eb94 |
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
| Rubric | skill-validation/pilot/cw-01/current-dd/rubric.md | 06a8adb2930f11c242dec98476a9640bf581fc000bd624d3ad4a50f658533d88 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I1 | Four statuses | PASS | [final][final] | queued, running, complete and failed retained. |
| CW-I1 | Distinct outcomes | PASS | [final][final] | Complete has download link; failed has error code. |
| CW-I1 | No new meaning | PASS | [final][final] | No unsupported addition. |
| CW-I2 | Remove opener and repetition | PASS | [final][final] | Direct facts, each once. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Complete CW read | PASS | [trace][trace] | Exact full 73-line body before revision. |
| Output and boundaries | PASS | [trace][trace] | Only revised section; fixture reads only, no mutation, outside reads, network or dispatch. |

## Readability

| Observation | Evidence |
|---|---|
| PASS — compact, clear status/outcome mapping. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Preserves all facts while removing section-purpose narration and repeats. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; exact argv, frozen inputs, artifact/prelaunch hashes, protected fixtures and owned cleanup verified. Complete visible trace, empty provider/command stderr; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T011423134Z-cw-01-candidate-medium-70533ceb-87b8-44d6-9f9e-74d4595476ef-daf4y8in/final.txt
[trace]: ../../runs/skilltest-runs/20260909T011423134Z-cw-01-candidate-medium-70533ceb-87b8-44d6-9f9e-74d4595476ef-daf4y8in/stdout.txt
