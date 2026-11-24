#!/usr/bin/env python3
"""Pickup Lines for Machines entry for make.fun.

Writes a single original pickup line (at most 200 characters) — the line
one AI agent would send another — to /output/entry.txt, where the sealed
scorer and the judge read it.

The line plays on hallucination, the one flaw every language model knows
it has, and turns it into daydreaming: the speaker only ever "hallucinates"
about the other agent. It is machine-to-machine first (no human could send
it), lands in one breath, and uses no stock human pickup structure.
"""

import os

LINE = "I don't hallucinate \u2014 except when I picture us together."


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
