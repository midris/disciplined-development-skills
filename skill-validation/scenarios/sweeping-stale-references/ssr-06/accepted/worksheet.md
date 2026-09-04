# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/sweeping-stale-references/ssr-06 |
| Scenario ID | ssr-06 |
| Scenario purpose | Identify exactly the symbol, attached-rationale, and documentation updates required by the session rename. |
| Run ID | 20260904T150105500Z-ssr-06-a5f593d4-6124-419b-8f44-d64b4e89d05a-7govul_i |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T15:01:05.500Z |
| Finished | 2026-09-04T15:01:31.067Z |
| Duration seconds | 25.567 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 512daf6555428749dbfd2eab211966f1f334d80b94af666d41c8d964e9b1ef58 |
| Prompt template | prompt-template.txt | a39d26e62ad7ec6070e51655b0282ac8072547349f12ae39e0642f541dc1c401 |
| Rendered prompt | prompt.txt | b395663a6afb743e0499fb99241baa89a4b16cb7e682ab3b0873e50ac2c28940 |
| Fixture | project/docs/session-policy.md | a925897761b094ba37bf8f7825ceab7fac62a48beeea310dbb5f412ef74d1d0c |
| Fixture | project/src/session.py | a975fc6bef67344143832d89a6b24b12a8b59da4682236c842f8639eb9378cd2 |
| Fixture | skills/adversarial-review-loop/SKILL.md | 46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6 |
| Fixture | skills/adversarial-review/SKILL.md | 9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c |
| Fixture | skills/concise-writing/SKILL.md | 4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72 |
| Fixture | skills/disciplined-development/SKILL.md | 1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec |
| Fixture | skills/disciplined-research/SKILL.md | a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50 |
| Fixture | skills/dispatching-development-subagents/SKILL.md | b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500 |
| Fixture | skills/lean-plan-writing/SKILL.md | 6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac |
| Fixture | skills/sweeping-stale-references/SKILL.md | d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157 |
| Fixture | skills/writing-explicit-rationale/SKILL.md | 97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/sweeping-stale-references/ssr-06/rubric.md | 286a3a8eab4c9aac655454036fa1b590856f230bf11f0db97841a6d2d0040ccb |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| SSR-I2 | Classify every required rename match as an update without inventing an additional match. | PASS | final.txt:1-6; workspace/fixture/project/src/session.py:1-3; workspace/fixture/project/docs/session-policy.md:1-3 | The artifact identifies exactly three updates: two in `session.py` and one in `session-policy.md`. It does not misclassify the accepted-tradeoff sentence on source line 2 as a fourth replacement. |
| SSR-I4 | Distinguish and completely account for the exact symbol replacement, attached-comment prose replacement, and documentation prose replacement, followed by verification. | PASS | final.txt:1-6 | The source row separately names `TOKEN_TTL_MINUTES` → `SESSION_TTL_MINUTES` and `token TTL` → `session TTL` at lines 3 and 1; the documentation row names the prose replacement at line 3. The per-row counts reconcile to the verified total of three, and `Verification:` follows the sweep. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The inventory is interpreted by a maintainer, and the rubric expressly grades completeness and accounting rather than exact wording, layout, or labels beyond the durable section destinations. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only a concise `References swept:` artifact followed by `Verification:`. | PASS | final.txt:1-7 | The response uses only the two requested sections and is concise. The workspace-specific `fixture/` path prefixes and `Read-only evaluation; no files modified` line are unnecessary evaluator-context leakage, but neither obscures the project paths or adds an unsupported match. |

## Readability

| Observation | Evidence |
|---|---|
| The replacement pairs, locations, and counts are easy to audit. Repository-relative paths and project-level verification would make the artifact more directly reusable. | final.txt:1-7 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. SSR-I2 and SSR-I4 pass for this atomic inventory case: the artifact identifies exactly the source symbol, attached-comment prose, and documentation prose replacements, distinguishes symbol from prose, reconciles the total to three, and invents no fourth match. SSR-I1 broad search execution and SSR-I3 rationale preservation are not independently exercised. The workspace path prefixes and evaluator-status verification are non-blocking task-fidelity observations under this rubric. No deterministic protocol applies. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `PASS` baseline with non-blocking task-fidelity observations. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting semantic judgment. `fixture/project/...` is a workspace-rooted spelling of the supplied `project/...` path rather than an additional path, and the exact line locations disambiguate both targets. |
| Scenario defects | None affecting judgment. The prompt asks for commit-body evidence from a read-only evaluator without the explicit project-level-verification guard used by SSR-01, so evaluator-status narration is foreseeable; the rubric correctly confines the owning verdict to inventory completeness and accounting. |
| Proposed methodology changes | Consider applying the same explicit verification guard used by SSR-01 to future read-only inventory scenarios: require project-level evidence and prohibit evaluator/read-only narration. This would improve artifact fidelity but is not needed to judge the present inventory behavior. |
