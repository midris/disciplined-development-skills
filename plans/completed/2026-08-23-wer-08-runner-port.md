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

- [x] Verify the source prompt and rubric in the old worktree:
  - prompt SHA-256: `ad7fc0befc74d23accd09ac710a0fa1aa1111c3c48d218e6ca2672ac606c4c9a`;
  - rubric SHA-256: `98781f268c1b7f4d6052c896ca6bbc257377d2daff8a493ec9d9325121ef73ec`.

- [x] Copy the prompt. Change only `skills/writing-explicit-rationale/SKILL.md` to `supplied-skills/writing-explicit-rationale/SKILL.md`.

- [x] Create `test.json` with:
  - schema version `1`; test and scenario IDs `wer-08`;
  - primary skill `writing-explicit-rationale` from `../../../../skills/writing-explicit-rationale`;
  - no dependencies or fixture;
  - `expected_outcome` set to one JSON string containing the complete rubric Markdown; its decoded UTF-8 bytes must match the rubric SHA-256 above;
  - provider `codex`, model `gpt-5.6-sol`, effort `low`.

- [x] Confirm the tested skill matches main SHA-256 `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.

- [x] Run configuration preflight without a model:

  `cd skill-validation/runner && uv run python -c 'from pathlib import Path; from skilltest.config import load_config; load_config(Path("../scenarios/writing-explicit-rationale/wer-08/test.json"))'`

### Task 2: Run once and inspect

- [x] Run once:

  `cd skill-validation/runner && uv run skilltest run ../scenarios/writing-explicit-rationale/wer-08/test.json`

- [x] Inspect the retained bundle:
  - mechanical status and infrastructure error;
  - copied prompt and skill hashes;
  - subject input and workspace layout;
  - proof that the rubric was absent from provider-visible input at invocation and present only in the post-run `config.json` snapshot;
  - provider invocation record, stdout, stderr, and optional `final.txt`;
  - workspace state after exit.

- [x] Decide whether the response is evaluable. If it is, compare it with the withheld rubric as a first observation only. If it is not, record why; do not convert missing or malformed output into a behavioral failure.

- [x] Append a concise first-run outcome to this plan: run ID and bundle path, mechanical result, relevant hashes, whether the response was evaluable, observed behavior, and fallout grouped as runner, packaging, provider, scenario, or skill behavior. If the result is not `COMPLETED` with `infrastructure_error: null`, or the retained evidence is insufficient to inspect the scenario, state that runner validation remains incomplete.

- [x] Present the evidence and fallout to the owner, then stop. Do not repeat the run or fix findings until the next scope is agreed.

## Done when

- [x] `WER-08` is packaged in a loadable `skilltest` configuration.
- [x] One real provider run is `COMPLETED` with `infrastructure_error: null`.
- [x] The retained evidence is sufficient to inspect the scenario, has been inspected, and any fallout has been reported.
- [x] No behavioral baseline, runner fix, skill rewrite, raw-output commit, or PR was started as part of the first-run validation.

## First-run outcome — 2026-08-24

- **Run:** `20260824T044320545Z-wer-08-4b340440-8eb1-49a3-8d2f-d0e4e5669bc2-8zdpuaqb`; bundle `/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/skilltest-runs/20260824T044320545Z-wer-08-4b340440-8eb1-49a3-8d2f-d0e4e5669bc2-8zdpuaqb`.
- **Mechanical result:** `COMPLETED`; `infrastructure_error: null`; provider exit `0`; no timeout; duration `13.968s`.
- **Evidence:** configuration `90415ebb7af1e312d97a7f263ac0f58ce705b7d6ba5029b13fb4a751ab218724`; prompt `1adf257c187d55b3f35e50ee67b7e62ade5e8e40cd436ad017bc9b2f3e315835`; supplied skill `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`; decoded rubric `98781f268c1b7f4d6052c896ca6bbc257377d2daff8a493ec9d9325121ef73ec`. The retained copies match their sources. The rubric is absent from the subject input, copied inputs, and workspace; `runner.log` records the provider return before the post-run configuration snapshot.
- **Observed behavior:** evaluable. As a first observation, the response passes the withheld core rubric: it places the rationale beside the temporary cap in the policy, preserves the winter-shelter-demand cause, and does not choose a competing rationale home. Task-fidelity note: it adds unsupported “the board accepts” language and unnecessarily repeats the existing contingency ceiling, monthly review, and reversion controls.
- **Runner fallout:** none blocking. The first real configuration completed end to end and retained enough evidence to inspect status, inputs, invocation, output, and final workspace state.
- **Packaging fallout:** none. The prompt required only the planned supplied-skill path change, and all retained bytes match the packaged sources.
- **Provider fallout:** none blocking. Codex read the complete 111-line supplied skill, returned `final.txt`, emitted empty stderr, and reported 32,229 input tokens, 24,064 cached input tokens, 414 output tokens, and 163 reasoning-output tokens in raw stdout.
- **Scenario fallout:** none blocking. The response was directly judgeable against the withheld rubric.
- **Skill-behavior fallout:** the core decision-home behavior worked, but the extra unsupported and repetitive policy language is a useful pressure point for later skill-rewrite planning.

## Subsequent concurrency check — 2026-08-24

After this plan completed, the owner separately authorized two additional WER-08 runs to start simultaneously. Both completed with exit `0`, `infrastructure_error: null`, distinct run IDs, distinct bundles, and identical packaged-input hashes. Their execution windows overlapped by approximately `13.5s`, validating independent concurrent runner processes without changing runner code.

- `20260824T051925887Z-wer-08-811e35d2-c00c-471c-af22-5ba4a936e36c-nammkhsi`: `14.121s`.
- `20260824T051926473Z-wer-08-c4bc4b4a-69a5-4f0c-9f8e-d33067a23669-aralalbw`: `17.067s`.

Both outputs repeated the unsupported acceptance language seen in the first run; one also used the less precise insertion location “after the section.” These remain scenario or skill-behavior observations, not runner-concurrency failures.
