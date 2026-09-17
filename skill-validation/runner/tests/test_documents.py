"""Contract tests for deterministic study-document operations (no providers)."""

import json
from pathlib import Path

import pytest

from skilltest.cli import main

FORMATS = Path(__file__).resolve().parents[3] / "skill-studies" / "formats"


@pytest.mark.parametrize(
    "kind,suffix",
    [
        ("protocol", "md"),
        ("case", "md"),
        ("assessment", "md"),
        ("manifest", "json"),
        ("index", "json"),
        ("result", "json"),
    ],
)
def test_generated_draft_checks_structurally_without_claiming_completion(tmp_path, capsys, kind, suffix):
    path = tmp_path / f"{kind}.{suffix}"
    assert main(["docs", "new", kind, "--output", str(path), "--format-version", "1"]) == 0
    capsys.readouterr()
    assert main(["docs", "check", str(path), "--json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["structurally_valid"] is True
    assert report["complete"] is False
    assert report["diagnostics"]
    original = path.read_bytes()
    assert main(["docs", "new", kind, "--output", str(path)]) == 1
    assert path.read_bytes() == original


def test_missing_required_section_and_unknown_version_are_distinct(tmp_path, capsys):
    path = tmp_path / "protocol.md"
    path.write_text(
        (FORMATS / "protocol.template.md")
        .read_text()
        .replace("## Sources and intended use", "## Unrecognised")
    )
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == "required-section" for d in json.loads(capsys.readouterr().out)["diagnostics"])
    path.write_text((FORMATS / "protocol.template.md").read_text().replace("`1`", "`99`", 1))
    assert main(["docs", "check", str(path), "--json"]) == 2
    assert any(d["rule"] == "unsupported-version" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.parametrize("mutation", ["missing-field", "wrong-type", "wrong-enum", "duplicate-id"])
def test_manifest_structure_rejects_broken_fields(tmp_path, capsys, mutation):
    value = json.loads((FORMATS / "manifest.template.json").read_text())
    if mutation == "missing-field":
        del value["conditions"]
    elif mutation == "wrong-type":
        value["conditions"] = "original"
    elif mutation == "wrong-enum":
        value["status"] = "approved"
    else:
        value["conditions"][0]["id"] = "original"
        value["conditions"].append(value["conditions"][0])
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(value))
    assert main(["docs", "check", str(path), "--json"]) == 1
    report = json.loads(capsys.readouterr().out)
    assert report["structurally_valid"] is False
    assert any(d["location"] for d in report["diagnostics"])


def test_readiness_requires_protocol_and_drafts_cannot_pass(tmp_path, capsys):
    case = tmp_path / "case.md"
    case.write_text((FORMATS / "case-definition.template.md").read_text())
    assert main(["docs", "check", str(case), "--ready-for", "collection", "--json"]) == 2
    capsys.readouterr()
    protocol = tmp_path / "protocol.md"
    protocol.write_text((FORMATS / "protocol.template.md").read_text())
    assert main(["docs", "check", str(protocol), "--ready-for", "collection", "--json"]) == 1
    assert json.loads(capsys.readouterr().out)["complete"] is False


def test_invalid_json_duplicate_keys_and_nonfinite_numbers_report_failure(tmp_path, capsys):
    path = tmp_path / "x.json"
    for raw in [
        "{",
        '{"format_version":"1","format_version":"2"}',
        '{"format_version":"1","value":NaN}',
    ]:
        path.write_text(raw)
        assert main(["docs", "check", str(path), "--json"]) == 1
        assert json.loads(capsys.readouterr().out)["diagnostics"][0]["rule"] == "invalid-document"


ROOT = FORMATS.parents[1]
STUDY = ROOT / "skill-studies/sweeping-stale-references"


@pytest.mark.process_smoke
def test_manifest_pins_survive_changed_working_files_and_reject_wrong_hash(tmp_path, capsys, monkeypatch):
    import hashlib, subprocess
    from skilltest.documents.references import Context
    from skilltest.documents import Report

    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    source = tmp_path / "source.txt"
    source.write_text("original")
    subprocess.run(["git", "-C", str(tmp_path), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(tmp_path),
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.test",
            "commit",
            "-qm",
            "fixture",
        ],
        check=True,
    )
    rev = subprocess.check_output(["git", "-C", str(tmp_path), "rev-parse", "HEAD"], text=True).strip()
    source.write_text("changed")
    ctx = Context(tmp_path / "manifest.json", Report())
    identity = {
        "path": "source.txt",
        "sha256": hashlib.sha256(b"original").hexdigest(),
        "version": None,
        "git_revision": rev,
    }
    assert ctx.read(identity) == b"original"
    identity["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="hash"):
        ctx.read(identity)
    identity["path"] = "../outside"
    with pytest.raises(ValueError, match="canonical"):
        ctx.read(identity)


@pytest.mark.process_smoke
def test_complete_manifest_and_results_verify_through_their_pins(document_study, capsys):
    root, _, _, _ = document_study
    for name in ["case/manifest.json", "results/1.json"]:
        assert main(["docs", "check", str(root / name), "--json"]) == 0
        assert json.loads(capsys.readouterr().out)["complete"] is True


@pytest.mark.parametrize(
    "mutation,rule",
    [
        ("missing-criterion", "criterion-coverage"),
        ("unknown-evidence", "evidence-id"),
        ("wrong-hash", "reference"),
        ("wrong-dimension", "criterion-dimension"),
        ("wrong-condition", "condition"),
    ],
)
@pytest.mark.process_smoke
def test_result_rejects_cross_record_errors(document_study, tmp_path, capsys, monkeypatch, mutation, rule):
    root, _, _, _ = document_study
    monkeypatch.chdir(root)
    source = root / "results/1.json"
    value = json.loads(source.read_text())
    if mutation == "missing-criterion":
        value["criteria"][0]["id"] = "different"
    elif mutation == "unknown-evidence":
        value["criteria"][0]["evidence"] = ["absent"]
    elif mutation == "wrong-hash":
        value["manifest"]["sha256"] = "0" * 64
    elif mutation == "wrong-dimension":
        value["criteria"][-1]["dimension"] = "procedural"
    else:
        value["condition"] = "candidate"
    if mutation == "wrong-dimension":
        value["criteria"].append({**value["criteria"][0], "id": "extra", "dimension": "functional"})
    path = tmp_path / "result.json"
    path.write_text(json.dumps(value))
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == rule for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_manifest_rejects_extra_subject_source_and_controller_overlap(
    document_study, tmp_path, capsys, monkeypatch
):
    root, _, _, _ = document_study
    monkeypatch.chdir(root)
    value = json.loads((root / "case/manifest.json").read_text())
    value["subject_sources"].append(value["authorities"]["policy"])
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(value))
    assert main(["docs", "check", str(path), "--json"]) == 1
    rules = {d["rule"] for d in json.loads(capsys.readouterr().out)["diagnostics"]}
    assert "subject-membership" in rules and "controller-overlap" in rules


def test_missing_link_and_criterion_field_are_not_complete(tmp_path, capsys):
    path = tmp_path / "case.md"
    path.write_text(
        (STUDY / "cases/moved-guide/assessment.md").read_text().replace("Overlap:", "Removed:", 1)
    )
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == "required-field" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.fixture
def document_study(tmp_path):
    """A two-attempt study in real Git; raw evidence is disposable, never a model run."""
    import hashlib, re, subprocess, stat

    root = tmp_path / "repo"
    root.mkdir()

    def git(*args):
        return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()

    git("init", "-q")
    # Fixture commits must not leave background Git maintenance racing read-only assertions.
    git("config", "gc.auto", "0")
    git("config", "maintenance.auto", "false")
    git("config", "user.name", "Fixture")
    git("config", "user.email", "fixture@example.test")

    def write(name, value):
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(value, indent=2) if isinstance(value, dict) else value)
        return p

    def commit():
        git("add", ".")
        git("commit", "-qm", "fixture")
        return git("rev-parse", "HEAD")

    def ident(name, revision=None):
        raw = (root / name).read_bytes()
        return {
            "path": name,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "version": "1",
            **({"git_revision": revision} if revision else {}),
        }

    fill = lambda text: re.sub(r"<[^>\n]+>", "example", text)
    protocol = fill((FORMATS / "protocol.template.md").read_text()).replace(
        "Status: draft", "Status: prepared"
    )
    scope = """### Batch: example
Status: owner-approved; authority recorded in this protocol.
Scope: exactly the two executions below.
Acceptance/inclusion: descriptive-only. Include all valid-setup executions regardless of outcome; retain unknowns. No automatic retry or replacement.
| Order | Case | Condition | Repetition | CONFIG |
|---:|---|---|---:|---|
| 1 | example | original | 1 | `case/original.json` |
| 2 | example | original | 2 | `case/original.json` |
Input identities: [manifest](case/manifest.json).
Attempt index: [index](example-run-index.json).
Assessment: [assessment](example-assessment.md).
"""
    protocol = protocol.replace("## Storage and accounting", scope + "\n## Storage and accounting")
    protocol = protocol.replace("Plan: example", "Plan: [plan](plan.md)")
    protocol += """
**Current accounting: 10 active minutes booked; 90 minutes remain under the 100-minute ceiling.**
Dispatched calls are **2 subject, 0 evaluator, 0 authoring, 0 retry**; remaining outer capacity is **2 / 2 / 1 / 1**.
| Work | Estimate | Basis |
|---|---:|---|
| Tooling | 20 | Fixture |
| Closure | 10 | Fixture |
| **Total** | **30** | Fixture |
"""
    write(
        "plan.md",
        "Accepted outer limits: 4 subject, 2 evaluator, 1 authoring and 1 retry invocations.",
    )
    write("protocol.md", protocol)
    write("spec.md", "Fixture spec")
    write("policy.txt", "Fixture policy")
    write("formats.md", "Fixture contract")
    write("schema.json", (FORMATS / "execution-result.schema.json").read_text())
    card = (
        fill((FORMATS / "case-definition.template.md").read_text())
        .replace("Definition version: example", "Definition version: 1")
        .replace("### example: example", "### F1: Outcome")
        .replace("Dimension: example", "Dimension: functional")
        .replace("Applies to: example", "Applies to: `original`")
    )
    write("case/assessment.md", card.replace("Status: draft", "Status: prepared"))
    write("case/prompt.md", "Do the fixture task")
    write("case/input.txt", "Fixture input")
    config = {
        "schema_version": "0.2",
        "id": "example-original",
        "prompt": "prompt.md",
        "fixtures": [{"source": "input.txt", "target": "input.txt"}],
        "execution": {"provider": "codex", "model": "fixture", "effort": "low"},
    }
    write("case/original.json", config)
    rev = commit()
    manifest = {
        "format_version": "1",
        "manifest_id": "example",
        "study_id": "example",
        "case_id": "example",
        "status": "frozen",
        "created_at": "2026-09-16",
        "source_revision": rev,
        "authorities": {
            k: ident(v)
            for k, v in {
                "spec": "spec.md",
                "protocol": "protocol.md",
                "format_contract": "formats.md",
                "execution_result_schema": "schema.json",
                "policy": "policy.txt",
            }.items()
        },
        "conditions": [
            {
                "id": "original",
                "configuration": {**ident("case/original.json"), "version": "0.2"},
                "target_skill": None,
            }
        ],
        "subject_sources": [ident("case/prompt.md"), ident("case/input.txt")],
        "controller_only": [],
    }
    manifest["authorities"]["criteria"] = [ident("case/assessment.md")]
    write("case/manifest.json", manifest)
    mrev = commit()
    mi = ident("case/manifest.json", mrev)
    attempts = []
    for n, judgment in [(1, "met"), (2, "not met")]:
        bundle = tmp_path / f"bundle-{n}"
        bundle.mkdir()
        (bundle / "config.json").write_text(json.dumps(config))
        (bundle / "final.txt").write_text(f"Fixture result {n}")
        (bundle / "result.json").write_text(
            json.dumps(
                {
                    "run_id": f"run-{n}",
                    "test": {"id": "example-original"},
                    "schema_version": "0.4",
                    "execution": {"invocation_started": True},
                }
            )
        )
        entries = [
            {
                "path": p.name,
                "type": "file",
                "mode": oct(stat.S_IMODE(p.stat().st_mode)),
                "bytes": p.stat().st_size,
                "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            }
            for p in bundle.iterdir()
        ]
        inv = tmp_path / f"inventory-{n}.json"
        inv.write_text(json.dumps({"format_version": "1", "bundle": str(bundle), "entries": entries}))
        eid = {
            "path": str(bundle / "final.txt"),
            "sha256": hashlib.sha256((bundle / "final.txt").read_bytes()).hexdigest(),
            "version": None,
        }
        result = {
            "schema_version": "1",
            "record_kind": "execution result",
            "result_id": f"result-{n}",
            "assessed_at": "2026-09-16",
            "run_id": f"run-{n}",
            "condition": "original",
            "manifest": mi,
            "assessor": {
                "name": "Fixture",
                "method": "human",
                "model": None,
                "session_id": None,
                "context": "Synthetic structural fixture",
            },
            "evidence": [{"id": "output", "artifact": eid, "selector": "whole file"}],
            "setup": {
                "status": "valid",
                "reason": "Synthetic usable setup",
                "evidence": ["output"],
            },
            "criteria": [
                {
                    "id": "F1",
                    "dimension": "functional",
                    "judgment": judgment,
                    "reason": "Synthetic outcome",
                    "consequence": "Outcome applies",
                    "evidence": ["output"],
                }
            ],
            "functional_result": judgment,
            "procedural_summary": "Not applicable",
            "observations": [],
            "uncertainty": [],
        }
        write(f"results/{n}.json", result)
        attempts.append(
            {
                "attempt_id": f"attempt-{n}",
                "case_id": "example",
                "condition": "original",
                "repetition": n,
                "attempt_number": 1,
                "retry_of": None,
                "manifest": mi,
                "authorization": {
                    "artifact": ident("protocol.md", rev),
                    "selector": "Batch: example",
                },
                "run_id": f"run-{n}",
                "allocation": {"pool": "subject", "charge": 1},
                "bundle": {
                    "path": str(bundle),
                    "inventory": {
                        "path": str(inv),
                        "sha256": hashlib.sha256(inv.read_bytes()).hexdigest(),
                        "version": "1",
                    },
                    "verified": True,
                },
                "result": None,
                "limitations": [],
            }
        )
    rrev = commit()
    for n, a in enumerate(attempts, 1):
        a["result"] = {
            "result_id": f"result-{n}",
            "record": ident(f"results/{n}.json", rrev),
        }
    write(
        "example-run-index.json",
        {
            "format_version": "1",
            "index_id": "example",
            "study_id": "example",
            "batch_id": "example",
            "attempts": attempts,
        },
    )
    irev = commit()
    assessment = f"""# Example: assessment
Format version: `1`
Assessment ID: `example`
Study / batch: `example` / `example`
Status: assessed
Scope and acceptance rules: [protocol](protocol.md#batch-example) at Git `{rev}`.
Attempt index: [index](example-run-index.json) at Git `{irev}`, SHA-256 `{ident("example-run-index.json")["sha256"]}`.
Assessor: Human; synthetic fixture.
## Coverage and execution results
| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
|---|---:|---:|---:|---:|---:|---:|
| example / original | 2 | 2 | 2 | 0 | 0 | 0 |
## Aggregate results
| Case / condition / criterion | Met | Not met | Insufficient evidence | Evidence |
|---|---:|---:|---:|---|
| example / original / F1 | 1 | 1 | 0 | result-1, result-2 |
| example / original / functional outcome | 1 | 1 | 0 | result-1, result-2 |
Acceptance: descriptive-only. No semantic claim from this structural fixture.
"""
    write("example-assessment.md", assessment)
    return root, write, commit, ident


@pytest.mark.process_smoke
def test_batch_readiness_uses_declared_scope_and_reconciles_counts(document_study, capsys):
    root, _, _, _ = document_study
    for stage in ["collection", "assessment"]:
        assert (
            main(
                [
                    "docs",
                    "check",
                    str(root / "protocol.md"),
                    "--ready-for",
                    stage,
                    "--batch",
                    "example",
                    "--json",
                ]
            )
            == 0
        )
        assert json.loads(capsys.readouterr().out)["complete"] is True
    path = root / "example-assessment.md"
    path.write_text(path.read_text().replace("| 1 | 1 | 0 |", "| 2 | 0 | 0 |", 1))
    assert (
        main(
            [
                "docs",
                "check",
                str(root / "protocol.md"),
                "--ready-for",
                "assessment",
                "--batch",
                "example",
                "--json",
            ]
        )
        == 1
    )
    assert any(d["rule"] == "aggregate" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
@pytest.mark.parametrize(
    "mutation,rule",
    [
        ("missing-result", "unfinished"),
        ("duplicate-attempt", "duplicate-id"),
        ("wrong-charge", "allocation"),
        ("missing-bundle", "reference"),
        ("wrong-run", "run-identity"),
        ("extra-inventory-file", "inventory-coverage"),
    ],
)
def test_index_rejects_attempt_and_evidence_errors(document_study, capsys, mutation, rule):
    root, write, _, _ = document_study
    value = json.loads((root / "example-run-index.json").read_text())
    attempt = value["attempts"][0]
    if mutation == "missing-result":
        attempt["result"] = None
    elif mutation == "duplicate-attempt":
        value["attempts"].append(attempt)
    elif mutation == "wrong-charge":
        attempt["allocation"]["charge"] = 0
    elif mutation == "missing-bundle":
        attempt["bundle"]["path"] += "/missing"
    elif mutation == "wrong-run":
        attempt["run_id"] = "wrong"
    else:
        (Path(attempt["bundle"]["path"]) / "extra").write_text("unaccounted")
    write("example-run-index.json", value)
    code = main(["docs", "check", str(root / "example-run-index.json"), "--json"])
    report = json.loads(capsys.readouterr().out)
    if mutation == "missing-result":
        assert code == 0 and report["complete"] is False
    else:
        assert code == 1
    assert any(d["rule"] == rule for d in report["diagnostics"])


@pytest.mark.process_smoke
def test_literal_inline_examples_do_not_make_completed_protocol_unfinished(document_study, capsys):
    root, _, _, _ = document_study
    path = root / "protocol.md"
    path.write_text(
        path.read_text() + "\nStore results as `results/<run-id>.json`; report `n/a — <reason>`.\n"
    )
    assert (
        main(
            [
                "docs",
                "check",
                str(path),
                "--ready-for",
                "assessment",
                "--batch",
                "example",
                "--json",
            ]
        )
        == 0
    )
    assert json.loads(capsys.readouterr().out)["complete"] is True


@pytest.mark.process_smoke
def test_working_links_and_current_collection_bytes_are_checked(document_study, capsys):
    root, _, _, _ = document_study
    p = root / "case/assessment.md"
    p.write_text(p.read_text() + "\nSee [missing](absent.md).\n")
    assert main(["docs", "check", str(p), "--json"]) == 1
    assert any(d["rule"] == "link" for d in json.loads(capsys.readouterr().out)["diagnostics"])
    (root / "case/input.txt").write_text("changed since freeze")
    assert (
        main(
            [
                "docs",
                "check",
                str(root / "protocol.md"),
                "--ready-for",
                "collection",
                "--json",
            ]
        )
        == 1
    )
    assert any(d["rule"] == "working-input" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_malformed_pinned_result_is_a_diagnostic_not_a_crash(document_study, capsys):
    root, write, commit, ident = document_study
    result = json.loads((root / "results/1.json").read_text())
    result["criteria"] = "not an array"
    write("results/1.json", result)
    rev = commit()
    idx = json.loads((root / "example-run-index.json").read_text())
    idx["attempts"][0]["result"]["record"] = ident("results/1.json", rev)
    write("example-run-index.json", idx)
    assert main(["docs", "check", str(root / "example-run-index.json"), "--json"]) == 1
    assert any(d["rule"] == "schema" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_scope_and_assessment_batch_cannot_be_silently_mixed(document_study, capsys):
    root, _, _, _ = document_study
    path = root / "protocol.md"
    path.write_text(path.read_text().replace("### Batch: example", "### Batch: different"))
    assert (
        main(
            [
                "docs",
                "check",
                str(path),
                "--ready-for",
                "assessment",
                "--batch",
                "different",
                "--json",
            ]
        )
        == 1
    )
    assert any(d["rule"] == "batch-identity" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_collection_reports_unsupported_inclusion_policy(document_study, capsys):
    root, _, _, _ = document_study
    path = root / "protocol.md"
    path.write_text(
        path.read_text().replace("Include all valid-setup executions", "Include only successful executions")
    )
    assert main(["docs", "check", str(path), "--ready-for", "collection", "--json"]) == 2
    assert any(
        d["rule"] == "unsupported-inclusion" for d in json.loads(capsys.readouterr().out)["diagnostics"]
    )


@pytest.mark.process_smoke
@pytest.mark.parametrize(
    "mutation,rule",
    [("time", "accounting"), ("forecast", "accounting"), ("calls", "allocation-total")],
)
def test_protocol_accounting_reconciles_declared_numbers(document_study, capsys, mutation, rule):
    root, _, _, _ = document_study
    p = root / "protocol.md"
    text = p.read_text()
    if mutation == "time":
        text = text.replace("10 active minutes booked", "11 active minutes booked")
    elif mutation == "forecast":
        text = text.replace("| **Total** | **30**", "| **Total** | **31**")
    else:
        text = text.replace("**2 subject, 0 evaluator", "**1 subject, 0 evaluator")
    p.write_text(text)
    assert main(["docs", "check", str(p), "--ready-for", "assessment", "--json"]) == 1
    assert any(d["rule"] == rule for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_missing_pin_is_not_replaced_by_current_working_file(document_study, capsys):
    root, write, _, _ = document_study
    result = json.loads((root / "results/1.json").read_text())
    del result["manifest"]["git_revision"]
    write("results/1.json", result)
    assert main(["docs", "check", str(root / "results/1.json"), "--json"]) == 1
    assert any(d["rule"] == "reference" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_missing_aggregate_row_unknown_outcome_and_bad_coverage_are_rejected(document_study, capsys):
    root, write, commit, ident = document_study
    path = root / "example-assessment.md"
    original = path.read_text()
    path.write_text(original.replace("| example / original / F1 | 1 | 1 | 0 | result-1, result-2 |\n", ""))
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == "criterion-coverage" for d in json.loads(capsys.readouterr().out)["diagnostics"])
    path.write_text(original.replace("| 2 | 2 | 2 | 0 | 0 | 0 |", "| 2 | 2 | 1 | 0 | 1 | 0 |"))
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == "coverage" for d in json.loads(capsys.readouterr().out)["diagnostics"])
    path.write_text(original)
    result = json.loads((root / "results/2.json").read_text())
    result["criteria"][0]["judgment"] = "insufficient evidence"
    result["functional_result"] = "insufficient evidence"
    write("results/2.json", result)
    rev = commit()
    idx = json.loads((root / "example-run-index.json").read_text())
    idx["attempts"][1]["result"]["record"] = ident("results/2.json", rev)
    write("example-run-index.json", idx)
    irev = commit()
    import re

    text = re.sub(r"(Attempt index: .*?Git `)[0-9a-f]{40}", lambda m: m[1] + irev, original)
    text = re.sub(
        r"(SHA-256 `)[0-9a-f]{64}",
        lambda m: m[1] + ident("example-run-index.json")["sha256"],
        text,
    )
    path.write_text(text)
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == "aggregate" for d in json.loads(capsys.readouterr().out)["diagnostics"])
    path.write_text(text.replace("| 1 | 1 | 0 |", "| 1 | 0 | 1 |"))
    assert main(["docs", "check", str(path), "--json"]) == 0
    capsys.readouterr()


@pytest.mark.process_smoke
def test_missing_attempt_must_remain_visible_in_coverage(document_study, capsys):
    root, write, commit, ident = document_study
    idx = json.loads((root / "example-run-index.json").read_text())
    idx["attempts"].pop()
    write("example-run-index.json", idx)
    rev = commit()
    path = root / "example-assessment.md"
    text = path.read_text()
    import re

    text = re.sub(r"(Attempt index: .*?Git `)[0-9a-f]{40}", lambda m: m[1] + rev, text)
    text = re.sub(
        r"(SHA-256 `)[0-9a-f]{64}",
        lambda m: m[1] + ident("example-run-index.json")["sha256"],
        text,
    )
    text = text.replace("| 1 | 1 | 0 |", "| 1 | 0 | 0 |")
    path.write_text(text)
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == "coverage" for d in json.loads(capsys.readouterr().out)["diagnostics"])
    path.write_text(
        text.replace("| 2 | 2 | 2 | 0 | 0 | 0 |", "| 2 | 1 | 1 | 0 | 0 | 1 |").replace(
            "result-1, result-2", "result-1"
        )
    )
    assert main(["docs", "check", str(path), "--json"]) == 0
    capsys.readouterr()


def test_historical_unknown_format_is_reported_unsupported(tmp_path, capsys):
    p = tmp_path / "historical.json"
    p.write_text('{"schema_version":"1-draft","assessment_id":"old"}')
    assert main(["docs", "check", str(p), "--json"]) == 2
    assert any(d["rule"] == "unsupported-version" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_historical_pilot_accounting_is_explicit_without_format_migration(document_study, capsys):
    root, write, _, _ = document_study
    write(
        "pilot-run-index.json",
        {
            "phase": "process-pilot",
            "attempts": [{"run_id": "legacy-1", "execution": {"invocation_started": True}}],
        },
    )
    p = root / "protocol.md"
    p.write_text(
        p.read_text()
        .replace("**2 subject, 0 evaluator", "**3 subject, 0 evaluator")
        .replace("**2 / 2 / 1 / 1**", "**1 / 2 / 1 / 1**")
        + "\n[Historical accounting](pilot-run-index.json)\n"
    )
    assert main(["docs", "check", str(p), "--ready-for", "assessment", "--json"]) == 0
    assert any(
        d["rule"] == "historical-accounting" and d["severity"] == "info"
        for d in json.loads(capsys.readouterr().out)["diagnostics"]
    )


@pytest.mark.process_smoke
def test_runtime_strata_counts_and_partition_are_verified(document_study, capsys):
    root, _, _, _ = document_study
    path = root / "example-assessment.md"
    text = path.read_text()
    text = text.replace(
        "## Aggregate results",
        "## Aggregate results\nEarlier PATH includes orders 1–1. Runtime-1 includes orders 2–2.",
    )
    text = text.replace(
        "| Met | Not met | Insufficient evidence | Evidence |",
        "| Combined M/N/U | Earlier PATH M/N/U | Runtime-1 M/N/U | Evidence |",
    )
    text = text.replace("| 1 | 1 | 0 |", "| 1 / 1 / 0 | 1 / 0 / 0 | 0 / 1 / 0 |")
    path.write_text(text)
    assert main(["docs", "check", str(path), "--json"]) == 0
    capsys.readouterr()
    path.write_text(text.replace("0 / 1 / 0", "1 / 0 / 0", 1))
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == "aggregate" for d in json.loads(capsys.readouterr().out)["diagnostics"])
    # Even internally consistent columns cannot silently omit a valid execution.
    path.write_text(text.replace("orders 2–2", "orders 3–3").replace("0 / 1 / 0", "0 / 0 / 0"))
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == "strata-coverage" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_doc_cli_cannot_execute_commands_embedded_in_markdown(document_study, tmp_path):
    import subprocess, sys

    root, _, _, _ = document_study
    marker = tmp_path / "must-not-exist"
    path = root / "protocol.md"
    path.write_text(path.read_text() + f"\n```sh\ntouch {marker}\n```\n")
    before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    command = Path(sys.executable).with_name("skilltest")
    run = subprocess.run(
        [str(command), "docs", "check", str(path), "--ready-for", "assessment", "--json"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    assert not marker.exists()
    assert before == {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}


@pytest.mark.process_smoke
def test_explicit_draft_or_empty_required_metadata_never_passes_readiness(document_study, capsys):
    root, _, _, _ = document_study
    path = root / "protocol.md"
    original = path.read_text()
    for text in [
        original.replace("Status: prepared", "Status: draft"),
        original.replace("Study ID: example", "Study ID:"),
    ]:
        path.write_text(text)
        assert main(["docs", "check", str(path), "--json"]) == 0
        assert json.loads(capsys.readouterr().out)["complete"] is False
        assert main(["docs", "check", str(path), "--ready-for", "collection", "--json"]) == 1
        capsys.readouterr()


@pytest.mark.process_smoke
def test_aggregate_evidence_cannot_name_an_unrelated_result(document_study, capsys):
    root, _, _, _ = document_study
    path = root / "example-assessment.md"
    path.write_text(path.read_text().replace("result-1, result-2", "result-1, nonexistent", 1))
    assert main(["docs", "check", str(path), "--json"]) == 1
    assert any(d["rule"] == "aggregate-evidence" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_readiness_checks_the_assessments_scope_pin(document_study, capsys):
    root, _, _, _ = document_study
    path = root / "example-assessment.md"
    import re

    path.write_text(
        re.sub(
            r"(Scope and acceptance rules: .*?Git `)[0-9a-f]{40}", lambda m: m[1] + "0" * 40, path.read_text()
        )
    )
    assert main(["docs", "check", str(root / "protocol.md"), "--ready-for", "assessment", "--json"]) != 0
    assert json.loads(capsys.readouterr().out)["diagnostics"]


@pytest.mark.process_smoke
def test_current_batch_cannot_hide_a_new_attempt_behind_an_old_index_pin(document_study, capsys):
    from copy import deepcopy

    root, write, _, _ = document_study
    value = json.loads((root / "example-run-index.json").read_text())
    extra = deepcopy(value["attempts"][1])
    extra["attempt_id"] = "attempt-3"
    extra["run_id"] = "run-3"
    extra["repetition"] = 3
    value["attempts"].append(extra)
    write("example-run-index.json", value)
    path = root / "protocol.md"
    path.write_text(
        path.read_text()
        .replace("**2 subject, 0 evaluator", "**3 subject, 0 evaluator")
        .replace("**2 / 2 / 1 / 1**", "**1 / 2 / 1 / 1**")
    )
    assert main(["docs", "check", str(path), "--ready-for", "assessment", "--json"]) == 1
    assert any(d["rule"] == "attempt-coverage" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_declared_document_version_must_match_retrieved_bytes(document_study, capsys):
    root, write, _, _ = document_study
    value = json.loads((root / "results/1.json").read_text())
    value["manifest"]["version"] = "99"
    write("results/1.json", value)
    assert main(["docs", "check", str(root / "results/1.json"), "--json"]) == 1
    assert any(d["rule"] == "reference-version" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_manifest_date_must_be_iso_date_or_datetime(document_study, capsys):
    root, write, _, _ = document_study
    value = json.loads((root / "case/manifest.json").read_text())
    value["created_at"] = "sometime"
    write("case/manifest.json", value)
    assert main(["docs", "check", str(root / "case/manifest.json"), "--json"]) == 1
    assert any(d["rule"] == "date" for d in json.loads(capsys.readouterr().out)["diagnostics"])


@pytest.mark.process_smoke
def test_runtime_orders_remain_planned_orders_when_an_earlier_attempt_is_missing(document_study, capsys):
    import re

    root, write, commit, ident = document_study
    index = json.loads((root / "example-run-index.json").read_text())
    index["attempts"].pop(0)
    write("example-run-index.json", index)
    revision = commit()
    path = root / "example-assessment.md"
    text = re.sub(r"(Attempt index: .*?Git `)[0-9a-f]{40}", lambda m: m[1] + revision, path.read_text())
    text = re.sub(
        r"(SHA-256 `)[0-9a-f]{64}", lambda m: m[1] + ident("example-run-index.json")["sha256"], text
    )
    text = text.replace("| 2 | 2 | 2 | 0 | 0 | 0 |", "| 2 | 1 | 1 | 0 | 0 | 1 |")
    text = text.replace("result-1, result-2", "result-2")
    text = text.replace(
        "## Aggregate results",
        "## Aggregate results\nEarlier PATH includes orders 1–1. Runtime-1 includes orders 2–2.",
    )
    text = text.replace(
        "| Met | Not met | Insufficient evidence | Evidence |",
        "| Combined M/N/U | Earlier PATH M/N/U | Runtime-1 M/N/U | Evidence |",
    )
    text = text.replace("| 1 | 1 | 0 | result-2", "| 0 / 1 / 0 | 0 / 0 / 0 | 0 / 1 / 0 | result-2")
    path.write_text(text)
    assert main(["docs", "check", str(path), "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["complete"]


@pytest.mark.parametrize("mutation", ["object-id", "array-config"])
@pytest.mark.process_smoke
def test_wrong_json_types_report_diagnostics_without_tracebacks(document_study, capsys, mutation):
    root, write, commit, ident = document_study
    manifest = json.loads((root / "case/manifest.json").read_text())
    if mutation == "object-id":
        manifest["conditions"][0]["id"] = {"wrong": "type"}
    else:
        (root / "case/original.json").write_text("[]")
        revision = commit()
        manifest["conditions"][0]["configuration"] = {
            **ident("case/original.json", revision),
            "version": "0.2",
        }
    write("case/manifest.json", manifest)
    assert main(["docs", "check", str(root / "case/manifest.json"), "--json"]) == 1
    assert json.loads(capsys.readouterr().out)["diagnostics"]
