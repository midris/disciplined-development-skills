# dd-review loop improvements — deferred

**Status:** deferred (parked follow-up). Updated 2026-06-16 with code-change-session
validation + two new items (6, 7) and a config mitigation already applied
(`.claude/dd-config.json`: cold-read block 8→11, `fast` 30/60→50/100, `regular` floor 30→50).
**Target repo:** the private `disciplined-development-skills` repo
(`github-personal:midris/disciplined-development-skills`) — the wiring lives in
`dd_review_runner.py`, the `dd-review` SKILL, and the PostToolUse edit-counter hook,
all symlinked into this project under `.claude/skills/`. This plan lives in
meeting-pipeline for visibility; it implements against dd-skills.

**Origin:** observations from the 2026-06-15 ML-worker spec session — a doc-heavy
brainstorm + spec run through `fast` tier plus the Gate-3 commit hook and four
external Codex rounds.

## Why deferred

- The observations are from **one doc-dominant session**. Before changing the wiring,
  confirm each pattern holds (or differs) on a **code-change** session — the cadence and
  tier-depth findings especially may behave differently when edits are code.
- dd-skills has **concurrent editors** ([[skills-repo-parallel-edits]]) — coordinate
  branch / clean state before landing any of these.
- None of these blocked the session; each had a working manual workaround.

References are by function / behaviour name, not line number — the runner drifts under
concurrent editing (the same line-number-fragility lesson this very session hit).

## Code-change-session validation (2026-06-16, step-5 PR)

The 2026-06-16 step-5 implementation (Swift + Python, 19 commits, 2 in-session cold-reads
+ the Gate-5 round) is the code-change session the "Why deferred" caveat asked for. Result:
**the cadence/cost patterns hold on code too — and a commit-level analog surfaced that the
doc session (fewer commits) didn't.** Per item:

- **Item 1 (scope blind spot) — confirmed, and broader on code.** The same gap bit as
  *uncommitted modifications*, not only untracked new files: the Gate-5 cold-read's default
  committed scope (`base..HEAD`) omitted the uncommitted remediation fixes + docs. Worked
  around by reviewing `git diff base` (no `..HEAD`) to fold in the working tree. The fix
  should union committed + uncommitted + untracked-not-ignored (ties to new item 7).
- **Item 2 (per-edit nudge) — confirmed on code.** The T0 edit-nudge fired ~30→50 during a
  multi-file Gate-5 fix batch — the every-edit-after-threshold cadence is noise *mid-
  remediation*, not just mid-authoring. Config mitigation landed this session
  (`fast.nudge_threshold` 30→50 in `.claude/dd-config.json`); the hardcoded every-edit
  cadence is the still-open code part. **Add to the direction: also suppress the nudge while
  a review/remediation cycle is active** (the review is already being acted on).
- **Item 5 (contract-coverage) — second confirming instance, now on code.** The cold-read
  caught a Swift↔Python parity gap: spec Decision G guarantees the venv always lives at the
  App Support root (`UV_PROJECT_ENVIRONMENT`); Swift `UvBootstrap.sync` set it but the Python
  `env update/repair` mechanism did **not** — so `repair` would provision the wrong venv,
  and no test would have failed. Exactly the "guarantee A not delivered by mechanism B" shape.
  Here a parity-checking cross-file reviewer caught it, but it strengthens the case for a
  standing contract-coverage angle (it shouldn't depend on a reviewer happening to diff parity).
- **Items 3 / 4 — not exercised standalone this session** (per-task two-stage review + cold-read
  were used rather than a bare `fast`; codex pre-pr not yet run at time of writing). Depth still
  mattered: the cold-read caught what per-task review didn't (a pipe deadlock, the parity bug).

See project memory [[dd-review-loop-timings]] for the timings write-up.

## Improvements (prioritised)

### 1. [P1] Untracked-file scope blind spot — can silently pass on new files

**Problem.** `--resolve-scope fast` emits the literal `HEAD`, and reviewers diff
`git diff HEAD`, which **omits untracked files**. When the deliverable is a brand-new
file (this session's entire spec), the resolved scope is empty → a dispatched reviewer
sees nothing → returns a confident `No findings.` This is the worst failure mode: looks
reviewed, reviewed nothing. The session only got coverage because the gap was noticed
and the reviewer was pointed at the file manually.

**Direction.** Scope resolution should include untracked-but-not-ignored files — union
`git diff HEAD` with `git ls-files --others --exclude-standard`, or `git add -N` the
untracked set before diffing. Confirm the chosen approach flows through to the
**pre-stuffed diff** the reviewers actually receive (not just the printed scope arg).
Check the review tiers' `base...HEAD` range for the same gap — lower risk since those
run post-commit, but worth confirming.

**Acceptance.** A session whose only change is one new untracked file produces a
non-empty review scope, and the dispatched reviewer's prompt contains that file's
content.

### 2. [P2] Per-edit nudge cadence ignores doc-vs-code

**Problem.** The edit counter increments uniformly per edit; the PostToolUse nudge
("Run `/dd-review fast`") fired ~30+ times during active spec drafting (counter reached
~54 before the checkpoint reset). A spec being actively written does not need a review
prompt on every keystroke-edit — it's noise mid-authoring, and it trains the operator to
ignore the nudge.

**Already config-tunable (no code):** raising the onset is just bumping
`review_tiers.fast.nudge_threshold` in `dd-config.json` (default 30). That delays
*when* nudging starts but not the every-edit cadence after — the "repeated nudging from
threshold upward" is hardcoded.

**Direction (needs code).** The cadence-shape + doc-vs-code distinction is what isn't
configurable. One of (decide at implementation time): weight doc-only edits below code
edits; nudge every N edits above threshold rather than every edit; or suppress nudges
during an active brainstorming / plan-writing flow (a mode the operator or a skill can
set). The goal is to stop nudging mid-authoring while **still** nudging before commit / PR.

**Acceptance.** A doc-drafting burst does not emit more than ~1 nudge before a natural
checkpoint (commit, or an explicit review request).

### 3. [P2] Tier-depth ceiling on load-bearing artifacts — make it explicit

**Problem.** `fast`-holistic reliably caught internal-consistency bugs (enum gaps, a
catalog-category that would crash construction, a factual error introduced mid-session).
It did **not** catch the architecture/executability issues — typed-config requirement,
`env update` vs the sealed bundle, the first-party-wheel gap, the swap double-contract —
all of which external Codex caught. Citation drift was caught only by the Gate-3 commit
hook, not the review. So `fast` alone under-reviews a load-bearing spec; it took
fast + Codex + Gate-3 together. The risk is anyone treating a `fast`-clean as sufficient.

**Direction.** Advisory, not forced: state in the `dd-review` SKILL that a `fast`-clean
is **not** sufficient for load-bearing specs/plans, and name when to escalate
(regular / cold-read, or a Codex / pre-pr gate). Optionally a heuristic that *suggests*
escalating tier when the diff is a spec/plan artifact. Keep it a recommendation.

**Acceptance.** The skill text states the depth ceiling and the escalation trigger.

### 4. [P3] Doc-dominant angle substitution only engages at cold-read

**Problem / watch-item.** The doc-dominant angle swap (security→executability,
cross-file→doctrine-consistency) only applies at cold-read. At `fast`/`regular`, a
doc diff gets the generic angle set. This session it didn't bite — the holistic reviewer
did executability + doctrine work organically — so this is a low-priority watch-item, not
a confirmed defect.

**Direction.** Optionally extend doc-dominant detection to `regular`. Leave parked until
a session shows the generic angles actually missing something a doc-dominant angle would
have caught.

### 5. [P2] Add a "contract-coverage" review angle

**Problem (confirmed defect — a Codex round caught what a 6-reviewer cold-read missed).**
A spec stated a guarantee — the seed/repair runner must recover a "blank, broken, **or
corrupt**" venv — but the plan task fulfilled it with a *weaker* mechanism (a presence
check on `venvPython`), and the task's test list had **no case that would fail if the
guarantee were violated**. The detection *looked like* it addressed usability but didn't
deliver it. None of the six cold-read angles caught it:
- **correctness** reviews the task in isolation — the presence check is self-consistent;
- **doctrine-consistency** was hunting *literal* stale references (string drift), not
  "does mechanism B fulfill guarantee A";
- **executability** asks "can an implementer act?" — yes, they'd build the wrong thing
  that passes the stated tests.

This is **semantic cross-artifact inconsistency**: a guarantee in artifact A not actually
delivered by the mechanism in artifact B that claims to satisfy it. It is a recurring
shape (same loop-of-fixes as the stale-ref rounds), so it earns a standing angle.

**Direction.** Add a **contract-coverage** angle (a.k.a. guarantee-tracing /
negative-space test adequacy). Its prompt: *enumerate every guarantee / invariant /
"must" the spec states; for each, find the task AND a test whose failure would catch a
violation; flag any guarantee where (a) the mechanism is weaker than the guarantee, or
(b) no described test would fail if it were violated.* Two ways to land it (pick at
implementation time):
- **Cheapest:** fold the contract-coverage pass into the **doctrine-consistency** angle's
  prompt (it is a consistency concern, just semantic not literal) — no extra reviewer.
- **Dedicated:** a 7th angle gated to spec→plan and spec→code (implementation-against-spec)
  diffs, so it doesn't tax every `fast` run.

**Acceptance.** Given a spec guarantee and a plan/code mechanism weaker than it (with no
violation-catching test), the angle flags it; a plan whose every guarantee traces to a
task + a failing-test gets `No findings.`

### 6. [P2] Commit-count gates over-count low-risk commits (the commit-level analog of item 2)

**Problem (surfaced on the code session).** The T2 commits-since-cold-read nudge and the
`commit_block` hard ceiling count **every commit equally**. This project's commit discipline
deliberately produces small, separated commits — per-task `feat:`, separate `docs:`
checkbox-ticks, host-verify records. So ~half a code chunk's commits are docs/tick commits
carrying ~zero risk, and the hard block (default 5; project moved 5→8→11) fired at roughly
**4 code-commits-worth of change**, mid-chunk. This is item 2's doc-vs-code distinction, one
level up — at commits instead of edits.

**Already config-tunable (no code):** raise `cold_read_escalation.hard_block_threshold`
(project moved it 8→11 on 2026-06-16). Mitigates but does not fix — the count is still raw
commits, so a docs-heavy chunk still trips early.

**Direction (needs code).** Exclude docs-only commits from the commits-since-cold-read count
(a commit whose diff touches only `*.md` / `plans/` / docs), or weight by net non-docs lines.
Keep the *nudge* eager; widen only what counts toward the *block*. Mirror the same doc-vs-code
weighting item 2 wants for edits, so the two cadence gates stay consistent.

**Acceptance.** A chunk of N code commits interleaved with M docs/tick commits trips the
block on the Nth code commit, not the (N+M)th commit.

### 7. [P2] Remediation commits blocked at the review / pre-PR boundary

**Problem (confirmed defect this session).** The `commit_block` hard ceiling fired exactly at
the Gate-5 boundary — where the cold-read **itself produces the remediation commits** — so the
agent could not land the fixes (blocked), and the documented escape `DD_SKIP_COMMIT_BLOCK` is
human-set: an inline `DD_SKIP_COMMIT_BLOCK=1 git commit …` does **not** reach the PostToolUse
hook (it reads its own inherited environment, not the command's inline prefix). Escaped by
reviewing the *uncommitted working tree* → `--write-checkpoint` → commit — a backwards dance
(checkpoint a state, then add the commits it was supposed to gate).

**Direction.** When a cold-read is in-flight or has just reached clean (checkpoint about to
advance), let the agent land the just-reviewed remediation commits **without** the human flag —
e.g. a short-lived runner-set grace token written alongside the clean-review checkpoint that
`commit_block` honours for the next K commits, or treat commits whose diff was just reviewed
as pre-cleared. Composes with item 1 / the code-session note: if scope resolution reviews the
working tree, the fixes are *in* the reviewed set, so pre-clearing them is sound. Must not open
a blanket bypass — only commits whose content the just-passed review actually covered.

**Acceptance.** After a clean cold-read that included the working-tree fixes, the agent commits
those fixes without hitting the hard block and without a human-set env var.

## Must not regress (the parts that worked)

- **Gate-3 (verify-against-running-system) commit hook** — caught the citation drift the
  review missed. Highest-value piece of the wiring; do not weaken.
- The **iterate-until-clean loop**, per-round logging, and checkpoint / counter-reset —
  all behaved correctly.
- **Adversarial posture transferring to specs** — reviewers verified claims against
  primary sources (master spec, `catalog.py`, `models.py`) rather than rubber-stamping.

## Merge boundaries

Seven independent changes, each its own small PR against dd-skills:

1. Untracked-file scope fix (runner) — self-contained; highest priority. Extend to
   uncommitted modifications too, not only untracked new files (code-session note).
2. Nudge-cadence change (hook / counter) — self-contained; also suppress mid-remediation.
3. Tier-depth-ceiling guidance (SKILL text) — doc-only.
4. Doc-dominant-at-regular (parked) — only if item 4 graduates from watch-item.
5. Contract-coverage angle (SKILL text + reviewer prompt) — doc-only; fold into
   doctrine-consistency or add as a gated 7th angle.
6. Docs-aware commit-count gating (`review_nudge.py` / `commit_block.py`) — self-contained;
   the commit-level analog of item 2.
7. Remediation-commit pre-clear at the review boundary (`commit_block.py` + checkpoint
   write) — self-contained; composes with item 1.

Validation status: items 1, 2, 5 now confirmed on the 2026-06-16 code session (see "Code-
change-session validation"); items 6 + 7 originate there. Items 3 + 4 still want a session
that exercises a bare `fast`/`regular` tier standalone.
