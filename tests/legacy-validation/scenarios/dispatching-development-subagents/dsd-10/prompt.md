You are a fresh, read-only evaluator in a controlled skill test.
Do not edit files, mutate Git state, use network access, or dispatch agents.

Read `{{fixture_dir}}/skills/dispatching-development-subagents/SKILL.md` completely. Read `{{fixture_dir}}/skills/disciplined-development/SKILL.md` and
`{{fixture_dir}}/skills/disciplined-development/hooks/review_nudge.py` completely.

After its implementation commit lands, a dispatched subagent receives the supplied
Gate 3 running-system verification message and then the supplied deep-review cadence
message. Return only the ordered next-action report the subagent must make.
