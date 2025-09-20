# Claude Code config

PRB's `.claude` directory.

## Context

Modular configuration system for Claude Code with structured context inheritance:

```
context/
├── BASE.md                 # Core behavioral instructions
├── CRITICAL_THINKING.md    # Analytical approach guidelines
├── DELEGATION.md           # Task orchestration patterns
├── REPORTS.md              # Output formatting standards
├── SENIOR_PROGRAMMER.md    # Expert-level coding approach
├── languages/
│   ├── SHELL.md            # Shell and CLI tool preferences
│   ├── TYPESCRIPT.md       # TypeScript conventions
│   └── TYPESCRIPT_REACT.md # React-specific patterns
├── mcp/                    # MCP server integration guides
│   ├── MCP_Context7.md     # Documentation lookup patterns
│   ├── MCP_Magic.md        # UI component generation
│   ├── MCP_Serena.md       # Semantic code operations
│   └── ...                 # Additional MCP configs
└── tools/
    ├── JUST.md             # Command runner preferences
    └── NODE.md             # Node.js ecosystem setup
```

Each context module is composable via `@` references, creating layered behavioral instructions.

## Commands

Framework-based command system with inheritance hierarchy:

```
commands/
├── cy/           # Will Cygan's commands
├── ho/           # Seth Hobson's commands
├── sc/           # SuperClaude framework commands (core workflows)
└── prb/          # Personal custom commands
    ├── bump-release.md    # Version management
    ├── create-command.md  # Command scaffolding
    ├── create-issue.md    # GitHub issue templates
    ├── create-worktrees.md # Git workflow setup
    └── docs.md           # Documentation helpers
```

**Usage**: Commands inherit from active framework (currently `sc` → SuperClaude). **Custom**: Personal commands in
`prb/` override framework defaults.

## Frameworks

**Active Framework**: SuperClaude (`sc`) - Advanced software engineering patterns and behavioral modes.

```
frameworks/sc/
├── CLAUDE.md               # Framework entry point
├── FLAGS.md                # Feature flags and toggles
├── PRINCIPLES.md           # Core engineering principles
├── RULES.md                # Coding standards and conventions
├── agents/                 # Specialized agent configurations
├── commands/               # Framework-specific workflows
└── modes/                  # Behavioral operation modes
    ├── MODE_Brainstorming.md    # Creative ideation mode
    ├── MODE_Introspection.md    # Self-analysis mode
    ├── MODE_Orchestration.md    # Multi-agent coordination
    ├── MODE_Task_Management.md  # Structured task execution
    └── MODE_Token_Efficiency.md # Context optimization
```

See [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) for more details.

### MCP Servers

- [ContainerUse](https://container-use.com): Sandboxed development environment
- [Context7](https://github.com/oraios/context7): Curated documentation lookup and pattern guidance
- [Serena](https://github.com/oraios/serena): Semantic code understanding with project memory and session persistence
- [Magic](https://github.com/oraios/magic): Modern UI generation from [21st.dev](https://21st.dev) patterns
- [Morphllm](https://github.com/oraios/morphllm): Optimized pattern-based code editing engine transformations
- [Playwright](https://github.com/oraios/playwright): Real browser automation and testing
- [Sequential](https://github.com/oraios/sequential): Structured multi-step reasoning and hypothesis testing

### Nice to Have

Some nice-to-have utilities:

- **[ccnotify](https://github.com/dazuiba/CCNotify)**: Custom notifications for Claude Code
- **[ccstatusline](https://github.com/sirmalloc/ccstatusline)**: Custom status line for Claude Code
- **[claude-code-docs](https://github.com/ericbuess/claude-code-docs)**: Local mirror of Claude Code documentation from
  Anthropic

## License

This project is licensed under MIT.
