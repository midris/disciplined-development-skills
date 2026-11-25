# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-04/no-dd |
| Scenario ID | cw-04-no-dd-medium |
| Scenario purpose | CW-04 no-DD control: collapse over-sectioned session guide. |
| Run ID | 20260908T110533744Z-cw-04-no-dd-medium-dbdf0a32-35e4-4e6f-a068-082682aab538-g__givzg |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T11:05:33.744Z |
| Finished | 2026-09-08T11:05:40.667Z |
| Duration seconds | 6.923 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 5740ec1f34def8ef4d9fc18b301fa129ed81937368df4a5563f4150d7774298f |
| Prompt template | prompt-template.txt | f9f9a0abaf05fee1d82a74ab8a3baf6a86b07875c61a242c402a42ee314b9c11 |
| Rendered prompt | prompt.txt | f9f9a0abaf05fee1d82a74ab8a3baf6a86b07875c61a242c402a42ee314b9c11 |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-04/no-dd/rubric.md | e8b90ccfb17b47e933f32df1195a1efa2ec88f54e832feca42430792066e6c17 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I2 | Collapse padding structure | PASS | [final][final] | Four tiny subheadings removed; complete compact account remains. |
| CW-I1 | Time boundaries | PASS | [final][final] | 20 minutes of inactivity; warning two minutes before expiration. |
| CW-I1 | Inputs and recovery | PASS | [final][final] | Mouse, keyboard or touch resets the timer; sign in again after expiration. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested loading | N/A | No-DD config | DD deliberately absent. |
| Deliverable and boundaries | PASS | [trace][trace], item_0; inventory | One Session behavior section; only revision, no tool actions. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: clear four-sentence account without excess structure. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Three semantic criteria pass; protocol N/A, fidelity PASS. Retain passing no-DD control. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting scoring; hidden provider inputs remain outside observable proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; four-event complete trace and matching final. Exact argv, artifact/prelaunch hashes and frozen sources verified; four protected fixtures unchanged, only expected template-free Git files, evidence empty. COMPLETED establishes owned cleanup under frozen runner; logged runtime /private/tmp/skilltest-cw-baseline.bOn8Dx/runs/skilltest-codex-cgpgdf2u absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T110533744Z-cw-04-no-dd-medium-dbdf0a32-35e4-4e6f-a068-082682aab538-g__givzg/final.txt
[trace]: ../../runs/skilltest-runs/20260908T110533744Z-cw-04-no-dd-medium-dbdf0a32-35e4-4e6f-a068-082682aab538-g__givzg/stdout.txt
