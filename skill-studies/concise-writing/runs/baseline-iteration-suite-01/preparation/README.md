# Remaining CW suite: execution preparation

Authority and current status: [protocol](../../../protocol.md).
The owner approved 144 subjects and fourteen Opus reviews on 2026-10-18, with no automatic retry, wording change or adoption.
The [comparison design](../../../drafts/baseline-iteration/comparison-proposal.md) defines the reuse path and fixed assessment boundaries.

## Inputs and order

The [schedule](schedule.json) contains 144 immutable slots: 36 Codex ordinary, 36 Claude ordinary, 36 Codex native and 36 Claude native.
Ordinary A/B/C each compare control, original, targeted and fuller, three repetitions per provider.
Native N1–N4 each compare original, targeted and fuller, three repetitions per provider; no native control is added.
Within each case, use cyclic rotations with case offsets and opposite provider starts.
Three repetitions fully rotate native conditions but cannot balance four ordinary conditions; disclose that residual order imbalance.
This is fixed ordering, not randomized collection or a reliability estimate.

The 48 configs preserve existing matched case/task/prompt/non-skill fixture bytes; only new conditions' assigned skill bodies differ.
Seven controller-only applicability cards extend condition IDs and setup links without changing criterion meanings.
The no-CW control receives no CW catalog or body; explicit-load arms require complete assigned instruction delivery before editing.
Native arms expose the available skill without asking for a load; qualified misses remain observations and output quality is assessed separately.
No policy, prior output, rubric, controller or authoring rationale is a subject input.
E reuses all five observations per condition/provider; input, source, draft and installed runtime identities still match that diagnostic.
These retained observations are not renamed or pooled into a new interleaved three-repetition batch.

## Runtime, retention and stopping

Codex 0.163.0 / gpt-5.6-sol low; Claude Code 2.1.301 / claude-sonnet-5 low; workspace-write, 900 seconds.
The unchanged [runtime adapter](runtime_setup.py) selects existing Python 3.14.8 and Git 2.56.0 inside each invocation's already permitted private scratch.
This neither broadens filesystem reads nor adds guidance.
[Runtime identities](runtime-identities.json) pin the exact binaries; twelve fresh zero-model installed-policy/CLI/isolation/Opus checks pass under this setup.
The active assessor is Codex; the reviewer is claude-opus-5-5 medium, read-only with native Read/Glob/Grep and no skills or shell.
Its CLI/model, complete-read timing and protected bytes must be checked separately from output judgment.

Raw bundles and inventories are retained at /Users/simon/work/personal/skill-study-private/concise-writing/baseline-suite-20261018 under the existing owner-accepted single-host arrangement.
Do not run Git in retained bundles; inspect files or disposable copies.
Run [collect_one.py](collect_one.py) with one global slot number, then inspect/clear that stopped receipt before advancing.
The controller freezes and verifies manifest/config/source/runtime identities, rejects repeated case/condition/repetition slots and exclusively claims each global slot.
It records every attempted invocation and charge, including zero-charge preallocation failures; an interrupted claim cannot silently restart.
Stop on infrastructure, contamination, unexpected identity/guidance, capture/retention failure or uncertain charge.
A valid behavioral failure does not stop the remaining schedule and is never excluded to improve scores.
No replacement, fallback model, retry-pool transfer or between-repetition edit is authorized.

## Review packets

Six ordinary packets, one per A/B/C and provider, contain twelve outputs each.
Eight native packets, one per N1–N4 and provider, contain nine outputs each; N3 has task-only observations and unmeasured CW functional effectiveness.
The evaluator sees complete task/source/notes and saved outputs, the fixed applicable policy/criteria and mechanical/length observations.
It emits first-pass judgments before reading the active assessment; record every disagreement without majority voting.
Freeze each copied packet and its read-only configuration before its funded call; the existing twelve/twenty-output qualifications bound these smaller packets.
A failed review remains charged and stops the affected decision; no automatic split or replacement is authorized.

## Inspection amendment after global slot 37

The first Claude ordinary subject completed and retained its output, but the inspector did not recognize its Write path argument ending in a newline.
The CLI had normalized that argument and written the declared report.md.
Only target-path recognition changes: strip a terminal CR/LF when inspecting the captured argument, while keeping every raw evidence byte intact.
Six path cases pass; removing the normalization makes exactly the retained-newline case fail.
Replay of the existing trace verifies complete assigned CW delivery before editing, the requested runtime/model and protected inputs, with no repeated call or setup exclusion.
The first Claude attempt retains its original controller/manifest identity; later slots use prospectively repinned inspection metadata with unchanged task, source, prompt, skill, schedule, policy, model, shell and permissions.
