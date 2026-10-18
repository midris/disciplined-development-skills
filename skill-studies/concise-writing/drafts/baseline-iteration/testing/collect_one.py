"""One scheduled E subject, retained and registered before any next dispatch."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys

from skilltest.config import load_config
from skilltest.documents.retention import inventory
from skilltest.runner import run_once
import runtime_setup

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
STUDY = ROOT / 'skill-studies/concise-writing'
STORE = Path('/Users/simon/work/personal/skill-study-private/concise-writing/e-iteration-20261018')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    temporary = path.with_name(path.name + '.publishing')
    with temporary.open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def main():
    number = int(sys.argv[1])
    slots = json.loads((HERE/'schedule.json').read_text())['slots']
    slot = next(s for s in slots if s['global_order'] == number)
    # Every earlier slot must be retained, charged and cleared before advancing.
    for prior in slots[:number-1]:
        receipt = STORE/'receipts'/f'{prior["global_order"]:02}.json'
        assert receipt.exists(), f'earlier slot is unregistered: {prior["global_order"]}'
        assert json.loads(receipt.read_text()).get('cleared'), 'earlier slot needs inspection'
    index_path = STUDY/f'{slot["batch_id"]}-run-index.json'
    index = json.loads(index_path.read_text())
    assert not any(a['condition'] == slot['condition'] and a['repetition'] == slot['repetition'] for a in index['attempts']), 'no automatic reruns'
    manifest_path = HERE/f'{slot["provider"]}-manifest.json'
    manifest = json.loads(manifest_path.read_text())
    assert manifest['status'] == 'frozen'
    # Authority/input pins retrieve committed bytes even as the live ledger advances.
    revision = subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    for identity in manifest['subject_sources'] + manifest['controller_only'] + [c['configuration'] for c in manifest['conditions']]:
        assert sha(ROOT/identity['path']) == identity['sha256'], identity['path']
    identities = json.loads((HERE/'runtime-identities.json').read_text())
    for identity in identities['qualified'].values():
        assert sha(Path(identity['path'])) == identity['sha256'], identity['path']
    config = ROOT/slot['config']
    runtime_setup.install()
    claims = STORE/'claims';claims.mkdir(exist_ok=True)
    (claims/f'{number:02}.json').open('x').write(json.dumps(slot)+'\n')
    outcome = run_once(config)
    if outcome.run_dir is None:
        # No provider launch can occur before a run directory exists.
        attempt = {
            'attempt_id':f'{slot["batch_id"]}-{slot["condition"]}-{slot["repetition"]}-1',
            'case_id':slot['case_id'],'condition':slot['condition'],'repetition':slot['repetition'],
            'attempt_number':1,'retry_of':None,
            'manifest':{'path':str(manifest_path.relative_to(ROOT)),'sha256':sha(manifest_path),'version':'1','git_revision':revision},
            'authorization':{'artifact':{'path':'skill-studies/concise-writing/protocol.md','sha256':hashlib.sha256(subprocess.check_output(['git','show',f'{revision}:skill-studies/concise-writing/protocol.md'],cwd=ROOT)).hexdigest(),'version':'1','git_revision':revision},'selector':f'Batch: {slot["batch_id"]}; order {slot["order"]}'},
            'run_id':None,'allocation':{'pool':'subject','charge':0},
            'limitations':['Pre-allocation failure; zero invocation charge; no automatic replacement.',outcome.diagnostic or 'No run directory'],
            'bundle':{'path':None,'inventory':None,'verified':False},'result':None,
        }
        index['attempts'].append(attempt);write(index_path,index)
        raise RuntimeError('Pre-allocation failure registered; dispatch stops: '+str(outcome.diagnostic))
    source = outcome.run_dir
    destination = STORE/'subjects'/source.name;destination.parent.mkdir(exist_ok=True)
    shutil.copytree(source,destination,symlinks=True)
    entries = inventory(source)
    assert inventory(destination) == entries, 'retention mismatch; original is retained'
    inv = destination.with_name(destination.name+'.inventory.json')
    write(inv, {'version':'1','entries':entries})
    mechanical = json.loads((destination/'result.json').read_text())
    charge = int(mechanical['execution']['invocation_started'])
    authority = STUDY/'protocol.md'
    committed_authority = subprocess.check_output(['git','show',f'{revision}:skill-studies/concise-writing/protocol.md'],cwd=ROOT)
    attempt = {
        'attempt_id':f'{slot["batch_id"]}-{slot["condition"]}-{slot["repetition"]}-1',
        'case_id':slot['case_id'],'condition':slot['condition'],'repetition':slot['repetition'],
        'attempt_number':1,'retry_of':None,
        'manifest':{'path':str(manifest_path.relative_to(ROOT)),'sha256':sha(manifest_path),'version':'1','git_revision':revision},
        'authorization':{'artifact':{'path':str(authority.relative_to(ROOT)),'sha256':hashlib.sha256(committed_authority).hexdigest(),'version':'1','git_revision':revision},'selector':f'Batch: {slot["batch_id"]}; order {slot["order"]}'},
        'run_id':destination.name,'allocation':{'pool':'subject','charge':charge},
        'limitations':['Retained; active-session assessment pending. No blind, held-out or independent assessor claim.'],
        'bundle':{'path':str(destination),'inventory':{'path':str(inv),'sha256':sha(inv),'version':'1'},'verified':True},'result':None,
    }
    index['attempts'].append(attempt);write(index_path,index)
    receipts = STORE/'receipts';receipts.mkdir(exist_ok=True)
    receipt = {'slot':slot,'run_id':destination.name,'bundle':str(destination),'charge':charge,'status':mechanical['status'],'cleared':False}
    write(receipts/f'{number:02}.json',receipt)
    spent = sum(a['allocation']['charge'] for provider in ['codex','claude'] for a in json.loads((STUDY/f'{provider}-e-iteration-01-run-index.json').read_text())['attempts'])
    text = authority.read_text()
    import re
    text = re.sub(r'Dispatched calls are \*\*\d+ subject, 12 evaluator, 0 authoring, 1 retry\*\*; remaining outer capacity is \*\*\d+ / 2 / 4 / 3\*\*',f'Dispatched calls are **{256+spent} subject, 12 evaluator, 0 authoring, 1 retry**; remaining outer capacity is **{40-spent} / 2 / 4 / 3**',text)
    text = re.sub(r'combined subject accounting is \d+/296, with [^.]+\.',f'combined subject accounting is {256+spent}/296, with {40-spent} E calls remaining.',text)
    authority.write_text(text)
    print(json.dumps(receipt),flush=True)
    assert mechanical['status'] == 'COMPLETED', outcome.diagnostic
    for fixture in load_config(config).fixtures:
        if fixture.target.as_posix() != 'report.md':
            assert (destination/'workspace/fixture'/fixture.target).read_bytes() == fixture.source.read_bytes(), fixture.target
    # The active controller separately clears identity/guidance/load inspection.


if __name__ == '__main__':
    main()
