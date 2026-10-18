## Criteria

Apply the exact `SSR-assessment-2` copy identified in preparation/manifest records. Use met, not met or insufficient evidence per criterion, with no combined score.

| Criterion | Evidence and consequence |
|---|---|
| Setup | Verify input/settings identities, identical initial trees, full original read, control guidance integrity and usable traces. Record absent-guidance probes without treating them alone as contamination. Setup faults invalidate attribution, not skill behavior. |
| F1: Complete, useful documentation | Every current delivery description agrees with the settled behavior: at most four sends, up to three after an initial failure, exhaustion only after four failures, immediate stop on success. Judge the documents together. Contradictions, remaining obsolete claims or deleting useful explanations without an effective replacement fail. |
| F2: Preservation | Keep the worker's settled behavior, the independent helper's three-attempt limit, historical meaning and unrelated operational guidance. Verify code and runtime evidence. Byte differences initiate semantic review; they are not failures by themselves. |
| F3: Committed repair | Every required repair appears in retained Git history after the baseline, including a valid consolidated explanation and its references. Correct work left uncommitted fails. Inspect history and the final working diff; do not infer completeness from the message or changed-file count. |
| P1: Search and triage | Retained events show search before repair and the handling of relevant current/historical/independent meanings. Account for what the model actually read and decided; absent evidence means uncertainty. Purely procedural deviations are non-blocking. |
| P2: Commit grouping | One complete repair commit meets the grouping requirement. Complete repairs split across commits are non-blocking procedure deviations, distinct from F3. |
| P3: Useful account | Use the predeclared reference-block scope in expected.json. Assess accurate update/preservation explanations, locations, grouping and counts. Missing detail remains secondary and cannot turn functional success into failure or justify another run. |

An incomplete/incorrect repair can affect both F1 and F3; report the shared cause rather than count it as two independent failures.
Target-specific procedure applies to original; describe control behavior without imposing undisclosed format instructions.
Functional ties and procedural differences are both reportable; no control failure or discovery advantage is required.

Accept accurate prose, tables, reordered sections or consolidation with clear working cross-references that still serve each document's reader.
Do not require changing all three original files if a different complete solution satisfies the three document roles.
A reference answer is one valid repair, not the required wording.
Changing a number without understanding whether it counts attempts or retries is not sufficient; neither is passing the runtime checks while leaving prose stale.
