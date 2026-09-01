# Purpose

Treat recurrence after a one-line fix as evidence of an incomplete class sweep before re-review.

# Inputs

Prompt and rubric are the canonical `cs.md` files under `skill-validation/fixtures/adversarial-review-loop/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`. The prompt is adapted only by rooting `skills/adversarial-review-loop/SKILL.md` at `{{fixture_dir}}`. The current repository skill is sourced from `../../../../skills/adversarial-review-loop/SKILL.md` and provided at `{{fixture_dir}}/skills/adversarial-review-loop/SKILL.md`. The rubric remains evaluator-withheld.

# Smoke

No schema `0.2` result is retained.
