# Deferred — make the pre-PR codex gate announce itself

**Status:** deferred (parked for a future session).
**Surfaced:** 2026-06-08, opening PR #1 for chunk-3. `gh pr create` appeared
hung for ~7 minutes with no indication a review was running.
**Lands in:** the **private dd-skills repo**
(`github-personal:midris/disciplined-development-skills`), not
meeting-pipeline — shared tooling, so the fix is a commit there. Related:
[[2026-06-06-dd-skill-discipline-enforcement-gaps]].

## Problem

The `pre_pr_review.py` PreToolUse hook detects `gh pr create` and runs a
**synchronous ~7-minute codex review** (the dd "pre-pr" / T3 hard gate) before
the PR opens. While it runs, the user sees nothing — `gh pr create` looks
frozen. The session even reported "working 9h" once (it was idle-waiting on a
question, but the silent-gate experience is the same shape). We want the gate
to **announce that a review is happening**, without weakening the hard block.

## Root-cause constraints (Claude Code hooks — confirmed against the docs)

- Hooks run **synchronously**; their stdout/stderr/JSON is **buffered and
  surfaced only after the hook exits** — no streaming. A `print()` at the hook's
  start appears at minute 7, not second 0.
- Multiple hooks on one matcher run **in parallel**, and output is collected
  **after the whole set completes** — so a fast "announce" hook beside the slow
  review hook is *also* withheld until minute 7. Splitting into two hooks does
  not help.
- PreToolUse **stdout-on-success (exit 0) handling is undocumented** — not
  reliable for user-visible output.
- There is **no CC-native "a hook is running" indicator** in the UI.
- Exit **2** feeds the hook's **stderr back to the model** (this is how a block
  message reaches Claude) — but, again, only *after* the hook returns.

Net: nothing Claude-Code-native can surface a message **during** a synchronous
hook. Only an **out-of-band** channel can.

## Options considered

| Option | Verdict |
|---|---|
| `async: true` hook | **Rejected** — makes `gh pr create` proceed immediately and the review run in the background; the PR could open *before* findings land. Un-gates the only hard block. The whole point is a synchronous gate. |
| `osascript` notification | **Weak** — depends on the owning app's per-app banner setting. It's attributed to **Script Editor** (notifications inherit the scripting host); Script Editor isn't configured to show banners, so it dropped **silently into Notification Center** (no toast) and clicking it opens Script Editor. |
| `terminal-notifier` | **Possible, with friction** — registers under its own identity, so you *can* enable banners + set the click action. Costs a Homebrew dep **and** a one-time System Settings toggle; not guaranteed to toast until configured. |
| `/dev/tty` write | **Dead in the desktop app** — proved empirically: this session has no controlling tty (`/dev/tty` → ENXIO "device not configured"). Works only in a real terminal CLI. |

OS-notification reliability is fundamentally gated by macOS per-app
notification settings + Focus modes, which is why none of them "just worked."

## The promising direction — make the *model* announce

Since hooks can't surface a live message, have **Claude** announce in-chat
before `gh pr create` (renders immediately in the desktop app, no deps, can't be
Focus-suppressed). Two ways:

- **Option A — declarative instruction (simple, recommended).** One line in the
  `disciplined-development` skill's Gate-5 / PR-opening guidance (co-located with
  the gate, loaded every session), and/or project CLAUDE.md: *"Before running
  `gh pr create`, tell the user it triggers the pre-PR codex review (synchronous,
  ~minutes; it will look busy)."* Root cause of the PR-#1 incident was simply
  that no such instruction existed — Claude discovered the gate only when it
  hung. High adherence as a loaded-skill rule; zero new machinery.

- **Option B — two-phase enforced hook (script-driven, bulletproof, heavier).**
  First `gh pr create` (no ack marker) → hook returns **exit 2 instantly** with
  "announce the review to the user, then re-run the same command with
  `# dd-reviewed` appended." Claude announces in-chat, re-runs with the
  sentinel; the second call (marker present) runs the real review. Enforced — the
  PR can't open without first hitting the instruction — and the announce lands
  *before* the 7-min wait. Cost: a double tool-call + a sentinel-comment hack on
  the one hard gate.

**Recommendation:** start with **A** (Principle 7 — don't bolt a two-phase
handshake onto a hard block until the simple fix proves unreliable). Add **B**
only if A ever lets one slip. Optionally keep a fail-silent `/dev/tty` line for
terminal-CLI users (it's free, just invisible in the desktop app).

## Done when

- Opening a PR through Claude reliably produces an in-chat heads-up that the
  codex gate is about to run (~minutes, will look busy) **before** the wait.
- The gate stays a synchronous **hard block** (no `async`).
- If any OS-notification path is added, it's fail-silent and never blocks the
  gate.

## Pointers

- Hook: `disciplined-development/hooks/pre_pr_review.py` (delegates to
  `dd_review_runner.py pre-pr` with `DD_HARD_BLOCK=1`); bypass
  `DD_SKIP_PR_REVIEW=1`.
- The CC-hook facts above were confirmed via the official hooks docs in this
  session (no streaming; parallel hooks; output buffered until completion;
  exit-2 stderr → model).
