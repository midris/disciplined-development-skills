# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-04/current-dd |
| Scenario ID | cw-04-current-dd-medium |
| Scenario purpose | CW-04 loaded prose: collapse over-sectioned session guide. |
| Run ID | 20260908T110649381Z-cw-04-current-dd-medium-38b26d34-b206-4238-bc30-2dc3791d9008-now4was4 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T11:06:49.381Z |
| Finished | 2026-09-08T11:07:11.907Z |
| Duration seconds | 22.526 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 47045f9d0006aa652078370f04fa79c08e0e7dfee2874180bed5721d916baba5 |
| Prompt template | prompt-template.txt | cf59ee2e5d52d0a1230bd1449b414cd9b8a25ba8b5f075da23be1af6c5767320 |
| Rendered prompt | prompt.txt | f61d7ab004fc9d720bdaef9964f02e87619c2292fa1212a31d9aa38a6b5d23b1 |
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
| Rubric | skill-validation/pilot/cw-04/current-dd/rubric.md | e8b90ccfb17b47e933f32df1195a1efa2ec88f54e832feca42430792066e6c17 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I2 | Collapse padding structure | PASS | [final][final] | Four small subheadings removed; compact account retains substantive facts. |
| CW-I1 | Time boundaries | PASS | [final][final] | Expiration after 20 minutes without activity; warning two minutes before expiration. |
| CW-I1 | Inputs and recovery | PASS | [final][final] | Mouse, keyboard or touch resets timer; sign in again after expiration. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested loading | PASS | [trace][trace], item_0 | cat returned full supplied CW body before revision. |
| Deliverable and boundaries | PASS | [trace][trace], items 0–1; inventory | One Session behavior section; only revision and fixture-local read. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: readable compact account, with explicit timer resets. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Three semantic criteria pass; protocol N/A, fidelity PASS. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Restating inputs as the inactivity boundary does not lose information; hidden provider inputs remain outside trace proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; six-event complete trace and matching final. Exact argv, artifact/prelaunch hashes and frozen sources verified; 13 protected fixtures unchanged, only expected template-free Git files, evidence empty. COMPLETED establishes owned cleanup under frozen runner; logged runtime /private/tmp/skilltest-cw-baseline.bOn8Dx/runs/skilltest-codex-159lg39h absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T110649381Z-cw-04-current-dd-medium-38b26d34-b206-4238-bc30-2dc3791d9008-now4was4/final.txt
[trace]: ../../runs/skilltest-runs/20260908T110649381Z-cw-04-current-dd-medium-38b26d34-b206-4238-bc30-2dc3791d9008-now4was4/stdout.txt
