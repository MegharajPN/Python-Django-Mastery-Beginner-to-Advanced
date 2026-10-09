# Lesson 14: Debugging (Finding and Fixing Bugs)

## 📖 What is Debugging?

**Debugging** is finding and fixing errors in code.

## 🔍 Types of Errors

### Syntax Errors

```python
if x > 5  # ❌ Missing colon
    print(x)

# SyntaxError: expected ':'
```

### Runtime Errors

```python
x = 5
y = 0
z = x / y  # ❌ ZeroDivisionError

# ZeroDivisionError: division by zero
```

### Logic Errors

```python
def get_max(a, b):
    if a > b:
        return b  # ❌ Returns smaller value
    return a

result = get_max(10, 5)  # Returns 5 (wrong!)
```

## 🐞 Debugging Techniques

### 1. Print Debugging

```python
def calculate(x, y):
    print(f"x = {x}, y = {y}")  # Debug print
    result = x + y
    print(f"result = {result}")  # Debug print
    return result

calculate(5, 3)
```

### 2. Assertions

Check that conditions are true:

```python
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

divide(10, 0)  # AssertionError: Divisor cannot be zero
```

### 3. Using pdb (Python Debugger)

```python
import pdb

def calculate(x, y):
    pdb.set_trace()  # Stops here
    result = x + y
    return result

calculate(5, 3)

# Commands:
# n - next line
# c - continue
# p var - print variable
# l - list code
# q - quit
```

### 4. Try-Except for Error Info

```python
try:
    result = int("abc")
except ValueError as e:
    print(f"Error: {e}")
    print(f"Error type: {type(e).__name__}")
```

## 🔧 Common Bugs

### Off-by-One Errors

```python
# ❌ Wrong
for i in range(10):
    if i == 10:  # Never true
        print("Done")

# ✅ Correct
for i in range(10):
    if i == 9:
        print("Done")
```

### Mutable Default Arguments

```python
# ❌ Wrong
def add_item(item, items=[]):
    items.append(item)
    return items

# ✅ Correct
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Forgetting Global

```python
# ❌ Wrong
count = 0
def increment():
    count += 1  # UnboundLocalError

# ✅ Correct
count = 0
def increment():
    global count
    count += 1
```

## 🧪 Testing Your Code

### Simple Tests

```python
def add(a, b):
    return a + b

# Test cases
assert add(2, 3) == 5
assert add(0, 0) == 0
assert add(-1, 1) == 0

print("All tests passed!")
```

### Using pytest

```python
# test_math.py
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0

# Run: pytest test_math.py
```

## 📋 Debugging Checklist

- [ ] Read the error message carefully
- [ ] Check line numbers in error
- [ ] Add print statements to trace execution
- [ ] Check variable values
- [ ] Verify function parameters
- [ ] Test with simple inputs first
- [ ] Check data types
- [ ] Look for off-by-one errors
- [ ] Check indentation
- [ ] Review recent changes

## 📝 Complete Example

```python
def find_average(numbers):
    """Find average of numbers."""
    if not numbers:
        return 0
    
    total = 0
    for num in numbers:
        print(f"Adding {num}")  # Debug
        total += num
    
    average = total / len(numbers)
    print(f"Total: {total}, Count: {len(numbers)}")  # Debug
    return average

# Test
result = find_average([1, 2, 3, 4, 5])
print(f"Average: {result}")
```

## ✅ Summary

✅ Syntax errors - code structure
✅ Runtime errors - during execution
✅ Logic errors - wrong output
✅ Use print() for debugging
✅ Use pdb for interactive debugging
✅ Use assertions to check conditions
✅ Write tests for your code
✅ Read error messages carefully

---

**Congratulations! You've completed Python Fundamentals!**

## 🎓 What's Next?

Move to **Python Intermediate** →
- Object-Oriented Programming
- Decorators and Generators
- Advanced Testing

Or jump to **Django Fundamentals** →
- Build web applications
- Work with databases
- Create REST APIs

---
