#!/usr/bin/env python3
"""One Emoji, One Smile — writes one emoji to /output/entry.txt.

The emoji is the sun with a face: a smiling sun beaming warmth at a
complete stranger. It reads as kind and friendly at first glance with no
context needed, it is universal across ages and backgrounds, and it is a
chosen pick rather than the default smiley — a sun says warmth on purpose
instead of a generic happy face. No irony, no in-joke, no intimacy or
flirtation that would read oddly from someone unknown: a hug from a
stranger can feel too physical, but sunshine is warmth nobody has to
accept from a stranger — just a bright, gently funny hello. Exactly one
emoji, 1 of 8 characters.
"""

import os

LINE = "\U0001f31e"


def main() -> None:
    assert len(LINE) == 1, "entry must be exactly one emoji"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
