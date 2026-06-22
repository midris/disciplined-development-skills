# Deferred (bug): the pre-PR review gate fails open silently

> **SUBSUMED (2026-06-21) by `plans/2026-06-21-review-tooling-overhaul-plan.md`.**
> Chunk 2 rewrites the gate fail-closed on *every* failure: a loose
> `looks_like_gh_pr_create` detector blocks an unparseable `gh pr create` outright,
> so the exact-command bisection below is no longer needed. Kept for the
> reproduction record.

**Status:** Deferred bug fix. Found 2026-06-20 during PR 5. **The fix lands upstream** in the private
dd-skills repo, not this consumer — the hook + matcher here are gitignored symlinks. Resolve the real
files with `readlink -f`:

```
readlink -f .claude/skills/disciplined-development/hooks/pre_pr_review.py
# → <dd-skills-clone>/skills/disciplined-development/hooks/pre_pr_review.py
# matcher:    <same dir>/lib/command_match.py   (find_gh_pr_create)
# tests:      <same dir>/tests/{test_command_match.py, test_pre_pr_review.py}
```

## Bug

`pre_pr_review.py` is a `PreToolUse` hook on **every** Bash call (settings matcher `"Bash"`). It reviews
a `gh pr create` only when `command_match.find_gh_pr_create(command)` returns non-`None`. Its branches:

- L89–91 `DD_SKIP_PR_REVIEW=1` → `logger.emit("skip", reason="env_bypass")`, `return 0`.
- L94 `match = find_gh_pr_create(command)`.
- **L95–97 `if match is None: return 0` — no emit, command allowed. This is the silent fail-open.**
- L100–114 unresolvable-`cwd` → `emit("block")`, `return 2` (**the fail-closed precedent to mirror**).
- L135 `emit("delegate")` → run engine; L151–153 `return 2` on a BLOCK; L156 `return 0` on pass.

`find_gh_pr_create(command: str) -> tuple[str | None, str] | None` (command_match.py:188) returns `None`
when it can't locate a `gh pr create`. So a `gh pr create` the matcher misses opens a PR **unreviewed
and unlogged** — the gate's only enforcement is evadable by command *shape*, not intent.

## Verified reproduction

PR #14 (this branch) opened unreviewed this way. Proof chain from the logs:
- `reviews.jsonl` has exactly one rec-5 row — a `BLOCK` at 13:05:36Z (the first, **standalone**
  `gh pr create`). The hook log (`.claude/.dd-state/.logs/dd-hooks-20260620.jsonl`, `hook=pre_pr_review`)
  has **no event after that** — no delegate/block/skip.
- PR #14 was created at 14:24:43Z. Hook runs on every Bash; `DD_SKIP_PR_REVIEW=0`. The only no-emit-allow
  path is L97 → so `find_gh_pr_create` returned `None` on the second (compound) command.

The exact failing command (~3.5 KB) is recoverable from the session transcript and **verified to
return `None`** (the steps below run as-is — extract → harness → `None`):

Step 1 — extract the exact failing command from the session transcript into `/tmp/cmd.txt` (the
transcript is JSONL of Claude Code events; pull the Bash `tool_use` whose `input.command` contains the
marker string):

```
T=~/.claude/projects/-Users-sidris-work-coronis-code-meeting-pipeline/4d3d6d9b-46b8-436f-90bc-42014dd2981a.jsonl
python3 -c "import json,sys
for l in open('$T'):
    m=json.loads(l).get('message',{})
    for b in (m.get('content') or []):
        if isinstance(b,dict) and b.get('type')=='tool_use' and b.get('name')=='Bash':
            c=b.get('input',{}).get('command','')
            if 're-attempt PR create' in c and 'gh pr create' in c:
                open('/tmp/cmd.txt','w').write(c); sys.exit()"
```

Step 2 — feed it to the matcher (this is the verified-`None` reproduction; swap in a trivial command
like `gh pr create --title x` to see a MATCH):

```
LIB=$(dirname "$(readlink -f .claude/skills/disciplined-development/hooks/pre_pr_review.py)")/lib
python3 -c "import sys; sys.path.insert(0,'$LIB'); from command_match import find_gh_pr_create as f; print(f(open('/tmp/cmd.txt').read()))"
# None  → silent skip (bug)   |   ('<cwd>', '<base>') → matched (reviewed)
```

## Localization (done; minimal trigger NOT yet isolated)

- The `gh pr create` **portion alone** (even with the full real markdown `--body` heredoc) → **MATCH**.
- The **full compound command** (`cd; git add; git commit -F - <<'EOF' …real body… EOF; git push 2>&1 |
  tail -2; echo "…(re-triggers the engine)…"; gh pr create …`) → **None**.
- It is specifically the preceding **`git commit -F - <<'EOF'` heredoc with the *real* multi-line body**
  that flips it: a minimal `x` commit body → MATCH; the real body → None. Individual suspects tested in
  isolation (`<…>` angle brackets, `recover()` parens, `==`, `**bold**`, links, emoji) each MATCH — so
  it is a **combination** in the body, not one char. A fresh agent should bisect the real commit body
  with the harness.

## Fix direction

1. **Harden `find_gh_pr_create`** to recognize `gh pr create` after preceding heredoc-bearing commands
   in a compound command. Regression fixtures: a compound `git commit -F - <<'EOF'…EOF` + `gh pr create`
   must match; the verified ~3.5 KB command (extracted above) must match.
2. **Fail safe:** when a command contains a `gh pr create` token the matcher can't resolve, **block**
   (mirror the L105 `unresolvable_cwd` branch — `emit("block")` + `return 2`) instead of L97 `return 0`.
   Guard against false positives (a command merely *mentioning* the string in unrelated text).

## Test scaffolding
- `tests/test_command_match.py` — add the compound-command fixtures above (assert match, not `None`).
- `tests/test_pre_pr_review.py` — add a case: a `gh pr create` token the matcher can't parse → hook
  returns 2 (or logs a skip), never a silent `return 0`.

Related (separate concern): logging this skip path — see `2026-06-20-adversarial-review-telemetry-deferred.md`.
