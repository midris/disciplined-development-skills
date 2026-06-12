"""Slim config loader for disciplined-development hooks.

Exposes ``get(dot_path)`` over ``dd-defaults.json`` (shipped beside this
module) deep-merged with an optional user override at
``.claude/dd-config.json`` — resolved under ``$CLAUDE_PROJECT_DIR`` (the
harness-set project root), else the current directory. User config wins on
overlapping keys; a malformed
or non-dict user config is discarded silently so defaults stand.

``DD_DEFAULTS`` / ``DD_CONFIG`` env vars override the respective file
locations (used by tests). Results are cached; call ``reset_config_cache()``
when the underlying files or env vars change.
"""
from __future__ import annotations

import functools
import json
import os
from pathlib import Path
from typing import Any

_DEFAULTS_FILENAME = "dd-defaults.json"
_USER_CONFIG_RELPATH = ".claude/dd-config.json"


def _defaults_path() -> Path:
    override = os.environ.get("DD_DEFAULTS")
    if override:
        return Path(override)
    return Path(__file__).resolve().parent / _DEFAULTS_FILENAME


def _user_config_path() -> Path:
    override = os.environ.get("DD_CONFIG")
    if override:
        return Path(override)
    # Hooks fire with the session shell's cwd, which need not be the project
    # root — resolve against CLAUDE_PROJECT_DIR (set by the harness) so consumer
    # overrides don't silently vanish off-root; fall back to cwd when unset.
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR")
    base = Path(project_dir) if project_dir else Path.cwd()
    return base / _USER_CONFIG_RELPATH


def _load_json_dict(path: Path) -> dict[str, Any]:
    """Load a JSON object from *path*; return {} on any failure or non-dict."""
    try:
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


@functools.lru_cache(maxsize=1)
def _load_defaults() -> dict[str, Any]:
    return _load_json_dict(_defaults_path())


@functools.lru_cache(maxsize=1)
def _load_user_config() -> dict[str, Any]:
    return _load_json_dict(_user_config_path())


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge *override* onto *base*; override wins on conflicts."""
    result = dict(base)
    for key, value in override.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


@functools.lru_cache(maxsize=1)
def _merged_config() -> dict[str, Any]:
    return _deep_merge(_load_defaults(), _load_user_config())


def get(dot_path: str, default: Any = None) -> Any:
    """Return the value at *dot_path* in the merged config, else *default*."""
    node: Any = _merged_config()
    for part in dot_path.split("."):
        if isinstance(node, dict) and part in node:
            node = node[part]
        else:
            return default
    return node


def reset_config_cache() -> None:
    """Clear cached defaults, user config, and merged result."""
    _load_defaults.cache_clear()
    _load_user_config.cache_clear()
    _merged_config.cache_clear()
