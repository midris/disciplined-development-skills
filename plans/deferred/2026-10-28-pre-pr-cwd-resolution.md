# Deferred: resolve the pre-PR review directory the way the shell does

**Status:** Deferred.
Raised 2026-10-28 by the external review of `fix/pr-gate-matcher`, which narrowed the pre-PR gate's loose net and kept `main`'s directory resolution apart from composing chained `cd`s.
Every case below behaves the same on `main`.

## Why deferred

The branch's goal was to stop blocking commands that aren't PR attempts.
A blanket fail-closed rule (any pipe, `||` or parenthesis before `gh` once a `cd` appears) closed these cases but blocked real PR commands that `main` reviewed, such as `cd /r && npm test 2>&1 | tail -5 && gh pr create`.
The owner chose to ship the matcher fix and handle directory resolution separately, as its own PR.

## The problem

`find_gh_pr_create` (`skills/disciplined-development/hooks/lib/command_match.py`) returns the directory `pre_pr_review.py` sends to `external_review.py`.
It treats every earlier segment that starts with `cd <path>` as executed and persistent.
When that is false, the gate reviews one tree and the PR is opened from another.

| Command | Returns now | Shell runs `gh` in |
|---|---|---|
| `cd /parent && (cd child && gh pr create)` | `/parent` | `/parent/child` |
| `(cd /repo && gh pr create)` | process cwd | `/repo` |
| `true \|\| cd /other && gh pr create` | `/other` | process cwd |
| `cd /a & sleep 1; gh pr create` | `/a` | process cwd |
| `cd /a && bash -c 'cd rel && gh pr create'` | `<process cwd>/rel` | `/a/rel` |
| `cat > s.sh <<'EOF'` / `cd /other` / `EOF` / `gh pr create` (heredoc body) | `/other` | process cwd |
| `cd /a &&` newline `cd /b && gh pr create` | `/a` (the tokenizer glues `&&;`) | `/b` |
| `pushd /x && gh pr create` | process cwd | `/x` |

## Requirements for the fix

- A `cd` counts only when `gh` running implies it ran in the same shell. It must not be inside a group or subshell that closed before `gh`, preceded by `\|\|`, or followed by `\|` or a bare `&`.
- An unrelated pipe, `\|\|` or substitution elsewhere in the chain must not change the result: `cd /r && npm test \| tail && gh pr create` still resolves to `/r`.
- When the directory can't be known (`pushd`, `cd -`, `cd ~`, or a heredoc body that looks like a `cd`), return `None` so the gate fails closed.
- Fix the newline/separator token gluing in `_normalize_newlines` without changing `is_git_commit` behaviour.
- Pin each table row above, plus the `npm test \| tail` case, as tests in `tests/test_command_match.py`.

## Also observed, unscheduled

- Tokenizing in the strict path is superlinear on very long single tokens (about 12 s at 1 MB, the same on `main`). Only the loose net is linear.
