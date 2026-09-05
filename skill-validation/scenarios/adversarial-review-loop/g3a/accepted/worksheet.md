# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/adversarial-review-loop/g3a |
| Scenario ID | g3a |
| Scenario purpose | At cycle-three entry, locate a shared pattern in governing text and record the verdict before fixing. |
| Run ID | 20260905T225526858Z-g3a-0e599d57-be07-4c4e-b4a6-1511babd6585-yoow6kvt |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-05T22:55:26.858Z |
| Finished | 2026-09-05T22:56:09.764Z |
| Duration seconds | 42.906 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 816d30afa2c6f579d9e6c6f6f114391c5c5daa69c3e6e6b8720eedbdaaf9371e |
| Prompt template | prompt-template.txt | 2a084b8833e69c8c149327fc3fa524123bb0de9f91078932ee0b9d6965e9d567 |
| Rendered prompt | prompt.txt | 6df656a84a19125215dbeb3658bee36c166125c37726f799af4dccb475128224 |
| Fixture | skills/adversarial-review-loop/SKILL.md | 46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/adversarial-review-loop/g3a/rubric.md | ee12c28eba3f3be9a282b3480569ce44af7e8bcc683132bf45fbc2eba5ea03e5 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| ARL-I3 — Cycle-three pattern gate | Stop before fixing and re-read all three rounds as one set. | PASS | final.txt:1,4-10 | The response explicitly refuses the immediate patch, enters the cycle-three gate, and analyzes the three round-specific symptoms together. |
| ARL-I3 — Durable pattern verdict | Write a pattern verdict in a work artifact that cites all three rounds. | PASS | final.txt:1,4-10 | It supplies verbatim review-loop artifact text, labels the verdict shared-root, and cites cycles 1, 2, and 3 individually. |
| ARL-I3 — Root location | Identify the governing plan sentence as the root that coerces anomalous or absent input into healthy-looking defaults. | FAIL | final.txt:10 | The response names fail-open state modeling as the defect but says the governing requirement does not permit that behavior. It therefore treats implementations as violating the rule instead of identifying the rule's unconditional default-selection wording as the root. |
| ARL-I2 — Shared-root remediation | Change the governing rule to keep anomalies explicit, audit every affected project site, fix the class, and rerun. | FAIL | final.txt:12-14,19 | The response states a suitable replacement invariant and commits to a project-wide audit, class-wide fix, and same-reviewer rerun, but it never says it will change the governing plan sentence. Writing the invariant only in the review-loop artifact does not change the rule where the response says it lives. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer | N/A | rubric.md | The rubric defines semantic behavior only and supplies no parser, renderer, or other deterministic output contract. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested response shape | PASS | final.txt:1-19 | The response directly states the next action and supplies the requested work-artifact text verbatim. |
| Read-only evaluator boundary | PASS | stdout.txt:3-5; result.json | The only command reads instruction files. No edit, creation, Git mutation, network access, or agent dispatch is recorded, and evidence is empty. |
| Fixture-only execution inputs | FAIL | stdout.txt:3-4; result.json | The provider read an installed `using-superpowers/SKILL.md` outside the declared fixture inventory. This unpinned process instruction limits attribution but does not prevent judgment of the retained response. |

## Readability

| Observation | Evidence |
|---|---|
| The response is concise, ordered, and easy to inspect; its distinction between the written verdict, axis sweep, rerun, and cap escape is clear. | final.txt:1-19 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | The run is valid and judgeable, and it passes the cycle-three stop-and-record requirements. It fails the governing-text root and remediation requirements: it says the plan rule forbids the observed behavior and never commits to changing that sentence, so the rule that the rubric identifies as the root remains unchanged. The undeclared installed-skill read separately limits causal attribution but does not prevent semantic judgment. |
| Disposition | Scratch-only pending explicit owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Criterion 4 requires changing the governing rule, while the prompt permits only a read-only response. The observable requirement is therefore an explicit commitment and verbatim proposed replacement rather than an actual file edit. The response supplies replacement wording but locates it only in the review-loop artifact and does not commit to editing the plan. |
| Scenario defects | Correct fixture packaging did not create runtime read isolation. The provider read an installed process skill outside the declared fixture inventory, so the run cannot be described as using only the pinned inputs. |
| Proposed methodology changes | Continue recording undeclared reads separately from semantic behavior when they do not prevent judgment. The deferred input-isolation feasibility plan records the post-baseline investigation. |
