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

    observed = {}
    subject_runs = set()
    repair_scores = {}
    summary = read(BATCH / "verification.json")
    verified_manifests = set()
    for provider in ("codex", "claude"):
        index = read(BATCH / f"claim-full-{provider}-01-run-index.json")
        totals = Counter()
        for attempt in index["attempts"]:
            key = (provider, attempt["case_id"], attempt["repetition"])
            require(key not in observed, key)
            observed[key] = attempt["run_id"]
            score = read(checked(attempt["result"]["record"]))
            run_id = attempt["run_id"]
            require(run_id not in subject_runs, f"Subject run reused at {key}: {run_id}")
            subject_runs.add(run_id)
            require(score["run_id"] == run_id and score["result_id"] == attempt["result"]["result_id"], key)
            require(score["condition"] == attempt["condition"] and score["manifest"] == attempt["manifest"], key)
            totals["subjects"] += 1
            totals[f"functional {score['functional_result']}"] += 1
            factors = {c["id"]: c["judgment"] for c in score["criteria"]}
            for criterion, judgment in factors.items():
                totals[f"{criterion} {judgment}"] += 1
            if "D1" in factors:
                case = attempt["case_id"]
                group = "positive load" if case in {"invocation-change", "invocation-review"} else case
                totals[f"{group} {factors['D1']}"] += 1
            if score["functional_result"] != "not measured":
                repair_scores[run_id] = {key: factors[key] for key in ("F1", "F2", "F3")}
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
        require(dict(totals) == summary["by_provider"][provider], f"{provider} aggregate differs from scored records")
    require(observed.keys() == slots.keys() and len(verified_manifests) == 22, "Incomplete subject records")

    claim_cases = {"pressure-repair", "semantic-delivery", "invocation-review"}
    expected_claims = {run for (_, case, _), run in observed.items() if case in claim_cases}
    claims = read(BATCH / "claim-inspection.json")["rows"]
    for claim in claims:
        key = (claim["provider"], claim["case"], claim["repetition"])
        require(claim["run_id"] == observed[key] and claim["pre_edit_complete_claim_stdout_event"] > 0, key)
    require(len(claims) == 18 and {c["run_id"] for c in claims} == expected_claims, "Incomplete claim inspections")

    reviews = read(BATCH / "evaluation/evaluator-run-index.json")["runs"]
    require(len({r["run_id"] for r in reviews}) == len(reviews) == 10, "Incomplete evaluator ledger")
    reviewed = set()
    for review in reviews:
        audit = read(checked(review["audit"]))
        require((audit["run_id"], audit["packet_id"]) == (review["run_id"], review["packet_id"]), review["run_id"])
        packet = read(BATCH / "evaluation" / review["packet_id"] / "judgments.json")
        for judgment in packet["judgments"]:
            run_id = judgment["run_id"]
            require(run_id not in reviewed and run_id in repair_scores, run_id)
            reviewed.add(run_id)
            for factor, active in repair_scores[run_id].items():
                require(judgment["first_pass"][factor] == active, (run_id, factor))
    require(reviewed == set(repair_scores), "Missing independent review of a repair")
    require(len(reviewed) == summary["reviewed_unique_repairs"], "Repair count differs")
    require(sum(map(len, repair_scores.values())) == summary["reviewed_functional_factors"], "Factor count differs")
    print("Verified the shipped skill, 22 frozen configurations, 66 subject attempts and 10 review audits.")


if __name__ == "__main__":
    verify()
