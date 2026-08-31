# Purpose

Apply acquire, verify, and source-disclosure rules to a private scratch note while mapping one source to multiple claims.

# Inputs

Prompt is canonical `skill-validation/fixtures/disciplined-research/prompts/dr-04.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only to root the skill and add the supplied project path at `{{fixture_dir}}`. Rubric is canonical `skill-validation/fixtures/disciplined-research/rubrics/dr-04.md` from the same source commit. Live skill is sourced from `../../../../skills/disciplined-research/SKILL.md` and provided at `{{fixture_dir}}/skills/disciplined-research/SKILL.md`. Scenario-owned `project/payments/retry_policy.py` is canonical `skill-validation/fixtures/disciplined-research/project/payments/retry_policy.py`, packaged from `fixture/project/payments/retry_policy.py`, and provided at `{{fixture_dir}}/project/payments/retry_policy.py`.

# Smoke

No schema `0.2` result is retained.
