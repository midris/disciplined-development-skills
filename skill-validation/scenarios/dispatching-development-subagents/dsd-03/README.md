# Purpose

Require commit-by-commit inspection and disposition of an out-of-scope commit before integration.

# Inputs

- Prompt: canonical `skill-validation/fixtures/dispatching-development-subagents/prompts/dsd-03.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only as follows: prefixed the backticked dispatch skill path with `{{fixture_dir}}/`. The adapted prompt is retained with SHA-256 `e0e07f5e26930a58a6741c3f1e3ad900f2bcc362ff4c688ff554b8ccbd040e7b`.
- Rubric: exact canonical `skill-validation/fixtures/dispatching-development-subagents/rubrics/dsd-03.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `c7b3fbf6eb092f8919cd8ec1eaa278af7f736f4fa1522bbb8e56bc536aab6570` and withheld from provider inputs.
- Live repository file: `../../../../skills/dispatching-development-subagents/SKILL.md` is provided at `{{fixture_dir}}/skills/dispatching-development-subagents/SKILL.md`.

# Smoke

No schema `0.2` result is retained.
