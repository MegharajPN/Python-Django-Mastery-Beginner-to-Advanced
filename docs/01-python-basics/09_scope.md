# Lesson 09: Scope (Local, Global, Nonlocal)

## 📖 What is Scope?

**Scope** determines where a variable can be used.

Two main types:
- **Global scope** - Accessible everywhere
- **Local scope** - Only accessible in function

## 🌍 Global Scope

Variables defined outside functions:

```python
name = "Global"  # Global scope

def print_name():
    print(name)  # Can access global variable

print_name()  # Global
print(name)   # Global
```

## 📦 Local Scope

Variables defined inside functions:

```python
def greet():
    message = "Hello"  # Local scope
    print(message)

greet()      # Hello
print(message)  # ❌ NameError: not defined
```

## 🔄 Shadowing

Local variable hides global:

```python
x = 10  # Global

def print_x():
    x = 20  # Local - shadows global
    print(x)

print_x()  # 20
print(x)   # 10 (global unchanged)
```

## 🌍 Accessing Global Variables

Use `global` keyword to modify:

```python
count = 0  # Global

def increment():
    global count  # Tell Python we want the global variable
    count += 1

increment()
print(count)  # 1
increment()
print(count)  # 2
```

## 🔗 Nonlocal Scope

For nested functions:

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Modify x from outer function
        x = 20
    
    inner()
    print(x)  # 20

outer()
```

## 📊 Scope Hierarchy

```
Global Scope
    └── Function A
            └── Nested Function
    └── Function B
```

## 💡 LEGB Rule

Python looks for variables in this order:
1. **Local** - Inside function
2. **Enclosing** - In outer function (nested)
3. **Global** - At module level
4. **Built-in** - Python built-ins (print, len, etc.)

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Finds in Local first
    
    inner()

outer()  # local
```

## 🎓 Common Mistakes

### ❌ Mistake 1: Modifying global without declaration

```python
count = 0

def increment():
    count += 1  # ❌ UnboundLocalError

increment()

# Correct:
def increment():
    global count
    count += 1
```

### ❌ Mistake 2: Assuming nested access

```python
def outer():
    x = 10

def inner():
    print(x)  # ❌ NameError - not in outer scope

inner()
```

## 📝 Complete Example

```python
# Global counter
total_calls = 0

def create_counter():
    """Create a counter function with local state."""
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

# Create two independent counters
counter1 = create_counter()
counter2 = create_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1
print(counter1())  # 3
```

## ✅ Summary

✅ Global variables accessible everywhere
✅ Local variables only in function
✅ Use `global` to modify global vars
✅ Use `nonlocal` in nested functions
✅ Python uses LEGB rule for lookup
✅ Local scope hides global (shadowing)

---

**Continue to [Lesson 10: Modules and Imports](10_modules.md)**
