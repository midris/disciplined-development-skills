# Review-loop improvements (orphaned-safeguard angle + whole-codebase cold-read) — DEFERRED

> **For agentic workers:** REQUIRED SUB-SKILLS before implementing: `superpowers:writing-skills`
> (Item 1 edits a skill — its Iron Law "no skill change without a failing test first" is binding) and
> `superpowers:test-driven-development` (Item 2 edits engine code). Implement task-by-task.

**Status:** DEFERRED. Surfaced 2026-06-21 from the recording-slice PR (`feat/rec-6-exposure`, PR #15).

**Goal:** Make the dd-review loop catch a class of defect it missed on PR 6 — a re-introduced capability
that fails to wire an existing, purpose-built safeguard. Two independent changes: (1) a new
**orphaned-safeguard review angle**, and (2) **cold-read reviews the whole codebase**, not just the
branch diff.

## ⚠️ Cross-repo — implementation is NOT in meeting-pipeline

The dd skills + hooks in this repo are **gitignored symlinks** into the private dd-skills repo. All
edits below land in:

- **Repo:** `/Users/sidris/work/personal/code/disciplined-development-skills` (remote
  `github-personal:midris/disciplined-development-skills`).
- **Before editing:** that repo has concurrent editors (see [[skills-repo-parallel-edits]]) — check
  `git -C <ddrepo> status` is clean and you're on an intended branch first; branch for the change.
- This plan file stays in meeting-pipeline (where the incident occurred); it could instead be moved
  into the dd-skills repo if you prefer the plan to live with the code.

## Motivating incident (the root cause this fixes)

PR 6 re-introduced recording start/stop (HTTP + menu + CLI) as thin adapters over the engine. A
purpose-built record-start permission gate — `PermissionCoordinator.ensureRecordingPermissions()`
(documented in its own header: *"the recording-lifecycle caller is responsible for invoking this gate
before every `CaptureWorker.start(writingTo:)` call … the redesigned lifecycle reinstates the call",*
with *"no type-level enforcement — the contract is by convention"*) — was **never wired in**. It had
**zero callers** (dead code). The requirement lived in a code doc-comment + a completed step-8
master-spec entry, **not** in the recording-slice plan or the control-plane spec that governed the work,
so every plan-anchored review (per-task + the opus whole-branch review) had nothing to check it against.
The external Codex pre-PR review caught it — by reasoning over the **whole codebase** (finding the
orphaned, documented-as-required API), an angle the diff-anchored reviews lacked.

The two changes below are the two halves of why Codex caught it and we didn't: the **angle** (what to
look for) and the **whole-codebase scope** (the visibility that makes the angle work — you cannot prove
an API has zero callers from a branch diff alone). They reinforce each other; the angle is most potent
in the whole-codebase cold-read tier.

---

## Item 1 — Orphaned-safeguard / unwired-contract review angle

**File:** `<ddrepo>/skills/adversarial-review/SKILL.md` — the `## Review angles` section (≈ line 90;
angles are specialized lenses added on top of the always-on baseline, e.g. the existing `durability`
angle). Add one new angle here.

**What the angle must capture (prose contract — write the skill text against the baseline test, do not
transcribe from here):** when a change **exposes, re-introduces, or adds a caller path to** a capability,
check whether the codebase already has a **purpose-built safeguard/integration** the new code is
supposed to use but doesn't. Two detection moves:
- **Documented-contract search** — grep the codebase for APIs whose own docs declare they must be
  invoked: phrases like *"caller is responsible"*, *"must call before"*, *"call … before every"*,
  *"reinstates the call"*, *"must not start"*, *"gate"*, *"by convention"*. For each, verify a live
  caller exists on the path the change touches.
- **Orphaned-public-API check** — a `public` function documented as a required gate/validator with
  **zero callers** is a red flag (the PR-6 `ensureRecordingPermissions()` case exactly).

Trigger condition (for the angle's "applies when" clause): the diff adds or re-introduces an
entry point to an existing subsystem (a new route/handler, menu action, CLI command, or a re-enabled
lifecycle). Skip for purely internal refactors that add no caller path.

**Iron Law (binding — `superpowers:writing-skills`):** this is a skill change, so it needs RED→GREEN→
REFACTOR, not a blind edit:
- **RED (baseline):** dispatch a reviewer subagent on a diff that adds a start/entry path but omits a
  call to an existing documented-as-required gate, **without** the new angle in its skill. Use the real
  PR-6 shape as the scenario: a `POST /recordings` + menu Start that call `engine.start` while a
  documented, zero-caller `ensureRecordingPermissions()` exists. Confirm the reviewer **misses** it
  (that's the failing test — if the baseline already catches it, the angle adds nothing; stop).
- **GREEN:** add the angle; re-run the same scenario; confirm the reviewer now flags the orphaned gate.
- **REFACTOR:** close any rationalization the reviewer used to dismiss it; keep the angle to one lens
  (it adds a check, it does not narrow the baseline).

**Done when:** the baseline scenario fails without the angle and passes with it (documented in the
change), and the angle reads as one additional lens consistent with the section's existing angles.

---

## Item 2 — Cold-read reviews the whole codebase, not the branch diff

**File:** `<ddrepo>/skills/disciplined-development/hooks/dd_review_runner.py`,
`_handle_resolve_scope` (≈ line 246). Today it maps (≈ lines 253-254):
`fast → HEAD`; `regular / cold-read / pre-pr → <fork-base-sha>..HEAD`. So **cold-read currently
reviews the fork-base diff** — the same diff-anchored view that missed the orphan.

**What:** split `cold-read` out of the `regular/cold-read/pre-pr` group so `--resolve-scope cold-read`
resolves to a **whole-codebase** scope (all tracked files — e.g. derived from `git ls-files` / a
full-tree sentinel), not a `<base>..HEAD` range. `regular` and `pre-pr` stay diff-scoped.

**Non-trivial design implication (flag — the implementer must resolve, this plan does not):** the
resolved scope flows into the reviewer/codex dispatch as the thing-under-review. Every other tier hands
the reviewer a **diff**; a whole-codebase cold-read hands it the **full file set**, which is a different
and far larger input. The implementer must:
- trace where the `--resolve-scope` output is consumed (the dispatch that feeds the reviewer the diff)
  and adapt it to feed a full-tree review — likely a *"review these files / this codebase"* framing
  rather than *"review this diff"*;
- account for the token/cost blow-up (whole codebase ≫ a branch diff) — bound or chunk if needed, and
  if anything is sampled/truncated, **log what was dropped** (silent truncation reads as full coverage);
- keep the empty-diff early-exit (≈ line 16) from wrongly short-circuiting a whole-codebase run.

**Also update:** the scope-mode comments (≈ lines 69-71, 253-254) and any cold-read scope description in
the `dd-review` skill doc (locate it under `<ddrepo>/skills/` — not symlinked into this project) so the
docs match the new behavior (`sweeping-stale-references`).

**Tests required (the runner has a `tests/` suite — e.g. `tests/test_pre_pr_review.py`):**
- `--resolve-scope cold-read` returns the whole-codebase scope (not a `<fork-base>..HEAD` range);
- `--resolve-scope regular` and `--resolve-scope pre-pr` are unchanged (still fork-base range);
- `--resolve-scope fast` unchanged (`HEAD`).

**Done when:** `python3 dd_review_runner.py --resolve-scope cold-read` prints a whole-codebase scope, a
cold-read review actually reads the full tree (not just changed files), and the dispatch + docs + tests
reflect it.

---

## Notes

- **Order independence:** the two items are independent and can land as separate PRs in the dd-skills
  repo. If doing both, Item 1's angle gains most of its value once Item 2 ships (whole-codebase
  visibility is what lets the orphaned-API check prove zero callers) — but Item 1 is still correct
  against the working-tree/`regular` scope, so neither blocks the other.
- **Related, but out of scope for this plan (do not implement here):** the deeper plan-hygiene lesson —
  when carving a slice plan out of a master spec, enumerate the superseded path's cross-cutting
  safeguards and carry each as a task or an explicit deferral so a by-convention code contract can't
  silently drop. That is a process/`CLAUDE.md` change, not a dd-skills change; raise separately if
  wanted. Captured here only as the root-cause context.
