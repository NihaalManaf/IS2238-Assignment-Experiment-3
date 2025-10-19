# Prompt Engineering Guide for AI-Generated Code

## 🎯 Quick Reference

Based on the IS2238 experiment comparing 5 prompt engineering techniques, this guide provides actionable templates for getting high-quality code from AI assistants.

---

## 📋 The Optimal Prompt Template

```markdown
You are a [ROLE] with [EXPERIENCE].

<[DESIGN_SECTION]>
Provide a detailed [ARCHITECTURE_ARTIFACT] for [PROJECT_DESCRIPTION].
The [PROJECT] should [KEY_FEATURES].
</[DESIGN_SECTION]>

Requirements:

- [FEATURE_1]
- [FEATURE_2]
- [FEATURE_3]
- [FEATURE_N]

Constraints:

- [CONSTRAINT_1]
- [CONSTRAINT_2]
- [CONSTRAINT_N]

Edge Cases to Handle:

- [EDGE_CASE_1]
- [EDGE_CASE_2]
- [EDGE_CASE_N]

Quality Standards:
The code must be:

- [STANDARD_1]
- [STANDARD_2]
- [STANDARD_N]

<[CODE_SECTION]>
Generate [DELIVERABLES] implementing the above design.
Include [ADDITIONAL_ARTIFACTS].
</[CODE_SECTION]>
```

---

## 🏆 Real Example: Task Manager (95/100 Score)

```markdown
You are a senior Python backend engineer with 10 years of experience.

<UML>
Provide a detailed UML class diagram and data flow description for a simple Task Manager App for two users.  
The app runs from the command line in a single Python file using Python 3.11 and only standard library.  
Features include: add, edit, delete, mark tasks as complete; assign due dates (YYYY-MM-DD) and priorities; view tasks per user.
</UML>

Requirements:

- Command-line interface
- Add, edit, delete tasks
- Mark tasks as complete/incomplete
- Assign due dates (YYYY-MM-DD format)
- Set priorities (High, Medium, Low)
- View tasks per user
- Data persistence

Constraints:

- Single Python file
- Python 3.11+ only
- Standard library only
- No external dependencies

Edge Cases to Handle:

- Invalid date formats
- Empty task titles
- Duplicate task names
- Invalid priority values
- Missing user selection
- File I/O errors

Quality Standards:
The code must be:

- Production-ready
- Well-structured with clear separation of concerns
- Fully documented with docstrings
- Comprehensive error handling
- Type-hinted throughout
- Include test suite

<Code>
Generate the production-ready Python code implementing the above design.  
Include tests and comprehensive documentation.
</Code>
```

**Result**: 911 lines, 6 classes, 52 functions, 95/100 quality score

---

## 📊 Prompt Complexity Levels

### Level 1: Basic (68% Quality)

**Use for**: Quick prototypes, throwaway code

```markdown
Build a [PROJECT] that does [BASIC_FEATURES].
```

**Example**:

```markdown
Build a Task Manager App for two users in a single Python file.
```

**Pros**: Fast to write (1 minute)  
**Cons**: Minimal validation, basic features, no tests

---

### Level 2: Contextual (65% Quality) ⚠️

**Use for**: When you need specific environment details

```markdown
You are building a [PROJECT] using [TECHNOLOGY].
The app should [FEATURES].
Store data using [DATA_STRUCTURE].
```

**Example**:

```markdown
You are building a Task Manager App using Python 3.11.
Store all data in memory using dictionaries.
```

**Pros**: Better organization  
**Cons**: Can cause feature regression without explicit requirements

**⚠️ Warning**: Context alone can lead to worse results than baseline!

---

### Level 3: Constrained (78% Quality)

**Use for**: Production code with specific requirements

```markdown
Build a [PROJECT] with [FEATURES].

Requirements:

- [REQ_1]
- [REQ_2]

Constraints:

- [CONSTRAINT_1]
- [CONSTRAINT_2]

Edge Cases:

- [EDGE_1]
- [EDGE_2]
```

**Example**:

```markdown
Build a Task Manager App.

Requirements:

- Add, edit, delete tasks
- Due dates and priorities
- View tasks per user

Constraints:

- Single file
- No external dependencies

Edge Cases:

- Handle invalid dates
- Prevent duplicate titles
- Validate priority values
```

**Pros**: Comprehensive validation, good error handling  
**Cons**: Still missing tests and documentation

---

### Level 4: Professional (88% Quality)

**Use for**: Production-ready code with tests

```markdown
You are a senior [DOMAIN] engineer with [YEARS] years of experience.
Write production-ready code for [PROJECT].

[PROJECT] should support:

- [FEATURE_1]
- [FEATURE_2]

Ensure the code is:

- Well-structured
- Fully tested
- Well-documented
- Error-handled
```

**Example**:

```markdown
You are a senior Python backend engineer with 10 years of experience.
Write production-ready code for a Task Manager App.

The app should support:

- Adding, editing, deleting tasks
- Due dates and priorities
- Multi-user support

Ensure the code is:

- Well-structured with clear separation
- Fully functional and bug-free
- Readable and well-commented
- Has comprehensive error handling
```

**Pros**: Professional quality, includes tests and docs  
**Cons**: No architectural documentation

---

### Level 5: Enterprise (95% Quality) ⭐

**Use for**: Production systems requiring full documentation

```markdown
You are a senior [DOMAIN] engineer with [YEARS] years of experience.

<[DESIGN]>
Provide detailed [ARCHITECTURE] for [PROJECT].
Include [DIAGRAMS] and [DOCUMENTATION].
</[DESIGN]>

Requirements: [DETAILED_REQUIREMENTS]
Constraints: [DETAILED_CONSTRAINTS]
Edge Cases: [DETAILED_EDGE_CASES]
Quality Standards: [DETAILED_STANDARDS]

<[CODE]>
Generate production-ready code implementing the above design.
Include [TESTS] and [DOCUMENTATION].
</[CODE]>
```

**Pros**: Enterprise quality, full documentation, comprehensive features  
**Cons**: Takes longer to write prompt (12 minutes)

**ROI**: 27% better quality for 12x time investment = 2.25% improvement per minute

---

## 🎓 Component Breakdown

### 1. Role Assignment

**Impact**: +10% quality improvement

```markdown
You are a [ROLE] with [EXPERIENCE].
```

**Examples**:

- `You are a senior Python backend engineer with 10 years of experience.`
- `You are an expert frontend developer specializing in React.`
- `You are a DevOps engineer with expertise in Kubernetes.`
- `You are a data scientist with 5 years of ML experience.`

**Why it works**: Triggers professional standards, best practices, and domain expertise.

---

### 2. Design-First Request

**Impact**: +7% quality improvement

```markdown
<UML>
Provide a detailed [ARTIFACT] for [PROJECT].
Include [DIAGRAMS] and [DESCRIPTIONS].
</UML>
```

**Examples**:

- `<UML>Provide a detailed class diagram and data flow description...</UML>`
- `<Architecture>Describe the system architecture and component interactions...</Architecture>`
- `<Design>Create a detailed design document with API specifications...</Design>`

**Why it works**: Forces architectural thinking before coding, leading to better structure.

---

### 3. Explicit Requirements

**Impact**: Essential for feature completeness

```markdown
Requirements:

- [FEATURE_1]: [DESCRIPTION]
- [FEATURE_2]: [DESCRIPTION]
- [FEATURE_N]: [DESCRIPTION]
```

**Example**:

```markdown
Requirements:

- User Authentication: Support login/logout with session management
- Data Persistence: Save data to JSON file with auto-save
- Input Validation: Validate all user inputs with clear error messages
- Multi-user Support: Isolate data between users
```

**Why it works**: Removes ambiguity, ensures all features are implemented.

---

### 4. Constraints & Limitations

**Impact**: Prevents over-engineering or wrong technology choices

```markdown
Constraints:

- [TECHNICAL_CONSTRAINT]
- [ARCHITECTURAL_CONSTRAINT]
- [DEPENDENCY_CONSTRAINT]
```

**Example**:

```markdown
Constraints:

- Single Python file implementation
- Python 3.11+ only
- Standard library only (no pip packages)
- Must run on Windows, Mac, and Linux
- File size under 1000 lines
```

**Why it works**: Guides technology choices and prevents scope creep.

---

### 5. Edge Cases

**Impact**: +13% improvement in robustness

```markdown
Edge Cases to Handle:

- [EDGE_CASE_1]
- [EDGE_CASE_2]
- [EDGE_CASE_N]
```

**Example**:

```markdown
Edge Cases to Handle:

- Empty string inputs
- Invalid date formats (handle gracefully)
- Duplicate entries (prevent or warn)
- File not found errors
- Concurrent access issues
- Memory limits exceeded
- Network timeouts
```

**Why it works**: AI won't think of all edge cases unless explicitly told.

---

### 6. Quality Standards

**Impact**: Ensures professional output

```markdown
Quality Standards:
The code must be:

- [STANDARD_1]
- [STANDARD_2]
- [STANDARD_N]
```

**Example**:

```markdown
Quality Standards:
The code must be:

- Production-ready with no TODOs or placeholders
- Fully documented with docstrings for all functions
- Type-hinted throughout (PEP 484)
- Include comprehensive error handling
- Follow PEP 8 style guidelines
- Include unit tests with >80% coverage
- Include integration tests for main workflows
- Include README with usage examples
```

**Why it works**: Sets expectations for code quality and completeness.

---

### 7. Structured Tags

**Impact**: Improves clarity and organization

```markdown
<[SECTION_NAME]>
[CONTENT]
</[SECTION_NAME]>
```

**Common Tags**:

- `<UML>...</UML>` - Design diagrams
- `<Architecture>...</Architecture>` - System design
- `<Code>...</Code>` - Implementation
- `<Tests>...</Tests>` - Test requirements
- `<Documentation>...</Documentation>` - Doc requirements

**Why it works**: Clearly separates concerns and guides AI's response structure.

---

## 🚫 Common Mistakes to Avoid

### ❌ Mistake 1: Vague Requirements

```markdown
Build a good task manager.
```

**Problem**: "Good" is subjective. No specific features defined.

**Fix**:

```markdown
Build a task manager with:

- CRUD operations for tasks
- Due dates and priorities
- Multi-user support
- Data persistence
```

---

### ❌ Mistake 2: Context Without Requirements

```markdown
You are building a task manager using Python.
Use modern best practices.
```

**Problem**: Can cause feature regression. No specific features or constraints.

**Fix**: Always pair context with explicit requirements and constraints.

---

### ❌ Mistake 3: Assuming Edge Cases

```markdown
Build a task manager with proper error handling.
```

**Problem**: "Proper" is ambiguous. AI might miss important edge cases.

**Fix**:

```markdown
Handle these edge cases:

- Invalid date formats
- Empty task titles
- Duplicate task names
- File I/O errors
```

---

### ❌ Mistake 4: No Quality Standards

```markdown
Build a task manager.
```

**Problem**: No guidance on code quality, testing, or documentation.

**Fix**:

```markdown
The code must be:

- Production-ready
- Fully tested
- Well-documented
- Type-hinted
```

---

### ❌ Mistake 5: Missing Role Assignment

```markdown
Build a task manager app.
```

**Problem**: Gets generic code without professional standards.

**Fix**:

```markdown
You are a senior software engineer with 10 years of experience.
Build a production-ready task manager app.
```

---

## 📈 Progressive Enhancement Strategy

Start simple and add complexity as needed:

### Step 1: Basic Prompt

```markdown
Build a [PROJECT] that does [FEATURES].
```

**Test**: Does it work? Does it have basic features?

---

### Step 2: Add Constraints

```markdown
Build a [PROJECT] that does [FEATURES].

Constraints:

- [CONSTRAINT_1]
- [CONSTRAINT_2]
```

**Test**: Does it follow constraints? Are edge cases handled?

---

### Step 3: Add Role

```markdown
You are a senior [ROLE] with [EXPERIENCE].
Build a [PROJECT] that does [FEATURES].

Constraints: [...]
```

**Test**: Is code quality professional? Are there tests?

---

### Step 4: Add Design-First

```markdown
You are a senior [ROLE] with [EXPERIENCE].

<UML>
Provide detailed design for [PROJECT].
</UML>

<Code>
Implement the above design.
</Code>
```

**Test**: Is architecture well-designed? Is it documented?

---

## 🎯 Domain-Specific Templates

### Web Application

```markdown
You are a senior full-stack engineer with 8 years of experience.

<Architecture>
Design a [WEB_APP] with:
- Frontend: [FRAMEWORK]
- Backend: [FRAMEWORK]
- Database: [DATABASE]
- API: [REST/GraphQL]
</Architecture>

Requirements:

- User authentication and authorization
- CRUD operations for [ENTITIES]
- Real-time updates using [WEBSOCKETS/POLLING]
- Responsive design for mobile and desktop

Constraints:

- Use [LANGUAGE] version [VERSION]
- Follow [FRAMEWORK] best practices
- Implement proper security (CSRF, XSS protection)

<Code>
Generate production-ready code with:
- Proper project structure
- Unit and integration tests
- API documentation
- Deployment configuration
</Code>
```

---

### Data Processing Pipeline

```markdown
You are a senior data engineer with 10 years of experience.

<Architecture>
Design a data pipeline that:
- Ingests data from [SOURCES]
- Processes data using [PROCESSING_LOGIC]
- Stores results in [DESTINATION]
</Architecture>

Requirements:

- Handle [DATA_VOLUME] per day
- Process data in [BATCH/STREAMING] mode
- Implement error handling and retry logic
- Monitor pipeline health

Constraints:

- Use Python 3.11+ with standard library
- Minimize external dependencies
- Run on [INFRASTRUCTURE]

<Code>
Generate production-ready code with:
- Modular pipeline components
- Comprehensive error handling
- Unit tests for each component
- Configuration management
- Logging and monitoring
</Code>
```

---

### Machine Learning Model

```markdown
You are a senior ML engineer with 7 years of experience.

<Design>
Design an ML solution for [PROBLEM]:
- Data preprocessing pipeline
- Model architecture
- Training strategy
- Evaluation metrics
- Deployment approach
</Design>

Requirements:

- Achieve [METRIC] of at least [TARGET]
- Handle [DATA_CHARACTERISTICS]
- Support [INFERENCE_REQUIREMENTS]

Constraints:

- Use [FRAMEWORK] (TensorFlow/PyTorch/scikit-learn)
- Model size under [SIZE_LIMIT]
- Inference time under [TIME_LIMIT]

<Code>
Generate production-ready code with:
- Data preprocessing scripts
- Model training code
- Evaluation scripts
- Inference API
- Model versioning
- Comprehensive tests
</Code>
```

---

## 💡 Pro Tips

### Tip 1: Iterate on Prompts

Don't expect perfection on first try. Refine your prompt based on results:

1. Start with Level 3 (Constrained)
2. Review output
3. Add missing requirements
4. Specify overlooked edge cases
5. Refine quality standards

### Tip 2: Save Successful Prompts

Build a personal library of prompts that worked well for different scenarios.

### Tip 3: Be Specific About "Production-Ready"

Define what production-ready means for your context:

- Tests? What coverage?
- Documentation? What format?
- Error handling? What level?
- Performance? What metrics?

### Tip 4: Request Examples

```markdown
Include usage examples in the documentation showing:

- Basic usage
- Advanced features
- Error handling
- Edge cases
```

### Tip 5: Specify Code Style

```markdown
Follow these style guidelines:

- PEP 8 for Python
- ESLint rules for JavaScript
- Google style guide for Java
- Include type hints
- Maximum line length: 100 characters
```

---

## 📊 Prompt ROI Calculator

| Prompt Level           | Time to Write | Quality Score | ROI (Quality/Time) |
| ---------------------- | ------------- | ------------- | ------------------ |
| Level 1 (Basic)        | 1 min         | 68%           | 68%/min            |
| Level 2 (Context)      | 2 min         | 65%           | 32.5%/min ⚠️       |
| Level 3 (Constrained)  | 5 min         | 78%           | 15.6%/min          |
| Level 4 (Professional) | 8 min         | 88%           | 11%/min            |
| Level 5 (Enterprise)   | 12 min        | 95%           | 7.9%/min           |

**Insight**: While ROI decreases with complexity, absolute quality increases significantly. Choose based on project needs:

- **Prototype**: Level 1-3
- **Production**: Level 4-5
- **Enterprise**: Level 5

---

## 🎓 Learning Path

### Beginner

1. Start with Level 1 prompts
2. Add explicit requirements (Level 3)
3. Practice identifying edge cases

### Intermediate

1. Master Level 3 prompts
2. Add role assignment (Level 4)
3. Request tests and documentation

### Advanced

1. Use design-first approach (Level 5)
2. Create domain-specific templates
3. Build prompt library for reuse

---

## 📚 Additional Resources

- **Full Experiment**: See `README.md` for complete analysis
- **Visual Summary**: See `EXPERIMENT_SUMMARY.md` for charts
- **Example Prompts**: See `Prompt1-5_cursor_chat.md` for real examples
- **Code Samples**: Check branches `Prompt1-5` for implementations

---

## 🎯 Quick Decision Tree

```
Need AI-generated code?
│
├─ Quick prototype?
│  └─ Use Level 1-3
│
├─ Production code?
│  ├─ Simple feature?
│  │  └─ Use Level 3-4
│  │
│  └─ Complex system?
│     └─ Use Level 4-5
│
└─ Enterprise system?
   └─ Use Level 5
```

---

## ✅ Prompt Checklist

Before submitting your prompt, verify:

- [ ] Role assigned (for professional code)
- [ ] Design requested first (for complex systems)
- [ ] All requirements explicitly listed
- [ ] Constraints clearly defined
- [ ] Edge cases enumerated
- [ ] Quality standards specified
- [ ] Deliverables requested (code, tests, docs)
- [ ] Structured tags used (for clarity)

---

**Remember**: The quality of AI-generated code is directly proportional to the quality of your prompt. Invest time in prompt engineering—it pays dividends in code quality.

---

**Last Updated**: October 19, 2025  
**Based on**: IS2238 Prompt Engineering Experiment  
**AI Model Tested**: Claude Sonnet 4.5 (via Cursor)
