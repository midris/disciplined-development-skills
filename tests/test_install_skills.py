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
    skills_dir = clone / "skills"
    skills_dir.mkdir()
    for name in skill_names:
        (skills_dir / name).mkdir()
        (skills_dir / name / "SKILL.md").write_text(f"---\nname: {name}\n---\n# {name}\n")
    # a dir WITHOUT a SKILL.md under skills/ — must be ignored
    (skills_dir / "not-a-skill").mkdir()
    (skills_dir / "not-a-skill" / "readme.txt").write_text("nope")
    # a stray file under skills/ — must be ignored
    (skills_dir / "README.md").write_text("# clone")
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
        assert link.resolve() == (clone / "skills" / name).resolve()
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


# ---------------------------------------------------------------------------
# Command-file symlink tests
# The installer globs every commands/*.md (no single hardcoded command). These
# tests seed an ARBITRARY command name into the clone so the assertions exercise
# the generic glob, not a dd-review-specific path. _make_clone seeds no
# commands/ by default; the seeder below adds one.
# ---------------------------------------------------------------------------

def _add_command_src(clone: Path, name: str = "generic-cmd.md") -> Path:
    """Seed commands/<name> into a test clone (arbitrary, non-dd-review name)."""
    cmd_src = clone / "commands"
    cmd_src.mkdir(parents=True, exist_ok=True)
    src_file = cmd_src / name
    src_file.write_text(f"---\ndescription: {name} command template\n---\n")
    return src_file


def test_command_symlink_created_and_resolves(tmp_path):
    clone = _make_clone(tmp_path)
    _add_command_src(clone)
    target = tmp_path / "project"
    target.mkdir()
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    dest = target / ".claude" / "commands" / "generic-cmd.md"
    assert dest.is_symlink(), "generic-cmd.md not a symlink"
    expected_src = clone / "commands" / "generic-cmd.md"
    assert dest.resolve() == expected_src.resolve()


def test_command_symlinks_every_command_in_glob(tmp_path):
    """The installer mirrors the skill loop: a glob over commands/*.md, so
    multiple command files each get their own symlink."""
    clone = _make_clone(tmp_path)
    _add_command_src(clone, "alpha-cmd.md")
    _add_command_src(clone, "beta-cmd.md")
    target = tmp_path / "project"
    target.mkdir()
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    commands = target / ".claude" / "commands"
    for name in ("alpha-cmd.md", "beta-cmd.md"):
        dest = commands / name
        assert dest.is_symlink(), f"{name} not a symlink"
        assert dest.resolve() == (clone / "commands" / name).resolve()


def test_no_commands_dir_is_noop(tmp_path):
    """Zero commands/*.md (no commands/ dir at all) must not error — a literal
    unmatched glob is skipped, mirroring the skill loop's guard."""
    clone = _make_clone(tmp_path)  # no _add_command_src -> no commands/ dir
    target = tmp_path / "project"
    target.mkdir()
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    assert not (target / ".claude" / "commands" / "generic-cmd.md").exists()


def test_command_symlink_idempotent(tmp_path):
    clone = _make_clone(tmp_path)
    _add_command_src(clone)
    target = tmp_path / "project"
    target.mkdir()
    _run(clone, target)
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    dest = target / ".claude" / "commands" / "generic-cmd.md"
    assert dest.is_symlink()
    # idempotent: still resolves to the same source
    expected_src = clone / "commands" / "generic-cmd.md"
    assert dest.resolve() == expected_src.resolve()


def test_command_real_file_not_clobbered(tmp_path):
    clone = _make_clone(tmp_path)
    _add_command_src(clone)
    target = tmp_path / "project"
    commands_dir = target / ".claude" / "commands"
    commands_dir.mkdir(parents=True)
    dest = commands_dir / "generic-cmd.md"
    dest.write_text("custom consumer content")
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    assert not dest.is_symlink(), "real file was replaced by a symlink"
    assert dest.read_text() == "custom consumer content"


def test_command_foreign_symlink_not_clobbered(tmp_path):
    clone = _make_clone(tmp_path)
    _add_command_src(clone)
    target = tmp_path / "project"
    commands_dir = target / ".claude" / "commands"
    commands_dir.mkdir(parents=True)
    other = tmp_path / "other-command.md"
    other.write_text("other")
    dest = commands_dir / "generic-cmd.md"
    dest.symlink_to(other)
    r = _run(clone, target)
    assert r.returncode == 0, r.stderr
    assert dest.resolve() == other.resolve(), "foreign symlink was overwritten"
    assert "generic-cmd.md" in (r.stdout + r.stderr)
