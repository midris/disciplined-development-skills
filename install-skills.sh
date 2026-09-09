#!/usr/bin/env bash
# Replace this bundle's skill directories with copies; leave other names alone.
# Usage: install-skills.sh <target-project-dir> [.claude|.agents]
set -euo pipefail

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "usage: $0 <target-project-dir> [.claude|.agents]" >&2
  exit 2
fi

INSTALL_DIR=${2:-.claude}
case "$INSTALL_DIR" in
  .claude|.agents) ;;
  *) echo "error: destination must be .claude or .agents" >&2; exit 2 ;;
esac
if [ ! -d "$1" ]; then
  echo "error: target project dir does not exist: $1" >&2
  exit 2
fi

CLONE=$(cd "$(dirname "$0")" && pwd -P)
TARGET=$(cd "$1" && pwd -P)
BASE="$TARGET/$INSTALL_DIR"

# Never traverse a shared parent link while deleting same-name destinations.
parents=("$BASE" "$BASE/skills")
if [ "$INSTALL_DIR" = .claude ]; then
  parents+=("$BASE/commands")
fi
for parent in "${parents[@]}"; do
  if [ -L "$parent" ] || { [ -e "$parent" ] && [ ! -d "$parent" ]; }; then
    echo "error: installation parent must be a real directory: $parent" >&2
    exit 1
  fi
done
mkdir -p "$BASE/skills"

for skill_md in "$CLONE"/skills/*/SKILL.md; do
  [ -f "$skill_md" ] || continue
  src=$(dirname "$skill_md")
  dest="$BASE/skills/$(basename "$src")"
  # No trailing slash: rm removes an existing link, never its target.
  rm -rf "$dest"
  cp -RPp "$src" "$dest"
  echo "copied: $dest"
done

# Slash-command templates use Claude-specific paths and variables.
if [ "$INSTALL_DIR" = .claude ]; then
  for src in "$CLONE"/commands/*.md; do
    [ -f "$src" ] || continue
    mkdir -p "$BASE/commands"
    dest="$BASE/commands/$(basename "$src")"
    rm -rf "$dest"
    cp -p "$src" "$dest"
    echo "copied: $dest"
  done
fi
