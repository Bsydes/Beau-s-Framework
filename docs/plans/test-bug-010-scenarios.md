# BUG-010 Test Scenarios

## Scenario 1: Clear and Simple
**Input:** "Fix the typo in line 42 of login.py"
**Expected Path:** Clear & scoped → Execute directly
**Should NOT match:** Complex/Multi-step

## Scenario 2: Clear but Complex
**Input:** "Refactor the entire authentication module and add comprehensive tests"
**Expected Path:** Complex/Multi-step → Consider Ephor
**Should NOT match:** Clear & scoped (even though scope is clear, complexity overrides)

## Scenario 3: Ambiguous and Unclear
**Input:** "Something's not working right"
**Expected Path:** Ambiguous → State assumption, proceed
**Should NOT match:** Needs clarification (too vague even for questions)

## Scenario 4: Needs Clarification
**Input:** "Maybe update the config?"
**Expected Path:** Needs clarification → Ask 1-2 questions
**Should NOT match:** Ambiguous
