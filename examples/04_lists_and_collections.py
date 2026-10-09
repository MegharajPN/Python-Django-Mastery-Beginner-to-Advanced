"""
Example 04: Lists and Collections
==================================

Learn lists, tuples, dictionaries, and sets.
"""

print("=== LISTS ===")
fruits = ["apple", "banana", "orange"]
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Modify lists
fruits.append("grape")
print(f"After append: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")
print()

print("=== TUPLES ===")
coordinates = (10, 20, 30)
print(f"Coordinates: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Unpacking
x, y, z = coordinates
print(f"Unpacked: x={x}, y={y}, z={z}")
print()

print("=== DICTIONARIES ===")
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A"
}

print(f"Student: {student}")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")

# Modify dictionary
student["email"] = "alice@example.com"
print(f"After adding email: {student}")

# Loop through
print("Student details:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()

print("=== SETS ===")
numbers = {1, 2, 3, 2, 1}  # Duplicates are removed
print(f"Numbers (no duplicates): {numbers}")

# Set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union (|): {set1 | set2}")
print(f"Intersection (&): {set1 & set2}")
print(f"Difference (-): {set1 - set2}")
print()

print("=== COMPLEX EXAMPLE ===")
# List of dictionaries (common pattern)
students_list = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 92}
]

print("Student Grades:")
total = 0
for student in students_list:
    print(f"  {student['name']}: {student['grade']}")
    total += student['grade']

average = total / len(students_list)
print(f"Average: {average:.1f}")
