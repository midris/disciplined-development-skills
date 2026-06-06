# Plan-checkbox discipline + discipline-nudge cadence

## Why

A real session using the current bundle (captured in the meeting-pipeline
repo's deferred doc `2026-06-06-dd-skill-discipline-enforcement-gaps.md`)
drifted in two checkbox-shaped ways:

- The active plan was written with **zero** task checkboxes, so the
  `inject_plan_state` hook reported "0 / 0 top-level tasks" for ~10
  commits — an info line that got tuned out.
- Themes landed across many commits with **no plan-side ticks**, because
  there were none to tick. CLAUDE.md's "flip checkboxes in the same
  commit" rule had nothing to bite on.

The four-tier review-cadence plan (`2026-06-06-four-tier-review-cadence.md`)
already owns the **enforcement / review-debt** axis via hard blocks. This
doc covers the orthogonal **checkbox + re-ground** axis, which the four-tier
plan does not touch.

## Scope

Three changes plus two explicit non-changes. No new hooks, no new state, no
new config schema beyond one default bump.

## Changes

### 1. `lean-plan-writing` — require a task-progress checklist

The skill currently *mentions* status checkboxes (a plan is "heavier on
the order… status checkboxes") but does not require them. The session
failure was a plan that omitted them entirely and slipped through.

Add a requirement: an implementation plan MUST carry a task checklist —
one checkbox per deliverable/step — so `inject_plan_state` and the
CLAUDE.md "tick in the same commit" rule have something to track. The
requirement applies to **implementation plans**, not every markdown file
under `plans/` — specs and discussion/deferred docs (like the one that
sourced this) legitimately have no task checkboxes.

Write-time doctrine, not a hook. It's the root-cause fix: guarantee the
boxes exist so the existing runtime surfaces have signal. The skill-writing
skill governs the exact wording and where it sits relative to the upstream
`superpowers:writing-plans` scaffolding (which owns step decomposition).

### 2. `discipline_nudge` — raise cadence + add a checkbox-tick reminder

Two edits to the same hook, landing together:

- **Threshold 25 → 50.** Firing every 25 tool calls fires prematurely in
  exploration-heavy stretches (reads/greps before real work), which trains
  the model to tune the nudge out — the same failure mode the doc is
  fighting. 50 makes each firing more likely to coincide with accumulated
  work worth re-grounding against. The counter already resets at every user
  turn (`inject_plan_state` zeroes it), so it only fires inside a single
  long autonomous stretch — exactly the drift scenario. Cap the value
  around 50–60; higher risks never firing within a turn.
  - Unit caveat (recorded so it isn't re-litigated): "fall between the
    review nudges" is only a loose mental model. `discipline_nudge` counts
    **all** tool calls; T0 counts **edits**; T1/T2 count **commits**. The
    axes don't line up cleanly, so 50 is chosen as a sensible round value,
    not tuned against the review thresholds.
- **Add a checkbox-tick line** to the fixed re-ground text: remind the
  model to flip completed checkboxes in the active plan before continuing.
  Stays a generic, state-blind line — consistent with the hook's deliberate
  fixed-message design (it must not inspect plan state; that would rebuild
  the rejected output-scanner subsystem). The stateful "does this plan have
  boxes / are they stale" question stays out of this hook.

Test-first per the CLAUDE.md hook-stack rule (every `discipline_nudge`
change needs a test — biggest blast radius in the repo).

### 3. `inject_plan_state` — no change

Considered and declined. It already prints `Progress: N / M tasks`, the
next-pending line, and a `(No checkboxes found)` line every turn. It is a
UserPromptSubmit advisory surface — it can only print, not block — and the
session evidence is that advisory text on this surface gets tuned out. The
only genuinely new signal it could add is a staleness *delta* ("N commits
since the plan last changed") — a cheap git-log version needs no new state,
but it loads that same tuned-out surface. With change #1 guaranteeing boxes
exist and change #2 reminding
the model to tick them, the two original failures are covered without
touching this hook. Leave it as-is.

### 4. No discipline waiver — non-change

The source doc's item #4 proposed a structured `# DISCIPLINE-WAIVE:`
escape hatch. Declined: the `DD_SKIP_<HOOK>` env vars already provide the
manual override, and the `writing-explicit-rationale` skill already covers
putting bypass reasoning on paper for reviewers. A waiver would duplicate
both. Do not build it.

## Out of scope (source-doc items deliberately not taken)

- **#2 adversarial-review-loop cycle tracker, #6 cap-aware per-surface
  state** — separate axis; not part of the checkbox work.
- **#5 plan-checkbox-stale detector** — see change #3; the delta-line
  version was considered and declined to avoid loading the tuned-out
  surface.
- **Session-length / direction-change policy** — non-tooling; out of scope
  here.

## Relationship to other plans

- `2026-06-06-four-tier-review-cadence.md` — sibling; owns the review
  cadence + hard-block enforcement axis. No file overlap with this work
  except both touch bundle docs (`README`, `dd-config.md`, CLAUDE.md);
  sequence to avoid doc-merge churn if both land close together.
- meeting-pipeline `…/deferred/2026-06-06-dd-skill-discipline-enforcement-gaps.md`
  — the source diagnosis. This doc resolves its checkbox items (#1 take,
  #5 decline) and its waiver item (#4 decline).

## Files touched (anticipated; firmed up in the implementation plan)

- `lean-plan-writing/SKILL.md` — the checklist requirement (change #1).
- `disciplined-development/hooks/discipline_nudge.py` — threshold + text
  (change #2), with a test in the same commit.
- `disciplined-development/hooks/dd-config.md` + `examples/dd-config.json`
  — `counters.discipline_threshold` default 25 → 50.
- `disciplined-development/hooks/README.md` — cadence/threshold mention if
  it cites the old number.
- `CLAUDE.md` — only if a load-bearing reference to the discipline cadence
  or the plan-checkbox rule drifts.

## Next step

Change #1 (the `lean-plan-writing` edit) is governed by
`superpowers:writing-skills` — TDD for documentation. It is **not** a
one-line edit; it follows RED → GREEN → REFACTOR:

- **RED (baseline):** a subagent writes an implementation plan *without*
  the requirement; confirm it omits a real task checklist (or emits
  section-heading "tasks" that aren't checkboxes — the session's exact
  failure). Capture rationalizations verbatim.
- **GREEN:** add the minimal requirement that addresses those specific
  failures — implementation plans carry a one-checkbox-per-deliverable
  task checklist; specs/discussion docs are exempt.
- **REFACTOR:** re-test, close loopholes ("headings are basically
  checkboxes," "this plan is too small to need them"). Add a
  rationalization-table row per loophole found.
- Then the repo's own substitute applies (CLAUDE.md): adversarial
  cold-read of the staged branch (`dd_review.py cold-read`) before commit
  — no automated test catches a worse instruction.

Change #2 (hook + config + docs) becomes a standard test-first
implementation plan (CLAUDE.md hook-stack rule: a test in the same commit
as the `discipline_nudge` change).

Both fold into one feature branch / PR.
