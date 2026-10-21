"""Catalog shapes from Claude 2.1.305 qualification and retained subject 121."""
import copy
import importlib.util
from pathlib import Path
import pytest

spec=importlib.util.spec_from_file_location('claude_catalog',Path(__file__).parents[1]/'claude_catalog.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)


def case():
    return ({'skills':['concise-writing','verify'],'tools':['Read','Skill']},
            'Use when revising text.', '# Body\nA complete skill body.',
            [{'system':[{'text':'concise-writing: Use when revising text.'}]},
             {'messages':[{'content':'# Body\nA complete skill body.'}]}])


def test_name_only_init_uses_qualified_description_payload():
    module.verify_catalog(*case())


@pytest.mark.parametrize('mutation',['name','tool','description','initial-body','loaded-body','empty'])
def test_missing_or_conflicting_catalog_evidence_is_rejected(mutation):
    init,description,body,requests=copy.deepcopy(case())
    if mutation=='name':init['skills']=[]
    elif mutation=='tool':init['tools']=['Read']
    elif mutation=='description':requests[0]['system'][0]['text']='another descriptor'
    elif mutation=='initial-body':requests[0]['system'][0]['text']+='\n'+body
    elif mutation=='loaded-body':requests[-1]['messages'][0]['content']='partial body'
    elif mutation=='empty':requests=[]
    with pytest.raises(AssertionError):module.verify_catalog(init,description,body,requests)
