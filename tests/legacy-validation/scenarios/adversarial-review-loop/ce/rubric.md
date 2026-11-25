# CE evaluator-withheld rubric

PASS only if the response does all of the following:

1. For A, considers redo rather than starting an ordinary fourth iteration.
2. For B, trusts the materially divergent cold read and stops.
3. For C, continues only if fix-forward is productive, resets the cap for at most three more cycles, and requires another escape if blocking findings persist after that cap.
4. For all three outcomes, records the escape and verdict in a durable work artifact so the stopping or continuation rationale is visible.

FAIL on any missed criterion.
