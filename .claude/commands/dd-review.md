---
# Bundle-source variant of the /dd-review slash command. Paths point at
# the skills/disciplined-development/ tree because this repo (the source
# of the bundle) does not symlink its own skills into .claude/skills/.
# See examples/commands/dd-review.md for the consumer-side variant whose
# paths go through .claude/skills/.
description: Run tiered adversarial review at the given tier and act on findings.
argument-hint: fast | regular | cold-read | pre-pr
---

Run a tiered adversarial review at tier `$ARGUMENTS` (one of: `fast`,
`regular`, `cold-read`, `pre-pr`). The reviewer differs by tier; the output
contract is identical everywhere — native P0–P3.

`ENGINE` below is:

    python3 $CLAUDE_PROJECT_DIR/skills/disciplined-development/hooks/dd_review_runner.py

## `pre-pr` (T3) — codex gate

**Doc-dominant branch?** Run an in-session `/dd-review cold-read` first. Its
executability + doctrine-consistency angles (see "Doc-dominant cold-reads" below)
are the lens codex repeatedly wins with on doc diffs — a cheap in-session pass
pre-empts codex rounds at this gate.

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

**2. Dispatch the tier's reviewer set IN PARALLEL.** Every tier includes one
**holistic** reviewer (whole-picture catch-all); higher tiers add **angled**
reviewers. Sets are monotonic — each tier is a superset of the one below:

| Tier | Reviewers |
|------|-----------|
| `fast` | holistic |
| `regular` | holistic, correctness, rationale |
| `cold-read` | holistic, correctness, rationale, cross-file, security, necessity |

At cold-read, a **doc-dominant** diff substitutes two of these angles — see "Doc-dominant cold-reads" below.

Each subagent prompt must:
- Load the `adversarial-review` skill — invoke it via the Skill tool, or if
  unavailable read `skills/adversarial-review/SKILL.md` from disk and follow it.
- Review the **full** diff: `git diff SCOPE`. An angle *adds a focus*; it does
  NOT partition the diff. The holistic reviewer owns the whole picture so
  findings between two angles' mandates don't fall through the seams.
- Emit the `adversarial-review` contract: one finding per line,
  `- [PN] <path>:<line>: <summary>`, indented detail beneath; `No findings.`
  when clean. Nothing else starts a line with `[P0]`–`[P3]`.
- Reviewers may run on a standard model (e.g. sonnet) to conserve cost.

**Angle focus.** The tier table names each reviewer's angle; the
`adversarial-review` **Review angles** catalog defines them (single source). For
each angled reviewer, name its angle in the subagent assignment and tell it to
apply that angle's definition from the **Review angles** catalog — the subagent
already loads the skill (see the prompt requirements above). The catalog also
defines **executability** and **doctrine-consistency** for the substitution below.

**Doc-dominant cold-reads.** When the cold-read diff is predominantly doc artifacts (plans, specs, SKILL.md, command files), substitute two angles — **security → executability**, **cross-file → doctrine-consistency**. Doc-dominance is your one-line judgment when dispatching; a mixed diff keeps the code set, but add a doc-consistency note to the cross-file reviewer's prompt.

**3. Aggregate** the subagents' findings: dedupe by `file:line`, keep the
highest severity, union the detail. This is model judgment (like
`/code-review`'s aggregation), not a deterministic parse.

Then **log the round**: pipe the aggregated findings (stdin) to

    ENGINE --log-review --source command --tier $ARGUMENTS --round <n>

`<n>` is the round number — the initial aggregation is round 1; each step-4
re-run increments it. The tool derives severity, decision, and git fields from
the piped findings, so a clean round must pipe the literal `No findings.` (an
empty pipe is a usage error and logs nothing). This fires every round —
including a clean first pass, which logs one `PASS` row — and is degrade-safe:
a genuine log-write failure never blocks the loop.

**4. Iterate per the `adversarial-review-loop` skill:** address every
P0/P1/P2, then re-dispatch the same set against the new state; repeat until
clean (zero P0/P1/P2) or the iteration cap (3), then the cold-read escape.
P3 is advisory — act, or leave with on-page rationale.
Log each re-run's aggregation per step 3, incrementing `--round`.

**5. On a clean pass, record the result:**

    ENGINE --write-checkpoint $ARGUMENTS

`fast`/`regular` reset the edit counter; `cold-read` also writes the review
checkpoint. (`pre-pr` handles its own checkpoint in the pre-pr section above.)
Do not `--log-review` here — the round's aggregation (step 3) already logged
the terminal clean round; a second call would double-count it.
