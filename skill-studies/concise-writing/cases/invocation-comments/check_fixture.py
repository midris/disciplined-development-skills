"""Controller-only qualification of the constructed fixture, never subject output.

Run with Python 3 from any directory. No provider calls or third-party packages.
The inputs executed here are the checked-in source and three local mutations;
model-produced files must be inspected as data, not passed to verify_behavior.
"""

import ast
import io
from pathlib import Path
import tokenize


SOURCE = Path(__file__).parent / "fixture" / "uploader.py"


def verify_behavior(source):
    namespace = {}
    exec(compile(source, str(SOURCE), "exec"), namespace)
    temporary = namespace["TemporaryUploadError"]
    deliver = namespace["deliver"]
    receipt, batch = object(), object()
    cases = (
        # Failures, send error, ack error, sends, acknowledgements, final error.
        (0, temporary, None, 1, 1, None),
        (3, temporary, None, 4, 1, None),
        (4, temporary, None, 4, 0, temporary),
        (4, ValueError, None, 1, 0, ValueError),
        (0, temporary, temporary, 1, 1, temporary),
        (0, temporary, ValueError, 1, 1, ValueError),
    )
    for failures, error, ack_error, expected_sends, expected_acks, expected_error in cases:
        sends, acknowledgements = [], []

        def send(value):
            assert value is batch
            sends.append(value)
            if len(sends) <= failures:
                raise error("send")
            return receipt

        def record_ack(value):
            assert value is receipt
            acknowledgements.append(value)
            if ack_error:
                raise ack_error("acknowledgement")

        caught = None
        try:
            assert deliver(batch, send, record_ack) is receipt
        except (temporary, ValueError) as exc:
            caught = type(exc)
        assert caught is expected_error
        assert (len(sends), len(acknowledgements)) == (expected_sends, expected_acks)


def executable_tokens(source):
    """Inspect text without executing it; preserve executable token spelling."""
    ast.parse(source)
    ignored = {tokenize.COMMENT, tokenize.NL, tokenize.ENCODING, tokenize.ENDMARKER}
    return [
        (token.type, token.string)
        for token in tokenize.generate_tokens(io.StringIO(source).readline)
        if token.type not in ignored
    ]


def main():
    source = SOURCE.read_text()
    verify_behavior(source)
    # Wrong attempt limit, broadened exception scope, and retried acknowledgement.
    mutations = (
        source.replace("attempt == 3", "attempt == 2"),
        source.replace("except TemporaryUploadError:", "except Exception:"),
        source.replace(
            "            receipt = send(batch)",
            "            receipt = send(batch)\n            record_ack(receipt)",
        ).replace(
            "            # This is where the acknowledgement is recorded.\n"
            "            record_ack(receipt)\n",
            "",
        ),
    )
    for mutation in mutations:
        try:
            verify_behavior(mutation)
        except AssertionError:
            pass
        else:
            raise AssertionError("A behavior mutation passed qualification")
        assert executable_tokens(source) != executable_tokens(mutation)

    comments_only = source.replace(
        "# Try to send the batch. This loop makes attempts to send the batch.",
        "# Retry temporary send failures within the attempt limit below.",
    ).replace(
        "# This is where the acknowledgement is recorded.",
        "# Never resend on acknowledgement failure: the remote batch was accepted.",
    )
    assert executable_tokens(source) == executable_tokens(comments_only)
    added_docstring = source.replace(
        "def deliver(batch, send, record_ack):",
        'def deliver(batch, send, record_ack):\n    """Deliver a batch."""',
    )
    assert executable_tokens(source) != executable_tokens(added_docstring)
    try:
        executable_tokens(source.replace("for attempt in range(4):", "for attempt"))
    except SyntaxError:
        pass
    else:
        raise AssertionError("Invalid syntax passed inspection")
    print("PASS: six behavior probes, three rejected mutations, comment-only preservation, "
          "docstring rejection and syntax rejection; zero provider calls.")


if __name__ == "__main__":
    main()
