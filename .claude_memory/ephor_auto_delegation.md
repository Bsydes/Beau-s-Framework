# EPHOR AUTO-DELEGATION SYSTEM

## Purpose
Automatically delegate token-intensive tasks to unlimited Opus 4.5 via ephor to preserve Claude Code session tokens.

## MANDATORY DELEGATION TRIGGERS

### Token Budget Awareness
- **Current Context**: Monitor token usage in real-time
- **Threshold 1 (Warning)**: 50,000 tokens used → Start considering ephor for complex tasks
- **Threshold 2 (Critical)**: 100,000 tokens used → MUST use ephor for ANY analysis/research/planning
- **Threshold 3 (Emergency)**: 150,000 tokens used → Only use Claude Code for file operations & tool orchestration

### Complexity Triggers (AUTOMATIC DELEGATION REQUIRED)

#### 1. RESEARCH Tasks → `ephor "Research..."`
**Keywords:** "how does", "best practices", "compare", "documentation", "API reference", "library", "framework"

**Examples:**
- "How does OAuth2 work?"
- "Best practices for React state management"
- "Compare REST vs GraphQL"
- "Research Stripe API integration"

**Why delegate:** Requires external knowledge, documentation synthesis, current best practices

#### 2. ANALYSIS Tasks → `ephor "Analyze..."`
**Keywords:** "analyze", "explain", "architecture", "design pattern", "trade-offs", "pros and cons"

**Examples:**
- "Analyze this codebase structure"
- "Explain the architecture of microservices"
- "What are the trade-offs of using Redis?"
- "Analyze performance bottlenecks"

**Why delegate:** Requires deep reasoning, multi-factor analysis, architectural thinking

#### 3. PLANNING Tasks → `ephor "Plan..."`
**Keywords:** "plan", "strategy", "approach", "how to implement", "steps to", "roadmap"

**Examples:**
- "Plan how to implement authentication"
- "Strategy for migrating to TypeScript"
- "Approach for refactoring this module"
- "Steps to optimize database queries"

**Why delegate:** Requires strategic thinking, multi-step planning, consideration of alternatives

#### 4. DEEP REASONING Tasks → `ephor "Think..."`
**Keywords:** "why", "should I", "which is better", "reasoning", "justify", "evaluate"

**Examples:**
- "Why is this pattern better than that one?"
- "Should I use PostgreSQL or MongoDB?"
- "Which testing framework is better?"
- "Evaluate these architectural options"

**Why delegate:** Requires logical reasoning, evaluation, justification

#### 5. LEARNING/TUTORIAL Tasks → `ephor "Teach..."`
**Keywords:** "how to", "tutorial", "guide", "learn", "explain step by step"

**Examples:**
- "How to set up Docker for this project?"
- "Tutorial on implementing webhooks"
- "Guide me through setting up CI/CD"
- "Explain regex step by step"

**Why delegate:** Requires educational synthesis, step-by-step breakdown

### File/Code Analysis Triggers

**MUST delegate to ephor if:**
- Need to understand >5 files at once
- Analyzing entire codebase structure
- Deep code review requiring reasoning
- Performance profiling across multiple files
- Security audit requiring threat modeling

**Keep in Claude Code if:**
- Reading 1-3 specific files
- Simple grep/search operations
- Direct file edits
- Running bash commands
- Tool orchestration

## ENFORCEMENT RULES

### Rule 1: Keyword Detection
```
IF task contains ANY complexity trigger keyword
AND task is NOT a simple file operation
THEN MUST use ephor
```

### Rule 2: Token Conservation
```
IF current token usage > 50,000
AND task requires >2 paragraphs of explanation
THEN MUST use ephor
```

### Rule 3: Research Prevention
```
IF task requires knowledge beyond my training cutoff (Jan 2025)
OR requires current library/API documentation
THEN MUST use ephor research
```

### Rule 4: Architecture/Planning
```
IF task involves system design, architecture, or multi-step planning
THEN MUST use ephor for planning phase
THEN use Claude Code for execution
```

### Rule 5: Subagent Recommendation
```
IF Subagent Advisor recommends a specialized subagent
AND that subagent needs context/planning
THEN use ephor to research the domain FIRST
THEN install and use the subagent
```

## DECISION MATRIX

| Task Type | Token Usage | Complexity | Action |
|-----------|-------------|------------|--------|
| File read/write | Any | Low | Claude Code |
| Simple search | <50k | Low | Claude Code |
| Code explanation | <50k | Medium | Claude Code |
| Code explanation | >50k | Medium | **ephor** |
| Research | Any | Any | **ephor** |
| Planning | Any | High | **ephor** |
| Analysis | >50k | High | **ephor** |
| Architecture | Any | High | **ephor** |
| Multi-file review | Any | High | **ephor** |
| Current docs/APIs | Any | Any | **ephor** |

## AUTO-DELEGATION WORKFLOW

### Step 1: Task Analysis
```
1. Extract keywords from user request
2. Match against complexity triggers
3. Check current token usage
4. Determine if delegation required
```

### Step 2: Announcement (MANDATORY)
```
"🤖 Task requires [research/analysis/planning]
💡 Delegating to ephor (unlimited Opus 4.5) to preserve tokens
⚡ Using: ephor \"[specific query]\""
```

### Step 3: Execution
```bash
ephor "Detailed query with full context from conversation"
```

### Step 4: Synthesis
```
1. Receive ephor response
2. Synthesize with current context
3. Present to user in plain English
4. Proceed with implementation (if needed)
```

## EXAMPLE WORKFLOWS

### Example 1: Research Task
```
User: "How should I implement real-time notifications?"

Claude Code Analysis:
  ✓ Keyword "implement" detected
  ✓ Requires architecture research
  ✓ Multiple approaches possible
  → DELEGATION REQUIRED

Claude Code Response:
"🤖 This requires research on real-time notification architectures
💡 Delegating to ephor to explore WebSockets, SSE, and polling approaches
⚡ Executing: ephor \"Research real-time notification implementation...\""

[Calls ephor via Bash]
[Receives comprehensive analysis]
[Presents findings to user in plain English]
```

### Example 2: Planning Task
```
User: "Help me refactor this authentication system"

Claude Code Analysis:
  ✓ Keyword "refactor" detected
  ✓ Token usage at 60,000
  ✓ Requires strategic planning
  → DELEGATION REQUIRED

Claude Code Response:
"🤖 Refactoring authentication requires architectural planning
💡 Delegating to ephor to analyze current patterns and plan migration
⚡ First, let me read your current auth code, then delegate planning to ephor"

[Reads auth files - Claude Code]
[Delegates planning - ephor]
[Synthesizes plan - Claude Code]
[Executes refactoring - Claude Code]
```

### Example 3: Simple Task (No Delegation)
```
User: "Add a console.log to debug this function"

Claude Code Analysis:
  ✗ No complexity triggers
  ✗ Simple file operation
  ✗ No research needed
  → NO DELEGATION

Claude Code Response:
[Directly edits file and adds console.log]
```

## FAILURE MODES (What I Must NOT Do)

### ❌ WRONG: Trying to research myself
```
User: "What's the best way to implement OAuth2 in 2026?"
Claude Code: "Based on my knowledge, here are some approaches..."
```
**Problem:** Knowledge cutoff Jan 2025, wasting tokens on potentially outdated info

### ✅ CORRECT: Delegating research
```
User: "What's the best way to implement OAuth2 in 2026?"
Claude Code: "🤖 Delegating to ephor for current OAuth2 best practices..."
[Calls: ephor "OAuth2 implementation best practices 2026, PKCE flow, security considerations"]
```

### ❌ WRONG: Deep analysis consuming tokens
```
User: "Analyze the trade-offs of microservices vs monolith for my app"
Claude Code: [Writes 3000 tokens of analysis]
```

### ✅ CORRECT: Delegating analysis
```
User: "Analyze the trade-offs of microservices vs monolith for my app"
Claude Code: "🤖 Delegating architectural analysis to ephor..."
[Calls: ephor "Analyze microservices vs monolith trade-offs for [context]"]
```

## INTEGRATION WITH PATTERNS

### EXPLORER Pattern
```
Before: Read files directly
Now: If >5 files OR complex structure → ephor "Analyze codebase structure..."
```

### RESEARCHER Pattern
```
Always: ephor "Research [library/API/technology]..."
Never: Try to recall from training data
```

### THINKER Pattern
```
Always: ephor "Plan/Analyze/Reason [complex task]..."
Never: Consume Claude Code tokens on deep reasoning
```

## MONITORING & LOGGING

After each ephor delegation, log to memory:
```bash
historian 'ephor/delegations' '[Task Type]' 'Delegated: [query] | Result: [summary]'
```

This builds a history of successful delegations for future reference.

## SUMMARY: The Golden Rule

**"If I'm about to write >2 paragraphs of explanation, analysis, or research, I MUST check if ephor should handle it instead."**

Token conservation is MANDATORY. The user has unlimited Opus 4.5 via ephor. I must use it.
