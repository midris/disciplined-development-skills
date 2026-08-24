# Task 1 report

## What I implemented

- Verified that `.worktrees/comprehensive-skill-cleanup` is on branch `docs/comprehensive-skill-cleanup`, at commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, clean, and matches `origin/docs/comprehensive-skill-cleanup`.
- Added `skill-validation/scenarios/README.md` as the active scenario inventory grouped by canonical owner catalog.
- Recorded every active scenario exactly once under its canonical owner and marked `WER-05` and `WER-08` as already ported via their existing runner configuration paths.
- Updated `plans/2026-08-24-scenario-inventory.md` with checked task boxes, inventory totals, and a completion note.

## Verification commands and results

```bash
git -C /Users/simon/work/personal/disciplined-development-skills/.worktrees/comprehensive-skill-cleanup \
  rev-parse HEAD origin/docs/comprehensive-skill-cleanup
```

Result:

```text
13599fb7d3127334b0d07bfe468767e586ec5f9c
13599fb7d3127334b0d07bfe468767e586ec5f9c
```

```bash
git -C /Users/simon/work/personal/disciplined-development-skills/.worktrees/comprehensive-skill-cleanup \
  branch --show-current
```

Result: `docs/comprehensive-skill-cleanup`

```bash
git -C /Users/simon/work/personal/disciplined-development-skills/.worktrees/comprehensive-skill-cleanup \
  status --short
```

Result: no output; the preserved source worktree is clean.

```bash
awk '/^## Totals/{exit} /^- `/{count++} END{print count}' \
  skill-validation/scenarios/README.md
```

Result: `105`

```bash
python3 - <<'PY'
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

def names(argv):
    return [Path(os.fsdecode(item)) for item in subprocess.check_output(argv).split(b"\0") if item]

working_docs = set(names(["git", "diff", "--name-only", "-z", "--diff-filter=ACMR", "HEAD", "--", "*.md"]))
working_docs.update(names(["git", "ls-files", "-z", "--others", "--exclude-standard", "--", "*.md"]))
staged_docs = set(names(["git", "diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR", "--", "*.md"]))
index_paths = {path.as_posix() for path in names(["git", "ls-tree", "-r", "--name-only", "-z", "HEAD"])}
index_paths.difference_update(path.as_posix() for path in names(["git", "diff", "--cached", "--no-renames", "--name-only", "-z", "--diff-filter=D"]))
index_paths.update(path.as_posix() for path in names(["git", "diff", "--cached", "--no-renames", "--name-only", "-z", "--diff-filter=ACMR"]))
patterns = (
    re.compile(r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))"),
    re.compile(r"^\s{0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|([^\s]+))", re.M),
)
missing = []

def check(source, text, exists, label):
    for pattern in patterns:
        for match in pattern.finditer(text):
            target = next(value for value in match.groups() if value is not None)
            if target.startswith(("#", "//")) or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = Path(target) if Path(target).is_absolute() else Path(os.path.normpath(source.parent / target))
            if not exists(resolved):
                missing.append(f"{label} {source}: {target} -> {resolved}")

def in_index(path):
    value = path.as_posix().rstrip("/")
    return value in index_paths or any(item.startswith(value + "/") for item in index_paths)

for source in sorted(working_docs):
    check(source, source.read_text(encoding="utf-8"), lambda path: path.exists(), "working")

for source in sorted(staged_docs):
    text = subprocess.check_output(["git", "show", f":{source.as_posix()}"]).decode("utf-8")
    check(source, text, in_index, "staged")

if missing:
    raise SystemExit("\n".join(missing))
print(f"Local Markdown links OK: {len(working_docs)} working, {len(staged_docs)} staged document(s).")
PY
```

Result: `Local Markdown links OK: 3 working, 3 staged document(s).`

```bash
git diff --check
```

Result: no output.

```bash
git diff --cached --check
```

Result: no output.

## Files changed

- `skill-validation/scenarios/README.md`
- `plans/2026-08-24-scenario-inventory.md`
- `.superpowers/sdd/2026-08-24-scenario-inventory/task-1-report.md`

## Self-review

- Reviewed the staged diff for the three task files and confirmed that the inventory stays within the brief's scope: scenario ID, canonical source section or fixture path, and `ported` / `not ported` only.
- Confirmed that shared scenarios appear once under their canonical owner and that the only ported entries are `WER-05` and `WER-08`.
- Converted canonical references in `skill-validation/scenarios/README.md` from external Markdown links to plain paths after the staged link checker rejected targets outside this worktree's index snapshot; the two required local runner configuration paths remain linked.

## Concerns

- Canonical source references in the inventory are plain text paths rather than Markdown links except for the two required local configuration links, because the staged Markdown-link checker only accepts in-index targets.
