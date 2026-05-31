"""Tests for install-skills.sh — the clone-and-symlink installer.

Each test builds an isolated fake "clone" (a copy of the script + stub skill
dirs) and a fake target project under tmp_path, then runs the installer and
asserts on the resulting symlinks. No network, no real skills.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_SRC = REPO_ROOT / "install-skills.sh"


def _make_clone(tmp_path: Path, skill_names=("alpha-skill", "beta-skill")) -> Path:
    clone = tmp_path / "clone"
    clone.mkdir()
    shutil.copy(SCRIPT_SRC, clone / "install-skills.sh")
    os.chmod(clone / "install-skills.sh", 0o755)
    for name in skill_names:
        (clone / name).mkdir()
        (clone / name / "SKILL.md").write_text(f"---\nname: {name}\n---\n# {name}\n")
    # a dir WITHOUT a SKILL.md — must be ignored
    (clone / "not-a-skill").mkdir()
    (clone / "not-a-skill" / "readme.txt").write_text("nope")
    # a stray file at clone root — must be ignored
    (clone / "README.md").write_text("# clone")
    return clone


def _run(clone: Path, target: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [str(clone / "install-skills.sh"), str(target)],
        capture_output=True, text=True,
    )


def test_creates_symlink_per_skill_dir(tmp_path):
    clone = _make_clone(tmp_path)
    target = tmp_path / "project"
    target.mkdir()
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    skills = target / ".claude" / "skills"
    for name in ("alpha-skill", "beta-skill"):
        link = skills / name
        assert link.is_symlink(), f"{name} not a symlink"
        assert link.resolve() == (clone / name).resolve()
    assert not (skills / "not-a-skill").exists()
    assert not (skills / "README.md").exists()


def test_creates_skills_dir_when_absent(tmp_path):
    clone = _make_clone(tmp_path)
    target = tmp_path / "project"
    target.mkdir()
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    assert (target / ".claude" / "skills").is_dir()


def test_idempotent_rerun(tmp_path):
    clone = _make_clone(tmp_path)
    target = tmp_path / "project"
    target.mkdir()
    _run(clone, target)
    skills = target / ".claude" / "skills"
    before = sorted(p.name for p in skills.iterdir())
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    after = sorted(p.name for p in skills.iterdir())
    assert before == after
    assert (skills / "alpha-skill").is_symlink()


def test_skips_preexisting_real_dir(tmp_path):
    clone = _make_clone(tmp_path)
    target = tmp_path / "project"
    skills = target / ".claude" / "skills"
    skills.mkdir(parents=True)
    (skills / "alpha-skill").mkdir()
    (skills / "alpha-skill" / "SKILL.md").write_text("local skill")
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    assert (skills / "alpha-skill").is_dir()
    assert not (skills / "alpha-skill").is_symlink()
    assert (skills / "alpha-skill" / "SKILL.md").read_text() == "local skill"
    assert (skills / "beta-skill").is_symlink()
    assert "alpha-skill" in (r.stdout + r.stderr)


def test_skips_symlink_to_different_target(tmp_path):
    clone = _make_clone(tmp_path)
    target = tmp_path / "project"
    skills = target / ".claude" / "skills"
    skills.mkdir(parents=True)
    other = tmp_path / "other"
    other.mkdir()
    (skills / "alpha-skill").symlink_to(other)
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    assert (skills / "alpha-skill").resolve() == other.resolve()
    assert "alpha-skill" in (r.stdout + r.stderr)
