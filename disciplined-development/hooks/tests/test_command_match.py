"""Tests for hooks.lib.command_match — the slim gh/git matchers (A5)."""

import os

from hooks.lib.command_match import (
    commit_landed,
    find_gh_pr_create,
    is_git_commit,
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


# ---- find_gh_pr_create ------------------------------------------------------


def test_find_gh_pr_create_plain():
    result = find_gh_pr_create("gh pr create")
    assert result is not None
    cwd, base = result
    # No chained `cd` → cwd is the process working directory.
    assert cwd == os.getcwd()
    assert base == ""


def test_find_gh_pr_create_base_long():
    _, base = find_gh_pr_create("gh pr create --base release")
    assert base == "release"


def test_find_gh_pr_create_base_short():
    _, base = find_gh_pr_create("gh pr create -B phase-22")
    assert base == "phase-22"


def test_find_gh_pr_create_base_short_eq():
    _, base = find_gh_pr_create("gh pr create -B=master")
    assert base == "master"


def test_find_gh_pr_create_base_long_eq():
    _, base = find_gh_pr_create("gh pr create --base=main")
    assert base == "main"


def test_find_gh_pr_create_chained_cd():
    cwd, _ = find_gh_pr_create("cd /other && gh pr create")
    assert cwd == "/other"


def test_find_gh_pr_create_chained_cd_last_wins():
    """Multiple chained `cd`s: the LAST one wins, and a relative `cd` is
    anchored to the process cwd (not to the prior absolute `cd`).

    This pins the accepted-edge contract (see the production comment in
    command_match.py): the resolver does not compose relative `cd`s. A
    future fix that correctly resolves `cd subdir` against the prior
    absolute `cd` must update this test in lockstep. E2's gh-wrapper
    forwards this cwd to `dd_review --cwd`."""
    # Last `cd` is absolute → it wins outright.
    cwd, _ = find_gh_pr_create("cd /a && cd /b && gh pr create")
    assert cwd == "/b"
    # Last `cd` is relative → anchored to process cwd, NOT to `/a`.
    cwd, _ = find_gh_pr_create("cd /a && cd subdir && gh pr create")
    assert cwd == os.path.join(os.getcwd(), "subdir")


def test_find_gh_pr_create_global_flag_skipped():
    result = find_gh_pr_create("gh --repo o/r pr create")
    assert result is not None


def test_find_gh_pr_create_non_gh_none():
    assert find_gh_pr_create("git status") is None


def test_find_gh_pr_create_unexpandable_cd_signals_unresolved_cwd():
    # A `gh pr create` after a `cd` to an unexpandable path (shell var /
    # substitution) is STILL matched — cwd is None to signal "matched but
    # cwd unresolvable", so the pre-PR gate can fail loud instead of failing
    # open (the bug: returning None made the wrapper treat it as not-a-PR and
    # let the unreviewed PR through).
    result = find_gh_pr_create("cd $X && gh pr create")
    assert result is not None
    cwd, base = result
    assert cwd is None and base == ""
