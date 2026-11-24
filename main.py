#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — writes one excuse line.

Deterministic: no randomness, no network, no input. The excuse is a
constant; the program only validates it against the gate (1-200 chars,
UTF-8, not only whitespace, exactly one line) and writes it to entry.txt.

The joke: the homework itself printed the classic excuse as an example,
so the dog — who believes it has done nothing wrong — simply followed
the instructions on the page. Dog logic, no embarrassment, no stock
cat / paper-taste / good-boy lines.
"""

import os

EXCUSE = (
    "You wrote 'the dog ate my homework' right there on the page. "
    "I was only following the example."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars, must be 1-200"
    assert text.strip(), "excuse must not be only whitespace"
    assert "\n" not in text, "excuse must be exactly one line"
    text.encode("utf-8")  # gate requires UTF-8 text
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
