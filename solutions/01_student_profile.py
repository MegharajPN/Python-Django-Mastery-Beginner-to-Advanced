"""
Solution 01: Student Profile
=============================

Create a student profile with variables and display their information.
This solution demonstrates:
- Creating variables of different types
- Using print() to display information
- Using f-strings for formatted output
- Checking data types
- Type conversion
"""

# Create variables for a student
name = "John Smith"
student_id = 12345
gpa = 3.85
is_enrolled = True
courses_taken = 15

# Display all information
print("=== Student Profile ===")
print(f"Student Name: {name}")
print(f"Student ID: {student_id}")
print(f"GPA: {gpa}")
print(f"Enrolled: {is_enrolled}")
print(f"Courses Taken: {courses_taken}")

# Display the type of each variable
print("\n=== Data Types ===")
print(f"name type: {type(name)}")
print(f"student_id type: {type(student_id)}")
print(f"gpa type: {type(gpa)}")
print(f"is_enrolled type: {type(is_enrolled)}")
print(f"courses_taken type: {type(courses_taken)}")

# Convert GPA to integer
gpa_integer = int(gpa)
print(f"\n=== Type Conversion ===")
print(f"GPA as float: {gpa}")
print(f"GPA as integer: {gpa_integer}")
print("Note: Decimal part was removed when converting to int")
