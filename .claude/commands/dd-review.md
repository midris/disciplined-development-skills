---
# Bundle-source variant of the /dd-review slash command. Paths point at
# the top-level disciplined-development/ tree because this repo (the source
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

    python3 $CLAUDE_PROJECT_DIR/disciplined-development/hooks/dd_review_runner.py

## `pre-pr` (T3) — codex gate

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

Each subagent prompt must:
- Load the `adversarial-review` skill — invoke it via the Skill tool, or if
  unavailable read `adversarial-review/SKILL.md` from disk and follow it.
- Review the **full** diff: `git diff SCOPE`. An angle *adds a focus*; it does
  NOT partition the diff. The holistic reviewer owns the whole picture so
  findings between two angles' mandates don't fall through the seams.
- Emit the `adversarial-review` contract: one finding per line,
  `- [PN] <path>:<line>: <summary>`, indented detail beneath; `No findings.`
  when clean. Nothing else starts a line with `[P0]`–`[P3]`.
- Reviewers may run on a standard model (e.g. sonnet) to conserve cost.

Angle focus lines (append exactly one to the corresponding reviewer):
- **correctness** — logic, boundary / off-by-one, wrong-variable, control-flow bugs.
- **rationale** — verify every docstring / comment / "safe" / "trusted" claim against the actual code.
- **cross-file** — divergence from canonical modules, broken imports, caller / contract drift.
- **security** — path traversal, injection, unvalidated input, unsafe path building.
- **necessity** — cut what doesn't earn its place. Code: dead code, over-engineering, premature abstraction / config (Principle 7). Prose: padded / verbose docs + comments — this reviewer also loads the `concise-writing` skill.

**3. Aggregate** the subagents' findings: dedupe by `file:line`, keep the
highest severity, union the detail. This is model judgment (like
`/code-review`'s aggregation), not a deterministic parse.

**4. Iterate per the `adversarial-review-loop` skill:** address every
P0/P1/P2, then re-dispatch the same set against the new state; repeat until
clean (zero P0/P1/P2) or the iteration cap (3), then the cold-read escape.
P3 is advisory — act, or leave with on-page rationale.

**5. On a clean pass, record the result:**

    ENGINE --write-checkpoint $ARGUMENTS

`fast`/`regular` reset the edit counter. `cold-read` also writes the review
checkpoint (`review.checkpoint = HEAD`) — this write is what unblocks the T3
pre-PR gate on retry; skipping it leaves the gate shut. (`pre-pr` handles its
own checkpoint in the pre-pr section above.)
