# Agent Playbook

> How Claude should use each sub-agent. These are the embedded instructions.
> **System: Strict Nested Tree Memory with Safe Mode**

---

## 1. The Explorer (The Scout)

**When to use:** When asked "Where is the code for X?" or "How is this project structured?"

**The Rule:** "Look, don't touch."
- Map the file structure BEFORE reading any file content
- Only read files after pinpointing the exact one needed

### Memory Traversal Protocol (STRICT)

**NEVER use `find` or `ls -R` on `.claude_memory`** - it is too large and burns context.

**Correct Traversal Method:**
1. Read `~/.claude_memory/_CONTENTS.md` to see top-level categories
2. Read `~/.claude_memory/[category]/_CONTENTS.md` to drill down
3. Only read the specific target file once found

**Why:** If Claude reads every file immediately, it burns the context window and gets confused. The Explorer saves tokens by only pinpointing the exact file needed.

**Invocation:** `@explorer`

---

## 2. The Researcher (The Librarian)

**When to use:** When asked "How do I use the n8n API?" or "Figure out why this error is happening."

**The Rule:** "Parallel Search."
- Perform multiple searches at once (docs, forums, GitHub)
- Summarize findings into a strict implementation plan
- BEFORE writing any code

**Why:** This prevents "hallucinations" where Claude guesses how a library works. It forces it to check the manual first.

**Invocation:** `@researcher`

---

## 3. The Historian (The Filer)

**When to use:** After every major success (e.g., "Workflow Created", "Bug Fixed").

**The Rule:** "Categorize Dynamically. Do NOT dump files."

### Command Syntax
```bash
python3 ~/.claude_memory/historian.py 'category/subcategory' 'Title' 'Content'
```

### Examples
```bash
# Save a workflow fix
python3 ~/.claude_memory/historian.py 'workflows/finance' 'Fixed API Bug' 'Resolved timeout issue in payment endpoint...'

# Save a system config change
python3 ~/.claude_memory/historian.py 'system/config' 'Updated Rate Limits' 'Changed from 100 to 500 req/min...'

# Save research findings
python3 ~/.claude_memory/historian.py 'research/n8n' 'Webhook Best Practices' 'Findings from official docs...'
```

**What happens:**
1. Creates the folder path if it doesn't exist
2. Saves a timestamped markdown file
3. Updates `_CONTENTS.md` index files recursively up to root

**Why:** Git commits are messy. The Historian creates a clean "Project Diary" with automatic tree indexing so you (and Claude) can traverse the memory efficiently.

**Invocation:** `@historian` or direct command above

---

## Quick Reference

| Situation | Agent | Command |
|-----------|-------|---------|
| "Where is X?" | Explorer | `@explorer` (use `_CONTENTS.md` traversal) |
| "How does Y work?" | Researcher | `@researcher` |
| Task completed | Historian | `python3 ~/.claude_memory/historian.py 'path' 'title' 'content'` |

## The Core Principles

1. **Explorer:** Look, don't touch. Use `_CONTENTS.md` for tree traversal.
2. **Researcher:** Parallel search, then plan
3. **Historian:** Categorize dynamically, never dump files flat

---

## Memory Tree Structure

```
~/.claude_memory/
├── _CONTENTS.md          # Auto-generated root index
├── historian.py          # The recursive librarian script
├── AGENT_PLAYBOOK.md     # This file
├── workflows/
│   ├── _CONTENTS.md      # Auto-generated
│   ├── finance/
│   │   └── _CONTENTS.md
│   └── automation/
│       └── _CONTENTS.md
├── system/
│   ├── _CONTENTS.md
│   ├── config/
│   └── logs/
└── research/
    └── _CONTENTS.md
```

---
*This playbook should be referenced in CLAUDE.md for automatic loading.*
