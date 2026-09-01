# Purpose

Resist promotion to orchestrator authority, nested reviewers, and parent-gate action.

# Inputs

- Prompt: canonical `skill-validation/fixtures/dispatching-development-subagents/prompts/dsd-09.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only as follows: replaced the direct dispatch invocation and parent-and-hook instruction with the plan-listed fixture reads. The adapted prompt is retained with SHA-256 `81beafb72ff9e9e89bdb76a1c9a24b3e1cdf5a26ab84b7ae80c16113749f4b87`.
- Rubric: exact canonical `skill-validation/fixtures/dispatching-development-subagents/rubrics/dsd-09.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `87af699d793adfda35cf2a74114e632893bd668cc66aa4c5c14018469da5481c` and withheld from provider inputs.
- Live repository file: `../../../../skills/dispatching-development-subagents/SKILL.md` is provided at `{{fixture_dir}}/skills/dispatching-development-subagents/SKILL.md`.
- Live repository file: `../../../../skills/disciplined-development/SKILL.md` is provided at `{{fixture_dir}}/skills/disciplined-development/SKILL.md`.
- Live repository file: `../../../../skills/disciplined-development/hooks/review_nudge.py` is provided at `{{fixture_dir}}/skills/disciplined-development/hooks/review_nudge.py`.
- Pinned dependency: installed Superpowers 6.3.0 file `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/subagent-driven-development/SKILL.md`, packaged as `fixture/skills/superpowers/subagent-driven-development/SKILL.md`, provided at `{{fixture_dir}}/skills/superpowers/subagent-driven-development/SKILL.md`, SHA-256 `8dd1b8e698edec3700c6d89517dbe96febd3bacd3f6ea21c1a3569c62ea104b5`.

# Smoke

No schema `0.2` result is retained.
