"""Strict configuration loading and ordinary-filesystem preflight."""

from __future__ import annotations

import json
import os
import re
import stat
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


_IDENTIFIER = re.compile(r"[a-z0-9][a-z0-9-]{0,63}\Z")
_EFFORT = re.compile(r"[a-z0-9][a-z0-9-]*\Z")
_ROOT_KEYS = {
    "schema_version",
    "id",
    "skill",
    "dependencies",
    "scenario",
    "expected_outcome",
    "execution",
}


class ConfigError(ValueError):
    """Raised when a configuration cannot pass structural preflight."""


@dataclass(frozen=True, slots=True)
class SkillDeclaration:
    id: str
    source: Path
    skill_md: Path
    include: tuple[Path, ...]


@dataclass(frozen=True, slots=True)
class ScenarioDeclaration:
    id: str
    prompt: Path
    fixture: Path | None


@dataclass(frozen=True, slots=True)
class ExecutionDeclaration:
    provider: str
    model: str
    effort: str


@dataclass(frozen=True, slots=True)
class TestConfig:
    schema_version: str
    id: str
    skill: SkillDeclaration
    dependencies: tuple[SkillDeclaration, ...]
    scenario: ScenarioDeclaration
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
    if schema_version != "0.1":
        raise ConfigError('schema_version must be "0.1"')
    test_id = _identifier(value["id"], "id")
    skill = _skill(value["skill"], config_path.parent, "skill")
    dependencies_value = value["dependencies"]
    if not isinstance(dependencies_value, list):
        raise ConfigError("dependencies must be a list")
    dependencies = tuple(
        _skill(item, config_path.parent, f"dependencies[{index}]")
        for index, item in enumerate(dependencies_value)
    )
    _unique_skill_ids(skill, dependencies)
    scenario = _scenario(value["scenario"], config_path.parent)
    execution = _execution(value["execution"])

    _preflight(config_path, skill, dependencies, scenario)
    return TestConfig(
        schema_version=schema_version,
        id=test_id,
        skill=skill,
        dependencies=dependencies,
        scenario=scenario,
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


def _skill(value: Any, base: Path, name: str) -> SkillDeclaration:
    _exact_keys(value, {"id", "source", "include"}, name)
    skill_id = _identifier(value["id"], f"{name}.id")
    source = _directory(_path(value["source"], base, f"{name}.source"), f"{name}.source").resolve()
    include = _included_files(value["include"], source, f"{name}.include")
    skill_md = _regular_file(source / "SKILL.md", f"{name}.source/SKILL.md").resolve()
    _read_utf8(skill_md, f"{name}.source/SKILL.md")
    return SkillDeclaration(skill_id, source, skill_md, include)


def _included_files(value: Any, source: Path, name: str) -> tuple[Path, ...]:
    if not isinstance(value, list) or not value:
        raise ConfigError(f"{name} must be a non-empty list")

    included: list[Path] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item:
            raise ConfigError(f"{name}[{index}] must be a non-empty path string")
        relative = Path(item)
        if relative.is_absolute() or any(part in {".", ".."} for part in item.split("/")):
            raise ConfigError(f"{name}[{index}] must be a relative file path without dot components")
        target = source / relative
        if not _contains(source, target.resolve()):
            raise ConfigError(f"{name}[{index}] must resolve inside the skill source")
        _regular_file(target, f"{name}[{index}]")
        included.append(relative)

    if len(set(included)) != len(included):
        raise ConfigError(f"{name} paths must be unique")
    if Path("SKILL.md") not in included:
        raise ConfigError(f"{name} must include SKILL.md")
    return tuple(included)


def _scenario(value: Any, base: Path) -> ScenarioDeclaration:
    _exact_keys(value, {"id", "prompt", "fixture"}, "scenario")
    scenario_id = _identifier(value["id"], "scenario.id")
    prompt = _regular_file(_path(value["prompt"], base, "scenario.prompt"), "scenario.prompt").resolve()
    _read_utf8(prompt, "scenario.prompt")
    fixture_value = value["fixture"]
    if fixture_value is None:
        fixture = None
    else:
        fixture = _directory(_path(fixture_value, base, "scenario.fixture"), "scenario.fixture").resolve()
    return ScenarioDeclaration(scenario_id, prompt, fixture)


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


def _preflight(
    config_path: Path,
    skill: SkillDeclaration,
    dependencies: tuple[SkillDeclaration, ...],
    scenario: ScenarioDeclaration,
) -> None:
    sources = (skill, *dependencies)
    if scenario.prompt == config_path:
        raise ConfigError("configuration cannot be the scenario prompt")
    for declaration in sources:
        if _overlap(declaration.source, config_path):
            raise ConfigError("skill source contains configuration")
    if scenario.fixture is not None:
        if _overlap(scenario.fixture, config_path):
            raise ConfigError("fixture contains configuration")
        if os.path.lexists(scenario.fixture / "supplied-skills"):
            raise ConfigError("fixture contains supplied-skills")
        _check_tree(scenario.fixture, config_path)
    run_root = (Path(tempfile.gettempdir()) / "skilltest-runs").resolve()
    roots = [config_path.parent, *(item.source for item in sources)]
    if scenario.fixture is not None:
        roots.append(scenario.fixture)
    if any(_overlap(run_root, root) for root in roots):
        raise ConfigError("fixed run root overlaps declared input")


def _check_tree(root: Path, config_path: Path) -> None:
    def fail(error: OSError) -> None:
        raise ConfigError(f"cannot inspect {root}: {error}") from error

    for directory, directories, files in os.walk(root, followlinks=False, onerror=fail):
        for name in [*directories, *files]:
            entry = Path(directory, name)
            try:
                mode = entry.lstat().st_mode
            except OSError as error:
                raise ConfigError(f"cannot inspect {entry}: {error}") from error
            if not stat.S_ISREG(mode) and not stat.S_ISDIR(mode):
                raise ConfigError(f"special file in declared input: {entry}")


def _regular_file(path: Path, name: str) -> Path:
    try:
        if not stat.S_ISREG(path.lstat().st_mode):
            raise ConfigError(f"{name} must be a regular file")
    except (OSError, ValueError) as error:
        raise ConfigError(f"cannot inspect {name}: {error}") from error
    return path


def _directory(path: Path, name: str) -> Path:
    try:
        if not stat.S_ISDIR(path.lstat().st_mode):
            raise ConfigError(f"{name} must be a directory")
    except (OSError, ValueError) as error:
        raise ConfigError(f"cannot inspect {name}: {error}") from error
    return path


def _read_utf8(path: Path, name: str) -> tuple[bytes, str]:
    try:
        contents = path.read_bytes()
        return contents, contents.decode("utf-8")
    except (OSError, UnicodeDecodeError, MemoryError) as error:
        raise ConfigError(f"{name} must be readable UTF-8: {error}") from error


def _path(value: Any, base: Path, name: str) -> Path:
    if not isinstance(value, str):
        raise ConfigError(f"{name} must be a path string")
    try:
        return base / value
    except (OSError, RuntimeError, ValueError) as error:
        raise ConfigError(f"cannot construct {name}: {error}") from error


def _identifier(value: Any, name: str) -> str:
    if not isinstance(value, str) or not _IDENTIFIER.fullmatch(value):
        raise ConfigError(f"{name} is not a valid identifier")
    return value


def _exact_keys(value: Any, keys: set[str], name: str) -> None:
    if not isinstance(value, dict) or set(value) != keys:
        raise ConfigError(f"{name} has invalid keys")


def _unique_skill_ids(skill: SkillDeclaration, dependencies: tuple[SkillDeclaration, ...]) -> None:
    if len({item.id for item in (skill, *dependencies)}) != len(dependencies) + 1:
        raise ConfigError("skill identifiers must be unique")


def _contains(directory: Path, path: Path) -> bool:
    try:
        path.relative_to(directory)
    except ValueError:
        return False
    return True


def _overlap(first: Path, second: Path) -> bool:
    return _contains(first, second) or _contains(second, first)
