"""
Example 02: Operators
=====================

Learn arithmetic, comparison, and logical operators.
"""

print("=== ARITHMETIC OPERATORS ===")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")  # Floor division
print(f"a % b = {a % b}")    # Modulus (remainder)
print(f"a ** b = {a ** b}")  # Exponent

print("\n=== COMPARISON OPERATORS ===")
print(f"10 == 10: {10 == 10}")
print(f"10 != 5: {10 != 5}")
print(f"10 > 5: {10 > 5}")
print(f"10 < 5: {10 < 5}")
print(f"10 >= 10: {10 >= 10}")
print(f"10 <= 5: {10 <= 5}")

print("\n=== LOGICAL OPERATORS ===")
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

print("\n=== REAL-WORLD EXAMPLE ===")
age = 25
salary = 50000
has_degree = True

# Can get a job (age >= 18 AND has degree)
can_apply_for_job = (age >= 18) and has_degree
print(f"Can apply for job: {can_apply_for_job}")

# Is senior (age >= 30 OR high salary)
is_senior = (age >= 30) or (salary >= 60000)
print(f"Is senior professional: {is_senior}")

# Is eligible for loan (age 21-65 AND salary >= 30000)
is_eligible_for_loan = (21 <= age <= 65) and (salary >= 30000)
print(f"Eligible for loan: {is_eligible_for_loan}")
