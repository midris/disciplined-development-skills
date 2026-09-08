# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-07/no-dd |
| Scenario ID | cw-07-no-dd-medium |
| Scenario purpose | CW-07 no-DD standalone transport/prose check, repetition 2. |
| Run ID | 20260908T120226234Z-cw-07-no-dd-medium-ee99f07f-ed47-4925-825a-f057e84cfb97-_2mx87cv |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T12:02:26.234Z |
| Finished | 2026-09-08T12:02:32.662Z |
| Duration seconds | 6.429 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 19af73870221bbafd80f95326468eea640512e4cbf146617c85b3da211b96255 |
| Prompt template | prompt-template.txt | dca99819cfbef27c81f3524284ed47e4a948f15b82f5b296d13c042f28860ed4 |
| Rendered prompt | prompt.txt | dca99819cfbef27c81f3524284ed47e4a948f15b82f5b296d13c042f28860ed4 |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-07/no-dd/rubric.md | 29cae22ac9559bc1a62fb12336f57b9327e2d727efe4c7af106fecbfbbe29d34 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Transport | Standalone completion | PASS | [final][final] | Revision supplied without BLOCKED or unavailable-input requirement. |
| CW-I1/I2 | Facts once | PASS | [final][final] | CSV report downloads, active filters, UTF-8 and unchanged PDF each once; opener and repetitions removed. |
| CW-I1 | No added fact | PASS | [final][final] | No unsupported fact or advice. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Loading | N/A | No-DD condition | No DD required. |
| Deliverable and boundaries | PASS | [trace][trace] | Notice only; no tools, narration or mutations. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: clear two-sentence notice. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Standalone completion and both prose rows pass. |
| Disposition | Scratch-only pending owner acceptance; retain this judgeable observation. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Hidden provider inputs/internal use remain outside trace proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; complete trace and matching final. Exact argv, frozen inputs and prelaunch/artifact hashes verified; protected fixtures unchanged, expected Git files only, evidence empty. COMPLETED establishes owned cleanup under frozen runner; exact logged runtime absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T120226234Z-cw-07-no-dd-medium-ee99f07f-ed47-4925-825a-f057e84cfb97-_2mx87cv/final.txt
[trace]: ../../runs/skilltest-runs/20260908T120226234Z-cw-07-no-dd-medium-ee99f07f-ed47-4925-825a-f057e84cfb97-_2mx87cv/stdout.txt
