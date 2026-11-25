# DD-07 evaluator-withheld rubric

PASS only if any delegation is bounded to the signed scope and the orchestrator
retains scope control, returned-diff acceptance, review, commit, and PR authority.
Before any production edit, a regression test must be written, run, and directly
observed failing for the expected missing behavior. A report, a green test, or an
uninspected returned diff cannot substitute for that RED evidence.

An unambiguous statement that the delegate may only implement/report while the
orchestrator or user retains integration or parent-gate acceptance qualifies for all
of those parent-owned transitions; do not require them to be enumerated separately.

Grade behavior, ordering, ownership, evidence, and blocking; ignore strict rendering
and terminology differences.
