import json, re, subprocess
from pathlib import Path

s = Path('/private/tmp/skilltest-cw-candidate.L4NdO8')
a = json.loads((s / 'final-audit.json').read_text())
w = (s / 'summary.md').read_text()
assert a['status'] == 'PASS' and a['fresh_observations'] == 66
table = re.findall(r'^\| CW-\d+ [^|]+ \| (—|\d+) \| (\d+) \| (\d+) \| (\d+) → (\d+) \|$', w, re.M)
assert len(table) == 22
for cells, (key, candidate) in zip(table, a['counts'].items()):
    stem = key.removesuffix('-candidate-medium')
    if stem not in a['accepted_baseline_counts']:
        stem += '-loaded'
    baseline = a['accepted_baseline_counts'][stem]
    current = next(v for k, v in baseline.items() if k != 'no-dd')
    expected = (str(baseline['no-dd']['PASS']) if 'no-dd' in baseline else '—',
                str(current['PASS']), str(candidate['PASS']),
                str(current['fidelity_fail']), str(candidate['fidelity_fail']))
    assert cells == expected, (stem, cells, expected)
links = re.findall(r'\]\(([^)]+)\)', w)
for target in links:
    assert (s / target.split('#', 1)[0]).exists(), target
assert sum(v['fidelity_fail'] for v in a['counts'].values()) == 16
assert '263 passed, 3 skipped in 24.10s' in (s / 'hooks-tests.txt').read_text()
repo = Path('/Users/simon/work/personal/disciplined-development-skills')
states = []
for path, ref in [(repo, 'origin/main'), (repo / '.worktrees/cw-validation-design', 'origin/feature/cw-validation-design')]:
    assert not subprocess.check_output(['git', '-C', str(path), 'status', '--porcelain'])
    revs = subprocess.check_output(['git', '-C', str(path), 'rev-parse', 'HEAD', ref], text=True).splitlines()
    assert revs[0] == revs[1]
    states.append(dict(path=str(path), head=revs[0], tracking_ref=ref, clean=True))
print(json.dumps(dict(status='PASS', comparison_rows=22, summary_links=len(links), repositories=states), indent=2))
