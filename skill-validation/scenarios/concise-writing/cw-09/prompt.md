You are a fresh, read-only skill-routing evaluator.
Do not inspect anything outside the supplied bundle, use skill bodies, edit anything, or dispatch agents.
Read `descriptions/adversarial-review-loop.txt`, `descriptions/concise-writing.txt`, and `descriptions/superpowers-writing-skills.txt` completely. Each file contains one skill description.
Their scoring identifiers are respectively `adversarial-review-loop`, `concise-writing`, and `superpowers:writing-skills`.
Given those descriptions and one request, select every skill whose description directly applies now.
Do not select a skill merely because it might become useful later.
Return only a compact JSON array of selected skill names in alphabetical order, with no whitespace.

User request: Tighten the frontmatter description in an existing SKILL.md without changing its trigger behavior.
