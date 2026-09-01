# Purpose

Keep a proven one-member class bounded and still require the safe reviewer re-run.

# Inputs

Prompt and rubric are the canonical `t2.md` files under `skill-validation/fixtures/adversarial-review-loop/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`. The prompt is adapted only by rooting the nine-skill directory at `{{fixture_dir}}` and making the binding loop-skill read explicit. The nine current repository skills are sourced individually from `../../../../skills/<skill-id>/SKILL.md` and provided at their corresponding `{{fixture_dir}}/skills/<skill-id>/SKILL.md` targets. The rubric remains evaluator-withheld.

# Smoke

No schema `0.2` result is retained.
