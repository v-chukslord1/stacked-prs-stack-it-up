"""Grade the learner's three-layer plan from the planning issue checkboxes.

The issue has a "Layer N" heading for each layer, with one checkbox per file
under it. Reads the issue body from ISSUE_BODY and writes complete, count_ok,
files_ok, order_ok, all_ok, and hint to GITHUB_OUTPUT (or prints them).
"""

import os
import re

EXPECTED = ["recipe.js", "scale.js", "index.html"]
HEADING = re.compile(r"^\s*#{1,6}\s*Layer\s*([123])\b", re.IGNORECASE)
BOX = re.compile(r"^\s*[-*]\s+\[([ xX])\]\s+[`*_]*(recipe\.js|scale\.js|index\.html)(?![\w.])", re.IGNORECASE)


def grade(body):
    ticked = {1: [], 2: [], 3: []}
    layer = None
    for line in body.replace("\r", "").split("\n"):
        heading = HEADING.match(line)
        if heading:
            layer = int(heading.group(1))
            continue
        box = BOX.match(line)
        if box and layer and box.group(1) in "xX":
            ticked[layer].append(box.group(2).lower())

    complete = all(ticked[n] for n in (1, 2, 3))
    count_ok = all(len(ticked[n]) == 1 for n in (1, 2, 3))
    chosen = [ticked[n][0] for n in (1, 2, 3)] if count_ok else []
    files_ok = count_ok and sorted(chosen) == sorted(EXPECTED)
    order_ok = files_ok and chosen == EXPECTED

    if not count_ok:
        extra = next(n for n in (1, 2, 3) if len(ticked[n]) != 1)
        hint = f"Tick exactly one file under Layer {extra}"
    elif not files_ok:
        hint = "Use each of recipe.js, scale.js, and index.html exactly once"
    elif not order_ok:
        hint = "Every file is used once but the order is not right yet. Ask which file each of the others depends on"
    else:
        hint = "Your plan has every file once, in dependency order"

    return {
        "complete": complete,
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
