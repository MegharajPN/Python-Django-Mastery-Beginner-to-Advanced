# Lesson 08: Functions

## 📖 What are Functions?

A **function** is reusable code that performs a specific task.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
```

## 📝 Defining Functions

### Basic Syntax

```python
def function_name():
    # Code here
    print("Hello")

# Call the function
function_name()  # Output: Hello
```

### Function with Parameters

```python
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(5, 3)  # Output: 5 + 3 = 8
add(10, 20)  # Output: 10 + 20 = 30
```

### Function with Return Value

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # 20

# Use directly
print(multiply(3, 7))  # 21
```

## 🎯 Parameters vs Arguments

**Parameters** are defined in the function definition.
**Arguments** are passed when calling the function.

```python
def introduce(name, age):  # name, age are PARAMETERS
    print(f"{name} is {age} years old")

introduce("Alice", 25)  # "Alice", 25 are ARGUMENTS
```

## ⚙️ Default Parameters

Set default values:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob", "Hi")  # Hi, Bob!
```

## 🔄 Multiple Return Values

Return multiple values as a tuple:

```python
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_and_remainder(17, 5)
print(q)  # 3
print(r)  # 2
```

## 📋 Keyword Arguments

Use parameter names when calling:

```python
def create_user(name, email, age):
    print(f"{name}, {email}, {age}")

# Positional arguments
create_user("Alice", "alice@example.com", 25)

# Keyword arguments
create_user(name="Bob", email="bob@example.com", age=30)

# Mixed
create_user("Charlie", age=35, email="charlie@example.com")
```

## 🌀 *args and **kwargs

### *args - Variable Number of Arguments

```python
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3))        # 6
print(sum_numbers(1, 2, 3, 4, 5))  # 15
```

### **kwargs - Keyword Arguments Dictionary

```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC
```

## 📚 Docstrings

Document your functions:

```python
def add(a, b):
    """
    Add two numbers and return the sum.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b

# Access docstring
print(add.__doc__)
help(add)
```

## 🎯 Type Hints

Indicate expected types:

```python
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

result: str = greet("Alice")
print(result)
```

## 💡 Common Patterns

### Early Return

```python
def validate_age(age):
    if age < 0:
        return False
    if age > 150:
        return False
    return True

# Better with early returns
def validate_age(age):
    if age < 0 or age > 150:
        return False
    return True
```

### Function Returning Function

```python
def create_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times_3 = create_multiplier(3)
print(times_3(10))  # 30
```

### Passing Functions

```python
def apply_operation(a, b, operation):
    return operation(a, b)

def add(x, y):
    return x + y

result = apply_operation(5, 3, add)
print(result)  # 8
```

## 🎓 Common Mistakes

### ❌ Mistake 1: Forgetting return statement

```python
def get_sum(a, b):
    a + b  # ❌ Doesn't return anything

result = get_sum(5, 3)
print(result)  # None

# Correct:
def get_sum(a, b):
    return a + b  # ✅
```

### ❌ Mistake 2: Parameters vs local variables

```python
def increment(x):
    x += 1  # ❌ Only changes local copy
    print(x)

num = 5
increment(num)  # Prints 6
print(num)  # Still 5!
```

### ❌ Mistake 3: Mutable default arguments

```python
# ❌ Wrong
def add_item(item, items=[]):
    items.append(item)
    return items

list1 = add_item(1)
list2 = add_item(2)
print(list1)  # [1, 2] - Both share same list!

# ✅ Correct
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## 📝 Complete Example

```python
def calculate_grade(scores: list) -> dict:
    """Calculate average and grade from scores."""
    if not scores:
        return {"average": 0, "grade": "N/A"}
    
    average = sum(scores) / len(scores)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"
    
    return {
        "average": round(average, 2),
        "grade": grade
    }

# Use the function
scores = [85, 90, 88, 92, 87]
result = calculate_grade(scores)
print(f"Average: {result['average']}")
print(f"Grade: {result['grade']}")
```

## 🏃 Practical Exercises

### Exercise 1: Temperature Converter
Create functions that:
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
3. Use type hints

**File**: `exercises/08_temperature_converter.py`

### Exercise 2: Calculator Functions
Create functions for:
1. Add, subtract, multiply, divide
2. All take two numbers
3. All return results

**File**: `exercises/08_calculator_functions.py`

## ✅ Summary

✅ Functions are reusable code blocks
✅ Parameters are inputs
✅ Return values are outputs
✅ Default parameters provide flexibility
✅ *args and **kwargs handle variable inputs
✅ Docstrings document functions
✅ Type hints clarify expectations
✅ Functions should do one thing well

## 🎯 What's Next?

→ **[Lesson 09: Scope](09_scope.md)**

In the next lesson:
- Local, global, and nonlocal scopes
- Variable lifetime
- Name resolution

---

**Ready?** Continue to [Lesson 09: Scope](09_scope.md)
