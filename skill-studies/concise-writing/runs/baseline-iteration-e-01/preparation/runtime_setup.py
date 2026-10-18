"""Controller-only E setup: select installed tools inside already granted scratch."""
from functools import wraps
import hashlib
import json
from pathlib import Path
import shlex

TOOLS = {
    'python3': Path('/opt/homebrew/opt/python@3.14/libexec/bin/python3').resolve(),
    'git': Path('/opt/homebrew/bin/git').resolve(),
}


def install():
    from skilltest.runtime import PreparationError
    from skilltest.claude_runtime import ClaudeRuntime
    from skilltest.codex_runtime import CodexRuntime

    for cls in (CodexRuntime, ClaudeRuntime):
        prepare = cls.prepare
        if getattr(prepare, '_cw_toolchain', False):
            continue

        @wraps(prepare)
        def prepared(self, fixture, _prepare=prepare):
            _prepare(self, fixture)
            directory = self.root / 'tmp' / 'toolchain'
            directory.mkdir(mode=0o700)
            identities = {}
            for name, target in TOOLS.items():
                if not target.is_file():
                    raise PreparationError(f'qualified tool is unavailable: {target}')
                (directory / name).symlink_to(target)
                identities[name] = {'path': str(target), 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()}
            self.environment['PATH'] = str(directory) + ':' + self.environment['PATH']
            (self.root / 'tmp/.zprofile').write_text('export PATH=' + shlex.quote(self.environment['PATH']) + '\n')
            self.log('CW prepared toolchain: ' + json.dumps(identities, sort_keys=True))

        prepared._cw_toolchain = True
        cls.prepare = prepared
