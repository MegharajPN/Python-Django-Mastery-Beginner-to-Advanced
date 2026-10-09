# Lesson 07: Loops (for and while)

## 📖 What are Loops?

A **loop** repeats a block of code multiple times.

Two types:
- **for loop**: Iterate through a sequence (list, string, range)
- **while loop**: Repeat while a condition is true

## 🔄 The for Loop

### Syntax

```python
for item in sequence:
    # Code here runs for each item
    print(item)
```

### Iterating Through Lists

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# orange
```

### Iterating Through Strings

```python
word = "Python"

for letter in word:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n
```

### Using range()

```python
# range(stop) - 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(1, 5):
    print(i)  # 1, 2, 3, 4

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### enumerate() - Get Index and Item

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"{index}: {color}")

# Output:
# 0: red
# 1: green
# 2: blue
```

### Looping Through Dictionaries

```python
student = {"name": "Alice", "age": 25, "grade": "A"}

# Loop through keys (default)
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

## ⏹️ break and continue

### break - Exit Loop

```python
for i in range(10):
    if i == 5:
        break  # Exit loop
    print(i)

# Output: 0, 1, 2, 3, 4
```

### continue - Skip Current Iteration

```python
for i in range(5):
    if i == 2:
        continue  # Skip this iteration
    print(i)

# Output: 0, 1, 3, 4
```

## 🔄 The while Loop

### Syntax

```python
while condition:
    # Code here repeats while condition is True
    print("Looping")
```

### Example

```python
count = 0

while count < 5:
    print(count)
    count += 1

# Output: 0, 1, 2, 3, 4
```

### User Input Loop

```python
password = ""

while password != "secret":
    password = input("Enter password: ")

print("Access granted!")
```

### Be Careful of Infinite Loops!

```python
# ❌ This runs forever!
while True:
    print("Never stops!")

# ✅ Always have exit condition
count = 0
while count < 10:
    print(count)
    count += 1
```

## 🔀 Loop Control with else

Execute code after loop completes (if no break):

```python
for i in range(5):
    print(i)
else:
    print("Loop completed!")  # Prints after loop

# ---

for i in range(5):
    if i == 2:
        break
else:
    print("This doesn't print")  # Doesn't print (break)
```

## 📝 Nested Loops

Loop inside a loop:

```python
# Print times table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")

# Output:
# 1 × 1 = 1
# 1 × 2 = 2
# ...
# 3 × 3 = 9
```

## 📋 List Comprehensions (Advanced Preview)

Concise way to create lists:

```python
# Without comprehension
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# With comprehension
squares = [i ** 2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

## 🎯 for vs while

| for | while |
|-----|-------|
| Use for known number of iterations | Use for unknown conditions |
| Iterate through sequences | Repeat until condition false |
| Cleaner for lists/ranges | Better for user input |
| `for item in list:` | `while condition:` |

## 💡 Common Mistakes

### ❌ Mistake 1: Forgetting to increment in while
```python
count = 0
while count < 5:
    print(count)
    # count += 1  # ❌ Forgot this - infinite loop!

count = 0
while count < 5:
    print(count)
    count += 1  # ✅ Correct
```

### ❌ Mistake 2: Off-by-one error with range
```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4 (not 1-5!)

# To get 1-5:
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5
```

### ❌ Mistake 3: Modifying list while looping
```python
items = [1, 2, 3, 4, 5]
for item in items:
    if item == 3:
        items.remove(item)  # ❌ Can skip items

# Better approach:
items = [1, 2, 3, 4, 5]
items = [i for i in items if i != 3]
```

## 📝 Complete Examples

### Example 1: Sum Numbers

```python
total = 0
for i in range(1, 6):
    total += i
print(f"Sum 1-5: {total}")  # 15
```

### Example 2: Find Maximum

```python
numbers = [5, 2, 8, 1, 9, 3]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Maximum: {maximum}")  # 9
```

### Example 3: Count Words

```python
text = "the quick brown fox"
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # {'the': 1, 'quick': 1, 'brown': 1, 'fox': 1}
```

## 🏃 Practical Exercises

### Exercise 1: Multiplication Table
Create a program that:
1. Takes a number from user
2. Prints multiplication table (1-10)

**File**: `exercises/07_multiplication_table.py`

### Exercise 2: Number Guessing Game
Create a program that:
1. Picks a random number
2. Lets user guess until correct
3. Counts guesses

**File**: `exercises/07_guessing_game.py`

## ✅ Summary

✅ for loops iterate through sequences
✅ while loops repeat while condition is true
✅ break exits the loop
✅ continue skips current iteration
✅ range() generates sequences of numbers
✅ enumerate() provides index and value
✅ Avoid infinite loops
✅ List comprehensions create lists concisely

## 🎯 What's Next?

→ **[Lesson 08: Functions](08_functions.md)**

In the next lesson:
- Define functions
- Parameters and arguments
- Return values
- Scope and variables

---

**Ready?** Continue to [Lesson 08: Functions](08_functions.md)
