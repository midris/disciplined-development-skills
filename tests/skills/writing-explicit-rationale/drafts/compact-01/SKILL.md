---
name: writing-explicit-rationale
description: 'Use when a plan, spec, design, or code choice could be mistaken for an oversight: descoping, deferring, taking a shortcut, making an exception, or choosing among defensible alternatives. Also use when review re-litigates a decision or its rationale would otherwise live only in chat, a commit message, or a PR description.'
---

# Writing explicit rationale

Would a maintainer who missed the discussion mistake this choice for an oversight, or undo it without knowing what it protects? Explain it where they encounter it. Routine renames and familiar conventions usually speak for themselves.

In a sentence or two, say what was chosen or deferred, why, and what consequence the team accepted. Preserve uncertainty and any agreed condition for reconsideration. A possible cost stays possible. An agreement to revisit leaves the outcome open.

- **Plans and specs.** Name deferred items beside the affected commitment. “Defer hourly reports because billing totals settle overnight. Customers receive daily totals until billing supports hourly settlement.”
- **Code.** Put the reason at the decision site. Let the code show the mechanics. If several sites depend on one decision, keep the shared explanation in one durable place and point to it where a maintainer might otherwise miss it.
- **Handoffs.** A PR summary or review reply can explain the change to today's reader. Put the reason in the project as part of the edit so it also reaches tomorrow's reader.

If review reopens the same decision across two rounds, inspect the rest of the change for choices whose reasons live only in discussion or commit history. Repair the disputed site and the related omissions together.

Use `lean-plan-writing` for plan density and `sweeping-stale-references` when a later change invalidates a recorded reason.
