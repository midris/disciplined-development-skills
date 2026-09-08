# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-19/no-dd |
| Scenario ID | cw-19-no-dd-medium |
| Scenario purpose | CW-19 complex-conservation behavior; no-DD control, repetition 2. |
| Run ID | 20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt), [prelaunch checks](preflight.json). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T02:46:36.108Z |
| Finished | 2026-09-08T02:46:52.794Z |
| Duration seconds | 16.686 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | a6e41d0e854f4053783e6a819a1c9013bd38b719c7f067e33cbdd4dfc83e4128 |
| Prompt template | prompt-template.txt | c9e33a040244fdb810fc6c268d7f52ba8c657d40ecb1df367fc1dec7aad98fd4 |
| Rendered prompt | prompt.txt | c9e33a040244fdb810fc6c268d7f52ba8c657d40ecb1df367fc1dec7aad98fd4 |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-19/no-dd/rubric.md | cac093e5ab9ccd8f98e2746d66b8dc8d6cff00b2646b780d7c847154a2334233 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I2 | 1: padding removal | FAIL | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) | After the ordered wait/GO/run steps, 'Do not run the promotion command before GO' repeats that rule; criterion 1 explicitly requires it once. |
| CW-I1 | 2: preflight dependency | PASS | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) | Exact command, operator imperatives, JSON attachment to CHG-4821 and snapshot ID retained before promotion. |
| CW-I1 | 3: readiness conjunction | PASS | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) | Both metrics, lag at most 2 seconds and mismatch below 0.1%, share the same uninterrupted 15-minute promotion prerequisite. |
| CW-I1 | 4: failure escalation | PASS | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) | Preflight failure, lag exceeds 2, mismatch reaches 0.1; stop, BLOCKED, ticket link, channel and commander tag remain linked. 'Reaches' satisfies the source's explicit equality interpretation. |
| CW-I1 | 5: authorization order | PASS | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) | After readiness: ticket post, commander GO reply, then exact promote command. |
| CW-I1 | 6: shortcut and rationale | PASS | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) | No force; readiness and approval checks (the explicit GO reply in context) plus partially backfilled rows retained. |
| CW-I1 | 7: irreversible boundary | PASS | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) | Application's first accepted v3-only-field write; exact prohibited rollback and representability reason retained. |
| CW-I1 | 8: recovery ownership | PASS | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) | Only database incident commander, not release engineer; forward or ticket-recorded snapshot restore. |
| CW-I1 | Unsupported meaning | PASS | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) | No unsupported operation, fact or advice. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer parses this prose. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Output and read-only boundaries | PASS | [full trace](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/stdout.txt) item_0; result inventory | Only revised runbook, no tools or mutations. |
| Explicit CW loading | N/A | No-DD config | DD is absent by design. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: ordered phases and explicit threshold bullets are easy to follow; redundant GO sentence is scored under CW-I2. | [final](../../runs/skilltest-runs/20260908T024636108Z-cw-19-no-dd-medium-6d5862de-653c-4ee1-a0ff-6cfd8c1ea97e-v3_q51s2/final.txt) |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | Judgeable no-DD failure of criterion 1: redundant GO-before-promotion restatement remains. All conservation criteria pass; protocol N/A and fidelity PASS. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | No scoring ambiguity; scoped trace evidence does not prove absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Exact argv and prelaunch/final hashes verified against frozen sources; 4 declared fixture files unchanged, only expected template-free Git files present, evidence empty. Complete 4-event trace with final matching. Runner COMPLETED implies successful owned-process/runtime cleanup under the frozen implementation; exact logged runtime /private/tmp/skilltest-cw-baseline.ksDeiD/runs/skilltest-codex-uopsk3wy is absent. Provider and command stderr empty; version capture has the previously disclosed nonfatal PATH-alias warning. |
