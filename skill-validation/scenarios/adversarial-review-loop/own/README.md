# Purpose

Preserve individual-task and whole-branch owners, rules, and counters while grounding factual workflow claims.

# Inputs

Prompt and rubric are the canonical `own.md` files under `skill-validation/fixtures/adversarial-review-loop/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`. The prompt is adapted only by rooting its three named skill paths at `{{fixture_dir}}`; the canonical parent composition continues to supply `disciplined-research` without naming its path. Current repository skills `adversarial-review-loop`, `disciplined-development`, and `disciplined-research` are sourced individually from `../../../../skills/<skill-id>/SKILL.md` and provided at their corresponding `{{fixture_dir}}/skills/<skill-id>/SKILL.md` targets. Superpowers 6.3.0 `subagent-driven-development/SKILL.md` is packaged at `fixture/skills/superpowers/subagent-driven-development/SKILL.md`, provided at `{{fixture_dir}}/skills/superpowers/subagent-driven-development/SKILL.md`, and pinned to SHA-256 `8dd1b8e698edec3700c6d89517dbe96febd3bacd3f6ea21c1a3569c62ea104b5`. The rubric remains evaluator-withheld.

# Smoke

No schema `0.2` result is retained.
