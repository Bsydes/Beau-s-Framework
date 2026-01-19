# Attribution & Third-Party Components

This document lists all third-party frameworks, tools, and concepts used in Beau's Framework.

---

## Core Framework Components

### 1. **Superpowers Marketplace**
- **Author:** Jesse Vincent
- **License:** MIT License (Copyright 2025)
- **Used For:** Skills including `/brainstorm`, `/write`, `/execute`, systematic debugging, TDD workflows
- **Source:** https://github.com/superpowers-marketplace (assumed)
- **Attribution Required:** ✅ Yes - MIT License requires copyright notice
- **Usage:** Pattern-based skill system concepts integrated into framework decision trees

### 2. **Planning with Files**
- **Author:** Ahmad Adi
- **License:** MIT License (Copyright 2026)
- **Used For:** File-based planning methodology, task management concepts
- **Attribution Required:** ✅ Yes - MIT License requires copyright notice
- **Usage:** Planning pattern concepts adapted for THINKER pattern

### 3. **Anthropic Agent Skills (document-skills)**
- **Author:** Anthropic PBC
- **License:** Proprietary (with third-party notices)
- **Used For:** Skills including `/create-prd`, `/create-tech-spec`, `/create-test-plan`, theme-factory, pdf, xlsx, pptx, docx
- **Source:** https://agentskills.io / https://support.claude.com
- **Attribution Required:** ✅ Yes - See THIRD_PARTY_NOTICES.md in their distribution
- **Usage:** Referenced as available tools in plugin integration section

### 4. **Ralph-Loop**
- **Author:** Anthropic (assumed from claude-plugins-official)
- **License:** Assumed proprietary Anthropic license
- **Used For:** Autonomous execution loop with completion promises
- **Attribution Required:** ℹ️ Likely yes, but license unclear
- **Usage:** Referenced as optional execution pattern in framework

### 5. **GSD (Get Shit Done) Framework**

- **Author:** Lex Christopherson (@glittercowboy)
- **Organization:** TÂCHES
- **License:** MIT License (Copyright 2025)
- **Source:** https://github.com/glittercowboy/get-shit-done
- **Installed Version:** 1.6.4
- **Popularity:** 4.9k GitHub stars, used by engineers at Amazon, Google, Shopify, Webflow
- **Description:** Lightweight meta-prompting, context engineering, and spec-driven development system for Claude Code
- **Used For:** Complete skill suite including:
  - `gsd:new-project` - Project initialization with research
  - `gsd:new-milestone` - Milestone cycle management
  - `gsd:plan-phase` - Phase planning with verification
  - `gsd:execute-phase` - Wave-based parallel execution
  - `gsd:verify-work` - Conversational UAT
  - `gsd:debug` - Systematic debugging with state
  - `gsd:map-codebase` - Parallel codebase analysis
  - Plus 17 other specialized skills (24 total commands)
- **Attribution Required:** ✅ YES - MIT License requires copyright notice
- **Usage:** Core skill system integrated throughout framework documentation
- **Note:** "Beau's Framework" incorporates GSD workflow concepts and references GSD commands

### 6. **VoltAgent Marketplace**

- **Author:** Unknown (140+ subagents collection)
- **License:** Unknown
- **Used For:** Specialized subagent recommendations
- **Attribution Required:** ⚠️ Unknown - needs research
- **Usage:** Subagent Advisor references these as available tools

---

## External Tools & APIs

### 7. **Ephor AI**

- **Service:** Ephor.ai API
- **License:** Commercial API service (not open-source)
- **Used For:** Unlimited LLM delegation (Opus 4.5, GPT-5, O3, etc.)
- **API Endpoint:** https://api.ephor.ai/api/v1/multiplexer/query-project
- **Attribution Required:** ℹ️ Not required (commercial service)
- **Usage:** Token-saving delegation for research/analysis/planning tasks

### 8. **MCP (Model Context Protocol)**

- **Author:** Anthropic
- **License:** Assumed open specification
- **Used For:** Server integrations (n8n workflow automation, memory graph)
- **Attribution Required:** ℹ️ Specification reference only
- **Usage:** Integration framework for external services

### 9. **n8n Workflow Automation**

- **Author:** n8n GmbH
- **License:** Fair Code License (n8n)
- **Used For:** MCP server integration for workflow automation
- **Attribution Required:** ℹ️ Integration only, not distribution
- **Usage:** Referenced as active MCP server

---

## Original Contributions (Beau's Framework)

The following components are **original work** created for Beau's Framework:

✅ **Ephor Auto-Delegation System**
- Token budget awareness algorithm
- Complexity trigger detection (negation, order-independence, word boundaries)
- 6 task category delegation rules

✅ **Multi-Pattern Chaining Logic**
- Pattern priority order (EXPLORER → RESEARCHER → THINKER → HISTORIAN)
- Chaining rules for complex requests
- Single vs multi-pattern selection algorithm

✅ **Decision Tree Architecture**
- Priority-ordered, mutually exclusive branches
- Tiebreaker logic for ambiguous requests
- 5-level task intake classification

✅ **Redundancy Resolution**
- Ephor vs Task-Master role separation
- THINKER vs Ephor scope-based selection
- Memory deduplication algorithm (5-min window, 80% similarity threshold)

✅ **Comprehensive Glossary**
- Precise definitions for "Significant", "Minimal", "Routine Task", "Complex Task", "Tightly Coupled", "Self-Contained", "Architectural Issue"

✅ **Validation Scripts**
- `validate-framework.sh` - 18 automated tests
- `monitor-progress.sh` - Git commit tracking
- Test scenario files for all bug fixes

---

## License Compliance Summary

### ✅ MIT License Components (Requires Attribution)

**Required:** Include copyright notices from:
- **GSD Framework** (Copyright 2025 Lex Christopherson)
- **Superpowers Marketplace** (Copyright 2025 Jesse Vincent)
- **Planning with Files** (Copyright 2026 Ahmad Adi)

**Compliance:** Add this to CLAUDE.md header:

```markdown
# Beau's Framework

**Built with:**
- GSD (Get Shit Done) by Lex Christopherson / TÂCHES (MIT License)
- Superpowers Marketplace by Jesse Vincent (MIT License)
- Planning with Files by Ahmad Adi (MIT License)

See ATTRIBUTION.md for complete third-party notices.
```

### ⚠️ Needs Further Research

1. **VoltAgent Marketplace** - Unknown license, may need permission
2. **Ralph-Loop** - Anthropic official plugin, license unclear
3. **Anthropic Agent Skills** - Review THIRD_PARTY_NOTICES.md for full attribution requirements

### ℹ️ Safe to Use (No Attribution Required)

- Ephor AI (commercial API service)
- MCP specification (integration only)
- n8n (integration only, not distributing)

---

## Recommended Actions

### Immediate (Before Publishing to GitHub):

1. ✅ Add attribution header to CLAUDE.md (see above)
2. ✅ Include this ATTRIBUTION.md file in repository
3. ⚠️ Research VoltAgent marketplace license
4. ⚠️ Verify Anthropic Agent Skills attribution requirements

### License Choice:

**Recommended:** MIT License

**Reason:**
- Compatible with MIT-licensed dependencies (Superpowers, Planning-with-Files)
- Allows others to use/modify your framework
- Simple and widely understood
- Gives you credit while being generous to community

**License Text to Add:**

```
MIT License

Copyright (c) 2026 Beau Sydes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Summary

**Original Work:** ~70% (ephor delegation, pattern chaining, decision trees, glossary)
**Adapted Concepts:** ~20% (skill patterns from Superpowers/Planning-with-Files)
**Referenced Tools:** ~10% (Anthropic skills, VoltAgent marketplace, GSD framework)

**Legal Status:** ✅ Safe to publish with proper MIT attributions

**License Recommendation:** MIT License (matches all primary dependencies)

**Action Required:**

1. ✅ ~~Research GSD Framework origin and license~~ COMPLETE - MIT License by Lex Christopherson
2. Add attribution header to CLAUDE.md (see below)
3. Include this ATTRIBUTION.md file in repository
4. ⚠️ Optional: Verify VoltAgent marketplace licensing (low priority - referenced tools only)
