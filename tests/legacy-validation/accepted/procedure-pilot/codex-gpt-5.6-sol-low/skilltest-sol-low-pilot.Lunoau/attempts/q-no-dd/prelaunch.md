# Pre-launch checks

Owner exact-command approval: "approved, please continue", 2026-09-07.
Working directory: /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike.
HEAD and PILOT_INPUT_REVISION: 0a22a44701032d5d3c367ea9c84f13bfc5202e62.
Clean worktree, pinned pilot/runner diff empty, and no prior command stdout/version capture: all checks exit 0.

Immediately before launch, /opt/homebrew/bin/codex --version and /usr/bin/shasum -a 256 /opt/homebrew/bin/codex both exited 0; output retained in cli-version.txt, version-stderr.txt and cli-sha256.txt.
Both fixed preflight reference files were nonempty and cmp of each fresh capture to its fixed reference exited 0.
CLI: codex-cli 0.153.4; SHA-256: b973d440acac501fd2594a43e7ca9ce41e0a65b9dfb28d0d7a7837c99e1261e3.
The unchanged command in approval-request.md was submitted with approved host execution; execution session 94517 was returned while it ran.
No authentication contents were read or displayed by the orchestrator.
