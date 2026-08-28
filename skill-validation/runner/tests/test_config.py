import json
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from skilltest.config import ConfigError, load_config


def _write(path: Path, content: str | bytes = "") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))
    return path


def _valid_config(tmp_path: Path) -> tuple[Path, dict[str, object]]:
    _write(tmp_path / "prompt.md", "follow the prompt")
    return tmp_path / "case.json", {
        "schema_version": "0.2",
        "id": "config-case",
        "prompt": "prompt.md",
        "fixtures": [],
        "execution": {"provider": "codex", "model": "gpt-5.6-sol", "effort": "low"},
    }


def _save(path: Path, value: object) -> bytes:
    raw = json.dumps(value, separators=(",", ":")).encode("utf-8")
    path.write_bytes(raw)
    return raw


def _reject(path: Path, value: object) -> None:
    _save(path, value)
    with pytest.raises(ConfigError):
        load_config(path)


# Catches a loader mutation that retains the schema 0.1 skill/scenario contract.
def test_load_config_accepts_an_empty_fixture_declaration(tmp_path: Path) -> None:
    config_path, value = _valid_config(tmp_path)
    raw = _save(config_path, value)

    loaded = load_config(config_path)

    assert loaded.schema_version == "0.2"
    assert loaded.id == "config-case"
    assert loaded.prompt == (tmp_path / "prompt.md").resolve()
    assert loaded.fixtures == ()
    assert loaded.execution.provider == "codex"
    assert loaded.execution.model == "gpt-5.6-sol"
    assert loaded.execution.effort == "low"
    assert loaded.config_path == config_path.resolve()
    assert loaded.config_bytes == raw
    with pytest.raises(FrozenInstanceError):
        loaded.id = "other"  # type: ignore[misc]


# Catches a loader mutation that rejects legal parent-directory sources or fails to canonicalize targets.
def test_load_config_accepts_multiple_files_and_canonicalizes_targets(tmp_path: Path) -> None:
    config_path, value = _valid_config(tmp_path / "case")
    _write(tmp_path / "case" / "real-source" / "a.txt", "a")
    (tmp_path / "case" / "source").symlink_to("real-source", target_is_directory=True)
    _write(tmp_path / "shared" / "b.txt", "b")
    value["fixtures"] = [
        {"source": "source/a.txt", "target": "docs/a.txt"},
        {"source": "../shared/b.txt", "target": "b.txt"},
    ]
    _save(config_path, value)

    loaded = load_config(config_path)

    assert [(item.source, item.target) for item in loaded.fixtures] == [
        ((tmp_path / "case" / "real-source" / "a.txt").resolve(), Path("docs/a.txt")),
        ((tmp_path / "shared" / "b.txt").resolve(), Path("b.txt")),
    ]


# Catches a parser mutation that accepts duplicate keys or non-finite JSON numbers.
@pytest.mark.parametrize(
    "raw",
    [
        b'{"schema_version":"0.2","schema_version":"0.2"}',
        b'{"schema_version":NaN}',
        b'{"schema_version":Infinity}',
        b'{"schema_version":-Infinity}',
        b'{"fixtures":[{"source":"a","source":"b"}]}',
        b"not-json",
    ],
)
def test_load_config_rejects_non_strict_json(tmp_path: Path, raw: bytes) -> None:
    config_path = _write(tmp_path / "case.json", raw)

    with pytest.raises(ConfigError):
        load_config(config_path)


# Catches a schema-validation mutation that accepts missing, stale, or unknown declaration keys.
def test_load_config_requires_exact_schema_keys(tmp_path: Path) -> None:
    mutations = [
        lambda value: value.pop("fixtures"),
        lambda value: value.__setitem__("skill", {"id": "primary"}),
        lambda value: value["execution"].__setitem__("extra", True),
        lambda value: value.__setitem__("fixtures", [{"source": "a.txt"}]),
        lambda value: value.__setitem__("fixtures", [{"source": "a.txt", "target": "a", "extra": True}]),
    ]
    for index, mutate in enumerate(mutations):
        config_path, value = _valid_config(tmp_path / str(index))
        _write(config_path.parent / "a.txt", "a")
        mutate(value)
        _reject(config_path, value)


# Catches a preflight mutation that defers prompt decoding until workspace preparation.
def test_load_config_rejects_non_utf8_prompt_before_run_allocation(tmp_path: Path) -> None:
    config_path, value = _valid_config(tmp_path)
    _write(tmp_path / "prompt.md", b"\xff")
    _save(config_path, value)

    with pytest.raises(ConfigError, match="prompt must be readable UTF-8"):
        load_config(config_path)


# Catches a filesystem mutation that follows a final prompt or fixture symlink.
@pytest.mark.parametrize("field", ["prompt", "source"])
def test_load_config_rejects_final_entry_symlinks(tmp_path: Path, field: str) -> None:
    config_path, value = _valid_config(tmp_path)
    _write(tmp_path / "real.txt", "real")
    (tmp_path / "link.txt").symlink_to("real.txt")
    if field == "prompt":
        value["prompt"] = "link.txt"
    else:
        value["fixtures"] = [{"source": "link.txt", "target": "input.txt"}]
    _reject(config_path, value)


# Catches a path-validation mutation that accepts absolute or non-regular prompt and source entries.
@pytest.mark.parametrize("field", ["prompt", "source"])
def test_load_config_rejects_absolute_or_non_regular_declared_files(
    tmp_path: Path, field: str
) -> None:
    config_path, value = _valid_config(tmp_path)
    source_directory = tmp_path / "source-directory"
    source_directory.mkdir()
    if field == "prompt":
        value["prompt"] = str(tmp_path / "prompt.md")
    else:
        value["fixtures"] = [{"source": str(tmp_path / "prompt.md"), "target": "input.txt"}]
    _reject(config_path, value)

    if field == "prompt":
        value["prompt"] = source_directory.name
    else:
        value["fixtures"] = [{"source": source_directory.name, "target": "input.txt"}]
    _reject(config_path, value)


# Catches a target-path mutation that permits ambiguous or non-canonical workspace destinations.
@pytest.mark.parametrize("target", ["/a", "a/", "a//b", "a\\b", ".", "..", "a/./b", "a/../b"])
def test_load_config_rejects_invalid_fixture_targets(tmp_path: Path, target: str) -> None:
    config_path, value = _valid_config(tmp_path)
    _write(tmp_path / "source.txt", "fixture")
    value["fixtures"] = [{"source": "source.txt", "target": target}]
    _reject(config_path, value)


# Catches a conflict mutation that permits duplicate or ancestor/descendant targets.
@pytest.mark.parametrize("targets", [("a", "a"), ("a", "a/b"), ("a/b", "a")])
def test_load_config_rejects_conflicting_fixture_targets(
    tmp_path: Path, targets: tuple[str, str]
) -> None:
    config_path, value = _valid_config(tmp_path)
    _write(tmp_path / "one.txt", "one")
    _write(tmp_path / "two.txt", "two")
    value["fixtures"] = [
        {"source": "one.txt", "target": targets[0]},
        {"source": "two.txt", "target": targets[1]},
    ]
    _reject(config_path, value)


# Catches scalar-validation mutations that broaden identifiers, providers, models, or efforts.
def test_load_config_validates_execution_scalars(tmp_path: Path) -> None:
    mutations = [
        lambda value: value.__setitem__("id", "Uppercase"),
        lambda value: value["execution"].__setitem__("provider", "other"),
        lambda value: value["execution"].__setitem__("provider", []),
        lambda value: value["execution"].__setitem__("model", ""),
        lambda value: value["execution"].__setitem__("effort", "too_much"),
        lambda value: value["execution"].pop("effort"),
    ]
    for index, mutate in enumerate(mutations):
        config_path, value = _valid_config(tmp_path / str(index))
        mutate(value)
        _reject(config_path, value)
