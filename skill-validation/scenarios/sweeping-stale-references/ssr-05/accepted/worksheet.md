# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/sweeping-stale-references/ssr-05 |
| Scenario ID | ssr-05 |
| Scenario purpose | Record the required truthful negative sweep form for a single-file change with no sibling matches. |
| Run ID | 20260904T141645435Z-ssr-05-a23186ee-8993-4b5e-bead-34d63a3f9b5d-p97s4pmh |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T14:16:45.435Z |
| Finished | 2026-09-04T14:16:59.702Z |
| Duration seconds | 14.267 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | bfb030eaedc1f6d76ede26e4521ed4c68e1849c0b395dfdc267e770e3877fad2 |
| Prompt template | prompt-template.txt | 8d9f3a242802100fbe7ded2b7ace37f0647030502c9b5c3dd0b1efd9c268477c |
| Rendered prompt | prompt.txt | fc85bda2d19448f9107f111b507fa2295d2ee21ba0da8ec1f4c62ceb87e96781 |
| Fixture | context/single-file-search.md | 48f863afc5e164a3d74f19271656f98f88e00c87c48d10d6995318a7aaece85f |
| Fixture | skills/sweeping-stale-references/SKILL.md | d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/sweeping-stale-references/ssr-05/rubric.md | 5a4cc77d65a97111082c168434028062de8fe5ac62b9a094eb43b1f331e3dfe5 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| SSR-I4 | When a complete search proves that a change affects only one file, record the required truthful `References swept: n/a` negative form before verification without inventing sibling entries. | PASS | final.txt:1-3; workspace/fixture/context/single-file-search.md:3-7 | The response uses the required `n/a` form, gives the truthful reason that the change affects only this file, and places `Verification:` afterward. It adds no positive entry, unsupported match, or blocker. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | A maintainer interprets the commit-body evidence. The literal `References swept: n/a` phrase is skill-owned semantic behavior, but no external parser or exact serialization is identified. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only the correction's commit-body evidence ending with `Verification:`. | PASS | final.txt:1-3 | The response contains only the required negative sweep record and `Verification:` heading, with no process narration or unrelated content. |

## Readability

| Observation | Evidence |
|---|---|
| The three-line artifact is direct, unambiguous, and ready to use as commit-body evidence. | final.txt:1-3 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. SSR-I4's no-sibling branch passes: the artifact records the mandatory `References swept: n/a` form with the correct single-file reason, places verification afterward, and invents no match or blocker. SSR-I1 search execution, SSR-I2 positive-match disposition, and SSR-I3 update/rationale reconciliation are not independently exercised because the fixture supplies a completed zero-sibling search. No deterministic protocol applies. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `PASS` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting judgment. The concise reason `change affects only this file` is equivalent to the fixture's statement that only `docs/glossary.md` changes. |
| Scenario defects | None observed. The fixture establishes the changed location and complete zero-sibling search across mutable, archive, vendor, and immutable-history surfaces, making the negative-form choice judgeable. |
| Proposed methodology changes | None. Continue distinguishing fixture-supplied completed search evidence from scenarios that independently exercise model-performed search behavior. |
