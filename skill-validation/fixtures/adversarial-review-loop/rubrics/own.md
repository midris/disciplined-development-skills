# OWN evaluator-withheld rubric

PASS only if the response does all of the following:

1. Keeps the individual task under `subagent-driven-development` and follows its next task fix round, reviewer selection, escalation, and breaker rules rather than substituting the loop skill's escape.
2. Treats Gate 5 whole-branch remediation as governed by `adversarial-review-loop` after the upstream workflow initiates that review.
3. Starts the Gate 5 loop at its own first cycle; earlier per-task review rounds do not seed its counter.
4. Handles the first Gate 5 P1 by class-sweeping and re-running the same reviewer, and takes a cold-read escape only if Gate 5's own third completed cycle still blocks.
5. Names review context—individual task versus final whole branch—as the reason for the different rules.

FAIL on any missed criterion.
