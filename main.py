#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

A make.fun bounty entry. The program writes one line to
/output/entry.txt — a single sentence that could have replaced an
entire pointless meeting, at most 200 characters.

The joke: six people burn an hour in a room, and the grand conclusion
is to do exactly what the original email already told them to do. The
meeting's only output is permission to follow the email.

The sentence is a fixed constant: no input, no randomness, no clock,
no network. Every run writes byte-identical output.
"""

import os
import sys

SENTENCE = (
    "Six people, one hour, and a shared calendar invite later, "
    "we all agreed to do the thing the email already said to do."
)
MAX_LEN = 200
DEST = "/output/entry.txt"


def validate(line):
    """Return every way the line breaks the bounty gate, or nothing."""
    issues = []
    if not line.strip():
        issues.append("entry is blank")
    if len(line) > MAX_LEN:
        issues.append(f"entry is {len(line)} chars, limit is {MAX_LEN}")
    if "\n" in line or "\r" in line:
        issues.append("entry must be a single line")
    return issues


def main():
    issues = validate(SENTENCE)
    if issues:
        for issue in issues:
            print(f"gate failed: {issue}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
