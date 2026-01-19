# RALPH Loop Test Scenario

**Created:** 2026-01-19
**Purpose:** Safe test scenario for validating RALPH autonomous execution

---

## Test 3: RALPH Autonomous Execution

### Status: VERIFIED (Installation) - READY FOR USER TESTING

**Plugin Location:** `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/ralph-loop/`

**Installation Status:** ✅ INSTALLED (official plugin)

---

## How RALPH Works

RALPH uses a **Stop hook** that intercepts Claude's exit attempts:

```
1. You run: /ralph-loop "task" --max-iterations N --completion-promise "DONE"
2. Claude works on task
3. Claude tries to exit
4. Stop hook blocks exit
5. Stop hook feeds SAME prompt back
6. Repeat until completion promise detected or max iterations reached
```

**Key Features:**
- Self-referential feedback loop
- Prompt stays constant
- Claude improves by reading its own previous work in files
- Autonomous iteration until completion

---

## Safe Test Scenario (Recommended)

**Test:** Create a simple validation report autonomously

**Command:**
```bash
/ralph-loop "Create a file called ralph_test_report.md with the following sections: 1) Test Name, 2) Timestamp, 3) Status (PASS). When complete, output <promise>REPORT_COMPLETE</promise>" --max-iterations 3 --completion-promise "REPORT_COMPLETE"
```

**Expected Behavior:**
1. **Iteration 1:** Claude creates ralph_test_report.md with basic content
2. **Iteration 2:** Claude reviews file, may enhance it
3. **Iteration 3:** Claude outputs `<promise>REPORT_COMPLETE</promise>`
4. **Loop ends:** RALPH detects completion promise and stops

**What to Watch For:**
- ✅ File created correctly
- ✅ Loop stops at completion promise (not max iterations)
- ✅ No infinite loop
- ✅ Claude improves work between iterations

**Cost Estimate:** $1-3 (3 iterations × ~1k tokens each)

---

## More Complex Test Scenario

**Test:** Self-validation of framework components

**Command:**
```bash
/ralph-loop "Analyze the Chief Agent Framework installation. Check: 1) historian.py exists and has save_snapshot + save_checkpoint functions, 2) CLAUDE.md has plugin integration section, 3) memory tree structure at ~/.claude_memory/. Create a validation report with findings. Output <promise>VALIDATION_COMPLETE</promise> when done." --max-iterations 5 --completion-promise "VALIDATION_COMPLETE"
```

**Expected Behavior:**
1. **Iteration 1:** Read historian.py, check functions
2. **Iteration 2:** Read CLAUDE.md, verify sections
3. **Iteration 3:** Examine memory tree structure
4. **Iteration 4:** Create validation report
5. **Iteration 5:** Review and finalize, output completion promise

**Cost Estimate:** $5-10 (5 iterations × ~2k tokens each)

---

## Test Commands

### Start RALPH (in a new Claude Code session)
```bash
# Simple test
/ralph-loop "Create ralph_test_report.md with sections: Test Name, Timestamp, Status. Output <promise>REPORT_COMPLETE</promise> when done." --max-iterations 3 --completion-promise "REPORT_COMPLETE"

# Complex test
/ralph-loop "Validate Chief Agent Framework components. Check historian.py, CLAUDE.md, memory tree. Create report. Output <promise>VALIDATION_COMPLETE</promise> when done." --max-iterations 5 --completion-promise "VALIDATION_COMPLETE"
```

### Cancel RALPH (if needed)
```bash
/cancel-ralph
```

### Monitor RALPH (separate terminal)
```bash
# Watch the RALPH state file
tail -f ~/.claude/ralph-loop.local.md

# Check current iteration
cat ~/.claude/ralph-loop.local.md | grep -i iteration
```

---

## Best Practices (from RALPH README)

### ✅ DO:
- Always set `--max-iterations` (prevents runaway loops)
- Use clear `--completion-promise` with unique XML tags like `<promise>DONE</promise>`
- Test with low iteration counts first (3-5)
- Monitor `.claude/ralph-loop.local.md` during execution
- Use `/cancel-ralph` if loop gets stuck

### ❌ DON'T:
- Don't use unlimited iterations
- Don't use vague completion criteria
- Don't run on production systems without testing first
- Don't forget the completion promise (loop will run until max iterations)
- Don't use common words as completion promise (use XML tags)

---

## Completion Criteria for Test 3

Test 3 is **PASSED** when:

- [ ] Simple test scenario completes successfully
- [ ] File is created with correct content
- [ ] Loop stops at completion promise (not max iterations)
- [ ] No infinite loop behavior
- [ ] `/cancel-ralph` works if needed

**Current Status:** Installation verified ✅, ready for user testing

---

## Integration with Framework

RALPH integrates with the Chief Agent Framework as:

**When to Use:**
- Autonomous implementation of well-defined tasks
- Test-driven development loops (write test → fail → fix → pass)
- Iterative refinement of code until all tests pass
- Self-improving documentation generation

**Pattern:**
```
User: "Build feature X with tests, iterate until passing"
  → GSD THINKER: Plan architecture
  → /ralph-loop with TDD instructions
  → RALPH iterates: implement → test → fix → repeat
  → HISTORIAN: Log completion
```

**Example:**
```bash
# After planning with THINKER pattern
/ralph-loop "Implement OAuth2 PKCE flow. Requirements: 1) Authorization endpoint, 2) Token endpoint, 3) Full test coverage, 4) All tests passing. Use TDD: write tests first, then implement. Output <promise>OAUTH_COMPLETE</promise> when all tests pass." --max-iterations 15 --completion-promise "OAUTH_COMPLETE"
```

---

## Why RALPH Wasn't Fully Tested in This Session

RALPH requires:
1. Actually running `/ralph-loop` slash command (not available via tools)
2. A separate Claude Code session (to avoid loop interference)
3. Real file operations and git history (autonomous environment)
4. User monitoring to verify behavior

**Recommendation:** User should test RALPH in a fresh Claude Code session with the simple test scenario above.

---

## Logging Test Results

After testing RALPH, log results:

```bash
# If test passed
python3 ~/.claude_memory/historian.py 'validation/framework-self-check' 'Test 3 Complete - RALPH Validated' 'Tested /ralph-loop with [scenario]. Iterations: [N]. Completion: [SUCCESS/MAXED OUT]. Loop stopped correctly. Framework integration confirmed.'

# If test failed
python3 ~/.claude_memory/historian.py 'validation/framework-self-check' 'Test 3 Issues - RALPH Investigation' 'Tested /ralph-loop with [scenario]. Issue: [description]. Needs troubleshooting.'
```

---

**Test prepared:** 2026-01-19 00:08:00
**Ready for user execution**
