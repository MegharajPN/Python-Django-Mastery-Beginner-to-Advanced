# Lesson 06: Conditions (if, elif, else)

## 📖 What are Conditions?

**Conditions** allow your program to make decisions. Execute different code based on conditions.

```python
age = 18

if age >= 18:
    print("You can vote!")
else:
    print("You must wait to vote.")
```

## ✅ The if Statement

Basic syntax:

```python
if condition:
    # Execute if condition is True
    print("Condition is true")
```

### Examples

```python
# Simple condition
score = 90
if score >= 80:
    print("Passed!")  # This prints

# With variables
age = 15
if age < 18:
    print("Minor")  # This prints

# Multiple conditions
temperature = 25
is_sunny = True
if temperature > 20 and is_sunny:
    print("Perfect day!")  # This prints
```

## 🔀 if-else Statement

Execute different code for True and False:

```python
if condition:
    # Execute if True
    print("Condition is true")
else:
    # Execute if False
    print("Condition is false")
```

### Example

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")  # This prints
```

## 🔀🔀 if-elif-else Statement

Test multiple conditions:

```python
if condition1:
    print("Condition 1 is true")
elif condition2:
    print("Condition 2 is true")
elif condition3:
    print("Condition 3 is true")
else:
    print("None of the conditions are true")
```

### Example

```python
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")  # This doesn't print
elif age < 65:
    print("Adult")  # This prints
else:
    print("Senior")
```

**Note**: Only the first True condition executes. The rest are skipped.

## 🧬 Comparison Operators

Use these in conditions:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal | `x == 5` |
| `!=` | Not equal | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater or equal | `x >= 5` |
| `<=` | Less or equal | `x <= 5` |

### Examples

```python
x = 10

print(x == 10)   # True
print(x != 10)   # False
print(x > 5)     # True
print(x < 5)     # False
print(x >= 10)   # True
print(x <= 15)   # True
```

## 🧠 Logical Operators

Combine multiple conditions:

### and

Both conditions must be True:

```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("Can drive")  # This prints
```

### or

At least one condition must be True:

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's weekend!")  # This prints
```

### not

Reverses the condition:

```python
is_raining = False

if not is_raining:
    print("Go outside!")  # This prints
```

## 🎯 Truth Table

```python
# AND
True and True    # True
True and False   # False
False and False  # False

# OR
True or True     # True
True or False    # True
False or False   # False

# NOT
not True         # False
not False        # True
```

## 🔤 String Conditions

### Comparison

```python
name = "Alice"

if name == "Alice":
    print("Hello Alice!")  # This prints

if name != "Bob":
    print("You're not Bob")  # This prints
```

### Membership (in, not in)

```python
text = "Hello, World!"

if "Hello" in text:
    print("Found it!")  # This prints

if "Python" not in text:
    print("Python not found")  # This prints
```

## 📋 List Conditions

### Check if item exists

```python
colors = ["red", "green", "blue"]

if "red" in colors:
    print("Red is available")  # This prints

if "yellow" not in colors:
    print("Yellow not available")  # This prints
```

### Check if list is empty

```python
items = []

if items:
    print("Items exist")
else:
    print("List is empty")  # This prints
```

## ⚡ Ternary Operator (One-line if-else)

Concise way to write simple if-else:

```python
# Normal if-else
age = 20
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary operator (same logic)
status = "Adult" if age >= 18 else "Minor"
```

### More Examples

```python
score = 75
grade = "Pass" if score >= 60 else "Fail"
print(grade)  # Pass

price = 100
discount = price * 0.9 if price > 50 else price
print(discount)  # 90
```

## 🎯 Nested Conditions

Conditions inside conditions:

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive alone")  # This prints
    else:
        print("Need adult supervision")
else:
    print("Too young to drive")
```

**Better with logical operators:**

```python
if age >= 18 and has_license:
    print("Can drive alone")
```

## 💡 Common Mistakes

### ❌ Mistake 1: Using = instead of ==
```python
if age = 18:  # ❌ SyntaxError (assignment, not comparison)
    print("Adult")

if age == 18:  # ✅ Correct (comparison)
    print("Adult")
```

### ❌ Mistake 2: Forgetting colon
```python
if age > 18  # ❌ SyntaxError
    print("Adult")

if age > 18:  # ✅ Correct
    print("Adult")
```

### ❌ Mistake 3: Indentation required
```python
if age > 18:
print("Adult")  # ❌ IndentationError

if age > 18:
    print("Adult")  # ✅ Correct
```

### ❌ Mistake 4: Case matters
```python
if age > 18:
    print("Adult")
Elif age > 13:  # ❌ 'Elif' not defined (case matters)
    print("Teen")

if age > 18:
    print("Adult")
elif age > 13:  # ✅ Correct (lowercase)
    print("Teen")
```

## 📝 Complete Example

```python
# Student grade system
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This executes
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}")
print(f"Grade: {grade}")

# Eligibility check
age = 20
income = 50000

eligible_for_loan = age >= 18 and income >= 30000

if eligible_for_loan:
    print("You can apply for a loan")
else:
    print("You don't meet requirements")
```

## 🏃 Practical Exercises

### Exercise 1: Grade Calculator
Create a program that:
1. Takes a test score
2. Assigns a letter grade (A/B/C/D/F)
3. Prints pass/fail status

**File**: `exercises/06_grade_calculator.py`

### Exercise 2: Login System
Create a program that:
1. Stores username and password
2. Takes user input
3. Checks if credentials match
4. Prints appropriate message

**File**: `exercises/06_login_system.py`

## ✅ Summary

✅ if statements test conditions
✅ elif tests additional conditions
✅ else handles default case
✅ Use comparison operators: ==, !=, >, <, >=, <=
✅ Use logical operators: and, or, not
✅ Don't forget the colon (:)
✅ Indentation is required
✅ Ternary for simple one-liners

## 🎯 What's Next?

→ **[Lesson 07: Loops](07_loops.md)**

In the next lesson:
- for loops (iterating)
- while loops (repeating)
- break and continue
- Loop control

---

**Ready?** Continue to [Lesson 07: Loops](07_loops.md)
