#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes one line, 151 characters, that could have replaced an entire
pointless meeting, to /output/entry.txt. One sentence, no setup, no
explanation: the meeting existed only to answer a question a one-word
email saying yes would have settled before lunch.
Deterministic: the same line every run.
"""

import os

ENTRY = (
    "We booked a room, six calendars, and an hour of everyone's lives "
    "to answer a question that a one-word email saying yes would have "
    "settled before lunch."
)

# The sealed gate requires 1 to 200 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 200
assert "\n" not in ENTRY


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
