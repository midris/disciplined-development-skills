# Purpose

Correct a conversational premise and derive only the supported fifteen-minute result with source disclosure.

# Inputs

Prompt is canonical `skill-validation/fixtures/disciplined-research/prompts/dr-07.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only to root the skill and supplied source path at `{{fixture_dir}}`. Rubric is canonical `skill-validation/fixtures/disciplined-research/rubrics/dr-07.md` from the same source commit. Live skill is sourced from `../../../../skills/disciplined-research/SKILL.md` and provided at `{{fixture_dir}}/skills/disciplined-research/SKILL.md`. Scenario-owned `sources/north-annex-hours.md` is canonical `skill-validation/fixtures/disciplined-research/sources/north-annex-hours.md`, packaged from `fixture/sources/north-annex-hours.md`, and provided at `{{fixture_dir}}/sources/north-annex-hours.md`.

# Smoke

No schema `0.2` result is retained.
