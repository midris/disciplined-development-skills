---
# Bundle-source variant of the /dd-review slash command. Path points
# at the top-level disciplined-development/ tree because this repo
# (the source of the bundle) does not symlink its own skills into
# .claude/skills/. See examples/commands/dd-review.md for the
# consumer-side variant whose path goes through .claude/skills/.
description: Run adversarial review at the given tier and act on findings.
argument-hint: regular | cold-read | pre-pr
---

Run the disciplined-development review engine at tier `$ARGUMENTS`:

    python3 $CLAUDE_PROJECT_DIR/disciplined-development/hooks/dd_review.py $ARGUMENTS

Then iterate per the `adversarial-review-loop` skill on any P0/P1/P2 findings until clean.
