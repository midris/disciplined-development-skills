# CLAUDE.md threading snippet

Paste the block below into your project's `CLAUDE.md` (e.g. under a
"Highest Priority Rules" heading) so the agent loads the doctrine and its
companions at the start of each session. Keep your project-specific rules as
overlays *on top of* it.

---

- Invoke the `disciplined-development` skill at the start of every session
  (path `.claude/skills/disciplined-development/SKILL.md`). It governs the gates,
  principles, and sub-skill dispatch: `adversarial-review`,
  `adversarial-review-loop`, `concise-writing`, `disciplined-research`,
  `dispatching-development-subagents`, `lean-plan-writing`,
  `sweeping-stale-references`, `writing-explicit-rationale`.
  The rules below are project-specific overlays on top of it.
- The hooks are **not** auto-registered. Merge the hook block from the bundle's
  `examples/settings.hooks.json` into `.claude/settings.json`, and drop a
  `.claude/dd-config.json` to tune behavior (start from the bundle's
  `examples/dd-config.json`; full schema in
  `.claude/skills/disciplined-development/hooks/dd-config.md`).
- The hooks enforce a multi-tier review cadence: T0 edit-counter nudge/block,
  T1 commit nudge, T2 commit-count nudge/block, T3 pre-PR gate on `gh pr create`.
  Thresholds are in `.claude/skills/disciplined-development/hooks/dd-config.md`.
- Periodic review per Principle 8 — at review-nudge signals or natural pauses,
  run a deep review per the adversarial-review skill, then log it via `dd-log`
  to reset the counter; iterate per `adversarial-review-loop` until clean.

---

> The skill dirs are symlinked in from a clone of `disciplined-development-skills`
> (see the repo README's install section). Gitignore the symlinks — they're
> machine-specific.
