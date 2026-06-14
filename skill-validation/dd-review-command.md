# /dd-review command — validation

Records the scenario set for the `/dd-review` command's pre-PR routing so it is
recoverable and re-runnable. Not a skill (`/dd-review` is a slash command), kept
here with the other validation records.

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

## On edits

Re-run A (RED on the pre-edit command, GREEN on the post-edit) plus B and C
(read-only) before changing the pre-pr routing note. Any wording that could read
as "cold-read replaces the gate" must re-pass C.
