---
name: writing-explicit-rationale
description: 'Use when a plan, spec, design, or code choice could be mistaken for an oversight: descoping, deferring, taking a shortcut, making an exception, or choosing among defensible alternatives. Also use when review re-litigates a decision or its rationale would otherwise live only in chat, a commit message, or a PR description.'
---

# Writing explicit rationale

**Would a future reader wonder whether you considered an alternative or simply overlooked it?** Ask this when trimming scope, accepting an exception, or making a design choice someone might reverse. Even a small omission can look accidental. Skip commentary on self-evident conventions, equivalent options and routine refactors.

## At the decision site

In a sentence or two, name the choice, explain why it fits, and state any consequence the team accepts. If the decision is provisional, give the agreed condition for revisiting it.

- **Plan or spec.** When trimming scope, keep the affected items identifiable beside the decision.
- **Code.** Explain why a plausible alternative would change behavior that matters. Let the implementation carry the mechanics.
- **Handoff.** Include the requested PR summary or review reply. A maintainer reading the changed file later should still be able to recover the reason. A link can supply detail once the decision itself is clear.

Base the explanation on the evidence available. State a risk as a risk. If the team agreed to reconsider an option, preserve the question it left open.

## When review reopens a decision

If the same choice comes up in two review rounds, read the change as a maintainer seeing it for the first time. Put the missing reason where the choice is visible. Check the other decisions in the change for reasons stranded in review or commit history and repair them in the same pass. Preserve existing explanations through routine edits.

## Worked examples

- **Test scope.** “Defer deleted-user and disabled-user tests until Product defines how those accounts appear in reports.” A reader can name the missing cases and what would unblock them.
- **Residual risk.** “We accept the risk of duplicate submissions in the preview because only authenticated staff use staging. Revisit duplicate protection before external rollout.”
- **Rule exception.** “Skip CLI parity for multi-select. The interaction depends on a visual preview. Revisit if operators need scripted selection.”
- **Capacity limit.** “Cap imports at 500 records so each batch fits one transaction. Larger imports need chunking. Revisit when telemetry shows demand.”
- **Code choice.** “Keep the original timestamp on retry so a delayed retry cannot put an older reading ahead of a newer one.”

## Rationalizations to catch

- “They asked me to simplify. Explaining the cut is someone else's job.” The editor making the cut can leave one sentence beside the affected item, even for a small deferral.
- “Everyone knows why. I'll put it in the PR or add it later.” Write the durable explanation while editing, then give the requested handoff. The next maintainer may have only the file.
- “The code shows what happens.” Ask whether the reader could explain why changing it would matter. An ordinary-looking default or boundary can embody a deliberate trade-off.

## Red flags before handoff

Check for a requirement or test that vanished under a “Later” heading, a policy exception that reads like an oversight, or a pointer whose destination never names the affected item. Restore enough context to identify the choice and its reason. If a repeated review produced only a reply or one comment, compare the reasons in the submitted change and discussion with what survives at each decision site. Repair any other consequential omission before closing the review.
