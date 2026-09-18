"""Resolve declared identities using bounded Git reads and retained file bytes."""

from hashlib import sha256
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import stat
import subprocess
import tempfile

from .formats import field, parse_json


def canonical(path):
    if not isinstance(path, str) or not path or "\\" in path or "\x00" in path:
        raise ValueError("identity path must be canonical")
    parts = PurePosixPath(path).parts
    if ".." in parts or str(PurePosixPath(path)) != path:
        raise ValueError("identity path must be canonical")
    return path


def regular_bytes(path):
    if not stat.S_ISREG(path.lstat().st_mode):
        raise ValueError(f"not a regular file: {path}")
    return path.read_bytes()


class Context:
    def __init__(self, path, report):
        self.path = Path(path)
        self.report = report
        self.cache = {}
        self.manifests = {}
        self.configs = {}
        self.criteria = {}
        try:
            self.root = Path(self.git_at(self.path.parent, "rev-parse", "--show-toplevel").decode().strip())
        except ValueError:
            try:
                self.root = Path(self.git_at(Path.cwd(), "rev-parse", "--show-toplevel").decode().strip())
            except ValueError:
                self.root = self.path.parent

    @staticmethod
    def git_at(root, *args):
        try:
            return subprocess.run(
                ["git", "--no-optional-locks", "-C", str(root), *args],
                capture_output=True,
                check=True,
                timeout=30,
            ).stdout
        except (OSError, subprocess.SubprocessError) as error:
            raise ValueError(f"Git identity unavailable: {args}") from error

    def read(self, identity, revision=None):
        path = canonical(identity["path"])
        rev = identity.get("git_revision", revision)
        digest = identity["sha256"]
        if not isinstance(digest, str) or not re.fullmatch("[0-9a-f]{64}", digest):
            raise ValueError(f"invalid hash for {path}")
        if Path(path).is_absolute():
            if rev is not None:
                raise ValueError(f"Git revision cannot identify external evidence: {path}")
            raw = regular_bytes(Path(path))
        else:
            if rev is not None and not re.fullmatch("[0-9a-f]{40}", rev):
                raise ValueError(f"full Git revision required for {path}")
            key = (path, rev)
            if key not in self.cache:
                if rev:
                    mode = self.git_at(self.root, "ls-tree", rev, "--", path).decode().split()
                    if not mode or mode[0] not in {"100644", "100755"}:
                        raise ValueError(f"Git regular file unavailable: {path}")
                    self.cache[key] = self.git_at(self.root, "show", f"{rev}:{path}")
                else:
                    self.cache[key] = regular_bytes(self.root / path)
            raw = self.cache[key]
        if sha256(raw).hexdigest() != digest:
            raise ValueError(f"hash mismatch: {path}")
        return raw

    def error(self, path, loc, rule, message, severity="error"):
        self.report.add(path, loc, rule, message, severity)

    def identity(self, ident, revision=None, owner=None, loc="$", frozen=False):
        try:
            if frozen and not Path(ident["path"]).is_absolute() and not ident.get("git_revision", revision):
                raise ValueError("Full Git revision required for a frozen repository citation")
            return self.read(ident, revision)
        except (OSError, ValueError, KeyError, TypeError) as error:
            self.error(owner or self.path, loc, "reference", str(error))
            return None

    def document(self, raw, path, expected, declared_version=None, allow_draft=False):
        from . import Report, structural

        local = Report()
        try:
            text = raw.decode("utf-8")
            if allow_draft:
                text = re.sub(r"^Status: draft$", "Status: prepared", text, count=1, flags=re.M)
            kind, value = structural(text, path, local)
            if kind != expected:
                local.add(path, "$", "artifact-kind", f"Expected {expected}, got {kind}")
            actual_version = (
                value.get("schema_version", value.get("format_version"))
                if isinstance(value, dict)
                else field(value, "Definition version" if expected == "case" else "Format version")
            )
            if declared_version is not None and actual_version != declared_version:
                local.add(
                    path, "version", "reference-version", "Declared version differs from retrieved document"
                )
        except (ValueError, UnicodeError, KeyError, TypeError) as error:
            local.add(path, "$", "invalid-document", str(error))
            value = None
        self.report.diagnostics.extend(local.diagnostics)
        self.report.structurally_valid &= local.structurally_valid
        self.report.complete &= local.complete
        self.report.unsupported |= local.unsupported
        return value if local.structurally_valid and local.complete and not local.unsupported else None

    def manifest(self, value, path, working=False):
        key = (str(path), value.get("source_revision"), str(value), working)
        if key in self.manifests:
            return self.manifests[key]
        revision = None if working else value["source_revision"]
        if not working and value["status"] != "frozen":
            self.error(
                path,
                "status",
                "unfinished",
                "Freeze inputs before stage readiness",
                "incomplete",
            )
        identities = []
        for name, ident in value["authorities"].items():
            identities.extend(
                (f"authorities.{name}", x) for x in (ident if isinstance(ident, list) else [ident])
            )
        identities += [(f"conditions.{c['id']}", c["configuration"]) for c in value["conditions"]]
        identities += [("subject_sources", x) for x in value["subject_sources"]]
        identities += [("controller_only", x) for x in value["controller_only"]]
        for loc, ident in identities:
            self.identity(ident, revision, path, loc)
        conditions = {c["id"]: c for c in value["conditions"]}
        source_map = {x["path"]: x for x in value["subject_sources"]}
        controller = {
            x["path"] for loc, x in identities if loc.startswith(("authorities", "controller_only"))
        }
        if controller & source_map.keys():
            self.error(
                path,
                "subject_sources",
                "controller-overlap",
                "Controller-only identities occur in subject sources",
            )
        expected = set()
        configs = {}
        # Materialize only declared pinned files into disposable controller scratch.
        # The actual config loader validates targets/settings, without dispatch.
        with tempfile.TemporaryDirectory(prefix="skilltest-docs-") as folder:
            base = Path(folder)
            for name, ident in source_map.items():
                if Path(name).is_absolute():
                    raise ValueError("subject sources must be repository-relative")
                raw = self.identity(ident, revision, path, "subject_sources")
                if raw is not None:
                    target = base / canonical(name)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(raw)
            for cid, condition in conditions.items():
                ident = condition["configuration"]
                config_name = canonical(ident["path"])
                if Path(config_name).is_absolute():
                    raise ValueError("configuration must be repository-relative")
                raw = self.identity(ident, revision, path, f"conditions.{cid}")
                if raw is None:
                    continue
                config = parse_json(raw)
                if not isinstance(config, dict):
                    self.error(
                        path, f"conditions.{cid}", "configuration", "Configuration must be a JSON object"
                    )
                    continue
                if ident.get("version") is not None and ident["version"] != config.get("schema_version"):
                    self.error(
                        path,
                        f"conditions.{cid}",
                        "reference-version",
                        "Declared version differs from configuration",
                    )
                configs[cid] = config
                # Reject escapes before asking the loader to read a source.
                sources = [config.get("prompt")] + [
                    f.get("source") for f in config.get("fixtures", []) if isinstance(f, dict)
                ]
                resolved = []
                for name in sources:
                    if not isinstance(name, str) or Path(name).is_absolute():
                        raise ValueError("configuration source must be relative")
                    resolved.append(
                        canonical(posixpath.normpath(posixpath.join(posixpath.dirname(config_name), name)))
                    )
                expected.update(resolved)
                if not set(resolved) <= source_map.keys():
                    self.error(
                        path,
                        f"conditions.{cid}",
                        "subject-membership",
                        "Configuration sources are missing from manifest",
                    )
                    continue
                config_path = base / config_name
                config_path.parent.mkdir(parents=True, exist_ok=True)
                config_path.write_bytes(raw)
                from skilltest.config import load_config, ConfigError

                try:
                    load_config(config_path)
                except ConfigError as error:
                    self.error(path, f"conditions.{cid}", "configuration", str(error))
                if condition["target_skill"] is not None and condition["target_skill"] not in resolved:
                    self.error(
                        path,
                        f"conditions.{cid}.target_skill",
                        "target-skill",
                        "Target skill is not supplied by this condition",
                    )
        if expected != source_map.keys():
            self.error(
                path,
                "subject_sources",
                "subject-membership",
                f"Expected exact configured union; missing {sorted(expected - source_map.keys())}, extra {sorted(source_map.keys() - expected)}",
            )
        cards = {}
        for ident in value["authorities"]["criteria"]:
            raw = self.identity(ident, revision, path, "authorities.criteria")
            if raw is None:
                continue
            text = self.document(raw, ident["path"], "case", ident.get("version"), allow_draft=working)
            if text is None:
                continue
            for name, want in [
                ("Study ID", value["study_id"]),
                ("Case ID", value["case_id"]),
            ]:
                if field(text, name) != want:
                    self.error(ident["path"], name, "identity", f"Expected {want}")
            parts = re.split(
                r"^### ",
                text.split("## Criteria", 1)[-1].split("## Limits", 1)[0],
                flags=re.M,
            )[1:]
            for card in parts:
                cid = card.split(":", 1)[0]
                applies = field(card, "Applies to") or ""
                ids = re.findall(r"`([^`]+)`", applies)
                if not ids:
                    ids = [x.strip() for x in applies.split(",")]
                if cid in cards:
                    self.error(
                        ident["path"],
                        cid,
                        "duplicate-id",
                        "Criterion repeated across definitions",
                    )
                if not ids or not set(ids) <= conditions.keys():
                    self.error(ident["path"], cid, "condition", "Unknown criterion condition")
                cards[cid] = (field(card, "Dimension"), set(ids))
        self.manifests[key] = (conditions, cards, configs)
        return conditions, cards, configs

    def result(self, value, path):
        raw = self.identity(value["manifest"], owner=path, loc="manifest", frozen=True)
        if raw is None:
            return None
        manifest = self.document(raw, value["manifest"]["path"], "manifest", value["manifest"].get("version"))
        if manifest is None:
            return None
        conditions, cards, configs = self.manifest(manifest, value["manifest"]["path"])
        condition = value["condition"]
        if condition not in conditions:
            self.error(path, "condition", "condition", "Condition not declared in manifest")
        expected = {cid for cid, (_, ids) in cards.items() if condition in ids}
        if {c["id"] for c in value["criteria"]} != expected:
            self.error(
                path,
                "criteria",
                "criterion-coverage",
                f"Require exactly {sorted(expected)}",
            )
        for c in value["criteria"]:
            if c["id"] in cards and c["dimension"] != cards[c["id"]][0]:
                self.error(
                    path,
                    c["id"],
                    "criterion-dimension",
                    "Dimension differs from criterion definition",
                )
        eids = {e["id"] for e in value["evidence"]}
        for c in [value["setup"], *value["criteria"], *value["observations"]]:
            if not set(c["evidence"]) <= eids:
                self.error(path, "evidence", "evidence-id", "Unknown evidence ID")
        for e in value["evidence"]:
            self.identity(e["artifact"], owner=path, loc=f"evidence.{e['id']}")
        return manifest

    def inventory(self, bundle, path):
        raw = self.identity(bundle["inventory"], owner=path, loc="bundle.inventory")
        if raw is None:
            return
        listing = parse_json(raw)
        base = Path(canonical(bundle["path"]))
        if not base.is_absolute() or base.is_symlink():
            raise ValueError("bundle must be a canonical absolute directory")
        if listing.get("format_version") != "1":
            self.error(
                path,
                "bundle.inventory",
                "unsupported-version",
                "Unsupported inventory version",
                "unsupported",
            )
            return
        if listing.get("bundle") != str(base):
            self.error(
                path,
                "bundle.inventory",
                "bundle-identity",
                "Inventory identifies another bundle",
            )
        actual = {}

        def visit(folder):
            for child in folder.iterdir():
                name = child.relative_to(base).as_posix()
                actual[name] = child.lstat()
                if stat.S_ISDIR(actual[name].st_mode):
                    visit(child)

        visit(base)
        entries = listing["entries"]
        names = [canonical(e["path"]) for e in entries]
        if any(Path(n).is_absolute() for n in names):
            raise ValueError("inventory entry must be relative")
        if len(set(names)) != len(names) or set(actual) != set(names):
            self.error(
                path,
                "bundle.inventory",
                "inventory-coverage",
                "Inventory does not match exact retained entries",
            )
        for entry in entries:
            name = entry["path"]
            target = base / name
            info = actual.get(name)
            if info is None:
                continue
            ok = oct(stat.S_IMODE(info.st_mode)) == entry["mode"]
            if entry["type"] == "file":
                ok &= (
                    stat.S_ISREG(info.st_mode)
                    and info.st_size == entry["bytes"]
                    and sha256(regular_bytes(target)).hexdigest() == entry["sha256"]
                )
            elif entry["type"] == "symlink":
                ok &= stat.S_ISLNK(info.st_mode) and os.readlink(target) == entry["target"]
            elif entry["type"] == "directory":
                ok &= stat.S_ISDIR(info.st_mode)
            else:
                ok = False
            if not ok:
                self.error(
                    path,
                    name,
                    "inventory-entry",
                    "Retained type/mode/bytes/hash or symlink differs",
                )
