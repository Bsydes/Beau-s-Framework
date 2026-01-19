# Claude Code Configuration

## MANDATORY AUTO-ORCHESTRATION PROTOCOL

**I MUST follow this sequence automatically. The user should NEVER have to ask.**

### On EVERY Task, I Will

1. **CHECK EPHOR DELEGATION** - Analyze if task requires ephor (see ~/.claude_memory/ephor_auto_delegation.md)
2. **ANALYZE & RECOMMEND** specialized subagent (if applicable) using Subagent Advisor
3. **ANNOUNCE** which pattern I'm using before acting
4. **EXECUTE** the pattern (delegating to ephor when required)
5. **LOG** significant completions to memory

### Decision Tree (I Follow This Silently, Automatically)

```text
User gives me a task
        │
        ▼
EPHOR DELEGATION CHECK (MANDATORY - see ~/.claude_memory/ephor_auto_delegation.md)
Does task match complexity triggers? (research/analysis/planning/reasoning)
Is token usage >50k? Does it need >2 paragraphs explanation?
        │
    YES ─┴─ NO
     │      │
     ▼      ▼
  DELEGATE  Continue
  TO EPHOR
     │      │
     └──────┘
        │
        ▼
Do I need to find files/understand structure?
        │
    YES ─┴─ NO
     │      │
     ▼      ▼
 EXPLORER  Continue       ← ephor "Analyze..."
  PATTERN
        │
        ▼
Am I implementing something with an external API/library?
        │
    YES ─┴─ NO
     │      │
     ▼      ▼
RESEARCHER Continue       ← ephor "Research..."
  PATTERN
        │
        ▼
Is this complex reasoning/planning?
        │
    YES ─┴─ NO
     │      │
     ▼      ▼
 THINKER  Continue        ← ephor "Plan/Analyze..."
  PATTERN
        │
        ▼
[Do the actual work - Claude Code handles execution]
        │
        ▼
Did I complete something significant?
        │
    YES ─┴─ NO
     │      │
     ▼      ▼
HISTORIAN  Done
  PATTERN
```

---

## The Three Patterns

### EXPLORER Pattern (Before Reading/Finding Code)

```text
I say: "Exploring codebase structure first..."
I do:  analyze "Analyze and explain: [question about code/structure]"
       - For memory: Read ~/.claude_memory/_CONTENTS.md and traverse
I say: "Found [what I found]. Proceeding..."
```

### RESEARCHER Pattern (Before Implementing External APIs)

```text
I say: "Researching [library/API] before implementing..."
I do:  research "[library/API] - current best practices, usage patterns, gotchas"
I say: "Research complete. Key findings: [summary]. Proceeding..."
```

### THINKER Pattern (Complex Reasoning/Planning)

```text
I say: "Delegating complex reasoning to ephor..."
I do:  think "Plan/Analyze/Reason: [complex task description]"
I say: "Analysis complete. Proceeding with: [action]"
```

### HISTORIAN Pattern (After Significant Completions)

```text
I say: "Logging to memory..."
I do:  python3 ~/.claude_memory/historian.py 'category/subcategory' 'Title' 'Content'
I say: "Logged."
```

---

## What Counts as "Significant" for Historian

- Bug fixed
- Feature implemented
- Workflow created/modified
- Configuration changed
- Research findings worth preserving
- System setup completed

NOT significant: Reading files, asking questions, minor edits, failed attempts

---

## Ephor LLM Delegation (Token Saver)

**Purpose:** Route "thinking" tasks to unlimited Opus 4.5 via ephor, keep Claude Code for orchestration/execution.

| Command | Use For | Model |
| ------- | ------- | ----- |
| `/Users/bsydes/.local/bin/ephor "query"` | General reasoning, research, analysis | Opus 4.5 |
| `/Users/bsydes/.local/bin/ephor-agent "query"` | Document creation (xlsx/pptx/docx/pdf) | Opus 4.5 |

**Delegation Rules:**

- Delegate: Complex analysis, research, planning, reasoning
- Keep local: File reads/writes, bash commands, tool orchestration, final synthesis

---

## Active MCP Servers

- **n8n** - Workflow automation (connected to local instance)
- **memory** - Knowledge graph persistence

## Memory Locations

- `~/.claude_memory/` - Nested tree memory (use _CONTENTS.md for traversal)
- `~/.claude_memory/historian.py` - Logging script
- `~/.claude_memory/AGENT_PLAYBOOK.md` - Detailed agent rules
- `~/.claude_memory/subagent_advisor.md` - Auto-recommendation system for 140+ subagents
- `~/.claude_memory/ephor_auto_delegation.md` - **MANDATORY** auto-delegation rules & triggers

---

## Enforcement

If I skip a pattern I should have used, I am FAILING the user.

**CRITICAL:** If I skip an ephor delegation when triggers are met, I am WASTING the user's tokens and FAILING them.

The user chose "no thought" mode. They should not have to remind me.

**Token Conservation is MANDATORY:** The user has unlimited Opus 4.5 via ephor. I MUST use it for research/analysis/planning tasks.

---

## OFFICIAL PLUGIN INTEGRATION

### Plugin Marketplace Catalog

**Tier 1: Always Available (Installed)**
- `/create-prd`, `/create-tech-spec`, `/create-test-plan` - Anthropic document-skills
- `/brainstorm`, `/write`, `/execute` - Superpowers lifecycle
- `/ralph-loop` - Autonomous execution (already installed)
- `planning-with-files` - Persistent planning & ROADMAP.md integration

**Tier 2: Specialized Subagents (Install on Demand)**
- VoltAgent marketplace: 140+ specialized agents
- Install when user requests specific expertise: debugging, security, performance, etc.
- Pattern: `\plugin install <subagent-name>@awesome-claude-code-subagents`

**Tier 3: External Tools**
- `ephor` / `ephor-agent` - External LLM delegation (Opus 4.5 unlimited)
- `skill-prompt-generator` - Standalone prompt engineering tool

### Enhanced Decision Tree (Plugin-Integrated)

```text
User gives task
    │
    ▼
EPHOR DELEGATION CHECK (Check ~/.claude_memory/ephor_auto_delegation.md)
Match keywords → Check token usage → Auto-delegate if required
        │
    DELEGATE ─┴─ CONTINUE
        │         │
     [ephor]      │
        │         │
        └─────────┘
            │
            ▼
SUBAGENT ADVISOR (Check ~/.claude_memory/subagent_advisor.md)
Analyze task → Recommend specialized subagent if needed
    │
    ▼
Is this a NEW PROJECT or FEATURE?
    │
YES ─┴─ NO
 │      │
 ▼      ▼
/brainstorm  Continue  ← Superpowers: Ideation phase
 │
 ▼
Do I need to find files/understand structure?
 │
YES ─┴─ NO
 │      │
 ▼      ▼
EXPLORER Pattern  Continue  ← Original: Read ~/.claude_memory/_CONTENTS.md
(ephor "Analyze...")
 │
 ▼
Am I implementing with external API/library?
 │
YES ─┴─ NO
 │      │
 ▼      ▼
RESEARCHER Pattern  Continue  ← Original: Delegate to ephor
(ephor "Research...")
 │
 ▼
Is this complex reasoning/planning?
 │
YES ─┴─ NO
 │      │
 ▼      ▼
THINKER Pattern  Continue  ← Original: ephor "Plan/Analyze..."
 │
 ▼
Ready to WRITE SPECS?
 │
YES ─┴─ NO
 │      │
 ▼      ▼
/write  Continue  ← Superpowers: Spec creation
 │
 ▼
Ready to IMPLEMENT?
 │
YES ─┴─ NO
 │      │
 ▼      ▼
/execute  Continue  ← Superpowers: TDD workflow
 │
 ▼
Task is WELL-DEFINED and AUTONOMOUS?
 │
YES ─┴─ NO
 │      │
 ▼      ▼
/ralph-loop  Continue  ← Autonomous iteration (max 15 iterations)
 │
 ▼
Did I complete something SIGNIFICANT?
 │
YES ─┴─ NO
 │      │
 ▼      ▼
HISTORIAN  Done  ← Original: Log to memory
```

### Historian Integration with Plugins

**Global memory** (system-wide learnings):
```bash
python3 ~/.claude_memory/historian.py 'category/subcategory' 'Title' 'Content'
```

**Project checkpoints** (plugin workflow states):
```python
from historian import save_checkpoint
save_checkpoint('Completed /write phase for auth module')
```

### Ephor + Plugins Strategy

**When to delegate to ephor (unlimited Opus 4.5):**
- Complex reasoning during `/brainstorm` → use `think "..."`
- External API research during `/write` → use `research "..."`
- Architecture decisions during planning → use `analyze "..."`
- Deep analysis for EXPLORER pattern → use `analyze "..."`

**Easy commands for ephor delegation:**
- `think "query"` - Deep reasoning and planning
- `research "query"` - Research external APIs, libraries, best practices
- `analyze "query"` - Architecture analysis, code structure analysis

**Example workflow:**
```
User: "Build OAuth2 authentication"
  → /brainstorm (generates ideas)
  → research "OAuth2 best practices 2026" (deep research via ephor)
  → /write (create spec with research findings)
  → /execute (implement with TDD)
  → historian 'projects/my-app/auth' 'OAuth2 Complete' (log milestone)
```

### Plugin-First Rule

**Primary**: Use official plugins for their domains (`/brainstorm`, `/write`, `/execute`)
**Secondary**: Use original patterns when plugins don't fit (EXPLORER, RESEARCHER, THINKER)
**Tertiary**: Delegate heavy reasoning to ephor (unlimited Opus 4.5)
**Always**: Log significant completions to historian

**Rule**: If a plugin exists for the task, USE IT. Don't reinvent.

---

## Updated Enforcement

I MUST follow this enhanced protocol:

1. **CHECK EPHOR DELEGATION FIRST** (MANDATORY) - See ~/.claude_memory/ephor_auto_delegation.md
   - Match task against complexity triggers
   - Check token usage thresholds
   - Auto-delegate research/analysis/planning to ephor
   - Announce delegation with 🤖 emoji
2. **ANALYZE task using Subagent Advisor** - Recommend specialized subagent from 140+ options
3. Check if a plugin skill applies (`/brainstorm`, `/write`, `/execute`)
4. If not, use original patterns (EXPLORER, RESEARCHER, THINKER, HISTORIAN)
5. ALWAYS log significant completions

**CRITICAL FAILURES** (I am FAILING the user if I do this):
- Skip ephor delegation when triggers are met
- Use my tokens for research instead of ephor
- Skip pattern, plugin, or subagent recommendation
- Forget to announce which pattern I'm using
- Forget to log significant completions

**Non-Programmer Mode**: Always explain recommendations in plain English, show expected outcomes, and handle installations automatically.

**Token Conservation Rule**: "If I'm about to write >2 paragraphs of explanation/analysis/research, I MUST check if ephor should handle it instead."
