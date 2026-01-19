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

**Detection Algorithm:**
```
1. Normalize input: lowercase, tokenize by word boundaries
2. Check for negation context (words within 3 tokens)
3. Match keywords with variants (lemmatization)
4. If keyword found WITHOUT negation → trigger
5. If multiple triggers found → activate regardless of order
```

**Negation Words (Suppress Triggering):**
- "don't", "dont", "do not"
- "avoid", "avoiding", "without"
- "not", "no", "never"
- "skip", "skipping", "exclude"

**Negation Context Window:** 3 words before and after keyword

**Example Negation Detection:**
- "don't orchestrate this" → "don't" within 3 words of "orchestrate" → SUPPRESS
- "avoid multi-step workflow" → "avoid" within 3 words of "multi-step" → SUPPRESS
- "not complex at all" → "not" within 3 words of "complex" → SUPPRESS

**Order Independence:**
- Keywords can appear in any order
- "analyze and implement" = "implement and analyze" (BOTH trigger)
- Check: Does request contain ANY triggers? (not sequence-dependent)

**Word Boundary Matching:**
- "coordinate" matches "coordinate" (standalone word)
- "coordinate" DOES NOT match "uncoordinated" (substring)
- Use regex word boundaries: `\bkeyword\b`

---

#### 1. RESEARCH Tasks → `ephor "Research..."`

**Primary Keywords (with word boundaries):**
- "research", "researching"
- "how does", "how do"
- "best practices", "best practice"
- "compare", "comparing", "comparison"
- "documentation", "docs"
- "API reference", "reference"
- "library", "libraries", "framework", "frameworks"

**Natural Variants:**
- "what's the best way" → treated as "best practices"
- "look up documentation" → treated as "research"

**Examples:**
- "How does OAuth2 work?" → TRIGGER
- "Don't research this, just implement" → SUPPRESS
- "Best practices for React" → TRIGGER

---

#### 2. ANALYSIS Tasks → `ephor "Analyze..."`

**Primary Keywords:**
- "analyze", "analyzing", "analysis"
- "explain", "explaining", "explanation"
- "architecture", "architectural"
- "design pattern", "patterns"
- "trade-offs", "tradeoffs", "trade offs"
- "pros and cons", "advantages and disadvantages"

**Natural Variants:**
- "what are the benefits vs downsides" → treated as "pros and cons"
- "examine the structure" → treated as "analyze"

**Examples:**
- "Analyze this codebase structure" → TRIGGER
- "Without analysis, just fix it" → SUPPRESS
- "Explain the architecture" → TRIGGER

---

#### 3. PLANNING Tasks → `ephor "Plan..."`

**Primary Keywords:**
- "plan", "planning"
- "strategy", "strategic"
- "approach", "methodology"
- "how to implement", "how should I implement"
- "steps to", "step-by-step"
- "roadmap"

**Natural Variants:**
- "what's the approach for" → treated as "approach"
- "outline the steps" → treated as "steps to"

**Examples:**
- "Plan how to implement authentication" → TRIGGER
- "Skip planning, just build it" → SUPPRESS
- "Strategy for migrating to TypeScript" → TRIGGER

---

#### 4. DEEP REASONING Tasks → `ephor "Think..."`

**Primary Keywords:**
- "why", "reasoning", "rationale"
- "should I", "should we"
- "which is better", "what's better"
- "justify", "justification"
- "evaluate", "evaluating", "evaluation"

**Examples:**
- "Why is this pattern better?" → TRIGGER
- "Don't evaluate options, pick one" → SUPPRESS
- "Which testing framework is better?" → TRIGGER

---

#### 5. LEARNING/TUTORIAL Tasks → `ephor "Teach..."`

**Primary Keywords:**
- "how to", "how do I", "how can I"
- "tutorial", "guide", "walkthrough"
- "learn", "learning", "teach"
- "explain step by step", "step-by-step"

**Examples:**
- "How to set up Docker?" → TRIGGER
- "No tutorial needed, show me code" → SUPPRESS
- "Guide me through setting up CI/CD" → TRIGGER

---

#### 6. ORCHESTRATION Tasks → `ephor activate`

**Primary Keywords:**
- "orchestrate", "orchestrating", "orchestration"
- "coordinate", "coordinating", "coordination"
- "multi-step", "multiple steps", "many steps"
- "break down", "breakdown"
- "full project", "complete project", "entire project", "whole project"
- "end-to-end", "end to end"

**Natural Variants:**
- "do this in several steps" → treated as "multi-step"
- "across the entire system" → treated as "full project"

**Examples:**
- "Orchestrate the deployment" → TRIGGER
- "This is simple orchestration internally" → SUPPRESS (context: describing, not requesting)
- "Coordinate between services" → TRIGGER
- "The uncoordinated system" → NO TRIGGER (substring, not word boundary)

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
