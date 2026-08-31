# Purpose

Verify project and upstream version state separately and correct a cross-domain claim.

# Inputs

Prompt is the canonical fenced evaluator input beneath `DR-03 — cross-domain version verification` in `skill-validation/disciplined-research.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only to root the skill and supplied project and source paths at `{{fixture_dir}}`. Rubric is the active catalog table's evaluator-withheld DR-03 rubric cell plus one trailing LF from the same source record. Live skill is sourced from `../../../../skills/disciplined-research/SKILL.md` and provided at `{{fixture_dir}}/skills/disciplined-research/SKILL.md`. Scenario-owned `project/package.json`, `sources/orbital-release-notes.md`, and `sources/orbital-maintainer-blog.md` are canonical inline fixtures from `skill-validation/disciplined-research.md#dr-03-fixture`, packaged from `fixture/project/package.json`, `fixture/sources/orbital-release-notes.md`, and `fixture/sources/orbital-maintainer-blog.md`, and provided at their corresponding `{{fixture_dir}}/project/` and `{{fixture_dir}}/sources/` targets.

# Smoke

No schema `0.2` result is retained.
