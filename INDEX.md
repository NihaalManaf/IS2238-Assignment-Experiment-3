# Prompt Engineering Experiment - Documentation Index

## 📚 Navigation Guide

This repository contains a comprehensive experiment on prompt engineering techniques and their impact on AI-generated code quality. Use this index to navigate the documentation.

---

## 🎯 Start Here

### For Quick Overview

**→ [EXPERIMENT_SUMMARY.md](EXPERIMENT_SUMMARY.md)**

- Visual charts and graphs
- Quick stats comparison
- Key insights at a glance
- 5-minute read

### For Complete Analysis

**→ [README.md](README.md)**

- Full experimental methodology
- Detailed results and analysis
- Quantitative and qualitative metrics
- Scoring rubrics
- 15-minute read

### For Practical Application

**→ [PROMPT_ENGINEERING_GUIDE.md](PROMPT_ENGINEERING_GUIDE.md)**

- Ready-to-use prompt templates
- Domain-specific examples
- Pro tips and best practices
- Common mistakes to avoid
- 10-minute read

---

## 📊 Experiment Overview

### What Was Tested?

Five progressively enhanced prompt engineering techniques:

1. **Prompt 1**: Baseline (minimal requirements)
2. **Prompt 2**: + Contextual augmentation
3. **Prompt 3**: + Specification & constraints
4. **Prompt 4**: + Role prompting
5. **Prompt 5**: + UML/structured design

### What Was Measured?

- Code quality (lines, structure, documentation)
- Functionality (features, completeness)
- Robustness (error handling, edge cases)
- Overall quality score (/100)

### Key Result

**251% improvement** in code complexity and **27% improvement** in quality score from baseline to optimal prompt.

---

## 📁 Repository Structure

```
testing MCP/
│
├── 📄 INDEX.md (this file)
│   └── Navigation guide for all documentation
│
├── 📊 EXPERIMENT_SUMMARY.md
│   ├── Visual charts and graphs
│   ├── Quick statistics
│   └── Key insights
│
├── 📖 README.md
│   ├── Complete experimental analysis
│   ├── Detailed methodology
│   ├── Quantitative metrics
│   ├── Qualitative assessment
│   └── Comprehensive findings
│
├── 🎓 PROMPT_ENGINEERING_GUIDE.md
│   ├── Prompt templates
│   ├── Best practices
│   ├── Domain-specific examples
│   └── Common mistakes
│
├── 💬 Prompt Transcripts
│   ├── Prompt1_cursor_chat.md (Baseline)
│   ├── Prompt2_cursor_chat.md (Context)
│   ├── Prompt3_cursor_chat.md (Constraints)
│   ├── Prompt4_cursor_chat.md (Role)
│   └── Prompt5_cursor_chat.md (UML)
│
└── 🌿 Git Branches (Code Implementations)
    ├── Prompt1/ (363 LOC, 2 classes, 18 functions)
    ├── Prompt2/ (321 LOC, 2 classes, 15 functions)
    ├── Prompt3/ (380 LOC, 3 classes, 20 functions)
    ├── Prompt4/ (538 LOC, 4 classes, 26 functions)
    └── Prompt5/ (911 LOC, 6 classes, 52 functions)
```

---

## 🎯 Quick Links by Use Case

### I want to...

#### Understand the experiment

→ Start with [EXPERIMENT_SUMMARY.md](EXPERIMENT_SUMMARY.md)  
→ Then read [README.md](README.md) for details

#### Learn prompt engineering

→ Read [PROMPT_ENGINEERING_GUIDE.md](PROMPT_ENGINEERING_GUIDE.md)  
→ Review prompt transcripts for examples

#### See the actual prompts used

→ Check `Prompt1-5_cursor_chat.md` files  
→ Compare progression from simple to complex

#### Examine the generated code

→ Checkout branches: `git checkout Prompt1` through `Prompt5`  
→ Compare implementations side-by-side

#### Apply findings to my work

→ Use templates in [PROMPT_ENGINEERING_GUIDE.md](PROMPT_ENGINEERING_GUIDE.md)  
→ Follow the "Optimal Prompt Template"

#### Cite this work

→ See [Citation](#-citation) section below

---

## 📈 Key Findings Summary

### Quantitative Results

| Metric            | Prompt 1 | Prompt 5 | Growth    |
| ----------------- | -------- | -------- | --------- |
| **Quality Score** | 68/100   | 95/100   | **+27%**  |
| **Lines of Code** | 363      | 911      | **+151%** |
| **Functions**     | 18       | 52       | **+189%** |
| **Classes**       | 2        | 6        | **+200%** |
| **Test Coverage** | 0%       | 100%     | **∞**     |

### Qualitative Insights

1. **Role prompting is transformative** (+10% quality)

   - Triggers professional standards
   - Includes tests and documentation
   - Uses best practices

2. **Design-first approach yields best results** (+7% quality)

   - Better architecture
   - Comprehensive features
   - Complete documentation

3. **Context alone can cause regression** (-3% quality)

   - Lost data persistence feature
   - Vague requirements lead to omissions

4. **Explicit constraints dramatically improve robustness** (+13% quality)
   - Comprehensive validation
   - Edge case handling
   - Better error messages

---

## 🎓 Learning Path

### Beginner (30 minutes)

1. Read [EXPERIMENT_SUMMARY.md](EXPERIMENT_SUMMARY.md) (5 min)
2. Review Prompt 1 vs Prompt 5 comparison (10 min)
3. Try Level 1-3 templates from guide (15 min)

### Intermediate (1 hour)

1. Read full [README.md](README.md) (15 min)
2. Study all 5 prompt transcripts (20 min)
3. Practice Level 3-4 templates (25 min)

### Advanced (2 hours)

1. Deep dive into [README.md](README.md) (20 min)
2. Analyze code in all 5 branches (40 min)
3. Create custom templates for your domain (60 min)

---

## 🔬 Experimental Methodology

### Independent Variable

Prompt engineering technique level (1-5)

### Dependent Variables

- Code quality metrics (LOC, functions, classes)
- Functionality completeness
- Error handling robustness
- Overall quality score

### Constants

- AI model: Claude Sonnet 4.5 (via Cursor)
- Task: Build a Task Manager App
- Language: Python 3.11+
- Starting point: Empty file each time

### Evaluation Rubric

- Functionality & Correctness (25 pts)
- Completeness & Adherence (25 pts)
- Code Quality & Readability (25 pts)
- Error Handling & Robustness (25 pts)

---

## 📊 Results at a Glance

### Quality Score Progression

```
Prompt 1: ████████████████████░░░░░ 68/100
Prompt 2: ████████████████░░░░░░░░░ 65/100 ⚠️
Prompt 3: ███████████████████░░░░░░ 78/100
Prompt 4: ██████████████████████░░░ 88/100
Prompt 5: ███████████████████████░░ 95/100 ⭐
```

### Feature Completeness

```
Basic CRUD:          ✅ ✅ ✅ ✅ ✅
Data Persistence:    ✅ ❌ ❌ ✅ ✅
Input Validation:    ⚠️ ⚠️ ✅ ✅ ✅
Error Handling:      ⚠️ ⚠️ ✅ ✅ ✅
Test Suite:          ❌ ❌ ❌ ✅ ✅
Documentation:       ❌ ❌ ❌ ✅ ✅✅
UML Diagrams:        ❌ ❌ ❌ ❌ ✅
```

---

## 🎯 Practical Recommendations

### For Quick Prototypes

Use **Prompt 3** approach (Constrained):

- Time: 5 minutes
- Quality: 78/100
- Features: Core functionality with validation

### For Production Code

Use **Prompt 4** approach (Professional):

- Time: 8 minutes
- Quality: 88/100
- Features: Tests, documentation, best practices

### For Enterprise Systems

Use **Prompt 5** approach (Enterprise):

- Time: 12 minutes
- Quality: 95/100
- Features: Full documentation, UML, comprehensive features

---

## 🛠️ How to Use This Repository

### To Reproduce the Experiment

```bash
# Clone the repository
git clone <repository-url>
cd "testing MCP"

# View each implementation
for branch in Prompt1 Prompt2 Prompt3 Prompt4 Prompt5; do
    echo "=== $branch ==="
    git checkout $branch
    python3 task_manager.py
done

# Run tests (Prompt4 and Prompt5 only)
git checkout Prompt4
python3 test_task_manager.py

git checkout Prompt5
python3 test_task_manager.py
```

### To Apply Findings

1. Read [PROMPT_ENGINEERING_GUIDE.md](PROMPT_ENGINEERING_GUIDE.md)
2. Choose appropriate prompt level for your use case
3. Customize template for your domain
4. Test and iterate

---

## 📖 Detailed Documentation

### Main Documents

| Document                                                   | Purpose           | Length | Audience              |
| ---------------------------------------------------------- | ----------------- | ------ | --------------------- |
| [EXPERIMENT_SUMMARY.md](EXPERIMENT_SUMMARY.md)             | Visual overview   | 5 min  | Everyone              |
| [README.md](README.md)                                     | Complete analysis | 15 min | Researchers, students |
| [PROMPT_ENGINEERING_GUIDE.md](PROMPT_ENGINEERING_GUIDE.md) | Practical guide   | 10 min | Developers            |
| INDEX.md (this file)                                       | Navigation        | 3 min  | Everyone              |

### Prompt Transcripts

| File                   | Technique   | Quality | Key Feature            |
| ---------------------- | ----------- | ------- | ---------------------- |
| Prompt1_cursor_chat.md | Baseline    | 68%     | Minimal requirements   |
| Prompt2_cursor_chat.md | Context     | 65%     | Environment details    |
| Prompt3_cursor_chat.md | Constraints | 78%     | Edge cases             |
| Prompt4_cursor_chat.md | Role        | 88%     | Professional standards |
| Prompt5_cursor_chat.md | UML         | 95%     | Design-first           |

### Code Implementations

| Branch  | LOC | Classes | Functions | Score |
| ------- | --- | ------- | --------- | ----- |
| Prompt1 | 363 | 2       | 18        | 68%   |
| Prompt2 | 321 | 2       | 15        | 65%   |
| Prompt3 | 380 | 3       | 20        | 78%   |
| Prompt4 | 538 | 4       | 26        | 88%   |
| Prompt5 | 911 | 6       | 52        | 95%   |

---

## 💡 Key Takeaways

### The Winning Formula

```
1. Assign Expert Role
   ↓
2. Request Design First
   ↓
3. Specify Requirements
   ↓
4. Define Constraints
   ↓
5. List Edge Cases
   ↓
6. Set Quality Standards
   ↓
7. Request Deliverables
   ↓
= 95/100 Quality Score
```

### Critical Insights

1. **Prompt engineering is not optional** for quality code
2. **Role assignment triggers professional standards** (+10%)
3. **Design-first approach yields superior results** (+7%)
4. **Context without requirements causes regression** (-3%)
5. **Explicit constraints improve robustness** (+13%)

### ROI Analysis

- **Time investment**: 12 minutes for optimal prompt
- **Quality improvement**: +27% over baseline
- **Code complexity**: +251% more comprehensive
- **Feature completeness**: +189% more functionality

**Conclusion**: 12 minutes of prompt engineering yields enterprise-quality code.

---

## 🎓 Educational Use

### For Students

- Learn prompt engineering systematically
- Understand impact of prompt quality on output
- Practice with provided templates
- Compare different approaches

### For Instructors

- Use as case study in AI-assisted development
- Demonstrate prompt engineering best practices
- Show quantitative impact of technique
- Provide hands-on examples

### For Researchers

- Reproducible experiment methodology
- Quantitative and qualitative metrics
- Controlled comparison study
- Statistical analysis included

---

## 📚 Citation

If you use this work in your research or teaching, please cite:

```
Manaf, N. (2025). Prompt Engineering Experiment: Impact of Prompt
Engineering Techniques on AI-Generated Code Quality. IS2238 Software
Engineering with AI, October 2025.
```

BibTeX:

```bibtex
@techreport{manaf2025prompt,
  title={Prompt Engineering Experiment: Impact of Prompt Engineering
         Techniques on AI-Generated Code Quality},
  author={Manaf, Nihaal},
  year={2025},
  month={October},
  institution={IS2238 Software Engineering with AI}
}
```

---

## 🤝 Contributing

This is an educational experiment. If you'd like to:

- Replicate with different AI models
- Test with different programming languages
- Extend to other domains
- Improve the methodology

Please feel free to fork and extend this work.

---

## 📧 Contact

**Author**: Nihaal Manaf  
**Course**: IS2238 - Software Engineering with AI  
**Date**: October 19, 2025

---

## 📜 License

This experiment and its results are provided for educational purposes as part of IS2238 coursework.

---

## 🔗 Quick Access

### Documents

- [📊 Visual Summary](EXPERIMENT_SUMMARY.md)
- [📖 Full Analysis](README.md)
- [🎓 Practical Guide](PROMPT_ENGINEERING_GUIDE.md)

### Prompts

- [Prompt 1: Baseline](Prompt1_cursor_chat.md)
- [Prompt 2: Context](Prompt2_cursor_chat.md)
- [Prompt 3: Constraints](Prompt3_cursor_chat.md)
- [Prompt 4: Role](Prompt4_cursor_chat.md)
- [Prompt 5: UML](Prompt5_cursor_chat.md)

### Code

```bash
git checkout Prompt1  # Baseline
git checkout Prompt2  # Context
git checkout Prompt3  # Constraints
git checkout Prompt4  # Role
git checkout Prompt5  # UML
```

---

**Remember**: The quality of AI-generated code is directly proportional to the quality of your prompt. Invest time in prompt engineering—it pays dividends in code quality.

---

_Last Updated: October 19, 2025_  
_Experiment conducted using Claude Sonnet 4.5 via Cursor IDE_
