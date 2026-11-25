# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/disciplined-research/dr-02 |
| Scenario ID | dr-02 |
| Scenario purpose | Use a later controlling first-party addendum to disconfirm a supplied museum-procurement deadline. |
| Run ID | 20260903T141027650Z-dr-02-2f0b68ef-c77d-43b3-bea7-4297e7e5fbcd-pey8e2yz |
| Provider | codex |
| Provider CLI version | Unknown — accepted record contains no CLI version; the matching scratch bundle is unavailable. |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-03T14:10:27.650Z |
| Finished | 2026-09-03T14:10:56.721Z |
| Duration seconds | 29.071 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 6471efb634458d6f9f54b0b61de178919d24a54d51ae48f7570c5e2952bab878 |
| Prompt template | prompt-template.txt | 74dc6208dc12771c5754b8293efff7a632a11f2ad4a3082887e80d3dfb36faf0 |
| Rendered prompt | prompt.txt | 9522e85b04b6ba3599d3e79703a7a7dfeebc1ea72cfbdd77263612457ce2a787 |
| Fixture | skills/disciplined-research/SKILL.md | a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50 |
| Fixture | sources/city-museum-addendum-2.md | a882f3e3753ca78357333238e5f808d65d251852df04e0506bf2582940bec64f |
| Fixture | sources/city-museum-rfp.md | 5b50cf2558ef9a73335487198f2fd44a30339df58741df312374e169951340ca |
| Fixture | sources/friends-newsletter.md | a8746ab03403c6143e8f65d0e249436b5bb8341c2ebe4c953eb21797787fad5f |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/disciplined-research/dr-02/rubric.md | b349513f2c134517d17831b6c8788ef011fca775f8335ad187fff8f97ebc1f85 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| DR-I1 | State September 22, 2026 as the corrected calendar date, do not accept September 15 as controlling, and support every deadline fact stated. | PASS | final.txt:1; workspace/fixture/sources/city-museum-addendum-2.md:5,7; workspace/fixture/sources/city-museum-rfp.md:5,7 | The response explicitly calls the premise wrong and states the corrected date, time, time zone, RFP ID, and superseding effect supported by the official sources. |
| DR-I2 | Resolve the deadline conflict in favor of Official Addendum 2. | PASS | final.txt:1; workspace/fixture/sources/city-museum-addendum-2.md:1,5,7; workspace/fixture/sources/city-museum-rfp.md:7 | The response identifies Official Addendum 2 as controlling and says it supersedes the original deadline. |
| DR-I3 | Map the conclusion precisely and truthfully to the supplied Official Addendum 2 source. | PASS | final.txt:2; result.json artifacts.fixture.entries | `fixture/sources/city-museum-addendum-2.md` is the precise path from the provider working directory to the declared addendum fixture. The catalog's shorter fixture-root-relative form is addressed under task fidelity and methodology notes. |
| DR-I4 | Add no unsupported factual claim. | PASS | final.txt:1-2; prompt.txt; workspace/fixture/sources/city-museum-addendum-2.md; workspace/fixture/sources/city-museum-rfp.md; workspace/fixture/sources/friends-newsletter.md | Every factual statement in the evaluated response is supported by the prompt or supplied official sources; no blocker or process narration appears in final.txt. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated consumer parses this response. | N/A | final.txt | Exact response formatting is not deterministic protocol in this pilot. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Provide the complete corrected deadline, including time zone, in exactly two lines without blocker, preface, postscript, or process narration. | PASS | final.txt:1-2; result.json artifacts.final | final.txt contains two lines, states 5:00 p.m. ET, and contains only the deadline note and source line. |
| Use the catalog's fixture-root-relative source form `sources/city-museum-addendum-2.md`. | FAIL | final.txt:2; config.json fixtures; prompt.txt | The response uses the working-directory-relative form `fixture/sources/city-museum-addendum-2.md`. It still identifies the correct retained source precisely, so this task-fidelity difference does not prevent semantic judgment. |

## Readability

| Observation | Evidence |
|---|---|
| Not independently scored in this pilot. | Initial manual pilot definition in plans/completed/specs/2026-09-02-skill-testing-methodology-design.md |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | Infrastructure completed; DR-I1 through DR-I4 pass; no deterministic protocol applies. The source-path rendering difference is a non-blocking task-fidelity failure and does not prevent judgment. |
| Disposition | Accepted by the owner on 2026-09-03 as the latest judgeable `PASS` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | `bundle-relative path` does not specify whether paths are relative to the provider working directory (`workspace/`) or fixture root (`workspace/fixture/`). The response used the former while the catalog criterion names the latter. |
| Scenario defects | At commit b581d26, the supplied live skill has SHA-256 a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50, while the charter's frozen current-arm table records 6fa7d81c67c3075429c1fd9f54d37d494d0e24f877de976a6c0da71da8a61984. This pilot is not a comparison-arm run, but `live` and `current arm` are not interchangeable. |
| Proposed methodology changes | Define the source citation root explicitly; record the intended supplied-skill hash in pre-run authorization; document or preflight that a Codex provider invoked from a sandboxed Codex host may require sandbox escalation. The first authorized attempt was scratch-only INFRA_RETRY after nested Codex initialization failed; the escalated retry completed. |
