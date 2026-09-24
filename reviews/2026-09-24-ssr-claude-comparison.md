# Claude SSR comparison close review

Scope: the 34-call `claude-comparison-01`, its fixed inputs, scored results, retained index, aggregate assessment and current-state documents.
Review: active-session self-review; not independent or blind.

The comparison is complete with 34 valid setups and no retry or replacement calls.
The [assessment](../skill-studies/sweeping-stale-references/claude-comparison-01-assessment.md) separates functional outcomes, timely native invocation and procedural accounting.
No skill or runner source changed during collection.

## Corrections during closing review

- Corrected a sanity result's unsupported observation dimension from `task` to `functional`; its outcome remains `not measured` and outside functional counts.
- Corrected order 24's F2 explanation to say only README changed; its preserved-behavior judgment and incomplete-repair outcome are unchanged.
- Swept current status through the plan, both protocols, handoff and discovery qualification instead of appending contradictory progress notes.
- Kept the owner-accepted rewrite reporting rule distinct from the candidate's new local n/a deviations; no historical score changed.

Order 4 exposes an existing convenience-file extraction limitation: a successful result followed by background cleanup events does not produce `final.txt`.
The complete response and cleanup are retained in the raw trace, which the result cites; this does not block this assessment.
A focused extractor regression/fix is a future runner task, not a reason for additional model calls or an in-collection runtime change.

## Verification

- All 34 raw bundles match every entry in their retained inventories; the zero-model preflight inventory also matches.
- Result-v2 schema checks, evidence hashes, manifest/authority Git pins and index pins pass.
- Complete original/candidate bodies are observed in all 24 explicit-load attempts and native orders 26, 27, 28, 30 and 32; the other native attempts have no SSR load.
- All 34 production catalogs contain SSR plus the same sixteen bundled skills and report `claude-sonnet-5`.
- Functional inspection and executable replay use disposable copies; retained Git indexes are untouched.
- All nine batch readiness checks pass; the new assessment is complete and structurally valid.
- Actual-CLI/isolation preflight: four passed, two deselected, zero model calls.
- Hook suite from its documented working directory: 263 passed, three skipped. An initial repository-root invocation had four import failures; the documented invocation resolves them without source changes.
- Combined accounting is 126 subject calls and 1,486 estimated active minutes; runner durations are included once.

No blocking findings remain after the corrections and repeat review.

DD-VERDICT: PASS
