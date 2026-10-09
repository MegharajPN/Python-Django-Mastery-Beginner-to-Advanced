# Lesson 02: Operators

## 📖 What are Operators?

**Operators** are symbols that perform operations on variables and values.

For example:
- `+` adds two numbers
- `>` checks if one number is greater than another
- `and` combines two conditions

## 🔢 Arithmetic Operators

Use these to perform math operations:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 2` | `3.0` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulus (remainder) | `7 % 2` | `1` |
| `**` | Exponent (power) | `2 ** 3` | `8` |

### Examples

```python
# Addition
result = 10 + 5
print(result)  # 15

# Subtraction
result = 10 - 5
print(result)  # 5

# Multiplication
result = 10 * 5
print(result)  # 50

# Division (always returns float)
result = 10 / 5
print(result)  # 2.0

# Floor Division (removes decimal)
result = 7 / 2
print(result)   # 3.5
result = 7 // 2
print(result)   # 3

# Modulus (remainder)
result = 7 % 2
print(result)  # 1

# Exponent
result = 2 ** 3
print(result)  # 8 (2 * 2 * 2)
```

## 🔀 Assignment Operators

Use these to assign and modify values:

| Operator | Example | Equivalent |
|----------|---------|------------|
| `=` | `x = 5` | Assign |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

### Examples

```python
x = 10
print(x)    # 10

x += 5      # Same as: x = x + 5
print(x)    # 15

x -= 3      # Same as: x = x - 3
print(x)    # 12

x *= 2      # Same as: x = x * 2
print(x)    # 24
```

## ⚖️ Comparison Operators

Compare two values and return True or False:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal | `5 == 5` | `True` |
| `!=` | Not Equal | `5 != 3` | `True` |
| `>` | Greater Than | `5 > 3` | `True` |
| `<` | Less Than | `5 < 3` | `False` |
| `>=` | Greater or Equal | `5 >= 5` | `True` |
| `<=` | Less or Equal | `5 <= 3` | `False` |

### Examples

```python
# Equal
print(5 == 5)      # True
print(5 == 3)      # False

# Not Equal
print(5 != 3)      # True
print(5 != 5)      # False

# Greater Than
print(5 > 3)       # True
print(3 > 5)       # False

# Less Than
print(5 < 3)       # False
print(3 < 5)       # True

# Greater or Equal
print(5 >= 5)      # True
print(5 >= 3)      # True

# Less or Equal
print(5 <= 5)      # True
print(3 <= 5)      # True

# Strings can be compared too
print("apple" == "apple")    # True
print("apple" < "banana")    # True (alphabetical)
```

## 🧠 Logical Operators

Combine conditions using `and`, `or`, `not`:

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be True | `True and True` → `True` |
| `or` | At least one must be True | `True or False` → `True` |
| `not` | Reverses the value | `not True` → `False` |

### Truth Table

```python
# AND
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OR
print(True or True)     # True
print(True or False)    # True
print(False or False)   # False

# NOT
print(not True)         # False
print(not False)        # True
```

### Real Examples

```python
age = 25
income = 50000

# Check if person can get loan (age >= 18 AND income >= 30000)
can_get_loan = (age >= 18) and (income >= 30000)
print(can_get_loan)  # True

# Check if it's weekend (day is Saturday OR day is Sunday)
day = "Saturday"
is_weekend = (day == "Saturday") or (day == "Sunday")
print(is_weekend)  # True

# Check if NOT a student
is_student = False
is_not_student = not is_student
print(is_not_student)  # True
```

## 📝 Complete Examples

### Example: Calculator

```python
# Input values
a = 10
b = 3

print("=== Arithmetic Operations ===")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
```

### Example: Eligibility Check

```python
# Check if person is eligible to vote
age = 20
citizenship = True
has_id = True

is_eligible = (age >= 18) and citizenship and has_id

print(f"Age: {age}")
print(f"Citizenship: {citizenship}")
print(f"Has ID: {has_id}")
print(f"Eligible to vote: {is_eligible}")
```

## 🎓 Common Mistakes

### ❌ Mistake 1: Mixing = and ==
```python
if x = 5:       # ❌ SyntaxError
    print(x)

if x == 5:      # ✅ Correct (comparison)
    print(x)

x = 5           # ✅ Correct (assignment)
```

### ❌ Mistake 2: Wrong operator for strings
```python
name = "Alice"
if name = "Alice":  # ❌ SyntaxError
    print("Match")

if name == "Alice": # ✅ Correct
    print("Match")
```

### ❌ Mistake 3: Forgetting parentheses in complex conditions
```python
# Unclear which operator is evaluated first
if age > 18 and status == "student" or income > 50000:
    pass

# Better: use parentheses to be clear
if (age > 18) and (status == "student") or (income > 50000):
    pass
```

## 🏃 Practical Exercises

### Exercise 1: Calculator
Create a program that:
1. Stores two numbers in variables
2. Performs all arithmetic operations
3. Prints the results

**File**: `exercises/02_calculator.py`

### Exercise 2: Eligibility Check
Create a program that checks if someone can:
- Apply for a job (age >= 18 AND has_education = True)
- Get a driver's license (age >= 16 AND passed_test = True)

**File**: `exercises/02_eligibility.py`

## 🔗 Key Concepts

| Operator Type | Purpose | Examples |
|---------------|---------|----------|
| **Arithmetic** | Math operations | +, -, *, /, //, %, ** |
| **Comparison** | Compare values | ==, !=, >, <, >=, <= |
| **Logical** | Combine conditions | and, or, not |
| **Assignment** | Assign/modify values | =, +=, -=, *=, /= |

## 📝 Summary

✅ Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
✅ Comparison operators return True/False
✅ Logical operators: `and`, `or`, `not`
✅ `=` assigns, `==` compares
✅ Use parentheses for clarity

## 🎯 What's Next?

→ **[Lesson 03: Strings](03_strings.md)**

In the next lesson:
- String operations
- String methods
- String formatting (f-strings, format())
- Escaping special characters

---

**Ready?** Continue to [Lesson 03: Strings](03_strings.md)
