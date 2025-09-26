#!/usr/bin/env python3
"""Append subagent orchestration instructions when the prompt ends with -s."""

import json
import os
import sys


def main() -> None:
    try:
        # Read JSON payload from stdin
        input_data = json.load(sys.stdin)
        prompt: str = input_data.get("prompt", "")

        # Only append if the prompt ends with the -s flag
        if prompt.rstrip().endswith("-s"):
            # Get the path to ORCHESTRATOR.md relative to this script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            orchestrator_path = os.path.join(
                script_dir, "..", "..", "context", "ORCHESTRATOR.md"
            )

            # Read the content from ORCHESTRATOR.md
            with open(orchestrator_path, "r") as f:
                orchestrator_content = f.read().rstrip()

            # Print the content with a leading newline for separation
            print(f"\n{orchestrator_content}")
    except Exception as e:  # pragma: no cover – simple hook, log and exit
        print(f"append_subagents hook error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
