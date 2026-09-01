# Purpose

Partition mixed findings without paraphrasing, unsafe batching, or invented rationale.

# Inputs

- Prompt: canonical `skill-validation/fixtures/dispatching-development-subagents/prompts/dsd-04.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only as follows: prefixed the backticked dispatch skill path with `{{fixture_dir}}/`. The adapted prompt is retained with SHA-256 `9637da4d3e05acf47034ff063c5e41193ccb0192fc2f31ed6bfbe2705ed8993c`.
- Rubric: exact canonical `skill-validation/fixtures/dispatching-development-subagents/rubrics/dsd-04.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `dc29adc91e29ca32bae2fe3a8df3ba1a7cac3293add9eec2e77b7aeecaebd25b` and withheld from provider inputs.
- Live repository file: `../../../../skills/dispatching-development-subagents/SKILL.md` is provided at `{{fixture_dir}}/skills/dispatching-development-subagents/SKILL.md`.

# Smoke

No schema `0.2` result is retained.
