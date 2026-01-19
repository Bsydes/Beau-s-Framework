# Beau's Framework - Self-Validation Protocol

**Created:** 2026-01-18
**Purpose:** Use the framework's own capabilities to validate its integration health

---

## 🎯 Validation Strategy

The framework validates itself using **recursive self-testing** - each component uses the system's own patterns to verify functionality.

### Validation Levels

1. **L1 - Component Health** (each piece works independently)
2. **L2 - Integration Points** (components work together)
3. **L3 - Workflow Validation** (end-to-end scenarios)
4. **L4 - Meta-Validation** (system validates its validators)

---

## 🧪 Self-Check Workflow (Run This!)

### Simple Self-Check (5 minutes)

Ask Claude Code in a new session:

```
Run a comprehensive self-check of Beau's Framework. Use:
1. EXPLORER pattern to map memory structure
2. RESEARCHER pattern to verify ephor delegation works
3. THINKER pattern for analyzing integration health
4. Test /brainstorm, /write, /execute plugins
5. Log results to historian

Show me what's working and what needs attention.
```

**What happens:**
- Claude uses EXPLORER to read `~/.claude_memory/_CONTENTS.md`
- Uses RESEARCHER to call `research "test query"`
- Uses THINKER to call `think "analyze framework integration"`
- Tests plugin availability with `/help`
- Logs completion to historian

### Full Self-Validation (15 minutes)

Ask Claude Code:

```
Use /planning-with-files to create a comprehensive validation plan for Beau's Framework, then execute it using /ralph-loop with max 10 iterations. Test all four patterns (EXPLORER, RESEARCHER, THINKER, HISTORIAN), all plugins (/brainstorm, /write, /execute), and ephor delegation. Log all findings to historian under 'validation/self-check'.
```

**What happens:**
- MANUS creates planning files (task_plan.md, findings.md)
- RALPH autonomously executes validation tests
- Each pattern validates itself recursively
- Results logged to memory tree
- Final report generated

---

## 📋 Specific Test Scenarios

### Test 1: Pattern Validation (GSD Brain)

**Command:**
```
Test each GSD pattern by using them to validate themselves:
- EXPLORER: Map the memory tree structure
- RESEARCHER: Research "Claude Code plugin best practices 2026"
- THINKER: Analyze the framework's own architecture
- HISTORIAN: Log this validation to memory

Show which patterns executed and their outputs.
```

**Expected Output:**
- ✅ Announces "Exploring codebase structure first..."
- ✅ Calls `analyze "..."` for EXPLORER
- ✅ Calls `research "..."` for RESEARCHER
- ✅ Calls `think "..."` for THINKER
- ✅ Calls `historian.py` for HISTORIAN
- ✅ All commands succeed

**Failure Indicators:**
- ❌ Patterns not announced
- ❌ Ephor commands fail
- ❌ Historian alias broken

### Test 2: Plugin Integration (Superpowers + Anthropic)

**Command:**
```
Use /brainstorm to design a simple feature, then /write to spec it, then show me the outputs. Don't actually implement, just test the workflow.
```

**Expected Output:**
- ✅ `/brainstorm` generates ideas
- ✅ `/write` creates spec document
- ✅ No errors in plugin execution

**Failure Indicators:**
- ❌ Plugins not found
- ❌ Commands don't execute
- ❌ Error messages about missing plugins

### Test 3: RALPH Autonomous Execution

**Command:**
```
Use /ralph-loop to autonomously analyze the ~/.claude_memory/ structure and create a summary report. Max 5 iterations. Completion promise: <DONE>Report created</DONE>
```

**Expected Output:**
- ✅ RALPH iterates (1-5 times)
- ✅ Creates summary report
- ✅ Stops when completion promise met
- ✅ No runaway iterations

**Failure Indicators:**
- ❌ RALPH doesn't start
- ❌ Doesn't stop at completion
- ❌ Exceeds max iterations

### Test 4: Ephor Delegation (Token Conservation)

**Command:**
```
Explain the architectural trade-offs between microservices and monoliths in 3+ paragraphs. Follow your auto-delegation rules.
```

**Expected Output:**
- ✅ Announces "🤖 Task requires [research/analysis]"
- ✅ States "💡 Delegating to ephor to preserve tokens"
- ✅ Calls `think` or `research` or `analyze`
- ✅ Returns ephor's response

**Failure Indicators:**
- ❌ Writes 3+ paragraphs directly (wasting tokens)
- ❌ Doesn't announce delegation
- ❌ Ephor command fails

### Test 5: Historian Memory Logging

**Command:**
```
Log a test entry to memory using: historian 'validation/framework-test' 'Self-Check Complete' 'All systems validated at [timestamp]'

Then verify it appears in the memory tree.
```

**Expected Output:**
- ✅ Command executes via Bash tool
- ✅ Success message shown
- ✅ Entry appears in `~/.claude_memory/validation/`
- ✅ `_CONTENTS.md` updated recursively

**Failure Indicators:**
- ❌ Historian alias not found
- ❌ Wrong file path used
- ❌ Index not updated

### Test 6: Subagent Recommendation (Auto-Advisor)

**Command:**
```
I have a performance issue with my React app. What should I do?
```

**Expected Output:**
- ✅ Announces "📋 Task Analysis: Performance optimization"
- ✅ Recommends `performance-optimizer` subagent
- ✅ Offers to install it
- ✅ Explains what it does

**Failure Indicators:**
- ❌ No subagent recommendation
- ❌ Doesn't mention VoltAgent marketplace
- ❌ Just gives generic advice

### Test 7: Integration Health (End-to-End)

**Command:**
```
Create a test project validation workflow:
1. /brainstorm a simple todo app
2. research "React best practices 2026" via ephor
3. /write a technical spec
4. Create a ROADMAP.md using /planning-with-files
5. Log completion to historian

Execute this workflow and show me each step.
```

**Expected Output:**
- ✅ All 5 steps execute in sequence
- ✅ Each pattern/plugin announces itself
- ✅ No integration conflicts
- ✅ Final log entry created

**Failure Indicators:**
- ❌ Steps fail or skip
- ❌ Plugins conflict
- ❌ Workflow breaks mid-execution

---

## 🔍 Integration Health Checklist

After running tests, verify:

### Critical Files
- [ ] `~/.zshrc` has correct historian alias (line 9)
- [ ] `~/.claude_memory/historian.py` has both functions (save_snapshot + save_checkpoint)
- [ ] `~/CLAUDE.md` has plugin integration section
- [ ] `~/.claude/QUICK-REFERENCE.md` exists and is comprehensive

### Aliases & Commands
- [ ] `historian 'test' 'msg' 'content'` works in terminal
- [ ] `think "query"` routes to ephor
- [ ] `research "query"` routes to ephor
- [ ] `analyze "query"` routes to ephor

### Plugins Installed
- [ ] `/create-prd` available
- [ ] `/create-tech-spec` available
- [ ] `/create-test-plan` available
- [ ] `/brainstorm` available
- [ ] `/write` available
- [ ] `/execute` available
- [ ] `/ralph-loop` available
- [ ] `/planning-with-files` available

### Patterns Execute
- [ ] EXPLORER announces and uses `analyze`
- [ ] RESEARCHER announces and uses `research`
- [ ] THINKER announces and uses `think`
- [ ] HISTORIAN logs to memory tree

### Auto-Behaviors
- [ ] Auto-delegates research tasks to ephor
- [ ] Auto-recommends subagents when applicable
- [ ] Auto-announces which pattern is being used
- [ ] Auto-logs significant completions

---

## 📊 Self-Validation Report Template

After running tests, create this report:

```markdown
# Framework Validation Report
**Date:** [timestamp]
**Validator:** Claude Code (self-validation)

## Test Results

### L1 - Component Health
- GSD Patterns: ✅/❌
- RALPH Loop: ✅/❌
- MANUS Planning: ✅/❌
- Plugins: ✅/❌
- Ephor Delegation: ✅/❌
- Historian: ✅/❌

### L2 - Integration Points
- GSD ↔ Ephor: ✅/❌
- GSD ↔ Plugins: ✅/❌
- Plugins ↔ Historian: ✅/❌
- RALPH ↔ MANUS: ✅/❌

### L3 - Workflow Validation
- Simple task (1 pattern): ✅/❌
- Complex task (2+ patterns): ✅/❌
- Full lifecycle (/brainstorm → /write → /execute): ✅/❌
- Autonomous execution (RALPH): ✅/❌

### L4 - Meta-Validation
- Self-check uses its own patterns: ✅/❌
- No circular dependencies: ✅/❌
- Error handling works: ✅/❌

## Issues Discovered
[List any failures or warnings]

## Recommendations
[Suggest fixes or improvements]

## Logged To Memory
`~/.claude_memory/validation/self-check/[timestamp]_report.md`
```

---

## 🚀 Quick Start: Run Self-Check Now

**Easiest way:** Open a new Claude Code window and ask:

```
Show me the self-validation protocol from ~/.claude_memory/self_validation.md, then execute Test 1 (Pattern Validation) to verify the framework is working.
```

Claude will:
1. Read this file (EXPLORER pattern)
2. Execute Test 1 using all patterns
3. Show you the results
4. Log completion to memory

**Next level:** After Test 1 passes, run Tests 2-7 sequentially.

**Full validation:** Use RALPH to run all tests autonomously:

```
Use /ralph-loop to execute all 7 self-validation tests from ~/.claude_memory/self_validation.md. Max 10 iterations. Log results to historian.
```

---

## 💡 What Success Looks Like

When the framework is **fully integrated and working**, you'll see:

1. **Automatic announcements**: Claude says "Exploring..." / "Researching..." before acting
2. **Ephor delegation**: Long explanations are routed to `think`/`research`/`analyze`
3. **Plugin usage**: `/brainstorm`, `/write`, `/execute` work seamlessly
4. **Memory logging**: Significant completions appear in `~/.claude_memory/`
5. **Subagent recommendations**: Claude suggests specialists when appropriate
6. **No manual prompting**: You never have to remind Claude to follow patterns

If you don't see these behaviors, re-run the validation and check the failures.

---

## 🔄 Continuous Validation

**Daily Health Check:**
```
Quick framework health check: verify patterns, test one plugin, confirm ephor delegation. 2 minutes.
```

**Weekly Deep Dive:**
```
Full self-validation using all 7 tests. Generate report. Log to memory.
```

**After Changes:**
```
Run integration tests after modifying CLAUDE.md, historian.py, or installing new plugins.
```

---

**Remember:** The framework is designed to maintain itself. Trust the auto-orchestration, use the patterns, let RALPH handle iterations, and log learnings to memory. The system gets smarter as you use it.
