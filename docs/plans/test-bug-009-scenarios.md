# BUG-009 Test Scenarios

## Scenario 1: EXPLORER + RESEARCHER
**Input:** "Understand how authentication works and then fix the login bug"
**Expected:** Announces both patterns, executes EXPLORER first, then RESEARCHER
**Pattern Chain:** EXPLORER → RESEARCHER

## Scenario 2: RESEARCHER + THINKER
**Input:** "Research OAuth2 best practices and design our implementation approach"
**Expected:** RESEARCHER first (external knowledge), then THINKER (design)
**Pattern Chain:** RESEARCHER → THINKER

## Scenario 3: EXPLORER + THINKER + HISTORIAN
**Input:** "Explore the payment module, analyze architecture, and check its evolution history"
**Expected:** Three patterns in sequence
**Pattern Chain:** EXPLORER → THINKER → HISTORIAN

## Scenario 4: Single Pattern (No Chain)
**Input:** "Fix the typo in README.md"
**Expected:** No pattern (direct execution)
**Pattern Chain:** None
