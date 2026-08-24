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

- [ ] Verify the canonical material in `.worktrees/comprehensive-skill-cleanup/skill-validation/writing-explicit-rationale.md`:
  - source prompt SHA-256: `04e991da2e028d059a6fe5ec508b731b73e54ccb67696413be42c719087df6e8`;
  - fixture SHA-256: `5e25960ed19f0e046ecb263282d9244b9a5026695cc16a7ddb08663f422e4f7e`;
  - rubric SHA-256: `2ea06ed57c8bbdf68a16c05d59a04b747ee14c7dc86e67c6d0e0072ca19bc18f`.

- [ ] Copy the prompt. Change only `skills/writing-explicit-rationale/SKILL.md` to `supplied-skills/writing-explicit-rationale/SKILL.md`.

- [ ] Materialize the fixture at `fixture/docs/architecture/ingest.md` with the exact canonical bytes.

- [ ] Create `test.json` with schema version `1`, IDs `wer-05`, the main skill source `../../../../skills/writing-explicit-rationale`, no dependencies, prompt `prompt.md`, fixture `fixture`, the complete rubric as the opaque `expected_outcome` string, and Codex `gpt-5.6-sol` at low effort. The decoded rubric bytes must match the SHA-256 above.

- [ ] Confirm the supplied main skill SHA-256 is `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.

- [ ] Load the configuration without invoking a model:

  `cd skill-validation/runner && uv run python -c 'from pathlib import Path; from skilltest.config import load_config; load_config(Path("../scenarios/writing-explicit-rationale/wer-05/test.json"))'`

### Task 2: Run once and inspect

- [ ] Run once:

  `cd skill-validation/runner && uv run skilltest run ../scenarios/writing-explicit-rationale/wer-05/test.json`

- [ ] Inspect `result.json`, copied inputs, subject input, provider invocation, stdout, stderr, optional `final.txt`, and final workspace. Confirm the prompt, fixture, and skill hashes match their packaged sources and that the rubric was absent from provider-visible runner additions.

- [ ] Decide whether the response is evaluable. If it is, compare it with the withheld rubric as one observation only. If it is not, record why without treating missing or malformed output as a behavioral failure.

- [ ] Append the run ID, bundle path, mechanical result, relevant hashes, evaluability, observed behavior, and fallout grouped as runner, packaging, provider, scenario, or skill behavior.

- [ ] Present the evidence and fallout, then stop. Do not rerun or begin fixes until the next scope is agreed.

## Done when

- [ ] `WER-05` is packaged in a loadable `skilltest` configuration with its fixture.
- [ ] One real provider run completes with `status: COMPLETED` and `infrastructure_error: null`.
- [ ] The retained evidence is sufficient to inspect the scenario and any fallout is reported.
- [ ] No baseline, broader validation process, runner change, or skill rewrite has started.
