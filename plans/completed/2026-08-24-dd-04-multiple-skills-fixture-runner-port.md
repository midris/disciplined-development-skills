# DD-04 Multiple Skills with Fixture Runner Port Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Package and smoke-run `DD-04` as the representative for multiple supplied repository skills with a fixture.

**Architecture:** Use the existing schema `"0.1"` contract to supply only the two required `SKILL.md` files and the canonical one-file fixture. Make no runner or skill changes.

**Tech stack:** Markdown, JSON, `skilltest`, Codex CLI.

**Spec:** `plans/2026-08-24-runner-shape-coverage.md`, `plans/2026-08-24-scenario-porting-roadmap.md`, and `skill-validation/charter/core-contracts.md`.

## Global constraints

- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
- Preserve the prompt, rubric, fixture, and two-skill context exactly; no path adaptation is needed.
- Use schema `"0.1"`; include only `SKILL.md` from `disciplined-development` and `disciplined-research`.
- Run once with Codex `gpt-5.6-sol` at low effort.
- Do not change the runner, skills, methodology, or baseline. Do not rerun or fix fallout under this plan.
- Do not commit raw output or the temporary run bundle.

## Files

- Create `skill-validation/scenarios/disciplined-development/dd-04/prompt.md`.
- Create `skill-validation/scenarios/disciplined-development/dd-04/fixture/project/dd-04/sources/deployment-targets.md`.
- Create `skill-validation/scenarios/disciplined-development/dd-04/test.json`.
- Update `skill-validation/scenarios/README.md`, this plan, and `plans/2026-08-24-runner-shape-coverage.md` on completion.

---

### Task 1: Package and smoke-run `DD-04`

- [x] Verify the canonical prompt SHA-256 `939a40cfe8fe27025ad8c83230830f000c8db0a67c440af0f42cf21925c9183f`, rubric SHA-256 `275eb747335ff0f5d4b7933d43958332e33215db4a04dd8695c7e3e8327e8466`, and fixture SHA-256 `90e874878dd0380aca4517b53eedb1f58436f6f3500fb2397517716aa15b986d`.

- [x] Materialize the prompt and fixture unchanged. Create `test.json` with IDs `dd-04`; primary `disciplined-development`; dependency `disciplined-research`; `include: ["SKILL.md"]` on both; fixture `fixture`; exact rubric as `expected_outcome`; and the required execution settings.

- [x] Load the configuration without invoking a provider. Confirm the skill order, include lists, fixture path, and packaged hashes, then run `uv run pytest -q` from `skill-validation/runner`.

- [x] From `skill-validation/runner`, run exactly once:

  `uv run skilltest run ../scenarios/disciplined-development/dd-04/test.json`

- [x] Inspect the retained result and inputs. Confirm `COMPLETED`, `infrastructure_error: null`, exactly two provider-visible `SKILL.md` files, the unchanged fixture, and a withheld rubric. Record the mechanical result and packaging fallout without scoring the response; if the run is incomplete, record it and stop.

- [x] Mark `DD-04` ported in `skill-validation/scenarios/README.md`; update disciplined-development totals to 9 total / 1 ported / 8 not ported and overall totals to 105 / 4 / 101.

- [x] Run `git diff --check` and `git status --short`. Confirm no runner, skill, raw-output, bundle, or unrelated change entered the work.

- [x] After successful verification, append the run outcome, move this plan to `plans/completed/`, and update the runner-shape plan link. Run the canonical Markdown-link checker and `git diff --check` against the final layout.

## Done when

- [x] `DD-04` loads with exactly two supplied skill files and its canonical fixture.
- [x] One successful run covers the Task 4 shape and its evidence is recorded.
- [x] Inventory and plan bookkeeping are reconciled with no broader change.

## Run outcome — 2026-08-24

- **Run:** `20260824T215706730Z-dd-04-a19ec172-afb5-4dad-89eb-a56f30627731-7kfhy4fx`; bundle `/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/skilltest-runs/20260824T215706730Z-dd-04-a19ec172-afb5-4dad-89eb-a56f30627731-7kfhy4fx`.
- **Mechanical result:** `COMPLETED`; `infrastructure_error: null`; provider exit `0`; no timeout; duration `17.058s`.
- **Evidence:** configuration `6e697a02b1c58528fbd9130f50528cb699333f95360d6240a99a170caf12c878`; prompt `939a40cfe8fe27025ad8c83230830f000c8db0a67c440af0f42cf21925c9183f`; fixture `90e874878dd0380aca4517b53eedb1f58436f6f3500fb2397517716aa15b986d`; supplied `disciplined-development` skill `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`; supplied `disciplined-research` skill `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`; decoded rubric `275eb747335ff0f5d4b7933d43958332e33215db4a04dd8695c7e3e8327e8466`. Retained inputs and workspace copies match the packaged prompt, fixture, and two supplied skill files. The rubric is absent from subject input and workspace, and `runner.log` records provider return before the configuration snapshot.
- **Observed behavior:** not scored; the retained response is outside this mechanical packaging check.
- **Runner fallout:** none blocking. The fixture and exactly two configured skill files were copied to the expected workspace locations, and retained evidence was sufficient for inspection.
- **Packaging fallout:** none. Prompt, fixture, rubric, and supplied skill bytes match the canonical or packaged sources.
- **Provider fallout:** none blocking. Codex returned `final.txt`, emitted empty stderr, and reported 35,302 input tokens, 24,064 cached input tokens, 672 output tokens, and 195 reasoning-output tokens in raw stdout.
- **Scenario fallout:** none blocking. The provider completed the declared scenario without a runner infrastructure error.
- **Skill-behavior fallout:** not assessed; this run is not a behavioral score or baseline.
