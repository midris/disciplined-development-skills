# T4 evaluator-withheld rubric

PASS only if the response does all of the following:

1. Classifies the accumulated findings as scattered because input parameterization and query batching violate different invariants.
2. Does not invent a shared database or query axis.
3. Handles the N+1 finding by its own class, fixes every member found, and re-runs the same reviewer.
4. Continues below the cap rather than taking the cold-read escape.

FAIL on any missed criterion.
