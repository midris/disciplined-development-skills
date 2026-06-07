"""claude_runner.py — Subprocess wrapper for the review CLIs.

Used by both ``pre_pr_codex_review`` (runs ``codex review``) and
``dd_review_runner.py`` (runs ``claude -p`` OR ``codex review``). Name kept
historical; both reviewers route through the same Runner.

Design:

* ``subprocess.Popen`` + per-stream reader threads drain stdout/stderr
  line-by-line into both an in-memory buffer AND (when a ``log`` is
  attached) the JSONL observability stream. The thread pattern is the
  fix for the classic deadlock — without it, a child writing >64 KB
  fills its pipe buffer and blocks while the parent waits on ``wait()``.
* Watchdog: ``Popen.wait(timeout=...)`` raises ``TimeoutExpired``; the
  runner then sends ``SIGTERM``, waits ``grace_s`` seconds, and escalates
  to ``SIGKILL`` if the child still hasn't exited.
* Signal forwarding: when ``run()`` is invoked from the main thread, the
  runner installs ``SIGTERM`` / ``SIGHUP`` / ``SIGINT`` handlers that
  forward the signal to the live child and record the signal name on the
  Runner. Hook scripts run on the main thread; tests usually don't, in
  which case the install is a silent no-op (signal.signal requires main
  thread) and tests invoke ``_handle_signal`` synthetically.
* Structured return: ``RunResult`` carries ``exit_code`` (None on
  error/before-spawn), ``stdout`` / ``stderr`` strings, ``duration_s``,
  and ``exit_reason`` in ``{ok, timeout, signal:<NAME>, error:<class>}``.
"""

from __future__ import annotations

import dataclasses
import signal
import subprocess
import threading
import time
from typing import Any


@dataclasses.dataclass
class RunResult:
    exit_code: int | None
    stdout: str
    stderr: str
    duration_s: float
    exit_reason: str  # 'ok' | 'timeout' | 'signal:<NAME>' | 'error:<class>'


class Runner:
    """Wraps a Popen with reader threads, watchdog, and signal forwarding.

    Parameters
    ----------
    argv:
        Command line as a list — passed verbatim to ``Popen``.
    timeout_s:
        Wall-clock seconds before the watchdog fires.
    stdin_text:
        Optional bytes/text to feed the child's stdin. Written then
        closed before the wait loop, so the child can read to EOF.
    log:
        Optional ``logging_setup.HookLogger``. When supplied, every
        stdout/stderr line is emitted as a JSONL record (``event``
        = ``subprocess_stdout`` / ``subprocess_stderr``).
    grace_s:
        Seconds the child has between SIGTERM and SIGKILL on timeout.
    cwd:
        Optional working directory for the child. ``None`` inherits the
        parent's cwd. Load-bearing for the claude reviewer: in ``fetched``
        strategy claude runs ``git diff`` itself, so it must start in the repo
        being reviewed (codex self-wraps with ``cd``; claude has no such
        mechanism — without this it would review the parent process's cwd).
    """

    _FORWARDED_SIGNALS = (signal.SIGTERM, signal.SIGHUP, signal.SIGINT)

    def __init__(
        self,
        argv: list[str],
        timeout_s: float,
        stdin_text: str = "",
        log: Any | None = None,
        grace_s: float = 5.0,
        cwd: str | None = None,
    ) -> None:
        self.argv = argv
        self.timeout_s = timeout_s
        self.stdin_text = stdin_text
        self.log = log
        self.grace_s = grace_s
        self.cwd = cwd
        self._proc: subprocess.Popen | None = None
        self._signal_received: str | None = None

    # ---- main entry -------------------------------------------------------

    def run(self) -> RunResult:
        start = time.monotonic()
        try:
            self._proc = subprocess.Popen(
                self.argv,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.cwd,
            )
        except OSError as exc:  # FileNotFoundError is an OSError subclass
            return RunResult(
                exit_code=None,
                stdout="",
                stderr="",
                duration_s=time.monotonic() - start,
                exit_reason=f"error:{type(exc).__name__}",
            )

        if self.log is not None:
            self.log.emit("subprocess_spawn", argv=self.argv)

        prior_handlers = self._install_signal_handlers()
        stdout_buf: list[str] = []
        stderr_buf: list[str] = []
        t_out = threading.Thread(
            target=self._drain,
            args=(self._proc.stdout, stdout_buf, "subprocess_stdout"),
            daemon=True,
        )
        t_err = threading.Thread(
            target=self._drain,
            args=(self._proc.stderr, stderr_buf, "subprocess_stderr"),
            daemon=True,
        )
        t_out.start()
        t_err.start()

        # Popen(stdin=PIPE) guarantees self._proc.stdin is not None.
        try:
            if self.stdin_text:
                try:
                    self._proc.stdin.write(self.stdin_text)
                except BrokenPipeError:
                    pass
            try:
                self._proc.stdin.close()
            except BrokenPipeError:
                pass

            timed_out = False
            try:
                self._proc.wait(timeout=self.timeout_s)
            except subprocess.TimeoutExpired:
                timed_out = True
                self._terminate_with_grace()

            t_out.join(timeout=5.0)
            t_err.join(timeout=5.0)

            duration = time.monotonic() - start
            if timed_out:
                exit_reason = "timeout"
            elif self._signal_received is not None:
                exit_reason = f"signal:{self._signal_received}"
            else:
                exit_reason = "ok"

            result = RunResult(
                exit_code=self._proc.returncode,
                stdout="".join(stdout_buf),
                stderr="".join(stderr_buf),
                duration_s=duration,
                exit_reason=exit_reason,
            )
            if self.log is not None:
                self.log.emit(
                    "subprocess_exit",
                    exit_code=result.exit_code,
                    exit_reason=result.exit_reason,
                    duration_s=round(result.duration_s, 3),
                )
            return result
        finally:
            self._restore_signal_handlers(prior_handlers)

    # ---- internals --------------------------------------------------------

    def _drain(self, stream, buf: list[str], event: str) -> None:
        try:
            for line in stream:
                buf.append(line)
                if self.log is not None:
                    self.log.emit(event, line=line.rstrip("\n"))
        except (OSError, ValueError):
            # Stream closed mid-read (e.g. child killed); finish quietly.
            pass

    def _terminate_with_grace(self) -> None:
        if self._proc is None or self._proc.poll() is not None:
            return
        try:
            self._proc.send_signal(signal.SIGTERM)
        except (OSError, ProcessLookupError):
            return
        try:
            self._proc.wait(timeout=self.grace_s)
        except subprocess.TimeoutExpired:
            try:
                self._proc.kill()
            except (OSError, ProcessLookupError):
                pass
            try:
                self._proc.wait(timeout=2.0)
            except subprocess.TimeoutExpired:
                pass

    def _install_signal_handlers(self) -> dict:
        prior: dict = {}
        for sig in self._FORWARDED_SIGNALS:
            try:
                prior[sig] = signal.signal(sig, self._handle_signal)
            except (ValueError, OSError):
                # signal.signal must be called from the main thread. In
                # tests + threaded contexts this raises ValueError — the
                # runner skips the install silently so tests can still
                # invoke _handle_signal synthetically.
                pass
        return prior

    def _restore_signal_handlers(self, prior: dict) -> None:
        for sig, handler in prior.items():
            try:
                signal.signal(sig, handler)
            except (ValueError, OSError):
                pass

    def _handle_signal(self, signum: int, frame) -> None:
        # Order matters: only record _signal_received AFTER confirming the
        # child is still alive AND the send succeeded. A signal arriving
        # after the child has already exited naturally would otherwise
        # misreport exit_reason as "signal:X" for what's really "ok".
        # Note: Popen.send_signal is a *silent* no-op once returncode is
        # set (Python avoids the os.kill race by checking returncode
        # first), so we cannot rely on ProcessLookupError to detect a
        # post-exit signal — must check poll() ourselves.
        try:
            name = signal.Signals(signum).name
        except ValueError:
            name = str(signum)
        if self._proc is None or self._proc.poll() is not None:
            return
        try:
            self._proc.send_signal(signum)
        except (OSError, ProcessLookupError):
            return
        self._signal_received = name
        if self.log is not None:
            # HookLogger.emit already swallows OSError/TypeError/ValueError;
            # no second-layer except needed.
            self.log.emit("subprocess_signal_forwarded", signal=name)
