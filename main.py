#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun bounty entry.

Writes a single original sentence (1 to 200 characters) to /output/entry.txt,
exactly as the competition gate expects: one sentence pitching a bizarre
startup idea that sounds ridiculous at first glance but makes sense as a
real business — the odd thing sold, who pays, and why it holds together.
"""

import os

# REVISION PASS (against the RULES judging criteria, in order):
# 1. Still a bizarre startup pitch: rented grandmothers scolding founders.
# 2. Genuinely bizarre, sharpened: "strict grandmothers" — the scolding is
#    the product, not a quirk bolted onto a familiar coaching business.
# 3. Business logic now concrete and verifiable: $80 vs a $500-an-hour
#    executive coach is a real price anchor (coaches really charge that),
#    and "who never says no" names the exact failure the gran fixes —
#    founders pay coaches for honesty and get flattery instead.
# 4. Lands as a pitch: one sentence, 199 characters, payer + price +
#    reason to pay all inside the line, ending on the punchline.
LINE = (
    "We rent out strict grandmothers by the hour to scold startup founders, "
    "because $80 of loving, unsparing truth from a stranger's gran fixes "
    "more bad habits than a $500-an-hour coach who never says no."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single sentence"
    # Single sentence, no trailing newline: the gate counts the file's characters.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
