#!/usr/bin/env python3
"""Append subagent orchestration instructions when the prompt ends with -s and the tool is not Task."""

import json
import os
import sys


def main() -> None:
    # Read JSON payload from stdin
    input_data = json.load(sys.stdin)
    tool_name = input_data.get("tool_name", "")
    transcript_path = input_data.get("transcript_path", "")

    # Only append if the tool is NOT Task (to avoid recursion)
    if tool_name != "Task":
        # Check if the last user prompt ends with "-s"
        if transcript_path and ends_with_s_flag(transcript_path):
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


def ends_with_s_flag(transcript_path: str) -> bool:
    """Check if the last message in the transcript is a user message ending with '-s'."""
    try:
        with open(transcript_path, "r") as f:
            last_line = None
            for line in f:
                last_line = line.strip()

            if last_line:
                data = json.loads(last_line)
                if data.get("type") == "user" and "message" in data:
                    content = data["message"].get("content", "")
                    # Only process string content (actual user messages)
                    # Skip list content (tool results)
                    if isinstance(content, str):
                        return content.rstrip().endswith("-s")
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        pass

    return False


if __name__ == "__main__":
    main()
