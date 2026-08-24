# Runner Shape Coverage Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Select one representative for each uncovered runner shape and create an approved plan to port and smoke-run it.

**Architecture:** Investigate one shape at a time. This plan selects the representative and solution; a separate plan owns implementation, the smoke run, the inventory update, and completion.

**Tech stack:** Markdown, JSON configuration schema version 1, `skilltest`, Codex CLI.

**Spec:** `plans/2026-08-24-scenario-porting-roadmap.md` and `skill-validation/charter/core-contracts.md`.

## Global constraints

- Use `origin/docs/comprehensive-skill-cleanup` at `13599fb7d3127334b0d07bfe468767e586ec5f9c` as the canonical scenario source.
- Preserve the selected scenario's prompt, rubric, fixture, dependencies, and declared skill context. Adapt only paths required by `skilltest` packaging.
- Do not change the runner without a separate owner-approved scope.
- Finish and review one shape before starting the next.

---

### Task 1: Primary skill with prompt only — `WER-08`

- [x] Port `WER-08` into a loadable configuration.
- [x] Complete and inspect one end-to-end run.
- [x] Record the result in `plans/completed/2026-08-23-wer-08-runner-port.md`.

### Task 2: Primary skill with fixture — `WER-05`

- [x] Port `WER-05` with its fixture.
- [x] Complete and inspect one end-to-end run.
- [x] Record the result in `plans/completed/2026-08-24-wer-05-runner-port.md`.

### Task 3: Multiple supplied skills

- [ ] Inspect the active candidates, their canonical inputs, and the runner contract.
- [ ] Select the representative.
- [ ] Develop and obtain approval for a faithful porting solution.
- [ ] Create a separate implementation plan that owns completion, then stop for review.

### Task 4: Multiple supplied skills with a fixture

- [ ] Inspect the active candidates, their canonical inputs, and the runner contract.
- [ ] Select the representative.
- [ ] Develop and obtain approval for a faithful porting solution.
- [ ] Create a separate implementation plan that owns completion, then stop for review.

### Task 5: Pinned external dependency

- [ ] Inspect the active candidates, their canonical inputs, and the runner contract.
- [ ] Select the representative.
- [ ] Develop and obtain approval for a faithful porting solution.
- [ ] Create a separate implementation plan that owns completion, then stop for review.

### Task 6: Description-only routing with no primary skill

- [ ] Inspect the active candidates, their canonical inputs, and the runner contract.
- [ ] Select the representative.
- [ ] Develop and obtain approval for a faithful porting solution.
- [ ] Create a separate implementation plan that owns completion, then stop for review.

## Done when

- Each uncovered shape has an approved representative, solution, and implementation plan.
- Each implementation plan owns the port, smoke run, inventory update, and completion.
- Testing methodology and baselines remain deferred.
