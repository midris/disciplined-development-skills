#!/usr/bin/env bash
# install-skills.sh — symlink this clone's skills + command file into a project
#
# Usage: install-skills.sh <target-project-dir>
#
# For every skill dir under skills/ in this clone (a subdir containing
# a SKILL.md), creates a symlink <target>/.claude/skills/<name> ->
# <this-clone>/skills/<name>. Idempotent and safe: skips (with a warning) any
# name that already exists as a real path or a symlink pointing elsewhere —
# it never clobbers a project-local skill.
#
# Also symlinks every command template under commands/ in this clone:
#   <this-clone>/commands/<name>.md
#   -> <target>/.claude/commands/<name>.md
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

# --- Command file symlinks --------------------------------------------------
# Glob every commands/*.md and mirror the skill loop above: one symlink per
# command, idempotent, never clobbering a real file or a foreign symlink. A
# stale link from an earlier layout is just another foreign symlink (skip+warn).
CMD_DIR="$TARGET/.claude/commands"

for cmd_src in "$CLONE"/commands/*.md; do
  [ -e "$cmd_src" ] || continue          # no matches -> literal glob, skip
  src=$(cd "$(dirname "$cmd_src")" && pwd -P)/$(basename "$cmd_src")
  name=$(basename "$cmd_src")
  mkdir -p "$CMD_DIR"
  dest="$CMD_DIR/$name"

  if [ -L "$dest" ]; then
    resolved=$(readlink -f "$dest" 2>/dev/null || true)
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
    echo "WARN: $name already exists as a real file — skipping (won't clobber)" >&2
    skipped=$((skipped + 1))
    continue
  fi

  ln -s "$src" "$dest"
  echo "linked: $name -> $src"
  created=$((created + 1))
done

echo "done: $created created, $already already-linked, $skipped skipped"
