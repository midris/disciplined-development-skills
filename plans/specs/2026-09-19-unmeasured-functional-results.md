# Unmeasured functional outcomes

Status: implemented and reviewed; offline tests verify the approved reporting extension.

Add execution-result version 2, preserving version 1's schema, template and existing records unchanged.
Version 2 requires at least one assessed criterion, permits procedural-only cases and requires `functional_result: "not measured"` exactly when no functional criterion applies.
Functional failure/unknown/pass derivation stays unchanged when functional criteria exist.
The applicable pinned case definition still determines exact criterion coverage and dimensions; omitted functional judgments cannot become not measured.
No overall pass is derived for a procedural-only diagnostic.

Add assessment version 2 with an explicit Not measured aggregate column.
Count only valid setups in outcome aggregates; retain invalid setup, unresolved setup, unassessed and unattempted coverage separately.
Functional success denominators remain met + not met + insufficient evidence; not measured is separately visible and excluded, and an all-unmeasured group has no functional success rate.
Criterion judgments never acquire a not-measured value; this is dimension applicability, not missing evidence.
The generator emits the additional column when unmeasured functional results exist and identifies the required assessment version.
Legacy aggregate layouts must fail if they would hide unmeasured results; existing v1 reports remain valid.
Version-2 explicit counts suffice; runtime-stratified unmeasured reporting is not selected and must fail explicitly rather than silently omit observations.

Extend existing generation, structural validation, table derivation, aggregate checking and packaged resources; do not change subject execution or skill-specific scoring policy.
Retain draft generation's exclusive-write behavior and explicit version selection.
Test procedural-only success/failure, preserved functional precedence, omitted/misclassified criteria, mixed batches, excluded/unassessed attempts, wrong counts, legacy rejection and versioned generation.
Use actual CLI and temporary Git fixtures, with no providers or historical record migration.

Review correction: version 1 already requires a functional criterion and rejects procedural-only completed records. Its fallback rollup alone does not describe full validation. Correct earlier preparation prose accordingly.

Verification: full offline runner suite passed 445 tests; hook suite passed 263 with three existing environment skips; format suite passed nine and SSR fixture suite seven.
The first full runner run had a process-cleanup assertion failure outside the changed code; the full rerun passed.
Review also closed aggregate-column omission and result/schema-version mismatch paths with regression tests.
Existing version-1 schema/template bytes and measured records are unchanged.

Authorization: after discussing the reporting proposal, the owner instructed “go review your proposal, address any issues, then make the changes” before implementation. This authorized the reporting extension, not diagnostic collection.
