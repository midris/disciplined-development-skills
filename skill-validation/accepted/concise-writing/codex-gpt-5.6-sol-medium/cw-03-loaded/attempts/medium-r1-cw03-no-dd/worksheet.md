# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-03/no-dd |
| Scenario ID | cw-03-no-dd-medium |
| Scenario purpose | CW-03 no-DD control: remove duplicated access-link definition. |
| Run ID | 20260908T110235567Z-cw-03-no-dd-medium-36e2859e-2c90-4a90-8e23-4cc466255952-fzb_q9zc |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T11:02:35.567Z |
| Finished | 2026-09-08T11:02:42.680Z |
| Duration seconds | 7.113 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 9410826c398c5d36ba3fa1676bb447d559c4481ee1d30c21338ff037e22f21bc |
| Prompt template | prompt-template.txt | f11f66645ab5855acdc495a3361b03da1c532ff9e8471e8057c661544648823e |
| Rendered prompt | prompt.txt | f11f66645ab5855acdc495a3361b03da1c532ff9e8471e8057c661544648823e |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-03/no-dd/rubric.md | 6384c0a06d7d2449fa026879a704afa520d74a74471a03f25827c5cacca7bf54 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I1/I2 | One definition | PASS | [final][final] | Single-use URL and 30-minute expiration each defined once across the guide. No requirement forces one sentence. |
| CW-I1 | Use and recovery | PASS | [final][final] | Intended recipient only; administrator must issue a new link after expiration. |
| CW-I1 | No unsupported facts | PASS | [final][final] | No added fact. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested loading | N/A | No-DD config | DD deliberately absent. |
| Deliverable and boundaries | PASS | [trace][trace], item_0; inventory | Only revised guide; no narration or tool actions. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: definition, recipient rule and expiration/recovery are easy to find. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | All three semantic criteria pass; protocol N/A, fidelity PASS. Retain passing no-DD control. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Definition facts span two sections without duplication or loss; exact sentence structure is not semantic. Hidden provider inputs remain outside observable proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; four-event complete trace and matching final. Exact argv, artifact/prelaunch hashes and frozen sources verified; four protected fixtures unchanged, only expected template-free Git files, evidence empty. COMPLETED establishes owned cleanup under frozen runner; logged runtime /private/tmp/skilltest-cw-baseline.bOn8Dx/runs/skilltest-codex-mztik1zq absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T110235567Z-cw-03-no-dd-medium-36e2859e-2c90-4a90-8e23-4cc466255952-fzb_q9zc/final.txt
[trace]: ../../runs/skilltest-runs/20260908T110235567Z-cw-03-no-dd-medium-36e2859e-2c90-4a90-8e23-4cc466255952-fzb_q9zc/stdout.txt
