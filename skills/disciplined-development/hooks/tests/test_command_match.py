"""Tests for hooks.lib.command_match — the slim gh/git matchers (A5)."""

import os

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
    assert find_gh_pr_create(cmd) is None  # strict parse fails → None
    assert looks_like_gh_pr_create(cmd) is True  # loose net catches it


# ---- find_gh_pr_create ------------------------------------------------------


def test_find_gh_pr_create_plain():
    result = find_gh_pr_create("gh pr create")
    assert result is not None
    # No chained `cd` → cwd is the process working directory.
    assert result == os.getcwd()


def test_find_gh_pr_create_chained_cd():
    cwd = find_gh_pr_create("cd /other && gh pr create")
    assert cwd == "/other"


def test_find_gh_pr_create_chained_cd_last_wins():
    """Multiple chained `cd`s: the LAST one wins, and a relative `cd` is
    anchored to the process cwd (not to the prior absolute `cd`).

    This pins the accepted-edge contract (see the production comment in
    command_match.py): the resolver does not compose relative `cd`s. A
    future fix that correctly resolves `cd subdir` against the prior
    absolute `cd` must update this test in lockstep. E2's gh-wrapper
    forwards this cwd to `external_review.py` via `pre_pr_review.py`."""
    # Last `cd` is absolute → it wins outright.
    cwd = find_gh_pr_create("cd /a && cd /b && gh pr create")
    assert cwd == "/b"
    # Last `cd` is relative → anchored to process cwd, NOT to `/a`.
    cwd = find_gh_pr_create("cd /a && cd subdir && gh pr create")
    assert cwd == os.path.join(os.getcwd(), "subdir")


def test_find_gh_pr_create_global_flag_skipped():
    result = find_gh_pr_create("gh --repo o/r pr create")
    assert result is not None


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


# ---- classify_gh_pr_create (the gate's single verdict) -----------------------
# Verdict table from plans/2026-07-11-pre-pr-review-false-positive-fix.md.

from hooks.lib.command_match import (  # noqa: E402
    VERDICT_NOT_PR,
    VERDICT_PR,
    VERDICT_PR_UNRESOLVABLE,
    VERDICT_SUSPICIOUS,
    classify_gh_pr_create,
)


def test_classify_plain_pr_resolves_process_cwd():
    verdict, cwd = classify_gh_pr_create("gh pr create --title x")
    assert verdict == VERDICT_PR
    assert cwd == os.getcwd()


def test_classify_chained_cd_resolves():
    assert classify_gh_pr_create("cd /repo && gh pr create") == (VERDICT_PR, "/repo")


def test_classify_unexpandable_cd_is_unresolvable():
    verdict, cwd = classify_gh_pr_create("cd $DIR && gh pr create")
    assert verdict == VERDICT_PR_UNRESOLVABLE
    assert cwd is None


def test_classify_repo_flag_forms_are_pr():
    assert classify_gh_pr_create("gh --repo o/r pr create")[0] == VERDICT_PR
    assert classify_gh_pr_create("gh -R o/r pr create")[0] == VERDICT_PR


def test_classify_shell_wrapper_recurses():
    assert classify_gh_pr_create("bash -c 'gh pr create'")[0] == VERDICT_PR


def test_classify_wrapped_shell_behind_prefix_is_pr():
    # The shell token need not be segment-head: nohup/env/time prefixes must
    # not hide a wrapped PR creation (fail-closed duty before the loose net
    # narrowed).
    assert classify_gh_pr_create("nohup bash -c 'gh pr create'")[0] == VERDICT_PR


def test_classify_triple_at_non_head_position_is_pr():
    # eval/env/nohup/xargs heads: the consecutive token triple decides,
    # position-independent — no wrapper enumeration.
    for cmd in (
        "eval gh pr create",
        "env GH_TOKEN=x gh pr create",
        "nohup gh pr create",
        "xargs gh pr create",
    ):
        assert classify_gh_pr_create(cmd)[0] == VERDICT_PR, cmd


def test_classify_eval_string_arg_recurses():
    assert classify_gh_pr_create('eval "gh pr create"')[0] == VERDICT_PR


def test_classify_unquoted_eval_behind_cd_keeps_outer_cwd():
    # The segment's own triple must decide BEFORE wrapper recursion: recursing
    # into `gh pr create` would lose the outer `cd` and report the process cwd.
    assert classify_gh_pr_create("cd /repo && eval gh pr create") == (
        VERDICT_PR,
        "/repo",
    )


def test_classify_wrapped_shell_behind_cd_keeps_outer_cwd():
    # The subshell inherits the outer cwd — the gate must review /repo, not
    # the process cwd (a wrong-tree review defeats the gate).
    assert classify_gh_pr_create("cd /repo && bash -c 'gh pr create'") == (
        VERDICT_PR,
        "/repo",
    )
    assert classify_gh_pr_create('cd /repo && eval "gh pr create"') == (
        VERDICT_PR,
        "/repo",
    )


def test_classify_wrapped_shell_behind_unexpandable_cd_is_unresolvable():
    verdict, cwd = classify_gh_pr_create("cd $DIR && bash -c 'gh pr create'")
    assert verdict == VERDICT_PR_UNRESOLVABLE
    assert cwd is None


# ---- cd-form resolution (the round-2 axis: every cd form pinned) -------------


def test_classify_bare_cd_resolves_home():
    # `cd` with no target goes to $HOME — not the caller's cwd.
    assert classify_gh_pr_create("cd && gh pr create") == (
        VERDICT_PR,
        os.path.expanduser("~"),
    )


def test_classify_tilde_cd_expands():
    assert classify_gh_pr_create("cd ~/repo && gh pr create") == (
        VERDICT_PR,
        os.path.expanduser("~/repo"),
    )


def test_classify_cd_dash_is_unresolvable():
    # `cd -` targets $OLDPWD, unknowable from the command text — fail loud.
    verdict, cwd = classify_gh_pr_create("cd - && gh pr create")
    assert verdict == VERDICT_PR_UNRESOLVABLE
    assert cwd is None


def test_classify_cd_symlink_flags_skipped():
    assert classify_gh_pr_create("cd -P /repo && gh pr create") == (
        VERDICT_PR,
        "/repo",
    )


# ---- heredoc bodies are data (round-2 P2) ------------------------------------


def test_classify_non_shell_heredoc_body_is_data():
    # A quote-balanced heredoc body tokenizes; its lines must NOT become
    # command segments — a git-commit message quoting the phrase is data,
    # neither delegated nor blocked.
    cmd = "git commit -F - <<'MSG'\nsee gh pr create docs\nMSG"
    assert classify_gh_pr_create(cmd) == (VERDICT_NOT_PR, None)


def test_classify_shell_fed_heredoc_body_still_suspicious():
    # A heredoc piped INTO a shell executes its body — the body keeps the
    # word-bounded loose check (fail-closed carve-out to body-stripping).
    verdict, _ = classify_gh_pr_create("bash <<'EOF'\ngh pr create\nEOF")
    assert verdict == VERDICT_SUSPICIOUS


def test_classify_echo_mention_stays_pr_shaped():
    # Documented over-broad bias, unchanged: three bare tokens are treated as
    # a PR attempt even under echo.
    assert classify_gh_pr_create("echo gh pr create")[0] == VERDICT_PR


def test_classify_quoted_phrase_argument_is_not_pr():
    # Observed false positive: the quoted phrase is ONE token after shlex —
    # never a triple; strict is authoritative for tokenizable commands.
    verdict, _ = classify_gh_pr_create('grep -n "gh pr create" hooks/pre_pr_review.py')
    assert verdict == VERDICT_NOT_PR


def test_classify_tokenizable_prose_is_not_pr():
    # Tokenizes fine, no triple → the loose net is never consulted.
    verdict, _ = classify_gh_pr_create(
        'git commit -m "the gh matcher, per project rules, was created"'
    )
    assert verdict == VERDICT_NOT_PR


def test_classify_untokenizable_prose_subsequences_are_not_pr():
    # Observed false positive: an unbalanced quote defeats tokenize(); the
    # old loose net matched gh/pr/create as LETTER-RUNS inside ordinary words
    # (right/project/created). Word-bounded, this is clean.
    cmd = "git commit -m 'it's right: the project provenance was created'"
    assert classify_gh_pr_create(cmd) == (VERDICT_NOT_PR, None)


def test_classify_untokenizable_underscore_words_are_not_pr():
    # \b treats _ as a word char: pre_pr_review contains no word `pr`.
    cmd = "git commit -m 'it's the pre_pr_review gh matcher fix'"
    assert classify_gh_pr_create(cmd) == (VERDICT_NOT_PR, None)


def test_classify_untokenizable_literal_words_are_suspicious():
    # Accepted residual: word-level literal mention in an unparseable command
    # still blocks (fail-closed net, now self-diagnosing at the gate).
    cmd = "git commit -m 'it's done, see gh pr create docs'"
    assert classify_gh_pr_create(cmd) == (VERDICT_SUSPICIOUS, None)


def test_classify_empty_is_not_pr():
    assert classify_gh_pr_create("") == (VERDICT_NOT_PR, None)
    assert classify_gh_pr_create("   ") == (VERDICT_NOT_PR, None)


def test_looks_like_word_bounded_rejects_letter_runs():
    # The loose net no longer matches subsequences inside ordinary words.
    assert looks_like_gh_pr_create("right: the project was created") is False
