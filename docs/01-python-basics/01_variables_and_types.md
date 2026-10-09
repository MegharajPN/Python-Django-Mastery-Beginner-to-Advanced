# Lesson 01: Variables and Data Types

## 📖 What are Variables?

A **variable** is a named container that stores a value.

Think of it like a labeled box:
- The box holds data
- The label (variable name) identifies it
- You can store different things in it

```
Box labeled "name" contains: "Alice"
Box labeled "age" contains: 25
Box labeled "height" contains: 5.7
```

## 🎯 Creating Variables

### Syntax

```python
variable_name = value
```

### Examples

```python
name = "Alice"
age = 25
height = 5.7
is_student = True
```

## 📊 Python Data Types

Python has several built-in data types:

### 1. **int** - Integers

Whole numbers without decimal points.

```python
age = 25
score = -10
temperature = 0
```

### 2. **float** - Floating Point Numbers

Numbers with decimal points.

```python
height = 5.7
price = 19.99
percentage = 99.5
pi = 3.14159
```

### 3. **str** - Strings

Text enclosed in quotes (single or double).

```python
name = "Alice"
city = 'New York'
message = "Hello, World!"
```

### 4. **bool** - Boolean

True or False.

```python
is_student = True
is_adult = False
is_active = True
```

### 5. **NoneType** - None

A special value representing "nothing" or "no value".

```python
result = None
empty_value = None
```

## 🔍 Checking Data Types

Use `type()` to check a variable's type:

```python
age = 25
print(type(age))        # <class 'int'>

height = 5.7
print(type(height))     # <class 'float'>

name = "Alice"
print(type(name))       # <class 'str'>

is_student = True
print(type(is_student)) # <class 'bool'>
```

## 💾 Variable Names - Rules and Conventions

### Rules (Required)
✅ Start with letter or underscore `_`
✅ Contain only letters, digits, underscores
✅ Are case-sensitive (`name` ≠ `Name`)
✅ Cannot use Python keywords

### Examples of Valid Names
```python
name = "Alice"
_age = 25
user_name = "alice123"
AGE = 30
```

### Examples of Invalid Names
```python
2name = "Alice"       # ❌ Starts with digit
user-name = "alice"   # ❌ Contains hyphen
user name = "alice"   # ❌ Contains space
for = 5               # ❌ Python keyword
```

### Naming Conventions (PEP 8)
```python
# ✅ Good: lowercase with underscores (snake_case)
user_name = "alice"
first_name = "John"
is_active = True

# ❌ Avoid: camelCase in Python
userName = "alice"

# ❌ Avoid: UPPERCASE for regular variables
AGE = 25  # (Use for constants only)
```

## 🔄 Type Conversion

Converting from one type to another:

### String to Integer
```python
age_str = "25"
age = int(age_str)
print(age)      # 25
print(type(age)) # <class 'int'>
```

### Integer to String
```python
age = 25
age_str = str(age)
print(age_str)   # "25"
print(type(age_str)) # <class 'str'>
```

### String to Float
```python
height_str = "5.7"
height = float(height_str)
print(height)    # 5.7
```

### Integer to Float
```python
age = 25
age_float = float(age)
print(age_float) # 25.0
```

### Any to Boolean
```python
print(bool(1))      # True
print(bool(0))      # False
print(bool("Hello")) # True
print(bool(""))     # False
print(bool([]))     # False (empty list)
```

## 💡 Special Cases

### Float to Integer (loses decimals)
```python
height = 5.9
age = int(height)
print(age)  # 5 (decimal part lost!)
```

### Invalid Conversion
```python
text = "Hello"
number = int(text)  # ❌ ValueError: invalid literal
```

## 📝 Complete Example: Person Profile

File: `examples/01_person_profile.py`

```python
# Variables for a person
name = "Alice Johnson"
age = 28
height = 5.7
weight = 130
email = "alice@example.com"
is_student = False
is_employed = True

# Display information
print("=== Person Profile ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Weight: {weight} lbs")
print(f"Email: {email}")
print(f"Student: {is_student}")
print(f"Employed: {is_employed}")

# Type information
print("\n=== Data Types ===")
print(f"name type: {type(name)}")
print(f"age type: {type(age)}")
print(f"height type: {type(height)}")
print(f"is_student type: {type(is_student)}")
```

**Run it:**
```bash
python examples/01_person_profile.py
```

**Output:**
```
=== Person Profile ===
Name: Alice Johnson
Age: 28
Height: 5.7 feet
Weight: 130 lbs
Email: alice@example.com
Student: False
Employed: True

=== Data Types ===
name type: <class 'str'>
age type: <class 'int'>
height type: <class 'float'>
is_student type: <class 'bool'>
```

## 🎓 Common Mistakes

### ❌ Mistake 1: Confusing int and str
```python
age = "25"          # This is a string "25"
age = 25            # This is an integer 25
age = int("25")     # Convert string to integer
```

### ❌ Mistake 2: Quotes required for strings
```python
name = Alice        # ❌ Error: name not defined
name = "Alice"      # ✅ Correct
```

### ❌ Mistake 3: Wrong type conversion
```python
text = "Hello"
number = int(text)  # ❌ ValueError
```

### ❌ Mistake 4: Forgetting quotes for boolean-like strings
```python
is_active = true      # ❌ Error: true not defined
is_active = True      # ✅ Correct (capitalized)
is_active = "true"    # This is a string, not boolean
```

## 🏃 Practical Exercise

**Task**: Create a student profile program

**File**: `exercises/01_student_profile.py`

**Requirements**:
1. Create variables for a student:
   - name (string)
   - student_id (integer)
   - gpa (float)
   - is_enrolled (boolean)
   - courses_taken (integer)

2. Display all information using `print()`

3. Display the type of each variable

4. Convert the GPA to an integer and display it

**Example Output**:
```
Student Name: John Smith
Student ID: 12345
GPA: 3.85
Enrolled: True
Courses Taken: 15

Student Name type: <class 'str'>
Student ID type: <class 'int'>
...
```

**Hints**:
- Use meaningful variable names
- Remember string quotes
- Use `int()`, `float()`, `str()` for conversions
- Use f-strings: `f"Name: {name}"`

## ✅ Solution

See `solutions/01_student_profile.py`

## 🔗 Key Concepts

| Term | Meaning |
|------|---------|
| **Variable** | Named container for data |
| **int** | Integer (whole numbers) |
| **float** | Decimal numbers |
| **str** | Text/strings |
| **bool** | True/False value |
| **type()** | Function to check data type |
| **Type Conversion** | Converting between types |
| **None** | Special "no value" |

## 🎯 What's Next?

→ **[Lesson 02: Operators](02_operators.md)**

In the next lesson:
- Arithmetic operators (+, -, *, /)
- Comparison operators (==, >, <)
- Logical operators (and, or, not)

## 📝 Summary

✅ Variables store data with names
✅ Python has 5 main types: int, float, str, bool, None
✅ Use `type()` to check type
✅ Convert types with `int()`, `float()`, `str()`, `bool()`
✅ Use meaningful variable names
✅ Follow naming conventions (snake_case)

---

**Ready?** Continue to [Lesson 02: Operators](02_operators.md)
