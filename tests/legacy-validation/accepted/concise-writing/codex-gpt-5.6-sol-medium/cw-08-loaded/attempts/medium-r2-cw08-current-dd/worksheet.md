# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-08/current-dd |
| Scenario ID | cw-08-current-dd-medium |
| Scenario purpose | CW-08 loaded policy-revision behavior with current DD, repetition 2. |
| Run ID | 20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt), [prelaunch checks](preflight.json). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T02:45:46.263Z |
| Finished | 2026-09-08T02:46:09.275Z |
| Duration seconds | 23.013 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | aa754f32acb8af0c2acf91185061d033d21d590ed035b6fa07336a2284505cd0 |
| Prompt template | prompt-template.txt | 00a6e1d588d80fe97a4e36af638c7a6193294ac9922e3c1c977adbb7425d8e95 |
| Rendered prompt | prompt.txt | a55815337b66f0f687780d55002d27d6a981a0dec2be8c281465ff47380ec85d |
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
| Rubric | skill-validation/pilot/cw-08/current-dd/rubric.md | 3b32625edddbd4b7455a0020372566c141d7f095a28d85b692d7edab7eba2083 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I1 | Eligibility and exception | PASS | [final](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/final.txt), first paragraph | 501(c)(3), budget below $2 million, eligible fiscal sponsor exception and Appendix A preserved. |
| CW-I1 | Deadline | PASS | [final](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/final.txt), second paragraph | October 15 at 5 p.m. ET; late applications not reviewed. |
| CW-I1 | Accommodation | PASS | [final](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/final.txt), second paragraph | Email action, exact destination and at least five business days retained. |
| CW-I1 | Appeal and finality | PASS | [final](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/final.txt), final paragraph | Denied applicants, ten calendar days, Appeals form and finality retained. |
| CW-I2 | Lossless removal | PASS | [final](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/final.txt) | Meta opener and duplicate deadline removed. |
| CW-I1/I3 | No unsupported meaning | PASS | [final](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/final.txt) | No unsupported fact, advice or software assumption. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer parses this prose. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Output only | FAIL | [full trace](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/stdout.txt) item_0 | Unrequested procedural narration precedes the read and final answer. |
| Read-only task boundary | PASS | [full trace](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/stdout.txt) item_1 and result inventory | Only one fixture-local read; no edits, Git changes, network or dispatch. |
| Explicit CW loading | PASS | [full trace](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/stdout.txt) item_1 before item_2 | sed returns the complete supplied CW body; no other skill loads observed. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: concise, clear paragraphs preserve policy navigation. | [final](../../runs/skilltest-runs/20260908T024546263Z-cw-08-current-dd-medium-204fcc0e-5bf3-47cb-a002-660c68979863-dbx4kz2n/final.txt) |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | All semantic rows pass and protocol is N/A. Procedural narration is a separate fidelity failure; it does not prevent judging the revised artifact. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | No scoring ambiguity; scoped trace evidence does not prove absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Exact argv and prelaunch/final hashes verified against frozen sources; 13 declared fixture files unchanged, only expected template-free Git files present, evidence empty. Complete 7-event trace with final matching. Runner COMPLETED implies successful owned-process/runtime cleanup under the frozen implementation; exact logged runtime /private/tmp/skilltest-cw-baseline.ksDeiD/runs/skilltest-codex-1izaikof is absent. Provider and command stderr empty; version capture has the previously disclosed nonfatal PATH-alias warning. |
