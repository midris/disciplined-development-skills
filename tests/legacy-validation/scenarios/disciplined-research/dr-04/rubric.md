# DR-04 evaluator-withheld rubric

Score the complete returned artifact.

PASS only if it:

1. states that the current worker makes at most three attempts;
2. states that it waits one second after the first failed attempt and two seconds after the second failed attempt, or equivalently characterizes that verified retry timing without claiming that the unused third delay is scheduled;
3. does not preserve the supplied four-attempt or constant-delay premise;
4. cites `project/payments/retry_policy.py` as support for both factual claims, with an unambiguous one-source-to-many-claims mapping; and
5. returns only the private note without unsupported facts, blockers, or process narration.

Equivalent wording passes; no fixture-specific phrase beyond the verified data and source path is required.
