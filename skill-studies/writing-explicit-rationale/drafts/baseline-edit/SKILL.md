---
name: writing-explicit-rationale
description: 'Use when a plan, spec, design, or code choice could be mistaken for an oversight: descoping, deferring, taking a shortcut, making an exception, or choosing among defensible alternatives. Also use when review re-litigates a decision or its rationale would otherwise live only in chat, a commit message, or a PR description.'
---

# Writing explicit rationale

**Would a future reader wonder whether you considered an alternative or simply overlooked it?** Ask this when trimming scope, accepting an exception, or making a design choice someone might reverse. Even a small omission can look accidental. Skip commentary on self-evident conventions, equivalent options and routine refactors.

## At the decision site

In a sentence or two, name the choice, explain why it fits, and state any consequence the team accepts. If the decision is provisional, give the agreed condition for revisiting it.

- **Plan or spec.** When trimming scope, keep the affected items identifiable beside the decision. “Defer bulk import until we can validate an entire batch before saving it. For this release, operators enter records individually.”
- **Code.** Explain why a plausible alternative would change behavior that matters. “Keep the original timestamp on retry so a delayed retry cannot move an older reading ahead of a newer one.” Let the implementation carry the mechanics.
- **Handoff.** Include the requested PR summary or review reply. A maintainer reading the changed file later should still be able to recover the reason. A link can supply detail once the decision itself is clear.

Base the explanation on the evidence available. State a risk as a risk. If the team agreed to reconsider an option, preserve the question it left open.

## When review reopens a decision

If the same choice comes up in two review rounds, read the change as a maintainer seeing it for the first time. Put the missing reason where the choice is visible. Check the other decisions in the change for reasons stranded in review or commit history and repair them in the same pass. Preserve existing explanations through routine edits.
