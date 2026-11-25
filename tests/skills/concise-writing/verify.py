"""Check the promoted study from the runner environment without calling a provider."""
import hashlib
import json
from pathlib import Path

from skilltest.config import load_config

STUDY = Path(__file__).resolve().parent
CASES = STUDY / "cases"
RESULTS = STUDY / "results"
ADOPTED = STUDY.parents[2] / "skills/concise-writing/SKILL.md"


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify():
    assert digest(ADOPTED) == "1889d41c2f90ec7c909ebf3baca0dd3c395fbc8d837003b21732599f26735422"
    for item in read(CASES / "input-sources.json")["inputs"]:
        assert digest(CASES / item["path"].split("/preparation/")[1]) == item["sha256"]

    cases = read(CASES / "configuration-index.json")["cases"]
    for case in cases:
        name = case["case"]
        assert (CASES / "criteria" / f"{name}.md").is_file()
        for provider in ("codex", "claude"):
            config = load_config(CASES / "configs" / f"{provider}-{name}-original-body.json")
            assert config.execution.provider == provider
            assert ADOPTED in [fixture.source.resolve() for fixture in config.fixtures]

    attempts = set()
    for index in RESULTS.rglob("*-run-index.json"):
        for attempt in read(index).get("attempts", []):
            identifier = attempt["attempt_id"]
            assert identifier not in attempts, identifier
            attempts.add(identifier)
            for ref in (attempt["manifest"], attempt["result"]["record"]):
                path = RESULTS / ref["path"].split("/runs/")[1]
                if digest(path) != ref["sha256"]:
                    path = path.parent / "revisions" / ref["git_revision"] / path.name
                assert digest(path) == ref["sha256"], path
    assert len(cases) == 10 and len(attempts) == 203
    print(f"Verified {len(cases)} cases on both providers and {len(attempts)} indexed attempts.")


if __name__ == "__main__":
    verify()
