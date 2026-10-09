"""
Example 05: Conditions (if, elif, else)
========================================

Learn conditional statements and decision making.
"""

print("=== SIMPLE IF ===")
age = 20

if age >= 18:
    print("You are an adult")
print()

print("=== IF-ELSE ===")
score = 45

if score >= 60:
    status = "Pass"
else:
    status = "Fail"

print(f"Score: {score}")
print(f"Status: {status}")
print()

print("=== IF-ELIF-ELSE ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")
print()

print("=== LOGICAL OPERATORS ===")
age = 25
has_license = True
has_insurance = True

# AND - both must be true
if age >= 18 and has_license and has_insurance:
    print("Can drive legally")
print()

# OR - at least one must be true
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")
print()

# NOT - reverses condition
is_raining = False

if not is_raining:
    print("Go outside!")
print()

print("=== TERNARY OPERATOR ===")
age = 15

# Long way
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
print(f"Long way: {status}")

# Short way (ternary)
status = "Adult" if age >= 18 else "Minor"
print(f"Ternary: {status}")
print()

print("=== MEMBERSHIP TESTS ===")
fruits = ["apple", "banana", "orange"]

if "apple" in fruits:
    print("Apple is in the list")

if "grape" not in fruits:
    print("Grape is not in the list")
print()

print("=== STRING CONDITIONS ===")
name = "Alice"

if name == "Alice":
    print("Hello Alice!")

if name.startswith("A"):
    print("Name starts with A")

if "ice" in name:
    print("'ice' is in the name")
print()

print("=== PRACTICAL EXAMPLE ===")
# Temperature-based advice
temperature = 25
is_sunny = True
is_windy = False

print(f"Temperature: {temperature}°C, Sunny: {is_sunny}, Windy: {is_windy}")

if temperature < 0:
    advice = "Wear heavy coat"
elif temperature < 10:
    advice = "Wear jacket"
elif temperature < 20:
    advice = "Wear sweater"
else:
    advice = "Light clothing"

if not is_sunny:
    advice += " and take umbrella"

if is_windy:
    advice += " and hold onto hat"

print(f"Advice: {advice}")
