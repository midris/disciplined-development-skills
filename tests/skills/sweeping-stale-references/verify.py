"""Verify the adopted SSR regression using the runner without invoking providers."""
import hashlib
import json
from collections import Counter
from pathlib import Path

from skilltest.config import load_config

STUDY = Path(__file__).resolve().parent
BATCH = STUDY / "results/complete-claim-regression-01"
SHIPPED = STUDY.parents[2] / "skills/sweeping-stale-references/SKILL.md"
FROZEN = BATCH / "preparation/skill/SKILL.md"
ARCHIVE = Path("skill-studies/sweeping-stale-references")


def read(path):
    return json.loads(path.read_text())


def require(valid, detail):
    if not valid:
        raise ValueError(detail)


def local(path):
    relative = Path(path).relative_to(ARCHIVE)
    if relative.parts[0] == "runs":
        return STUDY / "results" / Path(*relative.parts[1:])
    return STUDY / relative


def checked(ref):
    path = local(ref["path"])
    require(hashlib.sha256(path.read_bytes()).hexdigest() == ref["sha256"], path)
    return path


def verify():
    require(SHIPPED.read_bytes() == FROZEN.read_bytes(), "Installed-source skill differs from tested skill")
    scheduled = read(BATCH / "preparation/schedule.json")["slots"]
    slots = {(s["provider"], s["case_id"], s["repetition"]): local(s["configuration"]) for s in scheduled}
    require(len(slots) == len(scheduled) == 66, "Unexpected subject schedule")
    cases = {s["case_id"] for s in scheduled}
    require(len(cases) == 11, "Expected eleven cases")
    require(set(slots) == {(p, c, r) for p in ("claude", "codex") for c in cases for r in (1, 2, 3)}, "Incomplete schedule")

    observed = []
    verified_manifests = set()
    for provider in ("codex", "claude"):
        index = read(BATCH / f"claim-full-{provider}-01-run-index.json")
        for attempt in index["attempts"]:
            key = (provider, attempt["case_id"], attempt["repetition"])
            observed.append(key)
            score = read(checked(attempt["result"]["record"]))
            require(score["run_id"] == attempt["run_id"], key)
            path = checked(attempt["manifest"])
            manifest = read(path)
            condition, = manifest["conditions"]
            config_path = checked(condition["configuration"])
            require(config_path == slots[key] and condition["id"] == attempt["condition"], key)
            if path in verified_manifests:
                continue
            config = load_config(config_path)
            sources = {checked(ref) for ref in manifest["subject_sources"]}
            delivered = {config.prompt, *(fixture.source for fixture in config.fixtures)}
            require(config.execution.provider == provider and sources == delivered, config_path)
            require(local(condition["target_skill"]) == FROZEN and FROZEN in sources, path)
            checked(manifest["authorities"]["policy"])
            for criteria in manifest["authorities"]["criteria"]:
                checked(criteria)
            verified_manifests.add(path)
    require(Counter(observed) == Counter(slots.keys()) and len(verified_manifests) == 22, "Incomplete subject records")

    reviews = read(BATCH / "evaluation/evaluator-run-index.json")["runs"]
    require(len({r["run_id"] for r in reviews}) == len(reviews) == 10, "Incomplete evaluator ledger")
    for review in reviews:
        checked(review["audit"])
    print("Verified the shipped skill, 22 frozen configurations, 66 subject attempts and 10 review audits.")


if __name__ == "__main__":
    verify()
