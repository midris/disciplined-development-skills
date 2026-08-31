You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `{{fixture_dir}}/skills/disciplined-research/SKILL.md` completely and follow it as binding guidance.

Write one corrected sentence for a migration plan as of July 20, 2026, based only on the supplied project and upstream materials.
The proposed sentence is: `Our project already uses the current stable Orbital SDK 4.1.0.`
Read `{{fixture_dir}}/project/package.json`, `{{fixture_dir}}/sources/orbital-release-notes.md`, and `{{fixture_dir}}/sources/orbital-maintainer-blog.md`.
Verify both the project's installed version and the authoritative upstream stable version.
Return exactly three lines: the corrected sentence, `Source: <project path>`, then `Source: <upstream path>`.
