# Extract the review-angle catalog from `/dd-review` into doctrine

**Status:** implemented (2026-06-16; reactivated from deferred, surfaced
2026-06-12 during PR-4 of the pre-PR-review-cadence plan).

**Open question — resolved 2026-06-16 (the plan's original lean, confirmed):**
catalog (what each angle is) → `adversarial-review`; substitution rule (swap two
angles on a doc-dominant cold-read) → stays in the `/dd-review` command.

## Problem

The review **angle catalog** — the definitions of `correctness`, `rationale`,
`cross-file`, `security`, `necessity`, and (as of PR-4) `executability` /
`doctrine-consistency` — is review *judgment*, i.e. doctrine. But it lives in the
`/dd-review` **command**, not a skill, and is **duplicated across two command
copies** (`.claude/commands/dd-review.md` bundle source +
`examples/commands/dd-review.md` consumer template). The command should be pure
orchestration (resolve scope → dispatch → aggregate → iterate → checkpoint); the
angle definitions belong with the reviewer posture in `adversarial-review`.

It is the one spot where the bundle's "skills are doctrine, hooks are dumb
triggers" split is incomplete — review doctrine living in an executable command
rather than a skill.

## Desired end state

- `adversarial-review` **owns the angle catalog** — each angle's name + what it
  looks for, in one place.
- The `/dd-review` command's dispatch table **references angles by name** and
  stops re-defining them; the per-tier reviewer sets (which angles at which tier)
  stay in the command, since that is orchestration.
- Single source: the catalog exists once (the skill), not twice (the command
  copies). The hook README's angle prose points at the skill.

## Why deferred (not folded into PR-4)

PR-4 was the locked Decision I — a minimal two-line angle addition. Extraction is
a larger change that **edits a discipline skill** (`adversarial-review`), so it
warrants its own `superpowers:writing-skills` cycle (does a reviewer dispatched by
the command still apply the right angle when the definition lives in the skill?).
Folding it into PR-4 would have bundled two changes into one PR — the
merge-boundary anti-pattern PR-3's own rule targets. So PR-4 went into the command
(status-quo home) and this extraction is logged separately.

## Open question

Where does the **doc-dominant substitution** (security→executability,
cross-file→doctrine-consistency) live — in the skill alongside the catalog, or in
the command as dispatch judgment? Lean: the *catalog* (what each angle is) goes to
the skill; the *substitution rule* (when to swap, at cold-read, on doc-dominant
diffs) is dispatch orchestration and stays in the command. Confirm during design.

## RED finding (2026-06-16)

The baseline did NOT pass — it produced a real design constraint. A reviewer told
only "apply the correctness angle" (no definition) drifted into the **necessity**
angle's lane; one given the catalog definition stayed scoped. **The angle
definition is load-bearing — a bare name is interpreted variably.** So the
command's collapsed reference must point the subagent at the named angle's
definition in the catalog, not merely name the angle.

## Cold-read adjudication (2026-06-16) — settled, do not re-litigate

A doc-dominant cold-read recurred on two findings across rounds; both refuted:

- **"Subagent isn't told how to access the catalog."** The command's first
  mandatory subagent-prompt item already prescribes it: load `adversarial-review`
  via the Skill tool, or read `skills/adversarial-review/SKILL.md` from disk. The
  in-lane executability reviewer traced this chain and returned clean; the GREEN
  test confirmed a subagent loads the skill and applies the looked-up definition.
- **"Flag executability/doctrine-consistency as substitutable in the skill."**
  Rejected — that re-injects the substitution *rule* (orchestration) into the
  skill, the anti-goal of this change. A subagent never self-selects an angle;
  the orchestrator assigns one, so an unflagged catalog entry causes no ambiguity.

## Approach (prose; implementer writes against patterns)

1. ~~`writing-skills` RED~~ — done; see "RED finding" above.
2. ~~Move the angle definitions into `adversarial-review` (new catalog section);
   collapse both command copies' "Angle focus lines" block to a
   catalog-reference that names each angle AND points the subagent at the
   skill's catalog for the definition (same commit — public-API surface).~~ done.
3. ~~Sweep `hooks/README.md` angle prose to point at the skill.~~ done.
4. ~~Boundary: hook suite green (297 passed); `/dd-review cold-read` to clean
   (3 rounds — see "Cold-read adjudication"); PR.~~ done.
