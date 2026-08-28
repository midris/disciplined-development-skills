"""Strict configuration loading for prompt-runner schema 0.2."""

from __future__ import annotations

import json
import ntpath
import re
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Any


_IDENTIFIER = re.compile(r"[a-z0-9][a-z0-9-]{0,63}\Z")
_EFFORT = re.compile(r"[a-z0-9][a-z0-9-]*\Z")
_ROOT_KEYS = {"schema_version", "id", "prompt", "fixtures", "execution"}
_FIXTURE_KEYS = {"source", "target"}


class ConfigError(ValueError):
    """Raised when a configuration cannot pass structural preflight."""


@dataclass(frozen=True, slots=True)
class FixtureDeclaration:
    source: Path
    target: Path


@dataclass(frozen=True, slots=True)
class ExecutionDeclaration:
    provider: str
    model: str
    effort: str


@dataclass(frozen=True, slots=True)
class TestConfig:
    schema_version: str
    id: str
    prompt: Path
    fixtures: tuple[FixtureDeclaration, ...]
    execution: ExecutionDeclaration
    config_path: Path
    config_bytes: bytes


def load_config(path: Path) -> TestConfig:
    """Load one configuration without allocating a run or starting a process."""
    config_path = _regular_file(path, "configuration").resolve()
    config_bytes = _read_utf8(config_path, "configuration")[0]
    value = _parse_config(config_bytes, config_path)
    _exact_keys(value, _ROOT_KEYS, "configuration")

    schema_version = value["schema_version"]
    if schema_version != "0.2":
        raise ConfigError('schema_version must be "0.2"')
    test_id = _identifier(value["id"], "id")
    prompt = _declared_file(value["prompt"], config_path.parent, "prompt")
    _read_utf8(prompt, "prompt")
    fixtures = _fixtures(value["fixtures"], config_path.parent)
    execution = _execution(value["execution"])
    return TestConfig(
        schema_version=schema_version,
        id=test_id,
        prompt=prompt,
        fixtures=fixtures,
        execution=execution,
        config_path=config_path,
        config_bytes=config_bytes,
    )


def _parse_config(config_bytes: bytes, config_path: Path) -> dict[str, Any]:
    try:
        value = json.loads(
            config_bytes.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
        )
    except (
        UnicodeDecodeError,
        json.JSONDecodeError,
        ConfigError,
        MemoryError,
        RecursionError,
        ValueError,
    ) as error:
        raise ConfigError(f"invalid JSON configuration {config_path}: {error}") from error
    if not isinstance(value, dict):
        raise ConfigError("configuration must be an object")
    return value


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ConfigError(f"duplicate key: {key}")
        value[key] = item
    return value


def _reject_nonfinite(value: str) -> None:
    raise ConfigError(f"non-finite JSON number: {value}")


def _fixtures(value: Any, base: Path) -> tuple[FixtureDeclaration, ...]:
    if not isinstance(value, list):
        raise ConfigError("fixtures must be a list")
    fixtures = tuple(
        _fixture(item, base, f"fixtures[{index}]") for index, item in enumerate(value)
    )
    _reject_target_conflicts(fixtures)
    return fixtures


def _fixture(value: Any, base: Path, name: str) -> FixtureDeclaration:
    _exact_keys(value, _FIXTURE_KEYS, name)
    source = _declared_file(value["source"], base, f"{name}.source")
    return FixtureDeclaration(source=source, target=_target(value["target"], f"{name}.target"))


def _declared_file(value: Any, base: Path, name: str) -> Path:
    if not isinstance(value, str):
        raise ConfigError(f"{name} must be a path string")
    try:
        relative = Path(value)
    except (OSError, RuntimeError, ValueError) as error:
        raise ConfigError(f"cannot construct {name}: {error}") from error
    if relative.is_absolute():
        raise ConfigError(f"{name} must be a relative path")
    return _regular_file(base / relative, name).resolve()


def _target(value: Any, name: str) -> Path:
    if not isinstance(value, str):
        raise ConfigError(f"{name} must be a path string")
    parts = value.split("/")
    if (
        ntpath.splitdrive(value)[0]
        or "\\" in value
        or not value
        or any(part in {"", ".", ".."} for part in parts)
    ):
        raise ConfigError(f"{name} must be a canonical relative path")
    return Path(*parts)


def _reject_target_conflicts(fixtures: tuple[FixtureDeclaration, ...]) -> None:
    targets: list[tuple[str, ...]] = []
    for fixture in fixtures:
        target = fixture.target.parts
        if any(target[: len(existing)] == existing or existing[: len(target)] == target for existing in targets):
            raise ConfigError("fixture targets conflict")
        targets.append(target)


def _execution(value: Any) -> ExecutionDeclaration:
    _exact_keys(value, {"provider", "model", "effort"}, "execution")
    provider = value["provider"]
    model = value["model"]
    effort = value["effort"]
    if not isinstance(provider, str) or provider not in {"codex", "claude"}:
        raise ConfigError("execution.provider must be codex or claude")
    if not isinstance(model, str) or not model:
        raise ConfigError("execution.model must be a non-empty string")
    if not isinstance(effort, str) or not _EFFORT.fullmatch(effort):
        raise ConfigError("execution.effort is invalid")
    return ExecutionDeclaration(provider, model, effort)


def _regular_file(path: Path, name: str) -> Path:
    try:
        if not stat.S_ISREG(path.lstat().st_mode):
            raise ConfigError(f"{name} must be a regular file")
    except (OSError, ValueError) as error:
        raise ConfigError(f"cannot inspect {name}: {error}") from error
    return path


def _read_utf8(path: Path, name: str) -> tuple[bytes, str]:
    try:
        contents = path.read_bytes()
        return contents, contents.decode("utf-8")
    except (OSError, UnicodeDecodeError, MemoryError) as error:
        raise ConfigError(f"{name} must be readable UTF-8: {error}") from error


def _identifier(value: Any, name: str) -> str:
    if not isinstance(value, str) or not _IDENTIFIER.fullmatch(value):
        raise ConfigError(f"{name} is not a valid identifier")
    return value


def _exact_keys(value: Any, keys: set[str], name: str) -> None:
    if not isinstance(value, dict) or set(value) != keys:
        raise ConfigError(f"{name} has invalid keys")
