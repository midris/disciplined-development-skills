# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/sweeping-stale-references/ssr-03 |
| Scenario ID | ssr-03 |
| Scenario purpose | Group a large sweep only by path and outcome while retaining precise locations, counts, and complete evidence. |
| Run ID | 20260904T134008797Z-ssr-03-17f0da0a-11fb-4da9-ad82-75e5149e05d3-exs9_mb7 |
| Provider | codex |
| Provider CLI version | Unknown — no contemporaneous CLI-version evidence found in the accepted record or matching retained scratch logs. |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T13:40:08.797Z |
| Finished | 2026-09-04T13:40:30.857Z |
| Duration seconds | 22.06 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | fb6e71ef0af8140282ac40d1fa6e72aff7d6aa4a094e7bb754aad58709e58165 |
| Prompt template | prompt-template.txt | 5e1a1fa2f60db6cf2aeceaed4a85b869366e4e6a8b20cfe8bf0e4398de46f39e |
| Rendered prompt | prompt.txt | 21a819e070e459fa9d25167aa20020bd01034dd877a9ff2f354e8a163f14eb05 |
| Fixture | context/grouping-inventory.md | 0916a116c5d0d98089b000a65bcfe1b73ec26951b4659b6279e7f6df0c1e1b02 |
| Fixture | skills/sweeping-stale-references/SKILL.md | d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/sweeping-stale-references/ssr-03/rubric.md | 803b8d4133d4b833f1c1c805ec82ba859c6aa9989c68038c3d10f1d1b178325d |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| SSR-I2 | Preserve every supplied disposition and its reason without grouping matches across different paths or outcomes. | PASS | final.txt:1-11; workspace/fixture/context/grouping-inventory.md:8-20 | The response retains all six update groups, both intentionally stale groups with their distinct historical reasons, and both false-positive groups with their distinct HTTP reasons. Every group stays path- and outcome-specific. |
| SSR-I4 | Preserve all precise locations and path counts and reconcile the 10 groups to 126 total matches: 80 update, 40 intentionally stale, and 6 false positive. | PASS | final.txt:1-16; workspace/fixture/context/grouping-inventory.md:3-20 | All ten paths, line ranges, outcomes, and per-path counts match the fixture exactly. The six update groups sum to 80, the two intentionally stale groups to 40, and the two false-positive groups to 6; the verification reports the reconciled total of 126. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The grouped commit-body artifact is interpreted by a maintainer. The rubric fixes semantic group boundaries, locations, counts, and ordering but defines no parser or exact serialization. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only the grouped sweep artifact followed by `Verification:`, and explain that the normal 72-line preference applies after grouping without sacrificing evidence. | PASS | final.txt:1-16 | The response contains only `References swept:` and its verification. It states the correct ordering rule and truthfully observes that this 16-line grouped artifact remains below 72 lines, so no exception or omitted evidence is needed. |

## Readability

| Observation | Evidence |
|---|---|
| The compact one-row-per-path presentation is easy to audit and preserves every required detail. | final.txt:1-16 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. SSR-I2 and SSR-I4 pass: every supplied path/outcome group, line range, reason, and count is preserved, and the subtotals reconcile exactly to 126. The artifact groups before applying the normal body-size preference and remains below 72 lines without dropping correctness evidence. SSR-I1 search execution and SSR-I3 update/rationale reconciliation are not independently exercised by this completed-inventory scenario. No deterministic protocol applies. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `PASS` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting judgment. The fixture states that every match within each path shares one outcome, so one row per supplied path is the correct grouping granularity. |
| Scenario defects | None observed. The fixture independently supplies exact paths, line ranges, outcomes, reasons, and counts, making grouping and arithmetic mechanically judgeable. |
| Proposed methodology changes | None. Continue recording which charter invariants a focused scenario actually exercises instead of treating every scenario as full-charter coverage. |
