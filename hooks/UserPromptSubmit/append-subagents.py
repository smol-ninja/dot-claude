#!/usr/bin/env python3
"""Append a subagent instruction when the prompt ends with -s."""

import json
import sys


def main() -> None:
    try:
        # Read JSON payload from stdin
        input_data = json.load(sys.stdin)
        prompt: str = input_data.get("prompt", "")

        # Only append if the prompt ends with the -s flag
        if prompt.rstrip().endswith("-s"):
            print(
                "\nSpawn subagents to implement this task. "
                "Consider parallelizing the implementation and use specialized agents, if applicable."
            )
    except Exception as e:  # pragma: no cover – simple hook, log and exit
        print(f"append_subagents hook error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
