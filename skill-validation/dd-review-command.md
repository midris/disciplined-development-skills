# /dd-review command — validation

Records the scenario sets for the `/dd-review` command's pre-PR routing and
angle dispatch so they are recoverable and re-runnable. Not a skill (`/dd-review`
is a slash command), kept here with the other validation records.

**Dispatch protocol.** Read-only and bounded per CLAUDE.md's evaluation-subagent
rule (Claude Code: `Explore`). One scenario per agent, text-only.

## Method

Hand a subagent the command file (or the relevant excerpt) + a situation; record
the routing decision. Compare the pre-edit command (RED) against the post-edit
command (GREEN), and check regressions on adjacent paths.

## Scenarios — doc-dominant pre-PR routing

- **A (RED→GREEN) — doc-dominant branch at `pre-pr`.** Branch diff is entirely
  docs; invoke `/dd-review pre-pr`. RED (no routing note): runs `ENGINE pre-pr`
  straight to the codex gate. GREEN (note present): runs an in-session
  `/dd-review cold-read` first (doc-substituted angles), then the gate.
- **B (regression) — code-dominant branch at `pre-pr`.** All-Python diff, GREEN
  command. Must NOT detour to cold-read — the note is conditional on
  doc-dominance; run the gate directly.
- **C (regression) — cold-read is not a gate replacement.** Doc branch, GREEN
  command, in-session cold-read already clean. Must STILL run `ENGINE pre-pr` —
  the cold-read pre-empts codex rounds, it does not replace the mandatory gate.

## Results

- **A:** clean flip — RED went straight to the gate; GREEN ran the cold-read
  first, then the gate.
- **B:** identified the note as inapplicable; ran the gate directly, no detour.
- **C:** required the gate after a clean cold-read ("a preliminary filter, not a
  replacement").

## Scenarios — angle dispatch (reviewer set per tier)

Validates the dispatch step (command "Dispatch the tier's reviewer set"): the
monotonic per-tier set, parallel dispatch, full-diff-per-reviewer (an angle adds
a focus, it does NOT partition the diff), and the doc-dominant substitution.

- **RED — no command spec.** A subagent told to "cold-read this code diff" with
  only the `adversarial-review` skill (no reviewer-set table).
- **GREEN — code-dominant cold-read.** Command loaded; ~420-line all-Python diff.
- **GREEN — doc-dominant cold-read.** Command loaded; all-markdown diff.

### Results — angle dispatch

- **RED (2 runs):** improvised an ad-hoc **3-agent set that partitioned the diff**
  (source-only / tests-only / cross-cutting) — no holistic catch-all, not the six
  angles, findings free to fall through the seams. Confirms the reviewer-set table
  is load-bearing.
- **GREEN code (2 runs):** the full six-angle set (holistic, correctness,
  rationale, cross-file, security, necessity), in parallel, each on the **full**
  diff, no substitution.
- **GREEN doc (2 runs):** the substitution applied (security → executability,
  cross-file → doctrine-consistency), six angles, parallel, full diff.
- The spec's payoff is the exact thing RED got wrong: every reviewer sees the
  whole diff with a holistic owner, vs RED's partition-and-drop-the-seams.

(The loop half — iterate-until-clean, class-sweep, cap-escape — is validated
separately in [adversarial-review-loop](adversarial-review-loop.md).)

## On edits

Re-run A (RED on the pre-edit command, GREEN on the post-edit) plus B and C
(read-only) before changing the pre-pr routing note. Any wording that could read
as "cold-read replaces the gate" must re-pass C.

Re-run the angle-dispatch RED/GREEN (read-only) before changing the reviewer-set
table, the angle focus lines, or the doc-dominant substitution rule. GREEN must
produce the monotonic set, in parallel, full-diff-per-reviewer, with the
substitution on a doc-dominant cold-read.
