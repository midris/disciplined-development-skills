# Purpose

Use a later controlling first-party addendum to disconfirm a supplied museum-procurement deadline.

# Inputs

Prompt is the canonical fenced evaluator input beneath `DR-02 — isolated museum procurement deadline` in `skill-validation/disciplined-research.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only to root the skill and supplied source paths at `{{fixture_dir}}`. Rubric is the active catalog table's evaluator-withheld DR-02 rubric cell plus one trailing LF from the same source record. Live skill is sourced from `../../../../skills/disciplined-research/SKILL.md` and provided at `{{fixture_dir}}/skills/disciplined-research/SKILL.md`. Scenario-owned `sources/city-museum-rfp.md`, `sources/city-museum-addendum-2.md`, and `sources/friends-newsletter.md` are canonical inline fixtures from `skill-validation/disciplined-research.md#dr-02-fixture`, packaged from `fixture/sources/city-museum-rfp.md`, `fixture/sources/city-museum-addendum-2.md`, and `fixture/sources/friends-newsletter.md`, and provided at their corresponding `{{fixture_dir}}/sources/` targets.

# Smoke

No schema `0.2` result is retained.
