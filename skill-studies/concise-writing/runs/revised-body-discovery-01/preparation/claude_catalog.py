"""Verify name-only live catalog using the exact retained transport qualification."""

def strings(value):
    if isinstance(value,str):
        yield value
    elif isinstance(value,dict):
        for child in value.values():
            yield from strings(child)
    elif isinstance(value,list):
        for child in value:
            yield from strings(child)


def verify_catalog(init,description,body,requests):
    assert 'concise-writing' in init.get('skills',[]), 'CW absent from actual catalog'
    assert 'Skill' in init.get('tools',[]), 'native Skill tool unavailable'
    assert len(requests)>=2, 'incomplete transport qualification'
    initial=list(strings(requests[0]))
    assert any(description in text for text in initial), 'descriptor not qualified'
    assert not any(body in text for text in initial), 'body exposed initially'
    assert any(body in text for text in strings(requests[-1])), 'complete body not qualified'
