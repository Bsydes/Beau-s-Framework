# BUG-016 Test Scenarios - Tiebreaker Logic

## Scenario 1: Clear Scope but High Complexity (Tiebreaker: Complexity Wins)
**Input:** "Refactor all authentication files to use the new OAuth2 library"
**Scope:** Clear (authentication files)
**Complexity:** High (refactoring, new library, multiple files)
**Expected:** Complex/Multi-step → Consider Ephor (complexity overrides clear scope)

## Scenario 2: Multiple Interpretations but Clear Intent (Tiebreaker: Clarification Wins)
**Input:** "Update the config"
**Scope:** Somewhat clear (config file)
**Ambiguity:** Which config? Which settings?
**Expected:** Needs clarification → Ask questions (ambiguity overrides loose clarity)

## Scenario 3: Vague but Inferable (Tiebreaker: Ambiguous Wins)
**Input:** "The app feels slow"
**Scope:** Unclear
**Intent:** Performance issue (inferable)
**Expected:** Ambiguous → State assumption (can infer intent despite vagueness)

## Scenario 4: Edge Case - Truly Ambiguous (Default: Clarification)
**Input:** "Do something about the system"
**Scope:** Totally unclear
**Intent:** Unknown
**Expected:** Needs clarification (default when no branch clearly wins)
