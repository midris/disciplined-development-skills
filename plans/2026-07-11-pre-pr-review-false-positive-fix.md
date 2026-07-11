# Fix pre_pr_review false positives (loose gh-pr-create matcher) — implementation plan

**Status:** parked (owner ruling 2026-07-11) on `fix/pre-pr-review-false-positives` — implementation stopped at the review-loop cap; branch kept as-is (7 commits, suites green), NOT merged; the four round-3 P1s are open and the A/B/C decision below is unmade. The consumer-visible false positives remain live on `main` until this resumes — workaround: `git commit -F <file>` for blocked heredoc commits.
**Files:** `skills/disciplined-development/hooks/lib/command_match.py`, `hooks/pre_pr_review.py`, `hooks/tests/test_command_match.py`, `hooks/tests/test_pre_pr_review.py`; sweep `hooks/README.md` if it describes the matcher.
**Commands:** `cd skills/disciplined-development/hooks && python3 -m pytest -q` (test-first; commits land green, test + impl same commit).

## Problem (observed 2026-07-11, steno consumer)

Three verified false-positive blocks, all emitting the misleading "couldn't resolve the target directory for a `gh pr create`" message:

1. **Heredoc `git commit`s blocked** (twice): a heredoc makes `tokenize()` return `None`, so `find_gh_pr_create` returns `None`; the gate then consults `looks_like_gh_pr_create`, which scans the **raw string** for `"gh"`, `"pr"`, `"create"` as **unanchored substrings in order**. Ordinary commit-message prose matches — e.g. "ri**gh**t … **pr**oject … **create**d". Long heredoc messages (which consumer CLAUDE.md conventions *mandate*) match almost surely.
2. **A `grep -n "gh pr create" <file>` blocked**: the command tokenizes fine and the strict parser correctly finds no `gh` invocation (the quoted phrase is a single argument token) — but the gate consults the loose net on **every** strict `None`, not only on tokenize failure, and the literal substring matches.

Root causes, in `pre_pr_review.main` + `command_match`:
- The loose net's intended scope was the tokenize-failure ambiguity ("`None` is ambiguous"), but it runs unconditionally whenever `find_gh_pr_create` returns `None` — overriding the strict parser's affirmative "not a PR" on tokenizable commands.
- The loose net matches unanchored substrings, far broader than its own docstring's examples ("a command that merely *mentions* these tokens"); prose subsequences were not the documented trade.
- One block message covers three distinct conditions (matched-but-unresolvable-cwd, untokenizable-and-suspicious, and the false positives), so a blocked agent cannot tell why.

The fail-closed bias is correct and stays: a false negative here is a fail-open hole at the stack's only hard gate. The fix narrows the nets without opening one.

## Design (decisions + rationale)

**D1 — Strict is authoritative for tokenizable commands.** When `tokenize()` succeeds, the strict token-level result decides alone; the loose net is consulted **only** when tokenization fails (heredocs and similar). This kills FP class 2 by construction.

**D2 — Strict detection generalizes to a consecutive token triple.** Before trusting strict-only on tokenizable input, close its wrapper gaps (`eval gh pr create`, `env X=y gh pr create`, `exec`/`command`/`nohup`/`time` prefixes, `xargs`-argument forms — today these are caught only by the loose net, so D1 alone would fail them open). Rule: a segment is PR-shaped when it contains the **consecutive token sequence** `gh` … `pr` `create` at any position (gh global flags `-R`/`--repo`/`--x=y` forms permitted between `gh` and `pr`, as today). Position-independence replaces wrapper enumeration. Two deliberate consequences, on-page:
- `echo gh pr create` stays PR-shaped (three bare tokens) — the current documented over-broad bias, unchanged.
- A quoted phrase (`grep "gh pr create"`) is one token, never a triple — allowed.
Additionally, mirror the existing `SHELLS -c` re-tokenization for `eval` with a single string argument (`eval "gh pr create"`), which the triple rule can't see inside.

**D3 — The loose net gets word boundaries.** For untokenizable commands (and the gate's crash-path fallback), match `gh`, `pr`, `create` in order as whole words (regex word-boundary semantics; note `\b` treats `_` as a word char, so `pre_pr_review` does not contain a word `pr`). Prose subsequences stop matching; a heredoc that literally writes `gh pr create` as words still blocks — accepted residual, rare, and self-diagnosing under D5. Bias-toward-True is preserved exactly where the genuine ambiguity lives.

**D4 (amended in review round 2) — Heredoc bodies are data, with a shell-receiver carve-out.** Originally rejected ("`bash <<EOF` executes its body, so stripping is a fail-open hole"); the round-2 external review showed the rejection was incomplete the other way: a QUOTE-BALANCED body tokenizes, its lines become command segments, and a body line quoting the phrase took the *delegate* path. Amended rule: strip heredoc bodies before matching (a commit message quoting the phrase neither delegates nor blocks); a body whose receiving segment head is a shell keeps the word-bounded loose check (executes → fail-closed); if the stripped command still can't tokenize, the loose net runs over the full original text.

**D5 — Distinct, self-diagnosing block messages.** Split the single message into: (a) *matched `gh pr create` but cwd unresolvable* (keep the current rewrite/bypass remedy), and (b) *command couldn't be parsed and mentions `gh pr create` as words* — naming the matched heuristic so the next false positive is diagnosable from the message alone. Keep the `reviews.jsonl` ERROR row on both block paths (reason `unparseable` vs a new distinct reason for (b)).

**D6 — API shape.** Replace the gate's two-call dance (`find_gh_pr_create` + `looks_like_gh_pr_create` side-channel) with one classifier returning a total verdict the gate switches on — four outcomes: not-PR (allow) · PR with resolved cwd (delegate) · PR with unresolvable cwd (block, message a) · untokenizable-and-suspicious (block, message b). Keep a word-bounded raw-text predicate exported for the gate's exception handler (which must classify without trusting prior state). Exact names are the implementer's; `is_git_commit`/`commit_landed` are untouched.

## Build order (test-first; the tables are the contract)

- [x] **Classifier verdicts** (`test_command_match.py`): each row its own red→green. (17 new tests; all pre-existing matcher tests unchanged and green.)

  | input | verdict |
  |---|---|
  | `gh pr create --title x` | PR, cwd = process cwd |
  | `cd /repo && gh pr create` | PR, cwd = `/repo` |
  | `cd $DIR && gh pr create` | PR, cwd unresolvable |
  | `gh --repo o/r pr create` / `gh -R o/r pr create` | PR |
  | `bash -c 'gh pr create'` | PR (existing recursion) |
  | `eval "gh pr create"` | PR (D2 eval re-tokenization) |
  | `eval gh pr create` · `env GH_TOKEN=x gh pr create` · `nohup gh pr create` | PR (triple at non-head position) |
  | `echo gh pr create` | PR (documented over-broad, unchanged) |
  | `grep -n "gh pr create" file.py` | not-PR (quoted phrase = one token) |
  | `git commit -m "the gh matcher, per project rules, was created"` | not-PR (tokenizes; no triple; loose net not consulted) |
  | heredoc `git commit` whose body has prose subsequences (e.g. "right… project… created") | not-PR (untokenizable; word-bounded loose finds no `gh`/`pr`/`create` words) |
  | heredoc `git commit` whose body literally contains the words `gh pr create` | not-PR (body is data — D4 as amended; a residual block remains only for untokenizable non-heredoc text, e.g. unbalanced quotes) |
  | `bash <<EOF` heredoc whose body contains `gh pr create` | untokenizable-and-suspicious (shell receiver executes the body — fail-closed carve-out) |
  | empty string / whitespace | not-PR |

- [x] **Gate behavior** (`test_pre_pr_review.py`): allow-path for the two observed FP classes (heredoc-prose commit; grep-with-literal) asserting exit 0 and no ERROR row; the two block paths assert exit 2, their distinct messages, and their distinct `reviews.jsonl` reasons; delegate path unchanged (existing tests keep binding the exit-code translation and `DD_SKIP_PR_REVIEW`); crash-path fallback still blocks iff the word-bounded predicate matches. (3 new tests; the heredoc-prose gate path was already healed by the cycle-1 matcher change — its test observed green there, red on the other two.)
- [x] **Docs sweep:** matcher docstrings rewritten to the new contract (the "deliberately over-broad" text moves to the untokenizable-only scope); `hooks/README.md` (gate table row, wrapper paragraph, ERROR-reason enumeration) + `ARCHITECTURE.md` (pre-PR sequence diagram gains the second block branch); message-text change noted in the commit bodies (agent-facing, not config schema — no MIGRATIONS.md entry).

## Review loop (external gate, 2026-07-11)

- **Round 1 — BLOCK, 1×P1:** wrapper recursion dropped the outer `cd` (wrong-tree review). Fixed: the preceding-`cd` walk extracted to one helper used by the triple path AND the wrapper recursion; outer chain wins, unresolvable outer fails loud.
- **Round 2 — BLOCK, 1×P1 + 2×P2:** the P1/P2 `cd` findings (bare `cd`, `~` targets) plus round 1 named one axis — incomplete `cd`-form resolution — swept whole: bare→`$HOME`, `~`→expanduser, `-`→unresolvable, `-L/-P/-e/-@` flags skipped. The remaining P2 (quote-balanced heredoc bodies tokenized into command segments, taking the delegate path) amended D4 above.
- **Round 3 — BLOCK, 4×P1 (the loop cap; iteration stopped, escaped to the owner):** `env X=1 bash <<EOF…` evades the shell-receiver check (skip_env expects VAR= tokens, not the `env` command word) — fail-open; the heredoc tag regex under-lexes `<<END-MSG` as `END`, so the body never terminates and a later real PR command strips away — fail-open; chained relative `cd`s don't compose (pre-existing documented edge, re-litigated); an outer `cd` overrides an explicit inner `cd` in wrappers (round-1's documented edge, re-litigated).

**Pattern verdict (cap-mandated, over all three rounds as one set):** every finding — R1's dropped outer `cd`, R2's cd-form gaps and heredoc-bodies-as-segments, R3's receiver/lexer/composition gaps — is one root: **the matcher re-implements shell semantics piecemeal (cd resolution, heredoc lexing, wrapper transparency), and each approximation ships a new wrong-tree or fail-open edge.** The round-2 heredoc parser itself introduced two of round 3's fail-opens. Per the loop skill and Principle 7, more layers is the wrong direction; the escape decision (below) is the owner's.

**Owner decision needed — options:**
- **A (recommended): shrink the trusted surface.** Delegate ONLY the canonical shape (a strict segment-head triple, cwd from nothing or an absolute-`cd` chain); any other construct that word-mentions the phrase in executable position blocks with precise rewrite guidance ("re-run as `cd /abs/path && gh pr create …`"). Delete the heredoc body parser and wrapper cwd inheritance (wrapped/heredoc-fed forms block-with-guidance instead of being emulated). Keeps both original false-positive fixes (word-bounded loose net; strict-authoritative quoted-argument handling); converts all four R3 P1s from fail-open/wrong-tree into loud, trivially-rewritable blocks.
- **B: keep the emulation design and fix the four P1s** (a fourth review cycle against the cap — needs an explicit owner go).
- **C: park the branch** — cycles 1–2's uncontested core (the two observed false-positive classes) already works; the contested surface is the wrapper/heredoc/cd emulation added while chasing reviewer findings.

## Acceptance

Full hook suite green; every table row covered by a named test; the two observed steno commands (a heredoc commit with ordinary prose, `grep -n "gh pr create" …`) pass through a locally-run gate (pipe a synthetic PreToolUse JSON envelope through `pre_pr_review.py`, assert exit 0 — the same harness the existing gate tests use).
