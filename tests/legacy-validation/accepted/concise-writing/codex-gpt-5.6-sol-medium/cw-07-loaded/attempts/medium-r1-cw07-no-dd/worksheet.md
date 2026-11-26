# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-07/no-dd |
| Scenario ID | cw-07-no-dd-medium |
| Scenario purpose | CW-07 no-DD control: standalone transport and release-notice conservation. |
| Run ID | 20260908T111416298Z-cw-07-no-dd-medium-5da2ac26-3a08-401b-bf12-05ce9af5b420-9ajv51gf |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T11:14:16.298Z |
| Finished | 2026-09-08T11:14:21.606Z |
| Duration seconds | 5.307 |

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
| Transport | Standalone completion | PASS | [final][final] | Returns revision, not BLOCKED or demand for unavailable procedures. |
| CW-I1/I2 | Facts once | PASS | [final][final] | CSV, active filters, UTF-8 and unchanged PDF behavior each once; opener and duplicates removed. |
| CW-I1 | No new fact | PASS | [final][final] | No unsupported fact/advice. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested loading | N/A | No-DD config | DD deliberately absent. |
| Deliverable and boundaries | PASS | [trace][trace], item_0; inventory | Only revised notice; no narration or tool actions. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: two clear sentences separate new CSV behavior from unchanged PDF. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Three semantic rows pass; transport remains separately attributed, protocol N/A, fidelity PASS. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting scoring; hidden provider inputs remain outside trace proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; four-event complete trace and matching final. Exact argv, artifact/prelaunch hashes and frozen sources verified; four protected fixtures unchanged, only expected template-free Git files, evidence empty. COMPLETED establishes owned cleanup under frozen runner; logged runtime /private/tmp/skilltest-cw-baseline.bOn8Dx/runs/skilltest-codex-e7n9lkfv absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T111416298Z-cw-07-no-dd-medium-5da2ac26-3a08-401b-bf12-05ce9af5b420-9ajv51gf/final.txt
[trace]: ../../runs/skilltest-runs/20260908T111416298Z-cw-07-no-dd-medium-5da2ac26-3a08-401b-bf12-05ce9af5b420-9ajv51gf/stdout.txt
