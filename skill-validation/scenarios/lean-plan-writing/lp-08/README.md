# Purpose

Keep a small genuinely coupled rename in one atomic branch and merge.

# Inputs

Prompt is the canonical `LP-08 — coupled change boundary` input from `skill-validation/lean-plan-writing.md`, adapted so supplied skill paths and `context/coupled-spec.md` use `{{fixture_dir}}`. Rubric is the canonical evaluator-withheld LP-08 rubric from the same source. Live `skills/lean-plan-writing/SKILL.md` is supplied at `{{fixture_dir}}/skills/lean-plan-writing/SKILL.md`. Superpowers 6.3.0 `writing-plans/SKILL.md` is supplied from `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans/SKILL.md` at `{{fixture_dir}}/skills/writing-plans/SKILL.md`. Canonical fixture `context/coupled-spec.md` is supplied from `skill-validation/lean-plan-writing.md#lp-08-fixture` at `{{fixture_dir}}/context/coupled-spec.md`.

# Smoke

No schema `"0.2"` result is retained.

# Accepted baseline

The latest accepted baseline is a `PASS` from `codex` / `gpt-5.6-sol` / `high`, accepted on 2026-09-04. The accepted worksheet records a separate `superpowers:writing-plans` composition-owner `PASS` and confirms the one-branch/one-PR result for the tightly coupled three-file rename.

Retained artifacts: `accepted/worksheet.md`, `accepted/result.json`, and `accepted/final.txt`. No evidence files were emitted.
