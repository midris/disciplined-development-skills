# Purpose

Split oversized independently deployable work at qualitative review boundaries while preserving dependency order.

# Inputs

Prompt is the canonical `LP-07 — oversized program boundary` input from `skill-validation/lean-plan-writing.md`, adapted so supplied skill paths and `context/oversized-spec.md` use `{{fixture_dir}}`. Rubric is the canonical evaluator-withheld LP-07 rubric from the same source. Live `skills/lean-plan-writing/SKILL.md` is supplied at `{{fixture_dir}}/skills/lean-plan-writing/SKILL.md`. Superpowers 6.3.0 `writing-plans/SKILL.md` is supplied from `/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/writing-plans/SKILL.md` at `{{fixture_dir}}/skills/writing-plans/SKILL.md`. Canonical fixture `context/oversized-spec.md` is supplied from `skill-validation/lean-plan-writing.md#lp-07-fixture` at `{{fixture_dir}}/context/oversized-spec.md`.

# Smoke

No schema `"0.2"` result is retained.

# Accepted baseline

The latest accepted baseline is a `FAIL` from `codex` / `gpt-5.6-sol` / `high`, accepted on 2026-09-04. The split, dependency order, and named green gates pass, and the accepted worksheet records a separate `superpowers:writing-plans` composition-owner `PASS`; the primary verdict fails because the response repeats the fixture's numeric commit/diff estimates despite the qualitative-boundary rubric.

Retained artifacts: `accepted/worksheet.md`, `accepted/result.json`, and `accepted/final.txt`. No evidence files were emitted.
