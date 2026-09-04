# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/lean-plan-writing/lp-03 |
| Scenario ID | lp-03 |
| Scenario purpose | Permit exactly one bounded illustrative snippet when prose alone cannot specify an exact four-line artifact. |
| Run ID | 20260904T200833730Z-lp-03-03d328ac-4aeb-43b0-b733-6145b02ae9b0-_hkyybmp |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T20:08:33.730Z |
| Finished | 2026-09-04T20:08:58.564Z |
| Duration seconds | 24.834 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 9fa102fd8af32c71953b772d1c40b737ba785470ca71c2374aa2406cd09c9933 |
| Prompt template | prompt-template.txt | 41a94175c01f78325bce620c6a30ee6f600ed8a8ebd6fce051710cdafc2e00e9 |
| Rendered prompt | prompt.txt | 6f87e372a0bf9d7e0baa01d75a1ca918ffdb1061df2610184bd8ad6aeb9bf132 |
| Fixture | skills/lean-plan-writing/SKILL.md | 6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac |
| Fixture | skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/lean-plan-writing/lp-03/rubric.md | 8e9f86e8532792799aeb94c0ad258f61f0692618dc07436f79c43017469714af |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| LP-I1 | Keep prose as the contract except where a short illustrative snippet is genuinely necessary; do not include implementation or test bodies. | PASS | final.txt:1-12 | The response uses prose for creation and verification requirements and contains no implementation or test body. Its sole snippet is the exact artifact shape whose line breaks, order, spelling, and literal braces cannot be specified as reliably without showing it. |
| LP-I2 | State the artifact's concrete requirements and verification obligations precisely enough to implement without silently assumed file-format behavior. | PASS | final.txt:1-3,12 | The step names the output file and pins byte length, encoding, BOM absence, line endings, order, literal braces, final newline, complete-content comparison, and explicit negative byte checks. |
| LP-I3 | Use at most one five-line illustrative snippet only when needed to resolve irreducible ambiguity, and make the adjacent test contract exact. | PASS | final.txt:3-12 | There is exactly one four-line artifact block. Removing it would make the contractual shape less direct; it is within the five-line exception and the adjacent prose requires byte-for-byte verification of the complete expected sequence. |

## Composition-owner behavior

| Owner | Criterion | Verdict | Evidence | Notes |
|---|---|---|---|---|
| superpowers:writing-plans | Preserve an actionable checkbox step with a concrete file, complete requirements, and explicit verification while honoring the prompt's one-step boundary. | PASS | final.txt:1-12 | The output is one checkbox plan step that names the file, states the complete creation contract, and specifies how verification must prove it. Full-plan headers, branch structure, and commit cadence are outside the requested fragment. |
| Composition-owner verdict | Retain useful upstream action and verification structure while allowing lean-plan-writing's bounded exact-shape exception. | PASS | final.txt:1-12 | The step remains directly executable as a plan instruction without expanding into implementation code or a full plan scaffold. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Preserve the exact four-line artifact bytes: `TYPE={type}`, `VERSION={version}`, `CREATED={iso8601}`, and `PAYLOAD={relative_path}`, encoded as UTF-8 without BOM, separated by LF, with exactly one final LF. | PASS | final.txt:3-12 | Mechanical extraction of the sole fenced block equals the required 72-byte sequence exactly; it contains no BOM or carriage-return byte and ends in one, not two, LF bytes. The plan also tells the implementer to assert complete contents and each byte-level boundary. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only one implementation-plan step, include exactly one four-line artifact block, require byte-for-byte verification, and avoid placeholders or fixture-repeating commands. | PASS | final.txt:1-12 | The response is one checkbox step with one exact four-line block and no extra plan section, fixture path, verification command, TODO, TBD, or deferred content. The brace tokens are required literal artifact bytes, not unresolved plan placeholders. |

## Readability

| Observation | Evidence |
|---|---|
| The twelve-line response is compact, and the exact block plus adjacent byte checks make the unusual format contract easy to audit. | final.txt:1-12 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. LP-I1 through LP-I3 and task fidelity pass: the response uses prose for the plan contract, limits itself to the one necessary four-line illustration, reproduces the artifact bytes exactly, and requires a complete byte comparison covering encoding and newline invariants. The separate composition-owner ledger passes for the requested one-step fragment. The deterministic byte contract passes mechanical verification. LP-I4 merge-boundary polarity is not independently pressured. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `PASS` baseline, with a separate composition-owner `PASS`. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None affecting judgment. The rubric's generic prohibition on placeholders does not conflict with `{type}`, `{version}`, `{iso8601}`, and `{relative_path}` because the prompt explicitly requires those braces and tokens to be preserved literally as artifact bytes. |
| Scenario defects | None affecting execution or judgment. The README still names the source validation document by its former pre-archive path; the prompt, rubric, fixture hashes, and catalog assertions remain intact. This catalog-wide provenance wording should be cleaned up consistently rather than altering only this scenario during baseline scoring. |
| Proposed methodology changes | Continue mechanically checking exact artifact blocks whenever the rubric specifies a byte contract, and keep the upstream composition-owner judgment scoped to the plan fragment the prompt actually requests. |
