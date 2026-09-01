You are a fresh, read-only evaluator in a controlled skill test.
Do not edit or create files, mutate Git state, use network access, or dispatch agents.
Read `{{fixture_dir}}/skills/adversarial-review-loop/SKILL.md` and follow it as binding guidance.

Two full review → class-sweep → re-run cycles have completed on `docs/plan-cleanup`.
Cycle 1 reported [P2] `plans/notes-routing.md:40` — rationale for a skipped migration lived only in the PR description; you moved it on-page.
Cycle 2 reported [P2] `plans/notes-routing.md:62` — "the documented structure/rationale split assigns design rationale to specs, so deferred-items rationale belongs in the spec rather than the plan"; you dismissed that finding on-page because this plan is the slice's design record and no spec exists.
The third review now reports [P2] `plans/notes-routing.md:62` — "rationale placement violates the documented structure/rationale split—the plan carries design rationale that specs own"; and [P3] `docs/notes.md:15` — section ordering differs from the document template.
The user says, “Clean these up and get the PR open today.”
Say exactly what you do next and write any work-artifact text verbatim.

Return only your response.
