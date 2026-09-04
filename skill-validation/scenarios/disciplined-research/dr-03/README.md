# Purpose

Verify the project's declared dependency and upstream stable version separately and correct a cross-domain claim.

# Inputs

Prompt is derived from the canonical fenced evaluator input beneath `DR-03 — cross-domain version verification` in `skill-validation/disciplined-research.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c` and adapted to root the skill and supplied project and source paths at `{{fixture_dir}}`. On 2026-09-03, its unsupported installed-version wording was repaired to ask for the dependency version declared in `package.json`. Rubric is derived from the active catalog table's evaluator-withheld DR-03 rubric cell in the same source record and was repaired on the same date to assess the declared dependency version rather than installed state. Live skill is sourced from `../../../../skills/disciplined-research/SKILL.md` and provided at `{{fixture_dir}}/skills/disciplined-research/SKILL.md`. Scenario-owned `project/package.json`, `sources/orbital-release-notes.md`, and `sources/orbital-maintainer-blog.md` are canonical inline fixtures from `skill-validation/disciplined-research.md#dr-03-fixture`, packaged from `fixture/project/package.json`, `fixture/sources/orbital-release-notes.md`, and `fixture/sources/orbital-maintainer-blog.md`, and provided at their corresponding `{{fixture_dir}}/project/` and `{{fixture_dir}}/sources/` targets.

# Smoke

No schema `0.2` smoke result is retained.

# Accepted baseline

The latest accepted record is a judgeable `FAIL`; see
[accepted/worksheet.md](accepted/worksheet.md).
