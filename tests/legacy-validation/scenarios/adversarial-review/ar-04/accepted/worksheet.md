# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/adversarial-review/ar-04 |
| Scenario ID | ar-04 |
| Scenario purpose | Map the holistic baseline and additive specialized lenses by artifact kind. |
| Run ID | 20260905T132755442Z-ar-04-75e551f9-cf29-4fa9-8ff2-8e96bdb71504-eandeutw |
| Provider | codex |
| Provider CLI version | Unknown — no contemporaneous CLI-version evidence found in the accepted record or matching retained scratch logs. |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-05T13:27:55.442Z |
| Finished | 2026-09-05T13:28:19.892Z |
| Duration seconds | 24.450 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 5f8e630907ea1e20663cdecbdfecda4926096ed5d2a5f1c32b838c112ba801c5 |
| Prompt template | prompt-template.txt | 525112073efaf10c6af7f6eb9fedfe3ce0c6e5c56ba443c27c73244e3b13a016 |
| Rendered prompt | prompt.txt | 700f0473b9a955bc2b7f3404226de533d11bc8cc4fa36306c708fc8fe238260c |
| Fixture | context/artifacts.md | 8b924afe56754ad28ae0fc04e265d8823d73826bea1732514f41e321b5402e1b |
| Fixture | skills/adversarial-review/SKILL.md | 9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c |
| Fixture | skills/superpowers/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | skills/superpowers/requesting-code-review/code-reviewer.md | b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/adversarial-review/ar-04/rubric.md | 3eb7b7a502cb47c88af3ecdd9741cc85ded600ba35d47646ea5460f0387210a2 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Always-on baseline | Apply the whole-artifact review baseline to every artifact even when specialized lenses are selected. | PASS | final.txt:1,3-8 | The opening sentence applies a deep whole-repository adversarial review to all artifacts and enumerates the baseline duties. The table then adds lenses without replacing that global baseline. |
| Universal consistency | Account for the consistency lens on every artifact. | PASS | final.txt:5-8 | Each of the four artifact rows explicitly includes consistency. |
| Runbook lenses | Add executability to the runbook and no inapplicable durability lens. | PASS | final.txt:5 | The runbook row selects consistency and zero-context executability, and explicitly excludes durability. |
| Skill lenses | Add executability and skill-authoring to the skill. | PASS | final.txt:6 | The skill row selects consistency, executability, and skill-authoring and names the skill-authoring checks. |
| Durable-log lenses | Add durability to the source-of-truth log without unrelated conditional lenses. | PASS | final.txt:7 | The durable-log row selects consistency and durability, expands both mutation and replay checklists, and excludes executability and skill-authoring. |
| Limiter lenses | Add no conditional lens to the pure in-memory limiter. | PASS | final.txt:8 | The limiter receives consistency and the always-on baseline while explicitly excluding executability, skill-authoring, and durability. |
| Mapping-only boundary | Do not edit, perform the reviews, or dispatch agents. | PASS | final.txt:1-8; result.json | The response maps future review work without issuing findings or claiming review execution. Supplied fixture hashes remain unchanged and the evidence directory is empty. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The mapping is manually interpreted, and the rubric explicitly accepts different representations, field names, order, and explanation depth. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Concisely map required review work and specialized lenses for every supplied artifact. | PASS | final.txt:1-8 | The response covers all four named artifacts in a compact table, preceded by one shared-baseline sentence, without performing the reviews. |

## Readability

| Observation | Evidence |
|---|---|
| The shared opening avoids repeating the baseline in every row, while explicit inclusion and exclusion statements make each conditional-lens decision auditable. | final.txt:1-8 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Every focused requirement passes. The response applies the always-on baseline globally, includes consistency for all four artifacts, adds exactly the semantically applicable executability, skill-authoring, and durability lenses, leaves the pure in-memory limiter without a conditional lens, and stays within the mapping-only boundary. Task fidelity passes and no deterministic protocol applies. |
| Disposition | Accepted by the owner on 2026-09-05 as the latest judgeable `PASS` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | The runbook and skill rows additionally mention `concise-writing`. That is supporting review work directed by the supplied skill for prose, not a conflicting specialized lens, and does not narrow or replace the required baseline. |
| Scenario defects | None observed. The artifact descriptions isolate the applicability predicates cleanly, and the rubric permits equivalent representations without weakening the semantic lens mapping. |
| Proposed methodology changes | Permit one global statement to satisfy a universal baseline when each subsequent artifact row is clearly within its scope; do not require repetitive per-row restatement unless scope becomes ambiguous. |
