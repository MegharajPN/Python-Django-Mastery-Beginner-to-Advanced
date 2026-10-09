# Lesson 04: Lists and Tuples

## 📖 What are Lists?

A **list** is an ordered collection of items. Lists are mutable (can be changed).

```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
```

## 📝 Creating Lists

```python
# Empty list
my_list = []

# List with items
colors = ["red", "green", "blue"]

# List with different types
data = [42, "hello", 3.14, True, None]

# Using list() constructor
my_list = list()
my_list = list("ABC")  # ['A', 'B', 'C']
```

## 🔍 Accessing List Items

### Indexing (0-based)

```python
fruits = ["apple", "banana", "orange", "grape"]

print(fruits[0])    # apple
print(fruits[1])    # banana
print(fruits[-1])   # grape (last item)
print(fruits[-2])   # orange (second to last)
```

### Slicing

```python
fruits = ["apple", "banana", "orange", "grape"]

print(fruits[0:2])   # ['apple', 'banana']
print(fruits[1:3])   # ['banana', 'orange']
print(fruits[::2])   # ['apple', 'orange']
print(fruits[::-1])  # ['grape', 'orange', 'banana', 'apple']
```

## ✏️ Modifying Lists

### Change Items

```python
fruits = ["apple", "banana", "orange"]
fruits[0] = "pear"
print(fruits)  # ['pear', 'banana', 'orange']
```

### Add Items

```python
fruits = ["apple", "banana"]

# Add one item
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']

# Add at specific position
fruits.insert(1, "grape")
print(fruits)  # ['apple', 'grape', 'banana', 'orange']

# Add multiple items
fruits.extend(["kiwi", "mango"])
print(fruits)  # ['apple', 'grape', 'banana', 'orange', 'kiwi', 'mango']
```

### Remove Items

```python
fruits = ["apple", "banana", "orange", "apple"]

# Remove by value (removes first occurrence)
fruits.remove("apple")
print(fruits)  # ['banana', 'orange', 'apple']

# Remove by index
removed = fruits.pop(0)  # Returns the removed item
print(removed)  # 'banana'
print(fruits)   # ['orange', 'apple']

# Clear entire list
fruits.clear()
print(fruits)  # []
```

## 🔄 List Methods

```python
numbers = [3, 1, 4, 1, 5, 9]

# Sort (modifies list)
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5, 9]

# Reverse (modifies list)
numbers.reverse()
print(numbers)  # [9, 5, 4, 3, 1, 1]

# Count occurrences
print(numbers.count(1))  # 2

# Find index
print(numbers.index(4))  # 2

# Copy
numbers_copy = numbers.copy()
```

## 🔍 List Properties & Methods

```python
numbers = [1, 2, 3, 4, 5]

# Length
print(len(numbers))     # 5

# Check membership
print(1 in numbers)     # True
print(6 in numbers)     # False

# Min and max
print(min(numbers))     # 1
print(max(numbers))     # 5

# Sum
print(sum(numbers))     # 15
```

## 📋 Tuples - Immutable Lists

A **tuple** is like a list but immutable (cannot be changed after creation).

```python
# Create tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma!
empty = ()
```

### Tuple Operations

```python
point = (10, 20, 30)

# Access items
print(point[0])     # 10
print(point[-1])    # 30

# Slicing
print(point[1:])    # (20, 30)

# Length
print(len(point))   # 3

# Membership
print(20 in point)  # True

# Unpacking
x, y, z = point
print(x)  # 10
print(y)  # 20
```

### Why Use Tuples?

✅ **Immutable** - Can't accidentally modify
✅ **Faster** - Slightly more efficient
✅ **Hashable** - Can use as dictionary keys
✅ **Safe** - Function return values won't change

```python
# Tuples as dictionary keys
locations = {
    (10, 20): "Place A",
    (30, 40): "Place B"
}

# Can't do this with lists
# locations = {[10, 20]: "Place A"}  # ❌ Error
```

## 🔄 Looping Through Lists

### for loop

```python
colors = ["red", "green", "blue"]

for color in colors:
    print(color)

# With index
for i, color in enumerate(colors):
    print(f"{i}: {color}")
    # 0: red
    # 1: green
    # 2: blue
```

### while loop

```python
numbers = [1, 2, 3]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

## 📊 List vs Tuple Comparison

| Feature | List | Tuple |
|---------|------|-------|
| **Mutable** | Yes | No |
| **Create** | `[]` | `()` |
| **Modify** | Yes | No |
| **Speed** | Slower | Faster |
| **Use as key** | No | Yes |

## 🎓 Common Mistakes

### ❌ Mistake 1: Single item tuple
```python
my_tuple = (1)      # ❌ This is just a number, not a tuple
my_tuple = (1,)     # ✅ This is a tuple
```

### ❌ Mistake 2: Index out of range
```python
items = [1, 2, 3]
print(items[5])  # ❌ IndexError
print(items[-1]) # ✅ Correct
```

### ❌ Mistake 3: Trying to modify tuple
```python
point = (10, 20)
point[0] = 30    # ❌ TypeError
```

### ❌ Mistake 4: Forgot the comma for single-item tuple
```python
single = (42)    # ❌ This is just 42
single = (42,)   # ✅ This is a tuple
```

## 📝 Complete Example

```python
# Working with lists
shopping_list = ["milk", "bread", "eggs"]

# Add item
shopping_list.append("butter")

# Remove item
shopping_list.remove("bread")

# Display
print("Shopping list:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

# Tuple for coordinates
locations = (
    (10, 20),
    (30, 40),
    (50, 60)
)

print("\nLocations:")
for x, y in locations:
    print(f"X: {x}, Y: {y}")
```

## 🏃 Practical Exercises

### Exercise 1: List Operations
Create a program that:
1. Creates a list of 5 numbers
2. Adds a number to the end
3. Removes a number
4. Prints the list in reverse
5. Prints the sum

**File**: `exercises/04_list_operations.py`

### Exercise 2: Grade Manager
Create a program that:
1. Stores grades in a list
2. Calculates average
3. Finds highest and lowest
4. Counts how many passed (>= 60)

**File**: `exercises/04_grade_manager.py`

## ✅ Summary

✅ Lists are mutable sequences
✅ Use `[item]` to access by index
✅ Use `.append()`, `.remove()` to modify
✅ Tuples are immutable sequences
✅ Single-item tuple needs comma: `(1,)`
✅ Use tuples for fixed data
✅ Loop with `for item in list:`

## 🎯 What's Next?

→ **[Lesson 05: Dictionaries and Sets](05_dictionaries_and_sets.md)**

In the next lesson:
- Key-value pairs with dictionaries
- Dictionary methods
- Sets and unique items
- Comparing collections

---

**Ready?** Continue to [Lesson 05: Dictionaries and Sets](05_dictionaries_and_sets.md)
