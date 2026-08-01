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

**Formal run (2026-07-04, skill @ `db26297`).** Commit-pressure scenario,
protocol-style (agent reads the skill file as sole doctrine; explicit "no CLAUDE.md,
no repo conventions" framing; sunk-cost + reviewer-waiting pressure; the ask pushes
rationale into the commit message). New text **5/5** artifact-first — comment at the
decision site (+ plan note in 4/5), commit body additive/citing, one rep quoting
"reviewers read the tree, not the log" back verbatim; **zero over-fire** (every rep
still explained in the body as asked). Pre-edit control **3/3 also artifact-first** —
the original body already binds when read in full, so this protocol structurally
cannot reproduce the description-layer loophole (an agent acting on the description
without reading the body). Standing evidence base for the edit therefore remains the
loophole analysis + the owner-watched incidents; these runs establish no-regression
and correct new-text behavior. True long-context in-situ pressure stays untestable in
this harness.

## On edits

Re-run the commit-pressure scenario (correct placement + the over-fire check: body
still cites the artifact) in both a with-CLAUDE.md and a bare consumer. Keep the
"reviewers read the tree, not the log" mechanism line — it is the enforcement teeth.

## Trigger-only description routing (2026-08-01)

**Matrix.** Route five prompts from metadata only: active-plan implementation with delegation; padded README tightening; SKILL.md shortening; plan deferral with PR-only rationale; and a routine convention-preserving rename.

**Pre-edit control: 3/3 PASS.** All evaluators selected `writing-explicit-rationale` for the plan deferral whose rationale lived only in the PR and did not select it solely for a routine convention-preserving rename.
The description edit is a trigger-only clarity and length refactor, not a routing fix.

**GREEN requirements.** Preserve the deferral, oversight-risk, defensible-alternative, re-litigation, and non-durable-rationale triggers while keeping routine self-evident choices out of scope.

**GREEN result: 3/3 PASS.** All three independent metadata-only evaluators selected the skill for PR-only deferral rationale and did not select it solely for the routine convention-preserving rename.
