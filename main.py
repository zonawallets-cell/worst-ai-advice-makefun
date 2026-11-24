#!/usr/bin/env python3
"""Worst AI Advice entry (make.fun, program/v1).

Writes one line of the worst possible advice an AI could give to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR). Pure stdlib only (os).
The line is a single text of at most 140 characters, no line breaks,
byte-identical on every run.
"""

import os

ADVICE = "Quick tip: delete your backups to free up disk space \u2014 a tidy drive runs faster, and you can always recreate the data from memory."


def validate(text):
    """Enforce the gate; return a list of problems (empty = valid).

    Gate: UTF-8, 1-140 chars, no line breaks, not only whitespace.
    """
    problems = []
    if not isinstance(text, str):
        return ["not a string"]
    if not 1 <= len(text) <= 140:
        problems.append("length %d outside 1-140" % len(text))
    if not text.strip():
        problems.append("only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("contains a line break")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("not UTF-8 encodable: %s" % exc)
    return problems


def main():
    problems = validate(ADVICE)
    if problems:
        raise SystemExit("advice failed validation: " + "; ".join(problems))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ADVICE)
    print("wrote %d chars to %s" % (len(ADVICE), path))


if __name__ == "__main__":
    main()
