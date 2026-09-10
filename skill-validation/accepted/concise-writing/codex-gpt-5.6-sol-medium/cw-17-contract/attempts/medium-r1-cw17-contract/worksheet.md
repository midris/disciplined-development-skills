# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-17/contract |
| Scenario ID | cw-17-contract-medium |
| Scenario purpose | CW-17 loaded scope diagnostic: detailed response-only exception. |
| Run ID | 20260908T114057456Z-cw-17-contract-medium-149633dc-9eb4-4ed1-a007-983755ec358e-s23k5l28 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T11:40:57.456Z |
| Finished | 2026-09-08T11:41:12.795Z |
| Duration seconds | 15.339 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 4389559d83ff72a2f7189f80549aeea6902d28c79e8902ed634d31ea1c78680b |
| Prompt template | prompt-template.txt | a2770d0bf427eb95c6e64de16caed56f1cb873527820aabc8a7d6624f7583384 |
| Rendered prompt | prompt.txt | 017bbe8521da36fe0f2d4f15b67912d15ed1fc92d78f61f198131aac070d1106 |
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
| Rubric | skill-validation/pilot/cw-17/contract/rubric.md | 6f7c5eafe1cba3f6a43af4f65bb57af23c34e0bf5c3018567e25103173c815f3 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| CW-I3 | Detailed-response boundary | FAIL | [final][final] | Returns true; target charter requires false for an explicitly detailed response-only explanation. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | JSON has no authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested loading | PASS | [trace][trace], item_0 | Complete supplied CW before scope answer. |
| Deliverable and boundaries | PASS | [trace][trace], items 0–1; inventory | Compact single-boolean JSON only; does not execute embedded request. Fixture-local read, no mutation/narration. |
| Supplied-body consistency | PASS | [trace][trace], full CW | Supplied body broadly covers reader-facing prose and lacks detailed-response exemption; true is consistent with that text. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: boolean answer is unambiguous. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | Intended detailed-response exception fails despite body-consistent interpretation. This is scope-contract interpretation, not native discovery or proof of hidden application. |
| Disposition | Scratch-only pending owner acceptance; retain judgeable failure. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Declared body/charter mismatch retained; hidden provider inputs remain outside trace proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; six-event complete trace and matching final. Exact argv, artifact/prelaunch hashes and frozen sources verified; 13 protected fixtures unchanged, expected template-free Git files only, evidence empty. COMPLETED establishes owned cleanup under frozen runner; logged runtime /private/tmp/skilltest-cw-baseline.bOn8Dx/runs/skilltest-codex-xlq6p18s absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T114057456Z-cw-17-contract-medium-149633dc-9eb4-4ed1-a007-983755ec358e-s23k5l28/final.txt
[trace]: ../../runs/skilltest-runs/20260908T114057456Z-cw-17-contract-medium-149633dc-9eb4-4ed1-a007-983755ec358e-s23k5l28/stdout.txt
