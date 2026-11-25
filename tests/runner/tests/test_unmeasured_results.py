"""Versioned assessment reporting; fixtures use real Git, no providers."""
import json
import pytest
from jsonschema import Draft202012Validator
from skilltest.cli import main
from skilltest.documents import check
from skilltest.documents.formats import resource
# Shared fixture creates a complete two-attempt study with pinned Git evidence.
from test_documents import document_study

pytestmark = pytest.mark.process_smoke


def schema(version):
    name='execution-result.schema.json' if version=='1' else 'execution-result-v2.schema.json'
    return Draft202012Validator(json.loads(resource(name)))


@pytest.mark.parametrize('judgment',['met','not met','insufficient evidence'])
def test_procedural_only_is_unmeasured_never_a_functional_pass(document_study,judgment):
    root,*_=document_study
    r=json.loads((root/'results/1.json').read_text())
    r.update(schema_version='2',functional_result='not measured')
    r['criteria'][0].update(dimension='procedural',judgment=judgment)
    validator=schema('2');validator.validate(r)
    for wrong in ['met','not met','insufficient evidence']:
        r['functional_result']=wrong
        assert list(validator.iter_errors(r))
    r.update(schema_version='1',functional_result='met')
    assert list(schema('1').iter_errors(r))


def test_v2_functional_unknown_and_failure_rules_remain(document_study):
    root,*_=document_study;r=json.loads((root/'results/1.json').read_text());r['schema_version']='2'
    validator=schema('2')
    for judgment in ['met','not met','insufficient evidence']:
        r['criteria'][0]['judgment']=judgment;r['functional_result']=judgment;validator.validate(r)
        r['functional_result']='not measured';assert list(validator.iter_errors(r))
    r['criteria']=[];assert list(validator.iter_errors(r))


@pytest.mark.parametrize('kind',['result','assessment'])
def test_generate_v2_drafts_without_overwrite(tmp_path,kind):
    p=tmp_path/('draft.json' if kind=='result' else 'draft.md')
    args=['docs','new',kind,'--format-version','2','--output',str(p)]
    assert main(args)==0
    assert check(p).structurally_valid and not check(p).complete
    before=p.read_bytes();assert main(args)==1;assert p.read_bytes()==before


@pytest.fixture
def mixed_study(document_study):
    root,write,commit,ident=document_study
    protocol=(root/'protocol.md').read_text().replace('| 2 | example | original | 2 |','| 2 | example | diagnostic | 1 |')
    write('protocol.md',protocol)
    card=(root/'case/assessment.md').read_text()
    criterion=card.split('## Criteria\n',1)[1].split('## Limits',1)[0]
    procedural=criterion.replace('### F1: Outcome','### P3: Account').replace('Dimension: functional','Dimension: procedural').replace('`original`','`diagnostic`')
    write('case/assessment.md',card.replace('## Limits',procedural+'\n## Limits'))
    write('schema.json',json.loads(resource('execution-result-v2.schema.json')))
    revision=commit()
    m=json.loads((root/'case/manifest.json').read_text());m['source_revision']=revision
    for key in ['protocol','execution_result_schema']:
        m['authorities'][key]=ident(m['authorities'][key]['path'])
    m['authorities']['criteria']=[ident('case/assessment.md')]
    m['conditions'].append({**m['conditions'][0],'id':'diagnostic'})
    write('case/manifest.json',m);mr=commit();mi=ident('case/manifest.json',mr)
    index=json.loads((root/'example-run-index.json').read_text())
    for n,a in enumerate(index['attempts'],1):
        r=json.loads((root/f'results/{n}.json').read_text());r.update(schema_version='2',manifest=mi)
        a['manifest']=mi;a['authorization']['artifact']=ident('protocol.md',revision)
        if n==2:
            r.update(condition='diagnostic',functional_result='not measured')
            r['criteria'][0].update(id='P3',dimension='procedural',judgment='not met')
            a.update(condition='diagnostic',repetition=1)
        write(f'results/{n}.json',r)
    rr=commit()
    for n,a in enumerate(index['attempts'],1):a['result']['record']={**ident(f'results/{n}.json',rr), 'version': '2'}
    write('example-run-index.json',index);ir=commit()
    report=f'''# Mixed report
Format version: `2`
Assessment ID: `example`
Study / batch: `example` / `example`
Status: assessed
Scope and acceptance rules: [protocol](protocol.md#batch-example) at Git `{revision}`.
Attempt index: [index](example-run-index.json) at Git `{ir}`, SHA-256 `{ident('example-run-index.json')['sha256']}`.
Assessor: Human; structural fixture.
## Coverage and execution results
| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
|---|---:|---:|---:|---:|---:|---:|
| example / original | 1 | 1 | 1 | 0 | 0 | 0 |
| example / diagnostic | 1 | 1 | 1 | 0 | 0 | 0 |
## Aggregate results
| Case / condition / criterion | Met | Not met | Insufficient evidence | Not measured | Evidence |
|---|---:|---:|---:|---:|---|
| example / original / F1 | 1 | 0 | 0 | 0 | result-1 |
| example / original / functional outcome | 1 | 0 | 0 | 0 | result-1 |
| example / diagnostic / P3 | 0 | 1 | 0 | 0 | result-2 |
| example / diagnostic / functional outcome | 0 | 0 | 0 | 1 | result-2 |
'''
    write('example-assessment.md',report)
    return root,write,commit,ident


def test_mixed_v2_assessment_and_tables_count_unmeasured(mixed_study):
    root,*_=mixed_study
    r=check(root/'protocol.md','assessment','example');assert r.code('assessment')==0,r.diagnostics
    p=root/'tables.md'
    assert main(['docs','tables',str(root/'protocol.md'),'--batch','example','--index',str(root/'example-run-index.json'),'--output',str(p)])==0
    s=p.read_text();assert '| Not measured |' in s
    assert '| example / diagnostic / functional outcome | 0 | 0 | 0 | 1 |' in s
    assert '| example / original / functional outcome | 1 | 0 | 0 | 0 |' in s
    report_path = root/'example-assessment.md'
    aggregate = '| Case / condition / criterion' + s.split('| Case / condition / criterion', 1)[1].split('\n\n', 1)[0]
    report_path.write_text(report_path.read_text().split('## Aggregate results', 1)[0] + '## Aggregate results\n' + aggregate + '\n')
    report = check(report_path)
    assert report.code('assessment') == 0, report.diagnostics


@pytest.mark.parametrize('mode',['bad-count','legacy','missing-functional','wrong-dimension'])
def test_unmeasured_cannot_hide_counts_or_missing_criteria(mixed_study,mode):
    root,write,_,_=mixed_study
    if mode in ['bad-count','legacy']:
        p=root/'example-assessment.md';s=p.read_text()
        if mode=='bad-count':s=s.replace('0 | 0 | 0 | 1 | result-2','0 | 0 | 0 | 0 | result-2')
        else:
            s=s.replace('Format version: `2`','Format version: `1`').replace(' | Not measured','').replace('|---|---:|---:|---:|---:|---|','|---|---:|---:|---:|---|')
            s='\n'.join(' | '.join(line.split(' | ')[:4]+line.split(' | ')[5:]) if line.startswith('| example /') else line for line in s.splitlines())
        write(p,s);assert check(p).code('assessment')!=0
    else:
        r=json.loads((root/'results/1.json').read_text())
        r.update(functional_result='not measured')
        r['criteria'][0].update(dimension='procedural')
        if mode=='missing-functional':r['criteria'][0]['id']='P3'
        write('bad-result.json',r)
        report=check(root/'bad-result.json')
        assert any(d.rule in {'criterion-coverage','criterion-dimension'} for d in report.diagnostics),report.diagnostics


@pytest.mark.parametrize('status', ['invalid', 'insufficient evidence', 'unassessed', 'unattempted'])
def test_unmeasured_excluded_attempts_never_count_as_success(mixed_study, status):
    root, write, commit, ident = mixed_study
    index = json.loads((root/'example-run-index.json').read_text())
    if status == 'unattempted':
        index['attempts'].pop()
    elif status == 'unassessed':
        index['attempts'][1]['result'] = None
    else:
        record = json.loads((root/'results/2.json').read_text())
        record['setup']['status'] = status
        write('results/2.json', record)
        revision = commit()
        index['attempts'][1]['result']['record'] = {**ident('results/2.json', revision), 'version': '2'}
    write('example-run-index.json', index)
    p = root/'tables.md'
    assert main(['docs','tables',str(root/'protocol.md'),'--batch','example','--index',str(root/'example-run-index.json'),'--output',str(p)]) == 0
    row = next(s for s in p.read_text().splitlines() if s.startswith('| example / diagnostic / functional outcome |'))
    counts = row.split('|')[2:-2]
    assert all(int(n.strip()) == 0 for n in counts)


def test_v2_failure_takes_precedence_over_unknown(document_study):
    root, *_ = document_study
    record = json.loads((root/'results/1.json').read_text())
    record.update(schema_version='2', functional_result='not met')
    record['criteria'][0]['judgment'] = 'insufficient evidence'
    record['criteria'].append({**record['criteria'][0], 'id':'F2', 'judgment':'not met'})
    schema('2').validate(record)
    record['functional_result'] = 'insufficient evidence'
    assert list(schema('2').iter_errors(record))


def test_result_version_must_match_pinned_schema(mixed_study):
    root, write, commit, ident = mixed_study
    write('schema.json', json.loads(resource('execution-result.schema.json')))
    revision = commit()
    manifest = json.loads((root/'case/manifest.json').read_text())
    manifest['authorities']['execution_result_schema'] = ident('schema.json', revision)
    write('case/manifest.json', manifest)
    revision = commit()
    record = json.loads((root/'results/2.json').read_text())
    record['manifest'] = ident('case/manifest.json', revision)
    write('bad-result.json', record)
    report = check(root/'bad-result.json')
    assert any(d.rule == 'result-schema-version' for d in report.diagnostics)


@pytest.mark.parametrize('mode', ['missing', 'extra', 'version-one'])
def test_aggregate_shape_cannot_hide_unmeasured(mixed_study, mode):
    root, write, *_ = mixed_study
    p = root/'example-assessment.md'
    raw = p.read_text()
    if mode == 'missing':
        raw = raw.replace('Not measured', 'Other')
    elif mode == 'extra':
        raw = raw.replace('Not measured | Evidence', 'Not measured | Extra | Evidence')
    else:
        raw = raw.replace('Format version: `2`', 'Format version: `1`')
    write(p, raw)
    assert check(p).code('assessment') != 0
