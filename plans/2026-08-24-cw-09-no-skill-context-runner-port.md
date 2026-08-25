# No Skill Context and CW-09 Runner Port Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one explicit no-skill-context configuration shape and smoke-run `CW-09` with only its prompt and three-description fixture.

**Architecture:** Keep the existing primary-skill configuration unchanged. Add a strict alternative root shape selected by `"skill_context": "none"`; in that shape, `skill` and `dependencies` are absent, the provider receives the unchanged prompt and fixture, and the result records the explicit mode.

**Tech Stack:** Python 3.11+, pytest, Markdown, JSON, `skilltest`, Codex CLI.

**Spec:** `plans/completed/specs/2026-08-23-single-run-skill-test-runner-design.md`, `plans/2026-08-24-runner-shape-coverage.md`, `plans/2026-08-24-scenario-porting-roadmap.md`, and `skill-validation/charter/core-contracts.md`.

## Global Constraints

- Keep configuration schema `"0.1"`.
- Preserve the existing root shape exactly. The alternative root shape contains `schema_version`, `id`, `skill_context`, `scenario`, `expected_outcome`, and `execution`, with `skill_context` exactly `"none"` and no `skill` or `dependencies` fields.
- Reject null skill fields, an untagged missing skill or dependencies field, an unsupported `skill_context` value, and any mixture of the two root shapes.
- In no-skill-context mode, copy the fixture normally, supply no skill files or `supplied-skills` directory, and pass the prompt bytes unchanged without the skill preamble.
- Record no-skill-context results with test fields `id`, `skill_context: "none"`, and `scenario`; do not use null skill metadata. Preserve existing result records unchanged.
- Keep the result schema at integer version `1`.
- Add no routing, selection, description parsing, generic mode system, or scenario-ID special case.
- Use canonical scenario source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c` for `CW-09`; preserve its prompt, rubric, and three description files without adaptation.
- Run `CW-09` once with Codex `gpt-5.6-sol` at low effort. Record mechanical evidence only; do not score, rerun, establish a baseline, or fix fallout.
- Do not change providers, skills, methodology, or unrelated validation. Do not commit raw output or the temporary run bundle.
- Any change outside this contract requires separate owner approval.

---

### Task 1: Add the explicit no-skill-context shape

**Files:**

- Modify `skill-validation/runner/src/skilltest/config.py`.
- Modify `skill-validation/runner/src/skilltest/workspace.py`.
- Modify `skill-validation/runner/src/skilltest/results.py`.
- Modify `skill-validation/runner/result.schema.json`.
- Modify `skill-validation/runner/tests/conftest.py`.
- Modify `skill-validation/runner/tests/test_config.py`.
- Modify `skill-validation/runner/tests/test_workspace.py`.
- Modify `skill-validation/runner/tests/test_run.py`.
- Modify `skill-validation/runner/README.md`.
- Modify `plans/completed/specs/2026-08-23-single-run-skill-test-runner-design.md`.

- [ ] Add `test_load_config_accepts_explicit_no_skill_context` for the exact alternative root shape. Run it and confirm RED because the loader currently requires `skill` and `dependencies`.

- [ ] Add `test_load_config_rejects_ambiguous_skill_context_shapes` covering the four rejected forms named in Global Constraints. Run it and confirm RED where the current loader does not yet recognize the explicit shape.

- [ ] Make `TestConfig.skill` optional only for the tagged alternative, retain empty dependencies internally for that shape, and update preflight iteration without changing normal declarations. Run `uv run pytest -q tests/test_config.py` and require GREEN.

- [ ] Add `test_prepare_workspace_preserves_prompt_for_no_skill_context`. Require an exact fixture-only workspace, no `supplied-skills`, no retained skill files, and subject input identical to the prompt. Confirm RED, implement only that conditional preparation path, then run `uv run pytest -q tests/test_workspace.py` and require GREEN.

- [ ] Add `test_run_once_persists_no_skill_context_result`. Require provider input equal to the prompt and the explicit three-field test record. Confirm RED, add the matching result construction and schema alternative, then run `uv run pytest -q tests/test_run.py` and require GREEN.

- [ ] Document both exact configuration shapes, fixture-only workspace behavior, unchanged prompt transport, and the two result-record shapes in the runner README and completed runner design.

- [ ] Run `uv run pytest -q` from `skill-validation/runner`, then commit only the runner contract, tests, and contract documentation.

### Task 2: Package and smoke-run `CW-09`

**Files:**

- Create `skill-validation/scenarios/concise-writing/cw-09/prompt.md`.
- Create `skill-validation/scenarios/concise-writing/cw-09/fixture/descriptions/adversarial-review-loop.txt`.
- Create `skill-validation/scenarios/concise-writing/cw-09/fixture/descriptions/concise-writing.txt`.
- Create `skill-validation/scenarios/concise-writing/cw-09/fixture/descriptions/superpowers-writing-skills.txt`.
- Create `skill-validation/scenarios/concise-writing/cw-09/test.json`.
- Update `skill-validation/scenarios/README.md` and `plans/2026-08-24-scenario-porting-roadmap.md`.
- Complete and move this plan and `plans/2026-08-24-runner-shape-coverage.md` to `plans/completed/`.

- [ ] Verify canonical prompt SHA-256 `e7adf2a882598587029a14ba737da4a4aa87c1c5f57106f767f04c6e78584bf9`, rubric SHA-256 `efbc83413fa8b192f39b2716ab5985d1bb8fd3664c8de54679fcc5406dab4dcd`, description hashes `38843f7718501f52116bfd4f95a6640cb16b560851767df540c808a1ed18cefa`, `586a741a9cb28746078ca1b5f7aa570a4e621a5d2cdecac16e31bd6d2c82fd62`, and `5504b0825ec458aa8c20e9a55c6a932b36849e261a97aaf98af366e19a937154`, plus canonical description manifest `49c129fea1a0782f6daaf9908e134bf92ea684c031f52b12d520ebe3aac7b2a3`.

- [ ] Materialize the canonical prompt and three description files unchanged. Create `test.json` with schema `"0.1"`; IDs `cw-09`; `skill_context: "none"`; fixture `fixture`; exact rubric as `expected_outcome`; and Codex `gpt-5.6-sol` at low effort.

- [ ] Load the configuration without invoking a provider. Confirm the explicit mode, unchanged hashes, no declared or packaged skill files, fixture paths, unchanged subject input, and withheld rubric. Run the full runner suite.

- [ ] Obtain approval to export only the prompt and three description files, then run exactly once from `skill-validation/runner`:

  `uv run skilltest run ../scenarios/concise-writing/cw-09/test.json`

- [ ] Confirm `COMPLETED`, `infrastructure_error: null`, no provider-visible skill files or `supplied-skills`, the three unchanged description files, subject input equal to the prompt, and a withheld rubric. Record mechanical fallout only; if incomplete, record it and stop.

- [ ] Mark `CW-09` ported in `skill-validation/scenarios/README.md`; update concise-writing totals to 17 total / 1 ported / 16 not ported and overall totals to 105 / 6 / 99.

- [ ] Run the full runner suite, `git diff --check`, and `git status --short`. Confirm no skill, raw-output, bundle, methodology, or unrelated change entered the work.

- [ ] After successful verification, append the run outcome and mark runner-shape coverage complete. Move this plan and the runner-shape plan to `plans/completed/`; point this plan's Spec at the completed runner-shape plan and rewrite that plan's implementation-plan links relative to its final directory.

- [ ] Update the roadmap to mark runner-shape coverage complete and catalog migration current. Run the canonical Markdown-link checker and `git diff --check` against the final layout.

## Done When

- [ ] An explicit tag, not nulls or omission, distinguishes the no-skill-context configuration.
- [ ] Existing configurations and result records remain unchanged.
- [ ] One successful `CW-09` run covers description-only routing with only its canonical prompt and fixture.
- [ ] Inventory and plan bookkeeping are reconciled with no broader work.
