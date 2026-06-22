# Review Tooling Overhaul — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use `superpowers:subagent-driven-development`
> (recommended) or `superpowers:executing-plans` to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax. Follows `lean-plan-writing`: **prose is the
> contract; code is the implementer's job.**

**Design reference:** `plans/2026-06-21-review-tooling-overhaul.md` (architecture +
locked decisions D1–D7 + diagrams + log schema). Read it first.

## How to read this plan (target-first, ground at build time)

This plan describes the **target state to build** and the **goals** of each change —
it deliberately does **not** assert current-state facts (who calls what, exact line
numbers, "the only caller", types of existing fields). Those rot between chunks and
are the wrong thing to encode in a forward-looking doc.

**Ground every current-state claim against the source at the moment you act on it**
(`disciplined-research`): when a task says "delete X" or "reuse Y", first `grep`/read
the live tree to find what actually depends on it, then reconcile what you find — in
the same commit. The "Reconcile" sections list **known starting points, not closed
sets**: treat them as "at least these — verify and extend live." A consumer you find
that isn't listed is expected, not an exception.

## Goal & shape

Delete the `dd_review_runner.py` engine and the `/dd-review` command; stand up two
small tools on the surviving `lib/` primitives — a model-callable **log-review** tool
and a hook-callable whole-repo **external-review** gate — with one consolidated,
retrospective-grade review log. Four PR-sized chunks: (1) log-review tool, (2) gate,
(3) remove-and-reconcile the old machinery + docs, (4) all `SKILL.md` edits last.

**Tech stack:** Python 3 stdlib only, pytest; bash installer; markdown skills/docs;
codex CLI (external reviewer).

## Global constraints

- **stdlib-only** Python. **Test-first; commits land green** (test + impl same
  commit; never `test:` then `feat:`). Hook-stack + installer changes are
  mandatory-test.
- **Never squash-merge** (`gh pr merge --merge`); one PR per chunk.
- **Each commit body:** conventional-prefix subject; `References swept:` per
  `sweeping-stale-references` when load-bearing references move; `Verification:`
  listing commands actually run; `Co-Authored-By:` trailer from CLAUDE.md.
- **No `SKILL.md` edits before Chunk 4** (Decision 6 — drafted via
  `superpowers:writing-skills`, user-reviewed before applied).
- **Verify before claiming done** (Gate 3) and **diff every subagent commit against
  its scope** (`dispatching-development-subagents`).
- **Test-command cwd (read carefully — `tests/` is overloaded).** Every per-task
  `pytest tests/test_*.py` command below is the **hook** suite — run it from
  `skills/disciplined-development/hooks/` (that package's `tests/`, e.g.
  `cd skills/disciplined-development/hooks && python3 -m pytest tests/test_severity.py -v`).
  The **repo-root** suites are different dirs: `python3 -m pytest tests/ -q`
  (installer, top-level `tests/`) and `python3 -m pytest research/ -q` (research).
  Hook suite green before each PR; installer/research suites green when those trees
  are touched.
- **Pre-PR gate is the only hard review block, fail-closed** (Decision 3): a BLOCK
  verdict, a missing/unparseable verdict, or any operational failure blocks
  `gh pr create`; the human overrides with `DD_SKIP_PR_REVIEW`.

## Contracts shared across chunks

**Verdict (D7).** The reviewer ends its output with a **last non-blank line that
contains only** `DD-VERDICT: PASS` or `DD-VERDICT: BLOCK` (nothing trailing — it must
match the parser's whole-line regex exactly, so producer wording everywhere says
"a final line containing only …"). The gate decision is read from that line,
never from counting `[P0]`–`[P3]` tokens. Last-non-blank-line anchoring (not "last
match anywhere") is load-bearing: once the skill documents the verdict line, a
reviewer that echoes the contract mid-output must not inject a stray example verdict.

**Findings.** Emitted as `- [PN] <file>:<line>: <summary>` lines; parsed best-effort
for the log only (never the gate decision).

**Reuse surface (build on these — do not reinvent).** `lib/state.py` (per-branch
counters, `review.checkpoint`, fork-base math — `set_checkpoint`/`reset`/`read`/
`commits_since_checkpoint`/`commits_since_fork_base`/`resolve_fork_base`),
`lib/logging_setup.py` (`append_review` — the single `reviews.jsonl` writer; it stamps
`ts` itself), `lib/severity.py` (parsing home), `lib/reviewer_runner.py` (timeout-
bounded subprocess), `lib/plan.py` (`resolve_active_plan`), `lib/config.py`. Confirm
each signature against the file when you call it.

---

# Chunk 1 — Build the log-review tool

**Branch:** `feat/dd-log-review`. **Builds** the model-callable log-review tool +
shared parsers/record builder. Adds only; removes nothing.

### Task 1.1 — `parse_findings` + `parse_verdict` (in `lib/severity.py`)

**Build:** two pure parsers beside the existing severity code (leave the existing
functions in place — the engine still uses them until Chunk 3).
- `parse_findings(text, line_start=True) -> list[dict]`, each `{"severity":
  "P0".."P3", "file": str|None, "line": int|None, "summary": str}`. Accepts the same
  finding-line shapes the existing scanner accepts (bullet/quote/markdown-emphasis
  tolerance) and rejects the rubric legend. **Accepted limitation:** the rubric-echo
  guard can drop a real finding whose summary starts with `critical|important|minor|
  nit /` — harmless because findings are best-effort log data, not the gate decision.
- `parse_verdict(text) -> "PASS"|"BLOCK"|None`, read from the **last non-blank line
  only** (`^\s*DD-VERDICT:\s*(PASS|BLOCK)\s*$`, case-insensitive); `None` otherwise.

- [x] Write failing tests (table-driven). `parse_findings`: well-formed → full dict;
  emphasised `**[P0]**` → P0; missing line → `line:None`; missing path → `file:None`;
  rubric legend line → excluded; `No findings.` → `[]`; mid-prose `[P1]` (line_start)
  → excluded. `parse_verdict`: trailing `DD-VERDICT: BLOCK` → BLOCK; lowercase →
  parsed; absent → None; an example verdict earlier + real one on the last non-blank
  line → real one; a non-verdict line after a verdict → None.
- [x] Run → fail. `python3 -m pytest tests/test_severity.py -v`
- [x] Implement; run → pass.
- [x] Commit. `feat(severity): structured parse_findings + parse_verdict`

### Task 1.2 — Record builder + cadence context (`lib/review_record.py`, new)

**Build** the single producer of a `reviews.jsonl` row (schema in the design doc):
- `gather_cadence_context(repo, branch) -> dict` → the cadence + lookup keys the row
  needs: `repo`, `head_sha`, `branch`, `base` (fork-base), `edits_count`,
  `commits_since_checkpoint`. **State + git reads only, no `git diff`.** Compute
  `base` via `resolve_fork_base` (read the trunk list from `config` the way the
  cadence hooks do — confirm the key name in `config`/a hook when you write it).
  `commits_since_checkpoint` mirrors the hooks' fallback (`commits_since_checkpoint`
  else `commits_since_fork_base`) so the logged number matches what the hooks act on.
- `build_review_record(*, findings, source, reviewer, trigger, round, context,
  decision=None, reason=None, duration_s=None, extra=None) -> dict` — pure assembly.
  `context` is the `gather_cadence_context` dict. `extra` is the declared home for the
  best-effort, source-specific fields the schema lists (`run_id`, `session_id`,
  `harness`, `model`, `model_version`, `effort`, `angles`, `skill_version`,
  `dd_version`, `cap_hit`, `cold_read_escape`, `bypass`); absent ones omitted. Do
  **not** emit `ts` (`append_review` stamps it). No `scope` field. `duration_s` is a
  float when present. Decision precedence: explicit `decision` → `parse_verdict` →
  derive `BLOCK` iff any P0/P1/P2 in `parse_findings` else `PASS`. The raw reviewer
  text (the `findings` arg) is stored verbatim as the schema's **`output`** field;
  `parse_findings(findings)` derives `findings[]` and the `p0`–`p3` counts.

- [x] Write failing tests (temp git repo for `gather_cadence_context`): clean +
  `DD-VERDICT: PASS` → `decision=PASS`, counts 0, `findings:[]`; `[P1]` +
  `DD-VERDICT: BLOCK` → `decision=BLOCK`; explicit `ERROR`/`reason` passed through;
  verdict absent but `[P1]` → derived BLOCK; builder output has **no `ts`** and **no
  `scope`**, carries `output` (raw reviewer text verbatim); `extra` fields surface;
  `gather_cadence_context` runs no `git diff` and
  falls back to fork-base count when no checkpoint.
- [x] Run → fail; implement; run → pass.
- [x] Commit. `feat(review-record): rich row builder + cadence context (no diff)`

### Task 1.3 — `log_review.py` CLI (record + reset-fold)

**Build** the model-callable tool at **`skills/disciplined-development/hooks/log_review.py`**
(inside the hook package so it can `from hooks.lib import ...` — not a top-level
script). `python3 log_review.py --source <model-review|external-gate> --trigger <t>
[--round <n>] [--reviewer <id>] [--cwd <path>]`, findings on **stdin**. Appends one row via `append_review`; on a
clean result resets `edits.count` **and** stamps `review.checkpoint = HEAD`
(Decision 2 — always both). Exit 0 on success; exit 2 on usage error (missing flag,
or empty/whitespace stdin — a blank pipe must not log a false PASS). Never blocks on
a log-write failure.

- [x] Write failing tests (temp git repo + `DD_LOG_DIR` log isolation — mirror an
  existing hook test that uses an on-disk state dir): clean stdin → exit 0, one
  `PASS` row, `edits.count` reset, `review.checkpoint` == HEAD; `[P1]` stdin →
  `BLOCK` row, counters untouched; empty stdin → exit 2, no row; row carries
  `source`/`trigger`/`round`/cadence context/structured findings.
- [x] Run → fail; implement; run → pass.
- [x] Commit. `feat(log-review): consolidated review log + cadence reset tool`

### Task 1.4 — `dd-log` command + generalize the installer

**Build:** a **thin** `commands/dd-log.md` (NOT a copy of any large existing template)
— YAML frontmatter with a `description` that says *when to invoke* without
summarising the workflow (per `writing-skills`), then a short body: pipe aggregated
findings to `log_review.py` after each round. Add the repo's own real
`.claude/commands/dd-log.md`. Generalize `install-skills.sh` to symlink **every**
`commands/*.md` (idempotent; skip a real file; skip a foreign symlink) instead of any
single hardcoded command.

**Reconcile (ground live):** find how the installer currently handles the command
symlink + its tests, and any migration special-case; replace the hardcoded/single-
command logic with the glob, updating/removing whatever tests and migration code that
makes obsolete. Grep the installer + `tests/` for the current command handling first.

- [x] Update installer tests first (seed an arbitrary `commands/<name>.md`; assert
  symlink + resolves + idempotent + real-file-not-clobbered); remove tests asserting
  the obsolete single-command/migration behavior. Run → fail.
- [x] Generalize `install-skills.sh`; write the command files. Run → pass.
- [x] Commit. `feat(commands,installer): add dd-log; symlink all commands/*.md`

### Chunk 1 close-out
- [x] Hook + installer suites green; self-review (`adversarial-review` + `-loop`),
  address P0/P1/P2; open PR.

---

# Chunk 2 — Build the pre-PR gate (whole-repo, verdict-driven, fail-closed)

**Branch:** `feat/dd-external-review-gate`. **Builds** the external-review tool and
rewires the gate hook onto it. The engine becomes unused here; it's removed in
Chunk 3.

### Task 2.1 — Gate command detection (`lib/command_match.py`)

**Build:** `looks_like_gh_pr_create(command) -> bool` — a loose detector (True when
`gh`…`pr`…`create` appear in order, even when strict parsing fails). Deliberately
over-broad: a false block is human-overridable; a false allow is a fail-open hole.
**Change** the existing `gh pr create` matcher to return just the review `cwd`
(`str|None`) — a whole-repo gate needs no diff base, so drop base extraction.

**Reconcile (ground live):** confirm the current matcher's callers + return shape and
its module docstring before changing the contract; update the docstring and the one
gate caller to the new shape; reconcile its tests.

- [x] Write failing tests: `looks_like` True on a real-but-hard-to-parse compound
  `gh pr create` (a command the strict tokenizer chokes on — e.g. an unmatched quote —
  paired with a `find_gh_pr_create` → None assert on the same command), True on a
  trivial one, False on a non-PR command, and a documented over-broad case (a command
  merely mentioning the tokens → True, accepted). The matcher returns bare `cwd|None`.
- [x] Run → fail; implement (incl. docstring); run → pass.
- [x] Commit. `feat(command-match): loose gh-pr-create detector; drop base extraction`

### Task 2.2 — `external_review.py` (whole-repo, verdict-driven)

**Build** the hook-callable gate executor at
**`skills/disciplined-development/hooks/external_review.py`** (inside the hook package,
for `hooks.lib` imports — not a top-level script). `python3 external_review.py
[--cwd <path>]`.
Builds a **deterministic whole-repo, plan-anchored prompt**: a **pointer** to the
review skill (`config review.prompt_path`, resolved against the repo under review — a
path codex reads itself, not the stuffed skill body) + the active-plan path
(`plan.resolve_active_plan()`) + "review the repository against this plan; emit
`- [PN] file:line: summary` findings; end with a final line containing only `DD-VERDICT: PASS` or
`DD-VERDICT: BLOCK`." Runs codex via `reviewer_runner` (timeout from config), reads
the verdict for the decision (findings parsed best-effort for the log), logs the
attempt as a `reviews.jsonl` row via the shared builder + `append_review` (incl.
`reviewer`/`model`/`effort` read from the `review.*` config block seeded in this
chunk — see the config-seed step), and on PASS stamps state (reuse the
log-review path / `state` directly). **Computes no diff, no base.** Exit 0 = clean
(allow); non-zero = block — BLOCK verdict, missing/unparseable verdict, codex missing/
timeout/error, or empty output all return non-zero and log a `PASS`/`BLOCK`/`ERROR`+
`reason` row. Always fail-closed; no `DD_HARD_BLOCK`.

- [x] **Resolve the codex invocation first** (`disciplined-research` — load-bearing
  for the whole gate). **Resolved:** `codex exec --cd <repo> -m <model> -c
  model_reasoning_effort=<effort> -s read-only -o <last-message-file> "<prompt>"` —
  whole-repo prompt mode works; the verdict is read from the `-o` last-message file
  (robust against any stdout footer). No `codex review` fallback needed. Argv pinned via
  a `DD_CODEX_BIN` recording-shim seam (mirrors `test_dd_review_runner.py`).
- [x] **Seed the gate's reviewer config (additive — removes the forward dependency).**
  Added `reviewer`/`model`/`effort` to the `review` block in `lib/dd-defaults.json` +
  `examples/dd-config.full.json` (values from `review_tiers.pre_pr`, `default_effort` →
  `effort`); `examples/dd-config.json` (minimal) carries `review.reviewer` only — kept
  minimal, model/effort resolve from defaults via deep-merge. `review_tiers.pre_pr` left
  in place (Chunk 3 trims it). Config test asserts the new defaults + the override merge.
- [x] Write failing tests (codex shim + temp repo + `DD_LOG_DIR`): clean+`PASS` →
  exit 0, `PASS` row, checkpoint==HEAD, edits reset; `[P1]`+`BLOCK` → non-zero,
  `BLOCK` row, no reset; no verdict line → non-zero, `ERROR reason=no_verdict`;
  shim missing → `ERROR cli_missing`; timeout → `ERROR timeout`; empty stdout →
  `ERROR empty_output`; the prompt contains the active-plan path + skill pointer.
- [x] Run → fail; implement; run → pass.
- [x] Commit. `feat(external-review): whole-repo verdict-driven fail-closed gate tool`

### Task 2.3 — Rewire the pre-PR gate hook

**Change** `pre_pr_review.py` to delegate to `external_review.py` (via an overridable
script-path seam for tests) instead of the engine. Add the fail-closed branch: a
command where the strict matcher returns no cwd **but** `looks_like_gh_pr_create` is
True → **append an ERROR `reason=unparseable` row to `reviews.jsonl`** via the shared
review-record builder + `append_review` (NOT `logger.emit`, which writes rolling hook
events, not review rows — the "every attempt logs a review row" contract, D4), then
block (exit 2). Remove the base-resolution path and the `DD_HARD_BLOCK`
mechanism (the gate tool is always fail-closed now).

**Reconcile (ground live):** read the current hook + its tests; the Claude Code rule
is "PreToolUse blocks only on exit 2", so keep the any-nonzero→exit-2 translation and
the stderr re-emit; reconcile the tests that assert the old delegate target / base /
`DD_HARD_BLOCK` forwarding.

- [x] Write failing tests: genuine non-PR command → allow (exit 0), no row;
  unparseable-but-PR-shaped → exit 2 + `ERROR unparseable`, stderr names
  `DD_SKIP_PR_REVIEW`; parseable + tool exit 0 → exit 0; parseable + tool non-zero →
  exit 2, reviewer output on stderr; `DD_SKIP_PR_REVIEW=1` → exit 0.
- [x] Run → fail; implement; run → pass.
- [x] Commit. `fix(pre-pr-gate): whole-repo verdict gate, fail-closed; drop base chain`
  (body cites the fail-open deferred bug as resolved).

### Chunk 2 close-out
- [x] Hook suite green (353 passed/3 skipped). **Live smoke (Gate 3):** scratch
  consumer, real `gh pr create` via the real hook → real `external_review.py` → codex
  shim — seeded-BLOCK → exit 2 + BLOCK row, no reset; seeded-PASS → exit 0 + PASS row +
  `review.checkpoint`==HEAD + edits cleared; `head_sha` matches the `--cwd` repo.
  Whole-branch cold-read (Opus): one [P2] fail-open (unguarded `main()` → exit-1) fixed
  + re-review clean; 4 [P3] (3 fixed, PASS-stamp-wrap dismissed). PR open, held for user.

---

# Chunk 3 — Remove the old machinery; reconcile; rewrite docs

**Branch:** `refactor/dd-remove-engine`. **Goal:** the engine, the command, and every
dead-after-this artifact no longer exist, and **nothing in the tree references them.**
No `SKILL.md` edits (Chunk 4).

**Reconcile discipline (the core of this chunk).** For each removal below, the
procedure is: **(1) grep the whole repo** (code, tests, `research/`, `examples/`,
docs, config, `install-skills.sh`) for the symbol/file/key; **(2) reconcile every hit
you find** — port real consumers, delete dead tests, update docs — in the same commit;
**(3) re-grep to confirm zero live references** before committing; **(4) record the
sweep** in `References swept:`. The lists below are **starting points, not closed
sets** — a hit you didn't expect is the normal case, not an error.

### Task 3.1 — Remove the engine + command
**Remove:** `dd_review_runner.py`, `commands/dd-review.md` (+ the repo's
`.claude/commands/dd-review.md`), and their tests. Start by grepping for
`dd_review_runner` and `/dd-review` repo-wide; confirm Chunks 1–2 gave every live
caller a new home before deleting.
- [x] Grep → reconcile → re-grep → run hook suite → commit.
  `refactor(review): delete dd_review_runner engine and /dd-review command`
  Symbol sweep split by design: `tests/`/`lib/`/core-docs reconciled here; the
  remaining `dd_review_runner` refs are owned by 3.2 (`review_invocation.py`), 3.3/3.4
  (`dd-config.md`, `hook-recipes-claude-code.md`), 3.5 (hook README), or are
  intentionally-stale archived/active plans — so a whole-tree re-grep is not zero
  until those tasks land.

### Task 3.2 — Remove now-dead lib code
**Remove (each only after its consumers are reconciled):** the strategy-selector
module; the diff-oriented prompt helpers `external_review` did not reuse; and the
count/excerpt severity scanners now that the gate uses `parse_verdict` and the log
uses `parse_findings`. **Known reconcile starting points** (verify + extend live):
the deleted engine; the `research/` replay harness (port any severity-count use to
`parse_findings`, **preserving its existing CSV `(p0,p1,p2,p3)` columns**); and the
`tests/` that target these modules (delete or rewrite per `lean-plan-writing` — rewrite
when ≥3 assertions reference removed symbols).
- [x] Grep each symbol repo-wide → reconcile every consumer → re-grep clean.
- [x] Run hook suite **and** `python3 -m pytest research/ -q`.
- [x] Commit. `refactor(lib): drop strategy-selector, diff-stuffing, count-as-decision`
  (whole `review_prompt.py` removed, not parts — `external_review` reused none of it.
  Remaining symbol hits live in `hook-recipes-claude-code.md` → 3.4 and archived plans.)

### Task 3.3 — Trim config
**Goal:** config no longer carries engine-only keys, but the **cadence-hook tunables
remain**. The gate's `reviewer`/`model`/`effort` already moved to `review.*` in
Chunk 2 (Task 2.2's config-seed), so here just **trim the now-unread
`review_tiers.pre_pr`** (confirm by grep that nothing still reads it), the
strategy-selector block, and codex strategy knobs. **Keep** the cadence-tier
thresholds the surviving hooks read (removing them silently drops thresholds to
in-code defaults — an invisible regression), plus `review.prompt_path`, the codex
timeout, and the `review.*` reviewer keys added in Chunk 2.
**Reconcile (ground live):** grep for `review_tiers.pre_pr`'s readers before removing
it — confirm zero remain (the gate now reads `review.*`, the cadence hooks read the
other tiers); apply the trim across **every** config file that carries the key
(defaults + all example configs — find them by grep, don't assume one); confirm
`cleanup.py` never prunes `reviews.jsonl`; update the config-schema doc; reconcile the
config test.
- [x] Grep readers → trim defaults + all example configs → update schema doc +
  config test → run config + hook suites → commit.
  `refactor(config): drop pre-pr tier + strategy_selector; keep cadence tiers`

### Task 3.4 — Sweep `/dd-review` references; repoint nudges
**Goal:** no doc, hook nudge, example, or config still tells a reader to use
`/dd-review`; the cadence hooks point at a deep review + `dd-log` instead.
**Reconcile (ground live):** grep every `/dd-review` and engine-mode reference plus
any dangling pointer to a non-existent plan; triage each (update / false-positive /
intentionally-stale). Known extra `dd_review_runner` symbol hits deferred from 3.1
to triage here: `MIGRATIONS.md` (historical engine-rename narrative — likely
intentionally-stale, decide live) and the doc refs in `hook-recipes-claude-code.md`
(`dd-config.md`'s strategy block is 3.3's). Repoint the cadence hooks' nudge **and** remediation/bypass
text to neutral wording ("run a deep review per the skill; log via `dd-log` to reset
the counter"); reconcile the tests asserting the old nudge strings; update
`CLAUDE.md`/examples/README to name `dd-log` and drop tier vocabulary.
- [x] Grep → repoint → reconcile tests → re-grep clean → run hook suite → commit
  with full `References swept:`. `refactor(hooks): repoint review nudges onto the skill + dd-log`

### Task 3.5 — Rewrite the hook README (heavy drift)
**Goal:** the hook `README.md` review section / state model / CLI-modes table
describe the new world: one deep whole-repo mode; two tools; reset-folds-into-logging;
verdict-driven fail-closed gate; the new log schema. Cold-read it in one pass, gather
every stale claim, rewrite (not surgical); apply `concise-writing`. (There is no
`dd-review` *skill* doc — don't go looking for one; the command is gone in 3.1.)
- [x] Rewrite → commit. `docs(hooks): rewrite review/state-model docs for the two-tool model`

### Chunk 3 close-out
- [x] Hook + installer + research suites green; self-review; open PR.
  Suites green (hook 243/3, installer 11, research 3). Self-review: per-task
  adversarial reviews + a whole-branch cold-read (3 P2s found + fixed → re-review
  clean). Clean review logged via `log_review.py` (PASS row; counters reset). PR
  #29 open. External review (Gate 5 step 2) is a manual codex run — this source
  repo omits the `pre_pr_review` gate (advisory hooks only), same as Chunk 2's
  PR #28 where the manual codex pass found 2 real findings.

---

# Chunk 4 — Skill edits (all together, last)

**Branch:** `feat/dd-skill-updates`. Every `SKILL.md` change for this overhaul, in one
pass, **draft → user review → apply** (Decision 6), after Chunks 1–3 land so the
skills describe machinery that exists.

### Task 4.1 — Draft + apply skill edits (via `superpowers:writing-skills`)
Edits drafted, user-reviewed (Decision 6), and applied in
`skills/disciplined-development/SKILL.md` + `skills/adversarial-review/SKILL.md`:
- `adversarial-review` Output format — the `DD-VERDICT: PASS|BLOCK` **last-line**
  contract (internal reviews declare a verdict too) + few-shot examples to match;
- `adversarial-review` Review-angles — the one mode (deep, whole-repo, plan-anchored;
  model picks angles per "when to apply");
- **parent de-diff-scoping** (scope expansion, user-approved 2026-06-22):
  `disciplined-development` Gate 5 steps 1–2, Gate 1, and the mode-emphasis "Code
  review (giving)" row drop diff-scoped review for whole-repo, plan-anchored.
  *Grounding:* the literal tier vocabulary `fast`/`regular`/`cold-read` was NOT in
  these skills (it lived in the Chunk-3-removed engine/command/config), so the change
  reduced to reframing the one depth-tier line + the parent's diff-scoped wording.
- **Conditional logging line — DEFERRED, not applied** (see Out of scope). RED showed
  the control passes (a `dd-log` command merely named in config → Claude subjects log
  every round incl. clean without a skill line), so it fails the writing-skills
  failing-test bar; per-round logging stays driven by `CLAUDE.md` + `dd-log`.
- [x] Draft + user review (Decision 6); apply verdict + one-mode + parent de-diff-scope.
- [x] RED/GREEN per `skill-validation/` (sonnet subjects; snapshot RED / live GREEN):
  scope RED 4/4 diff-scoped → GREEN 3/3 whole-repo; verdict GREEN findings 3/3 BLOCK /
  clean 2/2 PASS / loophole 1/1; angle-selection regression 2/2. Recorded in
  `skill-validation/disciplined-development.md` (new) + `adversarial-review.md`.
- [x] Adversarial cold-read (opus) — trimmed the verdict prose, removed an unbacked
  earlier-line guard the cold-read flagged as self-contradicting the few-shot examples
  (3 cycles → clean PASS); behavioral re-tests at parity.

### Task 4.2 — Records, verify, PR
- [x] Present drafts to the user; apply on approval (verdict + one-mode + parent
  de-diff-scope; conditional logging deferred).
- [x] Update `skill-validation/` records — new `disciplined-development.md`,
  `adversarial-review.md` extended (verdict contract + scope/angle regression).
- [x] Hook suite green (243 passed, 3 skipped); committed; opened PR #30.
  `docs(skills): one deep whole-repo review mode; declared DD-VERDICT line; de-diff-scope parent doctrine`

---

## Out of scope (tracked elsewhere)
- **Conditional review-logging line in the skill (Decision 5, skill-side).** Deferred
  2026-06-22: RED control passes in Claude (a config-named `dd-log` → subjects log
  rounds without a skill line), failing the writing-skills failing-test bar. The
  harness-side half (the `dd-log` command + `CLAUDE.md` instruction) remains and works.
  Revisit when porting to Codex, where the config→behavior link may not pre-fire.
- **Orphaned-safeguard review angle** (deferred #3-item-1) — separate skill effort.
- **Hook-internal `T0`–`T3` gate vocabulary.** The `/dd-review` review-mode tiers
  (fast/regular/cold-read/pre-pr) are gone, and the overview docs (READMEs, CLAUDE.md,
  examples) describe the cadence tier-free. But the hooks' code docstrings, the
  `dd-config.md` schema descriptions, the hook tests, and the `hook-recipes` gate
  labels still use `T0`–`T3` as internal shorthand for the four cadence gates. Left
  intact deliberately — relabeling them is part of the deferred hook-script
  simplification, not this overhaul. (See the cadence-counter-structure deferral.)
  **Exception (2026-06-22, external review):** the *consumer-facing* `cold-read`
  reset-condition wording in `dd-config.md` + `hook-recipes` was corrected to
  "clean review" — it taught the wrong reset model (any clean deep review stamps
  `review.checkpoint`, not a distinct cold-read). The `T0`–`T3` labels, the
  `cold_read_escalation` key, and the same shorthand in hook *code*
  docstrings/tests stay deferred.
- **Cadence-counter structure** — `plans/deferred/2026-06-21-cadence-counters-structure-deferred.md`.
- **Threshold calibration** — `plans/deferred/2026-06-14-threshold-rationale-and-calibration.md`.
- **Codex/other-harness port** — the old `2026-06-10-codex-harness-port.md` was
  deleted as out-of-date; author a fresh plan if/when pursued.

## Coverage check (design → chunk)
- D1 deep/whole-repo → 2.2 + 4.1. D2 reset-both → 1.3 + 2.2. D3 fail-closed → 2.1 +
  2.2 + 2.3. D4 rich durable log → 1.1/1.2 + 1.3/2.2 + 3.3 (protect reviews.jsonl).
  D5 logging placement → 3.4 (concrete `dd-log`); skill-side line deferred
  (Out of scope). D6 skill drafts
  user-gated → Chunk 4. D7 declared verdict → shared contract + 1.1 + 2.2 + 4.1.
- Engine/command removal + reconcile → Chunk 3. Fail-open bug → 2.1/2.3. Uniform
  logging → Chunk 1. Whole-repo cold-read → folded into the one mode (2.2 + 4.1).
