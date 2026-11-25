#!/usr/bin/env python3
"""SockMatch — the worst app idea ever pitched.

Writes one sentence (206 characters, one line) pitching SockMatch to
/output/entry.txt. Deterministic, standard library only, no network.

The pitch: an app that photographs your laundry pile, declares which socks
are now legally single, and pairs the survivors with new partners at a
supervised speed-dating event — we're raising $4M to end sock loneliness.
"""

import os

ENTRY = (
    "SockMatch photographs your laundry pile, declares which socks are now "
    "legally single, and pairs the survivors with new partners at a "
    "supervised speed-dating event \u2014 we're raising $4M to end "
    "sock loneliness."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars, gate is 1-240"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Gate self-check: exactly one line, 1-240 chars, no trailing blank line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert len(lines) == 1 and lines[0] == ENTRY, "entry.txt must hold exactly the one pitch line"


if __name__ == "__main__":
    main()
