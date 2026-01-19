# BUG-012 & BUG-013 Test Scenarios

## BUG-012: Order Independence

### Scenario 1: Forward Order
**Input:** "analyze and implement caching"
**Expected:** Ephor ACTIVATES (both keywords present)

### Scenario 2: Reverse Order
**Input:** "implement caching and analyze performance"
**Expected:** Ephor ACTIVATES (both keywords present, order doesn't matter)

### Scenario 3: Scattered Keywords
**Input:** "implement feature X, then we'll analyze, and finally orchestrate deployment"
**Expected:** Ephor ACTIVATES (multiple triggers regardless of order)

## BUG-013: Negation Detection

### Scenario 1: Negation with "don't"
**Input:** "don't orchestrate this manually, just document it"
**Expected:** Ephor DOES NOT activate (negation detected)

### Scenario 2: Negation with "avoid"
**Input:** "avoid using multi-step workflows for this simple task"
**Expected:** Ephor DOES NOT activate (negation detected)

### Scenario 3: Negation with "without"
**Input:** "implement this without orchestration"
**Expected:** Ephor DOES NOT activate (negation detected)

### Scenario 4: Negation with "not"
**Input:** "this is not a complex multi-step process"
**Expected:** Ephor DOES NOT activate (negation detected)

### Scenario 5: False Negation (Should Still Activate)
**Input:** "this is definitely not simple - orchestrate all services"
**Expected:** Ephor ACTIVATES (double negative + explicit trigger)

## Word Boundary Detection

### Scenario 1: Partial Match (Should NOT trigger)
**Input:** "the uncoordinated system needs fixing"
**Expected:** Ephor DOES NOT activate ("coordinate" substring, not whole word)

### Scenario 2: Natural Variants (Should trigger)
**Input:** "do this in multiple steps"
**Expected:** Ephor ACTIVATES ("multiple steps" = "multi-step" variant)
