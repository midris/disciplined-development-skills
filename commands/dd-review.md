---
# Consumer template for the /dd-review slash command. Paths below assume the
# consumer-side install layout: the disciplined-development skill (and its
# hooks/ subdir) plus the companion skills are symlinked under .claude/skills/
# by install-skills.sh from a clone of disciplined-development-skills.
# Copy this file to your project's .claude/commands/dd-review.md;
# commit-or-gitignore is your choice.
description: Run tiered adversarial review at the given tier and act on findings.
argument-hint: fast | regular | cold-read | pre-pr
---

Run a tiered adversarial review at tier `$ARGUMENTS` (one of: `fast`,
`regular`, `cold-read`, `pre-pr`). The reviewer differs by tier; the output
contract is identical everywhere — native P0–P3.

`ENGINE` below is:

    python3 $CLAUDE_PROJECT_DIR/.claude/skills/disciplined-development/hooks/dd_review_runner.py

## `pre-pr` (T3) — codex gate

**Doc-dominant branch?** Run `/dd-review cold-read` in-session first — its
**executability** angle is the lens codex wins with on doc diffs, so a cheap pass
pre-empts codex rounds here.

Run the engine directly. It dispatches `codex review`, severity-scans the
output, hard-blocks on any P0/P1/P2, and on a clean pass writes the checkpoint
and resets the edit counter itself:

    ENGINE pre-pr

Iterate per the `adversarial-review-loop` skill on any findings until clean.
Do not hand-roll the codex call or the checkpoint — the engine owns T3.

## `fast` / `regular` / `cold-read` (T0–T2) — in-session subagents

These tiers run as **adversarial-review subagents** dispatched via the Task
tool (in-session, on the subscription — never `claude -p`). Steps:

**1. Resolve the diff scope** (do NOT guess it):

    ENGINE --resolve-scope $ARGUMENTS

This prints a single `git diff` argument — `HEAD` for `fast` (working tree vs
HEAD, catching in-flight edits) or `<fork-base>..HEAD` otherwise. Call it
`SCOPE`; pass it to every reviewer.

**2. Dispatch the tier's reviewer set IN PARALLEL.** Each tier adds depth:

| Tier | Reviewers |
|------|-----------|
| `fast` | holistic |
| `regular` | holistic + consistency |
| `cold-read` | holistic + every angle the artifact calls for (`adversarial-review` → "When to apply") |

The **holistic** reviewer applies the full `adversarial-review` baseline (bugs,
rationale, necessity); each angled reviewer applies one angle from the skill.

Each subagent prompt must:
- Load `adversarial-review` (Skill tool, or read `.claude/skills/adversarial-review/SKILL.md`).
- Review the **full** diff `git diff SCOPE` — an angle adds a focus, it never narrows scope.
- Emit the contract: one finding per line, `- [PN] <path>:<line>: <summary>`, detail
  indented; `No findings.` when clean. Nothing else starts a line with `[P0]`–`[P3]`.
- May run on a standard model (e.g. sonnet) to save cost.

**3. Aggregate** the findings: dedupe by `file:line`, keep the highest severity,
union the detail — model judgment, not a deterministic parse.

Then **log the round** — pipe the aggregated findings to:

    ENGINE --log-review --source command --tier $ARGUMENTS --round <n>

`<n>` starts at 1 and increments each step-4 re-run. The tool derives severity,
decision, and git fields from the piped findings, so a clean round must pipe the
literal `No findings.` (an empty pipe logs nothing). Fires every round — a clean
pass logs one `PASS` row — and never blocks the loop on a log-write failure.

**4. Iterate per `adversarial-review-loop`:** address every P0/P1/P2, re-dispatch
the same set against the new state, repeat until clean or the iteration cap (3),
then the cold-read escape. P3 is advisory — act, or leave with on-page rationale.
Log each re-run per step 3, incrementing `--round`.

**5. On a clean pass, record the result:**

    ENGINE --write-checkpoint $ARGUMENTS

`fast`/`regular` reset the edit counter; `cold-read` also writes the review
checkpoint. (`pre-pr` handles its own checkpoint in the pre-pr section above.)
Do not `--log-review` here — the round's aggregation (step 3) already logged
the terminal clean round; a second call would double-count it.
