#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes a single status update, in the voice of a lost sock, to
/output/entry.txt. The line is a fixed constant, so every run
produces byte-identical output.
"""

import os

LINE = (
    "Update: I'm stuck in the vending machine by the chips. "
    "People press B4 hoping I'm a snack. Honestly? Flattered."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
    # not only white space.
    if not 1 <= len(LINE) <= 120:
        raise ValueError(f"entry is {len(LINE)} characters, must be 1-120")
    if not LINE.strip():
        raise ValueError("entry must not be only white space")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the status update.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    print(LINE)


if __name__ == "__main__":
    main()
