#!/usr/bin/env python3
"""Write a one-line patch note for a bug in real life.

The note is a single line of 126 characters, in the terse register of a
real release note: the brain keeps replaying one embarrassing moment
from 2009 every night at 3 AM, and ships with no skip button.
"""
import os

PATCH_NOTE = (
    "v2.4.1: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2009 every night at 3 AM, with no skip button."
)

MAX_CHARS = 160


def validate(text: str) -> str:
    """Return the note unchanged, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"patch note must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("patch note must be a single line")
    if not text:
        raise SystemExit("patch note must not be only whitespace")
    if any(ord(ch) < 0x20 and ch != "\t" for ch in text):
        raise SystemExit("patch note must not contain control characters")
    if not text.startswith("v") or ": fixed a bug where " not in text:
        raise SystemExit("patch note must read as a versioned release note")
    return text


def main() -> None:
    text = validate(PATCH_NOTE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
