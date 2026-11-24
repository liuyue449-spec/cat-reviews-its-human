"""Cat Reviews Its Human — make.fun entry.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt (or to $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set, for local checks).
"""

import os

REVIEW = (
    "One star. He bought me a $60 bed. I sleep in the box it came in. "
    "He spent $60 learning nothing."
)


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
