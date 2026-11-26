"""Complete missing inline-link views, then independently verify preserved evidence."""
from pathlib import Path
import hashlib,json,re,shutil,tarfile,tempfile
from collections import Counter
ROOT=Path('/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design')
OUT=ROOT/'skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium'
SCRATCH=Path('/private/tmp/skilltest-cw-candidate.pITN2u')
TMP=Path('/private/tmp')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]; archive_sources={}; fixed=[]; checked_links=0
for package,expected in [('skilltest-cw-baseline.ksDeiD',18),('skilltest-cw-baseline.bOn8Dx',81)]:
    source=TMP/package; worksheets=sorted(source.glob('attempts/*/worksheet.md'))
    assert len(worksheets)==expected
    for w in worksheets:
        aid=w.parent.name; _,rep,key=aid.split('-',2); number,condition=key.split('-',1)
        scenario=number[:2]+'-'+number[2:]+'-'+('loaded' if condition in {'no-dd','current-dd'} else condition)
        group=OUT/scenario; destination=group/'attempts'/aid
        bundle=Path((w.parent/'command-stdout.txt').read_text().strip())
        assert bundle.parent==source/'runs/skilltest-runs'
        archive=group/'runs/skilltest-runs'/bundle.name/'bundle.tar.gz'
        assert archive.is_file() and archive not in archive_sources
        archive_sources[archive]=bundle
        for p in w.parent.iterdir(): assert p.is_file() and p.read_bytes()==(destination/p.name).read_bytes()
        body=w.read_text()
        links=re.findall(r'^\[[^\]]+\]: (.+)$',body,re.M)+re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',body)
        for target in links:
            if '://' in target: continue
            original=(w.parent/target).resolve(); dest=(destination/target).resolve()
            assert original.is_file() and not original.is_symlink()
            assert dest.is_relative_to(group)
            if not dest.exists():
                assert original.is_relative_to(bundle)
                dest.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(original,dest); fixed.append(str(dest.relative_to(OUT)))
            assert original.read_bytes()==dest.read_bytes(); checked_links+=1
        verdict=re.search(r'\| Overall verdict \| (PASS|FAIL|INCONCLUSIVE) \|',body)[1]
        fidelity='| FAIL |' in body.split('## Task fidelity')[1].split('## Readability')[0]
        rows.append(dict(scenario=scenario,condition=condition,repetition=rep,attempt=aid,bundle=bundle.name,source_package=package,verdict=verdict,fidelity_fail=fidelity))
assert len(rows)==99 and len({r['scenario'] for r in rows})==22
counts=Counter((r['scenario'],r['condition']) for r in rows)
assert len(counts)==33 and set(counts.values())=={3}
reference=json.loads((SCRATCH/'qualification/reuse-audit.json').read_text())['groups']
for (scenario,condition),count in counts.items():
    selected=[r for r in rows if (r['scenario'],r['condition'])==(scenario,condition)]
    number=''.join(scenario.split('-')[:2]); key=number+'-'+condition
    actual={v:sum(r['verdict']==v for r in selected) for v in ['PASS','FAIL','INCONCLUSIVE']}
    actual.update(evaluable=sum(r['verdict']!='INCONCLUSIVE' for r in selected),fidelity_fail=sum(r['fidelity_fail'] for r in selected))
    assert actual==reference[key],(key,actual)
restore=Path(tempfile.mkdtemp(prefix='cw-preservation-verified-',dir=SCRATCH))
archive_files=0
for i,(archive,bundle) in enumerate(sorted(archive_sources.items())):
    expected={bundle.name:None}
    for p in bundle.rglob('*'):
        assert not p.is_symlink()
        expected[bundle.name+'/'+str(p.relative_to(bundle))]=sha(p) if p.is_file() else None
    dest=restore/str(i); dest.mkdir()
    with tarfile.open(archive,'r:gz') as tar:
        members=tar.getmembers()
        assert {m.name for m in members}==set(expected) and len(members)==len(expected)
        assert all(m.isfile() or m.isdir() for m in members)
        tar.extractall(dest,filter='data')
    for name,digest in expected.items(): assert (sha(dest/name)==digest if digest else (dest/name).is_dir())
    archive_files+=len(expected)
provenance=OUT/'provenance.tar.gz'
selected=json.loads((SCRATCH/'preservation-selection.json').read_text())['selected_provenance']
expected={str(Path(p).relative_to(TMP)):sha(Path(p)) for p in selected}
dest=restore/'provenance'; dest.mkdir()
with tarfile.open(provenance,'r:gz') as tar:
    members=tar.getmembers()
    assert {m.name for m in members}==set(expected) and len(members)==len(expected)
    assert all(m.isfile() and not Path(m.name).is_absolute() and '..' not in Path(m.name).parts for m in members)
    tar.extractall(dest,filter='data')
for name,digest in expected.items(): assert sha(dest/name)==digest
archives=[*archive_sources,provenance]
assert set(OUT.rglob('*.tar.gz'))==set(archives) and not list(OUT.rglob('.git'))
print(json.dumps(dict(observations=99,conditions=33,scenarios=22,archives=len(archives),archive_entries=archive_files+len(expected),provenance_files=len(expected),inline_view_files_added=len(fixed),worksheet_links=checked_links,restore=str(restore),source_bytes_preserved=True,counts_match_accepted_audit=True,rows=rows,checksums={str(p.relative_to(OUT)):sha(p) for p in sorted(archives)}),indent=2))
