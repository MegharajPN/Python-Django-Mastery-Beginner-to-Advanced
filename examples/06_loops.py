"""
Example 06: Loops
=================

Learn for loops, while loops, and loop control.
"""

print("=== FOR LOOP WITH RANGE ===")
for i in range(5):
    print(i, end=" ")
print("\n")

print("=== FOR LOOP WITH LIST ===")
colors = ["red", "green", "blue"]
for color in colors:
    print(f"Color: {color}")
print()

print("=== FOR LOOP WITH ENUMERATE ===")
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
print()

print("=== FOR LOOP WITH DICTIONARY ===")
student = {"name": "Alice", "age": 25, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")
print()

print("=== BREAK STATEMENT ===")
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(i, end=" ")
print("\n")

print("=== CONTINUE STATEMENT ===")
for i in range(5):
    if i == 2:
        print(f"Skipping {i}")
        continue
    print(i, end=" ")
print("\n")

print("=== WHILE LOOP ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
print()

print("=== WHILE WITH BREAK ===")
password = ""
attempts = 0
while attempts < 3:
    # Simulating input (normally would use input())
    if attempts == 0:
        password = "wrong"
    elif attempts == 1:
        password = "wrong"
    else:
        password = "secret"

    if password == "secret":
        print("Access granted!")
        break
    else:
        print(f"Wrong password (attempt {attempts + 1})")
    attempts += 1
print()

print("=== NESTED LOOPS ===")
print("3x3 Times Table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:2d}", end=" ")
    print()
print()

print("=== LIST COMPREHENSION ===")
# Create list of squares
squares = [i ** 2 for i in range(6)]
print(f"Squares: {squares}")

# Create list with condition
evens = [i for i in range(10) if i % 2 == 0]
print(f"Even numbers: {evens}")
print()

print("=== PRACTICAL EXAMPLE: SUM ===")
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Numbers: {numbers}")
print(f"Sum: {total}")
