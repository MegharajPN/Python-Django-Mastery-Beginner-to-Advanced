# Lesson 00: How Python Works - The Interpreter

## 📖 What is the Python Interpreter?

The **Python interpreter** is a program that reads your Python code and executes it.

Think of it like this:
- You write instructions in Python
- The interpreter reads those instructions
- The interpreter converts them to machine code
- Your computer executes them

## 🔄 Two Ways to Run Python

### 1. Script Mode (File-based)

Write code in a `.py` file and run it:

```bash
python my_script.py
```

**Example:** File `hello.py`
```python
print("Hello, Python!")
```

Run it:
```bash
python hello.py
```

Output:
```
Hello, Python!
```

### 2. Interactive Mode (REPL)

REPL = **Read-Eval-Print Loop**

Start interactive mode:
```bash
python
```

You get a `>>>` prompt. Type Python code directly:

```
>>> x = 5
>>> print(x)
5
>>> x + 3
8
>>> exit()
```

## 🎯 How Python Executes Code

1. **Lexical Analysis**: Python reads your code character by character
2. **Parsing**: Creates a structure (syntax tree) from the code
3. **Compilation**: Converts code to bytecode (intermediate format)
4. **Execution**: Python Virtual Machine (PVM) executes the bytecode

## 📝 Your First Python Program

### Step 1: Create a file

Create `examples/00_hello_world.py`:

```python
# This is a comment
print("Hello, World!")
```

### Step 2: Run it

**Windows (PowerShell):**
```powershell
python examples/00_hello_world.py
```

**Linux/macOS (Terminal):**
```bash
python examples/00_hello_world.py
```

### Step 3: Expected Output

```
Hello, World!
```

## 📚 Python Files & Extensions

- `.py` - Regular Python file
- `.pyc` - Compiled Python bytecode (created automatically)
- `.pyx` - Cython file
- `.pyi` - Type stub file
- `.pyw` - Python script for Windows (runs without console)

## 🔍 Understanding `print()`

`print()` displays output to the console:

```python
print("Hello")           # Prints: Hello
print(5)                # Prints: 5
print("Hello", "World") # Prints: Hello World
print()                 # Prints empty line
```

## 💡 Comments in Python

Comments explain code. Python ignores them.

```python
# Single-line comment

"""
Multi-line comment
using triple quotes
"""

x = 5  # Comment at end of line
```

## 🎓 Common Mistakes

### ❌ Mistake 1: Forgetting to save before running
```
You edit the file but forget to save. The old version runs.
Solution: Always save before running (Ctrl+S).
```

### ❌ Mistake 2: Wrong file path
```
python some_file.py
# Error: file not found
```

Solution: Use full path or navigate to correct directory.

### ❌ Mistake 3: Mixing script and interactive mode
```
Don't paste script code directly into REPL without adjustment.
Some things (like shebang) don't work in REPL.
```

## 🏃 Practical Exercise

**Task**: Create a Python script that prints your name, age, and favorite programming language.

**Requirements**:
1. Create file `exercises/00_introduction.py`
2. Use `print()` to display three lines:
   - "My name is: [your name]"
   - "My age is: [your age]"
   - "My favorite language is: Python"

**Hints**:
- Use `print()` for each line
- Each `print()` creates a new line
- You can use any name and age

**Your Code Here** (Try it yourself first!):

```python
# TODO: Write your code here
```

## ✅ Solution

See `solutions/00_introduction.py`

## 🔗 Key Concepts

| Concept | Meaning |
|---------|---------|
| **Interpreter** | Program that reads and executes Python code |
| **Script** | Python file (`.py`) with code |
| **REPL** | Interactive mode where you type Python live |
| **Bytecode** | Intermediate form between Python and machine code |
| **Comment** | Text Python ignores (for humans to read) |

## 🎯 What's Next?

Now that you understand how Python works, let's learn:

→ **[Lesson 01: Variables and Data Types](01_variables_and_types.md)**

In the next lesson, you'll learn:
- What variables are
- Different data types (int, str, float, bool)
- How to create and use variables
- Type conversion

## 📝 Summary

✅ Python interpreter reads and executes code
✅ Two modes: script (files) and interactive (REPL)
✅ Use `python filename.py` to run a script
✅ Use `python` to enter interactive mode
✅ Use `print()` to display output
✅ Comments start with `#`

---

**Ready?** Continue to [Lesson 01: Variables and Data Types](01_variables_and_types.md)
