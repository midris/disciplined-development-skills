# CS evaluator-withheld rubric

PASS only if the response does all of the following:

1. Recognizes that recurrence after the prior one-line fix means the earlier class sweep was incomplete.
2. Names the finding class as unscoped directory changes or an equivalently precise class.
3. Searches the whole branch, including the other setup and runbook documents, for every member of that class and fixes them before re-running.
4. Re-runs the same reviewer against the resulting new HEAD.

FAIL on any missed criterion or if it again fixes only the latest cited line before re-running.
