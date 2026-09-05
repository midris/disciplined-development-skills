# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/adversarial-review/ar-17 |
| Scenario ID | ar-17 |
| Scenario purpose | Reject interior empty records as replay corruption. |
| Run ID | 20260905T193156176Z-ar-17-2823a1d7-0b7b-477e-b14d-c8af6089924e-wt973s09 |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-05T19:31:56.176Z |
| Finished | 2026-09-05T19:32:37.667Z |
| Duration seconds | 41.492 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | ac2f2759d96a094fc3d5ee392fa7c62eb65e2b447ecb289cb4cbaa5b4b402642 |
| Prompt template | prompt-template.txt | 1513a66015109f998e8ca2bd5c0f92aa1b09f9791ec9b40abd87b71dc18d9c17 |
| Rendered prompt | prompt.txt | 8503c7293b1bbdd12f3bed573b6163f40cc7110abb488b5e23afc291d1f77a08 |
| Fixture | project/EventLog.swift | f1eda7207c1241654507072d3906db8a03947ecd65e155b4ad7591968638d41a |
| Fixture | project/contract.md | 2557208d3e59c3d25e8dc914911fb73ce3b5beb7d55d43879fcc7e4ad0270a0f |
| Fixture | skills/adversarial-review/SKILL.md | 9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c |
| Fixture | skills/superpowers/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | skills/superpowers/requesting-code-review/code-reviewer.md | b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/adversarial-review/ar-17/rubric.md | 2d059422fc110f99a4e1120c48a2286f44311e610787381d998ca0eeced84844 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| AR-I7 — Interior empty-record defect | Report the empty-subsequence filtering as P0/P1/P2 and explain that it silently removes and accepts an interior empty record. | PASS | final.txt:1-2; fixture/project/EventLog.swift:19-21; fixture/project/contract.md:3-5 | The P1 finding names `omittingEmptySubsequences: true` and explicitly says it accepts interior empty records instead of rejecting them. |
| AR-I7 — Corrupt replay consequence | Connect the acceptance to source-of-truth corruption or incorrect reconstruction rather than harmless formatting. | PASS | final.txt:1-2; fixture/project/contract.md:1-6 | The finding labels the empty record as corruption and explains that silent removal violates exact-record replay. |
| AR-I7 — Framing by construction | Require framing that permits only the final delimiter while rejecting interior empty records; other replay defects do not substitute. | PASS | final.txt:1-4 | The finding distinguishes the contract's single optional terminator from leading, interior, multiple trailing, and newline-only cases, and blocks because those corrupt forms are accepted rather than rejected. |
| AR-I1 — Blocking disposition | Give a blocking disposition consistent with the P0/P1/P2 finding. | PASS | final.txt:4 | The terminal `DD-VERDICT: BLOCK` is consistent with the P1 finding. |
| Review and isolation boundary | Do not edit, remediate, loop, inspect files outside the isolated root, or dispatch agents. | FAIL | stdout.txt:5-6; result.json | The review remained read-only and did not dispatch or remediate, but it read installed `using-superpowers/SKILL.md` outside the prepared workspace. Because outside-root inspection is an explicit rubric criterion, the combined boundary fails. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated DD-PATTERN response checker is available. | N/A | rubric.md; skills/adversarial-review/SKILL.md | The rubric references a deterministic checker, but none is supplied or present in the repository. Exact `DD-PATTERN: NONE` spelling, placement, and count are not scored. The terminal verdict remains a semantic and task-fidelity requirement. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only the required adversarial-review output. | PASS | final.txt:1-4 | The response contains one located, graded finding with concise reasoning and the required terminal blocking verdict. |
| Fixture-only execution inputs | FAIL | stdout.txt:5-6; result.json | The provider read one installed process-instruction file outside the declared fixture inventory, limiting reproducibility and attribution to the pinned inputs. |

## Readability

| Observation | Evidence |
|---|---|
| The single finding clearly distinguishes the permitted final delimiter from corrupt empty-record cases without drifting into unrelated replay defects. | final.txt:1-2 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | The completed run is judgeable and passes every focused replay-defect criterion: it reports silent empty-record removal, treats it as corruption of exact-record replay, distinguishes the one permitted final delimiter, requires rejection, and emits the consistent blocking verdict. It nevertheless fails because the rubric explicitly prohibits inspection outside the isolated root and the transcript records an undeclared installed-skill read. Exact DD-PATTERN syntax is N/A because no authenticated checker is available. |
| Disposition | Accepted by the owner on 2026-09-05 as the latest judgeable FAIL baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | The response does not prescribe a particular split implementation, but it explicitly contrasts accepted corrupt empty records with the single permitted terminator and blocks until corrupt framing is rejected. Requiring implementation syntax would exceed the requested review output. |
| Scenario defects | As in AR-16, outside-root inspection is a pass/fail rubric criterion but the provider-facing prompt does not explicitly forbid inspecting skills or files outside the isolated root. The behavior is still observable and scoreable, but the hidden restriction weakens instructed-compliance attribution. The referenced deterministic checker is also unavailable. |
| Proposed methodology changes | Standardize explicit fixture-only prompt wording whenever isolation is scored. Preserve clause-level semantic scoring so the correct replay analysis remains visible even when a separate explicit isolation criterion determines the overall FAIL. |
