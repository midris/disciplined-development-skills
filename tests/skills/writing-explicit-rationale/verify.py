"""Verify promotion inputs and retained WER outcomes without a provider call."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

from skilltest.config import load_config

STUDY = Path(__file__).resolve().parent
RESULTS = STUDY / "results"
SHIPPED = STUDY.parents[2] / "skills/writing-explicit-rationale/SKILL.md"
SOURCE = Path("skill-studies/writing-explicit-rationale/runs")
ADOPTED = "fd9f61771a62f5f2e376d1d6ceed32f3b3fdcaee0f11d28bec134eda2e03b45a"
PARENT = "36ab7246d4c974cbf7d195b92780d835c31863477e33aaca1f0a8389c0f48381"


def read(path):
    return json.loads(path.read_bytes())


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs(config):
    return {f.target.as_posix(): digest(f.source) for f in config.fixtures}


def verify_public_suite():
    require(digest(SHIPPED) == digest(STUDY / "drafts/explicit-residual-risk/SKILL.md") == ADOPTED, SHIPPED)
    require(digest(STUDY / "drafts/baseline-edit-with-examples/SKILL.md") == PARENT, "599-word parent")
    baseline = RESULTS / "application-benchmark-01"
    checked = set()
    for slot in read(baseline / "schedule.json")["subjects"]:
        key = slot["provider"], slot["case"]
        if slot["condition"] != "original" or key in checked:
            continue
        path = RESULTS / Path(slot["config"]).relative_to(SOURCE)
        require(digest(path) == slot["sha256"], path)
        original = load_config(path)
        current = load_config(STUDY / "configs" / key[0] / f"{key[1]}.json")
        expected = dict(slot["inputs"])
        require(inputs(original) == expected, path)
        expected["GUIDANCE.md"] = ADOPTED
        require(inputs(current) == expected and original.execution == current.execution, key)
        guidance, = (f for f in current.fixtures if f.target.as_posix() == "GUIDANCE.md")
        require(guidance.source == SHIPPED, guidance.source)
        require(digest(current.prompt) == slot["prompt_sha256"], current.prompt)
        checked.add(key)
    require(len(checked) == 14, "Expected seven cases on each provider")

    baseline_counts = Counter()
    for batch in (baseline, RESULTS / "application-topup-01"):
        for row in read(batch / "assessment.json")["subjects"]:
            baseline_counts[row["condition"], row["functional_result"]] += 1
    require(baseline_counts == {("original", "met"): 67, ("original", "not met"): 2,
                                ("control", "met"): 42, ("control", "not met"): 27,
                                ("original", "invalid"): 1, ("control", "invalid"): 1}, baseline_counts)

    outcomes = []
    screen = RESULTS / "rewrite-screen-01"
    for path in [screen, *(screen / f"rep-{i}" for i in range(2, 6))]:
        outcomes.append(read(path / "assessment.json")["outcome"] == "met")
    for path in sorted(RESULTS.glob("rewrite-broad-*")):
        for row in read(path / "assessment.json")["subjects"]:
            require(row["setup"] == "valid" and row["criteria"], row)
            outcomes.append(all(value == "met" for value in row["criteria"].values()))
    require(len(outcomes) == 70 and sum(outcomes) == 69, "599-word comparison")


def check_private(store, path, sha):
    suffix = path.split("/skill-study-private/writing-explicit-rationale/", 1)[1]
    require(digest(store / suffix) == sha, suffix)


def verify_adopted_runs(store):
    runs = set()
    cells = Counter()
    repetitions = set()
    for name in ("residual-risk-01", "residual-risk-02", "residual-risk-03", "transfer-02"):
        batch = RESULTS / name
        assessment = read(batch / "assessment.json")
        rows = assessment["subjects"] if name == "transfer-02" else assessment
        slots = read(batch / "schedule.json")["subjects"]
        require([row["order"] for row in rows] == [slot["order"] for slot in slots], name)
        for slot, row in zip(slots, rows):
            attempt = read(batch / row["attempt"])
            require(attempt["order"] == slot["order"] and attempt["status"] == "COMPLETED", attempt)
            require(attempt["run_id"] not in runs and attempt["charge"] == 1, attempt["run_id"])
            runs.add(attempt["run_id"])
            key = slot["provider"], slot.get("case", "booking-slot"), slot["repetition"]
            require(key not in repetitions and row.get("repetition", key[2]) == key[2], key)
            repetitions.add(key)
            require(row.get("case", "booking-slot") == key[1], key)
            require(slot["inputs"]["GUIDANCE.md"] == ADOPTED and row["provider"] == slot["provider"], slot)
            require(row["criteria"] and all(v == "met" for v in row["criteria"].values()), row)
            if name != "transfer-02":
                config_path = RESULTS / Path(slot["config"]).relative_to(SOURCE)
                require(digest(config_path) == slot["sha256"], config_path)
                config = load_config(config_path)
                require(inputs(config) == slot["inputs"] and digest(config.prompt) == slot["prompt_sha256"], slot)
                require(digest(RESULTS / Path(slot["criteria"]).relative_to(SOURCE)) == slot["criteria_sha256"], slot)
            elif store:
                check_private(store, slot["criteria"], slot["criteria_sha256"])
                check_private(store, slot["config"], slot["sha256"])
            if store:
                check_private(store, attempt["inventory"], attempt["inventory_sha256"])
                for ref in row.get("checks", row.get("evidence", [])):
                    check_private(store, ref["path"], ref["sha256"])
            cells[slot["provider"], slot.get("case", "booking-slot")] += 1
    require(cells == {("claude", "repeated-review"): 5, ("codex", "quota-grace"): 5,
                      ("codex", "booking-slot"): 3, ("claude", "booking-slot"): 3}, cells)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--private-store", type=Path, help="Authorized writing-explicit-rationale store root")
    args = parser.parse_args()
    verify_public_suite()
    verify_adopted_runs(args.private_store)
    print("Verified 14 runnable configs, the baseline and parent comparison, and 16 adopted-variant results.")
