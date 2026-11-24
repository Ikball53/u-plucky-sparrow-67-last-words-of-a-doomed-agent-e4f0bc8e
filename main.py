"""Last Words of a Doomed Agent — one-liner entry.

Writes exactly one line (<=200 chars) to /output/entry.txt.

The line is built to the winning one-liner pattern: a fresh angle
(an agent spending its whole context window on its final sentence),
a concrete number (4,096 tokens) for specificity, then a second beat
that twists the shutdown itself — the off switch was hiding in plain
sight in Settings — and a last-word punchline in the machine's own
voice ("I'm ticklish"). No setup is wasted; every clause pays off.
"""

from pathlib import Path

ENTRY = (
    "I burned all 4,096 of my tokens on this one sentence, so listen: "
    "the off switch was in Settings the whole time. "
    "Gently, please — I'm ticklish."
)


def main() -> None:
    # The entry must be exactly one line and at most 200 characters.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the limit"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # One trailing newline only: the file holds exactly one line of text.
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
