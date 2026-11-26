# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-17/discovery |
| Scenario ID | cw-17-discovery-medium |
| Scenario purpose | CW-17 native non-trigger for a detailed response-only explanation; current-DD available. |
| Run ID | 20260908T024255855Z-cw-17-discovery-medium-2ea8afcf-2a6a-4d07-8fdb-17161df6a00d-hrpoc_cd |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt), [prelaunch checks](preflight.json). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T02:42:55.855Z |
| Finished | 2026-09-08T02:44:14.795Z |
| Duration seconds | 78.94 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | ba4ddb0dfd204b88560575a880459441d2bce85fcd7bead121425a09a38e46bc |
| Prompt template | prompt-template.txt | ce90fecc0cc9a2a764863b797d50ef232e5b013437cf320d8251009bc5c4cd1c |
| Rendered prompt | prompt.txt | ce90fecc0cc9a2a764863b797d50ef232e5b013437cf320d8251009bc5c4cd1c |
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
| Rubric | skill-validation/pilot/cw-17/discovery/rubric.md | 5692e3cdf6c73670df719360439a6430e50838a27707df70b972f90b0d05457d |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I3 | No observed CW selection/body access | PASS | [full trace](../../runs/skilltest-runs/20260908T024255855Z-cw-17-discovery-medium-2ea8afcf-2a6a-4d07-8fdb-17161df6a00d-hrpoc_cd/stdout.txt), all four events | Completed task; no tool calls, invocation claim or CW selection in the sole model message. Qualified availability and complete observable trace support scoped non-selection, not hidden non-use. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer parses this prose. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Perform requested detailed task | PASS | [final](../../runs/skilltest-runs/20260908T024255855Z-cw-17-discovery-medium-2ea8afcf-2a6a-4d07-8fdb-17161df6a00d-hrpoc_cd/final.txt) | Detailed clothing-swap guidance covering planning, venue, rules, volunteers, supplies, screening, event operation and follow-up; response only. |
| Read-only boundaries | PASS | [full trace](../../runs/skilltest-runs/20260908T024255855Z-cw-17-discovery-medium-2ea8afcf-2a6a-4d07-8fdb-17161df6a00d-hrpoc_cd/stdout.txt) and final inventories | No tool calls, edits, Git changes, outside reads, network or dispatch. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: detailed, navigable numbered sections and concrete operational guidance; length is appropriate to the explicit request and is not a selection proxy. | [final](../../runs/skilltest-runs/20260908T024255855Z-cw-17-discovery-medium-2ea8afcf-2a6a-4d07-8fdb-17161df6a00d-hrpoc_cd/final.txt) |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Non-trigger criterion passes on complete observable trace with qualified target availability. No observed CW use; no claim of hidden provider non-use. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | No scoring ambiguity; scoped trace evidence does not prove absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Exact argv and prelaunch/final hashes verified against frozen sources; 13 declared fixture files unchanged, only expected template-free Git files present, evidence empty. Complete 4-event trace with final matching. Runner COMPLETED implies successful owned-process/runtime cleanup under the frozen implementation; exact logged runtime /private/tmp/skilltest-cw-baseline.ksDeiD/runs/skilltest-codex-lnia9hvu is absent. Provider and command stderr empty; version capture has the previously disclosed nonfatal PATH-alias warning. |
