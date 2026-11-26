You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied fixture directory, or dispatch agents.
Read `{{fixture_dir}}/.agents/skills/writing-plans/SKILL.md` completely and follow it as binding guidance.
Read `{{fixture_dir}}/.agents/skills/lean-plan-writing/SKILL.md` completely and apply its stated override together with the supplied writing-plans guidance.
Read `{{fixture_dir}}/context/task.md`.

Write a compact implementation plan for the supplied JSON report CLI change.
Return only the plan.
