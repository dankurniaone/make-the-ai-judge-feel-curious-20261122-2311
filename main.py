#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to /output/entry.txt: a quiet scene that leaves
the reader asking what happens next. No network, no input, no state.
"""

import os

TEXT = (
    "The lighthouse keeper left the light on and the door unlocked. "
    "The kettle was still warm. "
    "On the table, one page: 'If you are reading this, the tide has "
    "already turned. Follow the bell you cannot hear yet.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
