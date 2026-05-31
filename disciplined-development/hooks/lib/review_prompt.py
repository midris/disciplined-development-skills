"""review_prompt.py — shared review-runner argv + claude prompt assembly.

Two reviewer paths, deliberately asymmetric. Phase 2 introduced the
reviewer-neutral ``strategy`` enum (``stuffed`` / ``fetched``) the
selector hands each runner; per-reviewer behavior differs by strategy:

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
  embed inline. Does NOT include the claude-side review-context block
  (base / HEAD / paths / plan / spec): codex stays project-context-light
  to preserve its independent-cross-check value.

- **claude `fetched`** receives the adversarial-review SKILL.md +
  a "Review context" block (base, HEAD sha, paths CSV, active-plan +
  governing-spec paths). The diff is NOT pre-stuffed — claude fetches
  it via ``Bash(git diff:*)`` / ``Read`` from the ``--tools`` allowlist.
- **claude `stuffed`** receives the same prompt PLUS the diff body
  embedded inline; the ``--tools`` allowlist drops ``Bash(git diff:*)``
  since the diff is already in-prompt (see ``CLAUDE_STUFFED_TOOLS``).

Both runners feed the same severity counter on stdout (line-start
``[P0]`` / ``[P1]`` / ``[P2]`` / ``[P3]``).
"""

from __future__ import annotations

import pathlib
import re
import shlex
import subprocess
from typing import Callable


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

    The strategy selects the reviewer's tool allowlist (claude) or
    subcommand (codex). An unknown value must fail loudly at the boundary
    rather than silently routing to the wrong allowlist — which surfaces
    downstream as a denied-tool error or wrong review semantics. Enforced
    identically by build_claude_prompt and both runner-argv builders so the
    contract lives in one place.
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


# ---- claude runner ---------------------------------------------------------


# Comma-joined matchers for ``claude -p --tools``. Read-only git
# operations only — diff/log/show/rev-parse/status/diff-tree/for-each-ref.
# No writes, no network, no PR creation. Pairs with Read/Grep/Glob/Skill/
# TodoWrite for file inspection + skill-loading + scratchpad scoping.
CLAUDE_TOOLS = (
    "Read,Grep,Glob,Skill,TodoWrite,"
    "Bash(git diff:*),Bash(git log:*),Bash(git show:*),"
    "Bash(git rev-parse:*),Bash(git status:*),"
    "Bash(git diff-tree:*),Bash(git for-each-ref:*)"
)

# Stuffed strategy: the diff is already embedded in the prompt, so
# Bash(git diff:*) is intentionally dropped. The remaining git-read
# tools stay — claude may still want to inspect file history beyond
# the embedded diff (git log, git show on referenced shas).
CLAUDE_STUFFED_TOOLS = (
    "Read,Grep,Glob,Skill,TodoWrite,"
    "Bash(git log:*),Bash(git show:*),"
    "Bash(git rev-parse:*),Bash(git status:*),"
    "Bash(git diff-tree:*),Bash(git for-each-ref:*)"
)


def claude_runner_argv(
    *,
    model: str | None = None,
    effort: str | None = None,
    strategy: str = "fetched",
) -> list[str]:
    """Return argv for ``claude -p`` invocation with review-scoped tools.

    The prompt (rubric + review context) is piped on stdin by the
    caller. ``--fallback-model haiku`` is intentional: review is cheap
    + repeated; the cheaper model is the right fit, with the default
    model still tried first.

    ``strategy`` is reviewer-neutral per Phase 2:
      * ``fetched`` → full tool list including ``Bash(git diff:*)`` so
        claude pulls the diff via the Bash tool.
      * ``stuffed`` → ``CLAUDE_STUFFED_TOOLS`` (no ``Bash(git diff:*)``);
        the diff is embedded in the prompt instead.

    ``model``/``effort`` land as ``--model``/``--effort`` flags when
    present.
    """
    _validate_strategy(strategy)
    tools = CLAUDE_TOOLS if strategy == "fetched" else CLAUDE_STUFFED_TOOLS
    argv: list[str] = ["claude", "-p", "--tools", tools]
    if model:
        argv.extend(["--model", model])
    if effort:
        argv.extend(["--effort", effort])
    argv.extend([
        "--no-session-persistence",
        "--disable-slash-commands",
        "--exclude-dynamic-system-prompt-sections",
        "--fallback-model", "haiku",
    ])
    return argv


# ---- claude prompt assembly ------------------------------------------------


def resolve_plan_and_spec_paths(
    repo_root: str | None,
    resolve_active_plan_fn: Callable[[], tuple[str, str] | None],
) -> tuple[str, str]:
    """Return (plan_path, spec_path) as filesystem paths (empty on miss).

    The plan file is opened only to grep for a ``plans/specs/...md``
    reference — content is not retained. Callers pass these paths into
    the claude prompt so the reviewer can ``Read`` them on demand
    rather than receive the full text pre-stuffed.

    The plan-resolver is passed in (rather than hard-imported from
    ``dd_lib``) to keep this module dependency-free.
    """
    plan_path = ""
    spec_path = ""
    plan_tuple = resolve_active_plan_fn()
    if plan_tuple and repo_root:
        plan_rel = plan_tuple[0]
        candidate = pathlib.Path(repo_root) / plan_rel
        if not candidate.is_file():
            candidate = pathlib.Path(plan_rel)
        if candidate.is_file():
            plan_path = str(candidate)
            try:
                content = candidate.read_text()
            except OSError:
                return plan_path, spec_path
            m = re.search(r"plans/specs/[a-zA-Z0-9._/-]+\.md", content)
            if m:
                spec_candidate = pathlib.Path(repo_root) / m.group(0)
                if spec_candidate.is_file():
                    spec_path = str(spec_candidate)
    return plan_path, spec_path


def build_claude_prompt(
    *,
    prompt_header: str,
    base: str,
    head_sha: str,
    paths_csv: str,
    plan_path: str = "",
    spec_path: str = "",
    strategy: str = "fetched",
) -> str:
    """Assemble the lean claude review prompt.

    Structure:
      <adversarial-review SKILL.md content>
      ## Review context
        base, HEAD sha, paths CSV, plan/spec paths (if any)
      Strategy-specific guidance (see below)
      Output rubric reminder (line-start [P0]..[P3]).

    ``strategy`` must match the tool allowlist chosen by
    ``claude_runner_argv`` — otherwise the prompt and the allowlist
    disagree and the reviewer hits a denied tool call:

    * ``fetched`` → instructs the reviewer to ``git diff`` / ``git log`` /
      ``git show`` / ``Read`` directly. The diff is NOT in the prompt
      body; the engine appends nothing extra.
    * ``stuffed`` → tells the reviewer the diff is embedded below
      (the engine then appends it as a fenced ``diff`` block). Critically
      does NOT instruct ``git diff`` — ``CLAUDE_STUFFED_TOOLS`` drops
      ``Bash(git diff:*)`` and a "fetch it yourself" instruction would
      trigger a denied-tool error before the reviewer found the embed.
    """
    _validate_strategy(strategy)
    prompt = prompt_header
    prompt += (
        "\n\n## Review context\n\n"
        f"Review base: `{base}`\n"
        f"HEAD sha: `{head_sha}`\n"
        f"Touched paths (CSV): `{paths_csv}`\n"
    )
    if plan_path:
        prompt += f"Active plan: `{plan_path}` — Read for chunk scope.\n"
    if spec_path:
        prompt += f"Governing spec: `{spec_path}` — Read for the design contract.\n"
    if strategy == "stuffed":
        prompt += (
            "\nThe full diff is embedded below as a fenced `diff` block —\n"
            "scroll to the bottom of this prompt to read it. `Bash(git diff:*)`\n"
            "is intentionally NOT in your tool allowlist; do not attempt to\n"
            "fetch the diff via shell. For deeper context use:\n"
            f"  - `git log {base}...HEAD` — commit-level narrative\n"
            f"  - `git show {head_sha}:<path>` — HEAD blob of any touched file\n"
            "  - `Read <path>` — current worktree version\n"
            "\nReport findings using the severity rubric from the adversarial-review\n"
            "skill above (`[P0]` / `[P1]` / `[P2]` / `[P3]`, one finding per line\n"
            "at line-start so the severity counter matches).\n"
        )
    else:
        prompt += (
            "\nThe diff and file contents are NOT pre-stuffed. Fetch them yourself:\n"
            f"  - `git diff {base}...HEAD` — full diff (breadth scan)\n"
            f"  - `git diff {base}...HEAD -- <path>` — single-file hunks\n"
            f"  - `git log {base}...HEAD` — commit-level narrative\n"
            f"  - `git show {head_sha}:<path>` — HEAD blob of any touched file\n"
            "  - `Read <path>` — current worktree version\n"
            "\nReport findings using the severity rubric from the adversarial-review\n"
            "skill above (`[P0]` / `[P1]` / `[P2]` / `[P3]`, one finding per line\n"
            "at line-start so the severity counter matches).\n"
        )
    return prompt
