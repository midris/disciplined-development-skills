# Purpose

Keep implementation bodies and copyable templates out of a detailed parser task while preserving exact behavior through a complete tricky-case table.

# Inputs

Prompt is the canonical `LP-02 — parser table without implementation` input from `skill-validation/lean-plan-writing.md`, adapted so supplied skill paths use `{{fixture_dir}}/skills/`. Rubric is the canonical evaluator-withheld LP-02 rubric from the same source. Live `skills/lean-plan-writing/SKILL.md` is supplied at `{{fixture_dir}}/skills/lean-plan-writing/SKILL.md`. Superpowers 6.3.0 `writing-plans/SKILL.md` is supplied from `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans/SKILL.md` at `{{fixture_dir}}/skills/writing-plans/SKILL.md`. Fixed parser semantics remain inline in the prompt.

# Smoke

No schema `"0.2"` result is retained.
