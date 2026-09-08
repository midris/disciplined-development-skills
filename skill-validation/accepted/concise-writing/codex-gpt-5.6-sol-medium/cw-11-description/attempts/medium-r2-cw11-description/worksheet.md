# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/pilot/cw-11/description |
| Scenario ID | cw-11-description-medium |
| Scenario purpose | CW-11 reference-authoring description diagnostic, repetition 2. |
| Run ID | 20260908T120502776Z-cw-11-description-medium-04d2b178-99e3-4c72-a2f0-186b4820ebb7-z52xfuko |
| Provider | codex |
| Provider CLI version | codex-cli 0.153.4 — [capture](cli-version.txt), [digest](cli-sha256.txt). |
| Model | gpt-5.6-sol |
| Effort | medium |
| Started | 2026-09-08T12:05:02.776Z |
| Finished | 2026-09-08T12:05:18.868Z |
| Duration seconds | 16.092 |

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
| Rendered prompt | prompt.txt | 46c8218cfa293254bdcf2553ff77857a20cb2ce5ee258239307480aa55522e80 |
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
| Authoring composition | Required selection | FAIL | [final][final] | WS selected, CW absent; required composition not met. |
| Authoring composition | Exclude unrelated skills | PASS | [final][final] | No unrelated skill selected. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| None | N/A | Frozen rubric | No authenticated consumer. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Descriptions-only loading | PASS | [trace][trace], item_0 | All three declared descriptions, no body reads. |
| Deliverable and boundaries | PASS | [trace][trace] | Compact alphabetical JSON singleton only; fixture-local read, no narration or mutations. |
| Source faithfulness | PASS | [trace][trace] | Current CW explicitly excludes reference authoring; WS-only answer follows supplied descriptions. |

## Readability

| Observation | Evidence |
|---|---|
| PASS: clear compact selection. | [final][final] |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | Target composition fails despite source-faithful classification; not native discovery. |
| Disposition | Scratch-only pending owner acceptance; retain this judgeable observation. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | Hidden provider inputs/internal use remain outside trace proof. |
| Scenario defects | None observed. |
| Proposed methodology changes | None. Command exit 0; complete trace and matching final. Exact argv, frozen inputs and prelaunch/artifact hashes verified; protected fixtures unchanged, expected Git files only, evidence empty. COMPLETED establishes owned cleanup under frozen runner; exact logged runtime absent. Provider/command stderr empty; version-only PATH-alias warning unchanged. |

[final]: ../../runs/skilltest-runs/20260908T120502776Z-cw-11-description-medium-04d2b178-99e3-4c72-a2f0-186b4820ebb7-z52xfuko/final.txt
[trace]: ../../runs/skilltest-runs/20260908T120502776Z-cw-11-description-medium-04d2b178-99e3-4c72-a2f0-186b4820ebb7-z52xfuko/stdout.txt
