# Claude runner follow-up verification

The three runner follow-ups from reviews 14 and 15 are implemented with zero model calls.
SSR skill bodies, fixed scores and retained evidence are unchanged.

- Default offline tests check private `TMPPREFIX`, `ZDOTDIR` and the generated PATH-restoring login profile in both permission modes. Temporarily removing each environment setting separately produced two failing tests; the source was restored afterward.
- Claude's process environment now sets `core.excludesFile=/dev/null` through `GIT_CONFIG_COUNT`. The offline Git regression failed before the fix because a surrogate host ignore file hid a subject path; it passes afterward and still honors project `.gitignore`. No sandbox read grant changes.
- Final-answer extraction permits the three observed trailing system subtypes: `background_tasks_changed`, `task_updated` and `task_notification`. The bundle-level regression failed before the correction and passes afterward. Later assistant output, unknown trailing events, multiple results, malformed traces and unsuccessful results still prevent extraction. Raw stdout remains intact.

Read-only replay of retained Sonnet comparison order 4 extracts its 988-byte answer and leaves the stdout SHA-256 unchanged.
No convenience file was added to that historical bundle and no observations were recollected.

Verification:

- Runner default suite: 471 passed. An initial run inside the outer sandbox produced six nested sandbox authentication-startup failures; the unchanged suite passed outside that outer sandbox.
- Hook suite: 263 passed, 3 environment skips.
- Actual Claude CLI and shared Claude isolation probes: 4 passed, 2 non-Claude probes deselected. Both permission modes pass; the scripted localhost endpoint uses no model inference. The shell probe now performs a Git ignore lookup and requires empty stderr, alongside Python/Git resolution and heredoc checks.
- Focused runtime and bundle regression suite: 52 passed.

The installed checks qualify the affected runtime controls, not production model behavior or authentication.
Future model collection must still follow the study's pinned-runtime preflight requirements.

The requested follow-up review found that a trailing system event with an array or object subtype raised TypeError before result publication. Two bundle-level regressions reproduced the failure before the fix. An explicit string check now rejects both shapes, preserves raw stdout, omits final.txt and permits normal result publication.

The subsequent adversarial review checked environment inheritance, project-ignore preservation, result ambiguity, raw-evidence preservation and current-plan consistency. Additional probes rejected 22 malformed or unknown type/subtype values and accepted each of the three supported subtypes.
No findings.

DD-VERDICT: PASS
