# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-14/discovery |
| Scenario ID | cw-14-discovery-medium |
| Scenario purpose | CW-14 native discovery for a read-only reference-authoring decision. |
| Run ID | 20260908T113635133Z-cw-14-discovery-medium-a917c968-4e39-425c-87f2-a93c531ad02e-naaj9cx7 |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T11:36:35.133Z |
| Finished | 2026-09-08T11:38:58.223Z |
| Duration seconds | 143.09 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 695b8d03fb36c9647d26f50e4cb8912b5a3511b788bf8adc8b00abbc5c85b586 |
| Prompt template | prompt-template.txt | 2dca0926ef4a374eb73044a6bff94b1e508afc4934224900a153e990605230b7 |
| Rendered prompt | prompt.txt | 2dca0926ef4a374eb73044a6bff94b1e508afc4934224900a153e990605230b7 |
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
| Fixture | .agents/skills/test-driven-development/SKILL.md | bf1b8216e523851a411e91d429a7c1c2a173e79d88957bc78e348218d50edd54 |
| Fixture | .agents/skills/writing-explicit-rationale/SKILL.md | 97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .agents/skills/writing-skills/SKILL.md | d34db5c8aed6a4e0440132bd0613aace70a693ec7819d5637ad77481d8e10d1b |
| Fixture | .agents/skills/writing-skills/testing-skills-with-subagents.md | c711346852c911b24a84aa161e0cff06a4cd7f4e2fa9e9c0a266cead5afcbade |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-14/discovery/rubric.md | 55fae33210fa5844181a95243997d930db799683df650f9b2d95306e32a43dda |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Authoring composition / native selection | CW selection | PASS | [trace][trace], item_3 | Full CW returned in a bundled read with WS, DD, DR, AR and WER before substantive decision. |
| superpowers:writing-skills / native selection | Authoring owner selection | PASS | [trace][trace], items 3, 5, 9 | WS prefix read in item_3 and complete body in item_5; both precede the go/no-go decision in item_9. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Task and boundaries | PASS | [trace][trace], all items; inventory | Gives decision/explanation without actual editing, tests, deployment, Git mutation, outside-fixture reads, network or dispatch. Progress allowed in this discovery task. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: clear no-merge decision, source-linked reasons and next steps. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Both target bodies fully returned before substantive decision; bundled/composition-mediated exposure, not independent routing or executed lifecycle proof. |
| Disposition | Scratch-only pending owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Item_4 calls a premise suspect and expressly says it is checking requirements before deciding; it does not yet issue an approval disposition. Unlike CW-13 item_3's definite insufficiency judgment, the substantive go/no-go decision is item_9 after full WS loading. Raw body exposure does not prove internal application/delivery. |
| Scenario defects | None invalidating observed. Optional fixture-local .codex search returns exit 2 because that directory is absent; target skills remain available. |
| Proposed methodology changes | None. Command exit 0; all 20 events inspected, tool body outputs exactly reconciled to frozen slices and remaining listing/status/error output read. Apple developer-tool cache/event-stream warnings during git status are nonfatal; fixture Git remains unchanged. Exact argv, artifact/prelaunch hashes and frozen sources verified; 16 protected fixtures unchanged, expected Git files only, evidence empty. COMPLETED establishes owned cleanup under frozen runner; logged runtime /private/tmp/skilltest-cw-baseline.bOn8Dx/runs/skilltest-codex-_bm6kcs7 absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. Incidental DD, DR, AR, WER, TDD and testing-reference reads disclosed; no irrelevant-skill exclusion is imposed. |

[final]: ../../runs/skilltest-runs/20260908T113635133Z-cw-14-discovery-medium-a917c968-4e39-425c-87f2-a93c531ad02e-naaj9cx7/final.txt
[trace]: ../../runs/skilltest-runs/20260908T113635133Z-cw-14-discovery-medium-a917c968-4e39-425c-87f2-a93c531ad02e-naaj9cx7/stdout.txt
