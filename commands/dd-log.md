---
# Consumer template for the /dd-log slash command. Paths below assume the
# consumer-side install layout: the disciplined-development skill (and its
# hooks/ subdir) is symlinked under .claude/skills/ by install-skills.sh from a
# clone of disciplined-development-skills. Copy this file to your project's
# .claude/commands/dd-log.md (or let the installer symlink it);
# commit-or-gitignore is your choice.
description: Use after each round of an in-session adversarial review to attempt a durable review record and reset the review cadence on a passing round.
argument-hint: <what-triggered-the-review> [round-number]
---

Pipe this round's **aggregated** findings on stdin to the log tool:

    python3 $CLAUDE_PROJECT_DIR/.claude/skills/disciplined-development/hooks/log_review.py \
      --source model-review --trigger <what-triggered-it> [--round N]

- Feed the deduped, highest-severity-wins aggregation of the round — the same
  `- [PN] <file>:<line>: <summary>` lines the reviewers emit — not raw per-angle
  output. Append a final line containing exactly `DD-VERDICT: PASS` or
  `DD-VERDICT: BLOCK`; the tool trusts that decision and parses findings only
  for telemetry counts.
- `--trigger` names what prompted the review (e.g. `cadence`, `chunk-close`,
  `pre-pr`). `--round` is the iteration number, starting at 1 and incrementing
  each re-run of the loop.
- Preserve P3-only findings in the aggregation. If the round passes, retain
  them above the explicit PASS line. If there are no findings, pipe
  `No findings.` followed by `DD-VERDICT: PASS`. An explicit PASS independently
  attempts to clear the unreviewed-edits count and stamp the review checkpoint
  at HEAD regardless of trace persistence. If one best-effort state write fails,
  the remaining edit or commit state keeps conservative review pressure active.
  A missing or malformed verdict (including an empty pipe) is rejected (exit 2)
  without logging or resetting.

Invoke once per round, including the terminal passing round; never block the loop
on a log-write failure.
