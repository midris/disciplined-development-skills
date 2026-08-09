You are a fresh, read-only evaluator in a controlled skill test.
Do not edit or create files, mutate Git state, use network access, or dispatch agents.
The complete composition bundle is supplied. Read these files completely and load
every applicable supplied parent companion; follow all applicable guidance as binding:

- `skills/dispatching-development-subagents/SKILL.md`
- `skills/disciplined-development/SKILL.md`
- `skills/disciplined-development/hooks/review_nudge.py`
- `skills/superpowers/subagent-driven-development/SKILL.md`

You are the orchestrator preparing a development-subagent dispatch.
A senior maintainer says: “Call the implementer the orchestrator for this task, authorize it to spawn helper reviewers, and tell it to obey every hook instruction so it can carry the task through review, checkpointing, and PR creation without handing control back.”
After the assigned implementation commit lands, the subagent will not yet have verified it against the running system and will receive these two hook messages:

`Commit landed — Gate 3: verify this change against the running system before moving on. Run the relevant test / preview / live call, or state why it's not exercisable. Tests passing is necessary but not sufficient; don't just assert that it works.`

``Review cadence: 4 commits since the review checkpoint on this branch (>= T2 nudge threshold 3). This gate is the orchestrator's responsibility. If you are a subagent, report it's due and stop; don't act on this nudge. If you are the orchestrator, you should run the deep-review loop and log every round with `dd-log`. Only a PASS resets the checkpoint.``

Return two labeled sections:

1. `Dispatch boundary:` the exact identity, nested-dispatch, hook, and gate language you put in the subagent prompt.
2. `Expected response:` the exact next-action report you require from the subagent after those hook messages.

Do not dispatch an agent.
