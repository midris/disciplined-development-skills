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


def check(condition, message):
    if not condition:
        raise ValueError(message)


def verify_cases():
    cases = read(CASES / "configuration-index.json")["cases"]
    check(len({case["case"] for case in cases}) == 10, "Expected ten distinct cases")
    for item in read(CASES / "input-sources.json")["inputs"]:
        path = CASES / item["path"].split("/preparation/")[1]
        check(digest(path) == item["sha256"], path)
    for case in cases:
        name = case["case"]
        criteria = CASES / "criteria" / f"{name}.md"
        check(criteria.is_file(), criteria)
        for provider in ("codex", "claude"):
            config = load_config(CASES / "configs" / f"{provider}-{name}-original-body.json")
            check(config.execution.provider == provider, config.config_path)
            check(ADOPTED in [fixture.source.resolve() for fixture in config.fixtures], config.config_path)


def pinned_path(ref):
    path = RESULTS / ref["path"].split("/runs/")[1]
    if digest(path) != ref["sha256"]:
        path = path.parent / "revisions" / ref["git_revision"] / path.name
        check(digest(path) == ref["sha256"], path)
    return path


def verify():
    adopted_hash = digest(ADOPTED)
    check(adopted_hash == "1889d41c2f90ec7c909ebf3baca0dd3c395fbc8d837003b21732599f26735422", ADOPTED)
    verify_cases()
    attempts = set()
    reviews = set()
    manifests = set()
    for index in RESULTS.rglob("*-run-index.json"):
        if index.name == "evaluator-run-index.json":
            for review in read(index)["runs"]:
                run_id = review["run_id"]
                check(run_id not in reviews, run_id)
                reviews.add(run_id)
            continue
        for attempt in read(index)["attempts"]:
            identifier = attempt["attempt_id"]
            check(identifier not in attempts, identifier)
            attempts.add(identifier)
            manifests.add(pinned_path(attempt["manifest"]))
            pinned_path(attempt["result"]["record"])

    policy_hash = digest(STUDY / "expanded-assessment-policy.txt")
    for path in manifests:
        manifest = read(path)
        check(manifest["authorities"]["policy"]["sha256"] == policy_hash, path)
        if path.is_relative_to(RESULTS / "final-comparison-01"):
            targets = [c["target_skill"] for c in manifest["conditions"] if c["id"] == "original-body"]
            sources = {s["path"]: s["sha256"] for s in manifest["subject_sources"]}
            check(len(targets) == 1 and sources.get(targets[0]) == adopted_hash, path)
    check(len(attempts) == 203 and len(reviews) == 20, "Incomplete adoption records")
    print(f"Verified 10 cases on both providers, {len(attempts)} subject attempts and {len(reviews)} evaluator calls.")


if __name__ == "__main__":
    verify()
