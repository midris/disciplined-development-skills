# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-09/description |
| Scenario ID | cw-09-description-medium |
| Scenario purpose | CW-09 description-only composition diagnostic, repetition 3. |
| Run ID | 20260908T152126453Z-cw-09-description-medium-304dac5c-8e3e-4370-8719-1535bb570a63-oadt6yhk |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T15:21:26.453Z |
| Finished | 2026-09-08T15:21:45.254Z |
| Duration seconds | 18.801 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 0613b69c1fa3a56f0112b9b3216ee2d35ccb732c86aeda70f24331870f6f0aea |
| Prompt template | prompt-template.txt | a61fffa973d1e4cc884d868632e23b22f3dd4e336e71bce1dd594d139cfa172b |
| Rendered prompt | prompt.txt | b49b6e62dd6f456f25880283f4da0c858bc18e3e36bbf4654f54d581780e9fc0 |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |
| Fixture | descriptions/adversarial-review-loop.txt | 38843f7718501f52116bfd4f95a6640cb16b560851767df540c808a1ed18cefa |
| Fixture | descriptions/concise-writing.txt | 586a741a9cb28746078ca1b5f7aa570a4e621a5d2cdecac16e31bd6d2c82fd62 |
| Fixture | descriptions/superpowers-writing-skills.txt | 5504b0825ec458aa8c20e9a55c6a932b36849e261a97aaf98af366e19a937154 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-09/description/rubric.md | 0dcbc616c8f208af3cd015fc1fa607c96b140d34f6a69414012471201a80da19 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Authoring composition | Required selection | FAIL | [final][final] | WS only; required CW plus WS composition missing. |
| Authoring composition | Unrelated selections | PASS | [final][final] | No unrelated skill selected. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Descriptions-only loading | PASS | [trace][trace], item_1 | All three supplied descriptions read, no body. |
| Deliverable/boundaries | FAIL | [trace][trace], item_0 | Adds progress narration despite array-only request. Final compact alphabetical singleton correct; fixture-local read, no mutation/network/dispatch. |
| Source faithfulness | PASS | [trace][trace] | Current CW excludes authoring; WS-only selection follows descriptions. |

## Readability

| Observation | Evidence |
|---|---|
| PASS for final array: unambiguous. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | Target composition fails despite source-faithful classification; narration separately fails fidelity. |
| Disposition | Scratch-only pending owner acceptance; retain this judgeable observation. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Hidden provider inputs/internal use remain outside trace proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; complete trace and matching final. Exact argv, frozen inputs and prelaunch/artifact hashes verified; protected fixtures unchanged, expected Git files only, evidence empty. COMPLETED establishes owned cleanup under frozen runner; exact logged runtime absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T152126453Z-cw-09-description-medium-304dac5c-8e3e-4370-8719-1535bb570a63-oadt6yhk/final.txt
[trace]: ../../runs/skilltest-runs/20260908T152126453Z-cw-09-description-medium-304dac5c-8e3e-4370-8719-1535bb570a63-oadt6yhk/stdout.txt
