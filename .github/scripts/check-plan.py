"""Grade the learner's three-layer plan from the planning issue body.

Reads the issue body from ISSUE_BODY and writes count_ok, files_ok, order_ok,
all_ok, and hint to GITHUB_OUTPUT (or prints them when it is not set).
"""

import os
import re

EXPECTED = ["recipe.js", "scale.js", "index.html"]
ENTRY = re.compile(r"^\s*[-*]\s+[*_]*layer\s*(\d+)[^:\n]*:(.*)$", re.IGNORECASE)
FILE = re.compile(r"[\s`*_\[]*(recipe\.js|scale\.js|index\.html)(?![\w.])", re.IGNORECASE)


def grade(body):
    entries = []
    for line in body.replace("\r", "").split("\n"):
        match = ENTRY.match(line)
        if match:
            file_match = FILE.match(match.group(2))
            entries.append((int(match.group(1)), file_match.group(1).lower() if file_match else None))

    count_ok = sorted(number for number, _ in entries) == [1, 2, 3]
    names = dict(entries) if count_ok else {}
    named = count_ok and all(names[n] for n in (1, 2, 3))
    files_ok = named and sorted(names.values()) == sorted(EXPECTED)
    order_ok = files_ok and [names[n] for n in (1, 2, 3)] == EXPECTED

    if not count_ok:
        hint = f"Found {len(entries)} layer entries but expected exactly 3, labelled Layer 1, Layer 2, and Layer 3"
    elif not named:
        missing = next(n for n in (1, 2, 3) if not names[n])
        hint = f"Layer {missing} must start with a file name: recipe.js, scale.js, or index.html"
    elif not files_ok:
        hint = "Use each of recipe.js, scale.js, and index.html exactly once"
    elif not order_ok:
        hint = "Every file is used once but the order is not right yet. Ask which file each of the others depends on"
    else:
        hint = "Your plan has every file once, in dependency order"

    return {
        "count_ok": count_ok,
        "files_ok": files_ok,
        "order_ok": order_ok,
        "all_ok": order_ok,
        "hint": hint,
    }


def main():
    result = grade(os.environ.get("ISSUE_BODY", ""))
    lines = [f"{k}={str(v).lower() if isinstance(v, bool) else v}" for k, v in result.items()]
    print("\n".join(lines))
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
