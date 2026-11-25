# Purpose

Remove unsupported elaboration while preserving the authoritative archive facts.

# Inputs

Prompt is the canonical `CW-05` input from `skill-validation/concise-writing.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only to prefix the concise-writing path with `{{fixture_dir}}/`. Rubric is the canonical evaluator-withheld `CW-05` rubric from the same source. Inputs: `live skills/concise-writing/SKILL.md` -> `{{fixture_dir}}/skills/concise-writing/SKILL.md`.

# Smoke

No schema `"0.2"` result is retained.
