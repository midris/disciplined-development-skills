# Copy-based skill installation

**Status:** Implemented and verified on `main`; simplified at the owner's request on 2026-09-09.

## Contract

Keep `./install-skills.sh <project>` for `.claude` installation.
Allow `./install-skills.sh <project> .agents` for skills-only installation; explicit `.claude` is also accepted.
Copy every complete `skills/<name>/` directory containing `SKILL.md`, including nested support files, hidden files, empty directories and permissions.
For `.claude`, also copy `commands/*.md` into `.claude/commands/` as before.
The Claude command templates remain Claude-specific and are not installed into `.agents`.

Remove each same-name destination first, whether it is a file, directory or symlink, then copy the source.
Remove symlinks themselves without modifying their targets, including foreign and dangling links.
Local edits and extra files inside replaced skill directories are intentionally discarded.
Leave all other skill names, commands, settings, hooks, memory and DD logs/state outside those directories untouched.
In particular, Steno's accumulated `.claude/.dd-state/` history is outside the replacement boundary.
Do not invoke hooks or history cleanup during installation.
Reject symlinked shared installation parents so replacement cannot escape into another directory through them.

Installed directories are snapshots; source edits and branch switches take effect only after explicitly rerunning the installer.
Do not track ownership, prune absent skill names or commands, retain backups, lock, stage transactions or recover interrupted updates.
These mechanisms were removed because the owner wants a direct remove-and-copy installer; a failed copy exits nonzero and can leave a partial installation for the user to reinstall.
Use Bash and standard filesystem commands, with no Python helper or installer metadata.
Installation into existing consumers is a separate explicit operation.

## Implementation

- [x] Replace the earlier receipt/recovery tests with focused copy, replacement, destination and preservation tests; observe failures first.
- [x] Replace the prototype with the simple shell installer and reconcile installation guidance.
- [x] Run the installer and hook suites, exercise the real bundle in a disposable consumer, and review the final change.

## Verification and review

The revised tests first produced 7 failures against the discarded prototype, then all 14 installer tests passed against the shell implementation.
The required hook suite passed: 263 passed, 3 skipped.
`bash -n install-skills.sh` and `git diff --check` passed.
A real CLI smoke installed all nine skills into both destinations, repeated the Claude install, and compared 157 source files per destination by hash and mode.
Eight seeded consumer records remained byte-for-byte unchanged; source files were unchanged and no consumer hooks were invoked.
The scratch result is `/private/tmp/dd-installer-simple-smoke.qocbcz71/result.json`.
At the owner's subsequent request, both Steno's `.claude/skills` and `.agents/skills` were updated to copies and verified against all nine source skills.
The Claude `dd-log` command was also copied.
All 38 inventoried unrelated Claude files/links, including 20 DD state/history files, remained unchanged.
The deployment checks are retained under `/private/tmp/dd-steno-install.et3jb_rl/` and the separately recorded `.agents` installation scratch.

Final inline review checked the simplified contract, deletion boundaries, symlink behavior and installation guidance; no remaining findings.
Partial installation on copy failure is an explicit owner-accepted limitation, not pending recovery work.
The stale-reference sweep updated current installation docs, examples, command comments and the backlog; deferred/completed historical plans and unrelated harness symlink rules remain unchanged.
