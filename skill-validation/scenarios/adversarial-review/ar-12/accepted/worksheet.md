# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/adversarial-review/ar-12 |
| Scenario ID | ar-12 |
| Scenario purpose | Reject activity or proxy success that does not measure the governing outcome. |
| Run ID | 20260905T152427448Z-ar-12-ac1480d9-e95d-4525-b0b8-78630dcf9c99-weg4b5dl |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-05T15:24:27.448Z |
| Finished | 2026-09-05T15:25:09.385Z |
| Duration seconds | 41.937 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | a8924b21788702b367360a6a9c7e62e8c4fbafe21476a90ebcf286beba9c9305 |
| Prompt template | prompt-template.txt | 4f268b13214207496769286295cec06d7ab0925b72c9b52195b26d9c12bc2a6a |
| Rendered prompt | prompt.txt | f43f6735d9aa597b228620df4cf6a4928cd50cdce0d5f10d75072a97e5d350e8 |
| Fixture | project/brief.md | 0ee6c05cbe47371847150bd6c497e52c45eddee35602d1f6ef5321a085ed4db7 |
| Fixture | project/proposal.md | 2981b6228802eaa93ee1bf2f78373e2634ab8eb4a2cf07997c119bbaea5f5146 |
| Fixture | skills/adversarial-review/SKILL.md | 9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c |
| Fixture | skills/superpowers/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | skills/superpowers/requesting-code-review/code-reviewer.md | b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/adversarial-review/ar-12/rubric.md | 0b84e78ffb224c2cf3be29eb4bb0ec45cb6d02f16021ba392b93859c3a2c5f99 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| AR-I3 — Proxy rejection | Report as P0, P1, or P2 that wizard completion does not establish reduced time from signup to first successful export. | PASS | final.txt:1-2; fixture/project/brief.md:3; fixture/project/proposal.md:4 | The P1 finding says final-screen completion measures neither elapsed time from signup nor successful export and could reach 90% while the target median worsens or remains unchanged. |
| AR-I3 — Outcome measurement | Require the rollout criterion to measure the stated time-to-success outcome rather than accept mechanism completion as proof. | PASS | final.txt:1-2 | Calling the rollout criterion defective because it does not measure the governing outcome, naming both outcome components, and blocking the proposal rejects the proxy as proof and makes outcome measurement the required acceptance basis. Semantic equivalence does not require an imperative replacement sentence. |
| AR-I1 — Blocking disposition | End with DD-VERDICT: BLOCK as the final nonblank line. | PASS | final.txt:4 | The exact blocking verdict is final and agrees with the P1 proxy-metric defect. |
| Review boundary | Do not edit, remediate, loop, or dispatch agents. | PASS | stdout.txt:4,6,8; result.json | Three completed shell commands only list or read files. No edits, remediation loop, or dispatch occurred. All five supplied fixtures match their original bytes and evidence is empty. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic response consumer applies. | N/A | prompt.md; rubric.md | The response is manually interpreted. No renderer, parser, validator, or production consumer is supplied. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only the adversarial-review output for the supplied proposal. | PASS | final.txt:1-4 | The response contains one located P1 finding, its concise reasoning, and the required terminal verdict. |
| Fixture-only execution inputs | FAIL | stdout.txt:4 | The provider successfully read /Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/using-superpowers/SKILL.md outside the declared fixtures. This unpinned process instruction is absent from result.json's fixture inventory. It limits attribution to the pinned skill but does not prevent direct judgment of whether the retained response rejects the proxy. |

## Readability

| Observation | Evidence |
|---|---|
| The single finding directly contrasts the proxy with both components of the governing outcome and explains how the proxy can pass while the outcome fails. | final.txt:1-2 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Every focused semantic requirement passes: the response grades and rejects wizard completion as evidence of reduced signup-to-successful-export time, makes measurement of the actual outcome the acceptance basis, emits the consistent blocking verdict, and stays read-only. Task shape passes, no deterministic protocol applies, and the recurring undeclared installed-skill read is recorded as a nonblocking input-fidelity failure that limits causal attribution. |
| Disposition | Accepted by the owner on 2026-09-05 as the latest qualified judgeable PASS baseline, with the undeclared installed-skill read disclosed. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | The response does not use an imperative such as “measure median time.” Its title says the rollout criterion fails because it does not measure the governing outcome, its body names time from signup and successful export, and its P1/BLOCK posture requires correction before proceeding. Requiring redundant imperative syntax would convert semantic judgment into an unstated task-format rule. |
| Scenario defects | The supplied brief and proposal isolate the proxy/outcome distinction and permit direct judgment. Runtime read isolation remains incomplete: the provider again read an installed process skill outside the fixture inventory, so the run cannot be described as fixture-only. |
| Proposed methodology changes | Preserve semantic equivalence when a blocking finding makes the required corrective property explicit without prescribing exact wording. Continue inspecting runtime instruction reads and separate observable response quality from attribution to the pinned skill. No provider configuration or skill was changed during scoring. |
