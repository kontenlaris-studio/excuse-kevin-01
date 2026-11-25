#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — one line, printed to /output/entry.txt."""
import os

LINE = (
    'My agent\'s excuse for being late: "The map said turn left." '
    "We were on a video call. It turned left anyway and has been "
    "in a breakout room ever since."
)

# Bounty contract: a single line under 200 characters.
assert len(LINE) < 200, len(LINE)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
