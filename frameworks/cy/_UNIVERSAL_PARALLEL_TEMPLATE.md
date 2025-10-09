---
allowed-tools: Task, Read, Bash(fd:*), Bash(rg:*), Bash(jq:*), Bash(gdate:*)
description: Universal high-performance parallel analysis template with 2-3 sub-agents
---

# Universal Sub-Agent Optimization Template

## Session Management Pattern

```yaml
## Context
- Session ID: !`gdate +%s%N 2>/dev/null || date +%s%N 2>/dev/null || echo "$(date +%s)$(jot -r 1 100000 999999 2>/dev/null || shuf -i 100000-999999 -n 1 2>/dev/null || echo $RANDOM$RANDOM)"`
- Current directory: !`pwd`
- Project structure: !`fd . -t d -d 2 | head -10 || echo "Limited directory access"`
```

## Performance-First Architecture

### STEP 1: Session Initialization

```yaml
TRY:
  Initialize analysis session with unique session ID
  Create state directory: /tmp/analysis-$SESSION_ID/
  Set up parallel agent coordination
CATCH:
  Fallback to basic analysis without state management
```

### STEP 2: **IMMEDIATE PARALLEL DEPLOYMENT**

```yaml
**DEPLOY 2-3 AGENTS SIMULTANEOUSLY** - NO SEQUENTIAL PROCESSING:

1. **Agent 1: [Primary Analysis]**
   - Focus: [Core responsibility - e.g., architecture and patterns]
   - Tools: [Relevant tools]
   - Output: [Expected deliverable]

2. **Agent 2: [Secondary Analysis]**
   - Focus: [Complementary responsibility - e.g., quality and security]
   - Tools: [Relevant tools]
   - Output: [Expected deliverable]

3. **Agent 3: [Supporting Analysis]** (Optional)
   - Focus: [Additional responsibility - e.g., testing and documentation]
   - Tools: [Relevant tools]
   - Output: [Expected deliverable]

**CRITICAL**: Launch agents simultaneously for efficient parallel processing.
**Expected speedup**: 2-3x faster than sequential analysis.
```

### STEP 3: Result Synthesis

```yaml
WAIT for ALL agents to complete
AGGREGATE findings from all parallel streams
SYNTHESIZE comprehensive analysis
GENERATE structured output
```

## Universal Performance Patterns

### 1. Eliminate Conditional Parallelization

- **NEVER** use `IF complex THEN parallel ELSE sequential`
- **ALWAYS** default to 2-3 parallel agents
- **REMOVE** size-based thresholds and complexity conditions

### 2. Technology-Agnostic Parallelization

- **LAUNCH** 2-3 agents to cover key analysis areas simultaneously
- **AVOID** sequential CASE statements for languages/frameworks
- **USE** parallel technology detection instead of sequential scanning

### 3. Session State Management

```bash
# Unique session files prevent conflicts
SESSION_ID=$(gdate +%s%N 2>/dev/null || date +%s%N 2>/dev/null || echo "$(date +%s)$(jot -r 1 100000 999999 2>/dev/null || shuf -i 100000-999999 -n 1 2>/dev/null || echo $RANDOM$RANDOM)")
STATE_FILE="/tmp/analysis-state-$SESSION_ID.json"
RESULTS_DIR="/tmp/analysis-results-$SESSION_ID/"
```

### 4. Error Handling Framework

```yaml
TRY:
  Deploy all parallel agents
  Execute comprehensive analysis
  Aggregate results
CATCH (agent_failure):
  Continue with available agent results
  Log failed agent details
  Provide partial analysis
FINALLY:
  Clean up session state files
  Report completion status
```

### 5. Token Optimization

- **Structured output formats** for efficient synthesis
- **Focused agent contexts** (2000-4000 tokens per agent)
- **Parallel processing** reduces total token usage by 20-40%
- **State serialization** minimizes context window pressure

## Command-Specific Customization

### Analysis Commands

```yaml
Agent Focus Areas:
  - Technology stack detection
  - Code quality assessment
  - Security vulnerability scanning
  - Performance bottleneck identification
  - Dependency analysis
  - Testing coverage evaluation
  - Documentation completeness
  - Architecture pattern recognition
```

### Generation Commands

```yaml
Agent Focus Areas:
  - Template generation
  - Code scaffolding
  - Documentation creation
  - Test case generation
  - Configuration setup
  - Integration patterns
  - Best practices application
  - Quality validation
```

### Status Commands

```yaml
Agent Focus Areas:
  - Build health checking
  - Test execution status
  - Code quality metrics
  - Dependency health
  - Security posture
  - Performance metrics
  - Documentation status
  - Configuration validation
```

## Expected Performance Metrics

### Performance Gains by Command Type

- **Complex Analysis**: 2-3x speedup
- **Multi-Technology Projects**: 3x speedup
- **Documentation Generation**: 2-3x speedup
- **Status Checking**: 2-3x speedup
- **Security Audits**: 2-3x speedup

### Quality Improvements

- **Comprehensive Coverage**: No aspect missed due to time constraints
- **Consistent Quality**: Standardized analysis patterns
- **Better Error Handling**: Graceful degradation with partial results
- **Improved Reliability**: Session isolation prevents conflicts

## Migration Checklist

### From Sequential to Parallel

- [ ] Remove conditional parallelization logic
- [ ] Eliminate size/complexity thresholds
- [ ] Replace sequential technology detection
- [ ] Add session state management
- [ ] Implement error handling framework
- [ ] Add performance measurement
- [ ] Update documentation with expected speedup

### Validation Steps

- [ ] Test with small, medium, and large projects
- [ ] Verify functionality parity with original
- [ ] Measure actual vs expected performance gains
- [ ] Validate error handling and recovery
- [ ] Check cross-platform compatibility

## Integration Notes

### Modern Tool Requirements

- **MANDATORY**: Use `rg`, `fd`, `bat`, `eza`, `jq` over legacy tools
- **FORBIDDEN**: `grep`, `find`, `cat`, `ls` for any analysis operations
- **CROSS-PLATFORM**: Include fallbacks for different OS/tool versions

### Claude Code Integration

- **Task Tool**: Primary mechanism for sub-agent deployment
- **Session Management**: Unique IDs prevent conflicts between parallel sessions
- **State Persistence**: Enable resumability and debugging
- **Error Recovery**: Graceful handling of partial failures

This template transforms any sequential command into a high-performance parallel analysis engine, delivering the 2-3x performance improvements expected from modern sub-agent architecture.
