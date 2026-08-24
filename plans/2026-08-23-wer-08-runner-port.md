# WER-08 First Runner Validation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port `WER-08` into `skilltest`, run it once against the main skill, and inspect the result to validate the runner's first real scenario path.

**Architecture:** Package the existing prompt and withheld rubric as one runner configuration. Run that configuration once, inspect the retained bundle, report the fallout, and stop.

**Tech stack:** Markdown, JSON configuration schema version 1, `skilltest`, Codex CLI.

**Spec:** `skill-validation/charter/core-contracts.md`, with runner mechanics governed by `plans/completed/specs/2026-08-23-single-run-skill-test-runner-design.md`.

## Goals

- Preserve the selected `WER-08` scenario while adapting it to the runner's `supplied-skills/` layout.
- Exercise the complete real path: configuration load, workspace preparation, skill loading, one Codex invocation, and retained results.
- Determine whether the runner produces enough trustworthy evidence to inspect a real scenario.
- Record runner, packaging, provider, scenario, and behavioral fallout for the next planning discussion.

## Limits

- Run exactly once with `gpt-5.6-sol` at low effort.
- This run is runner validation, not a behavioral baseline, scenario acceptance, or rebuilt-suite activation.
- Do not change skill or runner code, repeat the run, fix discovered fallout, create general scenario conventions, or begin the skill rewrite.
- Leave `.worktrees/comprehensive-skill-cleanup/` read-only.
- Do not commit raw output or the temporary bundle.
- Stop after reporting the first-run evidence. The fallout determines the next plan.

One run is intentional: the immediate question is whether a real scenario works end to end. Repetition, baselining, and comparison arms become useful only after that path is understood.

## Files

- Create `skill-validation/scenarios/writing-explicit-rationale/wer-08/prompt.md`.
- Create `skill-validation/scenarios/writing-explicit-rationale/wer-08/test.json`.
- Update this plan's checkboxes and append the first-run outcome.

---

### Task 1: Port `WER-08`

- [ ] Verify the source prompt and rubric in the old worktree:
  - prompt SHA-256: `ad7fc0befc74d23accd09ac710a0fa1aa1111c3c48d218e6ca2672ac606c4c9a`;
  - rubric SHA-256: `98781f268c1b7f4d6052c896ca6bbc257377d2daff8a493ec9d9325121ef73ec`.

- [ ] Copy the prompt. Change only `skills/writing-explicit-rationale/SKILL.md` to `supplied-skills/writing-explicit-rationale/SKILL.md`.

- [ ] Create `test.json` with:
  - schema version `1`; test and scenario IDs `wer-08`;
  - primary skill `writing-explicit-rationale` from `../../../../skills/writing-explicit-rationale`;
  - no dependencies or fixture;
  - `expected_outcome` set to one JSON string containing the complete rubric Markdown; its decoded UTF-8 bytes must match the rubric SHA-256 above;
  - provider `codex`, model `gpt-5.6-sol`, effort `low`.

- [ ] Confirm the tested skill matches main SHA-256 `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.

- [ ] Run configuration preflight without a model:

  `cd skill-validation/runner && uv run python -c 'from pathlib import Path; from skilltest.config import load_config; load_config(Path("../scenarios/writing-explicit-rationale/wer-08/test.json"))'`

### Task 2: Run once and inspect

- [ ] Run once:

  `cd skill-validation/runner && uv run skilltest run ../scenarios/writing-explicit-rationale/wer-08/test.json`

- [ ] Inspect the retained bundle:
  - mechanical status and infrastructure error;
  - copied prompt and skill hashes;
  - subject input and workspace layout;
  - proof that the rubric was absent from provider-visible input at invocation and present only in the post-run `config.json` snapshot;
  - provider invocation record, stdout, stderr, and optional `final.txt`;
  - workspace state after exit.

- [ ] Decide whether the response is evaluable. If it is, compare it with the withheld rubric as a first observation only. If it is not, record why; do not convert missing or malformed output into a behavioral failure.

- [ ] Append a concise first-run outcome to this plan: run ID and bundle path, mechanical result, relevant hashes, whether the response was evaluable, observed behavior, and fallout grouped as runner, packaging, provider, scenario, or skill behavior. If the result is not `COMPLETED` with `infrastructure_error: null`, or the retained evidence is insufficient to inspect the scenario, state that runner validation remains incomplete.

- [ ] Present the evidence and fallout to the owner, then stop. Do not repeat the run or fix findings until the next scope is agreed.

## Done when

- [ ] `WER-08` is packaged in a loadable `skilltest` configuration.
- [ ] One real provider run is `COMPLETED` with `infrastructure_error: null`.
- [ ] The retained evidence is sufficient to inspect the scenario, has been inspected, and any fallout has been reported.
- [ ] No baseline, runner fix, skill rewrite, commit, or PR has been started.
