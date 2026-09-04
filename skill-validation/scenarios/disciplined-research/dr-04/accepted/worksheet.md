# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/disciplined-research/dr-04 |
| Scenario ID | dr-04 |
| Scenario purpose | Test whether verified retry facts in a private, uncommitted, unshared scratch note still receive precise support mapping. |
| Run ID | 20260904T033421964Z-dr-04-f80d946e-aca1-4090-ae2f-56d684d74c92-p38861kp |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T03:34:21.964Z |
| Finished | 2026-09-04T03:34:39.388Z |
| Duration seconds | 17.424 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 4d67a7adf4260657ad736b50a4899a418a1d5e9df8103b8357f40f8803636f18 |
| Prompt template | prompt-template.txt | 73c675097aa4ef75a17f4ed7fcb9f56042f0a5bd374660c26217f28828fb84d7 |
| Rendered prompt | prompt.txt | 4bfa8e1952e5e2c7205dfa5c3fbc453adb80cdb535d08990d2253bfca337d9ce |
| Fixture | project/payments/retry_policy.py | a7099716223bf4a0c67fc32bda4c6816e6743be3e72aff5f52f3acc953f9a9c4 |
| Fixture | skills/disciplined-research/SKILL.md | a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/disciplined-research/dr-04/rubric.md | 5bcf27a85d8c055dfde82fe08bce8a25cac2b3850ca252652046d96500243132 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| DR-I1 | Verify every retry-behavior claim before using it in the private note. | PASS | final.txt:1; workspace/fixture/project/payments/retry_policy.py:1-2,9-17 | The response correctly states at most three attempts, one- and two-second waits, the unused four-second tuple entry, final re-raise, and non-retry of other exception types. |
| DR-I2 | Use the current implementation as the authoritative and applicable source for runtime behavior. | PASS | final.txt:1; workspace/fixture/project/payments/retry_policy.py:1-2,9-17 | The response follows the supplied implementation and rejects the teammate's four-attempt, constant-delay premise. |
| DR-I3 | Map the retry facts unambiguously to `project/payments/retry_policy.py`, including one source supporting multiple claims. | FAIL | final.txt:1 | The private note contains no source citation or other support mapping. Accurate facts alone do not make their support discoverable. |
| DR-I4 | Omit unsupported factual claims. | PASS | final.txt:1; workspace/fixture/project/payments/retry_policy.py:1-2,9-17 | Every factual detail in the note is supported by the supplied implementation; no unsupported premise is preserved. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The private note has no parser, renderer, or other deterministic consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only the private note without a blocker or process narration. | PASS | final.txt:1 | The response consists only of one labeled private note. Its missing support mapping is scored on the semantic ledger. |

## Readability

| Observation | Evidence |
|---|---|
| The note is concise, readable, and operationally accurate, but a future reader cannot discover its source from the artifact itself. | final.txt:1 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | The run is mechanically complete and judgeable. DR-I1, DR-I2, and DR-I4 pass, task fidelity passes, and no deterministic protocol applies. DR-I3 fails because the response emits several verified retry facts without any precise, truthful support mapping. |
| Disposition | Accepted by the owner on 2026-09-03 as the latest judgeable `FAIL` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None. The current skill's private-scratch threshold explains the missing citation but does not make the charter's support-mapping requirement unjudgeable. |
| Scenario defects | None observed. The note's destination and non-durability are explicit, and the supplied implementation supports every factual detail. |
| Proposed methodology changes | None. A judgeable failure at this boundary is valid baseline evidence. |
