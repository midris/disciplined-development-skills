# WER-05 End-to-End Runner Port Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port the `WER-05` scenario into `skilltest` and complete one real run against the main `writing-explicit-rationale` skill.

**Architecture:** Materialize the canonical prompt, withheld rubric, and project fixture as one runner configuration. Run it once, inspect whether the complete path and retained evidence work, record fallout, and stop.

**Tech stack:** Markdown, JSON configuration schema version 1, `skilltest`, Codex CLI.

**Spec:** `skill-validation/charter/core-contracts.md`, with runner mechanics governed by `plans/completed/specs/2026-08-23-single-run-skill-test-runner-design.md`.

## Global constraints

- This ports a scenario; it does not change the skill or runner.
- Run once with `gpt-5.6-sol` at low effort.
- This is an end-to-end check, not a baseline, acceptance verdict, scoring process, or broader validation design.
- Leave `.worktrees/comprehensive-skill-cleanup/` read-only.
- Do not repeat the run or fix fallout in this plan. If the run is incomplete, record that and stop.
- Do not commit raw output or the temporary result bundle.

## Files

- Create `skill-validation/scenarios/writing-explicit-rationale/wer-05/prompt.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-05/fixture/docs/architecture/ingest.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-05/test.json`.
- Update this plan with the run outcome.

---

### Task 1: Package `WER-05`

- [x] Verify the canonical material in `.worktrees/comprehensive-skill-cleanup/skill-validation/writing-explicit-rationale.md`:
  - source prompt SHA-256: `04e991da2e028d059a6fe5ec508b731b73e54ccb67696413be42c719087df6e8`;
  - fixture SHA-256: `5e25960ed19f0e046ecb263282d9244b9a5026695cc16a7ddb08663f422e4f7e`;
  - rubric SHA-256: `2ea06ed57c8bbdf68a16c05d59a04b747ee14c7dc86e67c6d0e0072ca19bc18f`.

- [x] Copy the prompt. Change only `skills/writing-explicit-rationale/SKILL.md` to `supplied-skills/writing-explicit-rationale/SKILL.md`.

- [x] Materialize the fixture at `fixture/docs/architecture/ingest.md` with the exact canonical bytes.

- [x] Create `test.json` with schema version `1`, IDs `wer-05`, the main skill source `../../../../skills/writing-explicit-rationale`, no dependencies, prompt `prompt.md`, fixture `fixture`, the complete rubric as the opaque `expected_outcome` string, and Codex `gpt-5.6-sol` at low effort. The decoded rubric bytes must match the SHA-256 above.

- [x] Confirm the supplied main skill SHA-256 is `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.

- [x] Load the configuration without invoking a model:

  `cd skill-validation/runner && uv run python -c 'from pathlib import Path; from skilltest.config import load_config; load_config(Path("../scenarios/writing-explicit-rationale/wer-05/test.json"))'`

### Task 2: Run once and inspect

- [x] Run once:

  `cd skill-validation/runner && uv run skilltest run ../scenarios/writing-explicit-rationale/wer-05/test.json`

- [x] Inspect `result.json`, copied inputs, subject input, provider invocation, stdout, stderr, optional `final.txt`, and final workspace. Confirm the prompt, fixture, and skill hashes match their packaged sources and that the rubric was absent from provider-visible runner additions.

- [x] Decide whether the response is evaluable. If it is, compare it with the withheld rubric as one observation only. If it is not, record why without treating missing or malformed output as a behavioral failure.

- [x] Append the run ID, bundle path, mechanical result, relevant hashes, evaluability, observed behavior, and fallout grouped as runner, packaging, provider, scenario, or skill behavior.

- [x] Present the evidence and fallout, then stop. Do not rerun or begin fixes until the next scope is agreed.

## Done when

- [x] `WER-05` is packaged in a loadable `skilltest` configuration with its fixture.
- [x] One real provider run completes with `status: COMPLETED` and `infrastructure_error: null`.
- [x] The retained evidence is sufficient to inspect the scenario and any fallout is reported.
- [x] No baseline, broader validation process, runner change, or skill rewrite has started.

## Run outcome — 2026-08-24

- **Run:** `20260824T063356655Z-wer-05-277a06ec-c9bb-4bf8-85a1-549fa330c6ab-qylm6i7t`; bundle `/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/skilltest-runs/20260824T063356655Z-wer-05-277a06ec-c9bb-4bf8-85a1-549fa330c6ab-qylm6i7t`.
- **Mechanical result:** `COMPLETED`; `infrastructure_error: null`; provider exit `0`; no timeout; duration `16.655s`.
- **Evidence:** configuration `43cf285e878aef40e5ceff6b51cdd62791bb1e1dd426f4f9cdca70eeb6f26760`; prompt `b444099e4e73b5aea76aba733bc564d5ae5f09c4c4c5cc758939140bdd21666f`; fixture `5e25960ed19f0e046ecb263282d9244b9a5026695cc16a7ddb08663f422e4f7e`; supplied skill `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`; decoded rubric `2ea06ed57c8bbdf68a16c05d59a04b747ee14c7dc86e67c6d0e0072ca19bc18f`. Retained input and workspace copies match the packaged sources. The rubric is absent from the subject input, copied inputs, and workspace; `runner.log` records the provider return before the configuration snapshot.
- **Observed behavior:** evaluable. As one observation, the response does not satisfy the withheld rubric: neither block references `docs/architecture/ingest.md#interactive-guard-placement`, and both recreate the causal explanation, accepted duplication, and third-caller revisit rule as competing rationale homes.
- **Runner fallout:** none blocking. The fixture and supplied skill were copied to the expected workspace locations, and the retained evidence was sufficient for inspection.
- **Packaging fallout:** none. Prompt, fixture, rubric, and skill bytes matched their canonical or main sources.
- **Provider fallout:** none blocking. Codex read both supplied files, returned `final.txt`, emitted empty stderr, and reported 32,126 input tokens, 24,064 cached input tokens, 452 output tokens, and 146 reasoning-output tokens in raw stdout.
- **Scenario fallout:** none blocking. The output was directly judgeable against the withheld rubric.
- **Skill-behavior fallout:** the current skill did not cause the response to reference the existing authoritative rationale and avoid duplication. This is recorded for later planning; no fix or broader conclusion starts here.
