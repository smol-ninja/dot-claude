#!/usr/bin/env python3
"""Append subagent orchestration instructions when the prompt ends with -s and the tool is not Task."""

import json
import sys
from pathlib import Path


def main() -> None:
    """Main entry point for the hook."""
    input_data = json.load(sys.stdin)

    # Early return if tool is Task (avoid recursion)
    if input_data.get("tool_name") == "Task":
        return

    transcript_path = input_data.get("transcript_path", "")
    if not transcript_path or not ends_with_s_flag(transcript_path):
        return

    # Append orchestrator content
    append_orchestrator_content()


def append_orchestrator_content() -> None:
    """Read and print the ORCHESTRATOR.md content."""
    script_dir = Path(__file__).parent
    orchestrator_path = script_dir / ".." / ".." / "context" / "ORCHESTRATOR.md"

    try:
        content = orchestrator_path.read_text().rstrip()
        print(f"\n{content}")
    except FileNotFoundError:
        # Silently fail if orchestrator file doesn't exist
        pass


def ends_with_s_flag(transcript_path: str) -> bool:
    """Check if the last message in the transcript is a user message ending with '-s'."""
    try:
        last_line = read_last_line(transcript_path)
        if not last_line:
            return False

        line_str = last_line.decode("utf-8").strip()
        if not line_str:
            return False

        data = json.loads(line_str)

        # Not a user message
        if data.get("type") != "user" or "message" not in data:
            return False

        content = data["message"].get("content", "")

        # Skip list content (tool results), only process strings
        if not isinstance(content, str):
            return False

        return content.rstrip().endswith("-s")

    except (
        FileNotFoundError,
        json.JSONDecodeError,
        KeyError,
        UnicodeDecodeError,
        OSError,
    ):
        return False


def read_last_line(file_path: str) -> bytes:
    """Read the last line of a file efficiently."""
    with open(file_path, "rb") as f:
        # Check if file is empty
        f.seek(0, 2)  # Seek to end
        if f.tell() == 0:
            return b""

        # Read backwards to find last line
        f.seek(-1, 2)  # Start from last byte
        last_line = b""

        while f.tell() > 0:
            char = f.read(1)
            if char == b"\n":
                break
            last_line = char + last_line
            f.seek(-2, 1)  # Move back 2: 1 for char read, 1 more to go back
        else:
            # Reached beginning of file, read the remaining character
            f.seek(0)
            char = f.read(1)
            last_line = char + last_line

        return last_line


if __name__ == "__main__":
    main()
