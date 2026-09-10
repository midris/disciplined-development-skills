"""Runner orchestration: in-memory provider outcomes, real artifact persistence."""

import hashlib
import json
from pathlib import Path
from unittest.mock import Mock

import jsonschema
import pytest

from skilltest import runner, workspace
from skilltest.providers import ProviderResult

SCHEMA = json.loads((Path(__file__).parents[1] / "result.schema.json").read_text())


@pytest.fixture
def provider_call(monkeypatch):
    call = Mock(return_value=ProviderResult("codex", True, exit_code=0))
    monkeypatch.setattr(runner, "invoke_provider", call)
    return call


def record(outcome):
    value = json.loads((outcome.run_dir / "result.json").read_text())
    jsonschema.validate(value, SCHEMA)
    return value


def fail_write(monkeypatch, filename):
    write = Path.write_bytes

    def partial(path, data):
        if path.name == filename or path.name.startswith(f".{filename}-"):
            write(path, data[:3])
            raise OSError("simulated partial write")
        return write(path, data)

    monkeypatch.setattr(Path, "write_bytes", partial)


@pytest.mark.parametrize("provider", ["codex", "claude"])
def test_rendered_request_and_raw_artifacts_are_preserved(build_config_case, provider_call, provider):
    # Break: wrong rendered request, parsed output, or pre-run rather than final inventories.
    template = b"{{workspace_dir}}\n{{fixture_dir}}\n{{evidence_dir}}\n"
    case = build_config_case(provider=provider, prompt_bytes=template,
                             fixtures=(("source.txt", "input.txt", b"original"),))
    observed_publication = []

    def respond(request, **kwargs):
        observed_publication.append((request.workspace_dir.parent / "config.json").exists())
        (request.workspace_dir / "fixture/input.txt").write_bytes(b"changed")
        (request.workspace_dir / "evidence/note.txt").write_bytes(b"evidence")
        if provider == "codex":
            request.final_output_path.write_bytes(b"final\x00bytes")
        return ProviderResult(provider, True, exit_code=0, stdout_bytes=b"not-json\n", stderr_bytes=b"warning")

    provider_call.side_effect = respond
    outcome = runner.run_once(case.config_path)
    assert outcome.exit_code == 0 and outcome.diagnostic is None
    request = provider_call.call_args.args[0]
    assert (request.provider, request.model, request.effort) == (provider, "gpt-5.6-sol", "low")
    assert request.workspace_dir == outcome.run_dir / "workspace"
    expected = "".join(f"{p.resolve()}\n" for p in (
        request.workspace_dir, request.workspace_dir / "fixture", request.workspace_dir / "evidence"))
    assert request.prompt_bytes == expected.encode()
    assert request.final_output_path == outcome.run_dir / "final.txt"
    assert observed_publication == [False]
    for name, content in {
        "config.json": case.config_path.read_bytes(), "prompt-template.txt": template,
        "prompt.txt": expected.encode(), "stdout.txt": b"not-json\n", "stderr.txt": b"warning",
        **({"final.txt": b"final\x00bytes"} if provider == "codex" else {}),
    }.items():
        assert (outcome.run_dir / name).read_bytes() == content
    value = record(outcome)
    assert value["status"] == "COMPLETED" and value["infrastructure_error"] is None
    assert value["execution"] == {
        "provider": provider, "model": "gpt-5.6-sol", "effort": "low", "executable": provider,
        "timeout_seconds": 900, "invocation_started": True, "timed_out": False, "exit_code": 0,
    }
    for kind, name, content in [("fixture", "input.txt", b"changed"), ("evidence", "note.txt", b"evidence")]:
        assert value["artifacts"][kind]["entries"] == [{
            "path": name, "type": "file", "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest(),
        }]
    assert {key: val["path"] for key, val in value["artifacts"].items()} == {
        "config": "config.json", "prompt_template": "prompt-template.txt", "prompt": "prompt.txt",
        "stdout": "stdout.txt", "stderr": "stderr.txt", "final": "final.txt",
        "fixture": "workspace/fixture", "evidence": "workspace/evidence",
    }
    assert (outcome.run_dir / "runner.log").read_text().splitlines()[-1].endswith("COMPLETED")
    assert not (outcome.run_dir / "subject-input.txt").exists()
    assert not (outcome.run_dir / "inputs").exists()


def test_preparation_failure_never_calls_provider(build_config_case, provider_call, monkeypatch):
    # Break: continuing into provider execution after failed preparation.
    monkeypatch.setattr(workspace.shutil, "copy2", Mock(side_effect=OSError("copy failed")))
    outcome = runner.run_once(build_config_case().config_path)
    assert outcome.exit_code == 1
    provider_call.assert_not_called()
    value = record(outcome)
    assert value["infrastructure_error"]["code"] == "PREPARATION_FAILED"
    assert value["execution"]["invocation_started"] is False


@pytest.mark.parametrize("result, expected", [
    (ProviderResult("codex", False, preparation_error="setup failed"), "PREPARATION_FAILED"),
    (ProviderResult("codex", False, launch_error="launch failed"), "PROVIDER_LAUNCH_FAILED"),
    (ProviderResult("codex", True, exit_code=0, cleanup_error="cleanup failed"), "PROVIDER_CLEANUP_FAILED"),
    (ProviderResult("codex", True, exit_code=7, cleanup_error="cleanup failed"), "PROVIDER_EXIT_NONZERO"),
])
def test_provider_failure_classification_retains_actual_outcome(build_config_case, provider_call, result, expected):
    # Break: wrong error precedence, invented exit status, or lost evaluable output.
    def respond(request, **kwargs):
        if result.invocation_started:
            request.final_output_path.write_bytes(b"judgeable answer")
        return result
    provider_call.side_effect = respond
    outcome = runner.run_once(build_config_case().config_path)
    value = record(outcome)
    assert outcome.exit_code == 1
    assert value["infrastructure_error"]["code"] == expected
    assert value["execution"]["exit_code"] == result.exit_code
    assert value["execution"]["invocation_started"] is result.invocation_started
    if result.invocation_started:
        assert (outcome.run_dir / "final.txt").read_bytes() == b"judgeable answer"


@pytest.mark.parametrize("timed_out, exit_code, expected", [
    (True, -15, "PROVIDER_TIMEOUT"), (False, 9, "PROVIDER_EXIT_NONZERO"),
])
def test_failed_provider_mutations_survive_artifact_failure(
    build_config_case, provider_call, monkeypatch, timed_out, exit_code, expected
):
    # Break: lost writes, or an artifact error masking the provider failure.
    def respond(request, **kwargs):
        (request.workspace_dir / "fixture/input.txt").write_bytes(b"changed")
        (request.workspace_dir / "evidence/note.txt").write_bytes(b"evidence")
        return ProviderResult("codex", True, exit_code=exit_code, timed_out=timed_out,
                              stdout_bytes=b"raw output", stderr_bytes=b"raw error")
    provider_call.side_effect = respond
    fail_write(monkeypatch, "stdout.txt")
    outcome = runner.run_once(build_config_case(fixtures=(("source.txt", "input.txt", b"original"),)).config_path)
    value = record(outcome)
    assert outcome.exit_code == 1 and value["infrastructure_error"]["code"] == expected
    assert value["execution"]["timed_out"] is timed_out
    assert value["execution"]["exit_code"] == exit_code
    assert value["artifacts"]["stdout"]["exists"] is False
    assert (outcome.run_dir / "stderr.txt").read_bytes() == b"raw error"
    for kind, name, data in [("fixture", "input.txt", b"changed"), ("evidence", "note.txt", b"evidence")]:
        assert (outcome.run_dir / "workspace" / kind / name).read_bytes() == data
        assert value["artifacts"][kind]["entries"][0]["sha256"] == hashlib.sha256(data).hexdigest()


@pytest.mark.parametrize("filename, artifact", [("stdout.txt", "stdout"), ("config.json", "config")])
def test_partial_artifact_is_removed_and_reported(build_config_case, provider_call, monkeypatch, filename, artifact):
    # Break: publishing a partial file as successfully retained evidence.
    case = build_config_case()
    def respond(request, **kwargs):
        request.final_output_path.write_bytes(b"judgeable final")
        return ProviderResult("codex", True, exit_code=0, stdout_bytes=b"output", stderr_bytes=b"error")
    provider_call.side_effect = respond
    fail_write(monkeypatch, filename)
    outcome = runner.run_once(case.config_path)
    value = record(outcome)
    assert outcome.exit_code == 1 and value["infrastructure_error"]["code"] == "ARTIFACT_WRITE_FAILED"
    assert value["artifacts"][artifact] == {"path": filename, "exists": False, "bytes": None, "sha256": None}
    assert not (outcome.run_dir / filename).exists()
    assert not list(outcome.run_dir.glob(f".{filename}-*"))
    assert (outcome.run_dir / "stderr.txt").read_bytes() == b"error"
    assert (outcome.run_dir / "final.txt").read_bytes() == b"judgeable final"


def test_result_publication_failure_removes_partial_file(build_config_case, provider_call, monkeypatch):
    # Break: leaving an incomplete result record after failed atomic publication.
    replace = Path.replace
    def fail_result(path, target):
        if target.name == "result.json":
            raise OSError("result failed")
        return replace(path, target)
    monkeypatch.setattr(Path, "replace", fail_result)
    outcome = runner.run_once(build_config_case().config_path)
    assert outcome.exit_code == 1
    assert outcome.diagnostic == "result artifact write failed: result failed"
    assert not (outcome.run_dir / "result.json").exists()
    assert not list(outcome.run_dir.glob(".result-*"))


@pytest.mark.parametrize("stdout, final", [
    (b'{"type":"system","subtype":"init"}\n{"type":"result","subtype":"success","is_error":false,"result":"answer"}\n', b"answer"),
    (b'{"type":"result","subtype":"success","is_error":false,"result":""}\n', b""),
    (b"not-json\n", None),
    (b"", None),
    (b'{"type":"result","subtype":"error_during_execution","is_error":true,"result":"error"}\n', None),
    (b'{"type":"result","subtype":"success","is_error":false,"result":"one"}\n{"type":"result","subtype":"success","is_error":false,"result":"two"}\n', None),
])
def test_claude_trace_is_retained_and_only_unambiguous_final_is_extracted(build_config_case, provider_call, stdout, final):
    provider_call.return_value = ProviderResult("claude", True, exit_code=0, stdout_bytes=stdout)
    outcome = runner.run_once(build_config_case(provider="claude").config_path)
    value = record(outcome)
    assert outcome.exit_code == 0 and value["status"] == "COMPLETED"
    assert (outcome.run_dir / "stdout.txt").read_bytes() == stdout
    path = outcome.run_dir / "final.txt"
    if final is None:
        assert not path.exists()
        assert "final answer" in (outcome.run_dir / "runner.log").read_text()
    else:
        assert path.read_bytes() == final


@pytest.mark.parametrize("timed_out, exit_code, cleanup_error, code", [
    (True, None, "unreaped", "PROVIDER_TIMEOUT"),
    (False, 0, "cleanup failed", "PROVIDER_CLEANUP_FAILED"),
])
def test_claude_lifecycle_results_use_existing_schema_and_codes(build_config_case, provider_call, timed_out, exit_code, cleanup_error, code):
    provider_call.return_value = ProviderResult("claude", True, exit_code=exit_code,
        timed_out=timed_out, cleanup_error=cleanup_error, stdout_bytes=b"partial trace")
    outcome = runner.run_once(build_config_case(provider="claude").config_path)
    value = record(outcome)
    assert value["infrastructure_error"]["code"] == code
    assert value["execution"]["exit_code"] == exit_code
    assert (outcome.run_dir / "stdout.txt").read_bytes() == b"partial trace"
