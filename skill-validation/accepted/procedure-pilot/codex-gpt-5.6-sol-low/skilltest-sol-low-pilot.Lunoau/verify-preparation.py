"""One-off frozen-source and worksheet audit, with synthetic preparation records."""
import hashlib
import json
from pathlib import Path
import subprocess

import jsonschema
from skilltest.config import load_config
from skilltest.providers import ProviderResult
from skilltest.results import publish_result, result_record
from skilltest.workspace import RunContext

ROOT = Path('/private/tmp/skilltest-sol-low-pilot.Lunoau')
REPO = Path('/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike')
PILOT = REPO / 'skill-validation/pilot'
SP = Path('/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0')
BASE = 'ca14bbe24f8aea957dbcfeece3511226e929243d'
cli = REPO / 'skill-validation/runner/.venv/bin/skilltest'
schema = json.loads((REPO / 'skill-validation/runner/result.schema.json').read_text())
inventory = {}
for path in sorted((PILOT / 'inputs').rglob('*')):
    if not path.is_file():
        continue
    rel = path.relative_to(PILOT / 'inputs').as_posix()
    if rel.startswith('dd/'):
        original = subprocess.check_output(['git', 'show', f'{BASE}:skills/{rel[3:]}'], cwd=REPO)
    elif rel == 'superpowers/LICENSE':
        original = (SP / 'LICENSE').read_bytes()
    elif rel.startswith('superpowers/'):
        original = (SP / 'skills' / rel[len('superpowers/'):]).read_bytes()
    else:
        scenario, suffix = rel[len('tasks/'):].split('/', 1)
        catalog = 'disciplined-research' if scenario == 'dr-02' else 'lean-plan-writing'
        original = subprocess.check_output(['git', 'show', f'{BASE}:skill-validation/scenarios/{catalog}/{scenario}/fixture/{suffix}'], cwd=REPO)
    assert path.read_bytes() == original, rel
    inventory[rel] = hashlib.sha256(original).hexdigest()

audit = json.loads((ROOT / 'audit.json').read_text())
worksheets = []
for scenario, catalog in [('dr-02', 'disciplined-research'), ('lp-01', 'lean-plan-writing')]:
    prompts = []
    for arm in ('no-dd', 'current-dd'):
        package = PILOT / scenario / arm
        config = load_config(package / 'test.json')
        original = subprocess.check_output(['git', 'show', f'{BASE}:skill-validation/scenarios/{catalog}/{scenario}/rubric.md'], cwd=REPO)
        assert (package / 'rubric.md').read_bytes() == original
        prompt = (package / 'prompt.md').read_text()
        if arm == 'current-dd':
            name = 'disciplined-research' if scenario == 'dr-02' else 'lean-plan-writing'
            prompt = ''.join(line for line in prompt.splitlines(keepends=True) if f'/.agents/skills/{name}/SKILL.md' not in line)
        prompts.append(prompt)
        row = next(r for r in audit if r.get('scenario') == scenario and r['arm'] == arm)
        run = Path(row['run_dir'])
        context = RunContext(run.name, '2026-09-06T00:00:00.000Z', run, run / '.skilltest-run', run / 'config.json', run / 'prompt-template.txt', run / 'prompt.txt', run / 'workspace', run / 'workspace/fixture', run / 'workspace/evidence', run / 'stdout.txt', run / 'stderr.txt', run / 'final.txt', run / 'runner.log', run / 'result.json')
        record = result_record(context, config, ProviderResult('codex', False), ('PREPARATION_FAILED', 'Synthetic worksheet check only; no provider invocation.'), '2026-09-06T00:00:00.000Z', 0)
        jsonschema.validate(record, schema)
        publish_result(context.result_path, record)
        destination = ROOT / f'{scenario}-{arm}-synthetic-worksheet.md'
        command = [str(cli), 'worksheet', str(package.relative_to(REPO)), str(run), '--output', str(destination)]
        result = subprocess.run(command, cwd=REPO, capture_output=True, text=True, timeout=30)
        assert result.returncode == 0, result.stderr
        sheet = destination.read_text()
        assert hashlib.sha256(original).hexdigest() in sheet
        assert '| Provider CLI version |  |' in sheet
        worksheets.append({'command': command, 'cwd': str(REPO), 'stdout': result.stdout, 'stderr': result.stderr, 'exit_code': result.returncode, 'synthetic': True})
    assert prompts[0] == prompts[1], scenario

records = [r for r in audit if 'native_entries' in r]
assert records[0]['bootstrap'] == records[1]['bootstrap']
assert (ROOT / 'no-dd-normalized.json').read_bytes() == (ROOT / 'current-dd-normalized.json').read_bytes()
(ROOT / 'preparation-checks.json').write_text(json.dumps({'frozen_sources': inventory, 'rubrics_equal': 4, 'prompt_pairs_equal_except_loading': 2, 'native_common_equal': True, 'bootstrap_files_equal': len(records[0]['bootstrap']), 'worksheets': worksheets}, indent=2) + '\n')
print('PASS: 16 frozen source files, 4 unchanged rubrics, 2 prompt pairs, 4 synthetic CLI worksheets; matching common native inputs.')
