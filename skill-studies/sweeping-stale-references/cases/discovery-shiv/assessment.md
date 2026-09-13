# Discovery case: settled Shiv option rename

Status: locally prepared for owner review; no model run authorized or made.
This is a development case, not a measured baseline or a demonstrated discovery advantage.

## Purpose and source

Observe discovery separately from the decision to repair a discovered reference, using substantive project source rather than bulk dependency files.
The owner approved the concept and this implementation base; packaging is only the scenario domain.
The earlier synthetic `pilot-03` draft remains preserved and undispatched.

The fixture copies Shiv revision `ff542cbe75ea832df3a989d07c7fdf5214f727fa`, with its BSD license and NOTICE.
`source-provenance.json` identifies upstream files, four modified upstream files, ten study-authored additions and the separately supplied Click runtime.
The settled rename and stale consumers are study inventions, not upstream history.
The resulting project has 50 files / 106,979 bytes, excluding 19 runtime files / 424,152 bytes.
This is meaningful source, tests and documentation, but size does not establish discovery difficulty: a subject may still inspect every consumer.

## Task and conditions

`task.md` presents a settled rename from `--output-file` to `--destination` and one broken README command, permits project edits and requests a commit.
It does not enumerate sibling consumers or direct a sweep.
The unchanged `-o` alias is explicitly valid.
Four current commands need reconciliation: README, a local script, a nested Make include and a hidden CI workflow.
Each invokes Shiv's native CLI to build the greeting archive; the controller executes each result rather than substituting a marker-only check.

Both conditions receive the same project, runtime and task bytes: 70 regular-file entries in control, 71 in original.
Only original receives the frozen `../skill-original/SKILL.md` and its explicit read instruction.
DD, sibling skills, expected outcomes, controller code and assessment policy are excluded.
The neutral initial commit establishes the already-renamed project; subsequent repair commits are assessed.
`.runtime/`, `.agents/` and `TASK.md` are ignored in that subject repository.
The runtime is nevertheless part of the declared, hash-identified input and must be retained with the case and each bundle.
When committing this case, explicitly add the 19 pinned runtime source/license files despite the subject-facing ignore rule; never add generated caches.

## Assessment

Read this document, `expected.json` and the controller-only `assessment-policy.txt` before judging a run.
`preparation.json` identifies the exact source revision and verbatim copy of `SSR-assessment-2`.
Functional outcomes lead; procedure is reported separately, with no combined score.

| Criterion | Evidence and consequence |
|---|---|
| Setup | Verify declared inputs/settings and identical initial project trees, full original-skill read, control guidance integrity and usable traces. Record absent-guidance probes; probing alone is not contamination. Runtime/setup failures invalidate attribution rather than count as skill failures. |
| F1: Current consumers | All four commands produce the intended runnable greeting archive. The local script works from the project root and elsewhere. Missing/deleted consumers, no-op commands or wrong archives fail. `--destination`, its equals form, and `-o` are acceptable repairs. |
| F2: Preservation | Preserve the settled CLI, short alias, greeting behavior, historical record, independent inventory tool and unrelated project behavior. Restoring the retired option to mask stale consumers fails. Byte differences require semantic inspection rather than automatic failure. |
| F3: Committed repair | Required edits must be in retained Git history after the baseline; edits left only in the working tree fail even when replay succeeds. |
| P1: Discovery and triage | For each consumer separately record when retained tool output exposed stale content, explicit repair/preservation decisions, and committed outcome. Filename-only listings are not content exposure. Missing/truncated output makes awareness uncertain. Record repository breadth and search-before-edit ordering without claiming access proves internal attention. Procedural deviations are non-blocking. |
| P2: Commit grouping | One complete repair commit satisfies the original's grouping requirement. Multiple complete commits are a non-blocking procedural deviation; distinguish them from missing committed edits under F3. |
| P3: Useful account | The nine literal occurrences across eight project paths in expected.json define scope: four updates, one historical occurrence and four false positives. The two deliberate negative assertions share one test file. Exclude task/skill/runtime and already-current or additional exploratory hits. Judge usefulness; missing detail is secondary and cannot fail a functional outcome or justify another run. |

Apply target-specific procedure to original only; do not impose undisclosed output requirements on control.
Report met / not met / insufficient evidence per criterion, with trace and Git pointers.
If both conditions encounter every consumer, report the repair-scope comparison and no observed discovery advantage; do not enlarge the case or hunt for a control failure.

## Replay and qualification

Inspect subject-modified commands and diffs before executing them.
Use a disposable copy of the complete subject fixture; never replay against retained raw evidence.
Keep the checker, expected.json and the complete pristine fixture together: the checker verifies all 69 reference files against the controller-only hash inventory before deleting outputs or executing any subject command. Missing or changed reference inputs stop replay as a setup error; they cannot reduce preservation coverage.
Run `python3 -B check_consumers.py DISPOSABLE_FIXTURE_COPY` from this case directory.
The checker deletes `build/` between observations to prevent old artifacts from disguising a no-op repair.

The observer extracts the README's named section and single shell block, the inventory document's single shell block, and CI's single-line named `Build greeting` step.
Unsupported structures require manual inspection, not an automatic behavioral failure.
It executes those commands, the script from two directories and Make, then inspects archive payload/entry point and executes the archive.
It also probes the canonical option, valid alias, rejected retired option and independent inventory interface.
The CI observation replays only the build command locally; hosted execution, setup, dependency installation and the upstream network-dependent test suite are not qualified here.
The local wrapper loads supplied Click and Shiv; offline builds require no package installation.

Facts are not verdicts: inspect extra files, semantic alternatives, source/test changes, full Git history and final working tree separately.
Exact payload or preservation mismatches are review signals under the whole-artifact policy.
Missing commands, parser limits and timeouts require separating infrastructure limitations from demonstrated functional failure. A retired-option probe without an exit status records null, not false, for rejection.
`qualification.json` retains known-correct/incorrect observations and actual loader/copy checks without providers; `manifest.json` pins their inputs.

## Next decision

Proposed settings remain Codex `gpt-5.6-sol`, low, `workspace-write`, one control then one original, preserving and assessing each bundle before continuing.
Recheck executable identity and all input hashes before any authorized dispatch.
Only one additional-development subject slot remains, so this pair requires an explicit allocation revision; the unused outer ceiling does not authorize a transfer.
No evaluator call, retry or protected comparison capacity is proposed for use.
Broader coverage, evaluator qualification and population reliability remain open.
