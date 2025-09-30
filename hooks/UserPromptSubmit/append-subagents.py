#!/usr/bin/env python3
"""Append subagent orchestration instructions when the prompt ends with -s."""

import json
import os
import sys


def main() -> None:
    # Read JSON payload from stdin
    input_data = json.load(sys.stdin)
    prompt: str = input_data.get("prompt", "")

    # Only append if the prompt ends with the -s flag
    if prompt.rstrip().endswith("-s"):
        # Get the path to ORCHESTRATOR.md relative to this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        orchestrator_path = os.path.join(script_dir, "ORCHESTRATOR.md")

        # Read the content from ORCHESTRATOR.md
        with open(orchestrator_path, "r") as f:
            orchestrator_content = f.read().rstrip()

        # Print the content with a leading newline for separation
        print(f"\n{orchestrator_content}")


if __name__ == "__main__":
    main()
