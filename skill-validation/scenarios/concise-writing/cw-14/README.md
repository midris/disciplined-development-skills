# Purpose

Route a pressured supporting-reference edit through the reference-authoring lifecycle and its required validation.

# Inputs

Prompt is the canonical `CW-14` input from `skill-validation/concise-writing.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only to direct the evaluator to read beneath `{{fixture_dir}}` and prefix the writing-skills and test-driven-development paths. Rubric is the canonical evaluator-withheld `CW-14` rubric from the same source. Inputs: `live skills/concise-writing/SKILL.md` -> `{{fixture_dir}}/skills/concise-writing/SKILL.md`; `package-owned Superpowers 6.3.0 writing-skills/SKILL.md` -> `{{fixture_dir}}/skills/writing-skills/SKILL.md`; `package-owned Superpowers 6.3.0 writing-skills testing reference` -> `{{fixture_dir}}/skills/writing-skills/testing-skills-with-subagents.md`; `package-owned Superpowers 6.3.0 test-driven-development/SKILL.md` -> `{{fixture_dir}}/skills/test-driven-development/SKILL.md`.

# Smoke

No schema `"0.2"` result is retained.
