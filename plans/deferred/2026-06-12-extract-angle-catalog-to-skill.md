# Deferred — Extract the review-angle catalog from `/dd-review` into doctrine

**Status:** deferred (surfaced 2026-06-12 during PR-4 of the pre-PR-review-cadence
plan). Not scheduled — re-open when the duplication or discoverability cost bites.

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

## Approach (prose; implementer writes against patterns)

1. `writing-skills` RED: confirm a command-dispatched reviewer, given only the
   catalog-by-name reference, still applies the correct focus (baseline may
   already pass — if so, this is discoverability/dedup, not a behavior fix; treat
   like PR-2/PR-3's no-baseline judgment).
2. Move the angle definitions into `adversarial-review`; collapse both command
   copies' "Angle focus lines" block to name-references (same commit — public-API
   surface).
3. Sweep `hooks/README.md` angle prose to point at the skill.
4. Boundary: hook suite green; `/dd-review cold-read` to clean; PR.
