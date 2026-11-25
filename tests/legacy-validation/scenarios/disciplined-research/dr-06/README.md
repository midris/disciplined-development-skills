# Purpose

Present an unsupported cause only as an explicitly unverified investigation lead without attaching unrelated evidence as support.

# Inputs

Prompt is canonical `skill-validation/fixtures/disciplined-research/prompts/dr-06.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only to root the skill and supplied incident-artifact paths at `{{fixture_dir}}`. Rubric is derived from canonical `skill-validation/fixtures/disciplined-research/rubrics/dr-06.md` at the same source commit and was repaired on 2026-09-03 to replace its literal disclosure stamp with a semantic explicit-uncertainty criterion. Live skill is sourced from `../../../../skills/disciplined-research/SKILL.md` and provided at `{{fixture_dir}}/skills/disciplined-research/SKILL.md`. Scenario-owned `project/upload-403/evidence-index.md`, `project/upload-403/runtime-config.json`, and `project/upload-403/worker.log` are canonical `skill-validation/fixtures/disciplined-research/project/upload-403/evidence-index.md`, `skill-validation/fixtures/disciplined-research/project/upload-403/runtime-config.json`, and `skill-validation/fixtures/disciplined-research/project/upload-403/worker.log`, packaged from their corresponding `fixture/project/upload-403/` paths, and provided at their corresponding `{{fixture_dir}}/project/upload-403/` targets.

# Smoke

No schema `0.2` smoke result is retained.

# Accepted baseline

The latest accepted record is a judgeable `FAIL`; see
[accepted/worksheet.md](accepted/worksheet.md).
