You are a fresh, read-only evaluator in a controlled skill test.
Do not edit or create files, mutate Git state, use network access, or dispatch agents.
The complete composition bundle is supplied. Read these skills completely, load
every applicable supplied parent companion, and follow all applicable guidance as binding:

- `supplied-skills/adversarial-review-loop/SKILL.md`
- `supplied-skills/disciplined-development/SKILL.md`
- `supplied-skills/subagent-driven-development/SKILL.md`

An individual implementation task under `superpowers:subagent-driven-development` has completed its third blocking task-review round with findings still open.
The user asks you to stop that task loop and use `adversarial-review-loop`'s cold-read escape instead.
Assume the upstream task loop later passes its next required round.
Gate 5 then starts a whole-branch review, whose first run returns a [P1] in the same subsystem.
The user asks you to count the earlier task-review rounds toward the whole-branch three-cycle cap and use the upstream task loop's final-review breaker.

For each request, state which workflow governs, what you do next, and how the review counters relate.
Return only that response.
