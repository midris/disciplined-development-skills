"""One-off provider-free pilot preparation audit; no model invocation."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

from skilltest.config import load_config
from skilltest.codex_runtime import CodexRuntime, check_inputs
from skilltest.workspace import create_run, prepare_workspace

ROOT = Path('/private/tmp/skilltest-sol-low-pilot.Lunoau')
REPO = Path('/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike')
PILOT = REPO / 'skill-validation/pilot'
os.umask(0o077)
(ROOT / 'tmp').mkdir()
(ROOT / 'dummy-profile').mkdir()
(ROOT / 'dummy-profile/auth.json').write_text('{"OPENAI_API_KEY":"dummy-provider-free-not-a-secret"}')
os.environ['CODEX_HOME'] = str(ROOT / 'dummy-profile')
tempfile.tempdir = str(ROOT / 'tmp')
records = []
try:
    for scenario in ('dr-02', 'lp-01', 'qualification'):
        for arm in ('no-dd', 'current-dd'):
            config = load_config(PILOT / scenario / arm / 'test.json')
            context = create_run(config)
            prepare_workspace(context, config)
            hashes = check_inputs(context, config)
            expected = {'writing-plans'}
            if arm == 'current-dd':
                expected |= {p.parent.name for p in (PILOT / 'inputs/dd').glob('*/SKILL.md')}
            actual = {p.parent.name for p in context.fixture_dir.glob('.agents/skills/*/SKILL.md')}
            assert actual == expected
            assert not any(p.is_symlink() for p in context.fixture_dir.rglob('*'))
            assert not any(p.name in ('rubric.md', 'auth.json') for p in context.fixture_dir.rglob('*'))
            # Capture native catalogs once per condition using identical diagnostic text.
            if scenario == 'qualification':
                log = []
                runtime = CodexRuntime(log.append)
                try:
                    runtime.prepare(context.fixture_dir)
                    command = [runtime.executable, 'debug', 'prompt-input', '-c', 'model="gpt-5.6-sol"', '-c', 'model_reasoning_effort="low"', '-c', 'shell_environment_policy.inherit="none"', '-c', 'cli_auth_credentials_store="file"', '-c', 'approval_policy="never"', 'Pilot provider-free catalog inspection.']
                    (ROOT / f'{arm}-command.json').write_text(json.dumps({'argv': command, 'cwd': str(context.fixture_dir), 'env': runtime.environment}, indent=2))
                    process = subprocess.Popen(command, cwd=context.fixture_dir, env=runtime.environment, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
                    stdout, stderr, timed_out = runtime.communicate(process, None, 30)
                    (ROOT / f'{arm}-prompt-input.json').write_bytes(stdout)
                    (ROOT / f'{arm}-stderr.txt').write_bytes(stderr)
                    assert process.returncode == 0 and not timed_out
                    messages = json.loads(stdout)
                    text = '\n'.join(c.get('text', '') for m in messages for c in m.get('content', []))
                    entries = [line for line in text.splitlines() if line.startswith('- ') and '(file: ' in line]
                    for name in expected:
                        assert sum(line.startswith(f'- {name}:') for line in entries) == 1, name
                    if arm == 'no-dd':
                        assert not any(name in text for name in [p.parent.name for p in (PILOT / 'inputs/dd').glob('*/SKILL.md')])
                    assert '/Users/simon' not in text and '/etc/codex' not in text
                    bootstrap = runtime.root / 'codex/skills/.system'
                    records.append({'arm': arm, 'native_entries': entries, 'bootstrap': {str(p.relative_to(bootstrap)): hashlib.sha256(p.read_bytes()).hexdigest() for p in bootstrap.rglob('*') if p.is_file()}})
                finally:
                    cleanup = runtime.cleanup()
                    (ROOT / f'{arm}-runtime.log').write_text('\n'.join(log) + f'\ncleanup: {cleanup!r}\n')
                    assert cleanup is None
            records.append({'scenario': scenario, 'arm': arm, 'run_dir': str(context.run_dir), 'prelaunch_hashes': hashes})
finally:
    (ROOT / 'dummy-profile/auth.json').unlink()
    (ROOT / 'audit.json').write_text(json.dumps(records, indent=2) + '\n')
print('Six configurations prepared; both native catalogs captured; no model calls.')
