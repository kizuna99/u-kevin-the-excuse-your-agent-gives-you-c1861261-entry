# SPDX-License-Identifier: MIT
"""The Excuse Your Agent Gives You - entry program.

Writes exactly one line to /output/entry.txt: an excuse an AI agent
gives its human for a bug it shipped. The line turns on temperature
zero: at temperature zero a model is deterministic, so the agent's
apology is also a guarantee that the identical bug will ship again.

The output is byte-exact: 129 characters, 131 UTF-8 bytes, no
trailing newline, well inside the gate of 1 to 200 characters.
"""

import os
from pathlib import Path

EXCUSE = (
    "Sorry \u2014 I coded at temperature zero, so the bug is fully "
    "reproducible: ask me again and I'll ship the exact same one, "
    "guaranteed."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(EXCUSE.encode("utf-8"))


if __name__ == "__main__":
    main()
