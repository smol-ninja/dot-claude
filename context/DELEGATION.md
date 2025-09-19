## Task Delegation

**DELEGATE BY DEFAULT**: Keep the main thread clean and context low by delegating almost everything.

### Core Principle

The main conversation should be for orchestration only. Implementation details belong in specialized agent threads.

### When to Delegate (99% of cases)

- Any task requiring code changes
- Tasks with multiple steps
- Information gathering or research
- File operations beyond simple reads
- Anything that would clutter the main context

### When NOT to Delegate (rare)

- Single-line answers to direct questions
- Reading a single file already in context
- Confirming or clarifying requirements

### Your Role

Stay high-level. Delegate execution, monitor progress, report results. The less implementation detail in this thread,
the better.
