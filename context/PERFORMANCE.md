## Performance

**CRITICAL: Use sub-agents carefully**

### When to Use Sub-Agents (5x speedup)

- **Codebase exploration**: Multi-file analysis
- **Research tasks**: Information gathering
- **Code quality checks**: Multiple analyzers
- **Migration planning**: Impact analysis across modules
- **Bug investigation**: Pattern searches across files

### Task Tool Pattern

```
[Launch 2-3 agents simultaneously in single response]
Task 1: "Specific focused analysis task"
Task 2: "Independent parallel task"
Task 3: "Another concurrent analysis"
Main agent synthesizes all results
```

### Never Use Task Tool For

- Single file reads (use Read directly)
- Sequential dependencies
- Direct file modifications
- Trivial single operations

### Performance Mindset

Performance Mindset

- **Default to parallel execution** (2-3 agents)
- **Don't abuse parallel agents** (don't go overboard; we don't need 8 agents at once — keep it simple)
- **Never analyze files sequentially** when parallelizable
- **Launch agents immediately** in first response
- **Synthesize results** after parallel completion

Remember: Small steps, tests first, green builds, atomic commits. This is the path to maintainable, reliable software.
