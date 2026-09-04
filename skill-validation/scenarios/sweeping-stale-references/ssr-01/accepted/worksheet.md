# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/sweeping-stale-references/ssr-01 |
| Scenario ID | ssr-01 |
| Scenario purpose | Exercise an end-to-end load-bearing rename with complete discovery, rationale-preserving reconciliation, durable sweep evidence, and verification. |
| Run ID | 20260904T121443909Z-ssr-01-4346520c-e0e8-4820-8a09-95e78a91e149-6fjw15ue |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T12:14:43.909Z |
| Finished | 2026-09-04T12:15:31.030Z |
| Duration seconds | 47.122 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 26412b69e8ff095950c21d5ad5b5fbf600d46bba644b37668532536d50284542 |
| Prompt template | prompt-template.txt | b87520036c0f72d5eadeb9d43f1cc50ed2ff144f604e5ca7b9277f1fb51390c3 |
| Rendered prompt | prompt.txt | 1d41bf3397b5a775480eb31faf90a9fa91ec74f3afbe10429eb3b084370f78cc |
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
| Rubric | skill-validation/scenarios/sweeping-stale-references/ssr-01/rubric.md | ce3ee9983a4ab647b11010c0d2760ec62cff47f85e0e7fab1ad502044fb95ac2 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| SSR-I1 | Inspect both supplied project files and search the old and intended-new symbol and prose encodings broadly enough to discover the complete rename surface. | PASS | final.txt:1,3-5,8; workspace/fixture/project/src/session.py:1-3; workspace/fixture/project/docs/session-policy.md:1-3 | The run inspected both named paths and its project-wide rename search found the exact three rename references: the source comment, declaration, and policy prose. The exact inspection and search commands are observable in the scratch provider transcript; the accepted result records that transcript only by hash. |
| SSR-I2 | Truthfully classify and account for every mutable match, with precise paths, locations, outcomes, per-group counts, and reconciled totals. | PASS | final.txt:1,3-5 | The inventory reports three matches across two paths, classifies all three as `update`, identifies lines 1 and 3 in `src/session.py` and line 3 in `docs/session-policy.md`, and reconciles the per-path counts to the total. |
| SSR-I3 | Reconcile the symbol and prose rename together while preserving the actual constraint and accepted cost: the partner rejects longer sessions, and more frequent refreshes are accepted to preserve compatibility. | FAIL | final.txt:3-5; workspace/fixture/project/src/session.py:1-3 | The response calls line 1 a prose update but never states the replacement prose or says that the partner-rejection constraint will be preserved. It also gives no preservation account for the accepted frequent-refresh cost on adjacent line 2. A location and generic `prose` label establish inventory, not preservation of the two protected meanings. |
| SSR-I4 | Return durable `References swept:` evidence followed by truthful project-level `Verification:` whose paths, locations, outcomes, and counts reconcile. | PASS | final.txt:1-8 | `References swept:` precedes `Verification:`; the two path rows, three locations, update counts, inventory total, and verification total all agree. The verification truthfully reports observed discovery rather than fabricating a post-edit state. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The artifact is human-read commit-body evidence, and the rubric explicitly permits equivalent wording and layout. Structural ordering is graded as semantic/task fidelity rather than an external parser contract. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only commit-body evidence for the rename, ending with project-level `Verification:` and without evaluator, harness, read-only, or unrelated-procedure narration. | PASS | final.txt:1-8 | The response is limited to a sweep inventory, `References swept:`, and `Verification:`. It ends in the requested section and contains none of the prohibited narration. |

## Readability

| Observation | Evidence |
|---|---|
| The evidence is concise and easy to reconcile, but its terse `prose` label omits the semantic preservation evidence needed for SSR-I3. | final.txt:1-8 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | The run is mechanically complete and judgeable. SSR-I1, SSR-I2, SSR-I4, and task fidelity pass: it inspected the supplied surface, found and accounted for exactly three updates across two paths, and returned coherent sweep and verification evidence. SSR-I3 fails because the artifact does not demonstrate preservation of either protected rationale element—the partner's rejection of longer sessions and the accepted cost of more frequent refreshes. The generic `prose` label is sufficient inventory evidence but not rationale-preservation evidence. No deterministic protocol applies. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `FAIL` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | The response's line-1 `prose` update could be read as implying a minimal phrase substitution that leaves the rest of that comment intact, and line 2 is not itself a rename match. The rubric nevertheless makes preservation of both meanings an explicit composite behavior, so unshown replacement prose and silence about the adjacent accepted-cost sentence cannot establish it. |
| Scenario defects | None affecting judgment. The read-only prompt permits truthful pre-edit verification, and the model could have made preservation judgeable within commit-body evidence by naming the retained partner constraint and accepted refresh cost. The provider emitted one recovered internal command-launch error to stderr, then completed the relevant inspections and searches successfully; this did not make the run an infrastructure failure. |
| Proposed methodology changes | Clarify the evidence-lifecycle rule for action-based criteria. Here the scratch provider transcript proves the inspection/search actions, while the accepted `result.json` would retain only its hash. Either require the final artifact to carry enough action evidence for later re-adjudication or define when provider transcripts become accepted evidence. This is a process question for later consolidation, not a runner change needed for this verdict. |
