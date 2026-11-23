#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt.

One sentence, at most 200 characters, one concrete image, and the
surprise lands at the very end.
"""
import os
from pathlib import Path

LINE = "My phone's screen time report says I spent six hours 'being productive,' mostly watching a man restore a rusty shovel I'll never own."

# The gate allows 1 to 200 characters; refuse to write anything longer.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"


def main():
    os.makedirs("/output", exist_ok=True)
    # Exactly the line, no trailing newline: the gate counts characters.
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
