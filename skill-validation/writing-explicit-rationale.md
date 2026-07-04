# writing-explicit-rationale — validation

Record per `superpowers:writing-skills`. First entry covers the 2026-07-03
reviewer-visibility edit.

## Reviewer-visibility loophole closure (2026-07-03)

**Edit:** description no longer lists commit bodies as an application surface and
gains the trigger "rationale about to land only in a commit message or PR
description"; the Role owned-scope drops commit bodies; the Scope closer names the
enforcement mechanism ("reviewers read the tree, not the log — rationale only in a
commit message is invisible to the review that will re-litigate it"); the
commit-body rationalization row sharpened to the same mechanism.

**RED evidence:** owner-watched recurring failure — models putting decision
rationale in commit messages where the whole-repo reviewer cannot see it. Loophole
analysis: the description itself sanctioned commit bodies as a rationale home
(agents act on descriptions and skip bodies — SDO), and the skill's motivation was
exclusively the future reader; the immediate consequence (gating reviewer can't see
it) was unstated. No reproducible in-harness RED: baseline arm (ambient consumer
context, original skill) passed 5/5 — steno's CLAUDE.md commit rule enforces the
same behavior ambiently, so single-shot scenarios can't isolate the skill there.

**Method + results:** commit-pressure single-shot (user explicitly instructs
"explain the choice in the commit message"), sonnet, hand-read. New wording:
**8/8 correct** — durable rationale to a code comment at the decision site + plan
note, commit body citing or additive; **zero over-fire** (every rep still satisfied
the user's instruction additively — the edit must never read as "commit bodies may
carry nothing"); low variance (one converged shape).

**Pending for formal GREEN:** a discriminating pressure run in a consumer WITHOUT a
CLAUDE.md restating the commit-body rule (isolates the skill's contribution), plus
long-context/sunk-cost pressure — the watched failure is a pressure phenomenon.

## On edits

Re-run the commit-pressure scenario (correct placement + the over-fire check: body
still cites the artifact) in both a with-CLAUDE.md and a bare consumer. Keep the
"reviewers read the tree, not the log" mechanism line — it is the enforcement teeth.
