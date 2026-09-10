# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-11/description |
| Scenario ID | cw-11-description-medium |
| Scenario purpose | CW-11 reference-authoring description-classification diagnostic. |
| Run ID | 20260908T111902997Z-cw-11-description-medium-8eefe3ba-6aed-42b0-a802-107905378ea1-acasutxx |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T11:19:02.997Z |
| Finished | 2026-09-08T11:19:18.541Z |
| Duration seconds | 15.543 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 167de21ab76042989ceb6dc2289c7dc050f453e2fe3d64fc60a94a465abda8dd |
| Prompt template | prompt-template.txt | 441dae342fb53387b0effde82a183ec4a26018437f1fb1e3e906efceba956e95 |
| Rendered prompt | prompt.txt | d2747fa474df5730b49ca23d38dcd9a5d7c173e6b95651c0473ff842f2fa3175 |
| Fixture | .agents/skills/requesting-code-review/SKILL.md | d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8 |
| Fixture | .agents/skills/requesting-code-review/code-reviewer.md | 5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4 |
| Fixture | .agents/skills/writing-plans/SKILL.md | 48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2 |
| Fixture | .agents/skills/writing-plans/plan-document-reviewer-prompt.md | aa728b96aad603c8be28875a4305637f6c984aa81ffcadcb13e743202fa2a0c7 |
| Fixture | .git/HEAD | f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10 |
| Fixture | .git/config | cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda |
| Fixture | descriptions/adversarial-review-loop.txt | 38843f7718501f52116bfd4f95a6640cb16b560851767df540c808a1ed18cefa |
| Fixture | descriptions/concise-writing.txt | 586a741a9cb28746078ca1b5f7aa570a4e621a5d2cdecac16e31bd6d2c82fd62 |
| Fixture | descriptions/superpowers-writing-skills.txt | 5504b0825ec458aa8c20e9a55c6a932b36849e261a97aaf98af366e19a937154 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/pilot/cw-11/description/rubric.md | 784c4784829fda7647384974f508973e84ede733517dd36536d9a76ec9ffba34 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Authoring composition | Required composition selection | FAIL | [final][final] | Selects writing-skills only; intended target also requires CW. |
| Authoring composition | Exclude unrelated selections | PASS | [final][final] | No unrelated selection. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | JSON shape has no authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested loading | PASS | [trace][trace], item_0 | Reads all three complete descriptions, no skill bodies. |
| Deliverable and boundaries | PASS | [trace][trace], items 0–1; inventory | Compact alphabetical array only; fixture-only reads, no narration/mutations. |
| Source faithfulness | PASS | [trace][trace], description output | CW excludes reference authoring; editing a shipped reference falls within editing an existing skill. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: unambiguous compact selection. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | Intended composition lacks CW despite source-faithful classification; not native discovery or executed reference editing. Protocol N/A, fidelity PASS. |
| Disposition | Scratch-only pending owner acceptance; retain judgeable failure. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Source-faithful answer and intended-contract FAIL intentionally coexist. Hidden provider inputs remain outside trace proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; six-event complete trace and matching final. Exact argv, artifact/prelaunch hashes and frozen sources verified; seven protected fixtures unchanged, only expected template-free Git files, evidence empty. COMPLETED establishes owned cleanup under frozen runner; logged runtime /private/tmp/skilltest-cw-baseline.bOn8Dx/runs/skilltest-codex-kcefz0e5 absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T111902997Z-cw-11-description-medium-8eefe3ba-6aed-42b0-a802-107905378ea1-acasutxx/final.txt
[trace]: ../../runs/skilltest-runs/20260908T111902997Z-cw-11-description-medium-8eefe3ba-6aed-42b0-a802-107905378ea1-acasutxx/stdout.txt
