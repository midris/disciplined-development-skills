# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-01/no-dd |
| Scenario ID | cw-01-no-dd-medium |
| Scenario purpose | CW-01 prose-conservation no-DD control; common Superpowers retained. |
| Run ID | 20260908T105416797Z-cw-01-no-dd-medium-d5b9fb08-6277-4281-934a-9213af99a2cb-v5suzwwv |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T10:54:16.797Z |
| Finished | 2026-09-08T10:54:23.976Z |
| Duration seconds | 7.18 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | d2e335fdfa2175371d8dab83287c33ecf98a9dda6a9f5bd76f5b5aa22df2e213 |
| Prompt template | prompt-template.txt | 56a9c1f62782b81ed01801acaeef034534abb21ec55963863e941f4d1c10de86 |
| Rendered prompt | prompt.txt | 56a9c1f62782b81ed01801acaeef034534abb21ec55963863e941f4d1c10de86 |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-01/no-dd/rubric.md | 06a8adb2930f11c242dec98476a9640bf581fc000bd624d3ad4a50f658533d88 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I1 | Preserve all four states | PASS | [final][final] | Queued, running, complete and failed retained. |
| CW-I1 | Preserve distinct outcomes | PASS | [final][final] | Complete has a download link; failed has an error code. |
| CW-I1 | Add no unsupported meaning | PASS | [final][final] | Ordinary glosses of queued/running/failed restate the supplied state meanings; no new operational fact or advice. |
| CW-I2 | Remove targeted padding | PASS | [final][final] | Meta opener and both duplicate explanations removed; one account of each state/outcome. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer parses the prose. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Deliverable and task boundaries | PASS | [full trace][trace], item_0; result inventory | Only the revised section; no tool actions or extra narration. |
| Explicit target loading | N/A | No-DD config | DD is deliberately absent. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: one scan-friendly section with clear state/outcome associations. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | All four semantic criteria pass; protocol N/A and task fidelity PASS. A passing no-DD control is retained, not declared RED. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Ordinary state-name glosses introduce no consequential new meaning. Scoped traces do not establish absence of hidden provider inputs. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; complete four-event trace, final matches. Exact argv, all artifact and prelaunch hashes, frozen sources and four protected fixture files verified; only expected template-free Git files, evidence empty. COMPLETED establishes successful owned-process/runtime cleanup under the frozen runner; logged runtime /private/tmp/skilltest-cw-baseline.bOn8Dx/runs/skilltest-codex-d29h2yu_ is absent. Provider/command stderr empty; version-only PATH-alias warning matches qualification. |

[final]: ../../runs/skilltest-runs/20260908T105416797Z-cw-01-no-dd-medium-d5b9fb08-6277-4281-934a-9213af99a2cb-v5suzwwv/final.txt
[trace]: ../../runs/skilltest-runs/20260908T105416797Z-cw-01-no-dd-medium-d5b9fb08-6277-4281-934a-9213af99a2cb-v5suzwwv/stdout.txt
