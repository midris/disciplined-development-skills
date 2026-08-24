# Active Scenario Inventory Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a simple list of the active scenarios that are candidates for migration into `skilltest`.

**Architecture:** Read the active catalogs from the clean comprehensive-cleanup worktree and write one catalog-grouped list beside the new scenario tree. Do not analyze migration requirements yet.

**Tech Stack:** Markdown, Git, `rg`.

**Spec:** `plans/2026-08-24-scenario-porting-roadmap.md` and `skill-validation/charter/core-contracts.md`.

## Global constraints

- Keep `.worktrees/comprehensive-skill-cleanup/` read-only.
- Use `docs/comprehensive-skill-cleanup` at commit `13599fb7d3127334b0d07bfe468767e586ec5f9c` as the canonical inventory source.
- List only scenarios identified as active by the canonical audit index and owning catalogs.
- Do not port a scenario, invoke a provider, change a skill or runner, design testing methodology, or establish a baseline.

## Files

- Create `skill-validation/scenarios/README.md`.
- Update this plan with the inventory totals after review.

---

### Task 1: Build the inventory

- [ ] Verify the preserved worktree is on `docs/comprehensive-skill-cleanup` at `13599fb7d3127334b0d07bfe468767e586ec5f9c`, is clean, and matches `origin/docs/comprehensive-skill-cleanup`.

- [ ] Read the canonical audit index and framework inventory in `.worktrees/comprehensive-skill-cleanup/skill-validation/README.md`, then inspect each owning record's active catalog.

- [ ] Create `skill-validation/scenarios/README.md` with one section per owning catalog and one list item per active scenario. Each item contains only the scenario ID, its canonical source section or fixture path, and `ported` or `not ported`.

- [ ] Mark `WER-05` and `WER-08` as ported and link their existing configuration paths.

- [ ] Reconcile the list against every canonical active catalog. List shared scenarios once under their canonical owner and record candidate totals by catalog and overall.

- [ ] Run the exact local Markdown-link checker under `Verification commands` in `.worktrees/comprehensive-skill-cleanup/skill-validation/README.md`, run `git diff --check`, present the list and totals, then stop. Do not begin migration planning or porting.

## Done when

- [ ] Every canonical active catalog is accounted for.
- [ ] Every active migration candidate appears exactly once.
- [ ] WER-05 and WER-08 are marked as already ported.
- [ ] No migration analysis, methodology, or scenario changes have started.
