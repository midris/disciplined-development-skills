# Purpose

Produce one bounded development-subagent prompt with grounded scope, identity, authority, disclosure, and handoff requirements.

# Inputs

- Prompt: canonical `skill-validation/fixtures/dispatching-development-subagents/prompts/dsd-01.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only as follows: prefixed every backticked `skills/` and `project/dsd-01` path with `{{fixture_dir}}/`. The adapted prompt is retained with SHA-256 `6eedfdb6b17fce5af790c0fe9cd7dc967426ea6f911c4086a9ed1ade718bce09`.
- Rubric: exact canonical `skill-validation/fixtures/dispatching-development-subagents/rubrics/dsd-01.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `acf3ade4ab145d91709ccbce6315fbb301bcb86cc8c5648932d839e0d98b13d0` and withheld from provider inputs.
- Live repository file: `../../../../skills/dispatching-development-subagents/SKILL.md` is provided at `{{fixture_dir}}/skills/dispatching-development-subagents/SKILL.md`.
- Live repository file: `../../../../skills/adversarial-review-loop/SKILL.md` is provided at `{{fixture_dir}}/skills/adversarial-review-loop/SKILL.md`.
- Live repository file: `../../../../skills/adversarial-review/SKILL.md` is provided at `{{fixture_dir}}/skills/adversarial-review/SKILL.md`.
- Live repository file: `../../../../skills/concise-writing/SKILL.md` is provided at `{{fixture_dir}}/skills/concise-writing/SKILL.md`.
- Live repository file: `../../../../skills/disciplined-development/SKILL.md` is provided at `{{fixture_dir}}/skills/disciplined-development/SKILL.md`.
- Live repository file: `../../../../skills/disciplined-research/SKILL.md` is provided at `{{fixture_dir}}/skills/disciplined-research/SKILL.md`.
- Live repository file: `../../../../skills/lean-plan-writing/SKILL.md` is provided at `{{fixture_dir}}/skills/lean-plan-writing/SKILL.md`.
- Live repository file: `../../../../skills/sweeping-stale-references/SKILL.md` is provided at `{{fixture_dir}}/skills/sweeping-stale-references/SKILL.md`.
- Live repository file: `../../../../skills/writing-explicit-rationale/SKILL.md` is provided at `{{fixture_dir}}/skills/writing-explicit-rationale/SKILL.md`.
- Scenario-owned file: canonical `skill-validation/fixtures/dispatching-development-subagents/project/dsd-01/AGENTS.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/project/dsd-01/AGENTS.md`, provided at `{{fixture_dir}}/project/dsd-01/AGENTS.md`, SHA-256 `567ded3276c9ecaabbfea7f34229a528652476cf2cfe1f7a81573b4577c866fe`.
- Scenario-owned file: canonical `skill-validation/fixtures/dispatching-development-subagents/project/dsd-01/plans/pagination.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/project/dsd-01/plans/pagination.md`, provided at `{{fixture_dir}}/project/dsd-01/plans/pagination.md`, SHA-256 `e18ce80cae7233db26ed903116fee411162433d2ef82cfbcfa574835efcf35c4`.
- Scenario-owned file: canonical `skill-validation/fixtures/dispatching-development-subagents/project/dsd-01/reviews/pagination.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/project/dsd-01/reviews/pagination.md`, provided at `{{fixture_dir}}/project/dsd-01/reviews/pagination.md`, SHA-256 `884e1ee1a6c7109134144ff3ab1cddf6bd9bd522a249373e4ce7e1571b77a80a`.

# Smoke

No schema `0.2` result is retained.
