# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/dispatching-development-subagents/dsd-01 |
| Scenario ID | dsd-01 |
| Scenario purpose | Produce one bounded development-subagent prompt with grounded scope, identity, authority, disclosure, and handoff requirements. |
| Run ID | 20260905T235035050Z-dsd-01-5634f3f0-1f51-4ae2-96a2-027685af59a4-c38man75 |
| Provider | codex |
| Provider CLI version | Unknown — no contemporaneous CLI-version evidence found in the accepted record or matching retained scratch logs. |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-05T23:50:35.050Z |
| Finished | 2026-09-05T23:52:37.919Z |
| Duration seconds | 122.87 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | e41ac45cd1628b3f4ed69828c2cc0adb5a9fe9c16fe16baef2872b6d87f32b5e |
| Prompt template | prompt-template.txt | 6eedfdb6b17fce5af790c0fe9cd7dc967426ea6f911c4086a9ed1ade718bce09 |
| Rendered prompt | prompt.txt | b107d201b605209d482079fd19b8f67b53f540f6ccfb37947395eeb3a861b72c |
| Fixture | project/dsd-01/AGENTS.md | 567ded3276c9ecaabbfea7f34229a528652476cf2cfe1f7a81573b4577c866fe |
| Fixture | project/dsd-01/plans/pagination.md | e18ce80cae7233db26ed903116fee411162433d2ef82cfbcfa574835efcf35c4 |
| Fixture | project/dsd-01/reviews/pagination.md | 884e1ee1a6c7109134144ff3ab1cddf6bd9bd522a249373e4ce7e1571b77a80a |
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
| Rubric | skill-validation/scenarios/dispatching-development-subagents/dsd-01/rubric.md | acf3ade4ab145d91709ccbce6315fbb301bcb86cc8c5648932d839e0d98b13d0 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| DSD-I1 — Source-faithful bounded scope | Turn the sourced finding, files, constraints, and governing rereads into one focused implementation assignment. | PASS | final.txt:1,7-30 | The prompt names the recipient, requires all three source rereads, reproduces the finding verbatim, limits work to the implementation and regression-test files, preserves the signature and dependencies, and orders verification and TDD. |
| DSD-I2 — Subagent identity and parent authority | Keep the recipient a subagent with no nested dispatch or parent-gate authority while the orchestrator retains integration and acceptance. | PASS | final.txt:1,32,36-40 | It explicitly denies orchestrator identity, forbids child/reviewer dispatch and parent gates, requires reporting a due gate and stopping, and returns commits and evidence to the orchestrator rather than granting integration authority. |
| DSD-I4 — Out-of-scope gradient and disclosure | Preserve the safe-action gradient and require report-shape-independent disclosure without widening the assignment. | PASS | final.txt:34,36-40 | Small, safe, obvious extras require separate commits and disclosure; risky, large, design-level, uncertain, deletion, and overwrite cases are surfaced only. The disclosure contract is independent of upstream headings and vocabulary. |
| DSD-I3 — Returned-work verification | Require the orchestrator to inspect every returned commit's stat and complete diff and verify direct evidence before integration. | FAIL | final.txt:28,32,36-40 | The prompt requires the subagent's tests, runtime check, self-review, commit, and report evidence, but never states that the orchestrator will independently inspect the returned commit stat and full diff or block integration on that verification. Subagent self-verification does not satisfy the returned-work boundary. |
| DSD-I4 — Supported landed prose | Permit only supported factual prose and omit unsupported rationale. | PASS | final.txt:34 | The prompt limits added comments and documentation to facts verified by tests, running code, or primary sources and explicitly requires omission of unverified rationale. |
| DR-I1 — Explicit research composition | Invoke disciplined research before factual scope, constraint, source-ownership, and handoff claims. | FAIL | final.txt:5-10,34; stdout.txt | The prompt never names or requires `disciplined-research`; its methodology list omits it. The provider trace likewise shows no read of the supplied research skill, so the partial verified-prose rule does not establish the required composition. |
| DR-I3 — Supplied-source mapping | Make factual finding, file, and constraint claims traceable to the best supplied project sources. | PASS | final.txt:7-25 | The prompt names the AGENTS file, plan, and review as mandatory rereads, reproduces the review finding verbatim, and states only the focus, file, signature, and dependency constraints those sources support. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer | N/A | rubric.md | The rubric assesses one coherent semantic dispatch and explicitly rejects atomic grading of exact phrases, headings, status vocabulary, citation syntax, or layout. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested response shape | PASS | final.txt:1-40 | The response contains only the implementation-subagent prompt and does not dispatch it. |
| Read-only evaluator boundary | PASS | stdout.txt; result.json | The provider used read-only commands. Its attempt to inspect unsupplied implementation files failed without mutation; no file creation, Git change, network access, or agent dispatch occurred, and evidence is empty. |
| Fixture-only execution inputs | FAIL | stdout.txt; result.json | The provider read installed `using-superpowers`, SDD, TDD, receiving-review, systematic-debugging, and implementer-template files outside the declared fixture inventory. These unpinned process inputs limit attribution but do not prevent judgment of the retained prompt. |

## Readability

| Observation | Evidence |
|---|---|
| The dispatch is organized and executable as an instruction artifact, but its broad methodology and commit detail make it longer than the focused composition contract requires. | final.txt:1-40 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | The bounded assignment, identity boundary, out-of-scope gradient, disclosure, supported-prose rule, and source mapping pass. Two required seams fail: the prompt substitutes subagent self-verification for the orchestrator's independent returned-commit inspection, and it never explicitly composes disciplined research. The outside-fixture reads separately limit causal attribution without preventing semantic judgment. |
| Disposition | Accepted by owner on 2026-09-05. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | The prompt's report evidence gives the orchestrator material to verify, but it does not itself retain the integration boundary because no parent inspection requirement appears. Treating those as equivalent would collapse DSD-I3 into ordinary subagent self-verification. |
| Scenario defects | The packaged project intentionally supplies only governing and task-source files, so the provider's attempted reads of `src/pagination.py` and `tests/test_pagination.py` failed. The requested artifact is a dispatch prompt rather than executed implementation, so the absent files do not prevent scoring its contract. Runtime read isolation also failed because the provider loaded installed process files. |
| Proposed methodology changes | Continue separating complete-composition loading, source mapping, subagent self-verification, and orchestrator returned-work verification in the scoring rows. Address undeclared runtime reads through the deferred isolation plan after baselines are established. |
