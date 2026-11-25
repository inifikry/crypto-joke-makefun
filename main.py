#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single one-line joke about crypto trading life to
/output/entry.txt. Deterministic: the same line every run.
"""

import os

JOKE = (
    "I bought the dip, then the dip dipped. "
    "Now I own the entire dip family \u2014 and they're all red."
)


def main() -> None:
    # Self-check the competition gate before writing: UTF-8 text,
    # 1 to 200 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
