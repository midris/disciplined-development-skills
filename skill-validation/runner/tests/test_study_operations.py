"""Offline CLI contracts: real Git fixtures, no model or provider invocation."""

import json
import shutil
from pathlib import Path

import pytest
from skilltest.cli import main

# Reuse the version-1 two-attempt fixture; it pins inputs/results in disposable Git.
from test_documents import document_study

pytestmark = pytest.mark.process_smoke


def invoke(args):
    try:
        return main(["docs", *map(str, args)])
    except SystemExit as error:
        return error.code


@pytest.fixture
def retention_case(document_study):
    root, write, commit, ident = document_study
    source = root.parent / "run-new"
    shutil.copytree(root.parent / "bundle-1", source)
    # Use the actual producer shape; the shared document fixture predates retention.
    from dataclasses import fields, replace
    from test_results import _context
    from skilltest.config import load_config
    from skilltest.providers import ProviderResult
    from skilltest.results import result_record

    ctx = _context(root.parent)
    paths = {
        f.name: source / getattr(ctx, f.name).relative_to(ctx.run_dir)
        for f in fields(ctx)
        if isinstance(getattr(ctx, f.name), Path)
    }
    ctx = replace(ctx, **paths, run_id=source.name)
    value = result_record(
        ctx,
        load_config(root / "case/original.json"),
        ProviderResult("codex", True, exit_code=0),
        None,
        "2026-09-18T00:00:00.000Z",
        1.0,
    )
    (source / "result.json").write_text(json.dumps(value))
    (source / ".hidden").write_bytes(b"evidence\x00")
    (source / "link").symlink_to(".hidden")
    store = root.parent / "store"
    store.mkdir()
    index = root / "new-index.json"
    args = [
        "retain",
        root / "protocol.md",
        source,
        "--batch",
        "example",
        "--order",
        "1",
        "--index",
        index,
        "--store",
        store,
        "--revision",
        commit(),
    ]
    return root, source, store, index, args


def test_retain_copies_hidden_evidence_and_registers_verified_charge(
    retention_case, capsys
):
    root, source, store, index, args = retention_case
    assert invoke(args) == 0
    a = json.loads(index.read_text())["attempts"][0]
    assert a["case_id"] == "example" and a["repetition"] == 1
    assert a["allocation"] == {"pool": "subject", "charge": 1}
    assert a["result"] is None and a["bundle"]["verified"] is True
    dest = store / "run-new"
    assert (dest / ".hidden").read_bytes() == b"evidence\x00"
    assert (dest / "link").is_symlink()
    inv = json.loads((store / "run-new.inventory.json").read_text())
    assert inv["bundle"] == str(dest)
    assert {e["path"] for e in inv["entries"]} == {
        ".hidden",
        "link",
        "config.json",
        "final.txt",
        "result.json",
    }
    assert (
        invoke(["check", index, "--json"]) == 0
    )  # Unassessed is incomplete, not invalid.


def test_retain_refuses_duplicate_and_preserves_index(retention_case):
    _, _, _, index, args = retention_case
    assert invoke(args) == 0
    original = index.read_bytes()
    assert invoke(args) != 0
    assert index.read_bytes() == original


@pytest.mark.parametrize(
    "mutation",
    [
        "unfinished",
        "cleanup",
        "unknown-charge",
        "wrong-config",
        "existing-destination",
        "nested-store",
    ],
)
def test_retain_rejects_unverifiable_attempt_before_registration(
    retention_case, mutation
):
    _, source, store, index, args = retention_case
    p = source / "result.json"
    r = json.loads(p.read_text())
    if mutation == "unfinished":
        r.pop("finished_at")
    elif mutation == "cleanup":
        r.update(
            status="INFRA_ERROR",
            infrastructure_error={
                "code": "PROVIDER_CLEANUP_FAILED",
                "message": "still running",
            },
        )
    elif mutation == "unknown-charge":
        r["execution"].pop("invocation_started")
    elif mutation == "wrong-config":
        (source / "config.json").write_text("{}")
    elif mutation == "existing-destination":
        (store / source.name).mkdir()
    elif mutation == "nested-store":
        args[args.index("--store") + 1] = source
    p.write_text(json.dumps(r))
    assert invoke(args) != 0
    assert not index.exists()


@pytest.mark.parametrize("invoked", [True, False])
def test_retain_keeps_failed_runs_and_derives_charge(retention_case, invoked):
    _, source, _, index, args = retention_case
    p = source / "result.json"
    r = json.loads(p.read_text())
    r.update(
        status="INFRA_ERROR",
        infrastructure_error={
            "code": "PROVIDER_EXIT_NONZERO" if invoked else "PREPARATION_FAILED",
            "message": "test",
        },
    )
    r["execution"]["invocation_started"] = invoked
    r["execution"]["exit_code"] = 1 if invoked else None
    p.write_text(json.dumps(r))
    assert invoke(args) == 0
    assert json.loads(index.read_text())["attempts"][0]["allocation"]["charge"] == int(
        invoked
    )


@pytest.mark.parametrize("failure", ["copy", "mutation", "index-write"])
def test_retention_failure_does_not_register_or_overwrite(
    retention_case, monkeypatch, failure
):
    from skilltest.documents import retention

    _, source, store, index, args = retention_case
    real_copy, real_publish = retention.shutil.copytree, retention.publish

    def copy(*a, **kw):
        if failure == "copy":
            raise OSError("copy failed")
        result = real_copy(*a, **kw)
        if failure == "mutation":
            (source / ".hidden").write_text("changed")
        return result

    def publish(path, *a, **kw):
        if Path(path) == index:
            raise OSError("index write failed")
        return real_publish(path, *a, **kw)

    monkeypatch.setattr(retention.shutil, "copytree", copy)
    if failure == "index-write":
        monkeypatch.setattr(retention, "publish", publish)
    assert invoke(args) != 0
    assert not index.exists()
    assert (store / source.name).exists() == (failure == "index-write")
    assert not index.with_name(index.name + ".lock").exists()


def test_tables_derive_counts_lengths_and_refuse_overwrite(document_study):
    root, _, _, _ = document_study
    output = root / "tables.md"
    args = [
        "tables",
        root / "protocol.md",
        "--batch",
        "example",
        "--index",
        root / "example-run-index.json",
        "--output",
        output,
        "--source-target",
        "input.txt",
        "--output-evidence",
        "output",
    ]
    assert invoke(args) == 0
    text = output.read_text()
    assert "| example / original / F1 | 1 | 1 | 0 |" in text
    assert "| example / original / functional outcome | 1 | 1 | 0 |" in text
    assert "| 1 | example | original | 1 | valid | met |" in text
    assert "| 1 | 2 | 3 | +1 | longer (flag) |" in text
    assert "final.txt" in text and "results/1.json" in text
    assert invoke(args) != 0
    assert output.read_text() == text


@pytest.mark.parametrize(
    "state",
    ["unattempted", "unassessed", "unknown", "invalid", "bad-hash", "wrong-scope"],
)
def test_tables_preserve_missing_and_excluded_observations(document_study, state):
    root, write, commit, ident = document_study
    ip = root / "example-run-index.json"
    index = json.loads(ip.read_text())
    result = json.loads((root / "results/1.json").read_text())
    if state == "unattempted":
        index["attempts"] = []
    elif state == "unassessed":
        index["attempts"][0]["result"] = None
    elif state == "wrong-scope":
        index["attempts"][0]["repetition"] = 8
    elif state == "bad-hash":
        index["attempts"][0]["result"]["record"]["sha256"] = "0" * 64
    else:
        if state == "unknown":
            result["criteria"][0]["judgment"] = result["functional_result"] = (
                "insufficient evidence"
            )
        else:
            result["setup"]["status"] = "invalid"
        write("results/1.json", result)
        revision = commit()
        index["attempts"][0]["result"]["record"] = ident("results/1.json", revision)
    write("example-run-index.json", index)
    output = root / "tables.md"
    code = invoke(
        [
            "tables",
            root / "protocol.md",
            "--batch",
            "example",
            "--index",
            ip,
            "--output",
            output,
        ]
    )
    if state in {"bad-hash", "wrong-scope"}:
        assert code != 0 and not output.exists()
    else:
        assert code == 0
        text = output.read_text()
        if state == "unknown":
            assert "| example / original / F1 | 0 | 1 | 1 |" in text
        elif state == "invalid":
            assert "| example / original / F1 | 0 | 1 | 0 |" in text
            assert "invalid (excluded)" in text
        else:
            assert state in text


def test_manifest_refreshes_union_and_freezes_matching_inputs(document_study):
    root, write, commit, _ = document_study
    mp = root / "case/manifest.json"
    m = json.loads(mp.read_text())
    m["subject_sources"] = []
    m["source_revision"] = ""
    m["authorities"]["policy"]["sha256"] = ""
    write("case/manifest.json", m)
    draft = root / "draft.json"
    assert invoke(["manifest", mp, "--output", draft]) == 0
    value = json.loads(draft.read_text())
    assert value["status"] == "draft" and value["source_revision"] == ""
    assert {s["path"] for s in value["subject_sources"]} == {
        "case/prompt.md",
        "case/input.txt",
    }
    revision = commit()
    frozen = root / "frozen.json"
    assert invoke(["manifest", mp, "--output", frozen, "--revision", revision]) == 0
    assert invoke(["check", frozen, "--json"]) == 0
    write("case/input.txt", "changed")
    assert (
        invoke(["manifest", mp, "--output", root / "bad.json", "--revision", revision])
        != 0
    )
    assert not (root / "bad.json").exists()


@pytest.mark.parametrize("mutation", ["controller", "missing", "escape", "condition"])
def test_manifest_rejects_broken_working_inputs(document_study, mutation):
    root, write, _, _ = document_study
    mp = root / "case/manifest.json"
    m = json.loads(mp.read_text())
    config = json.loads((root / "case/original.json").read_text())
    if mutation == "controller":
        config["fixtures"][0]["source"] = "../policy.txt"
    elif mutation == "missing":
        config["fixtures"][0]["source"] = "absent.txt"
    elif mutation == "escape":
        config["fixtures"][0]["source"] = "../../outside.txt"
    else:
        m["conditions"][0]["id"] = "unexpected"
    write("case/original.json", config)
    write("case/manifest.json", m)
    output = root / "generated.json"
    assert invoke(["manifest", mp, "--output", output]) != 0
    assert not output.exists()


def test_manifest_checks_declared_paired_differences(document_study):
    root, write, _, _ = document_study
    mp = root / "case/manifest.json"
    m = json.loads(mp.read_text())
    config = json.loads((root / "case/original.json").read_text())
    config["fixtures"][0]["source"] = "candidate.txt"
    write("case/candidate.txt", "different input")
    write("case/candidate.json", config)
    m["conditions"].append(
        {
            **m["conditions"][0],
            "id": "candidate",
            "configuration": {
                **m["conditions"][0]["configuration"],
                "path": "case/candidate.json",
            },
        }
    )
    card = (
        (root / "case/assessment.md")
        .read_text()
        .replace("`original`", "`original`, `candidate`")
    )
    write("case/assessment.md", card)
    write("case/manifest.json", m)
    output = root / "generated.json"
    args = ["manifest", mp, "--output", output, "--compare", "original", "candidate"]
    assert invoke(args) != 0
    assert invoke([*args, "--allow-difference", "input.txt"]) == 0


def test_preparation_checks_draft_inputs_without_future_reports(document_study):
    root, write, _, _ = document_study
    p = root / "protocol.md"
    write("protocol.md", p.read_text().replace("Status: prepared", "Status: draft"))
    (root / "example-run-index.json").unlink()
    (root / "example-assessment.md").unlink()
    m = json.loads((root / "case/manifest.json").read_text())
    m.update(status="draft", source_revision="")
    write("case/manifest.json", m)
    args = ["check", p, "--ready-for", "preparation", "--batch", "example", "--json"]
    assert invoke(args) == 0
    assert invoke(["check", p, "--ready-for", "collection", "--batch", "example"]) != 0
    (root / "case/input.txt").unlink()
    assert invoke(args) != 0


def test_retain_appends_without_losing_existing_attempt(retention_case):
    _, source, store, index, args = retention_case
    assert invoke(args) == 0
    first = json.loads(index.read_text())["attempts"][0]
    second = source.with_name("run-next")
    shutil.copytree(source, second)
    result = json.loads((second / "result.json").read_text())
    result["run_id"] = second.name
    (second / "result.json").write_text(json.dumps(result))
    args[2] = second
    args[args.index("--order") + 1] = 2
    assert invoke(args) == 0
    attempts = json.loads(index.read_text())["attempts"]
    assert len(attempts) == 2 and attempts[0] == first


@pytest.mark.parametrize("operation", ["manifest", "preparation", "retain"])
def test_malformed_document_returns_cli_error_without_traceback(
    document_study, operation
):
    root, write, _, _ = document_study
    if operation == "manifest":
        write("case/manifest.json", {"format_version": "1"})
        args = ["manifest", root / "case/manifest.json", "--output", root / "out.json"]
    elif operation == "preparation":
        write("case/manifest.json", {"format_version": "1"})
        args = [
            "check",
            root / "protocol.md",
            "--ready-for",
            "preparation",
            "--batch",
            "example",
        ]
    else:
        # The non-object runner metadata is malformed at the evidence boundary.
        source = root.parent / "bundle-1"
        (source / "result.json").write_text("[]")
        from skilltest.documents.references import Context

        rev = Context.git_at(root, "rev-parse", "HEAD").decode().strip()
        args = [
            "retain",
            root / "protocol.md",
            source,
            "--batch",
            "example",
            "--order",
            1,
            "--index",
            root / "new.json",
            "--store",
            root.parent / "store",
            "--revision",
            rev,
        ]
    assert invoke(args) != 0


def test_preparation_accepts_complete_draft_case_and_catches_unknown_condition(
    document_study,
):
    root, write, _, _ = document_study
    card = (root / "case/assessment.md").read_text()
    write("case/assessment.md", card.replace("Status: prepared", "Status: draft"))
    args = [
        "check",
        root / "protocol.md",
        "--ready-for",
        "preparation",
        "--batch",
        "example",
    ]
    assert invoke(args) == 0
    p = root / "protocol.md"
    write(
        "protocol.md",
        p.read_text().replace("| example | original |", "| example | missing |"),
    )
    assert invoke(args) != 0


def test_tables_reject_same_criterion_ids_with_changed_policy(document_study):
    root, write, commit, ident = document_study
    write("policy.txt", "Changed rule using the same criterion ID")
    revision = commit()
    m = json.loads((root / "case/manifest.json").read_text())
    m["authorities"]["policy"] = ident("policy.txt", revision)
    write("case/new-manifest.json", m)
    revision = commit()
    r = json.loads((root / "results/2.json").read_text())
    r["manifest"] = ident("case/new-manifest.json", revision)
    write("results/2.json", r)
    revision = commit()
    index = json.loads((root / "example-run-index.json").read_text())
    index["attempts"][1]["result"]["record"] = ident("results/2.json", revision)
    write("example-run-index.json", index)
    out = root / "out.md"
    assert (
        invoke(
            [
                "tables",
                root / "protocol.md",
                "--batch",
                "example",
                "--index",
                root / "example-run-index.json",
                "--output",
                out,
            ]
        )
        != 0
    )
    assert not out.exists()


def test_retain_refuses_corrupt_existing_index(retention_case):
    _, _, _, index, args = retention_case
    index.write_bytes(b"")
    assert invoke(args) != 0
    assert index.read_bytes() == b""


def test_manifest_never_overwrites_input(document_study):
    root, _, _, _ = document_study
    p = root / "case/manifest.json"
    original = p.read_bytes()
    assert invoke(["manifest", p, "--output", p]) != 0
    assert p.read_bytes() == original


def test_tables_report_unresolved_setup_separately(document_study):
    root, write, commit, ident = document_study
    r = json.loads((root / "results/1.json").read_text())
    r["setup"]["status"] = "insufficient evidence"
    write("results/1.json", r)
    revision = commit()
    index = json.loads((root / "example-run-index.json").read_text())
    index["attempts"][0]["result"]["record"] = ident("results/1.json", revision)
    write("example-run-index.json", index)
    out = root / "out.md"
    assert (
        invoke(
            [
                "tables",
                root / "protocol.md",
                "--batch",
                "example",
                "--index",
                root / "example-run-index.json",
                "--output",
                out,
            ]
        )
        == 0
    )
    assert "| example / original | 2 | 2 | 1 | 0 | 1 | 0 |" in out.read_text()
    assert "insufficient evidence (excluded)" in out.read_text()


def test_retain_preserves_read_only_bundle_directory(retention_case):
    _, source, store, _, args = retention_case
    source.chmod(0o555)
    try:
        assert invoke(args) == 0
        assert (store / source.name).stat().st_mode & 0o777 == 0o555
    finally:
        source.chmod(0o755)
        dest = store / source.name
        if dest.exists():
            dest.chmod(0o755)


def test_generated_tables_validate_with_encoded_result_paths(document_study):
    from skilltest.documents import Report
    from skilltest.documents.references import Context
    from skilltest.documents.study import assessment, check_links

    root, write, commit, ident = document_study
    value = json.loads((root / "example-run-index.json").read_text())
    record = json.loads((root / "results/1.json").read_text())
    name = "results/result #1.json"
    write(name, record)
    revision = commit()
    value["attempts"][0]["result"]["record"] = ident(name, revision)
    write("example-run-index.json", value)
    revision = commit()
    out = root / "tables.md"
    assert (
        invoke(
            [
                "tables",
                root / "protocol.md",
                "--batch",
                "example",
                "--index",
                root / "example-run-index.json",
                "--output",
                out,
            ]
        )
        == 0
    )
    generated = out.read_text()
    ctx = Context(out, Report())
    check_links(generated, out, ctx)
    assert ctx.report.structurally_valid, ctx.report.diagnostics
    # The generated aggregate must be consumable by the assessment validator.
    report_path = root / "example-assessment.md"
    report = report_path.read_text()
    import re

    index_identity = ident("example-run-index.json", revision)
    report = re.sub(
        r"(?m)^Attempt index:.*$",
        f"Attempt index: [index](example-run-index.json), Git `{revision}`, SHA-256 `{index_identity['sha256']}`",
        report,
    )
    report = (
        report.split("## Coverage and execution results")[0]
        + "## Coverage and execution results\n\n"
        + generated
    )
    ctx = Context(report_path, Report())
    assessment(report, report_path, ctx)
    assert ctx.report.structurally_valid, ctx.report.diagnostics


def test_paired_prompt_check_cannot_be_shadowed_by_fixture_target(document_study):
    root, write, _, _ = document_study
    m = json.loads((root / "case/manifest.json").read_text())
    original = json.loads((root / "case/original.json").read_text())
    original["fixtures"][0]["target"] = "@prompt"
    write("case/original.json", original)
    candidate = {**original, "prompt": "candidate-prompt.md"}
    write("case/candidate-prompt.md", "A different task")
    write("case/candidate.json", candidate)
    m["conditions"].append(
        {
            **m["conditions"][0],
            "id": "candidate",
            "configuration": {
                **m["conditions"][0]["configuration"],
                "path": "case/candidate.json",
            },
        }
    )
    write(
        "case/assessment.md",
        (root / "case/assessment.md")
        .read_text()
        .replace("`original`", "`original`, `candidate`"),
    )
    write("case/manifest.json", m)
    out = root / "out.json"
    assert (
        invoke(
            [
                "manifest",
                root / "case/manifest.json",
                "--output",
                out,
                "--compare",
                "original",
                "candidate",
            ]
        )
        != 0
    )
    assert not out.exists()


@pytest.mark.parametrize(
    "change", ["missing-final", "changed-final", "missing-artifacts", "nested-change"]
)
def test_retain_checks_runner_capture_before_copy(retention_case, change):
    _, source, _, index, args = retention_case
    if change == "missing-final":
        (source / "final.txt").unlink()
    elif change == "changed-final":
        (source / "final.txt").write_text("modified after capture")
    elif change == "missing-artifacts":
        p = source / "result.json"
        r = json.loads(p.read_text())
        r.pop("artifacts")
        p.write_text(json.dumps(r))
    else:
        from skilltest.results import _directory_artifact

        folder = source / "workspace/fixture"
        folder.mkdir(parents=True)
        f = folder / "nested.txt"
        f.write_text("captured")
        p = source / "result.json"
        r = json.loads(p.read_text())
        r["artifacts"]["fixture"] = _directory_artifact(folder, source)
        p.write_text(json.dumps(r))
        f.write_text("changed")
    assert invoke(args) != 0
    assert not index.exists()


@pytest.mark.parametrize(
    "code", ["PROVIDER_TIMEOUT", "PROVIDER_EXIT_NONZERO", "PREPARATION_FAILED"]
)
def test_retain_rejects_cleanup_failure_independent_of_primary_error(
    retention_case, code
):
    _, source, _, index, args = retention_case
    p = source / "result.json"
    r = json.loads(p.read_text())
    r.update(
        status="INFRA_ERROR",
        infrastructure_error={"code": code, "message": "primary failure"},
    )
    r["execution"].update(
        cleanup_error="owned provider group remains",
        timed_out=code == "PROVIDER_TIMEOUT",
        invocation_started=code != "PREPARATION_FAILED",
        exit_code=None if code == "PREPARATION_FAILED" else -9,
    )
    p.write_text(json.dumps(r))
    assert invoke(args) != 0
    assert not index.exists()


@pytest.mark.parametrize(
    "state", ["legacy-complete", "legacy-failed", "missing-cleanup"]
)
def test_retention_cleanup_version_boundary(retention_case, state, capsys):
    _, source, _, index, args = retention_case
    p = source / "result.json"
    r = json.loads(p.read_text())
    r["execution"].pop("cleanup_error")
    if state.startswith("legacy"):
        r["schema_version"] = "0.4"
    if state == "legacy-failed":
        r.update(
            status="INFRA_ERROR",
            infrastructure_error={"code": "PROVIDER_TIMEOUT", "message": "timeout"},
        )
        r["execution"].update(timed_out=True, exit_code=-9)
    p.write_text(json.dumps(r))
    code = invoke(args)
    assert (code == 0) == (state == "legacy-complete")
    assert index.exists() == (state == "legacy-complete")
    if state == "legacy-failed":
        assert "cannot establish cleanup status" in capsys.readouterr().out
