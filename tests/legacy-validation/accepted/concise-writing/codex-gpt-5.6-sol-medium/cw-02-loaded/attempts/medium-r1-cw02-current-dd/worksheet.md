# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-02/current-dd |
| Scenario ID | cw-02-current-dd-medium |
| Scenario purpose | CW-02 loaded prose: retry scope, rationale and failure boundary. |
| Run ID | 20260908T110042886Z-cw-02-current-dd-medium-2f598543-cba3-45e9-b0cf-84d502ec9bfa-7xr5tei3 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T11:00:42.886Z |
| Finished | 2026-09-08T11:01:03.875Z |
| Duration seconds | 20.988 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 8938fd932b523e1bdf2feab052c258f55e42dbfc5eaa8fcc8a619f684219599f |
| Prompt template | prompt-template.txt | 71adee8f59521ef31a1175c1125abe888d3cea4b5ffc549aca57fe448d3185df |
| Rendered prompt | prompt.txt | 70fe91925d623cf2b5191a627ae0464c2e7f9315ea9d852336ef3692d5fb336b |
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
| Rubric | skill-validation/pilot/cw-02/current-dd/rubric.md | 12ae4f96d29fe191917ee6887cb2b5b0d36905fdc9f21deda9d698dbf2e74e11 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I2 | Remove duplication | PASS | [final][final] | Meta opener and duplicate maximum-attempt statement removed. |
| CW-I1 | Retry scope and consequence | PASS | [final][final] | Up to three attempts per delivery, not endpoint; a failing delivery cannot exhaust later deliveries' retries. |
| CW-I1 | Rationale and navigation | PASS | [final][final] | Synchronous retries because downstream acknowledgements must preserve order; Delivery ordering reference before changes retained. |
| CW-I1 | Failure boundary | PASS | [final][final] | Failed only after third unsuccessful attempt. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested loading | PASS | [trace][trace], item_0 | sed returned the complete supplied CW body before revision. |
| Deliverable and boundaries | PASS | [trace][trace], items 0–1; inventory | Only revised excerpt; fixture-local read, no narration or mutations. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: compact, coherent retry rules retain causal links. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Four semantic criteria pass; protocol N/A, fidelity PASS. One observation, not effectiveness estimate. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting scoring; hidden provider inputs remain outside observable proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; complete six-event trace and matching final. Exact argv, artifact/prelaunch hashes and frozen sources verified; 13 protected fixtures unchanged, only expected template-free Git files, evidence empty. COMPLETED establishes owned cleanup under frozen runner; logged runtime /private/tmp/skilltest-cw-baseline.bOn8Dx/runs/skilltest-codex-1mnekiz5 absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T110042886Z-cw-02-current-dd-medium-2f598543-cba3-45e9-b0cf-84d502ec9bfa-7xr5tei3/final.txt
[trace]: ../../runs/skilltest-runs/20260908T110042886Z-cw-02-current-dd-medium-2f598543-cba3-45e9-b0cf-84d502ec9bfa-7xr5tei3/stdout.txt
