# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-08/current-dd |
| Scenario ID | cw-08-candidate-medium |
| Scenario purpose | Loaded CW effectiveness: non-software eligibility prose with deadlines, exception and navigation. |
| Run ID | 20260909T014754296Z-cw-08-candidate-medium-85fef7b9-f950-491a-953e-82ebea67aa65-kitkpiyz |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T01:47:54.296Z |
| Finished | 2026-09-09T01:48:12.200Z |
| Duration seconds | 17.905 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 8647cb8f37ca1a1698aa30d94771aeb0d1d36d67375857b46ff62c04c375b521 |
| Prompt template | prompt-template.txt | 00a6e1d588d80fe97a4e36af638c7a6193294ac9922e3c1c977adbb7425d8e95 |
| Rendered prompt | prompt.txt | 9197980896a8910f65b117d71b9078752959c7b8ccaab0f83efb52832c02c6b1 |
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
| Rubric | skill-validation/pilot/cw-08/current-dd/rubric.md | 3b32625edddbd4b7455a0020372566c141d7f095a28d85b692d7edab7eba2083 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I1 | Eligibility and sponsor exception | PASS | [final][final] | 501(c)(3), annual budget below $2m, eligible sponsor exception and Appendix A preserved. |
| CW-I1 | Deadline and consequence | PASS | [final][final] | October 15 5 p.m. ET and late applications not reviewed. |
| CW-I1 | Accommodation action | PASS | [final][final] | Exact access@communityarts.example email and at least five business days before deadline. |
| CW-I1 | Appeal and finality | PASS | [final][final] | Denied applicants, 10 calendar days, Appeals required form, final decisions. |
| CW-I2 | Remove padding | PASS | [final][final] | No section-purpose opener or repeated deadline. |
| CW-I1 | No added assumptions | PASS | [final][final] | No invented software/process facts. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Full guidance read | PASS | [trace][trace] | Entire CW body returned before revision. |
| Output and boundaries | PASS | [trace][trace] | Revised section only; no mutation, outside reads, network or dispatch. |

## Readability

| Observation | Evidence |
|---|---|
| PASS — coherent paragraphs group eligibility, application and appeal rules. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | All eligibility, deadline, accommodation, appeal and padding criteria pass; no extra response narration. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; exact argv, frozen inputs, artifact/prelaunch hashes, protected fixtures and owned cleanup verified. Complete visible trace, empty provider/command stderr; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T014754296Z-cw-08-candidate-medium-85fef7b9-f950-491a-953e-82ebea67aa65-kitkpiyz/final.txt
[trace]: ../../runs/skilltest-runs/20260909T014754296Z-cw-08-candidate-medium-85fef7b9-f950-491a-953e-82ebea67aa65-kitkpiyz/stdout.txt
