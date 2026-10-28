"""Tests for hooks.lib.command_match — the slim gh/git matchers (A5)."""

import os
import time

from hooks.lib.command_match import (
    commit_landed,
    find_gh_pr_create,
    is_git_commit,
    looks_like_gh_pr_create,
)

# ---- is_git_commit ----------------------------------------------------------


def test_is_git_commit_bare():
    assert is_git_commit("git commit -m hello") is True


def test_is_git_commit_with_global_flag():
    assert is_git_commit("git -C /repo commit -m hello") is True


def test_is_git_commit_echo_wrapper_false():
    assert is_git_commit("echo git commit") is False


def test_is_git_commit_non_commit_false():
    assert is_git_commit("git status") is False


# ---- commit_landed ----------------------------------------------------------


def test_commit_landed_marker_present():
    resp = {"stdout": "[master 1a2b3c4] do the thing\n 1 file changed", "exit_code": 0}
    assert commit_landed("git commit -m x", resp) is True


def test_commit_landed_quiet_exit_zero():
    resp = {"stdout": "", "exit_code": 0}
    assert commit_landed("git commit --quiet -m x", resp) is True


def test_commit_landed_dry_run_false():
    resp = {"stdout": "", "exit_code": 0}
    assert commit_landed("git commit --dry-run", resp) is False


def test_commit_landed_failed_exit_false():
    resp = {"stdout": "", "exit_code": 1}
    assert commit_landed("git commit --quiet -m x", resp) is False


def test_commit_landed_none_response_false():
    # A missing / non-dict tool_response must return False, never raise —
    # the PostToolUse caller may hand it whatever the harness provides.
    assert commit_landed("git commit -m x", None) is False


# ---- looks_like_gh_pr_create ------------------------------------------------


def test_looks_like_gh_pr_create_trivial():
    assert looks_like_gh_pr_create("gh pr create") is True


def test_looks_like_gh_pr_create_non_pr_false():
    assert looks_like_gh_pr_create("git status") is False


def test_looks_like_gh_pr_create_over_broad_mention_accepted():
    # A mention of the whole command returns True, quoted or not — accepted,
    # documented over-broad behavior. The function is a loose net for the
    # pre-PR gate's fail-closed path; a false positive is a human-overridable
    # block, a false negative is a fail-open hole.
    assert looks_like_gh_pr_create("echo gh pr create") is True
    assert looks_like_gh_pr_create('git commit -m "fix gh pr create"') is True


def test_looks_like_gh_pr_create_hard_to_parse_compound():
    # An unmatched quote makes tokenize() return None (strict parse fails).
    # looks_like must still return True on the same command where
    # find_gh_pr_create returns None, proving it is the net for parse failures.
    # This pairing is the load-bearing proof that looks_like is the fail-closed
    # net: find_gh_pr_create only works when the command is tokenizable; for
    # commands the strict parser chokes on, looks_like catches the PR attempt.
    cmd = "git commit -m 'it's done' && gh pr create"
    assert find_gh_pr_create(cmd) is None  # strict parse fails → None
    assert looks_like_gh_pr_create(cmd) is True  # loose net catches it


def test_looks_like_gh_pr_create_ignores_partial_words():
    # "through" / "printer" / "created" contain gh / pr / create.
    assert looks_like_gh_pr_create(
        'git commit -m "Route the check through the printer so it is created once"'
    ) is False
    # Same words in a command tokenize() can't parse (unmatched quote).
    assert looks_like_gh_pr_create(
        "git commit -m 'it's through the printer, created'"
    ) is False


def test_looks_like_gh_pr_create_ignores_other_verbs_after_pr():
    for cmd in (
        "gh pr",
        "gh pr --help",
        'gh issue create --title "Follow-up from pr #42: new edge case"',
        'gh release create v1.2 --notes "Merged pr #3 with new matcher"',
        'gh api repos/o/r/issues -f title="pr gate: new alias"',
        'gh issue comment 5 --body "the pr adds new tests"',
        'git -C "$REPO" commit -m "pr gate: create an ERROR row on block"',
        'echo "$USER opened pr 12 with new tests"',
        "git push origin $BR:pr/new-api",
        'gh pr -R "o/r" view 5',
        'gh pr --repo "$REPO" list --search create',
        "gh pr $N view",
        'git commit -m "$SCOPE: fix pr $NUM"',
        'git commit -m "docs: mention gh pr --web"',
        'gh issue create --title "Support gh pr -R"',
        'gh issue create --title "Support gh pr --repo"',
        'git commit -m "docs: `gh pr view` example"',
        "cat > notes.md <<'EOF'\nRun `gh pr checks` to see CI.\nEOF",
        'gh pr view 12 && echo "created"',
        "gh pr view 12\necho created",
        'gh pr list --search "create"',
        "gh pr list --search create",
        "gh pr comment 5 --body new",
        "gh pr ls --search create",
        "gh pr view 1 --json title | grep -c new",
        'gh pr comment 5 --body "see pr 7, new tests"',
        'gh pr merge 5 --subject "Merge pr #5: new matcher"',
        'gh pr edit 5 --body "this pr adds new flags"',
    ):
        assert looks_like_gh_pr_create(cmd) is False, cmd


def test_looks_like_gh_pr_create_catches_wrapped_invocations():
    for cmd in (
        "env GH_TOKEN=x gh pr create",
        "timeout 60 gh pr create",
        "gh pr -R o/r create",
        "gh --repo o/r pr new --fill",
        "/usr/local/bin/gh pr create",
        "echo `gh pr create`",
        "echo $(gh pr create)",
        'bash -c "cd $X && gh pr create"',
        "sh -ec 'gh pr create --fill'",
        "bash -euo pipefail -c 'gh pr create --fill'",
        "/opt/homebrew/bin/bash -c 'gh pr create --fill'",
        "cd $X && gh pr new",
        'URL="$(gh -R o/r pr create --fill)"',
        'URL="$(cd /repo && gh pr create --fill)"',
        'URL="$(timeout 60 gh pr create --fill)"',
        "$(which gh) pr create --fill",
        "$(which gh 2>&1) pr create --fill",
        "$(command -v gh &>/dev/null && echo gh) pr create",
        '"$(command -v gh)" pr create --fill',
        "GH=gh; $GH pr create --fill",
        "gh \\\n  pr create --fill",
        "gh pr \\\r\n  create --fill",
        'cd $X && gh "pr" create',
        'env A=1 gh pr "create"',
        '"$GH" pr create --fill',
        "${GH:-gh} pr create --fill",
        '"${GH:-gh}" pr create',
        "gh -R o/r pr --repo o/r create",
        "gh pr view $(gh pr create --fill)",
        "gh pr -R acme-co/web create --fill",
        "gh pr --repo ghe.acme.co/org/app create --fill",
        "gh pr -R o/list create",
        'gh pr -R "$(cat .repo)" create --fill',
        'gh pr --repo "$(gh repo view --json nameWithOwner -q .nameWithOwner)" create',
        'cd "$WT" && gh pr -R "$(git config --get dd.repo)" new --fill',
        'cd "$WT" && gh pr create>"$OUT"',
        "timeout 60 gh pr new>url.txt",
        "gh pr $GH_PR_FLAGS create --fill",
        "cd $WT && gh pr ${REPO_ARGS} create --fill",
        'gh pr "$@" create',
        "gh pr $(echo create)",
        "gh pr `echo create`",
        "gh pr --repo=\"$(cat .repo)\" create",
        'gh pr -R"o/$(cat .r)" create',
        "gh pr -R `cat .r` create",
        "gh pr $'create'",
        "gh pr 2>/dev/null create",
        # Verb past the scan window can't be ruled out: block.
        "gh pr " + "--x " * 100 + "create",
    ):
        assert looks_like_gh_pr_create(cmd) is True, cmd


def test_looks_like_gh_pr_create_catches_pr_after_quote_shifting_heredocs():
    # Each heredoc body has an odd quote count; shlex (unlike bash) counts
    # them, so the PR call would land inside one token if we tokenized.
    cmd = (
        "git commit -m \"$(cat <<'EOF'\nSupport 27\" displays\nEOF\n)\" && "
        'git push -u origin HEAD && gh pr create --title "Fix" '
        "--body \"$(cat <<'EOF'\nAdds 27\" support\nEOF\n)\""
    )
    assert looks_like_gh_pr_create(cmd) is True


def test_looks_like_gh_pr_create_linear_on_large_input():
    # Runs on every Bash call; backtracking patterns stalled for seconds on a
    # few KB of gh / pr prose or of long flag runs.
    para = "Run gh to list each pr; the pr view shows state. Use gh for the pr diff.\n"
    for cmd in (
        "cat > notes.md <<'EOF'\nIt's a log.\n" + para * 2000 + "EOF",
        "gh pr view\n" * 5000,
        "gh " + "-a pr " * 10000,
        "-a gh -a pr " * 5000,
        "-a $X -a pr " * 5000,
        "docker run " + "-e $X " * 10000,
        "gh pr view " * 10000 + "create",
        "gh " + "-pr" * 100000,
        "$a pr view " * 50000,
    ):
        start = time.monotonic()
        assert looks_like_gh_pr_create(cmd) is False
        assert time.monotonic() - start < 0.5, cmd[:40]


# ---- find_gh_pr_create ------------------------------------------------------


def test_find_gh_pr_create_plain():
    result = find_gh_pr_create("gh pr create")
    assert result is not None
    # No chained `cd` → cwd is the process working directory.
    assert result == os.getcwd()


def test_find_gh_pr_create_chained_cd():
    cwd = find_gh_pr_create("cd /other && gh pr create")
    assert cwd == "/other"


def test_find_gh_pr_create_chained_cd_composes_like_the_shell():
    """Chained `cd`s resolve the way the shell does: an absolute `cd` resets,
    a relative one is joined to the cwd so far. `pre_pr_review.py` forwards
    this cwd to `external_review.py`, so a wrong join reviews the wrong tree."""
    assert find_gh_pr_create("cd /a && cd /b && gh pr create") == "/b"
    assert find_gh_pr_create("cd /a && cd subdir && gh pr create") == "/a/subdir"
    assert find_gh_pr_create("cd sub && gh pr create") == os.path.join(
        os.getcwd(), "sub"
    )
    # Relative to an unknown base stays unknown; an absolute `cd` recovers.
    assert find_gh_pr_create("cd $X && cd sub && gh pr create") is None
    assert find_gh_pr_create("cd $X && cd /b && gh pr create") == "/b"
    assert find_gh_pr_create("cd /a; cd b\ngh pr create") == "/a/b"
    # Parens elsewhere don't disturb resolution.
    assert find_gh_pr_create("echo $(pwd) && gh pr create") == os.getcwd()
    assert find_gh_pr_create(
        "cd /r && gh pr create --body \"$(cat <<'EOF'\nx\nEOF\n)\""
    ) == "/r"


def test_find_gh_pr_create_skips_flags_between_pr_and_verb():
    # `-R/--repo` is a `gh pr`-level flag (`gh pr create --help`).
    assert find_gh_pr_create("cd /r && gh pr -R o/r create --fill") == "/r"
    assert find_gh_pr_create("cd /r && gh pr --repo=o/r new") == "/r"


def test_find_gh_pr_create_global_flag_skipped():
    result = find_gh_pr_create("gh --repo o/r pr create")
    assert result is not None


def test_find_gh_pr_create_matches_new_alias():
    assert find_gh_pr_create("cd /other && gh pr new --title x") == "/other"


def test_find_gh_pr_create_non_gh_none():
    assert find_gh_pr_create("git status") is None


def test_find_gh_pr_create_unexpandable_cd_signals_unresolved_cwd():
    # A `gh pr create` after a `cd` to an unexpandable path (shell var /
    # substitution): find_gh_pr_create returns None (cwd unresolvable →
    # treated same as not-a-PR in the new bare-cwd contract), and
    # looks_like_gh_pr_create returns True — the fail-closed pairing that
    # lets the pre-PR gate block rather than fail open.
    cmd = "cd $X && gh pr create"
    assert find_gh_pr_create(cmd) is None
    assert looks_like_gh_pr_create(cmd) is True
