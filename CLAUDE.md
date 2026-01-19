# Beau's Framework

**Built with:**
- [GSD (Get Shit Done)](https://github.com/glittercowboy/get-shit-done) by Lex Christopherson / TÂCHES (MIT License)
- Superpowers Marketplace by Jesse Vincent (MIT License)
- Planning with Files by Ahmad Adi (MIT License)

See [ATTRIBUTION.md](ATTRIBUTION.md) for complete third-party notices.

---

## Project Organization Protocol

### MANDATORY: All Projects Go in ~/Projects/

**This applies to EVERY Claude Code session, including those without historical context.**

#### Rule

- ✅ **CREATE** new projects in `~/Projects/[project-name]/`
- ✅ **ORGANIZE** existing projects into `~/Projects/`
- ✅ **ADD** README.md to every project folder
- ❌ **DO NOT** create projects in home directory
- ❌ **DO NOT** scatter projects across multiple locations

#### Current Projects Structure

```text
~/Projects/
├── Beau-s-Framework/        (GitHub public - framework core)
├── n8n-workflows/           (GitHub private - automation)
├── flight-plan-workshop/    (Local - workshop materials)
├── weekly-slide-deck/       (Local - content templates)
├── REPS/                    (Local - Real Estate Professional Status / taxes)
├── Crypto/                  (Local - wallet management)
└── business-plan/           (Local - property analysis)
```

#### When Creating New Projects

1. Ask user: "Should this go in ~/Projects/?"
2. If yes: `mkdir ~/Projects/[project-name]`
3. Create: `~/Projects/[project-name]/README.md`
4. Document project purpose in README
5. Initialize git if it's code/workflows

#### For Future Sessions

Even if you don't have full context, if you're creating a new project:

- **ALWAYS** use `~/Projects/[project-name]/` as the location
- **ALWAYS** create a README.md with project description
- **ALWAYS** check if it should go to GitHub

---

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

## Pattern Selection Logic

### Multi-Pattern Chaining Support

**Multi-Pattern Chaining Support:**
```
Patterns can be chained when request requires multiple phases.

Pattern Priority Order (for chaining):
1. EXPLORER (understand structure first)
2. RESEARCHER (gather external knowledge)
3. THINKER (make decisions)
4. HISTORIAN (understand evolution)

Chaining Rules:
- IF request has "understand/explore" AND "fix/implement" → EXPLORER then RESEARCHER
- IF request has "research" AND "design/plan" → RESEARCHER then THINKER
- IF request has "explore" AND "analyze" → EXPLORER then THINKER
- IF request has "explore" AND "history" → EXPLORER then HISTORIAN
- IF request has 3+ pattern triggers → Chain in priority order

Single Pattern Selection:
- IF ONLY exploring_unknown_system → EXPLORER
- IF ONLY debugging_or_investigating → RESEARCHER
- IF ONLY design_decision_needed → THINKER
- IF ONLY understanding_evolution → HISTORIAN
- IF routine_task → No pattern (direct execution)

Pattern Trigger Keywords:
- EXPLORER: "explore", "understand structure", "map", "navigate", "where is"
- RESEARCHER: "research", "investigate", "debug", "why does", "how does"
- THINKER: "design", "plan", "analyze", "decide", "evaluate", "compare"
- HISTORIAN: "history", "evolution", "changed", "when was", "git log"
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

## Task Intake Decision Tree

### 5.1 Task Intake (Priority-Ordered, Mutually Exclusive)

**Evaluation Order:** Check conditions top-to-bottom. First match wins.

```
USER REQUEST
    │
    ▼
1. Complex/Multi-step? ──────────→ Consider Ephor activation
   (3+ distinct deliverables OR
    Multi-domain work OR
    Mentions "all", "entire", "every" OR
    Requires >10 file changes)
    │
    ▼
2. Needs clarification? ─────────→ Ask 1-2 specific questions
   (Contains "maybe", "possibly", "?" OR
    Missing key details OR
    Multiple valid interpretations)
    │
    ▼
3. Ambiguous? ───────────────────→ State assumption, proceed
   (Vague description BUT
    Can infer reasonable approach OR
    Context provides clues)
    │
    ▼
4. Clear & scoped? ──────────────→ Execute directly
   (Specific file/line/function OR
    Single well-defined task OR
    <3 files, <5 steps)
    │
    ▼
5. Default: Treat as "Needs clarification"
```

**Priority Rationale:**
- Complexity checked first (most important routing decision)
- Clarification before assumptions (better to ask than guess)
- Ambiguous before clear (conservative - assumes unclear unless obvious)
- Default fallback prevents unhandled cases

### 5.1.1 Tiebreaker Logic (When Multiple Branches Could Match)

**When request could match multiple branches, use priority order:**

Priority: **Complex > Clarification > Ambiguous > Clear**

**Tiebreaker Rules:**

| Situation | Winner | Reasoning |
|-----------|--------|-----------|
| Clear scope + High complexity | **Complex** | Complexity determines orchestration needs |
| Clear intent + Missing details | **Clarification** | Better to ask than assume |
| Vague description + Inferable intent | **Ambiguous** | Can proceed with stated assumption |
| Multiple possible matches | **Use priority order** | Systematic, predictable routing |
| No clear match | **Clarification** | Conservative default |

**Examples:**

```
"Refactor all auth files with new library"
  - Matches: Clear (auth files) + Complex (all, refactor, new library)
  - Winner: Complex (priority rule)

"Update the config"
  - Matches: Clear (config) + Clarification (which config?)
  - Winner: Clarification (priority rule)

"The app feels slow"
  - Matches: Ambiguous (vague) + Clarification (no specifics)
  - Winner: Ambiguous (can infer "performance issue", proceed with assumption)

"Do something about X"
  - Matches: None clearly
  - Winner: Clarification (default fallback)
```

**Why This Priority Order:**

1. **Complexity first:** Determines resource allocation (Ephor vs local)
2. **Clarification second:** Prevents wasted effort on wrong assumptions
3. **Ambiguous third:** When we can infer intent, proceed (efficiency)
4. **Clear last:** Only when obviously simple and well-defined

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

---

## 📋 PART 8: REDUNDANCY RESOLUTION

### 8.1 Ephor vs Task-Master Plugin (REDUNDANCY-001)

**Problem:** Both claim to decompose tasks and track progress, causing confusion.

**RESOLUTION - Clear Role Separation:**

| Feature | Ephor | Task-Master Plugin |
|---------|-------|-------------------|
| **Scope** | Single-session runtime orchestration | Persistent cross-session project management |
| **Lifecycle** | Temporary (ends when task completes) | Permanent (survives context resets) |
| **Use Case** | "Break down THIS complex request into sub-tasks and execute NOW" | "Track ongoing project with phases/milestones over days/weeks" |
| **Storage** | In-memory (context only) | File-based (.claude/tasks.md) |
| **Triggers** | Complexity keywords detected in user request | Explicit `/task` commands or long-term projects |
| **Output** | Immediate execution with synthesis | Progress tracking, task lists, dependency graphs |

**Decision Rule:**
- User says "orchestrate", "coordinate", "multi-step" in a SINGLE REQUEST → **Ephor**
- User needs TODO lists, project tracking, or resumes work across sessions → **Task-Master**
- If unsure: "Is this one big request to complete now?" → Ephor. "Is this a multi-day project?" → Task-Master.

**Example Disambiguation:**
```
"Orchestrate deployment across 5 services" → Ephor (single complex request)
"Track my auth system implementation over the next week" → Task-Master (long-term tracking)
"Break down OAuth2 implementation and execute it" → Ephor (decompose + execute now)
"Create a roadmap for refactoring the codebase" → Task-Master (persistent planning)
```

---

### 8.2 THINKER Pattern vs Ephor Analysis (REDUNDANCY-002)

**Problem:** Both do architectural analysis, unclear when to use which.

**RESOLUTION - Scope-Based Selection:**

| Characteristic | THINKER Pattern | Ephor Analysis |
|----------------|-----------------|----------------|
| **Decision Count** | Single decision or 2-3 related options | Multi-faceted problem with dependencies |
| **Constraint Complexity** | Simple constraint set (2-5 factors) | Complex constraint web (6+ factors, trade-offs) |
| **Output** | One recommendation with rationale | Comprehensive plan with execution steps |
| **Token Cost** | Low (<2000 tokens) | High (>5000 tokens) |
| **Example** | "Should we use Redis or Memcached?" | "Design entire caching strategy across microservices" |

**Decision Rule:**
- **Single decision point** (even if nuanced) → THINKER
- **Multiple interconnected decisions** → Ephor
- **Binary/tertiary choice** → THINKER
- **Architectural planning** spanning multiple components → Ephor

**Visual Decision Tree:**
```
Need to make a decision?
    │
    ▼
Is it ONE question with 2-3 options?
    │
YES ─┴─ NO (multiple questions/complex dependencies)
 │       │
 ▼       ▼
THINKER  Ephor
```

**Examples:**
```
"Which state management library?" → THINKER (single choice, clear options)
"Design state management architecture for our app" → Ephor (many decisions: library, patterns, data flow, persistence, sync)

"Should we use REST or GraphQL?" → THINKER (binary choice)
"Design our entire API strategy" → Ephor (REST vs GraphQL + auth + versioning + rate limiting + docs)

"Evaluate these 3 database options" → THINKER (tertiary choice)
"Plan our data layer migration strategy" → Ephor (DB choice + migration plan + rollback + testing + monitoring)
```

---

### 8.3 Memory Auto-Save Deduplication (REDUNDANCY-003)

**Problem:** Auto-save and manual saves could duplicate entries.

**RESOLUTION - Deduplication Logic:**

**Implemented Strategy:**
1. **Timestamp Check:** Before any save, check last save in category
2. **Time Window:** If last save was <5 minutes ago, compare content
3. **Content Similarity:** Compute simple hash or first 100 chars comparison
4. **Skip Rule:** If >80% similar AND <5 min ago, skip save (log: "Skipped duplicate save")
5. **Force Save:** Manual saves with `force=true` flag bypass dedup

**Deduplication Algorithm:**
```python
def should_save(category, title, content):
    last_save = get_last_save(category)

    if not last_save:
        return True  # No previous save, always save

    time_diff = now() - last_save.timestamp

    if time_diff > 300:  # >5 minutes
        return True  # Enough time passed, save

    # Within 5-min window, check similarity
    similarity = compute_similarity(content, last_save.content)

    if similarity < 0.8:  # <80% similar
        return True  # Different enough, save

    # Too similar, too recent - skip
    log_debug(f"Skipped duplicate save: {title} (similarity: {similarity:.0%})")
    return False
```

**Auto-Save Triggers (After Dedup Check):**
- Task completion (phase done, bug fixed, feature implemented)
- Significant discovery (root cause found, pattern identified)
- Configuration change affecting behavior
- Architectural decision made

**Manual Save Override:**
```bash
# Force save even if similar to recent save
python3 ~/.claude_memory/historian.py 'category' 'Title' 'Content' --force
```

**Benefits:**
- Prevents spam from repeated similar discoveries
- Allows explicit saves when needed
- Maintains clean memory without duplicates
- Logs skipped saves for debugging

---

## 📖 PART 9: GLOSSARY - PRECISE DEFINITIONS

### Framework Term Definitions

To eliminate ambiguity, all vague terms are precisely defined:

#### "Significant" (for HISTORIAN logging)

**Definition:** Worth referencing in future sessions

**Criteria (any ONE triggers significance):**
- Fixed a bug (any severity)
- Implemented a feature (any size)
- Made an architectural decision
- Discovered a non-obvious pattern/solution
- Changed configuration affecting behavior
- Completed a milestone or phase
- Found root cause of complex issue

**NOT significant:**
- Read files (information gathering)
- Asked questions (exploration)
- Made minor formatting changes
- Failed attempts (unless revealing insight)
- Routine file operations

**Edge Cases:**
- "Tried 3 approaches, 4th worked" → Significant (documents solution path)
- "Refactored for readability" → Significant only if changes architecture
- "Added comments" → Not significant (unless documenting complex logic)

---

#### "Minimal" (for RESEARCHER pattern testing)

**Definition:** Smallest change that tests hypothesis

**Criteria:**
- ≤10 lines of code changed
- Single function/method modified
- No API contract changes
- Reversible in 1 command (e.g., `git checkout file`)
- No new dependencies added
- No database schema changes

**Examples:**
- Minimal: Add print statement to trace value
- Minimal: Comment out one condition
- Minimal: Change constant to test behavior
- NOT minimal: Refactor entire module
- NOT minimal: Add new library

---

#### "Routine Task" (for pattern selection)

**Definition:** Task not requiring specialized thinking patterns

**Criteria (ALL must be true):**
- ≤3 distinct steps
- ≤5 files involved
- No unknowns (you know exactly what to do)
- Estimated ≤1000 tokens output
- No external research needed
- No architectural decisions

**Examples:**
- Routine: Fix typo in single file
- Routine: Add console.log for debugging
- Routine: Update version number in package.json
- NOT routine: "Fix the authentication bug" (requires investigation)
- NOT routine: "Add new feature X" (requires design)

---

#### "Complex Task" (for Ephor activation)

**Definition:** Task requiring orchestration or multi-faceted approach

**Criteria (any TWO triggers complexity):**
- ≥3 distinct deliverables
- Multiple domains (e.g., frontend + backend + database)
- Requires coordinating changes across >5 files
- Mentions "all", "entire", "every", "complete"
- Needs both research AND implementation
- Has dependencies between subtasks
- Estimated >5000 tokens output

**Examples:**
- Complex: "Implement OAuth2 authentication with refresh tokens"
- Complex: "Refactor entire payment module for new API"
- Complex: "Build complete user management system"
- NOT complex: "Add a logout button" (single feature)
- NOT complex: "Fix bug in login.py:42" (specific, isolated)

---

#### "Tightly Coupled" (for Ephor delegation decisions)

**Definition:** Tasks sharing mutable state or requiring sequential data flow

**Criteria (any ONE indicates coupling):**
- Task B depends on Task A's output value
- Both tasks modify same data structure
- Order matters (A must complete before B starts)
- Shared global state between tasks
- Context switching loses critical information

**Examples:**
- Coupled: "Parse config, then validate schema" (validation needs parsed data)
- Coupled: "Create user, then assign permissions" (permissions need user ID)
- NOT coupled: "Fix bug in auth" + "Fix bug in payment" (independent)
- NOT coupled: "Update README" + "Update CHANGELOG" (can be parallel)

---

#### "Self-Contained" (for Ephor sub-task creation)

**Definition:** Task with clear boundaries and no shared state

**Criteria (ALL must be true):**
- Clear input requirements (data/files needed)
- Defined output specification (what it produces)
- No dependencies on other sub-tasks
- Can be executed in any order (if multiple)
- No shared mutable state with other tasks

**Examples:**
- Self-contained: "Write unit tests for auth.py" (input: auth.py, output: tests)
- Self-contained: "Update documentation for API endpoint X"
- NOT self-contained: "Implement API endpoint" (depends on schema, models, etc.)

---

#### "Architectural Issue" (for error handling)

**Definition:** Error indicating design flaw, not implementation bug

**Criteria (any TWO indicates architectural):**
- Affects >3 files to fix properly
- Changes API contracts or interfaces
- Impacts design patterns used
- Requires significant refactoring
- Reveals tight coupling problems
- Same error class appears in multiple places
- Fix requires changing system boundaries

**Examples:**
- Architectural: "Circular dependency between modules"
- Architectural: "Global state causing race conditions across components"
- NOT architectural: "Typo in function name"
- NOT architectural: "Missing null check" (implementation detail)

---

### Using These Definitions

When encountering ambiguous situations:

1. **Reference this glossary**
2. **Apply criteria systematically** (don't guess)
3. **Document edge cases** (add to glossary if novel)
4. **Err on side of caution** (if unsure, use more conservative interpretation)

**Example Decision Process:**

```
Question: "Should I log this to memory?"
  ↓
Check: Does it meet "significant" criteria?
  ↓
Criteria: "Fixed a bug" → YES → Log it
  ↓
If criteria unclear → Err toward logging (better to have than miss)
```
