"""review_prompt.py — codex review argv builder + shared helpers.

Phase 2 introduced the reviewer-neutral ``strategy`` enum (``stuffed`` /
``fetched``) the selector hands each runner; after E2 only the codex path
remains.

- **codex `fetched`** runs as a bare independent reviewer:
  ``codex review --base <ref>``. No prompt is piped in. Codex pages
  through ``<ref>...HEAD`` with its built-in rubric + tooling. Codex
  acts as a different model with no vested interest in the work; the
  project's adversarial-review SKILL is intentionally NOT injected
  in this mode.
- **codex `stuffed`** uses ``codex review -`` and reads ``skill_text +
  diff`` from stdin. The adversarial-review SKILL is injected here by
  design — codex's built-in rubric is rubric-only and benefits from
  the project's posture framing when the diff is small enough to
  embed inline.

``claude`` argv builders and prompt assembly (``claude_runner_argv``,
``build_claude_prompt``, ``CLAUDE_TOOLS``, ``CLAUDE_STUFFED_TOOLS``) were
removed in E2 — the ``claude -p`` reviewer path is gone.

Codex feeds the same severity counter on stdout (line-start
``[P0]`` / ``[P1]`` / ``[P2]`` / ``[P3]``).
"""

from __future__ import annotations

import shlex
import subprocess


# ---- shared helpers --------------------------------------------------------


def _git_in(target_git_dir: str | None, *args: str) -> subprocess.CompletedProcess:
    cmd = ["git"]
    if target_git_dir:
        cmd += ["-C", target_git_dir]
    cmd += list(args)
    # timeout-bounded + degrade-safe: gather_touched_paths runs inside the
    # pre-PR hard-block window, so a stuck git must not hang `gh pr create`.
    # On timeout/OS error return a non-zero CompletedProcess so callers that
    # branch on returncode degrade to their documented empty value.
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=5)
    except (OSError, subprocess.TimeoutExpired):
        return subprocess.CompletedProcess(cmd, 1, stdout="", stderr="")


_VALID_STRATEGIES = ("fetched", "stuffed")


def _validate_strategy(strategy: str) -> None:
    """Raise ValueError unless *strategy* is a known invocation strategy.

    The strategy selects the codex subcommand (``stuffed`` → ``codex review -``;
    ``fetched`` → ``codex review --base <ref>``). An unknown value must fail
    loudly at the boundary rather than silently routing to the wrong subcommand.
    """
    if strategy not in _VALID_STRATEGIES:
        raise ValueError(
            f"unknown strategy {strategy!r}; expected one of {_VALID_STRATEGIES}"
        )


def gather_touched_paths(target_git_dir: str | None, base: str) -> str:
    """Return paths_csv for the review-log row + loop-of-fixes overlap.

    Comma-joined. Rename pairs decompose to ``src,dst`` order. Deletions
    are included (overlap on a repeatedly deleted+recreated path IS a
    legitimate loop signal). Returns an empty string if the diff query
    fails — callers degrade gracefully (the log row carries an empty
    paths field).
    """
    r = _git_in(target_git_dir, "diff", "--name-status", f"{base}...HEAD")
    if r.returncode != 0:
        return ""
    full: list[str] = []
    for line in r.stdout.splitlines():
        if not line:
            continue
        parts = line.split("\t")
        if not parts:
            continue
        status = parts[0]
        if status.startswith("R") and len(parts) >= 3:
            full.append(parts[1])
            full.append(parts[2])
        elif len(parts) >= 2:
            full.append(parts[1])
    return ",".join(full)


# ---- codex runner ----------------------------------------------------------


def codex_runner_argv(
    target_git_dir: str | None,
    base: str,
    *,
    model: str | None = None,
    effort: str | None = None,
    strategy: str = "fetched",
) -> list[str]:
    """Return argv for codex review.

    ``strategy`` is reviewer-neutral per Phase 2 (``"stuffed"`` or
    ``"fetched"``):
      * ``fetched`` → ``codex review --base <ref>`` (default; codex
        fetches the diff itself).
      * ``stuffed`` → ``codex review -`` (caller pipes the diff on stdin).

    ``model`` and ``effort`` land as ``-c model=...`` and
    ``-c model_reasoning_effort=...`` overrides when present. Per the
    tiered-reviewer plan REPORT Rounds 6-8 they're omitted when None
    (codex uses its configured default).

    When ``target_git_dir`` is set (``cd other-repo && gh pr create``),
    sh-wraps the invocation so codex runs in the target tree.
    """
    # -c is a `codex review` subcommand option, NOT a top-level codex
    # flag. Place after the subcommand or the override is silently
    # dropped. Live verification (`codex review --help` excerpt):
    #     Options:
    #       -c, --config <key=value>
    #             Override a configuration value...
    # `codex --help` lists `review` as a subcommand and does NOT list
    # `-c` among the top-level options, confirming the asymmetry. If
    # codex ever lifts `-c` to top-level, the test below will still
    # pass (position is enforced relative to `review`) but the runtime
    # will continue to honor the override; nothing breaks.
    _validate_strategy(strategy)
    cmd: list[str] = ["codex", "review"]
    # The TOML value is single-line-quoted with double quotes per the
    # `-c` example in codex's help. Model + effort strings come from
    # project config (`review_tiers.<tier>.{model,default_effort}`) and
    # the Phase 1 validator restricts effort to {low, medium, high};
    # model is unconstrained but project-controlled. A model name
    # containing `"` would mangle the TOML — accepted because it's
    # vanishingly unlikely and project-controlled; the Phase 1
    # validator would be the natural place to add a `"`-rejecting
    # check if a real model slug ever arrives with embedded quotes.
    if model:
        cmd.extend(["-c", f'model="{model}"'])
    if effort:
        cmd.extend(["-c", f'model_reasoning_effort="{effort}"'])
    if strategy == "stuffed":
        cmd.append("-")
    else:
        cmd.extend(["--base", base])
    if target_git_dir:
        # Single-arg sh -c script that cd's then execs the whole codex argv.
        # The cmd tokens are shlex-quoted and interpolated as literals
        # before sh ever runs, so the exec line doesn't reference any
        # positional arg past $1 — no shift needed.
        script = f'cd "$1" && exec {" ".join(shlex.quote(c) for c in cmd)}'
        return ["sh", "-c", script, "_", target_git_dir]
    return cmd


