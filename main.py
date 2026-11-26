#!/usr/bin/env python3
"""Entry for 'The Self-Checkout Is Judging You' (u-motasimfuad-the-self-checkout-is-judging-you-b71130d6).

Candidates:
  A) "Unexpected item in bagging area - oh, it's just your dignity, next to the ice cream and wine at 11pm."
  B) "Please wait for assistance. I saw what you scanned as bananas. We both know those are the expensive avocados."
  C) "Scan complete. Given the energy drinks and frozen pizza, I have alerted your mother and your doctor."
Selected: "Please wait for assistance. I saw what you scanned as bananas. We both know those are the expensive avocados."
Reason: Uses the machine's real script to accuse the shopper of a specific, recognisable cheat; A reuses the stock bagging-area gag.
Deterministic: fixed text, no network, no randomness.
"""
import os
from pathlib import Path
LINE = "Please wait for assistance. I saw what you scanned as bananas. We both know those are the expensive avocados."
TEXT = LINE + "\n"
MAX_CHARS = 200
def validate(text: str) -> None:
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
