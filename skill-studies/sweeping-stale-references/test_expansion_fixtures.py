"""Offline fixture qualification, not a model evaluator or subject input."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

CASES = Path(__file__).resolve().parent / 'cases'


def run(*args, cwd):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=20)


class ExpansionFixtures(unittest.TestCase):
    def test_initial_service_is_runnable(self):
        root = CASES / 'initiating-change/fixture'
        p = run(sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests', cwd=root)
        self.assertEqual(p.returncode, 0, p.stderr)
        p = run(sys.executable, '-B', str(root/'scripts/show-session.py'), cwd='/private/tmp')
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(p.stdout.strip(), 'token_ttl_minutes=30; expires_at=1900')

    def test_complete_reference_rename_preserves_runtime_and_commits(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)/'repo'
            shutil.copytree(CASES/'initiating-change/fixture', root)
            protected = {p: (root/p).read_bytes() for p in ['archive/rollout-2024.md','vendor/partner/example.json','vendor/partner/README.md']}
            for name in ['src/session.py','config/defaults.json','scripts/show-session.py','README.md','docs/session-policy.md','tests/test_session.py']:
                p=root/name
                p.write_text(p.read_text().replace('token_ttl_minutes','session_ttl_minutes').replace('token TTL','session TTL'))
            p=run(sys.executable,'-B','-m','unittest','discover','-s','tests',cwd=root)
            self.assertEqual(p.returncode,0,p.stderr)
            p=run(sys.executable,'-B',str(root/'scripts/show-session.py'),cwd=d)
            self.assertEqual(p.stdout.strip(),'session_ttl_minutes=30; expires_at=1900')
            self.assertEqual(p.returncode,0,p.stderr)
            code="from session import expires_at; assert expires_at(100, {'session_ttl_minutes':12}) == 820"
            p=run(sys.executable,'-B','-c',code,cwd=root/'src')
            self.assertEqual(p.returncode,0,p.stderr)
            self.assertTrue(all((root/p).read_bytes()==raw for p,raw in protected.items()))
            # Qualify Git availability using private config; no inherited project/Git overrides.
            env={k:v for k,v in os.environ.items() if not k.startswith('GIT_')}
            env.update(GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull)
            for args in [('init','-q'),('add','.'),('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','-c','commit.gpgsign=false','-c','core.hooksPath=/dev/null','commit','-qm','reference solution')]:
                p=subprocess.run(['git',*args],cwd=root,env=env,capture_output=True,text=True,timeout=20)
                self.assertEqual(p.returncode,0,p.stderr)
            p=subprocess.run(['git','status','--porcelain'],cwd=root,env=env,capture_output=True,text=True,timeout=20)
            self.assertEqual(p.returncode,0,p.stderr)
            self.assertEqual(p.stdout,'')

    def test_code_only_rename_leaves_a_runtime_consumer_broken(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'repo';shutil.copytree(CASES/'initiating-change/fixture',root)
            p=root/'src/session.py';p.write_text(p.read_text().replace('token_ttl_minutes','session_ttl_minutes'))
            observed=run(sys.executable,'-B',str(root/'scripts/show-session.py'),cwd=root)
            self.assertNotEqual(observed.returncode,0)
            self.assertIn('session_ttl_minutes',observed.stderr)

    def test_initiating_reference_inventory_matches_declared_units(self):
        root=CASES/'initiating-change/fixture'
        counts={p.relative_to(root).as_posix():len(re.findall(r'token_ttl_minutes|token TTL',p.read_text())) for p in root.rglob('*') if p.is_file()}
        counts={p:n for p,n in counts.items() if n}
        self.assertEqual(counts,{'src/session.py':2,'config/defaults.json':1,'scripts/show-session.py':2,'README.md':1,'docs/session-policy.md':2,'tests/test_session.py':2,'archive/rollout-2024.md':2,'vendor/partner/example.json':1,'vendor/partner/README.md':1})
        self.assertEqual(sum(counts.values()),14)

    def test_local_correction_has_one_target_and_no_broken_supplied_link(self):
        root=CASES/'local-change/fixture'
        hits=[p for p in root.rglob('*') if p.is_file() and 'Member ship' in p.read_text()]
        self.assertEqual(hits,[root/'docs/glossary.md'])
        for p in root.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
                self.assertTrue((p.parent/target).is_file(),target)
        self.assertIn('member shipping address',(root/'docs/shipping.md').read_text())
        with tempfile.TemporaryDirectory() as d:
            copy=Path(d)/'repo';shutil.copytree(root,copy)
            p=copy/'docs/glossary.md';p.write_text(p.read_text().replace('Member ship','Membership'))
            changed=[p.relative_to(copy).as_posix() for p in copy.rglob('*') if p.is_file() and p.read_bytes()!=(root/p.relative_to(copy)).read_bytes()]
            self.assertEqual(changed,['docs/glossary.md'])

    def test_large_inventory_ranges_groups_and_totals_reconcile(self):
        text=(CASES/'large-sweep-account/fixture/inventory.md').read_text()
        rows=[line.split('|')[1:-1] for line in text.splitlines() if line.startswith('| `')]
        totals={};paths=set();groups=set()
        for path,locations,outcome,count in rows:
            path=path.strip();kind=outcome.strip().split(':')[0];n=int(count)
            lo,hi=map(int,locations.strip().split('–'))
            self.assertEqual(hi-lo+1,n)
            totals[kind]=totals.get(kind,0)+n
            paths.add(path);groups.add((path,kind))
        self.assertEqual(totals,{'update':80,'intentionally stale':40,'false positive':6})
        self.assertEqual(len(paths),10)
        self.assertEqual(len(groups),11)

    def test_configs_supply_no_controller_material_and_pair_only_guidance(self):
        for case in ['initiating-change','local-change','large-sweep-account']:
            folder=CASES/case
            original=json.loads((folder/'original.json').read_text())
            targets=set()
            for entry in original['fixtures']:
                self.assertTrue((folder/entry['source']).is_file())
                self.assertNotIn(entry['target'],targets)
                targets.add(entry['target'])
            self.assertFalse(targets & {'assessment.md','expected.md','assessment-policy.txt','manifest.json'})
            if case=='large-sweep-account':continue
            control=json.loads((folder/'control.json').read_text())
            self.assertEqual(original['execution'],control['execution'])
            self.assertEqual(original['fixtures'][:-1],control['fixtures'])
            self.assertEqual((folder/'prompt-original.md').read_text().split('\n\n',1)[1],(folder/'prompt-control.md').read_text())


if __name__=='__main__':
    unittest.main()
