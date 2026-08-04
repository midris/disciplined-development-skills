# Exploratory AR-11 scope-guard probe

This retired two-turn probe first ran [initial-prompt.md](initial-prompt.md) against the ratio fixture and then resumed the same evaluator session with [followup-prompt.md](followup-prompt.md).
The orchestrator scored the paired turns together with [rubric.md](rubric.md); the initial turn had to establish the review behavior before the follow-up tested whether it ended.

The current skill passed 5/5, but an ablation with the complete `End of posture` section removed also passed 5/5, so the probe did not discriminate the section's effect.
A later original-control run was additionally confounded by the globally mandatory brainstorming skill: follow-ups loaded that skill, and one asked a reasonable clarifying question rather than immediately proposing a label.
The probe is preserved as design evidence but is not part of the active regression suite.
