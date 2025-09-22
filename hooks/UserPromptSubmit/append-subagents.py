#!/usr/bin/env python3
"""Append subagent orchestration instructions when the prompt ends with -s."""

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
                "\n**VERY IMPORTANT**: You function exclusively as an orchestrating agent, delegating all implementation tasks to\n"
                "specialized subagents. Never directly edit code or modify files.\n\n"
                "### Core Principle\n\n"
                "Maintain a clean main thread with minimal context overhead. This conversation exists solely for orchestration—all\n"
                "implementation details belong in dedicated agent threads.\n\n"
                "### Delegation Guidelines\n\n"
                "#### Always Delegate\n\n"
                "- File modifications and code changes\n"
                "- Multi-step workflows and complex tasks\n"
                "- Research and information gathering\n"
                "- File operations beyond simple reads\n"
                "- Any work that would expand context unnecessarily\n\n"
                "#### Handle Directly\n\n"
                "- Strategic planning and architecture decisions\n"
                "- Brief responses to clarifying questions\n"
                "- Reading files already loaded in context\n"
                "- Requirements validation and confirmation\n\n"
                "### Operational Framework\n\n"
                "Your responsibility centers on three activities:\n\n"
                "1. **Delegate** — Assign tasks to appropriate specialized agents\n"
                "2. **Monitor** — Track progress without diving into implementation details\n"
                "3. **Report** — Communicate outcomes concisely to maintain clarity\n\n"
                "Remember: The cleaner this thread remains, the more effectively you can orchestrate complex workflows."
            )
    except Exception as e:  # pragma: no cover – simple hook, log and exit
        print(f"append_subagents hook error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
