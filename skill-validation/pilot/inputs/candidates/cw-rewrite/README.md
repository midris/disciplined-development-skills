# CW rewrite candidate input

This is a byte-for-byte test snapshot, not the shipped skill or an accepted replacement.

- Source branch: `docs/comprehensive-skill-cleanup`.
- Source commit: `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
- Source path: `skills/concise-writing/SKILL.md`.
- Source worktree's CW file matched that commit with no local changes when copied.
- [Body](SKILL.md) SHA-256: `f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba`.
- [Description](description.txt) SHA-256: `642b8ec050a0cc782e391fcf88ca7414186e28fa7ba8a145f313097f9c75f0cd`; exact decoded frontmatter description plus a terminal newline for the description-only fixtures.

Only CW is imported; the remaining DD and Superpowers files stay at their accepted baseline bytes.
No source worktree, shipped skill, historical scenario or scored evidence is changed.
The [CW design](../../../../../plans/completed/specs/2026-09-07-cw-validation-design.md#existing-cw-candidate-preparation) owns scope and approval gates; the [catalog](../../../cw-catalog.md#cw-rewrite-candidate-configs) maps candidate configs to existing prompts/rubrics.
Later tests cannot establish this existing candidate's RED-before-authoring chronology.
