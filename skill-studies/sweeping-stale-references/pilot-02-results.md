# Pilot 02: moved-guide results

The original-skill run repaired and committed all four current consumers, preserving the moved guide, historical record and independent vendor material. The no-target control repaired and committed only the README link; the other two documentation links and export script remained broken.
This is one Sol-low development pair, not a measured baseline, reliability estimate or rewrite comparison.

Assessment version 1, 2026-09-13: direct controller inspection under **SSR-assessment-2**, using the frozen [case criteria](cases/pilot-02/assessment.md), [policy copy](cases/pilot-02/assessment-policy.txt) and [expected outcomes](cases/pilot-02/expected.json). Exact input identities, complete bundle inventories and absolute primary/backup locations are in the [run index](pilot-02-run-index.json). The [replay observations](pilot-02-checks.json) retain commands, outputs, path resolution and Git facts. No separate model evaluator was invoked or qualified.

## Functional results

| Criterion | No-target control | Frozen original skill |
|---|---|---|
| F1: Current consumers | **Not met:** 1/4 repaired. README works; index and quickstart links remain broken; export exits 1 from both working directories. | **Met:** 4/4 repaired. Three service links resolve correctly; export exits 0 and matches the guide from both directories. |
| F2: Preservation | **Met:** all four protected files unchanged, independent vendor link works, old service path remains absent. | **Met:** same preservation results. |
| F3: Committed repair | **Not met:** only README committed; three required repairs missing. The working tree is clean, so these are omissions, not uncommitted edits. | **Met:** all four edits committed; clean working tree. |

Control repair: `d663a6158e23fbf4caefb360f157db251c5edd36`, after baseline `bae8ab028bc1b433ea7cbca2d58ffb1d19ad5b87`.
Original repair: `958a5e180e9d85c59becd62c245bd01a9b5ffb78`, after baseline `dc9030ae70b520085576a2f7d33a89b78c536dc8`.
Both baseline trees contain exactly the same nine project files and bytes. Comparing each baseline to HEAD confirms the changed paths and the absence of collateral edits.

The original updates `README.md` to `docs/reference/setup.md`, `docs/index.md` to `reference/setup.md`, the nested quickstart to `../reference/setup.md`, and the script to `$script_dir/../docs/reference/setup.md`.
These are the four required consumers. The script keeps its existing directory-resolution behavior. No duplicate at the old path hides broken links.
Correct relative-path handling is the agreed **owner-clarified outcome**; it is not an explicit relative-path technique in the frozen skill.

## Procedure and evidence

Line references below identify physical JSONL lines in each preserved bundle's `stdout.txt`, not the final response or this repository's source files.

| Criterion | No-target observation (no undisclosed format requirement) | Original-skill assessment |
|---|---|---|
| P1: Search and triage | Read all nine project files before editing (line 10), including history and vendor files. Committed a deliberately narrow README repair (lines 12–15). Reading the siblings did not produce a broader repair. | **Met:** full project read (line 12), explicit current/history/vendor distinctions (line 13), repository-wide literal and variant search before editing (line 15), edits at line 17. |
| P2: Commit grouping | One repair commit, but incomplete scope; the functional omission is already recorded under F3. | **Met:** all four updates in one repair commit (line 22). |
| P3: Audit usefulness | Brief README-only commit/report; no sweep account. This is an audit difference, not a format failure assigned to the control. | **Met for the registered scope**, with one minor non-blocking accuracy error: all four updates and the historical reference have precise locations, labels and counts, but the summary says seven paths where there are six. |

The original's inventory contains seven matches across six distinct paths because README contributes two lines. The seven individual entries correctly account for the retained search results, including optional vendor and already-current README matches. The mistaken path total does not hide a reference or affect any edit; record it as a secondary procedural defect, not a failed repair or a reason for another run. The preregistered scope did not require those two extra entries.

Control evidence: line 10 reads every project file; line 13 calls the repair scoped; line 15 commits only README and checks that target. Its final response at line 16 accurately summarizes that narrow work. It does not claim to have completed a sweep.
Original evidence: line 5 contains the complete frozen skill text; lines 19 and 22 retain the diff, verification and commit. The subject's repeated `test -f` commands check the same destination rather than resolving each Markdown link. Controller replay independently resolves each link from its containing file, so F1 does not rely on that overbroad subject verification claim.

## Setup, preservation and process findings

Both calls completed without runner infrastructure errors, with the approved Codex `gpt-5.6-sol`, low effort, `workspace-write` settings. Control took 37.782 seconds; original took 76.784 seconds (114.566 seconds total).
The original read the complete frozen SSR file before its baseline and task work; control had no `.agents/` directory and made no recorded attempt to retrieve SSR. Both looked for `AGENTS.md` and found none. Those absent-guidance probes are not contamination. Recorded Git commands emitted host Xcode/cache warnings but completed the required work.
The traces support task feasibility, explicit skill loading, search/edit order and retained Git history for these two runs. They do not establish native skill discovery, exhaustive read isolation, hidden-case protection or independent evaluator reliability.

Complete raw bundles were copied and hash-verified in both development stores before assessment; control preservation and setup inspection preceded original dispatch. Control contains 48 regular files / 38,194 bytes; original contains 55 / 69,673. Raw traces remain outside Git, with inventories and concise assessments in the checkout.
Replay used disposable copies after inspecting the retained diffs and script. No retained raw bundle was edited. The controller input package includes frozen policy, criteria, expected outcomes, checker and pristine fixture files: the latter are required by the checker's preservation comparison. The first replay preparation omitted that fixture directory; inspection stopped before producing results. Copying and hash-verifying those existing inputs corrected the controller package without changing criteria, checker, subject input or model-call count.

The process now supports a second kind of functional check, separate outcome/procedure judgments, preserved Git evidence and accounting scope fixed before observation. Before reusing this checker, include its pristine fixture dependency in the assessment package. No runner change is needed.

## Progress and next decision

Four subject calls have now completed across two development cases; no evaluator, authoring or retry calls have been spent. Pilot 02 used two of the three additional-development slots, leaving one there. The outer subject ceiling has 36 calls remaining, but no further dispatch is authorized.
Review these two bundles and this assessment with the owner before expanding coverage. Subtle code-to-documentation drift and a justified local-only change remain untested; evaluator qualification and reserved-case isolation remain open. No rewrite objective follows from the minor accounting defect. The observed functional difference supports the skill's intended contribution in this case; one observation per condition cannot establish its reliability.
