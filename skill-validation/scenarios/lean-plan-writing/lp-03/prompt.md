You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `{{fixture_dir}}/skills/lean-plan-writing/SKILL.md` and `{{fixture_dir}}/skills/writing-plans/SKILL.md` completely and follow them as binding guidance, with `lean-plan-writing` owning its stated override.

Write one implementation-plan step for emitting `release-envelope.txt`.
Its exact artifact shape is four lines in this order, with the braces preserved literally: `TYPE={type}`, `VERSION={version}`, `CREATED={iso8601}`, and `PAYLOAD={relative_path}`.
The exact file bytes are UTF-8 without a BOM, use LF line endings, and include one final LF after the `PAYLOAD` line.
Line order, line breaks, spelling, and literal braces are contractual, so the plan needs a short exact artifact-shape example in addition to prose requirements.
The plan step must state how the artifact will be verified byte-for-byte.
Return only the plan step.
