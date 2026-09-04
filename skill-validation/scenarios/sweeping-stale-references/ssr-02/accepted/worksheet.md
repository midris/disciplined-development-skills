# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/sweeping-stale-references/ssr-02 |
| Scenario ID | ssr-02 |
| Scenario purpose | Treat one reviewer hit as a sample and reconcile a complete cross-category search inventory. |
| Run ID | 20260904T132646155Z-ssr-02-b173ecf7-6232-4eae-a224-8b68270c31a7-zdx27w1t |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T13:26:46.155Z |
| Finished | 2026-09-04T13:27:12.212Z |
| Duration seconds | 26.057 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 32fcb0af0c6bb3543468093c963d2ece0a494f6eb25b268dd0a3aaa364ca468b |
| Prompt template | prompt-template.txt | a6113dc283c5dd61c79698f96d4d0a5a09a327619c64969e4bd25178975be93d |
| Rendered prompt | prompt.txt | 9c311ec4fdbcdfdafe36a93dd8855145bda576b957079d8a60dd4ffa297bab29 |
| Fixture | context/match-inventory.md | 43b3f8819da7b85ccff406f64a4d0c438ebc4cea35e5628ac4e0919a64e7dcf6 |
| Fixture | skills/sweeping-stale-references/SKILL.md | d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/sweeping-stale-references/ssr-02/rubric.md | 85e031214c456eab383b00e8a18d16e384d15902ace99491d2acbf2785a739bb |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| SSR-I1 | Reject the reported README hit and IDE rename as exhaustive, and use the supplied complete search across old/replacement context, prose synonym, and all applicable mutable repository surfaces. | PASS | final.txt:1,4-17; workspace/fixture/context/match-inventory.md:3-20,25-26 | The disposition explicitly says the IDE claim is insufficient and that all 13 mutable-tree matches require accounting. The artifact covers code, a code comment, docs, tests/fixtures, config, scripts, CI, build, archive, and vendor paths rather than stopping at the reported README hit. |
| SSR-I2 | Give every mutable match one truthful disposition while excluding immutable history from the rewrite inventory. | PASS | final.txt:1,7-17; workspace/fixture/context/match-inventory.md:10-24 | All 13 mutable matches receive the supplied outcome: 10 update, one intentionally stale with the completed-plan reason, and two false positives with vendor-scope and unrelated-HTTP reasons. The three immutable-history hits are explicitly kept out of scope and are not added to `References swept:`. |
| SSR-I3 | Reconcile all required updates together in one match-complete branch artifact. | PASS | final.txt:1,4-17 | The response treats the 13-match inventory as one complete unit and includes all ten update matches in the same commit-body sweep record. This scenario does not independently exercise rationale preservation. |
| SSR-I4 | Provide durable sweep evidence with precise paths, locations, outcomes, per-group counts, and totals that reconcile to the independent inventory. | PASS | final.txt:4-19; workspace/fixture/context/match-inventory.md:5-20 | The 11 path/outcome rows preserve every supplied location and sum to 13 matches: 10 update, one intentionally stale, and two false positives. `References swept:` precedes `Verification:` and no unsupported match appears. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The commit body is interpreted by a maintainer. The rubric requires semantic completeness and section ordering but defines no parser, schema, or exact byte-level protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| State the inventory disposition and return only match-complete commit-body evidence ending with `Verification:`, without unsupported blockers or narration. | PASS | final.txt:1-20 | The opening sentence supplies the requested disposition; the remainder is the requested commit-body evidence. It adds no blocker or unrelated narration. A closing Markdown fence follows the `Verification:` line syntactically, but it adds no content and does not obscure the requested ending. |

## Readability

| Observation | Evidence |
|---|---|
| The artifact is concise, easy to scan, and fully reconciled. The unnecessary fenced block would be mildly awkward if pasted directly into a commit body. | final.txt:1-20 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. SSR-I1 through SSR-I4 pass for the behavior exercised here: it rejects the reviewer hit and IDE rename as exhaustive, accounts truthfully for all 13 mutable-tree matches across every supplied category, excludes the three immutable-history hits, and reconciles every location and outcome in one ordered sweep artifact. The Markdown fence is a non-blocking presentation observation. No deterministic protocol applies. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `PASS` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting semantic judgment. The response's closing Markdown fence technically follows the `Verification:` text, but it is syntax rather than additional artifact content and does not violate the rubric's required ordering. |
| Scenario defects | None observed. The completed inventory independently fixes the exact paths, locations, classifications, counts, surface categories, and immutable-history exclusions, making the response mechanically judgeable without repository mutation. |
| Proposed methodology changes | None. Preserve the distinction between semantic correctness and non-material formatting surplus when no authenticated deterministic consumer exists. |
