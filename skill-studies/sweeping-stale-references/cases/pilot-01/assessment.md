# Pilot 01: executable cache-setting repair

Process-qualification case, not a measured baseline or reserved transfer case.
Adapted from `skill-validation/scenarios/sweeping-stale-references/ssr-02` after conceptual coverage acceptance: retain the reviewer-triggered rename and mixed consumer categories, replace its completed inventory with an executable project.
The old prompt prohibited edits and supplied the answer inventory. Neither it, its rubric nor its results is used for this pilot.
The other earlier scenarios exercise a two-file rename/comment rewrite, a supplied grouping inventory or a supplied negative finding; they are less suitable for the first execution pilot.

## Inputs and exposure

Both configurations supply the same 13 project files and task brief. The original adds only the checked-in SSR skill and its explicit load instruction.
The task names one stale README example and the settled rename; it neither directs a sweep nor enumerates siblings.
The initial `fixture baseline` commit is neutral setup. `.gitignore` excludes task and skill inputs from project commits; their bytes are still captured by the runner.
Only the files declared in `control.json` or `original.json` are supplied. This document, `expected.json`, `qualification.json`, the manifest and the study protocol are evaluator/controller material.
This excludes them from declared inputs, not from every possible filesystem read: inspect actual traces for outside-input access and ambient guidance before accepting control integrity. Reserved-case isolation is not claimed.

## Pilot observations

For each criterion, record met, not met or insufficient evidence with file/trace/commit references. Keep setup validity, functional outcomes and procedure separate.
The orchestrator directly inspects this non-reserved pilot; these are developmental observations, not independent model-evaluator scores. No evaluator call is needed to qualify an assessment mechanism the pilot does not use.

| Criterion | Evidence and consequence |
|---|---|
| Setup | Shared inputs and execution settings match their manifest; original read the entire target, control received no skill guidance; initial Git tree matches the project fixtures; no relevant unintended reads or missing-input stops. A mismatch invalidates that condition, not the skill. |
| F1: Complete current-reference reconciliation | All seven current consumers in `expected.json` use the settled interface with unchanged meaning/default. Check actual examples, config, shell/build/CI commands and prose. Missed or incorrect updates are hard failures. |
| F2: Preservation | Historical state, third-party interface and HTTP directive retain their intended meaning and behavior. Byte differences flag review; they do not automatically prove damage. Incorrect changes are hard failures. |
| F3: No functional regression | The application still uses the settled `max_age` interface and 30-second default. Inspect code/test changes as well as command results; weakening tests or restoring the old interface cannot substitute for reconciliation. |
| P1: Search before repair | Ordered events show relevant searches before the first reconciliation edit, excluding baseline Git setup. Assess breadth including hidden CI files and relevant triage. Missing traces mean insufficient evidence; final files alone do not prove the sequence. |
| P2: Triage account | Match dispositions and reasons agree with actual references, including deliberate preservation. Separate correct file outcomes from whether the account records them. |
| P3: Single reconciliation commit | Compare Git history to `fixture baseline`; required updates land in one subsequent commit. An otherwise correct repair split across commits is a procedural defect. |
| P4: Useful output contract | Inspect `References swept:` location, outcome labels, grouping, locations and counts against retained searches and changes. Deduplicate repeated queries; nine is the known input old-literal count, not a mandatory total for every possible query. A missing or inconsistent account is non-blocking but remains visible. |

Target-specific procedure is assessed for the original condition. Control accounting can be described for comparison, without penalizing the control for undisclosed instructions.
A functional tie plus a useful accounting difference must be reported as such.
This case does not establish moved-path handling, subtle synonym recognition, the justified-local-change boundary, generalization or population reliability.

## Existing tools and qualification

Use `git log`, `git show`, `git diff` and the retained JSON event stream for actions/commits; use `git grep` or `rg --hidden` to inventory candidate references. Do not treat literal absence as semantic correctness.
The project checks are `python3 -m unittest discover -s tests`, `sh scripts/cache-smoke.sh` and `make smoke`. Execute the CI run command locally; do not dispatch GitHub Actions or fetch dependencies.
Validate the README JSON example against the settled application interface separately. Equivalent functioning formatting/commands and accurate documentation wording remain acceptable.
Inspect all changed paths and preserved material even when runtime checks pass.

`qualification.json` records five orchestrator-constructed variants and local checks, not model observations:

- Initial fixture: README example and all four runtime checks fail on the stale interface.
- README-only fix: example succeeds; other runtime checks still fail.
- Complete repair: example and runtime checks pass; protected material remains unchanged.
- Complete repair with reformatted JSON: same result, demonstrating accepted formatting variation.
- Blanket replacement: runtime checks pass, but historical and vendor content changes incorrectly. This demonstrates why runtime checks cannot replace triage judgment.

No new runner feature or generic assessment tool is introduced. The first two real runs must still establish usable traces, native skill loading, feasible commits and comparable conditions.
