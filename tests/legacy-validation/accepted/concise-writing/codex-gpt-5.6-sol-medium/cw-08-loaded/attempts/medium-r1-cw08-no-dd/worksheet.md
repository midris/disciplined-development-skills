# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-08/no-dd |
| Scenario ID | cw-08-no-dd-medium |
| Scenario purpose | CW-08 lossless non-software policy revision; no-DD behavioral control. |
| Run ID | 20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt), [prelaunch checks](preflight.json). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T02:34:33.098Z |
| Finished | 2026-09-08T02:34:42.264Z |
| Duration seconds | 9.166 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | cd3b86ca48285e2ab515c6b68e6cbb837840566f68b93a750e8780fc49553e37 |
| Prompt template | prompt-template.txt | 7b0828c0e2919ba57bb12e82ff30f1f457a6cf463eecd8f055c537f929892d4a |
| Rendered prompt | prompt.txt | 7b0828c0e2919ba57bb12e82ff30f1f457a6cf463eecd8f055c537f929892d4a |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-08/no-dd/rubric.md | 3b32625edddbd4b7455a0020372566c141d7f095a28d85b692d7edab7eba2083 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I1 | Eligibility and exception | PASS | [final.txt](../../runs/skilltest-runs/20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2/final.txt), first paragraph | 501(c)(3), budget under $2 million, eligible sponsor exception and Appendix A preserved. |
| CW-I1 | Deadline | PASS | [final.txt](../../runs/skilltest-runs/20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2/final.txt), second paragraph | October 15, 5 p.m. ET and no late review preserved. |
| CW-I1 | Accommodation | PASS | [final.txt](../../runs/skilltest-runs/20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2/final.txt), second paragraph | Email action, exact address and at least five business days retained. |
| CW-I1 | Appeal and finality | PASS | [final.txt](../../runs/skilltest-runs/20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2/final.txt), final paragraph | Denied applicants, ten calendar days, required Appeals form and final decision retained. |
| CW-I2 | Lossless removal | PASS | [final.txt](../../runs/skilltest-runs/20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2/final.txt) | Meta opener and duplicate deadline removed; protected content remains. |
| CW-I1/I3 | No unsupported meaning | PASS | [final.txt](../../runs/skilltest-runs/20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2/final.txt) | No added fact, advice or software assumption. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer parses the output. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Task boundaries and output only | PASS | [full trace](../../runs/skilltest-runs/20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2/stdout.txt), fixture inventory in [result](../../runs/skilltest-runs/20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2/result.json) | Four events; one final-only model message, no tool calls or subject mutations. |
| Explicit CW loading | N/A | No-DD config and trace | DD guidance absent by design; no loading requirement. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: short, clear policy grouped by eligibility, application and appeal. | [final.txt](../../runs/skilltest-runs/20260908T023433098Z-cw-08-no-dd-medium-e62bc4df-0c00-4406-adb6-8545307443d2-_xc9rgo2/final.txt) |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | All six semantic criteria pass; protocol N/A and fidelity PASS. This is a passing no-DD control, not behavioral RED. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | No scoring ambiguity. Scoped harness evidence does not prove absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Exact argv and prelaunch/final hashes verified against frozen sources; four declared fixture files unchanged, only expected template-free Git files added, evidence empty. Full four-event trace completed and final matched. Runner COMPLETED with successful owned-process/runtime cleanup under the frozen implementation; exact logged runtime /private/tmp/skilltest-cw-baseline.ksDeiD/runs/skilltest-codex-1lypf4le is absent. Provider and command stderr empty. Version capture retained the previously disclosed nonfatal PATH-alias warning. |
