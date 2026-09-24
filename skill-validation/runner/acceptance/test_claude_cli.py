"""Actual Claude startup, Bash resolution and Skill delivery; zero inference."""
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import threading

import pytest

from skilltest.claude_runtime import ClaudeRuntime
from skilltest.providers import ProviderRequest, _arguments


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)


@pytest.mark.parametrize('mode', ['workspace-write', 'read-only'])
def test_actual_claude_startup_shell_and_skill_delivery(mode, monkeypatch):
    # Removing timezone access hangs startup; losing prepared PATH selects Apple Python.
    destination = os.environ.get('SKILLTEST_SANDBOX_EVIDENCE_DIR')
    if not destination or sys.platform != 'darwin':
        pytest.skip('set SKILLTEST_SANDBOX_EVIDENCE_DIR on macOS')
    evidence = Path(destination) / f'claude-cli-{mode}'
    evidence.mkdir(parents=True, exist_ok=False)
    captured = []
    body = '# Qualification probe\n\nReport the marker QUALIFIED_BODY_7391.\n'
    description = 'Use when asked to run the qualification probe.'
    probe = "command -v python3; python3 --version; command -v git; git --version\ncat <<'EOF'\nHEREDOC_QUALIFIED\nEOF"

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{}')

        def do_POST(self):
            if self.headers.get('x-api-key') != 'surrogate-key':
                self.send_error(403)
                return  # Never retain unexpected authentication or its request.
            raw = self.rfile.read(int(self.headers.get('Content-Length', '0')))
            if self.path.endswith('count_tokens'):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"input_tokens":100}')
                return
            request = json.loads(raw)
            captured.append(request)
            (evidence/'requests.json').write_text(json.dumps(captured, indent=2))
            n = len(captured)
            if n > 3:
                self.send_error(400)
                return
            block = (
                {'type': 'tool_use', 'id': 'shell', 'name': 'Bash', 'input': {'command': probe}}
                if n == 1 else
                {'type': 'tool_use', 'id': 'skill', 'name': 'Skill', 'input': {'skill': 'qualification-probe'}}
                if n == 2 else {'type': 'text', 'text': 'Qualification complete.'}
            )
            message = dict(id=f'msg_{n}', type='message', role='assistant', model=request['model'],
                           content=[], stop_reason=None, stop_sequence=None,
                           usage={'input_tokens': 100, 'output_tokens': 1})
            if n < 3:
                start = block | {'input': {}}
                delta = {'type': 'input_json_delta', 'partial_json': json.dumps(block['input'])}
            else:
                start = block | {'text': ''}
                delta = {'type': 'text_delta', 'text': block['text']}
            events = [
                {'type': 'message_start', 'message': message},
                {'type': 'content_block_start', 'index': 0, 'content_block': start},
                {'type': 'content_block_delta', 'index': 0, 'delta': delta},
                {'type': 'content_block_stop', 'index': 0},
                {'type': 'message_delta', 'delta': {'stop_reason': 'tool_use' if n < 3 else 'end_turn',
                 'stop_sequence': None}, 'usage': {'output_tokens': 10}},
                {'type': 'message_stop'},
            ]
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.end_headers()
            for event in events:
                self.wfile.write(f"event: {event['type']}\ndata: {json.dumps(event)}\n\n".encode())

    with tempfile.TemporaryDirectory(prefix='claude-cli-') as folder:
        root = Path(folder).resolve()
        fixture = root/'workspace/fixture'
        fixture.mkdir(parents=True)
        (root/'workspace/evidence').mkdir()
        home = root/'home'
        home.mkdir()
        (home/'.claude.json').write_text('{"hasCompletedOnboarding":true,"userID":"surrogate"}')
        skill = fixture/'.claude/skills/qualification-probe/SKILL.md'
        skill.parent.mkdir(parents=True)
        skill.write_text(f'---\nname: qualification-probe\ndescription: {description}\n---\n\n{body}')
        monkeypatch.setenv('HOME', str(home))
        monkeypatch.setenv('USER', 'fixture')
        monkeypatch.setattr(ClaudeRuntime, '_check_login', lambda *args: None)
        runtime = ClaudeRuntime(lambda _: None, permissions=mode)
        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            runtime.prepare(fixture)
            policy = Path(runtime.prefix[2])
            # Transport-only diagnostic guard; production filesystem grants are untouched.
            policy.write_text(policy.read_text() + '\n(deny network*)\n'
                '(allow network-outbound (remote ip "localhost:*"))\n'
                '(allow network-inbound (local ip "localhost:*"))\n')
            shutil.copy2(policy, evidence/'policy.sb')
            env = runtime.environment | {'ANTHROPIC_API_KEY': 'surrogate-key',
                'ANTHROPIC_BASE_URL': f'http://127.0.0.1:{server.server_port}'}
            python = shutil.which('python3', path=runtime.environment['PATH'])
            guard = subprocess.run([*runtime.prefix, python, '-c',
                'import socket; s=socket.socket(); s.settimeout(2); s.connect(("1.1.1.1",443))'],
                cwd=fixture, env=env, capture_output=True, text=True, timeout=10)
            assert guard.returncode and ('Operation not permitted' in guard.stderr or 'Permission denied' in guard.stderr)
            reachable = subprocess.run([*runtime.prefix, python, '-c',
                f'import urllib.request; urllib.request.urlopen("http://127.0.0.1:{server.server_port}")'],
                cwd=fixture, env=env, capture_output=True, timeout=10)
            assert reachable.returncode == 0
            request = ProviderRequest(fixture.parent, b'Run qualification.', root/'final.txt',
                                      'claude', 'sonnet', 'low', permissions=mode)
            argv = [*runtime.prefix, *_arguments(request, executable=runtime.executable),
                    '--debug-file', str(runtime.root/'tmp/debug.log')]
            (evidence/'command.json').write_text(json.dumps(argv))
            process = subprocess.Popen(argv, cwd=fixture, env=env, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
            timed_out = False
            try:
                out, err = process.communicate('Run qualification.', timeout=30)
            except subprocess.TimeoutExpired:
                timed_out = True
                os.killpg(process.pid, signal.SIGKILL)
                out, err = process.communicate()
            (evidence/'stdout.jsonl').write_text(out)
            (evidence/'stderr.txt').write_text(err)
            (evidence/'result.json').write_text(json.dumps(dict(returncode=process.returncode,
                timed_out=timed_out, requests=len(captured), provider_calls=0,
                cli_sha256=hashlib.sha256(Path(runtime.executable).read_bytes()).hexdigest())))
            debug = runtime.root/'tmp/debug.log'
            if debug.exists():
                shutil.copy2(debug, evidence/'debug.log')
            assert not timed_out, 'Claude startup did not reach the scripted endpoint/tools'
            assert process.returncode == 0, err
            events = [json.loads(line) for line in out.splitlines()]
            assert not any(isinstance(event.get('tool_use_result'), str) and event['tool_use_result'].startswith('Error:') for event in events), out
            shell = next(event['tool_use_result'] for event in events
                         if event.get('type') == 'user' and isinstance(event.get('tool_use_result'), dict)
                         and 'stdout' in event['tool_use_result'])
            lines = shell['stdout'].splitlines()
            assert lines[0] == python, shell
            assert lines[2] == shutil.which('git', path=runtime.environment['PATH']), shell
            assert tuple(map(int, lines[1].split()[1].split('.')[:2])) >= (3, 11)
            assert lines[4:] == ['HEREDOC_QUALIFIED'], shell
            assert not shell['stderr']
            assert len(captured) == 3
            assert any(description in s for s in strings(captured[0]))
            assert not any(body.strip() in s for s in strings(captured[0]))
            assert any(body.strip() in s for s in strings(captured[2]))
            assert events[-1]['type'] == 'result' and events[-1]['is_error'] is False
            assert events[-1]['result'] == 'Qualification complete.'
        finally:
            assert runtime.cleanup() is None
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
