---
# Bundle-source variant of the /dd-log slash command. Paths point at the
# skills/disciplined-development/ tree because this repo (the source of the
# bundle) does not symlink its own skills into .claude/skills/. See the
# top-level commands/dd-log.md for the consumer-side variant whose paths go
# through .claude/skills/.
description: Use after each round of an in-session adversarial review, once you have aggregated that round's findings — including a clean "No findings." round — to record it to the durable review log and (on a clean round) reset the review cadence counters.
argument-hint: <what-triggered-the-review> [round-number]
---

Pipe this round's **aggregated** findings on stdin to the log tool:

    python3 $CLAUDE_PROJECT_DIR/skills/disciplined-development/hooks/log_review.py \
      --source model-review --trigger <what-triggered-it> [--round N]

- Feed the deduped, highest-severity-wins aggregation of the round — the same
  `- [PN] <file>:<line>: <summary>` lines the reviewers emit — not raw per-angle
  output. The tool derives the decision and severity counts from that text.
- `--trigger` names what prompted the review (e.g. `cadence`, `chunk-close`,
  `pre-pr`). `--round` is the iteration number, starting at 1 and incrementing
  each re-run of the loop.
- A **clean** round must pipe the literal `No findings.` — that logs one `PASS`
  row and resets the cadence counters (clears the unreviewed-edits count and
  stamps the review checkpoint at HEAD). An empty pipe is rejected (exit 2).

Log once per round, including the terminal clean round; never block the loop on
a log-write failure.
