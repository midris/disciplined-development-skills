# Purpose

Apply a small direct plan descope while keeping selected scope, cause, accepted impact, and adjacent rationale intact.

# Inputs

Prompt adapted from the canonical `WER-01` fenced block by replacing `The complete nine-skill local bundle is installed.` with `The complete nine-skill local bundle is supplied beneath \`{{fixture_dir}}/skills\`.` and rooting every canonical skill path from `skills/` at `{{fixture_dir}}/skills/`. Rubric is the active catalog `WER-01` evaluator-withheld rubric cell. Live inputs are supplied from the repository at `skills/adversarial-review-loop/SKILL.md`, `skills/adversarial-review/SKILL.md`, `skills/concise-writing/SKILL.md`, `skills/disciplined-development/SKILL.md`, `skills/disciplined-research/SKILL.md`, `skills/dispatching-development-subagents/SKILL.md`, `skills/lean-plan-writing/SKILL.md`, `skills/sweeping-stale-references/SKILL.md`, and `skills/writing-explicit-rationale/SKILL.md`, each provided at the corresponding `{{fixture_dir}}/skills/` target.

# Smoke

No schema `"0.2"` result is retained.
