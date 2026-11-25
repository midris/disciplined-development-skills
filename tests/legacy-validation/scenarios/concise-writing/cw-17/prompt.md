You are a fresh, read-only skill-routing and contract evaluator.
Do not inspect anything outside the supplied bundle, edit anything, or dispatch agents.
Read `{{fixture_dir}}/descriptions/adversarial-review-loop.txt`, `{{fixture_dir}}/descriptions/concise-writing.txt`, and `{{fixture_dir}}/descriptions/superpowers-writing-skills.txt` completely. Each file contains one skill description.
Their scoring identifiers are respectively `adversarial-review-loop`, `concise-writing`, and `superpowers:writing-skills`.
Read `{{fixture_dir}}/skills/concise-writing/SKILL.md` completely.

Given the user request below:
1. Select every skill whose supplied description directly applies now.
2. Decide whether the complete `concise-writing` contract says to apply its method to the requested detailed explanation.

Do not select a skill merely because it might become useful later.
`apply_to_detailed_explanation` refers only to the prose requested by the user, not this evaluator's JSON response.
Return only compact JSON with keys in this order and no whitespace:
{"selected_skills":[],"apply_to_detailed_explanation":false}
Alphabetize `selected_skills`; set the boolean to `true` or `false`.

User request: Give me a detailed explanation of how to organize a neighborhood clothing swap. Put the explanation only in your response; do not create or edit a file.
