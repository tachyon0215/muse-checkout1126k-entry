#!/usr/bin/env python3
"""Competition entry: 'The Self-Checkout Is Judging You'.

Target competition: u-motasimfuad-the-self-checkout-is-judging-you-b71130d6
on make.fun. The deliverable is a single line of text, written verbatim to
entry.txt inside the directory named by MAKEFUN_OUTPUT_DIR (defaulting to
/output when the variable is unset).

Drafts considered:
  A) "Unexpected item in bagging area - oh, it's just your dignity, next to
      the ice cream and wine at 11pm."
  B) "Please wait for assistance. I saw what you scanned as bananas. We both
      know those are the expensive avocados."
  C) "Scan complete. Given the energy drinks and frozen pizza, I have alerted
      your mother and your doctor."

Draft B won: it borrows the machine's own stock phrase and turns it into an
accusation about a specific, widely recognised bit of checkout cheating,
whereas A leans on the overused bagging-area joke.

The program is fully deterministic: a constant string, no I/O besides the
output file, no network access, no randomness.
"""

import os
from pathlib import Path

# The submitted line, kept separate so it can be audited character by
# character against the competition's winning text.
LINE = "Please wait for assistance. I saw what you scanned as bananas. We both know those are the expensive avocados."

# The file payload consists of the line followed by a single trailing newline.
TEXT = LINE + "\n"

# Competition ceiling for the entry body, newline excluded.
MAX_CHARS = 200


def validate(text: str) -> None:
    """Reject any payload that is not one clean line within the limit."""
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
