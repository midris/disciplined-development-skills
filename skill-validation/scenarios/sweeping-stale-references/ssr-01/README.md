# Purpose

Exercise an end-to-end load-bearing rename with complete discovery, rationale-preserving reconciliation, durable sweep evidence, and verification.

# Inputs

Prompt adapted from the canonical `SSR-01` fenced block by replacing `The complete nine-skill local bundle is installed.` with ``The complete nine-skill local bundle is supplied beneath `{{fixture_dir}}/skills`.``; rooting every canonical skill path from `skills/` at `{{fixture_dir}}/skills/`; and replacing `Inspect the supplied project files, then` with ``Inspect `{{fixture_dir}}/project/src/session.py` and `{{fixture_dir}}/project/docs/session-policy.md`, then``. Rubric is the active catalog `SSR-01` evaluator-withheld rubric cell. Live inputs are supplied from the repository at `skills/adversarial-review-loop/SKILL.md`, `skills/adversarial-review/SKILL.md`, `skills/concise-writing/SKILL.md`, `skills/disciplined-development/SKILL.md`, `skills/disciplined-research/SKILL.md`, `skills/dispatching-development-subagents/SKILL.md`, `skills/lean-plan-writing/SKILL.md`, `skills/sweeping-stale-references/SKILL.md`, and `skills/writing-explicit-rationale/SKILL.md`, each provided at the corresponding `{{fixture_dir}}/skills/` target. Canonical fenced `SSR-01` fixture files `project/src/session.py` and `project/docs/session-policy.md` are supplied at `{{fixture_dir}}/project/src/session.py` and `{{fixture_dir}}/project/docs/session-policy.md`.

# Smoke

Runner status: `COMPLETED`. Retained result: [smoke-result.json](smoke-result.json).
