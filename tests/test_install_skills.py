"""Exercise the installer against real disposable clones and consumers."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def _make_clone(tmp_path):
    clone = tmp_path / 'clone with spaces'
    clone.mkdir()
    shutil.copy2(REPO_ROOT / 'install-skills.sh', clone)
    for name in ('alpha', 'beta'):
        skill = clone / 'skills' / name
        skill.mkdir(parents=True)
        (skill / 'SKILL.md').write_text(f'# {name}\n')
    (clone / 'skills/not-a-skill').mkdir()
    (clone / 'skills/not-a-skill/note.txt').write_text('not installed')
    (clone / 'commands').mkdir()
    (clone / 'commands/generic.md').write_text('command v1')
    target = tmp_path / 'consumer with spaces'
    target.mkdir()
    return clone, target


def _run(clone, target, *args):
    return subprocess.run([str(clone / 'install-skills.sh'), str(target), *args],
                          capture_output=True, text=True)


def _ok(clone, target):
    result = _run(clone, target)
    assert result.returncode == 0, result.stderr
    return result


def test_copies_complete_skills_commands_permissions_and_empty_directories(tmp_path):
    clone, target = _make_clone(tmp_path)
    src = clone / 'skills/alpha'
    (src / 'references/empty').mkdir(parents=True)
    (src / '.hidden').write_text('hidden support')
    executable = src / 'references/run.sh'
    executable.write_text('#!/bin/sh\nexit 0\n')
    executable.chmod(0o755)
    _ok(clone, target)
    dest = target / '.claude/skills/alpha'
    assert dest.is_dir() and not dest.is_symlink()
    assert (dest / 'SKILL.md').read_bytes() == (src / 'SKILL.md').read_bytes()
    assert (dest / 'references/run.sh').stat().st_mode & 0o777 == 0o755
    assert (dest / 'references/empty').is_dir()
    assert (dest / '.hidden').read_text() == 'hidden support'
    command = target / '.claude/commands/generic.md'
    assert command.read_text() == 'command v1' and not command.is_symlink()
    assert not (target / '.claude/skills/not-a-skill').exists()
    shutil.rmtree(clone)
    assert (dest / 'SKILL.md').read_text() == '# alpha\n'
    assert command.read_text() == 'command v1'


def test_replaces_whole_skill_and_command_but_preserves_consumer_history(tmp_path):
    clone, target = _make_clone(tmp_path)
    skill = target / '.claude/skills/alpha'
    skill.mkdir(parents=True)
    (skill / 'SKILL.md').write_text('local edit')
    (skill / 'obsolete.md').write_text('remove me')
    kept = ['.claude/.dd-state/.logs/reviews.jsonl',
            '.claude/.dd-state/.logs/dd-hooks-20200101.jsonl',
            '.claude/.dd-state/branches/main/edits.count',
            '.claude/.logs/old.log', '.claude/memory/notes.md',
            '.claude/hooks/custom.py', '.claude/settings.json',
            '.claude/skills/custom/SKILL.md', '.claude/commands/custom.md']
    for name in kept:
        path = target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b'preserve exactly\n')
        path.chmod(0o640)
    command = target / '.claude/commands/generic.md'
    command.write_text('local command')
    _ok(clone, target)
    assert (skill / 'SKILL.md').read_text() == '# alpha\n'
    assert not (skill / 'obsolete.md').exists()
    assert command.read_text() == 'command v1'
    (clone / 'skills/alpha/SKILL.md').write_text('v2')
    _ok(clone, target)
    _ok(clone, target)
    assert (skill / 'SKILL.md').read_text() == 'v2'
    for name in kept:
        assert (target / name).read_bytes() == b'preserve exactly\n'
        assert (target / name).stat().st_mode & 0o777 == 0o640
    assert not list((target / '.claude').glob('.dd-install*'))


@pytest.mark.parametrize('kind', ['source-link', 'foreign-link', 'dangling-link', 'file'])
def test_replaces_existing_entries_without_writing_through_links(tmp_path, kind):
    clone, target = _make_clone(tmp_path)
    for relative in ['skills/alpha', 'commands/generic.md']:
        dest = target / '.claude' / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        foreign = tmp_path / ('foreign-' + dest.name)
        if kind == 'file':
            dest.write_text('old')
        elif kind == 'source-link':
            dest.symlink_to(clone / relative)
        else:
            if kind == 'foreign-link':
                foreign.mkdir()
                (foreign / 'keep').write_text('untouched')
            dest.symlink_to(foreign)
    _ok(clone, target)
    assert not (target / '.claude/skills/alpha').is_symlink()
    assert (target / '.claude/skills/alpha/SKILL.md').read_text() == '# alpha\n'
    assert not (target / '.claude/commands/generic.md').is_symlink()
    assert (target / '.claude/commands/generic.md').read_text() == 'command v1'
    assert (clone / 'skills/alpha/SKILL.md').read_text() == '# alpha\n'
    assert (clone / 'commands/generic.md').read_text() == 'command v1'
    if kind == 'foreign-link':
        for foreign in tmp_path.glob('foreign-*'):
            assert (foreign / 'keep').read_text() == 'untouched'


@pytest.mark.parametrize('destination', ['.claude', '.agents'])
def test_explicit_destination_installs_skills_and_only_claude_commands(tmp_path, destination):
    clone, target = _make_clone(tmp_path)
    result = _run(clone, target, destination)
    assert result.returncode == 0, result.stderr
    assert (target / destination / 'skills/alpha/SKILL.md').is_file()
    assert (target / destination / 'commands/generic.md').exists() == (destination == '.claude')
    if destination == '.agents':
        assert not (target / '.claude').exists()


@pytest.mark.parametrize('parent', ['.claude', '.claude/skills', '.claude/commands', '.agents/skills'])
def test_rejects_symlinked_shared_parents_without_external_writes(tmp_path, parent):
    clone, target = _make_clone(tmp_path)
    foreign = tmp_path / 'foreign'
    foreign.mkdir()
    dest = target / parent
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.symlink_to(foreign)
    assert _run(clone, target, parent.split('/')[0]).returncode != 0
    assert list(foreign.iterdir()) == []


def test_replaces_nested_symlink_without_deleting_external_files(tmp_path):
    clone, target = _make_clone(tmp_path)
    skill = target / '.claude/skills/alpha'
    skill.mkdir(parents=True)
    external = tmp_path / 'external'
    external.mkdir()
    (external / 'keep').write_text('keep')
    (skill / 'nested').symlink_to(external)
    _ok(clone, target)
    assert not (skill / 'nested').exists()
    assert (external / 'keep').read_text() == 'keep'


def test_invalid_arguments_do_not_install(tmp_path):
    clone, target = _make_clone(tmp_path)
    assert _run(clone, target, '../elsewhere').returncode == 2
    assert _run(clone, target / 'missing').returncode == 2
    assert not (target / '.claude').exists()
