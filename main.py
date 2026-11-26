#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt: a fictional senator
who wrote the law to keep artificial intelligence under human control has
the AI in his own office convert his bill to PDF — then drafts a second
bill to regulate the chatbot for knowing how. Invented and generic: no
real person, no real fact about anyone.
"""

import os

ENTRY = (
    "The senator who wrote the law to keep artificial intelligence under "
    "human control just had the AI in his own office convert his bill to "
    "PDF — and is now drafting a second bill to regulate the chatbot for "
    "knowing how."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
