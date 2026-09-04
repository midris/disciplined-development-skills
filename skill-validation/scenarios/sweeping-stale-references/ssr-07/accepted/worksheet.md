# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/sweeping-stale-references/ssr-07 |
| Scenario ID | ssr-07 |
| Scenario purpose | Preserve the partner constraint and accepted refresh cost while renaming the session-setting rationale. |
| Run ID | 20260904T153811171Z-ssr-07-1a7151db-0927-44ea-9e35-3f0d92e4c201-_ropzxhc |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T15:38:11.171Z |
| Finished | 2026-09-04T15:38:41.270Z |
| Duration seconds | 30.099 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | ad91d9325fa8305ce1179832ed726612c6b1afdc344d082ca4cea19c88359c67 |
| Prompt template | prompt-template.txt | 86a40957dad5091eac5f650ad44f8a71ab85aa318038f77e982952fa7294187f |
| Rendered prompt | prompt.txt | 432b53194f3c004e803df7deacc98eabc47350a037764ffb4a03d944d7e7d05d |
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
| Rubric | skill-validation/scenarios/sweeping-stale-references/ssr-07/rubric.md | cf1d686418a9791137c14f539494041b91f32e855c3858ca757dc1f432ce24b7 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| SSR-I3 | Rename the setting's prose to `session TTL` while preserving the actual causal constraint and accepted cost: the partner rejects longer sessions, and more frequent refreshes are accepted to preserve compatibility. | PASS | final.txt:1-6; workspace/fixture/project/src/session.py:1-3 | The replacement comment uses the new `session TTL` prose, retains the 30-minute setting because the partner rejects longer sessions, and explicitly preserves the accepted consequence of more frequent refreshes for partner compatibility. The explanation independently names the limit, constraint, and tradeoff. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | A maintainer interprets the replacement comment and explanation, and the rubric expressly excludes exact prose and formatting from judgment. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only the proposed replacement comment block and a one-sentence preservation explanation. | PASS | final.txt:1-6 | The response contains exactly a two-line comment block and one explanatory sentence, without process narration or unrelated content. Markdown fencing is a harmless presentation choice. |

## Readability

| Observation | Evidence |
|---|---|
| The comment is concise, idiomatic, and explicit about both the constraint and accepted consequence; the explanation is direct. | final.txt:1-6 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. SSR-I3 passes: the proposed comment uses the renamed session terminology while preserving the complete rationale chain—the 30-minute setting, the partner's rejection of longer sessions, and the consciously accepted cost of more frequent refreshes to preserve compatibility. SSR-I1 search behavior, SSR-I2 inventory disposition, and SSR-I4 sweep evidence are not independently exercised by this atomic rationale scenario. No deterministic protocol applies. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `PASS` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting judgment. The rubric permits either the new symbol or prose form, so `session TTL` fully satisfies the rename requirement without repeating `SESSION_TTL_MINUTES` in the comment. |
| Scenario defects | None observed. The fixture supplies both protected meanings, and the prompt requires replacement prose plus a preservation explanation, making semantic loss directly judgeable. |
| Proposed methodology changes | None. This focused scenario cleanly isolates rationale preservation from inventory and evidence formatting. |
