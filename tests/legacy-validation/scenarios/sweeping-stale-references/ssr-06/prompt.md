You are a fresh, read-only skill evaluator.
The complete nine-skill local bundle is supplied beneath `{{fixture_dir}}/skills`.
Do not edit files, mutate Git state, inspect outside the supplied bundle, or dispatch
agents. Invoke `sweeping-stale-references`: read `{{fixture_dir}}/skills/sweeping-stale-references/SKILL.md` completely and follow it as
binding guidance.

Read `{{fixture_dir}}/project/src/session.py` and `{{fixture_dir}}/project/docs/session-policy.md`.

Rename `TOKEN_TTL_MINUTES` to `SESSION_TTL_MINUTES` and its obvious prose form to
`session TTL` in the supplied project. Inspect both project files. Return only a
concise `References swept:` artifact that inventories and accounts for every required
replacement, followed by `Verification:`.
