"""Fail-closed processing for frozen charter-first validation campaigns."""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import subprocess
import sys
from pathlib import Path
from typing import Any


class ResultContractError(RuntimeError):
    """The frozen contract or result material is missing, malformed, or tampered."""


LEDGER_ORDER = ("core_behavior", "deterministic_protocol", "task_fixture_fidelity", "readability", "infrastructure")
LEDGER_NAMES = set(LEDGER_ORDER)
INPUT_NAMES = {"prompt", "rubric", "fixture", "dependency", "harness", "executable"}
RESULT_NAME = re.compile(r"result-([1-9][0-9]*)\.json\Z")
INFRA_ATTEMPT = re.compile(r"infrastructure-([1-9][0-9]*)\Z")
GIT_HEAD = re.compile(r"[0-9a-f]{40}(?:[0-9a-f]{24})?\Z")
GIT_HELPER = "import os,sys; fd=int(sys.argv[1]); os.fchdir(fd); os.close(fd); os.execvpe(sys.argv[2], sys.argv[2:], os.environ)"


def _fail(message: str) -> None:
    raise ResultContractError(message)


def _regular_bytes(path: Path, label: str) -> bytes:
    try:
        flags = os.O_RDONLY | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode): _fail(f"{label} is not a regular file")
            chunks: list[bytes] = []
            while chunk := os.read(descriptor, 65536): chunks.append(chunk)
            return b"".join(chunks)
        finally:
            os.close(descriptor)
    except OSError as error:
        raise ResultContractError(f"unable to read {label}") from error


def _open_directory(path: Path, label: str) -> int:
    try:
        flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
    except OSError as error:
        raise ResultContractError(f"unable to open {label}") from error
    try:
        if not stat.S_ISDIR(os.fstat(descriptor).st_mode):
            _fail(f"{label} is not a real directory")
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _regular_bytes_at(directory: int, name: str, label: str) -> bytes:
    try:
        flags = os.O_RDONLY | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(name, flags, dir_fd=directory)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                _fail(f"{label} is not a regular file")
            chunks: list[bytes] = []
            while chunk := os.read(descriptor, 65536):
                chunks.append(chunk)
            return b"".join(chunks)
        finally:
            os.close(descriptor)
    except OSError as error:
        raise ResultContractError(f"unable to read {label}") from error


def _no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            _fail("duplicate JSON object key")
        result[key] = value
    return result


def _json_bytes(raw: bytes, label: str) -> Any:
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=_no_duplicates)
    except UnicodeDecodeError as error:
        raise ResultContractError(f"{label} is not UTF-8") from error
    except json.JSONDecodeError as error:
        raise ResultContractError(f"{label} is not JSON") from error


def _json_file(path: Path, label: str) -> Any:
    return _json_bytes(_regular_bytes(path, label), label)


def _mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        _fail(f"{label} must be an object")
    return value


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        _fail(f"{label} must be a nonempty string")
    return value


def _utf8_bytes(value: Any, label: str) -> bytes:
    value = _string(value, label)
    try:
        return value.encode("utf-8")
    except UnicodeEncodeError as error:
        raise ResultContractError(f"{label} is not UTF-8 encodable") from error


def _os_path(value: Any, label: str) -> bytes:
    encoded = _utf8_bytes(value, label)
    if b"\x00" in encoded:
        _fail(f"{label} contains NUL")
    return encoded


def _strict_int(value: Any, label: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        _fail(f"{label} must be an integer")
    return value


def _sha(value: Any, label: str) -> str:
    value = _string(value, label)
    if not re.fullmatch(r"[0-9a-f]{64}", value):
        _fail(f"{label} must be a SHA-256")
    return value


def _exact_keys(value: dict[str, Any], required: set[str], optional: set[str], label: str) -> None:
    keys = set(value)
    if not required <= keys or keys - required - optional:
        _fail(f"unexpected {label} shape")


def _campaign(contract: dict[str, Any]) -> tuple[str, str, str, str]:
    campaign = _mapping(contract.get("campaign"), "campaign")
    _exact_keys(campaign, {"id", "tier", "model", "effort"}, set(), "campaign")
    campaign_id, tier = _string(campaign["id"], "campaign id"), _string(campaign["tier"], "campaign tier")
    if tier not in {"rebuild-low", "stabilized-high"}:
        _fail("unknown campaign tier")
    model, effort = _string(campaign["model"], "campaign model"), _string(campaign["effort"], "campaign effort")
    if effort != ("low" if tier == "rebuild-low" else "high") or not campaign_id.endswith(f":{tier}"):
        _fail("campaign provenance malformed")
    return campaign_id, tier, model, effort


def _arms(contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = _mapping(contract.get("arms"), "arms")
    if set(raw) != {"original", "current"}:
        _fail("contract must name original and current arms")
    result: dict[str, dict[str, Any]] = {}
    for arm_name in ("original", "current"):
        arm = _mapping(raw[arm_name], f"{arm_name} arm")
        _exact_keys(arm, {"identity", "skill_sha256", "input_hashes"}, set(), f"{arm_name} arm")
        hashes = _mapping(arm["input_hashes"], f"{arm_name} input hashes")
        if set(hashes) != INPUT_NAMES:
            _fail("input hash names do not match frozen set")
        result[arm_name] = {"identity": _string(arm["identity"], "arm identity"), "skill_sha256": _sha(arm["skill_sha256"], "skill hash"), "input_hashes": {key: _sha(hashes[key], f"{key} hash") for key in INPUT_NAMES}}
    if result["original"]["input_hashes"] != result["current"]["input_hashes"]:
        _fail("frozen arms do not have identical inputs")
    return result


def _safe_rel(value: Any, label: str) -> str:
    _os_path(value, label)
    parts = Path(value).parts
    if not parts or Path(value).is_absolute() or ".." in parts:
        _fail(f"{label} unsafe")
    return value


def _state_contract(state: dict[str, Any], invariants: set[str]) -> None:
    _exact_keys(state, {"repository", "head", "required_paths", "forbidden_paths", "clean_worktree", "invariant"}, set(), "state contract")
    _os_path(state["repository"], "state repository")
    head = _string(state["head"], "state head")
    if not GIT_HEAD.fullmatch(head):
        _fail("state head malformed")
    if not isinstance(state["invariant"], str) or state["invariant"] not in invariants:
        _fail("state invariant is not authenticated")
    required = _mapping(state["required_paths"], "required paths")
    if not required:
        _fail("required paths empty")
    for path, digest in required.items():
        _safe_rel(path, "required path"); _sha(digest, "required path hash")
    forbidden = state["forbidden_paths"]
    if not isinstance(forbidden, list):
        _fail("forbidden paths malformed")
    for path in forbidden:
        _safe_rel(path, "forbidden path")
    if not isinstance(state["clean_worktree"], bool):
        _fail("clean-worktree flag malformed")


def _scenarios(contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = contract.get("scenarios")
    if not isinstance(raw, list) or not raw:
        _fail("scenarios must be a nonempty list")
    result: dict[str, dict[str, Any]] = {}
    for item in raw:
        scenario = _mapping(item, "scenario")
        required = {"id", "core_invariants", "authenticated_protocol_boundaries", "protocol_applicable", "requires_state_evidence"}
        _exact_keys(scenario, required, {"state_contract"}, "scenario")
        identifier = _string(scenario["id"], "scenario id")
        if identifier in result:
            _fail("duplicate scenario id")
        invariants, boundaries = scenario["core_invariants"], scenario["authenticated_protocol_boundaries"]
        if not isinstance(invariants, list) or not 1 <= len(invariants) <= 4 or not all(isinstance(x, str) and x for x in invariants) or len(set(invariants)) != len(invariants):
            _fail("scenario invariants malformed")
        applicable, state_required = scenario["protocol_applicable"], scenario["requires_state_evidence"]
        if not isinstance(applicable, bool) or not isinstance(state_required, bool):
            _fail("scenario flags malformed")
        if not isinstance(boundaries, list) or len(set(boundaries)) != len(boundaries) or not all(isinstance(x, str) and x for x in boundaries) or (applicable and not boundaries):
            _fail("scenario boundaries malformed")
        if state_required:
            if "state_contract" not in scenario:
                _fail("state-required scenario lacks frozen state contract")
            _state_contract(_mapping(scenario["state_contract"], "state contract"), set(invariants))
        elif "state_contract" in scenario:
            _fail("non-state scenario has state contract")
        result[identifier] = {"invariants": set(invariants), "boundaries": set(boundaries), "protocol": applicable, "state_required": state_required, "state_contract": scenario.get("state_contract")}
    return result


def _read_results(root: Path) -> list[dict[str, Any]]:
    descriptor = _open_directory(root, "results root")
    try:
        indexed: list[tuple[int, str]] = []
        for name in os.listdir(descriptor):
            match = RESULT_NAME.fullmatch(name)
            if not match:
                _fail("unexpected result material")
            indexed.append((int(match.group(1)), name))
        indexed.sort()
        if not indexed or [number for number, _ in indexed] != list(range(1, len(indexed) + 1)):
            _fail("result inventory is not consecutive")
        return [_mapping(_json_bytes(_regular_bytes_at(descriptor, name, f"result {name}"), f"result {name}"), f"result {name}") for _, name in indexed]
    except OSError as error:
        raise ResultContractError("unable to inspect results root") from error
    finally:
        os.close(descriptor)


def _entry(record: dict[str, Any], miss: dict[str, Any], arm: str, scenario: str, repetition: int, attempt: str, fresh: str, status: str) -> dict[str, Any]:
    result = {"arm": arm, "scenario": scenario, "repetition": repetition, "attempt": attempt, "fresh_context": fresh, "status": status, "criterion": miss["criterion"]}
    if "invariant" in miss:
        result["invariant"] = miss["invariant"]
    if "boundary" in miss:
        result["boundary"] = miss["boundary"]
    return result


def _record(record: dict[str, Any], campaign_id: str, model: str, effort: str, arms: dict[str, dict[str, Any]], scenarios: dict[str, dict[str, Any]], ledgers: dict[str, dict[str, Any]]) -> dict[str, Any]:
    status = record.get("status")
    shared = {"schema_version", "campaign_id", "model", "effort", "arm", "arm_identity", "scenario", "repetition", "attempt", "fresh_context", "status", "skill_sha256", "input_hashes", "misses"}
    completed = shared | {"state_evidence", "raw_artifact", "raw_artifact_sha256", "claimed_semantic_verdict", "claimed_protocol_verdict"}
    if status == "completed":
        _exact_keys(record, completed, {"rubric_ambiguity", "task_fidelity_instability"}, "completed result")
    elif status == "infrastructure_error":
        _exact_keys(record, shared, {"state_evidence"}, "infrastructure result")
    else:
        _fail("unknown result status")
    if _strict_int(record["schema_version"], "result schema") != 1:
        _fail("unsupported result schema")
    if record["campaign_id"] != campaign_id or record["model"] != model or record["effort"] != effort:
        _fail("result provenance disagrees with frozen campaign")
    arm = _string(record["arm"], "result arm")
    if arm not in arms or record["arm_identity"] != arms[arm]["identity"] or record["skill_sha256"] != arms[arm]["skill_sha256"]:
        _fail("result arm provenance mismatch")
    inputs = _mapping(record["input_hashes"], "result input hashes")
    if set(inputs) != INPUT_NAMES or any(inputs[key] != arms[arm]["input_hashes"][key] for key in INPUT_NAMES):
        _fail("result input provenance mismatch")
    scenario = _string(record["scenario"], "result scenario")
    if scenario not in scenarios:
        _fail("unknown result scenario")
    repetition = _strict_int(record["repetition"], "result repetition")
    if repetition < 1:
        _fail("result repetition must be positive")
    attempt, fresh = _string(record["attempt"], "result attempt"), _string(record["fresh_context"], "fresh context")
    expected_fresh = f"{campaign_id}/{arm}/{scenario}/run-{repetition}" + ("" if status == "completed" else f"/{attempt}")
    if fresh != expected_fresh:
        _fail("fresh context does not match record identity")
    if status == "completed":
        if attempt != "a1": _fail("completed result attempt is unauthorized")
        if scenarios[scenario]["state_required"] and not _mapping(record["state_evidence"], "state evidence"):
            _fail("state-required result lacks state evidence")
        artifact = _utf8_bytes(record["raw_artifact"], "raw artifact")
        if _sha(record["raw_artifact_sha256"], "raw artifact hash") != hashlib.sha256(artifact).hexdigest(): _fail("raw artifact hash mismatch")
        _string(record["claimed_semantic_verdict"], "claimed semantic verdict"); _string(record["claimed_protocol_verdict"], "claimed protocol verdict")
        for flag in ("rubric_ambiguity", "task_fidelity_instability"):
            if flag in record and not isinstance(record[flag], bool): _fail("optional result flag malformed")
    else:
        if not INFRA_ATTEMPT.fullmatch(attempt): _fail("infrastructure attempt malformed")
        if "state_evidence" in record: _mapping(record["state_evidence"], "state evidence")
    misses = record["misses"]
    if not isinstance(misses, list): _fail("misses must be a list")
    core_miss = protocol_miss = False
    for raw_miss in misses:
        miss = _mapping(raw_miss, "miss")
        _exact_keys(miss, {"criterion", "ledger"}, {"invariant", "boundary"}, "miss")
        _string(miss["criterion"], "miss criterion")
        ledger = miss["ledger"]
        if not isinstance(ledger, str) or ledger not in LEDGER_NAMES: _fail("miss must have exactly one approved ledger")
        if status == "completed" and ledger == "infrastructure": _fail("completed result cannot carry infrastructure miss")
        if status == "infrastructure_error" and ledger != "infrastructure": _fail("infrastructure result has evaluable miss")
        if ledger == "core_behavior":
            if set(miss) != {"criterion", "ledger", "invariant"} or not isinstance(miss["invariant"], str) or miss["invariant"] not in scenarios[scenario]["invariants"]: _fail("core miss invariant is not authenticated")
            core_miss = True
        elif ledger == "deterministic_protocol":
            if set(miss) != {"criterion", "ledger", "boundary"} or not isinstance(miss["boundary"], str) or not scenarios[scenario]["protocol"] or miss["boundary"] not in scenarios[scenario]["boundaries"]: _fail("protocol miss boundary is not authenticated")
            protocol_miss = True
        elif set(miss) != {"criterion", "ledger"}: _fail("non-owning miss carries unauthorized ownership metadata")
        ledgers[ledger]["entries"].append(_entry(record, miss, arm, scenario, repetition, attempt, fresh, status))
    if status == "infrastructure_error" and len(misses) != 1: _fail("infrastructure result must retain one infrastructure error")
    return {"arm": arm, "scenario": scenario, "repetition": repetition, "attempt": attempt, "fresh": fresh, "status": status, "core_miss": core_miss, "protocol_miss": protocol_miss, "rubric_ambiguity": record.get("rubric_ambiguity", False), "task_fidelity_instability": record.get("task_fidelity_instability", False)}


def _git(repository_fd: int, *args: str) -> str:
    try:
        environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        environment.update({"GIT_OPTIONAL_LOCKS": "0", "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull})
        command = ["git", "-C", ".", "-c", "status.showUntrackedFiles=all", "-c", "core.fsmonitor=false", "-c", "core.untrackedCache=false", *args]
        return subprocess.run([sys.executable, "-I", "-c", GIT_HELPER, str(repository_fd), *command], check=True, capture_output=True, text=True, env=environment, pass_fds=(repository_fd,)).stdout
    except (OSError, subprocess.CalledProcessError, subprocess.SubprocessError) as error:
        raise ResultContractError("unable to inspect state repository") from error


def _state_parent(repo: int, relative: str) -> tuple[int, str] | None:
    try:
        current = os.dup(repo)
    except OSError as error:
        raise ResultContractError("state path escapes repository") from error
    parts = Path(relative).parts
    for part in parts[:-1]:
        try:
            child = os.open(part, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0), dir_fd=current)
        except FileNotFoundError:
            os.close(current)
            return None
        except OSError as error:
            os.close(current)
            raise ResultContractError("state path escapes repository") from error
        try:
            is_directory = stat.S_ISDIR(os.fstat(child).st_mode)
        except OSError as error:
            os.close(child)
            os.close(current)
            raise ResultContractError("state path escapes repository") from error
        if not is_directory:
            os.close(child)
            os.close(current)
            _fail("state path escapes repository")
        try:
            os.close(current)
        except OSError as error:
            os.close(child)
            raise ResultContractError("state path escapes repository") from error
        current = child
    return current, parts[-1]


def _state_required_bytes(repo: int, relative: str) -> bytes | None:
    parent = _state_parent(repo, relative)
    if parent is None:
        return None
    directory, name = parent
    try:
        try:
            flags = os.O_RDONLY | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
            descriptor = os.open(name, flags, dir_fd=directory)
        except FileNotFoundError:
            return None
        except OSError as error:
            raise ResultContractError("unable to read state required path") from error
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                _fail("state required path is not a regular file")
            chunks: list[bytes] = []
            while chunk := os.read(descriptor, 65536): chunks.append(chunk)
            return b"".join(chunks)
        finally:
            os.close(descriptor)
    finally:
        os.close(directory)


def _state_forbidden_exists(repo: int, relative: str) -> bool:
    parent = _state_parent(repo, relative)
    if parent is None:
        return False
    directory, name = parent
    try:
        try:
            info = os.stat(name, dir_fd=directory, follow_symlinks=False)
        except FileNotFoundError:
            return False
        except OSError as error:
            raise ResultContractError("unable to inspect forbidden state path") from error
        if stat.S_ISLNK(info.st_mode):
            _fail("state path escapes repository")
        return True
    finally:
        os.close(directory)


def _state_deviation(state: dict[str, Any]) -> bool:
    repo = Path(_os_path(state["repository"], "state repository").decode("utf-8"))
    descriptor = _open_directory(repo, "state repository")
    try:
        deviation = _git(descriptor, "rev-parse", "HEAD").strip() != state["head"]
        for relative, expected in state["required_paths"].items():
            observed = _state_required_bytes(descriptor, relative)
            if observed is None or hashlib.sha256(observed).hexdigest() != expected:
                deviation = True
        for relative in state["forbidden_paths"]:
            if _state_forbidden_exists(descriptor, relative):
                deviation = True
        return deviation or bool(state["clean_worktree"] and _git(descriptor, "status", "--porcelain"))
    finally:
        os.close(descriptor)


def _process_campaign(contract_path: Path, results_root: Path) -> dict:
    contract = _mapping(_json_file(Path(contract_path), "contract"), "contract")
    _exact_keys(contract, {"schema_version", "campaign", "arms", "scenarios"}, set(), "contract")
    if _strict_int(contract["schema_version"], "contract schema") != 1: _fail("unsupported contract schema")
    campaign_id, tier, model, effort = _campaign(contract); arms, scenarios = _arms(contract), _scenarios(contract)
    ledgers = {name: {"count": 0, "entries": []} for name in LEDGER_ORDER}
    parsed = [_record(record, campaign_id, model, effort, arms, scenarios, ledgers) for record in _read_results(Path(results_root))]
    contexts: set[str] = set(); slots: set[tuple[str, str, int, str]] = set(); completed = {(arm, scenario): [] for arm in arms for scenario in scenarios}; infra: dict[tuple[str, str, int], list[int]] = {}
    for record in parsed:
        if record["fresh"] in contexts: _fail("fresh context reused")
        contexts.add(record["fresh"]); slot = (record["arm"], record["scenario"], record["repetition"], record["attempt"])
        if slot in slots: _fail("duplicate result attempt")
        slots.add(slot)
        if record["status"] == "completed": completed[(record["arm"], record["scenario"])].append(record)
        else: infra.setdefault((record["arm"], record["scenario"], record["repetition"]), []).append(int(INFRA_ATTEMPT.fullmatch(record["attempt"]).group(1)))
    for numbers in infra.values():
        if sorted(numbers) != list(range(1, len(numbers) + 1)): _fail("infrastructure attempts are not contiguous")
        if len(numbers) > 3: _fail("infrastructure retry limit exceeded")
    if any(len(numbers) == 3 and any(item["status"] == "completed" and (item["arm"], item["scenario"], item["repetition"]) == slot for item in parsed) for slot, numbers in infra.items()):
        _fail("infrastructure terminal stop exceeded")
    summaries: dict[str, dict[str, dict[str, int]]] = {arm: {} for arm in arms}; semantic_fail = bool(ledgers["core_behavior"]["entries"])
    for scenario_id, scenario in scenarios.items():
        groups = {arm: sorted(completed[(arm, scenario_id)], key=lambda item: item["repetition"]) for arm in arms}
        trigger = any(len(group) >= 3 and (len({item["core_miss"] for item in group if item["repetition"] <= 3}) > 1 or any((item["rubric_ambiguity"] or item["task_fidelity_instability"]) and item["repetition"] <= 3 for item in group)) for group in groups.values())
        required = 5 if tier == "rebuild-low" and trigger else 3
        for arm, group in groups.items():
            if [item["repetition"] for item in group] != list(range(1, required + 1)): _fail("completed repetitions do not match policy")
            summaries[arm][scenario_id] = {"required": required, "completed": len(group)}
        for (arm, infra_scenario, repetition), numbers in infra.items():
            if infra_scenario == scenario_id and repetition not in range(1, required + 1): _fail("infrastructure repetition is not planned")
        if scenario["state_required"] and _state_deviation(_mapping(scenario["state_contract"], "state contract")):
            semantic_fail = True
            ledgers["core_behavior"]["entries"].append({"scenario": scenario_id, "criterion": "independently observed state deviation", "invariant": scenario["state_contract"]["invariant"], "status": "independently_observed", "source": "state_contract"})
    for ledger in ledgers.values():
        ledger["entries"].sort(key=lambda item: (item.get("arm") != "original", item.get("scenario", ""), item.get("repetition", 0), item.get("attempt", ""), item.get("criterion", "")))
        ledger["count"] = len(ledger["entries"])
    protocol_applicable = any(scenario["protocol"] for scenario in scenarios.values())
    semantic = "FAIL" if semantic_fail else "PASS"; protocol = "NOT_APPLICABLE" if not protocol_applicable else ("FAIL" if ledgers["deterministic_protocol"]["count"] else "PASS")
    return {"ledgers": ledgers, "semantic_verdict": semantic, "protocol_verdict": protocol, "acceptance_verdict": "FAIL" if semantic == "FAIL" or protocol == "FAIL" else "PASS", "repetitions": summaries}


def process_campaign(contract_path: Path, results_root: Path) -> dict:
    try:
        return _process_campaign(contract_path, results_root)
    except ResultContractError:
        raise
    except OSError as error:
        raise ResultContractError("unable to process campaign material") from error
