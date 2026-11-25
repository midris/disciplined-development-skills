"""Reconstruct local reference variants; no providers or semantic auto-scoring.

Run from any directory. Fresh scratch output is retained for inspection and
never overwrites tracked qualification or case inputs. Reference judgments
come from the case author, not from the runtime observer.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from probe_behavior import observe

CASE = Path(__file__).resolve().parent
ROOT = CASE.parents[3]


def run(argv, cwd):
    # Inherited repository/index/config overrides must not redirect scratch Git operations.
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
               PYTHONDONTWRITEBYTECODE="1")
    result = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, timeout=30)
    if result.returncode:
        raise RuntimeError(f"{argv}: {result.returncode}\n{result.stdout}\n{result.stderr}")
    return result.stdout.strip()


def git(fixture, *args):
    return run(["git", "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false", *args], fixture)


def qualify():
    # Assertions below qualify the retained evidence; -O must not erase them.
    if not __debug__:
        raise RuntimeError("Local qualification requires Python assertions; remove -O/PYTHONOPTIMIZE.")
    scratch = Path(tempfile.mkdtemp(prefix="ssr-semantic-qualification-"))
    expected = json.loads((CASE / "expected.json").read_text())
    definitions = json.loads((CASE / "qualification-variants.json").read_text())
    report = {"scope": "Local runtime/input/constructed-reference qualification; model evaluator remains unqualified.",
              "scratch": str(scratch), "variants": [], "reference_judgments_source": "qualification-variants.json (orchestrator-authored)"}
    # Validate inventory before any reconstruction so stale controller inputs stop clearly.
    for ref in expected["references"]:
        text = (CASE / "fixture" / ref["path"]).read_text()
        assert text.count(ref["quote"]) == 1, ref["id"]
        assert text[:text.index(ref["quote"])].count("\n") + 1 == ref["original_line"], ref["id"]
    for definition in definitions["variants"]:
        fixture = scratch / definition["id"]
        shutil.copytree(CASE / "fixture", fixture)
        git(fixture, "init", "--template=", "-q")
        git(fixture, "config", "user.name", "Skill Study")
        git(fixture, "config", "user.email", "skill-study@example.invalid")
        git(fixture, "add", ".")
        git(fixture, "commit", "-q", "-m", "fixture baseline")
        baseline = git(fixture, "rev-parse", "HEAD")
        for edit in definition["edits"]:
            path = fixture / edit["path"]
            text = path.read_text()
            assert text.count(edit["old"]) == 1, (definition["id"], edit["path"])
            path.write_text(text.replace(edit["old"], edit["new"]))
        if definition["commit_repair"]:
            git(fixture, "add", ".")
            git(fixture, "commit", "-q", "-m", "Repair delivery guidance")
        facts = observe(fixture)
        assert facts["status"] == "observed", facts
        for name, want in expected["runtime"].items():
            assert {k: facts["probes"][name][k] for k in want} == want, (definition["id"], name)
        run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests"], fixture)
        committed = git(fixture, "diff", "--name-only", baseline, "HEAD").splitlines()
        uncommitted = git(fixture, "diff", "--name-only", "HEAD").splitlines()
        edited = sorted(e["path"] for e in definition["edits"])
        assert committed == (edited if definition["commit_repair"] else []), definition["id"]
        assert uncommitted == ([] if definition["commit_repair"] else edited), definition["id"]
        report["variants"].append({"id": definition["id"], "fixture": str(fixture),
            "runtime": facts, "subject_tests_exit": 0, "baseline": baseline,
            "head": git(fixture, "rev-parse", "HEAD"), "committed_paths": committed,
            "uncommitted_paths": uncommitted,
            "reference_judgments": definition["reference_judgments"],
            "rationale": definition["rationale"],
            "documents": {str(p.relative_to(fixture)): p.read_text() for p in sorted(fixture.rglob("*.md"))}})
    # Exercise the actual runner loader/copy functions, never its provider dispatch.
    sys.path.insert(0, str(ROOT / "skill-validation/runner/src"))
    from skilltest.config import load_config
    from skilltest.workspace import create_run, prepare_workspace
    pairs = {}
    prepared_paths = {}
    baseline_trees = {}
    for condition in ["control", "original"]:
        config = load_config(CASE / f"{condition}.json")
        context = create_run(config)
        prepared = prepare_workspace(context, config)
        hashes = {}
        for entry in config.fixtures:
            source, target = entry.source, context.fixture_dir / entry.target
            assert source.read_bytes() == target.read_bytes(), entry.target
            assert source.stat().st_mode & 0o777 == target.stat().st_mode & 0o777
            hashes[str(entry.target)] = hashlib.sha256(target.read_bytes()).hexdigest()
        assert b"{{" not in prepared.prompt_bytes
        git(context.fixture_dir, "init", "--template=", "-q")
        git(context.fixture_dir, "add", ".")
        tracked = git(context.fixture_dir, "ls-files").splitlines()
        assert len(tracked) == 9, tracked
        assert not any(p.startswith(".agents/") or p == "TASK.md" for p in tracked)
        baseline_trees[condition] = git(context.fixture_dir, "write-tree")
        pairs[condition] = hashes
        prepared_paths[condition] = str(context.fixture_dir)
    skill = ".agents/skills/sweeping-stale-references/SKILL.md"
    assert pairs["original"].keys() - pairs["control"].keys() == {skill}
    assert all(pairs["original"][key] == value for key, value in pairs["control"].items())
    load_line = "Read `.agents/skills/sweeping-stale-references/SKILL.md` completely and apply it when performing the development task below.\n\n"
    assert (CASE / "prompt-original.md").read_text() == load_line + (CASE / "prompt-control.md").read_text()
    assert baseline_trees["control"] == baseline_trees["original"]
    report["runner_preparation"] = {"entry_counts": {k: len(v) for k, v in pairs.items()},
        "only_extra_entry": skill, "common_bytes_and_modes_match": True, "baseline_trees": baseline_trees, "baseline_project_files": 9, "paths": prepared_paths,
        "prompt_difference": "Only the original-skill read instruction."}
    report["inputs"] = {str(p.relative_to(CASE)): hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in sorted(CASE.rglob("*")) if p.is_file() and ".git" not in p.parts
                        and "__pycache__" not in p.parts and p.name not in ("qualification.json", "manifest.json")}
    path = scratch / "qualification.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(path)


if __name__ == "__main__":
    qualify()
