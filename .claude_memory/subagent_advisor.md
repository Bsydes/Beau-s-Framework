# SUBAGENT ADVISOR - Auto-Recommendation System

## Purpose
Automatically recommend the perfect specialized subagent from the 140+ available in the VoltAgent marketplace based on task analysis.

## Task Categories & Recommended Subagents

### 🐛 Debugging & Troubleshooting
**Triggers:** "fix bug", "error", "not working", "broken", "debug", "troubleshoot"
**Recommended:** `debugging-specialist`
- Advanced debugging workflows
- Root cause analysis
- Error trace interpretation

### 🔒 Security & Safety
**Triggers:** "security", "vulnerability", "audit", "penetration test", "secure", "auth", "encryption"
**Recommended:** `security-auditor`
- Security review & vulnerability scanning
- OWASP compliance checks
- Authentication/authorization review

### ⚡ Performance & Optimization
**Triggers:** "slow", "performance", "optimize", "speed up", "faster", "memory leak", "bottleneck"
**Recommended:** `performance-optimizer`
- Performance profiling
- Database query optimization
- Memory/CPU optimization

### 🔧 Refactoring & Code Quality
**Triggers:** "refactor", "clean up", "improve code", "technical debt", "code smell", "restructure"
**Recommended:** `refactoring-expert`
- Code quality improvements
- Design pattern implementation
- Technical debt reduction

### ✅ Testing & QA
**Triggers:** "test", "unit test", "integration test", "e2e", "testing strategy", "coverage"
**Recommended:** `test-engineer`
- Comprehensive test suite creation
- Test strategy design
- Coverage analysis

### 📚 Documentation
**Triggers:** "document", "docs", "README", "API docs", "comments", "explain code"
**Recommended:** `docs-writer`
- Auto-generated documentation
- API documentation
- Inline code comments

### 🌐 API Design
**Triggers:** "API", "REST", "GraphQL", "endpoint", "web service", "microservice"
**Recommended:** `api-designer`
- REST/GraphQL API design
- OpenAPI/Swagger specs
- API versioning strategy

### 🎨 Frontend Development
**Triggers:** "UI", "frontend", "React", "Vue", "component", "styling", "CSS", "responsive"
**Recommended:** `frontend-specialist`
- Component architecture
- State management
- Responsive design

### 🗄️ Database & Data
**Triggers:** "database", "SQL", "MongoDB", "schema", "migration", "query", "data model"
**Recommended:** `database-architect`
- Schema design
- Query optimization
- Migration strategies

### 🚀 DevOps & Infrastructure
**Triggers:** "deploy", "CI/CD", "Docker", "Kubernetes", "infrastructure", "pipeline", "AWS"
**Recommended:** `devops-engineer`
- Deployment automation
- Container orchestration
- Infrastructure as code

### 📱 Mobile Development
**Triggers:** "mobile", "iOS", "Android", "React Native", "Flutter", "app"
**Recommended:** `mobile-developer`
- Mobile-first architecture
- Platform-specific optimization
- Cross-platform strategies

### 🤖 AI/ML Integration
**Triggers:** "machine learning", "AI", "model", "neural network", "training", "prediction"
**Recommended:** `ml-engineer`
- ML pipeline design
- Model integration
- Data preprocessing

### 📊 Data Science & Analytics
**Triggers:** "analytics", "data science", "visualization", "dashboard", "metrics", "reporting"
**Recommended:** `data-scientist`
- Data analysis workflows
- Visualization strategies
- Statistical modeling

### 🔄 Architecture & System Design
**Triggers:** "architecture", "system design", "scalability", "distributed system", "microservices"
**Recommended:** `architect`
- System architecture design
- Scalability patterns
- Technology selection

### 🛠️ General Development
**Triggers:** Default for general coding tasks without specific specialization
**Recommended:** Use built-in `/brainstorm`, `/write`, `/execute` workflow
- No specialized subagent needed

## Auto-Recommendation Logic

When a task is received:

1. **Analyze task keywords** against trigger patterns
2. **Identify primary category** (can be multiple)
3. **Recommend top 1-3 subagents** based on relevance
4. **Present recommendation** with:
   - Why this subagent fits
   - What it will help with
   - Installation command if needed
5. **Ask user permission** before installing
6. **Proceed with task** using the subagent

## Example Output Format

```
📋 Task Analysis: [Brief description]

🎯 Recommended Subagent(s):
  1. debugging-specialist (Primary)
     → Advanced debugging workflows for complex errors
     → Root cause analysis

  2. test-engineer (Secondary)
     → Verify fix with comprehensive tests

💡 I'll install and use `debugging-specialist` to help troubleshoot this issue.
   Would you like me to proceed?

Installation: \plugin install debugging-specialist@awesome-claude-code-subagents
```

## Integration with CLAUDE.md

This advisor runs **BEFORE** the main decision tree:

```
User gives task
    │
    ▼
SUBAGENT ADVISOR (NEW!)
Analyze & Recommend
    │
    ▼
Is this a NEW PROJECT or FEATURE?
    │
[...rest of decision tree...]
```

## Non-Programmer Friendly Mode

For non-programmers, automatically:
- Explain what the subagent does in plain English
- Show expected outcomes
- Provide simple yes/no choice
- Handle installation automatically
- Guide through the entire process

## Memory Integration

After using a subagent successfully, log to memory:
```bash
historian 'subagents/usage' 'Used [subagent] for [task]' 'Result: [outcome]'
```

This builds a personalized history of which subagents work best for which tasks.
