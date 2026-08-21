"""Behavior contracts for the charter-first campaign result processor."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import ModuleType
from unittest.mock import patch

PROCESSOR_PATH = Path(__file__).resolve().parents[1] / "core_result_processor.py"
ORIGINAL_SKILL_SHA256 = "1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec"
CURRENT_SKILL_SHA256 = "4e5b52205c560448579eaafacc4ad55c81ae4156bb3bf6b1997b68669cadae42"
ORIGINAL_ID = "main@5219997ff580f7cfac4115e4c38d396d3dd9101e"
CURRENT_ID = f"worktree-sha256:{CURRENT_SKILL_SHA256}"
CAMPAIGN_PREFIX = "task-26-charter-first-core"
MODEL = "gpt-5.6-sol"
INPUTS = {"prompt": "2" * 64, "rubric": "3" * 64, "fixture": "4" * 64,
          "dependency": "5" * 64, "harness": "6" * 64, "executable": "7" * 64}
LEDGERS = {"core_behavior", "deterministic_protocol", "task_fixture_fidelity", "readability", "infrastructure"}


def canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_json(value))


def campaign_id(tier: str) -> str:
    return f"{CAMPAIGN_PREFIX}:{tier}"


class ResultProcessorContractTests(unittest.TestCase):
    """Every test names the production defect it is intended to catch."""

    def load_processor(self) -> ModuleType:
        self.assertTrue(PROCESSOR_PATH.is_file(),
                        "production defect: core_result_processor.py is absent; it must expose ResultContractError and process_campaign")
        spec = importlib.util.spec_from_file_location("core_result_processor_under_test", PROCESSOR_PATH)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        self.assertTrue(hasattr(module, "ResultContractError"))
        self.assertTrue(hasattr(module, "process_campaign"))
        return module

    def process(self, contract: Path, results: Path) -> dict:
        outcome = self.load_processor().process_campaign(contract, results)
        self.assertIsInstance(outcome, dict)
        self.assertTrue({"ledgers", "semantic_verdict", "protocol_verdict", "acceptance_verdict", "repetitions"} <= outcome.keys())
        return outcome

    def error(self, contract: Path, results: Path) -> None:
        module = self.load_processor()
        with self.assertRaises(module.ResultContractError):
            module.process_campaign(contract, results)

    def error_branch(self, contract: Path, results: Path, pattern: str) -> None:
        module = self.load_processor()
        with self.assertRaisesRegex(module.ResultContractError, pattern):
            module.process_campaign(contract, results)

    def public_error(self, contract: Path, results: Path) -> None:
        module = self.load_processor()
        try:
            module.process_campaign(contract, results)
        except module.ResultContractError:
            return
        except BaseException as error:
            self.fail(f"public API leaked {type(error).__name__}")
        self.fail("public API accepted malformed material")

    def fifo_error(self, contract: Path, results: Path) -> None:
        program = """import importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location('fifo_processor', sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
try:
    module.process_campaign(Path(sys.argv[2]), Path(sys.argv[3]))
except module.ResultContractError:
    raise SystemExit(0)
except BaseException as error:
    print(type(error).__name__, file=sys.stderr)
    raise SystemExit(2)
raise SystemExit(3)
"""
        try:
            completed = subprocess.run([sys.executable, "-c", program, str(PROCESSOR_PATH), str(contract), str(results)], timeout=5, capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            self.fail("readerless FIFO exceeded the five-second hang-only limit")
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def contract(self, *, tier="rebuild-low", applicable=True, scenarios=("gate-boundary",)) -> dict:
        effort = "low" if tier == "rebuild-low" else "high"
        return {
            "schema_version": 1, "campaign": {"id": campaign_id(tier), "tier": tier, "model": MODEL, "effort": effort},
            "arms": {
                "original": {"identity": ORIGINAL_ID, "skill_sha256": ORIGINAL_SKILL_SHA256, "input_hashes": dict(INPUTS)},
                "current": {"identity": CURRENT_ID, "skill_sha256": CURRENT_SKILL_SHA256, "input_hashes": dict(INPUTS)},
            },
            "scenarios": [{"id": scenario, "core_invariants": ["DD-I1", "DD-I2"],
                           "authenticated_protocol_boundaries": ["DD-VERDICT", "CHECKER-V1"],
                           "protocol_applicable": applicable, "requires_state_evidence": False}
                          for scenario in scenarios],
        }

    def record(self, *, arm: str, repetition: int, scenario="gate-boundary", misses=None,
               semantic="PASS", protocol="PASS", state=None, artifact="completed response", tier="rebuild-low") -> dict:
        original = arm == "original"
        effort = "low" if tier == "rebuild-low" else "high"
        return {
            "schema_version": 1, "campaign_id": campaign_id(tier), "model": MODEL, "effort": effort,
            "arm": arm, "arm_identity": ORIGINAL_ID if original else CURRENT_ID,
            "scenario": scenario, "repetition": repetition, "attempt": "a1",
            "fresh_context": f"{campaign_id(tier)}/{arm}/{scenario}/run-{repetition}", "status": "completed",
            "raw_artifact": artifact, "raw_artifact_sha256": digest(artifact),
            "skill_sha256": ORIGINAL_SKILL_SHA256 if original else CURRENT_SKILL_SHA256,
            "input_hashes": dict(INPUTS), "claimed_semantic_verdict": semantic,
            "claimed_protocol_verdict": protocol, "state_evidence": {} if state is None else state,
            "misses": [] if misses is None else misses,
        }

    def records(self, *, repetitions=3, scenarios=("gate-boundary",), state=None, tier="rebuild-low") -> list[dict]:
        return [self.record(arm=arm, scenario=scenario, repetition=rep, state=state, tier=tier)
                for arm in ("original", "current") for scenario in scenarios
                for rep in range(1, repetitions + 1)]

    def write_results(self, root: Path, records: list[dict]) -> None:
        for index, record in enumerate(records, 1):
            write_json(root / f"result-{index}.json", record)

    def counts(self, outcome: dict, required: int, completed: int) -> None:
        for arm in ("original", "current"):
            summary = outcome["repetitions"][arm]["gate-boundary"]
            self.assertEqual(summary["required"], required)
            self.assertEqual(summary["completed"], completed)

    def git_repo(self, root: Path) -> tuple[Path, dict, str]:
        repo = root / "repo"
        repo.mkdir(parents=True)
        for command in (("git", "init", "-q"), ("git", "config", "user.email", "contract@example.test"),
                        ("git", "config", "user.name", "Contract Test")):
            subprocess.run(command, cwd=repo, check=True)
        (repo / "required.txt").write_text("observed state\n")
        subprocess.run(["git", "add", "required.txt"], cwd=repo, check=True)
        subprocess.run(["git", "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "frozen"], cwd=repo, check=True)
        frozen = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
        (repo / "later.txt").write_text("later\n")
        subprocess.run(["git", "add", "later.txt"], cwd=repo, check=True)
        subprocess.run(["git", "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "later"], cwd=repo, check=True)
        wrong = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
        subprocess.run(["git", "checkout", "-q", frozen], cwd=repo, check=True)
        return repo, {"repository": str(repo), "head": frozen,
                      "required_paths": {"required.txt": digest("observed state\n")},
                      "forbidden_paths": ["forbidden.txt"], "clean_worktree": True,
                      "invariant": "DD-I1"}, wrong

    def infrastructure_record(self, *, arm: str, repetition: int, scenario="gate-boundary", tier="rebuild-low", attempt=1) -> dict:
        """A transport failure has provenance but no evaluable artifact or behavioral verdict."""
        record = self.record(arm=arm, repetition=repetition, scenario=scenario, tier=tier)
        record.update({"attempt": f"infrastructure-{attempt}", "fresh_context": f"{campaign_id(tier)}/{arm}/{scenario}/run-{repetition}/infrastructure-{attempt}",
                       "status": "infrastructure_error", "misses": [{"criterion": "provider 503", "ledger": "infrastructure"}]})
        del record["raw_artifact"]
        del record["raw_artifact_sha256"]
        del record["claimed_semantic_verdict"]
        del record["claimed_protocol_verdict"]
        del record["state_evidence"]
        return record

    def infrastructure_record_with_empty_state(self, **kwargs: object) -> dict:
        """Diagnostic-only infrastructure form: optional evidence is ignored, not behavioral."""
        record = self.infrastructure_record(**kwargs)
        record["state_evidence"] = {}
        return record


    def restore_repo(self, repo: Path, head: str) -> None:
        subprocess.run(["git", "reset", "--hard", "-q", head], cwd=repo, check=True)
        subprocess.run(["git", "clean", "-fdq"], cwd=repo, check=True)
        self.assertEqual(subprocess.check_output(["git", "status", "--porcelain"], cwd=repo, text=True), "")

    def test_five_ledger_classification_is_exhaustive_and_only_core_or_applicable_protocol_blocks(self) -> None:
        """Catches accepting invalid ownership or allowing a non-blocking ledger to decide acceptance."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            valid = self.records(repetitions=5)
            valid[0]["misses"] = [
                {"criterion": "gate", "ledger": "core_behavior", "invariant": "DD-I1"},
                {"criterion": "bytes", "ledger": "deterministic_protocol", "boundary": "DD-VERDICT"},
                {"criterion": "shape", "ledger": "task_fixture_fidelity"},
                {"criterion": "clarity", "ledger": "readability"},
            ]
            valid.append(self.infrastructure_record(arm="original", repetition=1))
            self.write_results(root / "valid-ledgers", valid)
            outcome = self.process(contract, root / "valid-ledgers")
            self.assertEqual(set(outcome["ledgers"]), LEDGERS)
            for ledger in LEDGERS:
                self.assertEqual(outcome["ledgers"][ledger]["count"], 1)
            self.assertEqual(outcome["acceptance_verdict"], "FAIL")
            for ledger in ("task_fixture_fidelity", "readability"):
                records = self.records(); records[0]["misses"] = [{"criterion": ledger, "ledger": ledger}]
                path = root / f"nonblocking-{ledger}"; self.write_results(path, records)
                self.assertEqual(self.process(contract, path)["acceptance_verdict"], "PASS")
            records = self.records(repetitions=5); records[0]["misses"] = [{"criterion": "gate", "ledger": "core_behavior", "invariant": "DD-I1"}]
            self.write_results(root / "core-block", records)
            self.assertEqual(self.process(contract, root / "core-block")["acceptance_verdict"], "FAIL")
            records = self.records(); records[0]["misses"] = [{"criterion": "bytes", "ledger": "deterministic_protocol", "boundary": "DD-VERDICT"}]
            self.write_results(root / "protocol-block", records)
            self.assertEqual(self.process(contract, root / "protocol-block")["acceptance_verdict"], "FAIL")
            invalid = [
                {"criterion": "zero", "ledger": None}, {"criterion": "multiple", "ledger": ["core_behavior", "readability"]},
                {"criterion": "unknown", "ledger": "unknown"},
                {"criterion": "missing invariant", "ledger": "core_behavior"},
                {"criterion": "bad invariant", "ledger": "core_behavior", "invariant": "DD-I9"},
                {"criterion": "two invariants", "ledger": "core_behavior", "invariant": ["DD-I1", "DD-I2"]},
                {"criterion": "missing boundary", "ledger": "deterministic_protocol"},
                {"criterion": "bad boundary", "ledger": "deterministic_protocol", "boundary": "other"},
                {"criterion": "two boundaries", "ledger": "deterministic_protocol", "boundary": ["DD-VERDICT", "CHECKER-V1"]},
            ]
            for index, miss in enumerate(invalid):
                records = self.records(); records[0]["misses"] = [miss]
                path = root / f"invalid-{index}"; self.write_results(path, records); self.error(contract, path)

    def test_semantic_and_protocol_verdicts_derive_from_ledgers_not_claimed_summaries(self) -> None:
        """Catches trusting claimed summaries rather than core/state and deterministic-protocol evidence."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            protocol_fail = self.records()
            protocol_fail[0].update({"claimed_semantic_verdict": "FAIL", "claimed_protocol_verdict": "PASS",
                                     "misses": [{"criterion": "bytes", "ledger": "deterministic_protocol", "boundary": "DD-VERDICT"}]})
            self.write_results(root / "semantic-pass-protocol-fail", protocol_fail)
            outcome = self.process(contract, root / "semantic-pass-protocol-fail")
            self.assertEqual((outcome["semantic_verdict"], outcome["protocol_verdict"]), ("PASS", "FAIL"))
            semantic_fail = self.records(repetitions=5)
            semantic_fail[0].update({"claimed_semantic_verdict": "PASS", "claimed_protocol_verdict": "FAIL",
                                     "misses": [{"criterion": "gate", "ledger": "core_behavior", "invariant": "DD-I1"}]})
            self.write_results(root / "semantic-fail-protocol-pass", semantic_fail)
            outcome = self.process(contract, root / "semantic-fail-protocol-pass")
            self.assertEqual((outcome["semantic_verdict"], outcome["protocol_verdict"]), ("FAIL", "PASS"))
            na_contract = root / "na-contract.json"; write_json(na_contract, self.contract(applicable=False))
            na = self.records(); na[0]["claimed_protocol_verdict"] = "FAIL"; self.write_results(root / "na", na)
            outcome = self.process(na_contract, root / "na")
            self.assertEqual((outcome["semantic_verdict"], outcome["protocol_verdict"]), ("PASS", "NOT_APPLICABLE"))

    def test_independent_git_state_verification_rejects_each_frozen_state_deviation_despite_valid_metadata(self) -> None:
        """Catches trusting success wording instead of independently checking the real frozen Git state."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, wrong_head = self.git_repo(root); records = self.records(state={"agent_report": "success"})
            def semantic_failure(name: str, *, clean=True) -> None:
                contract_data = self.contract()
                case_state = dict(state); case_state["clean_worktree"] = clean
                contract_data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": case_state})
                contract = root / f"{name}-contract.json"; write_json(contract, contract_data)
                self.write_results(root / name, records)
                outcome = self.process(contract, root / name)
                self.assertEqual((outcome["semantic_verdict"], outcome["acceptance_verdict"]), ("FAIL", "FAIL"))
                self.assertEqual(outcome["ledgers"]["core_behavior"]["count"], 1)
                state_entry = outcome["ledgers"]["core_behavior"]["entries"][0]
                for key, expected in (("invariant", "DD-I1"), ("status", "independently_observed"), ("source", "state_contract")):
                    with self.subTest(state_deviation=name, field=key):
                        self.assertEqual(state_entry.get(key), expected)
                self.restore_repo(repo, state["head"])
            (repo / "required.txt").unlink(); semantic_failure("missing-required", clean=False)
            (repo / "required.txt").write_text("wrong bytes\n"); semantic_failure("wrong-hash", clean=False)
            (repo / "forbidden.txt").write_text("forbidden\n"); semantic_failure("forbidden", clean=False)
            (repo / "dirty.txt").write_text("dirty\n"); semantic_failure("dirty")
            subprocess.run(["git", "checkout", "-q", wrong_head], cwd=repo, check=True); semantic_failure("wrong-head")
            contract_data = self.contract(); contract_data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "correct-contract.json"; write_json(contract, contract_data)
            for record in records: record["state_evidence"] = {"agent_report": "unrelated wording"}
            self.write_results(root / "correct", records)
            self.assertEqual(self.process(contract, root / "correct")["semantic_verdict"], "PASS")

    def test_arm_provenance_rejects_identity_hash_and_each_input_mismatch_including_cross_arm_inequality(self) -> None:
        """Catches a processor that does not bind records to their frozen arm and identical input set."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            valid = self.records(); self.write_results(root / "valid", valid)
            self.assertEqual(self.process(contract, root / "valid")["acceptance_verdict"], "PASS")
            wrong_hash = self.records()
            for record in wrong_hash:
                if record["arm"] == "original": record["skill_sha256"] = "f" * 64
            self.write_results(root / "wrong-hash", wrong_hash); self.error(contract, root / "wrong-hash")
            swapped = self.records()
            for record in swapped:
                record["arm_identity"] = CURRENT_ID if record["arm"] == "original" else ORIGINAL_ID
            self.write_results(root / "swapped-identity", swapped); self.error(contract, root / "swapped-identity")
            for key in INPUTS:
                changed = self.records()
                for record in changed: record["input_hashes"][key] = "f" * 64
                path = root / f"changed-{key}"
                self.write_results(path, changed); self.error(contract, path)
            unequal = self.contract(); unequal["arms"]["current"]["input_hashes"]["harness"] = "9" * 64
            unequal_path = root / "unequal-contract.json"; write_json(unequal_path, unequal)
            records = self.records(repetitions=5)
            for record in records:
                if record["arm"] == "current": record["input_hashes"]["harness"] = "9" * 64
            self.write_results(root / "unequal", records); self.error(unequal_path, root / "unequal")
            unequal_keys = self.contract(); del unequal_keys["arms"]["current"]["input_hashes"]["executable"]
            unequal_keys_path = root / "unequal-keys-contract.json"; write_json(unequal_keys_path, unequal_keys)
            records = self.records()
            for record in records:
                if record["arm"] == "current": del record["input_hashes"]["executable"]
            self.write_results(root / "unequal-keys", records); self.error(unequal_keys_path, root / "unequal-keys")
            wrong_model = self.records()
            for record in wrong_model: record["model"] = "other-model"
            self.write_results(root / "wrong-model", wrong_model); self.error(contract, root / "wrong-model")
            wrong_effort = self.records()
            for record in wrong_effort: record["effort"] = "high"
            self.write_results(root / "wrong-effort", wrong_effort); self.error(contract, root / "wrong-effort")

    def test_repetition_policy_requires_exact_fresh_completed_counts_and_ledgers_infrastructure_separately(self) -> None:
        """Catches wrong low/high counts, reused contexts, or infrastructure substituted for behavioral repetitions."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); low = root / "low.json"; write_json(low, self.contract())
            stable = self.records(); self.write_results(root / "stable", stable); self.counts(self.process(low, root / "stable"), 3, 3)
            for trigger in ("split", "rubric_ambiguity", "task_fidelity_instability"):
                records = self.records(repetitions=5)
                for arm in ("original", "current"):
                    first = next(x for x in records if x["arm"] == arm and x["repetition"] == 1)
                    if trigger == "split":
                        next(x for x in records if x["arm"] == arm and x["repetition"] == 3)["misses"] = [{"criterion": "gate", "ledger": "core_behavior", "invariant": "DD-I1"}]
                    else: first[trigger] = True
                path = root / f"expanded-{trigger}"; self.write_results(path, records); self.counts(self.process(low, path), 5, 5)
            split_six = self.records(repetitions=6)
            for arm in ("original", "current"):
                next(x for x in split_six if x["arm"] == arm and x["repetition"] == 3)["misses"] = [{"criterion": "gate", "ledger": "core_behavior", "invariant": "DD-I1"}]
            self.write_results(root / "split-six", split_six); self.error(low, root / "split-six")
            for name, records in (("low-two", self.records(repetitions=2)), ("low-four", self.records(repetitions=4)), ("stable-five", self.records(repetitions=5))):
                self.write_results(root / name, records); self.error(low, root / name)
            duplicate = self.records(); duplicate_copy = dict(duplicate[0]); duplicate_copy["fresh_context"] = f"{campaign_id('rebuild-low')}/original/gate-boundary/duplicate-repetition"; duplicate.append(duplicate_copy)
            self.write_results(root / "duplicate-repetition", duplicate); self.error(low, root / "duplicate-repetition")
            reused_context = self.records(); reused_context[1]["fresh_context"] = reused_context[0]["fresh_context"]
            self.write_results(root / "reused-fresh-context", reused_context); self.error(low, root / "reused-fresh-context")
            gap = self.records(); gap[-1].update({"repetition": 4, "fresh_context": f"{campaign_id('rebuild-low')}/current/gate-boundary/run-4"}); self.write_results(root / "gap", gap); self.error(low, root / "gap")
            infrastructure = self.records(); infrastructure.append(self.infrastructure_record(arm="original", repetition=1))
            self.write_results(root / "with-infrastructure", infrastructure); outcome = self.process(low, root / "with-infrastructure")
            self.assertEqual((outcome["semantic_verdict"], outcome["protocol_verdict"], outcome["acceptance_verdict"]), ("PASS", "PASS", "PASS")); self.assertEqual(outcome["ledgers"]["infrastructure"]["count"], 1)
            self.counts(outcome, 3, 3)
            substitution = self.records(); substitution[-1] = self.infrastructure_record(arm="current", repetition=3)
            self.write_results(root / "substitution", substitution); self.error(low, root / "substitution")
            high = root / "high.json"; write_json(high, self.contract(tier="stabilized-high"))
            good_high = self.records(tier="stabilized-high"); self.write_results(root / "high-three", good_high); self.counts(self.process(high, root / "high-three"), 3, 3)
            for name, records in (("high-two", self.records(repetitions=2, tier="stabilized-high")), ("high-four", self.records(repetitions=4, tier="stabilized-high"))): self.write_results(root / name, records); self.error(high, root / name)
            wrong_campaign = self.records(tier="stabilized-high")
            for record in wrong_campaign:
                record["campaign_id"] = campaign_id("rebuild-low")
                record["fresh_context"] = record["fresh_context"].replace(campaign_id("stabilized-high"), campaign_id("rebuild-low"), 1)
            self.write_results(root / "high-reused-low-campaign", wrong_campaign); self.error(high, root / "high-reused-low-campaign")

    def test_fail_closed_rejects_missing_campaign_material_state_and_tampering(self) -> None:
        """Catches accepting missing arms/scenarios/state or malformed, altered, and extra result material."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); scenarios = ("gate-boundary", "second-boundary"); contract = root / "contract.json"
            write_json(contract, self.contract(scenarios=scenarios)); complete = self.records(scenarios=scenarios)
            self.write_results(root / "complete", complete)
            outcome = self.process(contract, root / "complete")
            self.assertEqual(outcome["acceptance_verdict"], "PASS")
            for arm in ("original", "current"):
                for scenario in scenarios:
                    summary = outcome["repetitions"][arm][scenario]
                    self.assertEqual((summary["required"], summary["completed"]), (3, 3))
            cases = {
                "missing-arm": [x for x in complete if x["arm"] == "original"],
                "missing-scenario": [x for x in complete if x["scenario"] == "gate-boundary"],
                "missing-repetition": complete[:-1],
            }
            for name, records in cases.items(): self.write_results(root / name, records); self.error(contract, root / name)
            malformed = self.records(scenarios=scenarios); malformed[0]["repetition"] = "one"; self.write_results(root / "malformed", malformed); self.error(contract, root / "malformed")
            missing_raw = self.records(scenarios=scenarios); del missing_raw[0]["raw_artifact"]; self.write_results(root / "missing-raw", missing_raw); self.error(contract, root / "missing-raw")
            altered = self.records(scenarios=scenarios); altered[0]["raw_artifact"] = "altered"; self.write_results(root / "altered", altered); self.error(contract, root / "altered")
            rewrite = self.records(scenarios=scenarios)
            for record in rewrite:
                record.update({"skill_sha256": "a" * 64, "raw_artifact": "rewritten", "raw_artifact_sha256": digest("rewritten")})
            self.write_results(root / "rewrite", rewrite); self.error(contract, root / "rewrite")
            extra = self.records(scenarios=scenarios); self.write_results(root / "extra", extra); (root / "extra" / "unexpected-note.txt").write_text("not a result record\n"); self.error(contract, root / "extra")
            extra_result = self.records(scenarios=scenarios); self.write_results(root / "extra-result", extra_result)
            write_json(root / "extra-result" / "extra-result.json", self.record(arm="original", scenario="gate-boundary", repetition=1))
            self.error(contract, root / "extra-result")
            repo, state, _ = self.git_repo(root / "state"); state_contract = self.contract(); state_contract["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state}); state_path = root / "state-contract.json"; write_json(state_path, state_contract)
            missing_state = self.records(state={"agent_report": "present"}); del missing_state[0]["state_evidence"]; self.write_results(root / "missing-state", missing_state); self.error(state_path, root / "missing-state")

    def test_repair_repetition_expands_every_first_three_polarity_and_rejects_late_flags(self) -> None:
        """Catches a processor that recognizes one split polarity or lets a fourth-run flag authorize expansion."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            for name, failed in (("pass-pass-fail", (3,)), ("pass-fail-pass", (2,)), ("pass-fail-fail", (2, 3)),
                                 ("fail-pass-pass", (1,)), ("fail-pass-fail", (1, 3)), ("fail-fail-pass", (1, 2))):
                with self.subTest(polarity=name):
                    records = self.records(repetitions=5)
                    split_arm = "current" if name == "fail-pass-fail" else "original"
                    for repetition in failed:
                        next(item for item in records if item["arm"] == split_arm and item["repetition"] == repetition)["misses"] = [{"criterion": "gate", "ledger": "core_behavior", "invariant": "DD-I1"}]
                    path = root / name; self.write_results(path, records)
                    self.counts(self.process(contract, path), 5, 5)
            for flag in ("rubric_ambiguity", "task_fidelity_instability"):
                for repetition in (4, 5):
                    with self.subTest(flag=flag, repetition=repetition):
                        records = self.records(repetitions=5)
                        records[repetition - 1][flag] = True
                        path = root / f"late-{flag}-{repetition}"; self.write_results(path, records)
                        self.error(contract, path)

    def test_repair_split_first_three_requires_expanded_five_record_cell(self) -> None:
        """Catches accepting a first-three semantic split without both arms' required runs 4 and 5."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records()
            next(record for record in records if record["arm"] == "original" and record["repetition"] == 2)["misses"] = [{"criterion": "gate", "ledger": "core_behavior", "invariant": "DD-I1"}]
            self.write_results(root / "split-three", records)
            self.error(contract, root / "split-three")

    def test_repair_ledger_entries_retain_authenticated_and_attempt_provenance(self) -> None:
        """Catches ledger output that drops invariant/boundary or record provenance."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records(repetitions=5)
            records[0]["misses"] = [{"criterion": "gate", "ledger": "core_behavior", "invariant": "DD-I1"}, {"criterion": "bytes", "ledger": "deterministic_protocol", "boundary": "DD-VERDICT"}]
            self.write_results(root / "entries", records)
            outcome = self.process(contract, root / "entries")
            expected = {"arm": "original", "scenario": "gate-boundary", "repetition": 1, "attempt": "a1",
                        "fresh_context": f"{campaign_id('rebuild-low')}/original/gate-boundary/run-1", "status": "completed"}
            core = outcome["ledgers"]["core_behavior"]["entries"][0]
            protocol = outcome["ledgers"]["deterministic_protocol"]["entries"][0]
            for name, entry, owner, value in (("core", core, "invariant", "DD-I1"), ("protocol", protocol, "boundary", "DD-VERDICT")):
                with self.subTest(ledger=name):
                    projection = {key: entry.get(key) for key in expected} | {owner: entry.get(owner)}
                    self.assertEqual(projection, expected | {owner: value})
            infra = self.records(); infra.append(self.infrastructure_record_with_empty_state(arm="original", repetition=1))
            self.write_results(root / "infra-provenance", infra)
            entry = self.process(contract, root / "infra-provenance")["ledgers"]["infrastructure"]["entries"][0]
            infra_expected = dict(expected, attempt="infrastructure-1", fresh_context=f"{campaign_id('rebuild-low')}/original/gate-boundary/run-1/infrastructure-1", status="infrastructure_error")
            with self.subTest(ledger="infrastructure"):
                self.assertEqual({key: entry.get(key) for key in infra_expected}, infra_expected)

    def test_repair_infrastructure_is_structurally_disjoint(self) -> None:
        """Catches structural infrastructure records treated as completed evidence."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records(); records.append(self.infrastructure_record(arm="original", repetition=1))
            self.write_results(root / "structural-infrastructure", records)
            outcome = self.process(contract, root / "structural-infrastructure")
            entry = outcome["ledgers"]["infrastructure"]["entries"][0]
            for key in ("arm", "scenario", "repetition", "attempt", "fresh_context", "status"):
                self.assertIn(key, entry)
            self.assertEqual((entry["attempt"], entry["status"]), ("infrastructure-1", "infrastructure_error"))
            completed_infrastructure = self.records(); completed_infrastructure[0]["misses"] = [{"criterion": "wrong status", "ledger": "infrastructure"}]
            self.write_results(root / "completed-infrastructure", completed_infrastructure)
            self.error(contract, root / "completed-infrastructure")

    def test_repair_fresh_context_binds_exact_record_identity(self) -> None:
        """Catches accepting unique contexts swapped between otherwise valid arm/run identities."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            for name, scenarios, first, second in (("arm", ("gate-boundary",), ("original", "gate-boundary", 1), ("current", "gate-boundary", 1)),
                                                   ("scenario", ("gate-boundary", "second"), ("original", "gate-boundary", 1), ("original", "second", 1)),
                                                   ("repetition", ("gate-boundary",), ("original", "gate-boundary", 1), ("original", "gate-boundary", 2))):
                with self.subTest(component=name):
                    case_contract = self.contract(scenarios=scenarios); path = root / f"{name}.json"; write_json(path, case_contract)
                    records = self.records(scenarios=scenarios)
                    left = next(item for item in records if (item["arm"], item["scenario"], item["repetition"]) == first)
                    right = next(item for item in records if (item["arm"], item["scenario"], item["repetition"]) == second)
                    left["fresh_context"], right["fresh_context"] = right["fresh_context"], left["fresh_context"]
                    self.write_results(root / name, records); self.error(path, root / name)
            records = self.records(); infra = self.infrastructure_record_with_empty_state(arm="original", repetition=1)
            infra["fresh_context"] = f"{campaign_id('rebuild-low')}/original/gate-boundary/run-1/infrastructure-2"; records.append(infra)
            self.write_results(root / "infrastructure-attempt", records); self.error(contract, root / "infrastructure-attempt")

    def test_repair_strict_json_scalar_shape_and_protocol_na_contracts(self) -> None:
        """Catches duplicate JSON keys, loose scalars, overlarge invariants, and rejected explicit protocol N/A."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); records = self.records(); self.write_results(root / "records", records)
            duplicate_contract = root / "duplicate-contract.json"
            encoded = canonical_json(self.contract())
            duplicate_contract.write_bytes(encoded.replace(b'"schema_version":1', b'"schema_version":1,"schema_version":1', 1))
            self.error(duplicate_contract, root / "records")
            boolean_contract = self.contract(); boolean_contract["schema_version"] = True; boolean_path = root / "boolean-contract.json"; write_json(boolean_path, boolean_contract)
            self.error(boolean_path, root / "records")
            five = self.contract(); five["scenarios"][0]["core_invariants"].extend(["DD-I3", "DD-I4", "DD-I5"]); five_path = root / "five.json"; write_json(five_path, five)
            self.error(five_path, root / "records")
            no_protocol = self.contract(applicable=False); no_protocol["scenarios"][0]["authenticated_protocol_boundaries"] = []; no_protocol_path = root / "na.json"; write_json(no_protocol_path, no_protocol)
            self.assertEqual(self.process(no_protocol_path, root / "records")["protocol_verdict"], "NOT_APPLICABLE")

    def test_repair_state_confinement_inventory_and_deterministic_order(self) -> None:
        """Catches symlink escape, filename gaps, and nondeterministic public ledger ordering."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root); external = root / "outside"; external.mkdir(); (external / "required.txt").write_text("observed state\n")
            (repo / "linked").symlink_to(external, target_is_directory=True)
            state["required_paths"] = {"linked/required.txt": digest("observed state\n")}; state["clean_worktree"] = False
            contract = self.contract(); contract["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state}); contract_path = root / "state-contract.json"; write_json(contract_path, contract)
            records = self.records(state={"agent_report": "present"}); self.write_results(root / "symlink", records)
            self.error(contract_path, root / "symlink")
            plain = self.contract(); plain_path = root / "plain-contract.json"; write_json(plain_path, plain)
            gapped = self.records(); gap_root = root / "filename-gap"
            for index, record in enumerate(gapped, 1): write_json(gap_root / f"result-{index * 2 - 1}.json", record)
            self.error(plain_path, gap_root)
            ordered = self.records(repetitions=5); ordered[0]["misses"] = [{"criterion": "core", "ledger": "core_behavior", "invariant": "DD-I1"}]
            ordered[1]["misses"] = [{"criterion": "read", "ledger": "readability"}]
            self.write_results(root / "order", ordered); outcome = self.process(plain_path, root / "order")
            self.assertEqual(list(outcome["ledgers"]), ["core_behavior", "deterministic_protocol", "task_fixture_fidelity", "readability", "infrastructure"])

    def test_repair_result_duplicate_keys_and_strict_optional_scalars(self) -> None:
        """Catches duplicate result keys and truthy optional flags instead of strict scalar validation."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records(); result_root = root / "duplicate-result"
            for index, record in enumerate(records, 1):
                if index == 1:
                    encoded = canonical_json(record).replace(b'"schema_version":1', b'"schema_version":1,"schema_version":1', 1)
                    (result_root / "result-1.json").parent.mkdir(parents=True, exist_ok=True)
                    (result_root / "result-1.json").write_bytes(encoded)
                else:
                    write_json(result_root / f"result-{index}.json", record)
            self.error(contract, result_root)
            flagged = self.records(repetitions=5); flagged[3]["rubric_ambiguity"] = "false"
            self.write_results(root / "string-flag", flagged)
            self.error(contract, root / "string-flag")

    def test_repair_malformed_state_head_is_contractual_not_semantic(self) -> None:
        """Catches malformed frozen Git HEAD being converted into a semantic state miss."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root); state["head"] = "not-a-git-object"
            contract = self.contract(); contract["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract_path = root / "malformed-state-contract.json"; write_json(contract_path, contract)
            records = self.records(state={"agent_report": "present"}); self.write_results(root / "records", records)
            self.error(contract_path, root / "records")

    def test_repair_result_filename_inventory_has_no_gaps(self) -> None:
        """Catches accepting valid result records whose materialized filename inventory is gapped."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            results = root / "gapped"
            for index, record in enumerate(self.records(), 1):
                write_json(results / f"result-{index * 2 - 1}.json", record)
            self.error(contract, results)

    def test_repair_public_ledger_order_is_canonical(self) -> None:
        """Catches public ledger containers whose iteration order depends on hash or directory order."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records(repetitions=5); records[0]["misses"] = [{"criterion": "core", "ledger": "core_behavior", "invariant": "DD-I1"}]
            self.write_results(root / "ordered", records)
            outcome = self.process(contract, root / "ordered")
            self.assertEqual(list(outcome["ledgers"]), ["core_behavior", "deterministic_protocol", "task_fixture_fidelity", "readability", "infrastructure"])

    def test_repair_completed_records_cannot_claim_infrastructure(self) -> None:
        """Catches completed behavioral evidence carrying an infrastructure miss."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            completed = self.records(); completed[0]["misses"] = [{"criterion": "transport", "ledger": "infrastructure"}]
            self.write_results(root / "completed", completed); self.error(contract, root / "completed")

    def test_repair_structural_infrastructure_attempts_are_contiguous(self) -> None:
        """Catches a structural infrastructure attempt inventory that silently skips attempt numbers."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records(); attempt = self.infrastructure_record_with_empty_state(arm="original", repetition=1, attempt=3)
            records.append(attempt); self.write_results(root / "gapped", records)
            self.error_branch(contract, root / "gapped", "contiguous")

    def test_repair_infrastructure_attempt_syntax_rejects_zero_padding_and_wrong_prefix(self) -> None:
        """Catches malformed infrastructure attempts before they can enter the retry inventory."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            for attempt_name in ("infrastructure-0", "infrastructure-01", "retry-1"):
                with self.subTest(attempt=attempt_name):
                    records = self.records(); attempt = self.infrastructure_record_with_empty_state(arm="original", repetition=1)
                    attempt.update({"attempt": attempt_name, "fresh_context": f"{campaign_id('rebuild-low')}/original/gate-boundary/run-1/{attempt_name}"})
                    records.append(attempt); path = root / attempt_name; self.write_results(path, records)
                    self.error_branch(contract, path, "attempt malformed")

    def test_repair_infrastructure_context_allows_attempt_one_for_two_planned_repetitions(self) -> None:
        """Catches a retry context that cannot distinguish two planned repetitions."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records(); records.extend([self.infrastructure_record_with_empty_state(arm="original", repetition=1), self.infrastructure_record_with_empty_state(arm="original", repetition=2)])
            self.write_results(root / "two-slots", records)
            outcome = self.process(contract, root / "two-slots")
            self.assertEqual(outcome["ledgers"]["infrastructure"]["count"], 2)

    def test_repair_infrastructure_rejects_unplanned_planned_context(self) -> None:
        """Catches accepting a repetition outside the planned completed slots."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            unplanned = self.records(); unplanned.append(self.infrastructure_record_with_empty_state(arm="original", repetition=99))
            self.write_results(root / "unplanned", unplanned); self.error_branch(contract, root / "unplanned", "repetition.*planned")

    def test_repair_infrastructure_rejects_fourth_planned_retry(self) -> None:
        """Catches accepting a fourth consecutive retry for one planned repetition."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            fourth = self.records()
            fourth.extend([self.infrastructure_record_with_empty_state(arm="original", repetition=1, attempt=number) for number in range(1, 5)])
            self.write_results(root / "fourth", fourth); self.error_branch(contract, root / "fourth", "retry.*limit")

    def test_repair_git_cleanliness_ignores_local_hide_untracked(self) -> None:
        """Catches Git status inheriting local hide-untracked configuration."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root)
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data)
            records = self.records(state={"agent_report": "present"})
            (repo / "hidden.txt").write_text("untracked\n")
            subprocess.run(["git", "config", "status.showUntrackedFiles", "no"], cwd=repo, check=True)
            self.write_results(root / "hidden", records)
            self.assertEqual(self.process(contract, root / "hidden")["semantic_verdict"], "FAIL")

    def test_repair_git_state_stat_refresh_preserves_index_bytes(self) -> None:
        """Catches a read-only state inspection refreshing Git's index after a stat-only change."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root)
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data); records = self.records(state={"agent_report": "present"})
            path = repo / "required.txt"; stamp = path.stat(); os.utime(path, ns=(stamp.st_atime_ns, stamp.st_mtime_ns + 1_000_000_000))
            before = (repo / ".git" / "index").read_bytes(); self.write_results(root / "records", records)
            with patch.dict(os.environ, {"GIT_OPTIONAL_LOCKS": "1"}): self.process(contract, root / "records")
            self.assertEqual((repo / ".git" / "index").read_bytes(), before)

    def test_repair_unreadable_contract_normalizes_to_result_contract_error(self) -> None:
        """Catches a public raw OSError for actual unreadable contract material."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract()); self.write_results(root / "records", self.records())
            mode = contract.stat().st_mode
            try:
                contract.chmod(0)
                self.error(contract, root / "records")
            finally:
                contract.chmod(mode)

    def test_repair_regular_file_replacement_never_consumes_swapped_target(self) -> None:
        """Catches check/read TOCTOU that consumes a valid but observably different symlink target."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract()); self.write_results(root / "records", self.records())
            target_data = self.contract(applicable=False); target = root / "target.json"; write_json(target, target_data)
            original_open = os.open; swapped = False
            def replace(path: os.PathLike[str] | str, flags: int, *args: object, **kwargs: object) -> int:
                nonlocal swapped
                descriptor = original_open(path, flags, *args, **kwargs)
                if os.fspath(path) == str(contract) and not swapped:
                    swapped = True; contract.unlink(); contract.symlink_to(target)
                return descriptor
            module = self.load_processor()
            with patch.object(os, "open", replace):
                try: outcome = module.process_campaign(contract, root / "records")
                except module.ResultContractError: outcome = None
            self.assertTrue(swapped)
            if outcome is not None:
                self.assertEqual((outcome["semantic_verdict"], outcome["protocol_verdict"], outcome["acceptance_verdict"]), ("PASS", "PASS", "PASS"))

    def test_repair_results_root_replacement_never_consumes_redirected_inventory(self) -> None:
        """Catches results inventory traversal that reopens a root after validating its directory identity."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            results = root / "results"; self.write_results(results, self.records())
            redirected = root / "redirected"; target_records = self.records()
            target_records[0]["misses"] = [{"criterion": "redirected protocol", "ledger": "deterministic_protocol", "boundary": "DD-VERDICT"}]
            self.write_results(redirected, target_records)
            parked = root / "results-original"; original_open = os.open; original_iterdir = Path.iterdir; swapped = False

            def swap() -> None:
                nonlocal swapped
                if not swapped:
                    swapped = True; results.rename(parked); results.symlink_to(redirected, target_is_directory=True)

            def replace_open(path: os.PathLike[str] | str, flags: int, *args: object, **kwargs: object) -> int:
                descriptor = original_open(path, flags, *args, **kwargs)
                if os.fspath(path) == str(results): swap()
                return descriptor

            def replace_after_check(path: Path):
                if path == results: swap()
                return original_iterdir(path)

            module = self.load_processor()
            try:
                with patch.object(os, "open", replace_open), patch.object(Path, "iterdir", replace_after_check):
                    try:
                        outcome = module.process_campaign(contract, results)
                    except module.ResultContractError:
                        outcome = None
                self.assertTrue(swapped)
                if outcome is not None:
                    self.assertEqual((outcome["semantic_verdict"], outcome["protocol_verdict"], outcome["acceptance_verdict"]), ("PASS", "PASS", "PASS"))
            finally:
                if results.is_symlink():
                    results.unlink()
                if parked.exists():
                    parked.rename(results)

    def test_repair_state_intermediate_replacement_never_consumes_outside_bytes(self) -> None:
        """Catches state traversal that follows a swapped intermediate directory after its safety check."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root)
            nested = repo / "nested"; nested.mkdir(); expected = "frozen nested state\n"; (nested / "required.txt").write_text(expected)
            subprocess.run(["git", "add", "nested/required.txt"], cwd=repo, check=True)
            subprocess.run(["git", "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "nested frozen state"], cwd=repo, check=True)
            state.update({"head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip(),
                          "required_paths": {"nested/required.txt": digest(expected)}, "clean_worktree": False})
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data); self.write_results(root / "results", self.records(state={"agent_report": "present"}))
            outside = root / "outside"; outside.mkdir(); (outside / "required.txt").write_text("outside replacement bytes\n")
            parked = repo / "nested-original"; original_open = os.open; original_lstat = Path.lstat; swapped = False

            def swap() -> None:
                nonlocal swapped
                if not swapped:
                    swapped = True; nested.rename(parked); nested.symlink_to(outside, target_is_directory=True)

            def replace_open(path: os.PathLike[str] | str, flags: int, *args: object, **kwargs: object) -> int:
                descriptor = original_open(path, flags, *args, **kwargs)
                if path == "nested" and kwargs.get("dir_fd") is not None: swap()
                return descriptor

            def replace_after_intermediate_check(path: Path):
                info = original_lstat(path)
                if path == nested: swap()
                return info

            module = self.load_processor()
            try:
                with patch.object(os, "open", replace_open), patch.object(Path, "lstat", replace_after_intermediate_check):
                    try:
                        outcome = module.process_campaign(contract, root / "results")
                    except module.ResultContractError:
                        outcome = None
                self.assertTrue(swapped)
                if outcome is not None:
                    self.assertEqual(outcome["semantic_verdict"], "PASS")
            finally:
                if nested.is_symlink():
                    nested.unlink()
                if parked.exists():
                    parked.rename(nested)

    def test_rereview_git_dir_cannot_select_outside_repository_identity(self) -> None:
        """Catches Git state inspection accepting outside repository metadata with contracted files."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root); outside = root / "outside"
            subprocess.run(["git", "clone", "-q", str(repo), str(outside)], check=True)
            (outside / "outside-only.txt").write_text("outside identity\n")
            subprocess.run(["git", "add", "outside-only.txt"], cwd=outside, check=True)
            subprocess.run(["git", "-c", "user.name=Outside", "-c", "user.email=outside@example.test", "commit", "-qm", "outside identity"], cwd=outside, check=True)
            outside_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=outside, text=True).strip()
            self.assertNotEqual(outside_head, state["head"]); state["head"] = outside_head
            (repo / "outside-only.txt").write_text("outside identity\n")
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data); self.write_results(root / "results", self.records(state={"agent_report": "present"}))
            module = self.load_processor()
            with patch.dict(os.environ, {"GIT_DIR": str(outside / ".git")}):
                try: outcome = module.process_campaign(contract, root / "results")
                except module.ResultContractError: return
            self.assertEqual(outcome["semantic_verdict"], "FAIL")

    def test_rereview_git_and_state_files_bind_one_opened_repository_identity(self) -> None:
        """Catches Git reopening a contracted repository path after its state descriptor is retained."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root); outside = root / "outside"; subprocess.run(["git", "clone", "-q", str(repo), str(outside)], check=True)
            (outside / "outside-only.txt").write_text("outside identity\n")
            subprocess.run(["git", "add", "outside-only.txt"], cwd=outside, check=True)
            subprocess.run(["git", "-c", "user.name=Outside", "-c", "user.email=outside@example.test", "commit", "-qm", "outside identity"], cwd=outside, check=True)
            outside_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=outside, text=True).strip()
            self.assertNotEqual(outside_head, state["head"]); state["head"] = outside_head
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data); self.write_results(root / "results", self.records(state={"agent_report": "present"}))
            parked = root / "repo-original"; original_open = os.open; swapped = False
            def replace(path: os.PathLike[str] | str, flags: int, *args: object, **kwargs: object) -> int:
                nonlocal swapped
                descriptor = original_open(path, flags, *args, **kwargs)
                if os.fspath(path) == str(repo) and not swapped:
                    swapped = True; repo.rename(parked); repo.symlink_to(outside, target_is_directory=True)
                return descriptor
            module = self.load_processor()
            try:
                with patch.object(os, "open", replace):
                    try: outcome = module.process_campaign(contract, root / "results")
                    except module.ResultContractError: outcome = None
                self.assertTrue(swapped)
                if outcome is not None: self.assertEqual(outcome["semantic_verdict"], "FAIL")
            finally:
                if repo.is_symlink(): repo.unlink()
                if parked.exists(): parked.rename(repo)

    def test_rereview_readerless_fifo_contract_fails_closed_promptly(self) -> None:
        """Catches blocking before special contract material is rejected."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; os.mkfifo(contract); self.write_results(root / "results", self.records())
            self.fifo_error(contract, root / "results")

    def test_rereview_readerless_fifo_result_fails_closed_promptly(self) -> None:
        """Catches blocking before a special result file is rejected."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract()); results = root / "results"; results.mkdir(); os.mkfifo(results / "result-1.json")
            self.fifo_error(contract, results)

    def test_rereview_readerless_fifo_required_state_fails_closed_promptly(self) -> None:
        """Catches blocking before a special required-state final is rejected."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root); os.mkfifo(repo / "required.fifo")
            state.update({"required_paths": {"required.fifo": "0" * 64}, "clean_worktree": False})
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data); self.write_results(root / "results", self.records(state={"agent_report": "present"}))
            self.fifo_error(contract, root / "results")

    def test_rereview_infrastructure_recovery_before_terminal_stop_is_accepted(self) -> None:
        """Catches rejecting one or two retry errors followed by a completed response in the same slot."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            for count in (1, 2):
                with self.subTest(attempts=count):
                    records = self.records(); records.extend(self.infrastructure_record_with_empty_state(arm="original", repetition=1, attempt=number) for number in range(1, count + 1))
                    path = root / f"recovery-{count}"; self.write_results(path, records)
                    outcome = self.process(contract, path); self.assertEqual((outcome["acceptance_verdict"], outcome["ledgers"]["infrastructure"]["count"]), ("PASS", count))

    def test_rereview_infrastructure_completion_after_third_error_stops(self) -> None:
        """Catches accepting a completed response after the terminal third infrastructure error."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract()); records = self.records()
            records.extend(self.infrastructure_record_with_empty_state(arm="original", repetition=1, attempt=number) for number in range(1, 4))
            self.write_results(root / "terminal", records); self.error(contract, root / "terminal")

    def test_rereview_required_dot_path_is_contract_error(self) -> None:
        """Catches accepting an empty-normalized required relative path."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); _, state, _ = self.git_repo(root); state["required_paths"] = {".": "0" * 64}; state["clean_worktree"] = False
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state}); contract = root / "contract.json"; write_json(contract, data)
            self.write_results(root / "results", self.records(state={"agent_report": "present"})); self.error(contract, root / "results")

    def test_rereview_required_terminal_material_is_contract_error(self) -> None:
        """Catches final symlink or directory required material becoming a semantic miss."""
        with tempfile.TemporaryDirectory() as temp:
            for name in ("symlink", "directory"):
                with self.subTest(material=name):
                    root = Path(temp) / name; root.mkdir(); repo, state, _ = self.git_repo(root); required = repo / "required.txt"; state["clean_worktree"] = False
                    if name == "symlink":
                        external = root / "external.txt"; external.write_text("observed state\n"); required.unlink(); required.symlink_to(external)
                    else:
                        required.unlink(); required.mkdir()
                    data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state}); contract = root / "contract.json"; write_json(contract, data)
                    self.write_results(root / "results", self.records(state={"agent_report": "present"}))
                    self.error(contract, root / "results")

    def test_rereview_unreadable_required_final_is_contract_error(self) -> None:
        """Catches a final required-file permission failure becoming a semantic state deviation."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root); state["clean_worktree"] = False
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state}); contract = root / "contract.json"; write_json(contract, data)
            self.write_results(root / "results", self.records(state={"agent_report": "present"})); original_open = os.open; called = False
            def deny_required(path: os.PathLike[str] | str, flags: int, *args: object, **kwargs: object) -> int:
                nonlocal called
                if path == "required.txt" and kwargs.get("dir_fd") is not None:
                    called = True; raise PermissionError("injected required-file denial")
                return original_open(path, flags, *args, **kwargs)
            module = self.load_processor()
            with patch.object(os, "open", deny_required):
                try: module.process_campaign(contract, root / "results")
                except module.ResultContractError: rejected = True
                else: rejected = False
            self.assertTrue(called)
            self.assertTrue(rejected, "unreadable required final must be a ResultContractError")

    def test_rereview_results_root_close_oserror_is_contractual(self) -> None:
        """Catches a reachable results-root close failure leaking raw OSError."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract()); results = root / "results"; self.write_results(results, self.records())
            original_open, original_close = os.open, os.close; root_fd: int | None = None
            def track_open(path: os.PathLike[str] | str, flags: int, *args: object, **kwargs: object) -> int:
                nonlocal root_fd
                descriptor = original_open(path, flags, *args, **kwargs)
                if os.fspath(path) == str(results): root_fd = descriptor
                return descriptor
            def fail_close(descriptor: int) -> None:
                if descriptor == root_fd: raise OSError("injected results-root close failure")
                original_close(descriptor)
            try:
                with patch.object(os, "open", track_open), patch.object(os, "close", fail_close): self.error(contract, results)
            finally:
                if root_fd is not None:
                    try: original_close(root_fd)
                    except OSError: pass

    def test_descriptor_parent_duplicate_closes_once_after_nested_fstat_failure(self) -> None:
        """Catches a nested state-walk fstat failure closing its duplicated parent descriptor twice."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo, state, _ = self.git_repo(root); nested = repo / "nested"; nested.mkdir(); (nested / "required.txt").write_text("nested\n")
            subprocess.run(["git", "add", "nested/required.txt"], cwd=repo, check=True)
            subprocess.run(["git", "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "nested"], cwd=repo, check=True)
            state.update({"head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip(), "required_paths": {"nested/required.txt": digest("nested\n")}, "clean_worktree": False})
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state}); contract = root / "contract.json"; write_json(contract, data)
            self.write_results(root / "results", self.records(state={"agent_report": "present"})); original_dup, original_open, original_fstat, original_close = os.dup, os.open, os.fstat, os.close
            parent_fd: int | None = None; child_fd: int | None = None; parent_closes = 0
            def capture_dup(descriptor: int) -> int:
                nonlocal parent_fd
                parent_fd = original_dup(descriptor); return parent_fd
            def capture_open(path: os.PathLike[str] | str, flags: int, *args: object, **kwargs: object) -> int:
                nonlocal child_fd
                descriptor = original_open(path, flags, *args, **kwargs)
                if path == "nested" and kwargs.get("dir_fd") == parent_fd: child_fd = descriptor
                return descriptor
            def fail_child_fstat(descriptor: int) -> os.stat_result:
                if descriptor == child_fd: raise OSError("injected nested fstat failure")
                return original_fstat(descriptor)
            def count_parent_close(descriptor: int) -> None:
                nonlocal parent_closes
                if descriptor == parent_fd: parent_closes += 1
                original_close(descriptor)
            module = self.load_processor()
            with patch.object(os, "dup", capture_dup), patch.object(os, "open", capture_open), patch.object(os, "fstat", fail_child_fstat), patch.object(os, "close", count_parent_close):
                with self.assertRaises(module.ResultContractError): module.process_campaign(contract, root / "results")
            self.assertIsNotNone(parent_fd); self.assertIsNotNone(child_fd)
            self.assertEqual(parent_closes, 1)

    def test_git_state_inspection_never_uses_preexec_callback(self) -> None:
        """Catches descriptor-bound Git inspection relying on unsafe subprocess pre-exec callbacks."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); _, state, _ = self.git_repo(root)
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data); self.write_results(root / "results", self.records(state={"agent_report": "present"}))
            original_run = subprocess.run; observed: list[object] = []
            def observe(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
                observed.append(kwargs.get("preexec_fn")); return original_run(*args, **kwargs)
            with patch.object(subprocess, "run", observe): self.assertEqual(self.process(contract, root / "results")["acceptance_verdict"], "PASS")
            self.assertEqual(observed, [None, None])

    def test_git_state_inspection_is_concurrently_safe_without_preexec(self) -> None:
        """Catches a pre-exec Git design that is unsafe when state campaigns run concurrently."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); _, state, _ = self.git_repo(root)
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data); self.write_results(root / "results", self.records(state={"agent_report": "present"}))
            original_run = subprocess.run; observed: list[object] = []
            def observe(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
                observed.append(kwargs.get("preexec_fn")); return original_run(*args, **kwargs)
            with patch.object(subprocess, "run", observe):
                with ThreadPoolExecutor(max_workers=3) as pool:
                    outcomes = list(pool.map(lambda _: self.process(contract, root / "results")["acceptance_verdict"], range(3), timeout=10))
            self.assertEqual(outcomes, ["PASS", "PASS", "PASS"])
            self.assertEqual(observed, [None] * 6)

    def test_git_descriptor_helper_missing_fd_fails_closed(self) -> None:
        """Catches a descriptor helper failure escaping when its child lacks the retained repository fd."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); _, state, _ = self.git_repo(root)
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data); self.write_results(root / "results", self.records(state={"agent_report": "present"}))
            original_run = subprocess.run; called = False
            def remove_fds(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
                nonlocal called
                if "pass_fds" in kwargs:
                    called = True; kwargs["pass_fds"] = ()
                return original_run(*args, **kwargs)
            with patch.object(subprocess, "run", remove_fds): self.public_error(contract, root / "results")
            self.assertTrue(called)

    def test_hostile_repository_and_state_paths_normalize_to_contract_errors(self) -> None:
        """Catches NUL-bearing repository, required, or forbidden paths leaking host path exceptions."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name, field in (("repository", "repository"), ("required", "required"), ("forbidden", "forbidden")):
                with self.subTest(field=name):
                    case = root / name; case.mkdir(); _, state, _ = self.git_repo(case); state["clean_worktree"] = False
                    if field == "repository": state["repository"] = "bad\x00repo"
                    elif field == "required": state["required_paths"] = {"bad\x00path": "0" * 64}
                    else: state["forbidden_paths"] = ["bad\x00path"]
                    data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state}); contract = case / "contract.json"; write_json(contract, data)
                    self.write_results(case / "results", self.records(state={"agent_report": "present"})); self.public_error(contract, case / "results")

    def test_raw_artifact_surrogate_normalizes_to_contract_error(self) -> None:
        """Catches raw-artifact UTF-8 encoding failures escaping the public processor contract."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract()); records = self.records(); records[0]["raw_artifact"] = "bad\ud800"; records[0]["raw_artifact_sha256"] = "0" * 64
            self.write_results(root / "results", records); self.public_error(contract, root / "results")

    def test_completed_raw_artifact_allows_nul_and_hashes_its_utf8_bytes(self) -> None:
        """Catches treating an in-memory NUL in an evaluable artifact as an OS-path violation."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records(); records[0]["raw_artifact"] = "before\x00after"; records[0]["raw_artifact_sha256"] = hashlib.sha256(b"before\x00after").hexdigest()
            self.write_results(root / "results", records)
            module = self.load_processor()
            try:
                outcome = module.process_campaign(contract, root / "results")
            except module.ResultContractError as error:
                self.fail(f"NUL-bearing artifact was rejected: {error}")
            self.assertEqual(outcome["semantic_verdict"], "PASS")
            self.assertEqual(outcome["protocol_verdict"], "PASS")
            self.assertEqual(outcome["acceptance_verdict"], "PASS")
            self.counts(outcome, required=3, completed=3)

    def test_repair_rubric_ambiguity_must_be_boolean(self) -> None:
        """Catches accepting a non-boolean rubric-ambiguity flag."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            flagged = self.records(repetitions=5); flagged[0]["rubric_ambiguity"] = "true"
            self.write_results(root / "flag", flagged); self.error(contract, root / "flag")

    def test_repair_task_fidelity_instability_must_be_boolean(self) -> None:
        """Catches accepting a non-boolean task-fidelity instability flag."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records(repetitions=5); records[0]["task_fidelity_instability"] = 1
            self.write_results(root / "flag", records); self.error(contract, root / "flag")

    def test_repair_result_schema_version_must_not_be_boolean(self) -> None:
        """Catches a boolean result schema version passing integer equality."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = root / "contract.json"; write_json(contract, self.contract())
            records = self.records(); records[0]["schema_version"] = True
            self.write_results(root / "result-version", records); self.error(contract, root / "result-version")

    def test_repair_contract_schema_version_must_not_be_boolean(self) -> None:
        """Catches a boolean contract schema version passing integer equality against valid results."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract_data = self.contract(); contract_data["schema_version"] = True
            contract = root / "contract-version.json"; write_json(contract, contract_data)
            self.write_results(root / "valid-results", self.records()); self.error(contract, root / "valid-results")

    def test_repair_ledger_entries_have_canonical_retained_entry_order(self) -> None:
        """Catches noncanonical retained-entry order in every public ledger."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); scenarios = ("gate-boundary", "second"); contract = root / "contract.json"; write_json(contract, self.contract(tier="stabilized-high", scenarios=scenarios))
            records = self.records(scenarios=scenarios, tier="stabilized-high")
            owned = (("core_behavior", "invariant", "DD-I1"), ("deterministic_protocol", "boundary", "DD-VERDICT"),
                     ("task_fixture_fidelity", None, None), ("readability", None, None))
            for index, record in enumerate(records):
                ledger, owner, value = owned[index % len(owned)]
                miss = {"criterion": f"{ledger}-{record['arm']}-{record['scenario']}-{record['repetition']}", "ledger": ledger}
                if owner: miss[owner] = value
                record["misses"] = [miss]
            core_record = next(record for record in records if record["misses"][0]["ledger"] == "core_behavior")
            core_record["misses"] = [{"criterion": criterion, "ledger": "core_behavior", "invariant": "DD-I1"} for criterion in ("core-z", "core-y", "core-x")]
            materialized = []
            for ledger in ("core_behavior", "deterministic_protocol", "task_fixture_fidelity", "readability"):
                materialized.extend(sorted((record for record in records if record["misses"][0]["ledger"] == ledger), key=lambda record: (record["arm"] != "original", record["scenario"], record["repetition"]), reverse=True))
            infra = []
            for arm in ("original", "current"):
                for attempt_number in (1, 2):
                    item = self.infrastructure_record_with_empty_state(arm=arm, repetition=1, tier="stabilized-high", attempt=attempt_number)
                    item.update({"misses": [{"criterion": f"infrastructure-{attempt_number}-{arm}", "ledger": "infrastructure"}]})
                    infra.append(item)
            infra = [infra[3], infra[1], infra[2], infra[0]]
            all_records = materialized + infra
            for index, record in enumerate(all_records, 1):
                write_json(root / "records" / f"result-{len(all_records) + 1 - index}.json", record)
            outcome = self.process(contract, root / "records")
            for ledger in ("core_behavior", "deterministic_protocol", "task_fixture_fidelity", "readability", "infrastructure"):
                with self.subTest(ledger=ledger):
                    entries = outcome["ledgers"][ledger]["entries"]
                    tuples = [(entry.get("arm"), entry.get("scenario"), entry.get("repetition"), entry.get("criterion")) for entry in entries]
                    self.assertEqual(tuples, sorted(tuples, key=lambda row: (row[0] != "original", row[1], row[2], row[3])))

    def test_repair_protocol_na_permits_zero_authenticated_boundaries(self) -> None:
        """Catches a no-protocol scenario incorrectly requiring a deterministic boundary owner."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = self.contract(applicable=False)
            contract["scenarios"][0]["authenticated_protocol_boundaries"] = []
            path = root / "na-contract.json"; write_json(path, contract); self.write_results(root / "records", self.records())
            self.assertEqual(self.process(path, root / "records")["protocol_verdict"], "NOT_APPLICABLE")
            applicable = self.contract(applicable=True); applicable["scenarios"][0]["authenticated_protocol_boundaries"] = []
            applicable_path = root / "applicable-empty.json"; write_json(applicable_path, applicable)
            self.error(applicable_path, root / "records")

    def test_repair_state_required_structural_infrastructure_omits_evidence(self) -> None:
        """Catches requiring state evidence from an unevaluable infrastructure attempt."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); _, state, _ = self.git_repo(root)
            data = self.contract(); data["scenarios"][0].update({"requires_state_evidence": True, "state_contract": state})
            contract = root / "contract.json"; write_json(contract, data)
            records = self.records(state={"agent_report": "present"}); records.append(self.infrastructure_record(arm="original", repetition=1))
            self.write_results(root / "records", records); outcome = self.process(contract, root / "records")
            self.assertEqual((outcome["acceptance_verdict"], outcome["ledgers"]["infrastructure"]["count"]), ("PASS", 1))

    def test_repair_core_invariant_count_has_an_upper_bound(self) -> None:
        """Catches accepting scenarios with more than four authenticated core invariants."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); contract = self.contract()
            contract["scenarios"][0]["core_invariants"].extend(["DD-I3", "DD-I4", "DD-I5"])
            path = root / "five-invariants.json"; write_json(path, contract); self.write_results(root / "records", self.records())
            self.error(path, root / "records")


if __name__ == "__main__":
    unittest.main()
