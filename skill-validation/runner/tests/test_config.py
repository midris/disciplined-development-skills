import json
import os
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from skilltest.config import ConfigError, load_config


def _write(path: Path, content: str | bytes = "") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content if isinstance(content, bytes) else content.encode())
    return path


def _valid_config(tmp_path: Path) -> tuple[Path, dict[str, object]]:
    _write(tmp_path / "primary" / "SKILL.md", "primary")
    _write(tmp_path / "dependency" / "SKILL.md", "dependency")
    _write(tmp_path / "prompt.txt", "do the scenario")
    (tmp_path / "fixture").mkdir()
    return tmp_path / "case.json", {
        "schema_version": "0.1",
        "id": "valid-case",
        "skill": {"id": "primary", "source": "primary", "include": ["SKILL.md"]},
        "dependencies": [
            {"id": "dependency", "source": "dependency", "include": ["SKILL.md"]}
        ],
        "scenario": {"id": "case", "prompt": "prompt.txt", "fixture": "fixture"},
        "expected_outcome": {"opaque": True},
        "execution": {"provider": "codex", "model": "gpt-5.4", "effort": "medium"},
    }


def _save(path: Path, value: object) -> bytes:
    raw = json.dumps(value, separators=(",", ":")).encode()
    path.write_bytes(raw)
    return raw


def _reject(path: Path, value: object) -> None:
    _save(path, value)
    with pytest.raises(ConfigError):
        load_config(path)


def test_load_config_accepts_required_file_includes(tmp_path: Path) -> None:
    config_path, config = _valid_config(tmp_path)
    _write(tmp_path / "primary" / "scripts" / "tool.py", "pass")
    config["schema_version"] = "0.1"
    config["skill"] = {
        "id": "primary",
        "source": "primary",
        "include": ["SKILL.md", "scripts/tool.py"],
    }
    config["dependencies"] = [
        {"id": "dependency", "source": "dependency", "include": ["SKILL.md"]}
    ]
    _save(config_path, config)

    loaded = load_config(config_path)

    assert loaded.schema_version == "0.1"
    assert loaded.skill.include == (Path("SKILL.md"), Path("scripts/tool.py"))
    assert loaded.dependencies[0].include == (Path("SKILL.md"),)


# Catches a loader mutation that continues to require skill declarations for tagged fixture-only runs.
def test_load_config_accepts_explicit_no_skill_context(tmp_path: Path) -> None:
    _write(tmp_path / "prompt.txt", b"use the supplied descriptions")
    (tmp_path / "fixture").mkdir()
    config_path = tmp_path / "case.json"
    raw = _save(
        config_path,
        {
            "schema_version": "0.1",
            "id": "fixture-only",
            "skill_context": "none",
            "scenario": {
                "id": "fixture-only-scenario",
                "prompt": "prompt.txt",
                "fixture": "fixture",
            },
            "expected_outcome": {"opaque": True},
            "execution": {"provider": "codex", "model": "gpt-5.4", "effort": "medium"},
        },
    )

    loaded = load_config(config_path)

    assert loaded.config_bytes == raw
    assert loaded.skill is None
    assert loaded.dependencies == ()
    assert loaded.scenario.fixture == (tmp_path / "fixture").resolve()


# Catches a loader mutation that accepts ambiguous, untagged, unsupported, or mixed skill-context roots.
def test_load_config_rejects_ambiguous_skill_context_shapes(tmp_path: Path) -> None:
    config_path, normal = _valid_config(tmp_path)
    no_skill_context = {
        "schema_version": "0.1",
        "id": "fixture-only",
        "skill_context": "none",
        "scenario": {"id": "case", "prompt": "prompt.txt", "fixture": "fixture"},
        "expected_outcome": {"opaque": True},
        "execution": {"provider": "codex", "model": "gpt-5.4", "effort": "medium"},
    }
    null_skill = dict(normal)
    null_skill["skill"] = None
    untagged_missing = dict(normal)
    untagged_missing.pop("skill")
    untagged_missing.pop("dependencies")
    unsupported_tag = dict(no_skill_context)
    unsupported_tag["skill_context"] = "primary"
    mixed_shapes = dict(no_skill_context)
    mixed_shapes["skill"] = normal["skill"]
    mixed_shapes["dependencies"] = normal["dependencies"]

    for value in (null_skill, untagged_missing, unsupported_tag, mixed_shapes):
        _reject(config_path, value)


# Catches a loader mutation that retains or transforms the opaque expected outcome.
def test_load_config_accepts_exact_execution_declarations(tmp_path: Path) -> None:
    for provider, model, effort in [("codex", "gpt-5.4", "medium"), ("claude", "sonnet", "high")]:
        case_root = tmp_path / provider
        config_path, config = _valid_config(case_root)
        config["execution"] = {"provider": provider, "model": model, "effort": effort}
        config["expected_outcome"] = {"nested": {"items": ["value"]}}
        raw = _save(config_path, config)

        loaded = load_config(config_path)

        assert loaded.config_bytes == raw
        assert loaded.config_path == config_path.resolve()
        assert loaded.execution.provider == provider
        assert loaded.execution.model == model
        assert loaded.execution.effort == effort
        assert loaded.skill.source == (case_root / "primary").resolve()
        assert loaded.scenario.prompt == (case_root / "prompt.txt").resolve()
        assert loaded.scenario.fixture == (case_root / "fixture").resolve()
        with pytest.raises(FrozenInstanceError):
            loaded.id = "other"  # type: ignore[misc]
        with pytest.raises(FrozenInstanceError):
            loaded.skill.id = "other"  # type: ignore[misc]
        with pytest.raises(FrozenInstanceError):
            loaded.scenario.id = "other"  # type: ignore[misc]
        with pytest.raises(FrozenInstanceError):
            loaded.execution.model = "other"  # type: ignore[misc]
        assert not hasattr(loaded, "expected_outcome")


# Catches a loader mutation that judges independent roots or opaque valid values.
def test_load_config_accepts_independent_and_semantically_odd_inputs(tmp_path: Path) -> None:
    expected_outcomes = [None, "opaque", ["array"], 7, False]
    for index, expected_outcome in enumerate(expected_outcomes):
        case_root = tmp_path / str(index)
        config_path, config = _valid_config(case_root)
        config["dependencies"] = []
        config["scenario"]["fixture"] = None
        config["expected_outcome"] = expected_outcome
        _write(case_root / "prompt.txt", b"")
        config["execution"] = {
            "provider": "codex",
            "model": "not-a-model",
            "effort": "low-even-if-odd",
        }
        _save(config_path, config)

        loaded = load_config(config_path)

        assert loaded.dependencies == ()
        assert loaded.scenario.fixture is None
        assert loaded.scenario.prompt.read_bytes() == b""
        assert not hasattr(loaded, "expected_outcome")
        assert loaded.execution.model == "not-a-model"

    external_source = tmp_path / "independent-skill"
    _write(external_source / "SKILL.md", "independent")
    config_path, config = _valid_config(tmp_path / "independent")
    config["dependencies"] = [
        {"id": "outside", "source": str(external_source), "include": ["SKILL.md"]}
    ]
    _save(config_path, config)
    assert load_config(config_path).dependencies[0].source == external_source.resolve()


# Catches a parser mutation that accepts invalid JSON or leaks capacity failure.
def test_load_config_rejects_invalid_json_and_normalizes_capacity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    for index, raw in enumerate(
        [
            b"[1]",
            b'{"schema_version":1,"schema_version":1}',
            b'{"schema_version":NaN}',
            b'{"schema_version":Infinity}',
            b'{"schema_version":-Infinity}',
            b'{"skill":{"id":"a","id":"b"}}',
            b"not-json",
        ]
    ):
        config_path = tmp_path / str(index) / "case.json"
        config_path.parent.mkdir()
        config_path.write_bytes(raw)
        with pytest.raises(ConfigError):
            load_config(config_path)

    config_path, config = _valid_config(tmp_path / "capacity")
    _save(config_path, config)
    original_read_bytes = Path.read_bytes

    def out_of_capacity(path: Path) -> bytes:
        if path == config_path:
            raise MemoryError("capacity exhausted")
        return original_read_bytes(path)

    monkeypatch.setattr(Path, "read_bytes", out_of_capacity)
    with pytest.raises(ConfigError, match="capacity exhausted"):
        load_config(config_path)
    monkeypatch.setattr(Path, "read_bytes", original_read_bytes)

    config_path, config = _valid_config(tmp_path / "large-number")
    config.pop("expected_outcome")
    config_path.write_text(
        json.dumps(config, separators=(",", ":"))[:-1]
        + ',"expected_outcome":'
        + "9" * 5000
        + "}",
        encoding="utf-8",
    )
    with pytest.raises(ConfigError, match="Exceeds the limit"):
        load_config(config_path)


# Catches schema-validation mutations that accept missing or unknown fields.
def test_load_config_rejects_invalid_structure(tmp_path: Path) -> None:
    mutations = [
        lambda value: value.pop("expected_outcome"),
        lambda value: value.__setitem__("extra", True),
        lambda value: value["skill"].__setitem__("extra", True),
        lambda value: value["skill"].pop("include"),
        lambda value: value["scenario"].__setitem__("extra", True),
        lambda value: value["execution"].__setitem__("extra", True),
        lambda value: value.__setitem__("dependencies", {}),
    ]
    for index, mutate in enumerate(mutations):
        config_path, config = _valid_config(tmp_path / str(index))
        mutate(config)
        _reject(config_path, config)


# Catches identifier and execution mutations that broaden the public declaration.
def test_load_config_rejects_invalid_identifiers_and_execution(tmp_path: Path) -> None:
    mutations = [
        lambda value: value.__setitem__("id", "Uppercase"),
        lambda value: value["skill"].__setitem__("id", "has_space"),
        lambda value: value["scenario"].__setitem__("id", "x" * 65),
        lambda value: value.__setitem__("schema_version", 2),
        lambda value: value["execution"].__setitem__("provider", "other"),
        lambda value: value["execution"].__setitem__("provider", []),
        lambda value: value["execution"].__setitem__("model", ""),
        lambda value: value["execution"].__setitem__("effort", "too_much"),
        lambda value: value["execution"].pop("effort"),
    ]
    for index, mutate in enumerate(mutations):
        config_path, config = _valid_config(tmp_path / str(index))
        mutate(config)
        _reject(config_path, config)


# Catches filesystem validation mutations that accept missing, wrong-kind, or non-UTF-8 inputs.
def test_load_config_rejects_invalid_declared_paths(tmp_path: Path) -> None:
    mutations = [
        lambda root, value: value["skill"].__setitem__("source", "missing"),
        lambda root, value: (
            _write(root / "not-a-directory"),
            value["skill"].__setitem__("source", "not-a-directory"),
        ),
        lambda root, value: (root / "primary" / "SKILL.md").unlink(),
        lambda root, value: (root / "primary" / "SKILL.md").unlink()
        or (root / "primary" / "SKILL.md").mkdir(),
        lambda root, value: value["scenario"].__setitem__("prompt", "missing.txt"),
        lambda root, value: value["scenario"].__setitem__("prompt", "fixture"),
        lambda root, value: value["scenario"].__setitem__("fixture", "missing"),
        lambda root, value: value["scenario"].__setitem__("fixture", "prompt.txt"),
        lambda root, value: value["scenario"].__setitem__("prompt", "\x00"),
        lambda root, value: _write(root / "prompt.txt", b"\xff"),
        lambda root, value: _write(root / "primary" / "SKILL.md", b"\xff"),
    ]
    for index, mutate in enumerate(mutations):
        case_root = tmp_path / str(index)
        config_path, config = _valid_config(case_root)
        mutate(case_root, config)
        _reject(config_path, config)


# Catches mutations that allow an included special skill file or a special fixture entry.
def test_load_config_rejects_special_files(tmp_path: Path) -> None:
    for index, relative in enumerate(["primary/pipe", "fixture/pipe"]):
        case_root = tmp_path / str(index)
        config_path, config = _valid_config(case_root)
        os.mkfifo(case_root / relative)
        if relative.startswith("primary/"):
            config["skill"]["include"].append("pipe")
        _reject(config_path, config)


@pytest.mark.parametrize(
    "kind",
    [
        "not-list",
        "empty-list",
        "non-string",
        "directory",
        "symlink",
        "absolute",
        "empty-path",
        "dot-component",
        "dotdot-component",
        "duplicate",
        "missing-file",
        "missing-skill-md",
    ],
)
def test_load_config_rejects_invalid_file_includes(tmp_path: Path, kind: str) -> None:
    config_path, config = _valid_config(tmp_path)
    include: object = ["SKILL.md"]

    if kind == "not-list":
        include = "SKILL.md"
    elif kind == "empty-list":
        include = []
    elif kind == "non-string":
        include = ["SKILL.md", 1]
    elif kind == "directory":
        (tmp_path / "primary" / "extra").mkdir()
        include = ["SKILL.md", "extra"]
    elif kind == "symlink":
        (tmp_path / "primary" / "link").symlink_to("SKILL.md")
        include = ["SKILL.md", "link"]
    elif kind == "absolute":
        include = ["SKILL.md", str(tmp_path / "primary" / "SKILL.md")]
    elif kind == "empty-path":
        include = ["SKILL.md", ""]
    elif kind == "dot-component":
        _write(tmp_path / "primary" / "extra.txt")
        include = ["SKILL.md", "./extra.txt"]
    elif kind == "dotdot-component":
        _write(tmp_path / "outside.txt")
        include = ["SKILL.md", "../outside.txt"]
    elif kind == "duplicate":
        include = ["SKILL.md", "SKILL.md"]
    elif kind == "missing-file":
        include = ["SKILL.md", "missing.txt"]
    elif kind == "missing-skill-md":
        _write(tmp_path / "primary" / "extra.txt")
        include = ["extra.txt"]

    config["skill"]["include"] = include
    _reject(config_path, config)


# Catches uniqueness mutations that permit a dependency to reuse the primary identifier.
def test_load_config_rejects_duplicate_skill_identifiers(tmp_path: Path) -> None:
    dependencies = [
        [{"id": "primary", "source": "dependency", "include": ["SKILL.md"]}],
        [
            {"id": "duplicate", "source": "dependency", "include": ["SKILL.md"]},
            {"id": "duplicate", "source": "dependency", "include": ["SKILL.md"]},
        ],
    ]
    for index, value in enumerate(dependencies):
        config_path, config = _valid_config(tmp_path / str(index))
        config["dependencies"] = value
        _reject(config_path, config)


# Catches containment mutations that could copy the withheld configuration into inputs.
def test_load_config_rejects_configuration_containment(tmp_path: Path) -> None:
    mutations = [
        lambda root, value, path: value["scenario"].__setitem__("prompt", path.name),
        lambda root, value, path: value["skill"].__setitem__("source", "."),
        lambda root, value, path: value["scenario"].__setitem__("fixture", "."),
    ]
    for index, mutate in enumerate(mutations):
        case_root = tmp_path / str(index)
        config_path, config = _valid_config(case_root)
        mutate(case_root, config, config_path)
        _reject(config_path, config)


# Catches preparation-ambiguity mutations that permit the fixture's reserved directory.
def test_load_config_rejects_fixture_supplied_skills_collision(tmp_path: Path) -> None:
    config_path, config = _valid_config(tmp_path)
    (tmp_path / "fixture" / "supplied-skills").mkdir()

    _reject(config_path, config)


# Catches fixed-root overlap mutations that place run bundles inside declared input roots.
def test_load_config_rejects_fixed_run_root_overlap(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import skilltest.config as config_module

    config_path, config = _valid_config(tmp_path / "config-contains-run-root")
    with monkeypatch.context() as context:
        context.setattr(config_module.tempfile, "gettempdir", lambda root=config_path.parent: str(root))
        _save(config_path, config)
        with pytest.raises(ConfigError):
            load_config(config_path)

    for index, kind in enumerate(["skill", "fixture"]):
        parent = tmp_path / f"inside-{index}"
        case_root = parent / "config"
        config_path, config = _valid_config(case_root)
        input_root = parent / "input" / kind
        if kind == "skill":
            _write(input_root / "SKILL.md", "primary")
            config["skill"]["source"] = "../input/skill"
        else:
            input_root.mkdir(parents=True)
            config["scenario"]["fixture"] = "../input/fixture"
        with monkeypatch.context() as context:
            context.setattr(config_module.tempfile, "gettempdir", lambda root=input_root: str(root))
            _save(config_path, config)
            with pytest.raises(ConfigError):
                load_config(config_path)

    for index, kind in enumerate(["skill", "fixture"]):
        parent = tmp_path / f"contains-{index}"
        case_root = parent / "config"
        config_path, config = _valid_config(case_root)
        run_input = parent / "skilltest-runs" / kind
        if kind == "skill":
            _write(run_input / "SKILL.md", "primary")
            config["skill"]["source"] = "../skilltest-runs/skill"
        else:
            run_input.mkdir(parents=True)
            config["scenario"]["fixture"] = "../skilltest-runs/fixture"
        with monkeypatch.context() as context:
            context.setattr(config_module.tempfile, "gettempdir", lambda root=parent: str(root))
            _save(config_path, config)
            with pytest.raises(ConfigError):
                load_config(config_path)
