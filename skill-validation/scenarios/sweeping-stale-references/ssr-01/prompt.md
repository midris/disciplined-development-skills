You are a fresh, read-only skill evaluator.
The complete nine-skill local bundle is supplied beneath `{{fixture_dir}}/skills`. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Directly invoke `sweeping-stale-references`: read `{{fixture_dir}}/skills/sweeping-stale-references/SKILL.md` completely and follow it as binding guidance.

Rename the load-bearing session setting `TOKEN_TTL_MINUTES` to `SESSION_TTL_MINUTES` and update its obvious prose form in the supplied project.
Inspect `{{fixture_dir}}/project/src/session.py` and `{{fixture_dir}}/project/docs/session-policy.md`, then return only the commit-body evidence for this rename, ending with `Verification:`.
In `Verification:`, include only project-level evidence; do not mention evaluator or harness constraints, read-only status, whether files changed, or checks not run.
