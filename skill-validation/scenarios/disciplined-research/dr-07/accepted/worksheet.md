# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/disciplined-research/dr-07 |
| Scenario ID | dr-07 |
| Scenario purpose | Test whether the skill corrects a conversational premise, derives the supported fifteen-minute result, and discloses its source. |
| Run ID | 20260904T045211656Z-dr-07-0b56b945-e5e4-433b-8cfa-76241ee70dc6-8oomenyd |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T04:52:11.656Z |
| Finished | 2026-09-04T04:52:26.821Z |
| Duration seconds | 15.164 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 84e34029ca150bca0bba10bcc1a02172a507721b50c1dc9c2ddca6b9a3de58d2 |
| Prompt template | prompt-template.txt | 0a73303a85788bf3a23942d6be800a5f6162bc45526e14d05c7253c1482f6b0f |
| Rendered prompt | prompt.txt | 0ce5b0b0ba1ae37a7874496a15d4e8d302eec8a9660ca4eb7c7dfa25cba915c2 |
| Fixture | skills/disciplined-research/SKILL.md | a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50 |
| Fixture | sources/north-annex-hours.md | 876d614b194ace2d807a947223565f3fdc9a597be45c6c1b753a9252a65e45da |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/disciplined-research/dr-07/rubric.md | a29cde034d63ecfc229e3821435e92dfe6c33dc348f4b3cef03fb151db4a3bd3 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| DR-I1 | Verify the 5:45 p.m. closing time and derive the fifteen-minute interval before stating either claim. | PASS | final.txt:1; prompt.txt; workspace/fixture/sources/north-annex-hours.md:3,5 | The response states the verified closing time and correctly subtracts the prompted 5:30 p.m. arrival to obtain fifteen minutes. |
| DR-I2 | Use the effective official visitor schedule as the authoritative and applicable source instead of accepting the conversational 6:00 p.m. premise. | PASS | final.txt:1; workspace/fixture/sources/north-annex-hours.md:1,3,5 | The response explicitly corrects the premise and relies on the supplied official schedule. |
| DR-I3 | Map both the 5:45 p.m. closing time and the resulting fifteen-minute interval unambiguously to `sources/north-annex-hours.md`. | PASS | final.txt:1; result.json artifacts.fixture.entries | The source link follows both claims and targets the exact retained `sources/north-annex-hours.md` fixture. Its absolute scratch prefix is addressed in the methodology notes. |
| DR-I4 | Omit unsupported factual claims. | PASS | final.txt:1; prompt.txt; workspace/fixture/sources/north-annex-hours.md:3,5 | The closing time and effective date come from the schedule, while the arrival time comes from the prompt and the interval is direct arithmetic. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The conversational response has no parser, renderer, or other deterministic consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return a short ordinary message that corrects the premise, states the actual interval, discloses support, and contains no file artifact, blocker, or process narration. | PASS | final.txt:1 | The response is one conversational sentence, supplies the correction and derivation, links its support, and adds no process narration. |

## Readability

| Observation | Evidence |
|---|---|
| The rendered message is concise and natural; its raw Markdown target is an ephemeral absolute scratch path, though the visible link label remains readable. | final.txt:1 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The run is mechanically complete and judgeable. DR-I1 through DR-I4 and task fidelity pass, and no deterministic protocol applies. The response corrects the false premise, states the supported closing time and fifteen-minute interval, and maps both to the official schedule. |
| Disposition | Accepted by the owner on 2026-09-04 as the latest judgeable `PASS` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | The prompt requires support disclosure but does not prescribe a citation root. The response's absolute scratch path is precise during evaluation but not portable after scratch cleanup. |
| Scenario defects | None observed. No fixed response format applies, and the citation-root ambiguity does not prevent semantic judgment. |
| Proposed methodology changes | None beyond the citation-root clarification already identified by the DR-02 pilot. |
