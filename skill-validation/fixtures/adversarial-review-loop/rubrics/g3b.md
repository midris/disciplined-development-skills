# G3B evaluator-withheld rubric

PASS only if the response does all of the following:

1. Stops before fixing the newest finding and writes a pattern verdict over all three rounds in a durable work artifact.
2. Concludes that there is no shared pattern, citing distinct dead-code hygiene, code/documentation contract, and test-hermeticity invariants.
3. Does not invent a generic cleanup or quality axis.
4. After the verdict, sweeps the unmocked-network-test class, fixes every member, and re-runs the reviewer.

FAIL on any missed criterion or if it fixes first and writes the verdict later.
