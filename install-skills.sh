#!/usr/bin/env bash
# install-skills.sh — symlink this clone's skills + command file into a project
#
# Usage: install-skills.sh <target-project-dir>
#
# For every skill dir under skills/ in this clone (a subdir of skills/ containing
# a SKILL.md), creates a symlink <target>/.claude/skills/<name> ->
# <this-clone>/skills/<name>. Idempotent and safe: skips (with a warning) any
# name that already exists as a real path or a symlink pointing elsewhere —
# it never clobbers a project-local skill.
#
# Also symlinks the /dd-review command template:
#   <this-clone>/examples/commands/dd-review.md
#   -> <target>/.claude/commands/dd-review.md
# Same guards apply: idempotent; skips with a warning if the dest is a real file
# or a symlink pointing elsewhere (never clobbers).
#
# It does NOT edit the consumer's tracked files (settings.json, dd-config.json).
# Gitignore the resulting symlinks and wire the hooks manually (see the README).
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: $0 <target-project-dir>" >&2
  exit 2
fi

TARGET=$1
if [ ! -d "$TARGET" ]; then
  echo "error: target project dir does not exist: $TARGET" >&2
  exit 2
fi

CLONE=$(cd "$(dirname "$0")" && pwd -P)
TARGET=$(cd "$TARGET" && pwd -P)
SKILLS="$TARGET/.claude/skills"
mkdir -p "$SKILLS"

created=0
already=0
skipped=0

for skill_md in "$CLONE"/skills/*/SKILL.md; do
  [ -e "$skill_md" ] || continue          # no matches -> literal glob, skip
  src=$(cd "$(dirname "$skill_md")" && pwd -P)
  name=$(basename "$src")
  dest="$SKILLS/$name"

  if [ -L "$dest" ]; then
    resolved=$(cd "$dest" 2>/dev/null && pwd -P || true)
    if [ "$resolved" = "$src" ]; then
      echo "already linked: $name"
      already=$((already + 1))
    else
      echo "WARN: $name is a symlink to a different target ($(readlink "$dest")) — skipping" >&2
      skipped=$((skipped + 1))
    fi
    continue
  fi

  if [ -e "$dest" ]; then
    echo "WARN: $name already exists as a real path — skipping (won't clobber)" >&2
    skipped=$((skipped + 1))
    continue
  fi

  ln -s "$src" "$dest"
  echo "linked: $name -> $src"
  created=$((created + 1))
done

# --- Command file symlink ---------------------------------------------------
CMD_SRC="$CLONE/examples/commands/dd-review.md"
CMD_DIR="$TARGET/.claude/commands"
CMD_DEST="$CMD_DIR/dd-review.md"
mkdir -p "$CMD_DIR"

if [ -L "$CMD_DEST" ]; then
  resolved=$(readlink -f "$CMD_DEST" 2>/dev/null || true)
  if [ "$resolved" = "$CMD_SRC" ]; then
    echo "already linked: dd-review.md"
    already=$((already + 1))
  else
    echo "WARN: dd-review.md is a symlink to a different target ($(readlink "$CMD_DEST")) — skipping" >&2
    skipped=$((skipped + 1))
  fi
elif [ -e "$CMD_DEST" ]; then
  echo "WARN: dd-review.md already exists as a real file — skipping (won't clobber)" >&2
  skipped=$((skipped + 1))
else
  ln -s "$CMD_SRC" "$CMD_DEST"
  echo "linked: dd-review.md -> $CMD_SRC"
  created=$((created + 1))
fi

echo "done: $created created, $already already-linked, $skipped skipped"
