# CLAUDE.md threading snippet

Paste the block below into your project's `CLAUDE.md` (e.g. under a
"Highest Priority Rules" heading) so the agent loads the doctrine and its
companions at the start of each session. Keep your project-specific rules as
overlays *on top of* it.

---

- Invoke the `disciplined-development` skill at the start of every session
  (path `.claude/skills/disciplined-development/SKILL.md`). It governs the gates,
  principles, and sub-skill dispatch: `adversarial-review`,
  `adversarial-review-loop`, `disciplined-research`, `lean-plan-writing`,
  `sweeping-stale-references`, `writing-explicit-rationale`. The rules below are
  project-specific overlays on top of it.
- The hooks are **not** auto-registered. Add the hook block to
  `.claude/settings.json` (see `disciplined-development/hooks/README.md`) and drop
  a `.claude/dd-config.json` to tune behavior (start from `examples/dd-config.json`;
  full schema in `disciplined-development/hooks/dd-config.md`).

---

> The skill dirs are symlinked in from a clone of `disciplined-development-skills`
> (see the repo README's install section). Gitignore the symlinks — they're
> machine-specific.
