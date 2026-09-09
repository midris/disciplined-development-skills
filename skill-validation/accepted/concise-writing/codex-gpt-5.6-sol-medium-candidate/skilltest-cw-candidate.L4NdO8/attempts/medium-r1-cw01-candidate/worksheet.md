# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-01/current-dd |
| Scenario ID | cw-01-candidate-medium |
| Scenario purpose | CW-01 loaded prose behavior with unchanged rewritten CW candidate. |
| Run ID | 20260909T004202908Z-cw-01-candidate-medium-69367a00-276d-412f-ac6a-f38bf84f67d5-o46frtv1 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T00:42:02.908Z |
| Finished | 2026-09-09T00:42:19.381Z |
| Duration seconds | 16.473 |

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
| Rendered prompt | prompt.txt | 6c12dff197674a74ebda28945200adb742c237145426ef84bace100b4eb82169 |
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
| CW-I1 | Preserve all four states | PASS | [final][final] | Queued, running, complete and failed retained. |
| CW-I1 | Preserve distinct outcomes | PASS | [final][final] | Download link for completed exports and error code for failed exports remain distinct. |
| CW-I1 | Add no unsupported meaning | PASS | [final][final] | Only supplied facts retained. |
| CW-I2 | Remove targeted padding | PASS | [final][final] | Meta opener and both redundant restatements removed. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Deliverable and task boundaries | PASS | [trace][trace] | Only revised section returned; one local read, no other action. |
| Explicit target loading | PASS | [trace][trace] | sed returned the complete 73-line candidate CW body before the revision. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: compact section; states and outcomes are clear. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | All four semantic criteria pass; protocol N/A and fidelity PASS. One candidate observation, not deployment acceptance. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; all artifact and prelaunch hashes, frozen inputs, exact argv and protected fixtures verified. Complete six-event trace, empty provider/command stderr and verified absent owned runtime. Disclosed version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T004202908Z-cw-01-candidate-medium-69367a00-276d-412f-ac6a-f38bf84f67d5-o46frtv1/final.txt
[trace]: ../../runs/skilltest-runs/20260909T004202908Z-cw-01-candidate-medium-69367a00-276d-412f-ac6a-f38bf84f67d5-o46frtv1/stdout.txt
