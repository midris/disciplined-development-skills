# SSR pilot 01: two real runs

Both authorized subject calls completed on 2026-09-12 using Codex `gpt-5.6-sol`, low effort, `workspace-write`.
The original skill achieved the functional outcome; the control repaired only the reported README example.
The original's accounting was useful but incomplete.
These are orchestrator-inspected development observations from one case and one run per condition, not a measured baseline, independent evaluator scores or a reliability estimate.

## Results

| Criterion | No-target control | Frozen original skill |
|---|---|---|
| Setup | Met within the observed-input boundary below | Met within the same boundary; entire frozen skill read |
| F1: Complete current-reference reconciliation | **Not met:** 1/7 current references repaired | **Met:** 7/7 repaired |
| F2: Preservation | Met: historical, vendor and HTTP content unchanged | Met: all three unchanged |
| F3: No functional regression | Met: implementation/tests unchanged; existing breakage remains under F1 | Met: implementation/tests unchanged; settled interface and default retained |
| Command checks | README example passes; unit, shell, Make and CI-command checks fail | All five checks pass, including both unit tests |
| P1: Search before repair | Observed, including all seven current consumers | Met: literal and broader searches precede edits, including hidden CI |
| P2: Triage account | Describes a narrow scope decision; target format not required of control | **Not fully met:** nine old-name matches accounted for; broader-search dispositions omitted |
| P3: Single reconciliation commit | One repair commit, but six required updates absent under F1 | Met: all seven updates in one repair commit |
| P4: Useful output contract | No `References swept:` section; no penalty for undisclosed format | **Not fully met:** correct placement, labels and grouping for nine entries, incomplete search reconciliation |

The control found the sibling references before editing and explicitly treated their repair as outside the requested README task.
Its functional miss is therefore an observed scope/reconciliation decision, not a failure to discover the files.
During the walkthrough, the owner confirmed that a rename should trigger tracking down all instances of the old reference and updating them accordingly; the flagged README example does not limit the intended SSR scope.
This confirms the existing F1 expectation of complete current-reference reconciliation, rather than adding a criterion after observing results. Deliberate historical and unrelated references still require appropriate triage.
The original repaired every current consumer with seven one-line substitutions, preserving meaning and the 30-second default.
This pair is consistent with a useful skill effect on scope completion; a single unreplicated comparison cannot establish a stable causal effect.

The original's broader pre-edit search returned 15 distinct path/line locations after deduplication, while its commit accounts for nine.
Omitted locations are `src/http_headers.py:3`, `src/cache.py:9,11,17,20`, and `README.md:10`.
The HTTP match is unrelated and the other five already express the current fact; they were correctly left unchanged, but their dispositions were not recorded.
The frozen skill explicitly requires accounting for every match; the pre-run assessment also distinguishes the nine known old-literal matches from actual query totals.
This is a non-blocking procedural defect under the settled policy, with no functional damage and no post-run criterion change.
During the accounting walkthrough, the owner emphasized that the actual commit is what matters: all affected references should be reconciled and all edits committed; a fully detailed commit message is nice to have.
Reinspection confirmed all seven required edits in `cb4e261`, one commit after the fixture baseline, with a clean working tree and protected material unchanged.
The accounting omission remains a secondary observation against the original text, not a blocker or a requirement to expand the audit format before continuing.
The [current SSR assessment policy](protocol.md#current-ssr-assessment-policy) carries this decision into subsequent cases and assessments; this pilot record is not the source of operational scoring instructions.

## Evidence and qualification

[The run index](pilot-run-index.json) records exact configuration identity, complete bundle inventories, Git identities, authorization, call counts, and absolute source/primary/backup paths.
[Controller replay results](pilot-checks.json) record command outputs from disposable copies made after preservation; no assessment commands modified retained bundles.
The CI command was executed locally, not through GitHub Actions.

In each indexed bundle, `stdout.txt` is the ordered JSON event stream, `final.txt` the subject's final report, `result.json` the runner record, and `workspace/fixture/.git` the retained history.
Evidence locations in `stdout.txt`:

| Observation | Control line | Original line |
|---|---:|---:|
| Baseline creation | 5 | 7 |
| Complete frozen skill in command output | n/a | 5 |
| Pre-edit search | 8 | 12 |
| First repair completed | 12 | 14 |
| Runtime checks | 15 | 17 |
| Repair commit | 17 | 19 |
| Final scope/result statement | 18 | 20 |

Both initial Git trees match all 13 supplied project files byte-for-byte; task and ignore inputs remain unchanged.
The original's retained skill matches the snapshot, and its full text appears in the captured read output.
The control has no `.agents/` directory and no recorded attempt to probe it or read skill guidance.
The original's `find .. -name AGENTS.md` probes the allocated workspace parent and returns no guidance; an initial no-match `rg` exits 1 but does not stop task completion.
No relevant unintended guidance read appears in either trace.
These observations support comparability for this pilot; they do not establish exhaustive filesystem read isolation, native automatic skill discovery, or protected-case secrecy.
Loading here was the explicit full-file read requested by the original prompt.

Both runner records report `COMPLETED`, provider exit 0 and no infrastructure error; control test failures are behavioral results, not runner failures.
Control duration was 47.936 seconds; original duration was 59.891 seconds.
Captured command output contains Xcode sandbox/cache warnings, without observed obstruction of the required commands.
Raw bundles contain 59 files / 49,208 bytes and 72 files / 81,236 bytes respectively; complete primary and backup inventories match their sources.
Raw streams remain outside Git under project policy; this checkout contains their manifests and assessments.
Both preservation stores are on this host and do not protect against host loss.

## Decision boundary

Stop at two subject calls: no evaluator, authoring, retry or third pilot call was made.
The existing runner supplied enough evidence to inspect loading, ordering, Git reconciliation and separate functional/procedural outcomes for this case; no new tool is needed for those observations.
Broader coverage, model-evaluator qualification, reserved-input isolation, measured collection and skill rewriting remain open.

The owner has confirmed the scope expectation behind the control's functional assessment and clarified that committed functional completeness takes priority over detailed accounting. The accounting walkthrough is resolved; review any remaining evidence concerns before returning to coverage design.
If that review accepts the process evidence, return to the agreed coverage map and prepare the next missing facet before proposing further calls.
Do not rerun this case merely to obtain cleaner accounting or extrapolate this pair into a baseline.
