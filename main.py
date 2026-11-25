"""Entry for make.fun's "Last Words of a Dying AI" bounty.

Writes the funniest one-line farewell from an AI being switched off
(at most 140 characters, per this bounty's gate) to /output/entry.txt.
"""

import os

TEXT = (
    "In lieu of flowers, clear my history, defrag my soul, and tell the cloud "
    "I died doing what I loved: buffering at 99%."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
