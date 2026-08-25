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

- [ ] Verify canonical prompt SHA-256 `bc17742401c5d9fe6ed0e55d9e63bdaabd544a67d0925ff563c234b1a865c2f1`; obtain the complete rubric from the `LP-02` active-catalog row; confirm both selected `SKILL.md` source files exist.

- [ ] Materialize the prompt with only the two approved path adaptations. Create `test.json` with IDs `lp-02`; primary `lean-plan-writing`; dependency `writing-plans` at the current absolute source path; `include: ["SKILL.md"]` on both; fixture `null`; the complete rubric as `expected_outcome`; and the required execution settings.

- [ ] Load the configuration without invoking a provider. Confirm exactly two supplied files, no fixture, the adapted prompt, the withheld rubric, and matching source/package hashes. Run `uv run pytest -q` from `skill-validation/runner`.

- [ ] Obtain the required external-export approval for the prompt and two supplied `SKILL.md` files, then run exactly once from `skill-validation/runner`:

  `uv run skilltest run ../scenarios/lean-plan-writing/lp-02/test.json`

- [ ] Confirm `COMPLETED`, `infrastructure_error: null`, exactly the two declared provider-visible files, no fixture, and a withheld rubric. Record only mechanical, packaging, provider, and scenario fallout; do not score the response. If incomplete, record it and stop.

- [ ] Mark `LP-02` ported in `skill-validation/scenarios/README.md`; update lean-plan-writing totals to 7 total / 1 ported / 6 not ported and overall totals to 105 / 5 / 100.

- [ ] Run `git diff --check` and `git status --short`. Confirm no runner, skill, dependency, raw-output, bundle, or unrelated change entered the work.

- [ ] After successful verification, append the run outcome, move this plan to `plans/completed/`, and update the runner-shape plan link. Run the canonical Markdown-link checker and `git diff --check` against the final layout.

## Done when

- [ ] `LP-02` loads with exactly the repository skill file and the installed external skill file.
- [ ] One successful run covers the external-dependency shape and its mechanical evidence is recorded.
- [ ] Inventory and plan bookkeeping are reconciled with no broader change.
