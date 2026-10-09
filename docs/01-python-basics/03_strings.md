# Lesson 03: Strings

## 📖 What are Strings?

A **string** is text enclosed in quotes. It's one of Python's most important data types.

```python
name = "Alice"
message = 'Hello, World!'
long_text = """This is a
multi-line string"""
```

## 🔤 String Basics

### Creating Strings

```python
# Single quotes
str1 = 'Hello'

# Double quotes
str2 = "Hello"

# Triple quotes (multi-line)
str3 = """Hello
World"""

# Empty string
str4 = ""
```

**Note**: Single and double quotes are equivalent in Python.

### Accessing Characters

Strings are sequences. Access characters by index (0-based):

```python
name = "Alice"
print(name[0])    # A
print(name[1])    # l
print(name[2])    # i
print(name[-1])   # e (last character)
print(name[-2])   # c (second to last)
```

### String Length

```python
text = "Python"
length = len(text)
print(length)     # 6
```

## ✂️ String Slicing

Extract parts of strings using `[start:end:step]`:

```python
text = "Hello, World!"

print(text[0:5])      # "Hello"
print(text[7:12])     # "World"
print(text[:5])       # "Hello" (from start)
print(text[7:])       # "World!" (to end)
print(text[::2])      # "Hlo ol!" (every 2nd char)
print(text[::-1])     # "!dlroW ,olleH" (reversed)
```

## 🔗 String Concatenation

Combine strings with `+`:

```python
first = "John"
last = "Smith"
full_name = first + " " + last
print(full_name)   # John Smith

# Repeat strings
stars = "*" * 10
print(stars)       # **********
```

## 📝 String Formatting

### f-strings (Modern, Recommended)

```python
name = "Alice"
age = 25

# Simple substitution
print(f"My name is {name}")
# Output: My name is Alice

# With expressions
print(f"I am {age} years old")
print(f"Next year I'll be {age + 1}")
print(f"My name is {name.upper()}")
```

### format() Method

```python
text = "Hello, {}!"
print(text.format("Alice"))  # Hello, Alice!

text = "{} is {} years old"
print(text.format("Bob", 30)) # Bob is 30 years old
```

### % Formatting (Old Style)

```python
name = "Charlie"
print("Hello, %s!" % name)  # Hello, Charlie!
```

## 🛠️ String Methods

Strings have built-in methods:

```python
text = "  Hello, World!  "

# Case conversion
print(text.upper())        # "  HELLO, WORLD!  "
print(text.lower())        # "  hello, world!  "
print(text.capitalize())   # "  hello, world!  "
print(text.title())        # "  Hello, World!  "

# Whitespace
print(text.strip())        # "Hello, World!"
print(text.lstrip())       # "Hello, World!  "
print(text.rstrip())       # "  Hello, World!"

# Search & Replace
print(text.find("Hello"))  # 2
print(text.count("l"))     # 3
print(text.replace("Hello", "Hi"))  # "  Hi, World!  "

# Check properties
print(text.startswith("H"))  # False (has spaces)
print("Hello".startswith("H"))  # True
print("123".isdigit())     # True
print("abc".isalpha())     # True
```

## 🔍 Common String Operations

### Check if substring exists

```python
text = "Hello, World!"

if "World" in text:
    print("Found it!")  # This prints

if "Python" not in text:
    print("Python not found")  # This prints
```

### Split and Join

```python
# Split string into list
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'orange']

# Join list into string
items = ["apple", "banana", "orange"]
result = ", ".join(items)
print(result)  # apple, banana, orange
```

### Strip quotes and spaces

```python
text = "  Hello, World!  "
clean = text.strip()
print(clean)  # "Hello, World!"

# Remove specific characters
text = "###Hello###"
clean = text.strip("#")
print(clean)  # "Hello"
```

## ⚠️ Special Characters

Use escape sequences for special characters:

```python
# Newline
print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2

# Tab
print("Name\tAge")
print("Alice\t25")
# Output:
# Name    Age
# Alice   25

# Backslash
path = "C:\\Users\\Name"
print(path)  # C:\Users\Name

# Quote
text = "He said \"Hello!\""
print(text)  # He said "Hello!"

# Raw string (ignore escapes)
path = r"C:\Users\Name"
print(path)  # C:\Users\Name
```

## 📊 String Properties

| Method | Returns | Example |
|--------|---------|---------|
| `len()` | Length | `len("Hello")` → 5 |
| `.upper()` | Uppercase | `"hello".upper()` → "HELLO" |
| `.lower()` | Lowercase | `"HELLO".lower()` → "hello" |
| `.strip()` | Remove spaces | `" hi ".strip()` → "hi" |
| `.split()` | Split into list | `"a,b".split(",")` → ["a", "b"] |
| `.replace()` | Replace text | `"hi".replace("h", "H")` → "Hi" |
| `.find()` | Find index | `"hello".find("ll")` → 2 |
| `.startswith()` | Check start | `"hello".startswith("he")` → True |
| `.isdigit()` | Check if digits | `"123".isdigit()` → True |

## 💡 Common Mistakes

### ❌ Mistake 1: Forgetting quotes
```python
name = Alice      # ❌ Error: name not defined
name = "Alice"    # ✅ Correct
```

### ❌ Mistake 2: Mixing quote types incorrectly
```python
text = "Hello'   # ❌ Error: mismatched quotes
text = "Hello"   # ✅ Correct
```

### ❌ Mistake 3: Index out of range
```python
text = "Hi"
print(text[5])   # ❌ IndexError
print(text[-1])  # ✅ Correct (last char)
```

### ❌ Mistake 4: Strings are immutable
```python
text = "Hello"
text[0] = "J"    # ❌ TypeError: can't assign to character
text = "Jello"   # ✅ Create new string
```

## 📝 Complete Example

```python
# Working with strings
name = "John Smith"
email = "john@example.com"

print(f"Name: {name}")
print(f"Email: {email}")
print(f"Name length: {len(name)}")
print(f"First name: {name.split()[0]}")
print(f"Email uppercase: {email.upper()}")
print(f"Domain: {email.split('@')[1]}")

# Multi-line string
bio = """
My name is John
I love Python
I'm a developer
"""
print(bio)
```

## 🏃 Practical Exercises

### Exercise 1: String Manipulation
Create a program that:
1. Takes a name as input
2. Prints it in uppercase
3. Prints it in lowercase
4. Prints just the first letter
5. Prints the length

**File**: `exercises/03_string_manipulation.py`

### Exercise 2: Email Parser
Create a program that:
1. Takes an email address
2. Extracts the username (before @)
3. Extracts the domain (after @)
4. Prints both parts

**File**: `exercises/03_email_parser.py`

## ✅ Summary

✅ Strings are text enclosed in quotes
✅ Access characters with index: `str[0]`
✅ Slice strings: `str[start:end]`
✅ Use f-strings for formatting: `f"Hello {name}"`
✅ String methods: `.upper()`, `.lower()`, `.split()`, etc.
✅ Strings are immutable (can't change characters)
✅ Use escape sequences for special characters

## 🎯 What's Next?

→ **[Lesson 04: Lists and Tuples](04_lists_and_tuples.md)**

In the next lesson:
- Create and modify lists
- List methods and operations
- Tuple immutability
- List comprehensions

---

**Ready?** Continue to [Lesson 04: Lists and Tuples](04_lists_and_tuples.md)
