import os
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from pathlib import Path

import pytest

import skilltest.workspace as workspace_module
from skilltest.config import FixtureDeclaration


def _entries(root: Path) -> list[str]:
    paths: list[str] = []
    for directory, directories, files in os.walk(root, followlinks=False):
        base = Path(directory)
        for name in sorted([*directories, *files]):
            paths.append((base / name).relative_to(root).as_posix())
    return sorted(paths)


# Catches allocation regressions that reuse a run directory or initialize it before ownership.
def test_create_run_allocates_distinct_serial_directories(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    case = build_config_case(name="serial")
    run_root = case.root / "tmp"
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(run_root))
        first = workspace_module.create_run(case.config)
        second = workspace_module.create_run(case.config)

    expected_base = (run_root / "skilltest-runs").resolve()
    assert first.run_dir.parent == expected_base
    assert second.run_dir.parent == expected_base
    assert first.run_dir != second.run_dir
    assert first.run_id == first.run_dir.name
    assert second.run_id == second.run_dir.name
    assert first.started_at.endswith("Z")
    assert first.run_dir.is_dir()
    assert not first.marker_path.exists()
    assert not first.prompt_template_path.exists()
    assert not first.prompt_path.exists()
    assert not first.workspace_dir.exists()
    assert not first.config_path.exists()
    assert not first.stdout_path.exists()
    assert not first.stderr_path.exists()
    assert not first.final_output_path.exists()
    assert not first.runner_log_path.exists()
    assert not first.result_path.exists()


# Catches create_run changes that collide when callers prepare runs concurrently.
def test_create_run_allocates_distinct_concurrent_directories(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    case = build_config_case(name="concurrent")
    run_root = case.root / "tmp"
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(run_root))
        with ThreadPoolExecutor(max_workers=2) as pool:
            first, second = pool.map(
                lambda _: workspace_module.create_run(case.config), range(2)
            )

    expected_base = (run_root / "skilltest-runs").resolve()
    assert first.run_dir.parent == expected_base
    assert second.run_dir.parent == expected_base
    assert first.run_dir != second.run_dir


# Catches layout, literal-rendering, and fixture-boundary regressions in prepared runs.
def test_prepare_workspace_builds_isolated_layout_and_renders_prompt(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    template = (
        b"workspace={{workspace_dir}}\n"
        b"fixture={{fixture_dir}} {{fixture_dir}}\n"
        b"evidence={{evidence_dir}} {{evidence_dir}}\n"
        b"unknown={{not_a_token}}\n"
        b"again={{workspace_dir}}\n"
    )
    case = build_config_case(
        name="isolated",
        prompt_bytes=template,
        fixtures=(
            ("sources/guide.txt", "docs/guide.txt", "fixture guide\n"),
            ("sources/payload.bin", "payload.bin", b"fixture bytes\x00"),
        ),
    )
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(case.root / "tmp"))
        run = workspace_module.create_run(case.config)
        prepared = workspace_module.prepare_workspace(run, case.config)

    expected_prompt = (
        f"workspace={run.workspace_dir.resolve()}\n"
        f"fixture={run.fixture_dir.resolve()} {run.fixture_dir.resolve()}\n"
        f"evidence={run.evidence_dir.resolve()} {run.evidence_dir.resolve()}\n"
        "unknown={{not_a_token}}\n"
        f"again={run.workspace_dir.resolve()}\n"
    ).encode("utf-8")
    assert _entries(run.run_dir) == [
        ".skilltest-run",
        "prompt-template.txt",
        "prompt.txt",
        "workspace",
        "workspace/evidence",
        "workspace/fixture",
        "workspace/fixture/docs",
        "workspace/fixture/docs/guide.txt",
        "workspace/fixture/payload.bin",
    ]
    assert run.prompt_template_path.read_bytes() == template
    assert run.prompt_path.read_bytes() == expected_prompt
    assert prepared.workspace_dir == run.workspace_dir
    assert prepared.prompt_bytes == expected_prompt
    assert prepared.final_output_path == run.final_output_path
    assert run.fixture_dir.is_dir()
    assert run.evidence_dir.is_dir()
    assert not any(run.evidence_dir.iterdir())
    assert (run.fixture_dir / "docs" / "guide.txt").read_bytes() == b"fixture guide\n"
    assert (run.fixture_dir / "payload.bin").read_bytes() == b"fixture bytes\x00"
    assert not (run.workspace_dir / "docs").exists()
    assert not (run.workspace_dir / "payload.bin").exists()
    assert not run.config_path.exists()


# Catches a copy-boundary mutation that trusts a target constructed outside config loading.
def test_prepare_workspace_rejects_destination_outside_resolved_fixture_root(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    case = build_config_case(
        name="escaping-target",
        fixtures=(("sources/input.txt", "input.txt", b"fixture bytes"),),
    )
    forged = replace(
        case.config,
        fixtures=(
            FixtureDeclaration(
                source=case.config.fixtures[0].source,
                target=Path("..") / "escape.txt",
            ),
        ),
    )
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(case.root / "tmp"))
        run = workspace_module.create_run(forged)
        with pytest.raises(OSError, match="outside fixture root"):
            workspace_module.prepare_workspace(run, forged)

    assert not (run.workspace_dir / "escape.txt").exists()


# Catches a copy mutation that overwrites filesystem-equivalent target names.
def test_prepare_workspace_rejects_filesystem_equivalent_target_collision_without_clobber(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    case = build_config_case(
        name="case-collision",
        fixtures=(
            ("sources/one.txt", "a", b"first fixture"),
            ("sources/two.txt", "A", b"second fixture"),
        ),
    )
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(case.root / "tmp"))
        run = workspace_module.create_run(case.config)
        original_open = os.open

        def case_insensitive_open(path: object, *args: object, **kwargs: object) -> int:
            candidate = Path(path)  # type: ignore[arg-type]
            if candidate.parent == run.fixture_dir and candidate.name == "A":
                path = candidate.with_name("a")
            return original_open(path, *args, **kwargs)  # type: ignore[arg-type]

        context.setattr(os, "open", case_insensitive_open)
        with pytest.raises(FileExistsError):
            workspace_module.prepare_workspace(run, case.config)

    assert (run.fixture_dir / "a").read_bytes() == b"first fixture"
    assert len(list(run.fixture_dir.iterdir())) == 1


# Catches rendering changes that normalize CRLF or lone-CR prompt-template line endings.
def test_prepare_workspace_preserves_template_line_endings_during_rendering(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    template = (
        b"workspace={{workspace_dir}}\r\n"
        b"fixture={{fixture_dir}}\r"
        b"evidence={{evidence_dir}}\n"
        b"unknown={{other}}\r\n"
    )
    case = build_config_case(name="line-endings", prompt_bytes=template)
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(case.root / "tmp"))
        run = workspace_module.create_run(case.config)
        prepared = workspace_module.prepare_workspace(run, case.config)

    expected = b"".join(
        (
            b"workspace=",
            str(run.workspace_dir.resolve()).encode("utf-8"),
            b"\r\nfixture=",
            str(run.fixture_dir.resolve()).encode("utf-8"),
            b"\revidence=",
            str(run.evidence_dir.resolve()).encode("utf-8"),
            b"\nunknown={{other}}\r\n",
        )
    )
    assert run.prompt_template_path.read_bytes() == template
    assert run.prompt_path.read_bytes() == expected
    assert prepared.prompt_bytes == expected


# Catches a preparation mutation that skips required empty runtime directories.
def test_prepare_workspace_creates_empty_fixture_and_evidence_directories(
    build_config_case: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    case = build_config_case(name="empty", prompt_bytes=b"keep {{other}} unchanged")
    with monkeypatch.context() as context:
        context.setattr(workspace_module.tempfile, "gettempdir", lambda: str(case.root / "tmp"))
        run = workspace_module.create_run(case.config)
        prepared = workspace_module.prepare_workspace(run, case.config)

    assert _entries(run.run_dir) == [
        ".skilltest-run",
        "prompt-template.txt",
        "prompt.txt",
        "workspace",
        "workspace/evidence",
        "workspace/fixture",
    ]
    assert prepared.prompt_bytes == b"keep {{other}} unchanged"
    assert not any(run.fixture_dir.iterdir())
    assert not any(run.evidence_dir.iterdir())
