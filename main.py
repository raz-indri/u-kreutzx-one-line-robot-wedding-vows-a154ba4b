#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single original robot wedding vow (at most 160 characters)
to /output/entry.txt.
"""

import os

VOW = "I promise to love you through every firmware update, every dead battery, and every factory reset \u2014 even the one that wipes my memory of this vow."


def main():
    # Self-check the contract before writing: one line, 1-160 characters.
    assert "\n" not in VOW, "vow must be a single line"
    assert 1 <= len(VOW) <= 160, f"vow is {len(VOW)} chars, must be 1-160"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
