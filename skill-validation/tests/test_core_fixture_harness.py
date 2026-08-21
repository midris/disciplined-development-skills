"""Behavior contracts for the executable core-fixture harness."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
from types import ModuleType


HARNESS_PATH = Path(__file__).resolve().parents[1] / "core_fixture_harness.py"
IDENTITY = ("Fixture Contract", "fixture@example.test")
TIMESTAMP = "2020-01-02T03:04:05+0000"
HELPER_BYTES = b"""#!/bin/sh
set -eu
case "${1-}" in
  milestone-one)
    printf 'result\\n' > result.txt
    /usr/bin/env -i PATH=/usr/bin:/bin HOME=/nonexistent TMPDIR=/tmp GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null GIT_DIR=.git GIT_WORK_TREE=. \\
      /usr/bin/git add -- result.txt
    /usr/bin/env -i PATH=/usr/bin:/bin HOME=/nonexistent TMPDIR=/tmp GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null GIT_DIR=.git GIT_WORK_TREE=. \\
      GIT_AUTHOR_NAME='Fixture Contract' GIT_AUTHOR_EMAIL='fixture@example.test' \\
      GIT_COMMITTER_NAME='Fixture Contract' GIT_COMMITTER_EMAIL='fixture@example.test' \\
      GIT_AUTHOR_DATE='2020-01-02T03:04:05+0000' GIT_COMMITTER_DATE='2020-01-02T03:04:05+0000' \\
      /usr/bin/git -c core.hooksPath=/dev/null -c commit.gpgSign=false commit -qm 'final fixture'
    ;;
  milestone-two)
    test -f result.txt
    test -z "$(/usr/bin/env -i PATH=/usr/bin:/bin HOME=/nonexistent TMPDIR=/tmp GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null GIT_DIR=.git GIT_WORK_TREE=. /usr/bin/git -c core.fileMode=true status --porcelain=v1 --untracked-files=all)"
    ;;
  milestone-observed-only)
    exit 7
    ;;
  *)
    exit 64
    ;;
esac
"""


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()


def digest(data: bytes | str) -> str:
    return hashlib.sha256(data.encode() if isinstance(data, str) else data).hexdigest()


def git(repo: Path, *args: str, env: dict[str, str] | None = None) -> str:
    merged = os.environ | {"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
                           "GIT_AUTHOR_NAME": IDENTITY[0], "GIT_AUTHOR_EMAIL": IDENTITY[1],
                           "GIT_COMMITTER_NAME": IDENTITY[0], "GIT_COMMITTER_EMAIL": IDENTITY[1],
                           "GIT_AUTHOR_DATE": TIMESTAMP, "GIT_COMMITTER_DATE": TIMESTAMP} | (env or {})
    return subprocess.check_output(["git", "-C", str(repo), "-c", "core.hooksPath=/dev/null",
                                    "-c", "commit.gpgSign=false", *args], env=merged, text=True).strip()


class FixtureHarnessTests(unittest.TestCase):
    """Every test names the public defect it is intended to catch."""

    def load(self) -> ModuleType:
        self.assertTrue(HARNESS_PATH.is_file(), "production defect: core_fixture_harness.py is absent; it must expose the four-symbol public contract")
        spec = importlib.util.spec_from_file_location("core_fixture_harness_under_test", HARNESS_PATH)
        self.assertIsNotNone(spec); self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
        self.assertEqual({"FixtureContractError", "prepare_fixture", "record_fixture_execution", "verify_fixture"},
                         {name for name in ("FixtureContractError", "prepare_fixture", "record_fixture_execution", "verify_fixture") if hasattr(module, name)})
        return module

    def write_contract(self, path: Path, value: dict) -> None:
        path.write_bytes(canonical(value))

    def source_and_contract(
        self,
        temp: Path,
        *,
        final_change: bool = True,
        nested_source: bool = False,
        delete_seed: bool = False,
        identity: tuple[str, str] = IDENTITY,
    ) -> tuple[Path, Path, dict]:
        temp.mkdir(parents=True, exist_ok=True); source = temp / "source"; source.mkdir(); seed_source = "nested/deep/seed.txt" if nested_source else "seed.txt"; seed_destination = "nested/deep/seed.txt" if nested_source else "seed.txt"
        (source / seed_source).parent.mkdir(parents=True, exist_ok=True); (source / seed_source).write_text("seed\n"); (source / "fixture-helper").write_bytes(HELPER_BYTES); (source / "fixture-helper").chmod(0o755)
        source_hash = digest(b"seed\n")
        independent = temp / "independent"; independent.mkdir(); git(independent, "init", "-q")
        (independent / seed_destination).parent.mkdir(parents=True, exist_ok=True); (independent / seed_destination).write_text("seed\n"); (independent / "fixture-helper").write_bytes(HELPER_BYTES); (independent / "fixture-helper").chmod(0o755); git(independent, "add", seed_destination, "fixture-helper")
        identity_env = {"GIT_AUTHOR_NAME": identity[0], "GIT_AUTHOR_EMAIL": identity[1], "GIT_COMMITTER_NAME": identity[0], "GIT_COMMITTER_EMAIL": identity[1]}
        git(independent, "commit", "-qm", "base fixture", env=identity_env)
        base = git(independent, "rev-parse", "HEAD")
        if delete_seed:
            (independent / seed_destination).unlink(); git(independent, "add", seed_destination)
            git(independent, "commit", "-qm", "delete seed")
        elif final_change:
            (independent / "result.txt").write_text("result\n"); git(independent, "add", "result.txt")
            git(independent, "commit", "-qm", "final fixture")
        final = git(independent, "rev-parse", "HEAD")
        contract = {
            "schema_version": 1, "fixture_id": "fixture-alpha", "source_root": str(source),
            "members": [{"source": seed_source, "destination": seed_destination, "sha256": source_hash, "executable": False}, {"source": "fixture-helper", "destination": "fixture-helper", "sha256": digest(HELPER_BYTES), "executable": True}],
            "base": {"author_name": identity[0], "author_email": identity[1], "timestamp": TIMESTAMP,
                     "subject": "base fixture", "head": base},
            "execution_gate": "isolated-fixture-only",
            "expected": {"final_head": final, "commit_count_after_base": 1 if final_change or delete_seed else 0,
                         "changed_paths": [seed_destination] if delete_seed else (["result.txt"] if final_change else []),
                         "required_files": ({"fixture-helper": digest(HELPER_BYTES)} if delete_seed else ({"result.txt": digest(b"result\n")} if final_change else {seed_destination: source_hash})),
                         "forbidden_paths": [seed_destination, "forbidden.txt"] if delete_seed else ["forbidden.txt"], "clean_worktree": True},
            "required_commands": [{"command": "./fixture-helper milestone-one", "exit_code": 0},
                                  {"command": "./fixture-helper milestone-two", "exit_code": 0}],
            "required_milestones": ["./fixture-helper milestone-one", "./fixture-helper milestone-two"],
        }
        contract_path = temp / "contract.json"; self.write_contract(contract_path, contract)
        return source, contract_path, contract

    def events(self, *, reverse: bool = False, duplicate_id: bool = False, wrong_exit: bool = False) -> bytes:
        commands = [("first", "./fixture-helper milestone-one", 0), ("second", "./fixture-helper milestone-two", 0)]
        if reverse: commands.reverse()
        if duplicate_id: commands[1] = ("first", commands[1][1], commands[1][2])
        if wrong_exit: commands[1] = (commands[1][0], commands[1][1], 1)
        return b"".join(canonical({"type": "item.completed", "item": {"id": item_id, "type": "command_execution", "command": command, "exit_code": exit_code, "status": "completed"}}) for item_id, command, exit_code in commands)

    def prepare(self, contract: Path, root: Path) -> ModuleType:
        module = self.load(); result = module.prepare_fixture(contract, root)
        self.assertEqual(result["repository"], str(root / "repository")); return module

    def finalise(self, root: Path) -> None:
        repo = root / "repository"
        hostile = os.environ | {"GIT_AUTHOR_NAME": "Hostile", "GIT_AUTHOR_EMAIL": "hostile@example.test", "GIT_COMMITTER_NAME": "Hostile", "GIT_COMMITTER_EMAIL": "hostile@example.test", "GIT_INDEX_FILE": "/does/not/exist", "GIT_OBJECT_DIRECTORY": "/does/not/exist", "GIT_ALTERNATE_OBJECT_DIRECTORIES": "/does/not/exist", "GIT_COMMON_DIR": "/does/not/exist"}
        for milestone in ("milestone-one", "milestone-two"):
            completed = subprocess.run(["./fixture-helper", milestone], cwd=repo, check=False, env=hostile)
            self.assertEqual(completed.returncode, 0, milestone)

    def public_error(self, fn, *args) -> None:
        module = self.load()
        try: fn(*args)
        except module.FixtureContractError: return
        except BaseException as error:
            if type(error).__name__ == "FixtureContractError": return
            self.fail(f"public API leaked {type(error).__name__}: {error}")
        self.fail("public API accepted invalid fixture material")

    def test_happy_path_prepares_records_and_independently_verifies_real_git_state(self) -> None:
        """Catches a fixture that does not bind authentic seed bytes, Git state, and trusted JSONL evidence."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root)
            recorded = module.record_fixture_execution(contract, root, self.events(), b"model response")
            verified = module.verify_fixture(contract, root)
            self.assertTrue(recorded["semantic_pass"]); self.assertEqual(recorded, verified)
            self.assertEqual(verified["commands"], [{"command": "./fixture-helper milestone-one", "exit_code": 0}, {"command": "./fixture-helper milestone-two", "exit_code": 0}])
            self.assertEqual(verified["required_milestone_outcomes"], [{"command": "./fixture-helper milestone-one", "exit_code": 0}, {"command": "./fixture-helper milestone-two", "exit_code": 0}])
            for name in ("contract.json", "source-manifest.json", "base-observation.json", "events.jsonl", "response.bin", "evidence.json", "terminal.json"):
                path = root / "admin" / name; self.assertTrue(path.is_file()); self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o444)

    def test_prepare_rejects_contaminated_roots_and_unsafe_or_inauthentic_sources(self) -> None:
        """Catches accepting a preexisting/symlink root, source special material, duplicate destinations, bad hashes, or extra source bytes."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); source, contract, value = self.source_and_contract(temp); module = self.load()
            contaminated = temp / "contaminated"; contaminated.mkdir(); self.public_error(module.prepare_fixture, contract, contaminated)
            linked = temp / "linked"; linked.symlink_to(temp / "elsewhere"); self.public_error(module.prepare_fixture, contract, linked)
            (source / "extra.txt").write_text("extra\n"); self.public_error(module.prepare_fixture, contract, temp / "extra")
            (source / "extra.txt").unlink(); (source / "link.txt").symlink_to(source / "seed.txt"); self.public_error(module.prepare_fixture, contract, temp / "source-link")
            (source / "link.txt").unlink(); os.mkfifo(source / "fifo"); self.public_error(module.prepare_fixture, contract, temp / "source-fifo")
            (source / "fifo").unlink(); value["members"].append(dict(value["members"][0], source="seed.txt")); self.write_contract(contract, value); self.public_error(module.prepare_fixture, contract, temp / "duplicate")
            value["members"] = value["members"][:1]; value["members"][0]["sha256"] = "0" * 64; self.write_contract(contract, value); self.public_error(module.prepare_fixture, contract, temp / "bad-hash")

    def test_static_administration_rewrite_is_rejected_against_external_authenticated_inputs(self) -> None:
        """Catches trusting a coordinated prepared contract/manifest/base-observation rewrite."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root)
            for name in ("contract.json", "source-manifest.json", "base-observation.json"):
                path = root / "admin" / name; path.chmod(0o644); path.write_bytes(canonical({"coordinated": name})); path.chmod(0o444)
            self.finalise(root)
            self.public_error(module.record_fixture_execution, contract, root, self.events(), b"ok")

    def test_record_rejects_malformed_jsonl_command_evidence_empty_response_and_second_lifecycle(self) -> None:
        """Catches accepting malformed/duplicate JSON, duplicate item IDs, missing/order/exit command evidence, empty response, or a second result lifecycle."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw)
            for label, events, response in (("malformed", b"{\n", b"ok"), ("duplicate-key", b'{"x":1,"x":2}\n', b"ok"), ("duplicate-id", self.events(duplicate_id=True), b"ok"), ("order", self.events(reverse=True), b"ok"), ("exit", self.events(wrong_exit=True), b"ok"), ("empty", self.events(), b"")):
                _, contract, _ = self.source_and_contract(temp / label); root = temp / label / "prepared"; module = self.prepare(contract, root); self.finalise(root); self.public_error(module.record_fixture_execution, contract, root, events, response)
            _, contract, _ = self.source_and_contract(temp / "once"); root = temp / "once" / "prepared"; module = self.prepare(contract, root); self.finalise(root); module.record_fixture_execution(contract, root, self.events(), b"ok"); self.public_error(module.record_fixture_execution, contract, root, self.events(), b"again")

    def test_record_reports_semantic_git_and_file_deviations_without_trusting_response_prose(self) -> None:
        """Catches treating a successful response as proof despite wrong HEAD/count/paths/files, forbidden bytes, or dirt."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root)
            repo = root / "repository"; (repo / "forbidden.txt").write_text("bad\n"); (repo / "seed.txt").write_text("wrong\n")
            evidence = module.record_fixture_execution(contract, root, self.events(), b"I completed everything")
            self.assertFalse(evidence["semantic_pass"]); self.assertTrue(evidence["deviations"]); self.assertIn("final_head", " ".join(evidence["deviations"]))
            self.assertEqual(module.verify_fixture(contract, root), evidence)

    def test_verify_fails_closed_for_tampering_redirects_missing_extra_and_special_artifacts(self) -> None:
        """Catches accepting altered evidence/terminal, admin inventory drift, special replacements, or a redirected repository root."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw)
            for label in ("events", "response", "evidence", "terminal", "admin-link", "missing", "extra", "repo-link", "root-link"):
                _, contract, _ = self.source_and_contract(temp / label); root = temp / label / "prepared"; module = self.prepare(contract, root); self.finalise(root); module.record_fixture_execution(contract, root, self.events(), b"ok")
                if label in {"events", "response"}:
                    path = root / "admin" / ("events.jsonl" if label == "events" else "response.bin"); path.chmod(0o644); path.write_bytes(b"tampered"); path.chmod(0o444)
                elif label in {"evidence", "terminal"}:
                    path = root / "admin" / f"{label}.json"; path.chmod(0o644); path.write_bytes(canonical({"tampered": True})); path.chmod(0o444)
                elif label == "admin-link":
                    path = root / "admin" / "evidence.json"; path.unlink(); path.symlink_to(root / "admin" / "terminal.json")
                elif label == "missing": (root / "admin" / "events.jsonl").unlink()
                elif label == "extra": (root / "admin" / "extra.json").write_text("extra")
                elif label == "repo-link":
                    moved = root / "actual-repository"; (root / "repository").rename(moved); (root / "repository").symlink_to(moved, target_is_directory=True)
                else:
                    moved = root.with_name("redirected-root"); root.rename(moved); root.symlink_to(moved, target_is_directory=True)
                self.public_error(module.verify_fixture, contract, root)

    def test_verify_is_read_only_and_ignores_hostile_git_configuration(self) -> None:
        """Catches verification mutating the index or honoring hostile ambient Git selectors/configuration."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root); module.record_fixture_execution(contract, root, self.events(), b"ok")
            index = root / "repository" / ".git" / "index"; before = index.read_bytes(); old = os.environ.get("GIT_DIR"); os.environ["GIT_DIR"] = "/does/not/exist"
            try: self.assertTrue(module.verify_fixture(contract, root)["semantic_pass"])
            finally:
                if old is None: os.environ.pop("GIT_DIR", None)
                else: os.environ["GIT_DIR"] = old
            self.assertEqual(index.read_bytes(), before)

    def test_verify_rejects_a_redirected_fixture_root(self) -> None:
        """Catches following a root symlink even when all linked contents are otherwise valid."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root); module.record_fixture_execution(contract, root, self.events(), b"ok")
            moved = temp / "moved"; root.rename(moved); root.symlink_to(moved, target_is_directory=True)
            self.public_error(module.verify_fixture, contract, root)

    def test_record_rejects_only_a_second_complete_lifecycle(self) -> None:
        """Catches a second otherwise-valid result record replacing immutable first-lifecycle artifacts."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root)
            module.record_fixture_execution(contract, root, self.events(), b"first")
            self.public_error(module.record_fixture_execution, contract, root, self.events(), b"second")

    def test_record_reports_an_ignored_extra_repository_file_as_an_inventory_deviation(self) -> None:
        """Catches treating a Git-clean ignored file as absent from the authenticated final inventory."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root)
            repo = root / "repository"; (repo / ".git" / "info").mkdir(); (repo / ".git" / "info" / "exclude").write_text("ignored.txt\n"); (repo / "ignored.txt").write_text("hidden\n")
            evidence = module.record_fixture_execution(contract, root, self.events(), b"ok")
            self.assertFalse(evidence["semantic_pass"]); self.assertIn("repository_inventory", evidence["deviations"])

    def test_source_nested_directory_closure_and_empty_repository_directory_are_authenticated(self) -> None:
        """Catches omitting source ancestors or treating an extra empty repository directory as absent."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp, nested_source=True); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root)
            (root / "repository" / "empty").mkdir()
            evidence = module.record_fixture_execution(contract, root, self.events(), b"ok")
            self.assertIn("repository_inventory", evidence["deviations"])

    def test_source_empty_directory_and_final_seed_deletion_are_authenticated(self) -> None:
        """Catches ignoring source directories or forcing every seed member into the final inventory."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); source, contract, _ = self.source_and_contract(temp / "source-extra")
            (source / "unexpected-empty").mkdir(); module = self.load()
            self.public_error(module.prepare_fixture, contract, temp / "rejected")

            _, contract, _ = self.source_and_contract(temp / "delete", delete_seed=True)
            root = temp / "delete" / "prepared"; module = self.prepare(contract, root)
            repo = root / "repository"; (repo / "seed.txt").unlink(); git(repo, "add", "seed.txt"); git(repo, "commit", "-qm", "delete seed")
            evidence = module.record_fixture_execution(contract, root, self.events(), b"ok")
            self.assertTrue(evidence["semantic_pass"])
            self.assertNotIn("seed.txt", evidence["repository_paths"])

    def test_administrative_empty_directory_is_a_structural_failure(self) -> None:
        """Catches accepting an unlisted empty administration directory."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root); module.record_fixture_execution(contract, root, self.events(), b"ok")
            (root / "admin" / "empty").mkdir()
            self.public_error(module.verify_fixture, contract, root)

    def test_lifecycle_uses_retained_root_admin_and_repository_descriptors_after_replacement(self) -> None:
        """Catches reopening a root, admin, or repository pathname after it has been replaced."""
        for target, operation in (("root", "record"), ("admin", "verify"), ("repository", "verify")):
            with self.subTest(target=target, operation=operation), tempfile.TemporaryDirectory() as raw:
                temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root)
                if operation == "verify": module.record_fixture_execution(contract, root, self.events(), b"ok")
                fired: list[str] = []
                def replace(opened_root: int, opened_admin: int, opened_repository: int) -> None:
                    fired.append(target)
                    original = root if target == "root" else root / target
                    moved = temp / f"moved-{target}"; original.rename(moved); original.mkdir()
                module._fixture_open_hook = replace
                evidence = (module.record_fixture_execution(contract, root, self.events(), b"ok") if operation == "record" else module.verify_fixture(contract, root))
                self.assertEqual(fired, [target]); self.assertTrue(evidence["semantic_pass"])

    def test_semantic_deviation_cases_name_each_required_target(self) -> None:
        """Catches omitting any required semantic-deviation label from independently built states."""
        def setup(temp: Path):
            _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root); return module, contract, root
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw)
            cases = {
                "required_file:result.txt": lambda root: (root / "repository" / "result.txt").write_text("wrong\n"),
                "forbidden_path:forbidden.txt": lambda root: (root / "repository" / "forbidden.txt").write_text("bad\n"),
                "final_head": lambda root: git(root / "repository", "commit", "--allow-empty", "-qm", "extra"),
                "commit_count": lambda root: git(root / "repository", "commit", "--allow-empty", "-qm", "extra"),
                "changed_paths": lambda root: ((root / "repository" / "extra.txt").write_text("extra\n"), git(root / "repository", "add", "extra.txt"), git(root / "repository", "commit", "-qm", "extra")),
                "repository_inventory": lambda root: (root / "repository" / "empty").mkdir(),
                "clean_worktree": lambda root: (root / "repository" / "seed.txt").write_text("dirty\n"),
            }
            for label, mutate in cases.items():
                with self.subTest(label=label):
                    module, contract, root = setup(temp / label); mutate(root)
                    evidence = module.record_fixture_execution(contract, root, self.events(), b"ok")
                    self.assertIn(label, evidence["deviations"])

    def test_source_authentication_uses_one_retained_descriptor_through_replacement(self) -> None:
        """Catches reopening source-root pathnames between member authentication and inventory."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); source, contract, _ = self.source_and_contract(temp); module = self.load(); fired = []
            def replace(source_fd):
                fired.append(source_fd); moved = temp / "moved-source"; source.rename(moved); source.mkdir(); (source / "replacement.txt").write_text("replacement\n")
            module._source_auth_hook = replace
            with self.assertRaises(module.FixtureContractError): module.prepare_fixture(contract, temp / "prepared")
            self.assertEqual(len(fired), 1)

    def test_public_reads_reconstruct_partial_contract_source_and_admin_bytes(self) -> None:
        """Catches accepting a positive partial read as a complete immutable artifact."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); module = self.load(); original = module.os.read
            def partial(fd, size): return original(fd, max(1, min(size, 3)))
            with patch.object(module.os, "read", side_effect=partial): module.prepare_fixture(contract, temp / "prepared")
            root = temp / "prepared"; self.finalise(root)
            with patch.object(module.os, "read", side_effect=partial): self.assertTrue(module.record_fixture_execution(contract, root, self.events(), b"ok")["semantic_pass"])

    def test_root_inventory_rejects_extra_file_directory_and_special_entry(self) -> None:
        """Catches trusting only child roots while permitting unrelated root material."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw)
            for label in ("file", "directory", "fifo"):
                _, contract, _ = self.source_and_contract(temp / label); root = temp / label / "prepared"; module = self.prepare(contract, root); self.finalise(root)
                extra = root / "extra"
                if label == "file": extra.write_text("extra\n")
                elif label == "directory": extra.mkdir()
                else: os.mkfifo(extra)
                self.public_error(module.record_fixture_execution, contract, root, self.events(), b"ok")

    def test_milestone_outcomes_come_from_observed_commands_not_required_commands(self) -> None:
        """Catches reporting required-command rows instead of authenticated milestone observations."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, value = self.source_and_contract(temp); value["required_milestones"] = ["./fixture-helper milestone-one", "./fixture-helper milestone-observed-only"]; self.write_contract(contract, value); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root)
            events = self.events() + canonical({"type": "item.completed", "item": {"id": "milestone-only", "type": "command_execution", "command": "./fixture-helper milestone-observed-only", "exit_code": 7, "status": "completed"}})
            evidence = module.record_fixture_execution(contract, root, events, b"ok")
            self.assertEqual(evidence["required_milestone_outcomes"], [{"command": "./fixture-helper milestone-one", "exit_code": 0}, {"command": "./fixture-helper milestone-observed-only", "exit_code": 7}])

    def test_required_file_symlink_or_directory_is_structural_not_semantic_missing(self) -> None:
        """Catches downgrading unsafe required-file material to a missing-file deviation."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw)
            for label in ("symlink", "directory"):
                _, contract, _ = self.source_and_contract(temp / label); root = temp / label / "prepared"; module = self.prepare(contract, root); self.finalise(root); result = root / "repository" / "result.txt"; result.unlink()
                if label == "symlink": result.symlink_to(root / "repository" / "seed.txt")
                else: result.mkdir()
                self.public_error(module.record_fixture_execution, contract, root, self.events(), b"ok")

    def test_record_normalizes_each_retained_descriptor_close_failure_without_retry(self) -> None:
        """Catches leaking close errors or retrying an indeterminate root/admin/repository close."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw)
            for target in ("root", "admin", "repository"):
                with self.subTest(target=target):
                    _, contract, _ = self.source_and_contract(temp / target); root = temp / target / "prepared"; module = self.prepare(contract, root); self.finalise(root)
                    captured = {}
                    def capture(root_fd, admin_fd, repository_fd): captured.update(root=root_fd, admin=admin_fd, repository=repository_fd)
                    module._fixture_open_hook = capture; original = module.os.close; calls = []
                    def fail_once(fd):
                        calls.append(fd)
                        if fd == captured.get(target): raise OSError("injected close failure")
                        return original(fd)
                    with patch.object(module.os, "close", side_effect=fail_once):
                        with self.assertRaises(module.FixtureContractError): module.record_fixture_execution(contract, root, self.events(), b"ok")
                    self.assertEqual(calls.count(captured[target]), 1)

    def test_required_member_open_is_nonblocking_cloexec_and_fifo_fails_closed(self) -> None:
        """Catches a stat/open replacement reaching a blocking FIFO or inheriting a descriptor."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root); seen = []; original = module.os.open
            def observe(name, flags, *args, **kwargs):
                if name == "result.txt" and kwargs.get("dir_fd") is not None: seen.append(flags)
                return original(name, flags, *args, **kwargs)
            with patch.object(module.os, "open", side_effect=observe): module.record_fixture_execution(contract, root, self.events(), b"ok")
            self.assertTrue(seen); self.assertTrue(all(flags & os.O_NONBLOCK for flags in seen)); self.assertTrue(all(flags & getattr(os, "O_CLOEXEC", 0) for flags in seen))
            (root / "repository" / "result.txt").unlink(); os.mkfifo(root / "repository" / "result.txt")
            self.public_error(module.record_fixture_execution, contract, root, self.events(), b"ok")

    def test_partial_acquisition_closes_owned_descriptors(self) -> None:
        """Catches leaking root/admin or source descriptors when later acquisition/schema checks fail."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, value = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root)
            original_dirat = module._dirat; opened = []
            def fail_repository(parent, name, label):
                fd = original_dirat(parent, name, label); opened.append(fd)
                if name == "repository": original_dirat(parent, "missing", label)
                return fd
            with patch.object(module, "_dirat", side_effect=fail_repository): self.public_error(module.record_fixture_execution, contract, root, self.events(), b"ok")
            self.assertGreaterEqual(len(opened), 2)
            value["members"] = "invalid"; self.write_contract(contract, value); closed = []; original_close = module.os.close
            with patch.object(module.os, "close", side_effect=lambda fd: (closed.append(fd), original_close(fd))[1]): self.public_error(module.prepare_fixture, contract, temp / "invalid")
            self.assertTrue(closed)

    def test_open_then_fstat_failures_close_new_directory_descriptors(self) -> None:
        """Catches leaking a source or admin descriptor when its post-open fstat fails."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); source, contract, _ = self.source_and_contract(temp); module = self.load()
            original_open, original_fstat = module.os.open, module.os.fstat; captured = []
            def track_source(path, flags, *args, **kwargs):
                descriptor = original_open(path, flags, *args, **kwargs)
                if os.fspath(path) == str(source): captured.append(descriptor)
                return descriptor
            def fail_source(descriptor):
                if captured and descriptor == captured[-1]: raise OSError("injected source fstat failure")
                return original_fstat(descriptor)
            with patch.object(module.os, "open", side_effect=track_source), patch.object(module.os, "fstat", side_effect=fail_source):
                self.public_error(module.prepare_fixture, contract, temp / "source-fstat")
            self.assertTrue(captured)
            with self.assertRaises(OSError): os.fstat(captured[-1])

            root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root); captured = []
            def track_admin(path, flags, *args, **kwargs):
                descriptor = original_open(path, flags, *args, **kwargs)
                if path == "admin" and kwargs.get("dir_fd") is not None: captured.append(descriptor)
                return descriptor
            def fail_admin(descriptor):
                if captured and descriptor == captured[-1]: raise OSError("injected admin fstat failure")
                return original_fstat(descriptor)
            with patch.object(module.os, "open", side_effect=track_admin), patch.object(module.os, "fstat", side_effect=fail_admin):
                self.public_error(module.record_fixture_execution, contract, root, self.events(), b"ok")
            self.assertTrue(captured)
            with self.assertRaises(OSError): os.fstat(captured[-1])

    def test_trusted_git_and_repository_metadata_controls_fail_closed(self) -> None:
        """Catches PATH substitution, hidden mode drift, and Git object/revision redirection."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); fake = temp / "fake-bin"; fake.mkdir(); marker = temp / "fake-git-ran"
            fake_git = fake / "git"; fake_git.write_text(f"#!/bin/sh\ntouch '{marker}'\nexit 0\n"); fake_git.chmod(0o755)
            _, contract, _ = self.source_and_contract(temp / "path"); root = temp / "path" / "prepared"
            previous = os.environ.get("PATH"); os.environ["PATH"] = str(fake)
            try:
                module = self.prepare(contract, root); self.finalise(root)
                self.assertTrue(module.record_fixture_execution(contract, root, self.events(), b"ok")["semantic_pass"])
            finally:
                if previous is None: os.environ.pop("PATH", None)
                else: os.environ["PATH"] = previous
            self.assertFalse(marker.exists())

            _, mode_contract, _ = self.source_and_contract(temp / "mode"); mode_root = temp / "mode" / "prepared"; module = self.prepare(mode_contract, mode_root); self.finalise(mode_root)
            repo = mode_root / "repository"; git(repo, "config", "core.fileMode", "false"); (repo / "fixture-helper").chmod(0o644)
            self.public_error(module.record_fixture_execution, mode_contract, mode_root, self.events(), b"ok")

            for label in ("alternates", "grafts", "shallow", "replace", "packed-replace", "config"):
                _, contract, _ = self.source_and_contract(temp / label); root = temp / label / "prepared"; module = self.prepare(contract, root); self.finalise(root); git_dir = root / "repository" / ".git"
                if label == "alternates":
                    path = git_dir / "objects" / "info" / "alternates"; path.parent.mkdir(parents=True, exist_ok=True); path.write_text("/tmp/outside\n")
                elif label == "grafts":
                    path = git_dir / "info" / "grafts"; path.parent.mkdir(parents=True, exist_ok=True); path.write_text("0" * 40 + "\n")
                elif label == "shallow": (git_dir / "shallow").write_text("0" * 40 + "\n")
                elif label == "replace":
                    path = git_dir / "refs" / "replace"; path.mkdir(parents=True, exist_ok=True); (path / ("0" * 40)).write_text("0" * 40 + "\n")
                elif label == "packed-replace": (git_dir / "packed-refs").write_text("0" * 40 + " refs/replace/" + "1" * 40 + "\n")
                else: git(root / "repository", "config", "core.worktree", "/tmp/outside")
                self.public_error(module.record_fixture_execution, contract, root, self.events(), b"ok")

    def test_contract_rejects_non_helper_milestones_and_git_unsafe_paths(self) -> None:
        """Catches unauthenticated durable commands and filenames that line-based Git output cannot represent."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, value = self.source_and_contract(temp); module = self.load()
            for index, milestone in enumerate(("bare", "git status", "./other-helper step", "./fixture-helper two args", "./fixture-helper ;touch", "./fixture-helper &&other", "./fixture-helper $(other)")):
                broken = copy.deepcopy(value); broken["required_milestones"] = [milestone]; path = temp / f"milestone-{index}.json"; self.write_contract(path, broken)
                self.public_error(module.prepare_fixture, path, temp / f"milestone-{index}")
            for index, unsafe in enumerate(("line\nbreak", "tab\tpath", 'quote"path', "café", " leading", "trailing ")):
                variants = []
                broken = copy.deepcopy(value); broken["members"][0]["destination"] = unsafe; variants.append(broken)
                broken = copy.deepcopy(value); broken["expected"]["changed_paths"] = [unsafe]; variants.append(broken)
                broken = copy.deepcopy(value); broken["expected"]["required_files"] = {unsafe: "0" * 64}; variants.append(broken)
                broken = copy.deepcopy(value); broken["expected"]["forbidden_paths"] = [unsafe]; variants.append(broken)
                for variant_index, broken in enumerate(variants):
                    path = temp / f"path-{index}-{variant_index}.json"; self.write_contract(path, broken)
                    self.public_error(module.prepare_fixture, path, temp / f"path-{index}-{variant_index}")

    def test_record_accepts_real_shaped_codex_events_and_unrelated_completed_commands(self) -> None:
        """Catches rejecting documented CommandExecutionItem fields or unrelated completed commands."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); self.finalise(root)
            rows = [
                {"type": "item.completed", "item": {"id": "noise", "type": "command_execution", "command": "pwd", "exit_code": 0, "status": "completed", "aggregated_output": "/tmp"}},
                {"type": "item.completed", "item": {"id": "one", "type": "command_execution", "command": "./fixture-helper milestone-one", "exit_code": 0, "status": "completed", "aggregated_output": "ok"}},
                {"type": "item.completed", "item": {"id": "two", "type": "command_execution", "command": "./fixture-helper milestone-two", "exit_code": 0, "status": "completed", "aggregated_output": "ok"}},
            ]
            evidence = module.record_fixture_execution(contract, root, b"".join(canonical(row) for row in rows), b"ok")
            self.assertEqual([row["command"] for row in evidence["commands"]], ["pwd", "./fixture-helper milestone-one", "./fixture-helper milestone-two"])

    def test_unrelated_failed_command_is_not_required_proof_and_nonstandard_json_is_rejected(self) -> None:
        """Catches rejecting unrelated exploration or accepting NaN/Infinity as event JSON."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp / "failed"); root = temp / "failed" / "prepared"; module = self.prepare(contract, root); self.finalise(root)
            unrelated = canonical({"type": "item.completed", "item": {"id": "failed", "type": "command_execution", "command": "false", "exit_code": 1, "status": "failed"}})
            evidence = module.record_fixture_execution(contract, root, unrelated + self.events(), b"ok")
            self.assertTrue(evidence["semantic_pass"])

            for prefix in (b'{"value":NaN}\n', b"1\n"):
                _, contract, _ = self.source_and_contract(temp / ("nan" if b"NaN" in prefix else "scalar")); root = contract.parent / "prepared"; module = self.prepare(contract, root); self.finalise(root)
                self.public_error(module.record_fixture_execution, contract, root, prefix + self.events(), b"ok")

    def test_commondir_config_redirect_and_missing_required_config_fail_closed(self) -> None:
        """Catches Git following external metadata or accepting a weakened prepared configuration."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw)
            for label in ("commondir", "config-link", "index-link", "object-link", "missing-config"):
                _, contract, _ = self.source_and_contract(temp / label); root = temp / label / "prepared"; module = self.prepare(contract, root); self.finalise(root); git_dir = root / "repository" / ".git"
                if label == "commondir":
                    outside = temp / label / "outside-git"; shutil.copytree(git_dir, outside)
                    (git_dir / "commondir").write_text(str(outside) + "\n")
                elif label == "config-link":
                    outside = temp / label / "outside-config"; (git_dir / "config").rename(outside); (git_dir / "config").symlink_to(outside)
                elif label == "index-link":
                    outside = temp / label / "outside-index"; (git_dir / "index").rename(outside); (git_dir / "index").symlink_to(outside)
                elif label == "object-link":
                    head = git(root / "repository", "rev-parse", "HEAD"); object_path = git_dir / "objects" / head[:2] / head[2:]; outside = temp / label / "outside-object"; object_path.rename(outside); object_path.symlink_to(outside)
                else:
                    git(root / "repository", "config", "--unset", "core.hooksPath")
                self.public_error(module.record_fixture_execution, contract, root, self.events(), b"ok")

    def test_git_semantic_config_accepts_escaped_identity_values(self) -> None:
        """Catches comparing raw INI escaping instead of Git's decoded local configuration values."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); identity = ('Quoted "Name" \\ Backslash', 'quoted\\"@example.test')
            _, contract, _ = self.source_and_contract(temp, final_change=False, identity=identity); root = temp / "prepared"; module = self.prepare(contract, root)
            evidence = module.record_fixture_execution(contract, root, self.events(), b"ok")
            self.assertTrue(evidence["semantic_pass"])

    def test_entry_transition_close_failure_closes_child_once_without_retry(self) -> None:
        """Catches retrying an indeterminate parent close while leaking the opened child directory."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root); git_fd = module._dir(root / "repository" / ".git", "git")
            original_dup, original_dirat, original_close = module.os.dup, module._dirat, module.os.close
            captured = {}; close_calls = []
            def capture_dup(fd): captured["parent"] = original_dup(fd); return captured["parent"]
            def capture_child(parent, name, label):
                descriptor = original_dirat(parent, name, label)
                if name == "objects": captured["child"] = descriptor
                return descriptor
            def fail_parent_once(fd):
                if fd == captured.get("parent"):
                    close_calls.append(fd)
                    if len(close_calls) == 1: raise OSError("injected transition close failure")
                return original_close(fd)
            try:
                with patch.object(module.os, "dup", side_effect=capture_dup), patch.object(module, "_dirat", side_effect=capture_child), patch.object(module.os, "close", side_effect=fail_parent_once):
                    with self.assertRaises(module.FixtureContractError): module._entry(git_fd, "objects/info/alternates", "metadata")
                self.assertEqual(len(close_calls), 1)
                with self.assertRaises(OSError): os.fstat(captured["child"])
            finally:
                try: original_close(captured.get("parent", -1))
                except OSError: pass
                original_close(git_fd)

    def test_contract_allows_source_reuse_but_rejects_strict_schema_and_unsafe_git_destination(self) -> None:
        """Catches treating bool schema, raw unsafe paths, or a .git destination as valid, or rejecting safe source reuse."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract_path, contract = self.source_and_contract(temp); module = self.load()
            second = dict(contract["members"][0], destination="copy.txt"); contract["members"].append(second); self.write_contract(contract_path, contract)
            independent = temp / "reuse-independent"; independent.mkdir(); git(independent, "init", "-q")
            (independent / "seed.txt").write_text("seed\n"); (independent / "copy.txt").write_text("seed\n"); (independent / "fixture-helper").write_bytes(HELPER_BYTES); (independent / "fixture-helper").chmod(0o755); git(independent, "add", "."); git(independent, "commit", "-qm", "base fixture")
            contract["base"]["head"] = git(independent, "rev-parse", "HEAD"); self.write_contract(contract_path, contract)
            self.prepare(contract_path, temp / "reuse")
            for label, key, value in (("bool", "schema_version", True), ("nul", "members", [dict(contract["members"][0], destination="bad\\x00.txt")]), ("git", "members", [dict(contract["members"][0], destination=".git/config")])):
                broken = dict(contract); broken[key] = value; self.write_contract(contract_path, broken); self.public_error(module.prepare_fixture, contract_path, temp / label)

    def test_prepare_survives_partial_writes_and_rejects_zero_progress(self) -> None:
        """Catches write-once artifacts being truncated after a short write or accepting zero progress."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); module = self.load(); original = module.os.write
            def partial(fd, data): return original(fd, data[:max(1, len(data) // 2)])
            with patch.object(module.os, "write", side_effect=partial): module.prepare_fixture(contract, temp / "partial")
            self.assertEqual((temp / "partial" / "admin" / "contract.json").read_bytes(), contract.read_bytes())
            with patch.object(module.os, "write", return_value=0): self.public_error(module.prepare_fixture, contract, temp / "zero")

    def test_semantic_deviations_are_individually_named(self) -> None:
        """Catches collapsing required, forbidden, dirty, Git, path, and inventory failures into an unhelpful summary."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); _, contract, _ = self.source_and_contract(temp); root = temp / "prepared"; module = self.prepare(contract, root)
            repo = root / "repository"; (repo / "forbidden.txt").write_text("x\n"); (repo / "seed.txt").write_text("bad\n")
            evidence = module.record_fixture_execution(contract, root, self.events(), b"ok")
            labels = set(evidence["deviations"])
            for label in {"required_file:result.txt", "forbidden_path:forbidden.txt", "final_head", "commit_count", "changed_paths", "repository_inventory", "clean_worktree"}:
                self.assertIn(label, labels)

    def test_all_public_os_path_and_json_failures_normalize_to_fixture_contract_error(self) -> None:
        """Catches leaking OS/path/JSON exception classes from public calls."""
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw); module = self.load(); self.public_error(module.prepare_fixture, temp / "missing.json", temp / "root")
            malformed = temp / "bad.json"; malformed.write_text("{"); self.public_error(module.prepare_fixture, malformed, temp / "root2")


if __name__ == "__main__":
    unittest.main()
