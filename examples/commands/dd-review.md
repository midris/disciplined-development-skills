---
# Consumer template for the /dd-review slash command. The path below
# assumes the consumer-side install layout: the disciplined-development
# skill (and its hooks/ subdir) is symlinked under .claude/skills/ by
# install-skills.sh from a clone of disciplined-development-skills.
# Copy this file to your project's .claude/commands/dd-review.md;
# commit-or-gitignore is your choice.
description: Run adversarial review at the given tier and act on findings.
argument-hint: regular | cold-read | pre-pr
---

Run the disciplined-development review engine at tier `$ARGUMENTS`:

    python3 $CLAUDE_PROJECT_DIR/.claude/skills/disciplined-development/hooks/dd_review_runner.py $ARGUMENTS

Then iterate per the `adversarial-review-loop` skill on any P0/P1/P2 findings until clean.
