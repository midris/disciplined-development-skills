"""One-shot accepted-evidence copy/archive, not runner or scoring code."""
from pathlib import Path
import hashlib, json, os, re, shutil, sys, tarfile, tempfile
from collections import Counter, defaultdict

REPO=Path('/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design')
OUT=REPO/'skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium'
SCRATCH=Path('/private/tmp/skilltest-cw-candidate.pITN2u')
TMP=Path('/private/tmp')
PACKAGES=[TMP/'skilltest-cw-baseline.ksDeiD',TMP/'skilltest-cw-baseline.bOn8Dx']
assert not OUT.exists(), 'refuse existing destination'
AUDIT_ONLY='--audit-only' in sys.argv
rows=[]; archives=[]; views=[]; seen=set(); counts=Counter()
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def checked(p):
    assert p.is_file() and not any(q.is_symlink() for q in [p,*p.parents]),p
    assert p.name not in {'auth.json','credentials.json','.credentials.json'},p
    data=p.read_bytes()
    # Report only the path, never matching bytes. No host profiles are selected.
    assert not re.search(rb'(?:sk-proj-|sk-ant-api\d+-)[A-Za-z0-9_-]{20,}|eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}',data),('possible credential',str(p))
    return data

def inventory(directory):
    result={}
    for p in sorted(directory.rglob('*')):
        assert not p.is_symlink(),p
        if p.is_file(): checked(p); result[str(p.relative_to(directory))]=sha(p)
        else: assert p.is_dir(); result[str(p.relative_to(directory))]=None
    return result

def copy(source,dest):
    checked(source)
    if not AUDIT_ONLY:
        dest.parent.mkdir(parents=True,exist_ok=True)
        assert not dest.exists(); shutil.copyfile(source,dest)
        assert source.read_bytes()==dest.read_bytes()
    views.append((source,dest))

def archive(dest,files):
    assert not dest.exists()
    expected={}
    for source,name in sorted(files,key=lambda row:row[1]):
        assert name not in expected and not Path(name).is_absolute() and '..' not in Path(name).parts
        if source.is_file(): checked(source); expected[name]=sha(source)
        else: assert source.is_dir() and not source.is_symlink(); expected[name]=None
    if not AUDIT_ONLY:
        dest.parent.mkdir(parents=True,exist_ok=True)
        with tarfile.open(dest,'x:gz',format=tarfile.PAX_FORMAT) as tar:
            for source,name in sorted(files,key=lambda row:row[1]): tar.add(source,arcname=name,recursive=False)
    archives.append((dest,expected))

for package,expected in zip(PACKAGES,[18,81]):
    worksheets=sorted(package.glob('attempts/*/worksheet.md')); assert len(worksheets)==expected
    for worksheet in worksheets:
        attempt=worksheet.parent; _,rep,condition=attempt.name.split('-',2)
        number,variant=condition.split('-',1)
        purpose='loaded' if variant in {'no-dd','current-dd'} else variant
        scenario=number[:2]+'-'+number[2:]+'-'+purpose
        group=OUT/scenario
        bundle=Path((attempt/'command-stdout.txt').read_text().strip())
        assert bundle.parent==package/'runs/skilltest-runs' and bundle not in seen
        seen.add(bundle)
        data=json.loads((bundle/'result.json').read_text())
        assert data['status']=='COMPLETED' and data['execution']['exit_code']==0
        assert (data['execution']['provider'],data['execution']['model'],data['execution']['effort'])==('codex','gpt-5.6-sol','medium')
        inv=inventory(bundle)
        archive(group/'runs/skilltest-runs'/bundle.name/'bundle.tar.gz',[(bundle,bundle.name)]+[(bundle/p,bundle.name+'/'+p) for p in inv])
        for p in sorted(attempt.iterdir()):
            assert p.is_file(),p
            copy(p,group/'attempts'/attempt.name/p.name)
        body=worksheet.read_text()
        for target in re.findall(r'^\[[^\]]+\]: (.+)$',body,re.M):
            source=(attempt/target).resolve()
            assert source.is_relative_to(bundle) and source.is_file(),source
            dest=group/'runs/skilltest-runs'/bundle.name/source.relative_to(bundle)
            if not dest.exists(): copy(source,dest)
        verdict=re.search(r'\| Overall verdict \| (PASS|FAIL|INCONCLUSIVE) \|',body)[1]
        fidelity='| FAIL |' in body.split('## Task fidelity')[1].split('## Readability')[0]
        counts[(condition,verdict)]+=1
        rows.append(dict(scenario=scenario,condition=variant,repetition=rep,attempt=attempt.name,bundle=bundle.name,source_package=package.name,verdict=verdict,fidelity_fail=fidelity))
assert len(rows)==99 and len({r['scenario'] for r in rows})==22
assert len({(r['scenario'],r['condition']) for r in rows})==33
assert all(n==3 for n in Counter((r['scenario'],r['condition']) for r in rows).values())

# Select supporting primary evidence, not whole scratch trees or runtime profiles.
provenance=set()
def files(directory):
    for p in directory.iterdir():
        if p.is_file() and not p.is_symlink(): provenance.add(p)
def tree(directory):
    assert directory.is_dir(),directory
    for p in directory.rglob('*'):
        if p.is_file(): provenance.add(p)
old,new=PACKAGES
for p in [old/'summary.md',new/'summary.md',new/'approval-commands.md',new/'command-audit.json',new/'handoff-audit.md']:
    assert p.is_file(); provenance.add(p)
for name in ['cli-version.txt','cli-sha256.txt','version-stderr.txt','reconciliation.md','medium-schedule-audit.txt','input-audit.json','handoff-audit.txt']:
    provenance.add(old/'preflight'/name)
qual=TMP/'skilltest-cw-catalog-qualification.YiAoRu'
for name in ['summary.md','cli-version.txt','cli-sha256.txt','cli-version-stderr.txt','network-controls.json','no-network.sb','reuse-audit.json','catalog-v2-stdout.txt','catalog-v2-stderr.txt','final-checks.json','write-stdout.txt','write-stderr.txt']:
    provenance.add(qual/name)
files(qual/'native-v2')
pilot=TMP/'skilltest-sol-low-pilot.Lunoau'
files(pilot/'preflight')
for name in ['audit.json','preparation-checks.json','no-network.sb','no-dd-prompt-input.json','current-dd-prompt-input.json','no-dd-normalized.json','current-dd-normalized.json','no-dd-command.json','current-dd-command.json','no-dd-runtime.log','current-dd-runtime.log']:
    provenance.add(pilot/name)
ext=pilot/'extension.xWS8Q2/preflight'
files(ext); files(ext/'catalog-v3')
provenance.add(pilot/'cw-inputs.veav95/preflight/reconciliation-audit-output.json')
for label in ['q-no-dd','q-current-dd']:
    attempt=pilot/'attempts'/label; files(attempt)
    text=(attempt/'result.md').read_text()
    bundle=Path(re.search(r'^Bundle: (.+)\.$',text,re.M)[1])
    assert bundle.parent==pilot/'runs/skilltest-runs'; tree(bundle)
spike=TMP/'skilltest-controlled-inputs.MTAyGQ'
for label in ['control-debug','parent-debug','A1-debug','B1-debug','B2-debug','A2-debug']:
    tree(spike/'outputs'/label)
for name in ['run-private.sh','spike.py']: provenance.add(spike/'commands'/name)
archive(OUT/'provenance.tar.gz',[(p,str(p.relative_to(TMP))) for p in provenance])
if AUDIT_ONLY:
    print(json.dumps(dict(observations=99,conditions=33,scenarios=22,archives=len(archives),selected_provenance=sorted(str(p) for p in provenance)),indent=2))
    raise SystemExit

# Independently restore archives and validate every selected file/directory.
restore=Path(tempfile.mkdtemp(prefix='cw-preservation-restore-',dir=SCRATCH))
for i,(path,expected) in enumerate(archives):
    destination=restore/str(i); destination.mkdir()
    with tarfile.open(path,'r:gz') as tar:
        members=tar.getmembers()
        assert len(members)==len(expected) and {m.name for m in members}==set(expected)
        assert all(m.isfile() or m.isdir() for m in members)
        tar.extractall(destination,filter='data')
    for name,digest in expected.items():
        p=destination/name
        assert (p.is_dir() if digest is None else sha(p)==digest),(path,name)
for source,dest in views: assert source.read_bytes()==dest.read_bytes()
for worksheet in OUT.glob('*/attempts/*/worksheet.md'):
    for target in re.findall(r'^\[[^\]]+\]: (.+)$',worksheet.read_text(),re.M):
        assert (worksheet.parent/target).resolve().is_relative_to(OUT)
        assert (worksheet.parent/target).is_file()
    for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',worksheet.read_text()):
        if '://' not in target: assert (worksheet.parent/target).exists(),(worksheet,target)
assert not list(OUT.rglob('.git'))
print(json.dumps(dict(observations=99,conditions=33,scenarios=22,archives=len(archives),archive_files=sum(len(e) for _,e in archives),readable_copies=len(views),restore=str(restore),destination=str(OUT),provenance_files=len(provenance),rows=rows,checksums={str(p.relative_to(OUT)):sha(p) for p,_ in archives}),indent=2))
