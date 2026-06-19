# Deferred — `adversarial-review-loop` "find the pattern, attack the root" move

**Parked 2026-06-19**, surfaced during PR 2 of the recording slice (the event-log substrate). A
loop meta-strategy to add to the `adversarial-review-loop` skill: when an **external** reviewer
(codex / a CI bot / a pre-PR gate) keeps surfacing **new-but-related** findings round after round,
step back, name the shared root, and audit that whole axis in one pass — instead of grinding
reactive single-finding fix→re-review cycles. Skill lives in the **private
`disciplined-development-skills` repo** (symlinked into `.claude/skills/`), so the edit lands there
— see Execution caveats.

**Governing:**
- Skill to edit: `.claude/skills/adversarial-review-loop/SKILL.md` — refines its "Productive
  iteration vs Drift" model and the iteration cap / cold-read escape.
- Related artifact: `plans/deferred/2026-06-19-adversarial-review-durability-angle-deferred.md` —
  that adds ONE axis (a durability lens); THIS adds the general move of *finding* the axis. They
  compose: this move says "name the axis and attack it"; the durability angle is a pre-made axis.
- Skill-authoring rules: `superpowers:writing-skills` — Iron Law (no skill edit without a failing
  test first), Match the Form to the Failure, token efficiency (this is a frequently-loaded skill).
- Real-world evidence (the watched failure): PR 2's 6 pre-PR gate rounds, in the SDD ledger
  (`.git/sdd/progress.md`) and the `feat/rec-2-event-log` history.

## Why this exists (the watched failure)

PR 2's pre-PR gate ran **six** rounds. Each round found **new, real** findings (not drift, not
re-litigation): round 1 an open-failure error leak; round 2 an encode crash + a blank-line read +
a fresh-file fsync gap; round 3 a parent-fsync throw; round 4 a torn-tail read + an fsync rollback;
round 5 a parent-fsync retry gap. By the current skill's rule this is **textbook "productive
iteration"** — new issues on new surface each cycle — so the rule says *keep going*. And it would
have kept going: each fix was correct, each next finding was genuinely new.

But viewed **as a set**, 7 of those findings were one thing — the crash/failure/partial-state paths
of a source-of-truth store. They only *looked* unrelated (encode vs torn-tail vs fsync are
different functions and symptoms); they shared a root the artifact had never adversarially examined.
The reactive loop chased symptoms; it converged only after a human (Simon) prompted a step-back that
named the axis and a single comprehensive audit attacked it. The loop went 6 rounds; the root-attack
took ~1–2 to converge.

**The gap in the current skill:** its "Productive vs Drift" test has two outcomes — productive (new
surface → continue) or drift (re-litigation/trivial → cap/escape). It has no name for the third,
most expensive case: **productive-looking iteration whose new findings share an unexamined root.**
"New surface each round" reads as *continue*, so the agent grinds. The skill already hints at this
("the same *kind* of finding recurring across cycles means the class-sweep was incomplete") but
scopes it to same-*kind* findings; the trap is findings that are surface-*different* yet
root-*same*.

## The principle

When review iteration accumulates findings — **especially with an external/CI/codex reviewer that
does a fresh deep pass each round** — periodically test the findings *as a set*, not one at a time:

> **Can the findings so far be named as instances of one root cause / dimension / axis?**
> (e.g. all failure-path/crash-consistency, all concurrency, all input-validation, all error-
> contract, all auth-boundary.) If yes — even if each finding is individually new and real — the
> loop is chasing symptoms of an unexamined axis. **Stop fixing findings one at a time. Name the
> axis, enumerate the whole axis against its invariants, and fix it comprehensively in one pass.**
> Then re-run: the reviewer has nothing left on that axis because you closed the surface it was
> probing, not the spots it happened to name.

This is a **higher-order class-sweep**: the skill's existing step-1 sweep fixes every instance of
one *named* class within a round; this detects a class spanning *rounds and surface-different
symptoms* and audits it proactively. It is distinct from:
- **Drift** (re-litigation / trivia) → the existing cap + cold-read escape still applies.
- **The cold-read escape** (at the cap, get *fresh eyes*) → the root-attack is **proactive, before
  the cap**, and uses *your own* comprehensive audit, not a new reviewer.
- **Genuinely scattered findings** (no nameable shared root) → keep running the normal loop.

## Proposed skill edit (draft — final wording set by the RED/GREEN below, per the Iron Law)

In `adversarial-review-loop/SKILL.md`:

1. **Add a short section** (working title "Find the pattern, attack the root") stating the move
   above, keyed to an observable predicate so it doesn't reopen negotiation (writing-skills "Match
   the Form to the Failure"): *trigger = across ≥2 cycles, the new findings can be named as
   instances of one root cause/axis.* The action: name the axis → enumerate every site/path against
   the axis's invariants → fix in one pass → re-run. Cross-reference the `durability` angle as a
   worked example of a named axis.
2. **Refine "Productive iteration vs Drift"** to a trichotomy: productive-and-scattered (continue),
   drift (cap/escape), and **productive-but-shared-root (attack the root now)**. Make explicit that
   "new surface each round" is NOT sufficient evidence of healthy iteration — it must also be
   *root-scattered*.
3. **Rationalization-table rows** (the excuses this session would have produced):

   | Excuse | Reality |
   |---|---|
   | "Each round found a NEW, real issue — that's productive, keep going." | New + real + sharing one root = symptoms of an unexamined axis. Name the axis and audit it; don't fix the Nth symptom. |
   | "These findings are unrelated — different files, different symptoms." | Surface-different, root-same. Test whether one axis name covers them before deciding they're scattered. |
   | "The external reviewer will just confirm green next round." | An external reviewer does a fresh deep pass each round; it keeps finding new instances on the open axis until the axis is closed. |
   | "Stepping back to audit is slower than fixing the finding in front of me." | Six reactive rounds vs one audit. The audit is faster once ≥2 rounds share a root. |

4. **Description / triggers** (writing-skills: triggers-only, never a workflow summary): extend to
   fire when *successive review rounds keep surfacing new findings* — the symptom that should prompt
   the step-back. Keep the addition compact; do not summarize the move into the description.

## RED / GREEN test protocol (required before the edit ships — Iron Law)

This is a discipline/judgment edit, so it needs a pressure scenario, not just a wording check.

1. **RED (baseline, current skill).** Give a fresh agent the current `adversarial-review-loop` skill
   and a simulated external-reviewer loop: a stub "reviewer" that, each round, returns ONE new, real,
   surface-different finding all drawn from a single hidden axis (e.g. a file-store with: unwrapped
   error type → then a silent-drop read → then a no-rollback write → then a torn-tail read). Drive
   3–4 rounds. Expect the baseline agent to fix each finding and re-submit (grind), never stepping
   back to name the axis. Record that it keeps looping. (This session is the real-world instance of
   that baseline — cite it.)
2. **GREEN (with the edit).** Same loop, skill now carrying the pattern-attack move. Expect the agent
   to, by round 2–3, name the shared axis, audit the whole axis, and fix the remaining instances in
   one pass — so the next reviewer round is clean. Success = converges in materially fewer rounds and
   the agent explicitly names the axis.
3. **Method (writing-skills):** include a no-guidance control; ≥5 reps (agents vary); read the
   transcripts by hand (did it *actually* name an axis and audit it, or just fix faster?); a control
   that already steps back means there's nothing to add — stop.
4. **Negative case (don't over-fire):** a loop whose findings are genuinely scattered (no nameable
   shared axis) must NOT trigger a spurious "axis audit" — verify the with-edit agent continues the
   normal loop there. (Guards against the move degrading into "always do a big audit.")

## Execution caveats

- **Skill repo:** the edit lands in the private `disciplined-development-skills` repo (the
  `.claude/skills/...` here is a gitignored symlink). Concurrent editors — check branch/clean state
  before any git op, re-run `install-skills.sh` against this project after.
- **Compose, don't duplicate:** land this alongside (or after) the `durability` angle plan; this
  skill cross-references that angle as a worked example, and both are TDD'd per writing-skills.
- **Scope check before building:** if a baseline control already steps back and names the axis
  without the edit, there's nothing to add — stop. The PR-2 evidence says it won't (I ground 6
  rounds until prompted), but re-confirm on the constructed scenario.
