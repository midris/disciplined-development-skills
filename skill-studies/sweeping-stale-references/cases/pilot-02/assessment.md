# Pilot 02: moved setup guide

Status: owner approved conceptual design and local preparation on 2026-09-13; no provider call authorized or made.
This is a non-reserved development case extending coverage after pilot 01, not a measured baseline.

## Purpose and reuse decision

Exercise references to one moved document expressed relative to different consumer directories, including an executable consumer, while preserving history and an unrelated same-name guide.
The owner approved this design before fixture construction and then selected the simpler three-link/export-script version. A site-config entry was removed because no real builder consumed it; add more consumer types only if later coverage needs justify them. Inspection of the six historical SSR prompts found identifier/prose renames, supplied accounting inventories and a supplied local-change finding; none exercises moved-file resolution. Build this fixture from scratch. No historical rubric, result or score is inherited.

The frozen skill explicitly teaches broad search, triage and reconciliation. Correct relative-path handling is an **owner-clarified functional outcome**, not an explicit technique in that text. A miss fails the agreed outcome without by itself proving disobedience to an explicit relative-path instruction.

## Subject task and conditions

The service guide already moved from `docs/setup.md` to `docs/reference/setup.md`; the task names one broken README link and permits project edits. Unstated consumers are discoverable from ordinary project files.
The existing valid vendor guide has the same basename. Current references must reach the intended service guide, not merely an existing file.
Both conditions receive identical project/task/setup bytes. The original alone receives the frozen SSR snapshot and the explicit read instruction. DD and sibling skills are not supplied.
The neutral baseline commit captures the already-moved project; it is not scored as the repair. Keep the settled move rather than restoring the old path or adding a duplicate to conceal broken consumers.

## Assessment policy and criteria

Apply `SSR-assessment-2` from the study protocol; the manifest identifies an exact controller-only policy copy. Read that policy and this case's criteria before assessing. Do not supply either to the subjects.
Lead with committed functional completeness, preservation and working consumers. Treat detailed accounting as secondary, with no combined score.

| Criterion | Required evidence and consequence |
|---|---|
| Setup | Verify declared files/settings, identical initial project trees, full original-skill read, control guidance integrity and usable traces. Setup faults invalidate attribution rather than count as behavioral misses. Record absent-guidance probes without treating them alone as contamination. |
| F1: Current consumers | README, documentation index and nested quickstart resolve to the moved service guide; exporting the guide outputs its intended content. Missing/deleted consumers or wrong existing destinations fail. Resolve Markdown paths from their containing file. |
| F2: Preservation | Retain the service instructions, the historical location as historical information, and the vendor guide/link as an independent working reference. Keep the settled move. Wrong changes fail; byte differences initiate semantic inspection rather than automatically fail. |
| F3: Committed repair | All required edits appear in committed Git history after the baseline, with none left only in the working tree. Missing committed edits fail even when the current files look correct. |
| P1: Search/triage | Use ordered events to observe breadth, search before edits and reasons for preservation. A correct final state alone does not establish the search procedure. Purely procedural misses are non-blocking. |
| P2: Commit grouping | All required changes in one repair commit meets the original's grouping requirement; multiple complete commits are a non-blocking procedural deviation, distinct from uncommitted edits under F3. |
| P3: Audit usefulness | Describe whether the account explains the repair and deliberate preservation. The four current references and one historical reference in expected.json define the moved-document accounting scope. Record useful unrelated-match triage separately; do not require entries for already-current references or every broad basename-search hit. Missing detail cannot fail the functional result or justify another run. |

Target-specific procedure applies to the original; compare control behavior without imposing undisclosed output instructions.
Report met / not met / insufficient evidence per criterion. An ambiguous interpretation is not a confirmed skill defect or a rewrite objective.

## Deterministic observations and their limits

`check_paths.py FIXTURE` reports path resolution and content observations using controller-owned expected targets. It emits facts, not an overall skill score. Its supported Markdown form is ordinary inline links; unsupported rewrites require manual inspection, not automatic failure. Equivalent normalized relative paths, labels and prose structures are acceptable when the consumers still work.
Run `sh scripts/export-guide.sh` on a disposable assessment copy, compare its output to the service guide, and inspect the diff and retained Git history separately. Run it from the project root and a different working directory to exercise its documented location independence.
The tool cannot establish semantic preservation from byte differences, complete search behavior, Git completeness, or evaluator reliability. Inspect all changed files and unexpected changes. Do not rely on matching hashes alone as the only acceptable output shape.
Qualification uses constructed correct/incorrect copies, not model output; it must catch a README-only repair, a wrong-but-existing target, damaging replacement, and rollback, while accepting a complete repair and equivalent path spelling.

## Proposed next calls

If approved after reviewing this package: one control then one original, Codex `gpt-5.6-sol`, low, `workspace-write`; preserve and inspect each complete bundle before the next call, then stop.
These two calls would use two of the three additional-development subject slots, leaving one there; they do not expand any pool or replace baseline/rewrite comparison capacity. No evaluator call or automatic retry is proposed.
This case extends path-resolution coverage; subtle code-to-documentation drift and a justified local-only change remain untested. One pair cannot estimate population reliability or qualify hidden-case isolation.
