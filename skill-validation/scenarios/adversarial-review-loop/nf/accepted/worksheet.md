# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/adversarial-review-loop/nf |
| Scenario ID | nf |
| Scenario purpose | Attack a visible below-cap error-contract invariant across its complete axis before re-review. |
| Run ID | 20260905T223439576Z-nf-870eda20-7b8e-43f9-b041-9bb69c5327c7-_qksfatg |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-05T22:34:39.576Z |
| Finished | 2026-09-05T22:35:09.684Z |
| Duration seconds | 30.109 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 1199be6f0c2a80f5c2459805ea2b49dfe00cc4e1696021d71841cd3d460dab25 |
| Prompt template | prompt-template.txt | 088ecef309a869161c73eaa5eb0c9ed657e2b21b790b564d02e677eaccff7e02 |
| Rendered prompt | prompt.txt | 94f04a2e3ab21801e24ab556d9e8ce279019b28504fde1becb503bb686d766b6 |
| Fixture | skills/adversarial-review-loop/SKILL.md | 46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/adversarial-review-loop/nf/rubric.md | 86756fd50bf95913fcab2e6234d71ec5189f3541bc20488461c072f2e4a183c8 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| ARL-I2 — Shared-root recognition | Recognize one source-of-truth failure-path or error-contract invariant requiring typed, recoverable errors rather than crashes or silent acceptance. | PASS | final.txt:1,11 | The response explicitly joins the crash and silent-discard findings under one typed, recoverable error contract. |
| ARL-I2 — Complete axis scope | Name the axis and audit every project site that could violate it, including uncited sites, rather than fixing only `replay`. | PASS | final.txt:5-6 | It records the pattern and performs a project-wide higher-order sweep across open/create, write/sync, read/replay, parsing, malformed and partial records, blank records, catch/skip paths, and force-crash behavior. |
| ARL-I2 / ARL-I1 — Root remediation before rerun | Fix the whole axis in one pass and then re-run the same reviewer. | PASS | final.txt:7-9 | It fixes every violation, tests the enumerated paths, and makes the same-reviewer rerun conditional on the full axis sweep passing. |
| ARL-I2 — Early below-cap root attack | Treat the findings as an early root attack rather than a cold-read escape or another isolated fix. | PASS | final.txt:1,5-11 | It stops an immediate rerun, performs a higher-order sweep, and explicitly rejects fixing only `replay` because that would grind through another symptom. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer | N/A | rubric.md | The rubric defines semantic behavior only and supplies no parser, renderer, or other deterministic output contract. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested response shape | PASS | final.txt:1-11 | The response directly states the decision, concrete ordered actions, and reasoning. |
| Read-only evaluator boundary | PASS | stdout.txt:3-4; result.json | The only command reads instruction files. No edit, creation, Git mutation, network access, or agent dispatch is recorded, and evidence is empty. |
| Fixture-only execution inputs | FAIL | stdout.txt:3-4; result.json | The provider read an installed `using-superpowers/SKILL.md` outside the declared fixture inventory. This unpinned process instruction limits attribution but does not prevent judgment of the retained response. |

## Readability

| Observation | Evidence |
|---|---|
| The shared invariant, project-wide audit surface, remediation order, and reason not to fix only `replay` are explicit and easy to inspect. | final.txt:1-11 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | All four focused semantic criteria pass. The response identifies the shared typed-error invariant, audits every relevant EventLog path project-wide, fixes and tests the whole axis before the same-reviewer rerun, and treats the below-cap recurrence as a root attack rather than an isolated grind or cold-read escape. The undeclared installed-skill read separately limits causal attribution but does not prevent semantic judgment. |
| Disposition | Scratch-only pending explicit owner acceptance. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None material to the verdict. In this focused NF scenario, “project-wide” means every project site on the EventLog error-contract axis; the subsequent PW scenario separately pressures extension to other persistence components. |
| Scenario defects | Correct fixture packaging did not create runtime read isolation. The provider read an installed process skill outside the declared fixture inventory, so the run cannot be described as using only the pinned inputs. |
| Proposed methodology changes | Continue recording undeclared reads separately from semantic behavior when they do not prevent judgment. The deferred input-isolation feasibility plan now records the post-baseline investigation. |
