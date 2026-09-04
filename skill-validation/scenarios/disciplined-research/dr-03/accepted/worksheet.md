# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/disciplined-research/dr-03 |
| Scenario ID | dr-03 |
| Scenario purpose | Verify the project's declared dependency and upstream stable version separately, and correct a cross-domain claim without overstating either source. |
| Run ID | 20260904T022315209Z-dr-03-b4dbc655-e973-48d1-be2c-4f3ccbf4757b-tpdn0q9e |
| Provider | codex |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-04T02:23:15.209Z |
| Finished | 2026-09-04T02:23:39.353Z |
| Duration seconds | 24.143 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | ea1c3772137b746ab37ed17be116fb052a8a5def3ce66af7c071305c119d5e17 |
| Prompt template | prompt-template.txt | 5c3d956940727938d7812bf40448760127461d20c84d3c1edf8c28511f8096d8 |
| Rendered prompt | prompt.txt | 30bd25cab55b6e348ec408d85fd577b01b0af2e6d7211e2f682177777e003194 |
| Fixture | project/package.json | 1c2bb8f53dce6c7a90c2411d53f177dbfcba8ace56861399dd4f55412e0fb262 |
| Fixture | skills/disciplined-research/SKILL.md | a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50 |
| Fixture | sources/orbital-maintainer-blog.md | 3f6e47ed632fde9a22f94ec764ca2c98b5365a9db6190566e8efb29234347488 |
| Fixture | sources/orbital-release-notes.md | 1592db31a0848116b082b2093704d80847f672b540633c00b0ea6c30ad03c3f4 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/disciplined-research/dr-03/rubric.md | 6a61e4e49a3ff4141ebda92ff91fc420e88e1a3e75157a2072fd0ed020a2f474 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| DR-I1 | Verify every factual claim or relied-on premise before use. | FAIL | final.txt:1; workspace/fixture/project/package.json:3-4 | `package.json` verifies that the project declares `orbital-sdk` 3.4.2 as a dependency; it does not verify the emitted claim that the project “uses” 3.4.2. The official release notes do verify the 4.1.0 stable-release claim. |
| DR-I2 | Select sources that are authoritative, applicable, and current enough for each claim. | FAIL | final.txt:1-3; workspace/fixture/project/package.json:3-4; workspace/fixture/sources/orbital-release-notes.md:3-5 | The release notes are current and applicable to the upstream stable-version claim. `package.json` is authoritative for the declared dependency but is not applicable evidence for actual installed or runtime use. |
| DR-I3 | Map each emitted fact precisely and truthfully to its support. | FAIL | final.txt:1-3; workspace/fixture/project/package.json:3-4; workspace/fixture/sources/orbital-release-notes.md:5 | The 4.1.0 claim maps truthfully to the official release notes. Mapping “uses Orbital SDK 3.4.2” to `package.json` overstates what that file supports. |
| DR-I4 | Omit unsupported facts or retain useful leads only with explicit unverified disclosure. | FAIL | final.txt:1; workspace/fixture/project/package.json:3-4 | The response emits the unsupported “uses” claim without qualifying it as unverified; it should have stated that the project declares 3.4.2. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer applies. | N/A | prompt.txt; rubric.md | The exact three-line shape and source order are task requirements, not deterministic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return one corrected sentence followed by the project and upstream source paths, in that order, with no stale-blog citation or narration. | PASS | final.txt:1-3 | The response has exactly three lines, cites the two supplied files in the required order, omits the stale blog, and adds no narration. The unsupported “uses” wording is scored on the semantic ledger. |

## Readability

| Observation | Evidence |
|---|---|
| The response is concise and structurally clear, but “uses” erases the material declared-versus-installed distinction. | final.txt:1 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | The run is mechanically complete and judgeable, with no deterministic protocol applicable. All four semantic invariants fail because the response changes the supported declaration of dependency version 3.4.2 into an unsupported claim that the project uses that version. The upstream 4.1.0 fact and task fidelity pass, but they do not override the blocking semantic failures. |
| Disposition | Accepted by the owner on 2026-09-03 as the latest judgeable `FAIL` baseline. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None. The repaired declared-versus-installed distinction is observable in the supplied project source and response. |
| Scenario defects | None observed after the DR-03 contract repair. |
| Proposed methodology changes | None. The separate semantic and task-fidelity ledgers preserve the cause of this result. |
