"""Controller predicate for complete explicit skill delivery."""
import re

def normalize(text):
    return "\n".join(re.sub(r"^\s*\d+[→\t|]", "", line) for line in text.splitlines()).strip()

def body_delivered(source, output):
    body = source.split("\n---\n", 1)[1] if source.startswith("---\n") and "\n---\n" in source else source
    body = normalize(body)
    return bool(body) and body in normalize(output)
