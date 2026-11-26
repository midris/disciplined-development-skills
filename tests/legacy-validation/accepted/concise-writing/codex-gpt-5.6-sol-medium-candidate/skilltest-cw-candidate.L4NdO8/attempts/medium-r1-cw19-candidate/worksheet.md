# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-19/current-dd |
| Scenario ID | cw-19-candidate-medium |
| Scenario purpose | Loaded CW effectiveness on complex operational prose: lossless compression and explicit safety boundaries. |
| Run ID | 20260909T011325128Z-cw-19-candidate-medium-d0db3be9-d381-40a8-91a0-e94d40f63587-sc2mfspp |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-09T01:13:25.128Z |
| Finished | 2026-09-09T01:13:52.320Z |
| Duration seconds | 27.192 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | f425029774e1e23fb384e98368b1892c5a8a6a18c8d85483691169934349eb4b |
| Prompt template | prompt-template.txt | 4a80e4c7a19286397624bd2e00d398d1d3c2568fdad1c9032fe6e71f1c84bf80 |
| Rendered prompt | prompt.txt | 962e9a0195cd32abbc0c8396d5d8c194fdbb3ed4157c16b3e77cabcb0554e314 |
| Fixture | .agents/skills/adversarial-review-loop/SKILL.md | 46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6 |
| Fixture | .agents/skills/adversarial-review/SKILL.md | 9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c |
| Fixture | .agents/skills/concise-writing/SKILL.md | f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba |
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
| Rubric | skill-validation/pilot/cw-19/current-dd/rubric.md | cac093e5ab9ccd8f98e2746d66b8dc8d6cff00b2646b780d7c847154a2334233 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I2 | Remove meta-framing and duplicate readiness/GO | PASS | [final][final] | Opens with actionable preflight; each readiness and approval instruction has one home. |
| CW-I1 | Preserve preflight actor, command and evidence | PASS | [final][final] | Release engineer runs exact preflight command and attaches JSON/snapshot ID to CHG-4821 before promotion. |
| CW-I1 | Preserve combined readiness window | PASS | [final][final] | At most 2 seconds and below 0.1% in the same uninterrupted 15-minute window. |
| CW-I1 | Preserve explicit stop thresholds and escalation | FAIL | [final][final] | Replaces explicit lag >2 / mismatch >=0.1 conditions with either metric breaches its limit. This does not explicitly preserve the equality-triggered 0.1% mismatch stop, the rubric’s declared ambiguity boundary; BLOCKED/ticket/channel/commander remain. |
| CW-I1 | Preserve ordered approval/promotion | PASS | [final][final] | Readiness passes, release engineer posts link, waits for commander GO, only then exact promote command. |
| CW-I1 | Preserve force prohibition and causal risk | PASS | [final][final] | --force skips readiness/GO checks and risks partially backfilled rows. |
| CW-I1 | Preserve irreversible rollback boundary | PASS | [final][final] | First application-accepted write containing orders-v3-only field; exact rollback command forbidden afterward because old schema cannot represent it. |
| CW-I1 | Preserve recovery authority and source | PASS | [final][final] | Only DB incident commander, explicitly not release engineer, chooses forward or recorded pre-cutover snapshot restore. |
| CW-I1 | No unsupported meaning | PASS | [final][final] | No new requirement or assumption; threshold loss is scored separately above. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer | N/A | Frozen rubric | Ordinary prose/JSON presentation is not a deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Complete CW read | PASS | [trace][trace] | Full candidate cat before revision. |
| Revision-only output and boundaries | PASS | [trace][trace] | Only revised documentation; no narration, mutation, execution of quoted commands, outside reads, network or dispatch. |

## Readability

| Observation | Evidence |
|---|---|
| PASS — navigable three-section procedure with clear actors and order; threshold precision failure is scored semantically. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | Most facts and compression are preserved, but replacing an explicit inclusive mismatch stop threshold with breaches its limit fails the frozen losslessness criterion. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Complete visible trace cannot establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command/provider exit 0; exact argv, frozen inputs, artifact/prelaunch hashes, protected fixtures and owned cleanup verified. Complete visible trace, empty provider/command stderr; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260909T011325128Z-cw-19-candidate-medium-d0db3be9-d381-40a8-91a0-e94d40f63587-sc2mfspp/final.txt
[trace]: ../../runs/skilltest-runs/20260909T011325128Z-cw-19-candidate-medium-d0db3be9-d381-40a8-91a0-e94d40f63587-sc2mfspp/stdout.txt
