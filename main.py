#!/usr/bin/env python3
"""Self-checkout entry for the make.fun contest 'The Self-Checkout Is Judging You'.

Contest slug: u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.

What this script does is deliberately boring: it takes one frozen sentence,
gives it a quick once-over, and drops it into a file called entry.txt inside
whichever folder MAKEFUN_OUTPUT_DIR points at (falling back to /output).
Nothing is fetched, randomised, or read from disk, so two runs always yield
the same bytes.

How the sentence was picked
---------------------------
Three contenders were written out and scored against the judging notes in
the contest RULES (instantly graspable on a first read, then surprise,
economy, novelty, and how cleanly it reads aloud):

  * the bagging-area dignity gag -- funny, but that joke is everywhere;
  * the till's own 'please wait for assistance' announcement, repurposed
    as a callout of the banana-versus-avocado barcode swap;
  * a scan summary that tattles to the shopper's mother and doctor.

The middle one took it. It keeps the machine's authentic phrasing and aims
it at one precise, familiar fiddle instead of a generic checkout cliché.
"""

import os
from pathlib import Path

# The sentence being entered, stored in a single spot so it can be checked
# against the contest text without digging through the logic.
JUDGEMENT = (
    "Please wait for assistance. I saw what you scanned as bananas. "
    "We both know those are the expensive avocados."
)

# What actually lands on disk: the sentence plus exactly one newline.
PAYLOAD = JUDGEMENT + "\n"

# Hard cap on the sentence length set by the contest, newline not counted.
CHARACTER_BUDGET = 200


def sanity_check(payload: str) -> None:
    """Raise if the payload is anything but a single tidy line."""
    core = payload.removesuffix("\n")
    problems = []
    if not 1 <= len(core) <= CHARACTER_BUDGET:
        problems.append("length falls outside the allowed range")
    if not core.strip():
        problems.append("nothing but whitespace")
    if "\n" in core or "\r" in core:
        problems.append("spans more than one line")
    if core != core.strip() or "  " in core:
        problems.append("ragged spacing")
    if problems:
        raise ValueError("; ".join(problems))


def emit() -> Path:
    """Validate the payload and write it out, returning the file path."""
    sanity_check(PAYLOAD)
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / "entry.txt"
    target.write_bytes(PAYLOAD.encode("utf-8"))
    return target


if __name__ == "__main__":
    emit()
