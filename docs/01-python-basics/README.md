# Python Basics - Complete Guide

Welcome to Python fundamentals! This is your starting point for mastering Python.

## 📖 What You'll Learn

In this module, you'll master:

1. **Python Interpreter & Execution**
2. **Variables and Data Types**
3. **Operators (Arithmetic, Logical, Comparison)**
4. **Strings and String Operations**
5. **Type Conversion**
6. **Lists, Tuples, Sets, Dictionaries**
7. **Conditional Statements (if/elif/else)**
8. **Loops (for, while, break, continue)**
9. **Functions and Parameters**
10. **Variable Scope (Local, Global, Nonlocal)**
11. **Modules and Imports**
12. **Exception Handling (try/except/finally)**
13. **File I/O Operations**
14. **JSON and CSV Handling**
15. **Debugging and Logging**

## 🎯 Learning Approach

Each lesson follows this structure:

### 1. Concept Explanation
A clear, simple explanation of what the concept is and why it matters.

### 2. Syntax & Examples
Runnable code examples you can copy and execute immediately.

### 3. Code Walkthrough
Line-by-line explanation of how the code works.

### 4. Common Mistakes
Errors beginners make and how to avoid them.

### 5. Practical Exercise
A hands-on task for you to implement.

### 6. Solution
A separate file with the solution.

## ✅ Getting Started

### 1. Verify Your Python Installation

```powershell
python --version
python -c "import sys; print(sys.version)"
```

### 2. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 3. Navigate to Examples

All example code is in the `examples/` directory. Run any example with:

```bash
python examples/01_hello_world.py
```

## 📚 Lesson Order

Work through the lessons in order:

1. **[00 - Python Interpreter](00_interpreter.md)** - How Python works
2. **[01 - Variables and Data Types](01_variables_and_types.md)** - Variables, int, float, bool, str
3. **[02 - Operators](02_operators.md)** - Arithmetic, comparison, logical operators
4. **[03 - Strings](03_strings.md)** - String operations, formatting, methods
5. **[04 - Lists and Tuples](04_lists_and_tuples.md)** - Sequences, indexing, slicing
6. **[05 - Dictionaries and Sets](05_dictionaries_and_sets.md)** - Key-value pairs, unique items
7. **[06 - Conditions](06_conditions.md)** - if, elif, else, ternary operators
8. **[07 - Loops](07_loops.md)** - for, while, break, continue, else
9. **[08 - Functions](08_functions.md)** - Definition, parameters, return values
10. **[09 - Scope](09_scope.md)** - Local, global, nonlocal variables
11. **[10 - Modules and Imports](10_modules.md)** - import, from, packages
12. **[11 - Exception Handling](11_exceptions.md)** - try, except, finally, raise
13. **[12 - File I/O](12_file_io.md)** - Reading, writing, pathlib
14. **[13 - JSON and CSV](13_json_csv.md)** - Working with data formats
15. **[14 - Debugging](14_debugging.md)** - pdb, print debugging, assertions

## 🏃 Quick Start Example

Create a file `hello.py`:

```python
# This is a comment
name = input("What's your name? ")
print(f"Hello, {name}! Welcome to Python.")
```

Run it:

```bash
python hello.py
```

## 💡 Tips for Success

✅ **Type out the code** - Don't copy-paste. Typing builds muscle memory.

✅ **Run every example** - Execute the code to see it work.

✅ **Modify the code** - Change values and see what happens.

✅ **Try all exercises** - Don't look at solutions immediately.

✅ **Use the Python REPL** - Test quick ideas with `python` command

✅ **Read error messages** - They tell you what's wrong.

✅ **Experiment** - Try things that might break—that's how you learn.

## 🐍 The Python REPL (Interactive Mode)

The Python REPL is your playground. Type `python` to enter interactive mode:

```
C:\Users\Administrator\Desktop\Python-Django> python
Python 3.11.2 (main, Feb 16 2023, 12:48:08) [MSC v.1916 64 bit (AMD64)]
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 5
>>> y = 3
>>> x + y
8
>>> x * y
15
>>> 
```

Exit with `exit()` or Ctrl+Z (Windows) / Ctrl+D (Linux/macOS).

## 📁 Files in This Section

```
docs/01-python-basics/
├── README.md                    # This file
├── 00_interpreter.md           # How Python works
├── 01_variables_and_types.md   # Variables and data types
├── 02_operators.md             # All operators
├── 03_strings.md               # String operations
├── 04_lists_and_tuples.md      # Sequences
├── 05_dictionaries_and_sets.md # Dictionaries and sets
├── 06_conditions.md            # if/elif/else
├── 07_loops.md                 # for and while
├── 08_functions.md             # Function definition
├── 09_scope.md                 # Variable scope
├── 10_modules.md               # Imports and modules
├── 11_exceptions.md            # Exception handling
├── 12_file_io.md               # File operations
├── 13_json_csv.md              # JSON and CSV
└── 14_debugging.md             # Debugging techniques
```

## 🎓 Learning Timeline

- **Lesson 1-2**: 1 day (interpreter + variables)
- **Lesson 3-5**: 2 days (operators, strings, collections)
- **Lesson 6-9**: 3 days (conditions, loops, functions)
- **Lesson 10-14**: 2 days (scope, modules, exceptions, files)

**Total**: 1 week to complete all lessons

## 🔍 How to Use Each Lesson

1. **Read the concept** - Understand what and why
2. **Read the example** - See how it works
3. **Run the example** - Execute in your terminal
4. **Trace the code** - Understand each line
5. **Do the exercise** - Implement it yourself
6. **Check the solution** - Compare with official answer
7. **Modify and experiment** - Break it, fix it, learn

## ✨ Start Here

👉 **Begin with [Lesson 00: Python Interpreter](00_interpreter.md)**

Then progress to Lesson 01, 02, and so on in order.

## 🆘 If You Get Stuck

1. **Re-read the concept** - Maybe something wasn't clear
2. **Look at the example again** - Try running it step-by-step
3. **Check the common mistakes** - Your issue might be listed
4. **Review the hints** - Don't jump to the solution
5. **Try the REPL** - Test your understanding interactively
6. **Experiment** - Modify the code to understand it

## 📊 Your Progress

Mark off each lesson as you complete it:

- [ ] Lesson 00: Python Interpreter
- [ ] Lesson 01: Variables and Data Types
- [ ] Lesson 02: Operators
- [ ] Lesson 03: Strings
- [ ] Lesson 04: Lists and Tuples
- [ ] Lesson 05: Dictionaries and Sets
- [ ] Lesson 06: Conditions
- [ ] Lesson 07: Loops
- [ ] Lesson 08: Functions
- [ ] Lesson 09: Scope
- [ ] Lesson 10: Modules and Imports
- [ ] Lesson 11: Exception Handling
- [ ] Lesson 12: File I/O
- [ ] Lesson 13: JSON and CSV
- [ ] Lesson 14: Debugging

## 🎯 Next Steps

After completing all Python basics lessons:

1. Do all the exercises in `exercises/`
2. Run tests with `pytest exercises/`
3. Review the solutions
4. Move to **Python Intermediate** in `docs/02-python-intermediate/`

---

**Ready to start?** → [Lesson 00: Python Interpreter](00_interpreter.md)
