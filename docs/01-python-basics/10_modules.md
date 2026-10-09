# Lesson 10: Modules and Imports

## 📖 What are Modules?

A **module** is a file containing Python code. Modules help organize code into reusable pieces.

```python
# math_helpers.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

## 📥 Importing Modules

### Import Entire Module

```python
import math_helpers

result = math_helpers.add(5, 3)
print(result)  # 8
```

### Import Specific Items

```python
from math_helpers import add, subtract

result = add(5, 3)
print(result)  # 8
```

### Import with Alias

```python
import math_helpers as mh
from math_helpers import add as addition

result = addition(5, 3)
print(result)  # 8
```

### Import All (Not Recommended)

```python
from math_helpers import *  # ❌ Can cause conflicts

result = add(5, 3)
```

## 🎯 Built-in Modules

Python includes many modules:

### math Module

```python
import math

print(math.pi)       # 3.14159...
print(math.sqrt(16)) # 4.0
print(math.ceil(3.2))# 4
print(math.floor(3.8)) # 3
```

### random Module

```python
import random

print(random.random())      # Random float 0-1
print(random.randint(1, 10)) # Random int 1-10
print(random.choice([1, 2, 3])) # Random item

names = ["Alice", "Bob", "Charlie"]
random.shuffle(names)  # Shuffle list
```

### datetime Module

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)  # 2026-10-09 14:30:45.123456

tomorrow = now + timedelta(days=1)
print(tomorrow)
```

### collections Module

```python
from collections import Counter, defaultdict

# Count items
words = ["apple", "banana", "apple", "orange"]
count = Counter(words)
print(count)  # Counter({'apple': 2, 'banana': 1, ...})

# Default values
d = defaultdict(list)
d['items'].append(1)
```

## 📁 Creating Your Own Module

### math_helpers.py

```python
"""Helper functions for mathematics."""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def is_even(n):
    """Check if number is even."""
    return n % 2 == 0
```

### main.py

```python
from math_helpers import add, multiply, is_even

print(add(5, 3))         # 8
print(multiply(4, 2))    # 8
print(is_even(4))        # True
```

## 📦 Packages

A **package** is a folder with modules and `__init__.py`:

```
my_project/
├── math_helpers/
│   ├── __init__.py      # Makes it a package
│   ├── basic.py
│   └── advanced.py
└── main.py
```

### Importing from Packages

```python
from math_helpers.basic import add
from math_helpers.advanced import complex_calc

result = add(5, 3)
```

## 🔍 Checking Module Contents

```python
import math

# See all attributes
print(dir(math))

# Check if has attribute
print(hasattr(math, 'pi'))  # True

# Get docstring
print(math.__doc__)

# See module location
print(math.__file__)
```

## 💡 Common Modules

| Module | Purpose | Example |
|--------|---------|---------|
| `math` | Math operations | `math.sqrt()` |
| `random` | Random values | `random.randint()` |
| `datetime` | Date/time | `datetime.now()` |
| `json` | JSON handling | `json.loads()` |
| `os` | OS operations | `os.getcwd()` |
| `sys` | System info | `sys.version` |
| `re` | Regular expressions | `re.search()` |
| `collections` | Data structures | `Counter()` |

## 🎓 Common Mistakes

### ❌ Mistake 1: Circular imports

```python
# a.py
from b import something

# b.py
from a import something_else  # ❌ Circular!
```

### ❌ Mistake 2: Wrong import path

```python
from math_helpers import add  # ❌ Module not found

# Put math_helpers.py in same directory or in path
```

### ❌ Mistake 3: Shadowing built-ins

```python
import math  # ✅
math = 5     # ❌ Overwrites the module!
```

## 📝 Complete Example

```python
# utils.py
"""Utility functions."""

def greet(name):
    return f"Hello, {name}!"

def multiply(a, b):
    return a * b

# main.py
from utils import greet, multiply
import random
from datetime import datetime

print(greet("Alice"))
print(multiply(3, 4))
print(random.randint(1, 100))
print(datetime.now())
```

## ✅ Summary

✅ Modules are reusable Python files
✅ Import with `import` or `from`
✅ Built-in modules available (math, random, etc.)
✅ Create your own modules
✅ Use `dir()` to explore modules
✅ Organize code into packages
✅ Avoid circular imports

---

**Continue to [Lesson 11: Exception Handling](11_exceptions.md)**
