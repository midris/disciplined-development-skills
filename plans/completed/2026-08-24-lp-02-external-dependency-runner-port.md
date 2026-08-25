# LP-02 External Dependency Runner Port Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Package and smoke-run `LP-02` using the repository's `lean-plan-writing` skill and the currently installed external `writing-plans` skill.

**Architecture:** Use the existing schema `"0.1"` contract with one explicitly included file per skill. Point the dependency at its current host path; make no runner, skill, vendoring, version-resolution, or provenance changes.

**Tech stack:** Markdown, JSON, `skilltest`, Codex CLI.

**Spec:** `plans/2026-08-24-runner-shape-coverage.md`, `plans/2026-08-24-scenario-porting-roadmap.md`, and `skill-validation/charter/core-contracts.md`.

## Global constraints

- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c` for the `LP-02` prompt and rubric.
- Use `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans` as the current best-effort external source. Do not add pinning or sourcing machinery.
- Use schema `"0.1"`; include only `SKILL.md` from `lean-plan-writing` and `writing-plans`; use no fixture.
- Adapt only the prompt paths from `skills/...` to `supplied-skills/...`.
- Run once with Codex `gpt-5.6-sol` at low effort. Do not score behavior, rerun, or fix fallout.
- Do not change the runner, skills, methodology, or baseline. Do not commit raw output or the temporary run bundle.
- If the external source is unavailable or the existing runner cannot package it, record the blocker and stop. Any code change requires separate approval.

## Files

- Create `skill-validation/scenarios/lean-plan-writing/lp-02/prompt.md`.
- Create `skill-validation/scenarios/lean-plan-writing/lp-02/test.json`.
- Update `skill-validation/scenarios/README.md`, this plan, and `plans/2026-08-24-runner-shape-coverage.md` on completion.

---

### Task 1: Package and smoke-run `LP-02`

- [x] Verify canonical prompt SHA-256 `bc17742401c5d9fe6ed0e55d9e63bdaabd544a67d0925ff563c234b1a865c2f1`; obtain the complete rubric from the `LP-02` active-catalog row; confirm both selected `SKILL.md` source files exist.

- [x] Materialize the prompt with only the two approved path adaptations. Create `test.json` with IDs `lp-02`; primary `lean-plan-writing`; dependency `writing-plans` at the current absolute source path; `include: ["SKILL.md"]` on both; fixture `null`; the complete rubric as `expected_outcome`; and the required execution settings.

- [x] Load the configuration without invoking a provider. Confirm exactly two supplied files, no fixture, the adapted prompt, the withheld rubric, and matching source/package hashes. Run `uv run pytest -q` from `skill-validation/runner`.

- [x] Obtain the required external-export approval for the prompt and two supplied `SKILL.md` files, then run exactly once from `skill-validation/runner`:

  `uv run skilltest run ../scenarios/lean-plan-writing/lp-02/test.json`

- [x] Confirm `COMPLETED`, `infrastructure_error: null`, exactly the two declared provider-visible files, no fixture, and a withheld rubric. Record only mechanical, packaging, provider, and scenario fallout; do not score the response. If incomplete, record it and stop.

- [x] Mark `LP-02` ported in `skill-validation/scenarios/README.md`; update lean-plan-writing totals to 7 total / 1 ported / 6 not ported and overall totals to 105 / 5 / 100.

- [x] Run `git diff --check` and `git status --short`. Confirm no runner, skill, dependency, raw-output, bundle, or unrelated change entered the work.

- [x] After successful verification, append the run outcome, move this plan to `plans/completed/`, and update the runner-shape plan link. Run the canonical Markdown-link checker and `git diff --check` against the final layout.

## Done when

- [x] `LP-02` loads with exactly the repository skill file and the installed external skill file.
- [x] One successful run covers the external-dependency shape and its mechanical evidence is recorded.
- [x] Inventory and plan bookkeeping are reconciled with no broader change.

## Run outcome — 2026-08-25

- **Run:** `20260825T012106996Z-lp-02-0fb3958b-8cca-46fa-af05-0a6e4beadeb4-7vbmpbg3`; bundle `/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/skilltest-runs/20260825T012106996Z-lp-02-0fb3958b-8cca-46fa-af05-0a6e4beadeb4-7vbmpbg3`.
- **Mechanical result:** `COMPLETED`; `infrastructure_error: null`; provider exit `0`; no timeout; duration `65.809s`.
- **Evidence:** configuration `eb087912586c3f9ca2282a469c059924102b569ae90116cec0251028c0274970`; adapted prompt `43c33c3ce101a174432c28210eb92780a44c35011d9738156c25e355ba2bf8b6`; supplied `lean-plan-writing` skill `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac`; supplied external `writing-plans` skill `48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2`. Retained inputs and workspace copies match the two configured files, no fixture is present, and the rubric is absent from subject input and workspace. `runner.log` records provider return before the configuration snapshot.
- **Observed behavior:** not scored; the retained response is outside this mechanical packaging check.
- **Runner fallout:** none blocking. The external dependency packaged as exactly its declared `SKILL.md` file and the retained evidence was sufficient for inspection.
- **Packaging fallout:** none. The two approved prompt-path adaptations and both supplied skill hashes matched preflight evidence.
- **Provider fallout:** none blocking. Codex returned `final.txt`, emitted empty stderr, and reported 32,892 input tokens, 24,064 cached input tokens, 1,824 output tokens, and 437 reasoning-output tokens in raw stdout.
- **Scenario fallout:** none blocking. The provider completed the declared external-dependency shape without a runner infrastructure error.
- **Skill-behavior fallout:** not assessed; this run is not a behavioral score or baseline.
