#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who the message was meant for, and the unsent
message itself, exactly as it was typed.

The entry is written byte-for-byte, with no trailing newline, so the
file holds exactly the confession and nothing else.
"""

import os

ENTRY = (
    "To: my little brother, who still thinks I moved away for the job\n"
    "I wasn't running toward anything. I was running away from being the one who had to hold us together."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
