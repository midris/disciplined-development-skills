"""Tests for hooks.lib.command_match — the slim gh/git matchers."""

import pytest

from hooks.lib import command_match

commit_landed = command_match.commit_landed
find_gh_pr_create = command_match.find_gh_pr_create
is_git_commit = command_match.is_git_commit
looks_like_gh_pr_create = command_match.looks_like_gh_pr_create


def find_git_commit(*args, **kwargs):
    assert hasattr(command_match, "find_git_commit"), (
        "command_match must expose find_git_commit(command, base_cwd, env=None)"
    )
    return command_match.find_git_commit(*args, **kwargs)

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


def test_commit_landed_direct_exit_zero():
    resp = {"stdout": "", "exit_code": 0}
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


def test_commit_landed_ignores_success_looking_stdout_on_failure():
    resp = {"stdout": "[master 1a2b3c4] do the thing\n", "exit_code": 1}
    assert commit_landed("git commit -m x", resp) is False


def test_commit_landed_unresolved_target_selector_still_uses_exit_status():
    resp = {"stdout": "", "exit_code": 0}
    assert commit_landed("git -C /other commit -m x", resp) is True


@pytest.mark.parametrize(
    "command",
    [
        "echo ready && git commit -m x",
        "git commit -m x && echo done",
        "cd /other && git commit -m x",
    ],
)
def test_commit_landed_zero_exit_compound_can_trigger_verification(command):
    assert commit_landed(command, {"stdout": "", "exit_code": 0}) is True


@pytest.mark.parametrize(
    "command",
    [
        "git commit -m x & echo done",
        "echo ready & git commit -m x",
        "git commit -m x |& tee commit.txt",
        "echo ready |& git commit -m x",
    ],
)
def test_commit_landed_rejects_background_and_stderr_pipeline_status(command):
    assert commit_landed(command, {"stdout": "", "exit_code": 0}) is False


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
    # `echo gh pr create` returns True — accepted, documented over-broad behavior.
    # The function is a loose net for the pre-PR gate's fail-closed path; a
    # false positive is a human-overridable block, a false negative is a
    # fail-open hole.
    assert looks_like_gh_pr_create("echo gh pr create") is True


def test_looks_like_gh_pr_create_hard_to_parse_compound():
    # An unmatched quote makes tokenize() return None (strict parse fails).
    # looks_like must still return True on the same command where
    # find_gh_pr_create returns None, proving it is the net for parse failures.
    # This pairing is the load-bearing proof that looks_like is the fail-closed
    # net: find_gh_pr_create only works when the command is tokenizable; for
    # commands the strict parser chokes on, looks_like catches the PR attempt.
    cmd = "git commit -m 'it's done' && gh pr create"
    assert find_gh_pr_create(cmd, "/payload", env={}) is None  # strict parse fails → None
    assert looks_like_gh_pr_create(cmd) is True  # loose net catches it


# ---- find_gh_pr_create ------------------------------------------------------


def test_find_gh_pr_create_plain_uses_payload_cwd():
    assert find_gh_pr_create("gh pr create", "/payload", env={}) == "/payload"


def test_find_gh_pr_create_allows_selector_looking_title_value():
    command = "gh pr create --title GH_REPO=owner/other"
    assert find_gh_pr_create(command, "/payload", env={}) == "/payload"


@pytest.mark.parametrize(
    "command",
    [
        "echo ready && gh pr create",
        "gh pr create && echo done",
        "cd /other && gh pr create",
    ],
)
def test_find_gh_pr_create_rejects_every_compound_action(command):
    assert find_gh_pr_create(command, "/payload", env={}) is None
    assert looks_like_gh_pr_create(command) is True


@pytest.mark.parametrize(
    "command",
    [
        "echo ready & gh pr create",
        "gh pr create & echo done",
        "echo ready |& gh pr create",
        "gh pr create |& tee pr.txt",
    ],
)
def test_find_gh_pr_create_rejects_background_and_stderr_pipeline(command):
    assert find_gh_pr_create(command, "/payload", env={}) is None
    assert looks_like_gh_pr_create(command) is True


@pytest.mark.parametrize(
    "command",
    [
        "gh --repo o/r pr create",
        "gh --repo=o/r pr create",
        "gh -R o/r pr create",
        "gh -Ro/r pr create",
        "GH_REPO=o/r gh pr create",
        "gh pr create ; echo done",
        "gh pr create || echo failed",
        "gh pr create | tee pr.txt",
        "echo ready ; gh pr create",
    ],
)
def test_find_gh_pr_create_rejects_unresolved_target_forms(command):
    assert find_gh_pr_create(command, "/payload", env={}) is None


def test_find_gh_pr_create_rejects_inherited_gh_repo():
    assert find_gh_pr_create("gh pr create", "/payload", env={"GH_REPO": "o/r"}) is None


def test_find_gh_pr_create_rejects_present_empty_inherited_gh_repo():
    assert find_gh_pr_create("gh pr create", "/payload", env={"GH_REPO": ""}) is None


@pytest.mark.parametrize("base_cwd", [None, 7, ""])
def test_find_gh_pr_create_requires_string_payload_cwd(base_cwd):
    assert find_gh_pr_create("gh pr create", base_cwd, env={}) is None


def test_find_gh_pr_create_non_gh_none():
    assert find_gh_pr_create("git status", "/payload", env={}) is None


def test_unrelated_and_chain_is_not_a_pr_match():
    command = "echo ready && git status"
    assert find_gh_pr_create(command, "/payload", env={}) is None
    assert looks_like_gh_pr_create(command) is False


@pytest.mark.parametrize("operator", ["&", "|&"])
def test_unrelated_operator_compound_is_not_a_pr_match(operator):
    command = f"echo ready {operator} git status"
    assert find_gh_pr_create(command, "/payload", env={}) is None
    assert looks_like_gh_pr_create(command) is False


# ---- find_git_commit -------------------------------------------------------


def test_find_git_commit_plain_uses_payload_cwd():
    assert find_git_commit("git commit -m x", "/payload", env={}) == "/payload"


@pytest.mark.parametrize(
    "command",
    [
        "git commit -C HEAD",
        "git commit -m GIT_DIR=/other/.git",
        "git commit -m GIT_WORK_TREE=/other",
        "git commit -m GIT_COMMON_DIR=/other/.git",
    ],
)
def test_find_git_commit_allows_commit_position_selector_lookalikes(command):
    assert find_git_commit(command, "/payload", env={}) == "/payload"


@pytest.mark.parametrize(
    "command",
    [
        "echo ready && git commit -m x",
        "git commit -m x && echo done",
        "cd /other && git commit -m x",
    ],
)
def test_find_git_commit_rejects_every_compound_action(command):
    assert is_git_commit(command) is True
    assert find_git_commit(command, "/payload", env={}) is None


@pytest.mark.parametrize(
    "command",
    [
        "echo ready & git commit -m x",
        "git commit -m x & echo done",
        "echo ready |& git commit -m x",
        "git commit -m x |& tee commit.txt",
    ],
)
def test_find_git_commit_rejects_background_and_stderr_pipeline(command):
    assert is_git_commit(command) is True
    assert find_git_commit(command, "/payload", env={}) is None


@pytest.mark.parametrize(
    "command",
    [
        "git -C /other commit -m x",
        "git --git-dir /other/.git commit -m x",
        "git --git-dir=/other/.git commit -m x",
        "git --work-tree /other commit -m x",
        "git --work-tree=/other commit -m x",
        "GIT_DIR=/other/.git git commit -m x",
        "GIT_WORK_TREE=/other git commit -m x",
        "GIT_COMMON_DIR=/other/.git git commit -m x",
        "git commit -m x ; echo done",
        "git commit -m x || echo failed",
        "git commit -m x | tee commit.txt",
        "echo ready ; git commit -m x",
    ],
)
def test_find_git_commit_rejects_unresolved_target_forms(command):
    assert is_git_commit(command) is True
    assert find_git_commit(command, "/payload", env={}) is None


@pytest.mark.parametrize("name", ["GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR"])
def test_find_git_commit_rejects_inherited_git_target_selector(name):
    assert find_git_commit("git commit -m x", "/payload", env={name: "/other"}) is None


@pytest.mark.parametrize("name", ["GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR"])
def test_find_git_commit_rejects_present_empty_inherited_selector(name):
    assert find_git_commit("git commit -m x", "/payload", env={name: ""}) is None


@pytest.mark.parametrize("base_cwd", [None, 7, ""])
def test_find_git_commit_requires_string_payload_cwd(base_cwd):
    assert find_git_commit("git commit -m x", base_cwd, env={}) is None


def test_unrelated_and_chain_is_not_a_commit_match():
    command = "echo ready && git status"
    assert is_git_commit(command) is False
    assert find_git_commit(command, "/payload", env={}) is None


@pytest.mark.parametrize("operator", ["&", "|&"])
def test_unrelated_operator_compound_is_not_a_commit_match(operator):
    command = f"echo ready {operator} git status"
    assert is_git_commit(command) is False
    assert find_git_commit(command, "/payload", env={}) is None
