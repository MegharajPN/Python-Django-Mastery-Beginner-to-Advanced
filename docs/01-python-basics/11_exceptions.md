# Lesson 11: Exception Handling (try, except, finally)

## 📖 What are Exceptions?

An **exception** is an error that occurs during program execution.

```python
x = 10 / 0  # ❌ ZeroDivisionError
```

## 🛡️ The try-except Block

Catch and handle errors:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## 🎯 Multiple Exceptions

```python
try:
    number = int("abc")  # ValueError
    result = 10 / 0      # ZeroDivisionError
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catch Multiple with One Handler

```python
try:
    result = 10 / 0
except (ZeroDivisionError, ValueError):
    print("Math error!")
```

## 🔄 else Block

Runs if no exception:

```python
try:
    number = int("42")
except ValueError:
    print("Invalid input")
else:
    print(f"Success: {number}")  # This prints
```

## 🔚 finally Block

Always runs, exception or not:

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup code here")  # Always runs
```

## 🎓 Common Exceptions

| Exception | Cause | Example |
|-----------|-------|---------|
| `ValueError` | Wrong type | `int("abc")` |
| `TypeError` | Wrong type operation | `"5" + 5` |
| `IndexError` | List index out of range | `lst[100]` |
| `KeyError` | Dict key doesn't exist | `d["missing"]` |
| `ZeroDivisionError` | Divide by zero | `10 / 0` |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `AttributeError` | Attribute doesn't exist | `obj.missing_attr` |
| `NameError` | Variable not defined | `print(undefined_var)` |

## 🚀 Raising Exceptions

Create your own errors:

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")  # Error: Age cannot be negative
```

## 📝 Complete Example

```python
def divide(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None
    else:
        return result
    finally:
        print("Division attempt completed")

print(divide(10, 2))   # 5
print(divide(10, 0))   # Error message, None
print(divide("10", 2)) # Error message, None
```

## ✅ Summary

✅ Try-except catches errors
✅ Multiple exceptions possible
✅ else runs if no exception
✅ finally always runs
✅ Can raise your own exceptions
✅ Use except clauses specific

---

**Continue to [Lesson 12: File I/O](12_file_io.md)**
