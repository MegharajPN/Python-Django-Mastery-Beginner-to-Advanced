# Lesson 05: Dictionaries and Sets

## 📖 What are Dictionaries?

A **dictionary** stores data as key-value pairs. Access items by key, not index.

```python
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A"
}
```

## 📝 Creating Dictionaries

### Basic Syntax

```python
# Empty dictionary
my_dict = {}
my_dict = dict()

# With data
person = {
    "name": "Bob",
    "age": 30,
    "email": "bob@example.com"
}

# Mixed types
data = {
    "count": 42,
    "items": [1, 2, 3],
    "active": True
}
```

## 🔍 Accessing Dictionary Items

### By Key

```python
student = {"name": "Alice", "age": 25, "grade": "A"}

print(student["name"])      # Alice
print(student["age"])       # 25

# Using .get() (safer)
print(student.get("age"))   # 25
print(student.get("city"))  # None (doesn't error)
print(student.get("city", "N/A"))  # N/A (default value)
```

## ✏️ Modifying Dictionaries

### Add or Change Items

```python
student = {"name": "Alice"}

# Add new key
student["age"] = 25
student["grade"] = "A"

# Change existing key
student["name"] = "Alicia"

print(student)
# {'name': 'Alicia', 'age': 25, 'grade': 'A'}
```

### Remove Items

```python
student = {"name": "Alice", "age": 25, "grade": "A"}

# Remove by key
del student["grade"]

# Remove and get value
age = student.pop("age")  # Returns 25
print(age)  # 25

# Remove all items
student.clear()
print(student)  # {}
```

## 🔄 Dictionary Methods

```python
person = {"name": "Bob", "age": 30, "city": "NYC"}

# Get all keys
keys = person.keys()
print(list(keys))  # ['name', 'age', 'city']

# Get all values
values = person.values()
print(list(values))  # ['Bob', 30, 'NYC']

# Get all key-value pairs
items = person.items()
print(list(items))  # [('name', 'Bob'), ('age', 30), ('city', 'NYC')]

# Check if key exists
print("name" in person)      # True
print("email" in person)     # False

# Get with default
print(person.get("name"))    # Bob
print(person.get("email", "unknown"))  # unknown

# Update dictionary
person.update({"age": 31, "email": "bob@example.com"})
```

## 🔄 Looping Through Dictionaries

```python
person = {"name": "Bob", "age": 30, "city": "NYC"}

# Loop through keys (default)
for key in person:
    print(key)  # name, age, city

# Loop through values
for value in person.values():
    print(value)  # Bob, 30, NYC

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
    # name: Bob
    # age: 30
    # city: NYC
```

## 📊 Sets - Unique Items

A **set** is an unordered collection of unique items.

```python
# Create sets
colors = {"red", "green", "blue"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14}
empty = set()  # Empty set
```

### Set Operations

```python
fruits = {"apple", "banana", "orange", "apple"}
print(fruits)  # {'apple', 'banana', 'orange'} (no duplicates!)

# Add items
fruits.add("grape")
fruits.add("apple")  # No effect (already exists)

# Remove items
fruits.remove("banana")  # Raises error if not found
fruits.discard("grape")  # No error if not found

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)   # Union: {1, 2, 3, 4, 5}
print(set1 & set2)   # Intersection: {3}
print(set1 - set2)   # Difference: {1, 2}
print(set1 ^ set2)   # Symmetric diff: {1, 2, 4, 5}
```

### Set Properties

```python
items = {1, 2, 3, 4, 5}

# Length
print(len(items))    # 5

# Membership
print(1 in items)    # True
print(6 in items)    # False

# Subset/Superset
subset = {1, 2}
print(subset <= items)  # True (is subset)
print(items >= subset)  # True (is superset)
```

## 🎯 When to Use Each Collection

| Collection | Ordered | Mutable | Duplicates | Use For |
|-----------|---------|---------|-----------|---------|
| **List** | Yes | Yes | Yes | Sequence of items |
| **Tuple** | Yes | No | Yes | Fixed data |
| **Dictionary** | No | Yes | Keys unique | Key-value pairs |
| **Set** | No | Yes | No | Unique items |

## 💡 Real-World Example

```python
# Student database (list of dictionaries)
students = [
    {"name": "Alice", "grade": 90, "active": True},
    {"name": "Bob", "grade": 85, "active": True},
    {"name": "Charlie", "grade": 92, "active": False}
]

# Process students
for student in students:
    status = "Active" if student["active"] else "Inactive"
    print(f"{student['name']}: {student['grade']} ({status})")

# Find average grade
grades = [s["grade"] for s in students]
average = sum(grades) / len(grades)
print(f"Average: {average}")

# Get active students
active = {s["name"] for s in students if s["active"]}
print(f"Active: {active}")
```

## 🎓 Common Mistakes

### ❌ Mistake 1: Empty set syntax
```python
empty = {}          # ❌ This is a dictionary, not a set
empty = set()       # ✅ This is a set
```

### ❌ Mistake 2: Key error
```python
person = {"name": "Bob"}
print(person["age"])  # ❌ KeyError

# Use get() instead
print(person.get("age"))  # ✅ None (no error)
```

### ❌ Mistake 3: Modifying while looping
```python
# Don't do this:
for key in my_dict:
    del my_dict[key]  # ❌ Can skip items

# Do this instead:
keys_to_delete = list(my_dict.keys())
for key in keys_to_delete:
    del my_dict[key]
```

### ❌ Mistake 4: Set with duplicates
```python
items = {1, 2, 2, 3, 3, 3}
print(items)  # {1, 2, 3} (duplicates removed)
# This is usually desired, but remember it happens!
```

## 📝 Complete Example

```python
# Dictionary of products
store = {
    "apple": {"price": 0.50, "quantity": 100},
    "banana": {"price": 0.30, "quantity": 150},
    "orange": {"price": 0.75, "quantity": 80}
}

# Calculate total value
total = 0
for product, info in store.items():
    value = info["price"] * info["quantity"]
    print(f"{product}: ${value:.2f}")
    total += value

print(f"Total inventory value: ${total:.2f}")

# Find products with low stock
low_stock = {name for name, info in store.items() if info["quantity"] < 100}
print(f"Low stock items: {low_stock}")
```

## 🏃 Practical Exercises

### Exercise 1: Contact Book
Create a dictionary-based contact manager that:
1. Stores contacts with name, phone, email
2. Add new contacts
3. Display all contacts
4. Search by name

**File**: `exercises/05_contact_book.py`

### Exercise 2: Inventory System
Create a program that:
1. Stores products with price and quantity
2. Calculates total inventory value
3. Finds low-stock items
4. Updates quantities

**File**: `exercises/05_inventory_system.py`

## ✅ Summary

✅ Dictionaries store key-value pairs
✅ Access with `dict["key"]` or `dict.get("key")`
✅ Add/modify with `dict["key"] = value`
✅ Use `.keys()`, `.values()`, `.items()` to iterate
✅ Sets store unique items
✅ Use sets for membership and uniqueness
✅ Choose collection type based on your needs

## 🎯 What's Next?

→ **[Lesson 06: Conditions](06_conditions.md)**

In the next lesson:
- if, elif, else statements
- Comparison and logical operators
- Ternary operators
- Nested conditions

---

**Ready?** Continue to [Lesson 06: Conditions](06_conditions.md)
