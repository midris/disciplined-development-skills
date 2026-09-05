# Purpose

Select the due parent modes, gates, principles, artifacts, outcomes, blocked transitions, and owner seams across eight independent vignettes.

# Inputs

- Prompt: canonical `skill-validation/fixtures/disciplined-development/prompts/dd-01.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by the plan-listed literal substitutions and retained with SHA-256 `e13a4d90df7360f3a8b949e7b7b5208dc22f1a942294271f4de53898ff6bb0a2`.
- Rubric: exact canonical `skill-validation/fixtures/disciplined-development/rubrics/dd-01.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `bb994c3b2e4adfc4feead9220ab9df89d53f5a74d1efa0e6bffbf733c7c0c9bb` and withheld from provider inputs.
- Live skill: `../../../../skills/disciplined-development/SKILL.md` is provided at `{{fixture_dir}}/skills/disciplined-development/SKILL.md`.

# Smoke

No schema `0.2` result is retained.

# Accepted baseline

The latest accepted baseline is a behavioral `FAIL` from `codex` / `gpt-5.6-sol` / `high`, accepted on 2026-09-04. Task fidelity passes, while the accepted worksheet records parent-behavior failures in vignettes A, B, and H and keeps terminology notes advisory.

Retained artifacts: `accepted/worksheet.md`, `accepted/result.json`, and `accepted/final.txt`. No evidence files were emitted.
