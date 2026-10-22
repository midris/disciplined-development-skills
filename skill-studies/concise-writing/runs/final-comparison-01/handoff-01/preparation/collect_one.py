"""One remaining-suite subject, retained and registered before any next dispatch."""
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


ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent
COLLECTION = HERE.parent
STUDY = ROOT / 'skill-studies/concise-writing'
STORE = Path('/Users/simon/work/personal/skill-study-private/concise-writing/final-comparison-20261022/handoff-01')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    temporary = path.with_name(path.name + '.publishing')
    with temporary.open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def inventory_record(destination, entries):
    return {'format_version':'1','bundle':str(destination),'entries':entries}


def ensure_unattempted(slot, attempts):
    assert not any(all(a[k]==slot[k] for k in ('case_id','condition','repetition')) for a in attempts), 'no automatic reruns'


def check_previous(slots, number, store):
    for prior in slots[:number-1]:
        receipt=store/'receipts'/f'{prior["global_order"]:03}.json'
        assert receipt.exists(), f'earlier slot is unregistered: {prior["global_order"]}'
        assert json.loads(receipt.read_text()).get('cleared'), 'earlier slot needs inspection'
        idx=json.loads((COLLECTION/f'{prior["batch_id"]}-run-index.json').read_text())
        assert any(a.get('result') and a['case_id']==prior['case_id'] and a['condition']==prior['condition'] and a['repetition']==prior['repetition'] for a in idx['attempts']), 'score the prior complete artifact before advancing'


def main():
    number = int(sys.argv[1])
    assert 1 <= number <= 12, 'only the approved twelve-subject handoff may dispatch'
    slots = json.loads((HERE/'schedule.json').read_text())['slots']
    slot = next(s for s in slots if s['global_order'] == number)
    subprocess.run([sys.executable, '-m', 'skilltest', 'docs', 'check', str(STUDY/'protocol.md'), '--ready-for', 'collection', '--batch', slot['batch_id']], check=True)
    check_previous(slots,number,STORE)
    index_path = COLLECTION/f'{slot["batch_id"]}-run-index.json'
    index = json.loads(index_path.read_text())
    ensure_unattempted(slot,index['attempts'])
    manifest_path = HERE/'manifests'/f'{slot["provider"]}-{slot["case_id"]}-manifest.json'
    manifest = json.loads(manifest_path.read_text())
    assert manifest['status'] == 'frozen'
    # Authority/input pins retrieve committed bytes even as the live ledger advances.
    revision = subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    for identity in manifest['subject_sources'] + manifest['controller_only'] + [c['configuration'] for c in manifest['conditions']]:
        assert sha(ROOT/identity['path']) == identity['sha256'], identity['path']
    identities = json.loads((HERE/'runtime-identities.json').read_text())
    for identity in identities['qualified'].values():
        assert sha(Path(identity['path'])) == identity['sha256'], identity['path']
    actual_cli = shutil.which(slot['provider'])
    assert actual_cli and Path(actual_cli).resolve() == Path(identities['qualified'][slot['provider']]['path']), 'CLI selection drift'
    config = ROOT/slot['config']
    import runtime_setup
    runtime_setup.install()
    claims = STORE/'claims';claims.mkdir(exist_ok=True)
    (claims/f'{number:03}.json').open('x').write(json.dumps(slot)+'\n')
    outcome = run_once(config)
    if outcome.run_dir is None:
        # No provider launch can occur before a run directory exists.
        attempt = {
            'attempt_id':f'{slot["batch_id"]}-{slot["case_id"]}-{slot["condition"]}-{slot["repetition"]}-1',
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
    write(inv, inventory_record(destination, entries))
    mechanical = json.loads((destination/'result.json').read_text())
    charge = int(mechanical['execution']['invocation_started'])
    authority = STUDY/'protocol.md'
    committed_authority = subprocess.check_output(['git','show',f'{revision}:skill-studies/concise-writing/protocol.md'],cwd=ROOT)
    attempt = {
        'attempt_id':f'{slot["batch_id"]}-{slot["case_id"]}-{slot["condition"]}-{slot["repetition"]}-1',
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
    write(receipts/f'{number:03}.json',receipt)
    spent = sum(a['allocation']['charge'] for p in COLLECTION.glob('*run-index.json') for a in json.loads(p.read_text())['attempts'])
    assert spent <= 12
    text = authority.read_text()
    import re
    text = re.sub(r'Dispatched calls are \*\*\d+ subject, (\d+) evaluator, 0 authoring, 2 retry\*\*; remaining outer capacity is \*\*\d+ / (\d+) / 4 / 2\*\*',lambda m:f'Dispatched calls are **{610+spent} subject, {m[1]} evaluator, 0 authoring, 2 retry**; remaining outer capacity is **{12-spent} / {m[2]} / 4 / 2**',text)
    text = re.sub(r'combined subject accounting is \d+/622, with [^.]+\.',f'combined subject accounting is {610+spent}/622, with {12-spent} approved handoff calls available; the earlier E diagnostic is spent.',text)
    authority.write_text(text)
    print(json.dumps(receipt),flush=True)
    assert mechanical['status'] == 'COMPLETED', outcome.diagnostic
    for fixture in load_config(config).fixtures:
        if fixture.target.as_posix() not in {
            slot['output']
        }:
            assert (destination/'workspace/fixture'/fixture.target).read_bytes() == fixture.source.read_bytes(), fixture.target
    # The active controller separately clears identity/guidance/load inspection.


if __name__ == '__main__':
    main()
