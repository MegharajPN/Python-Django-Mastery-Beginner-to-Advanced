"""
Example 01b: Type Conversion
============================

Learn how to convert between different data types.
"""

print("=== String to Integer ===")
age_str = "25"
age_int = int(age_str)
print(f"age_str = '{age_str}' (type: {type(age_str).__name__})")
print(f"age_int = {age_int} (type: {type(age_int).__name__})")

print("\n=== Integer to String ===")
age = 25
age_str = str(age)
print(f"age = {age} (type: {type(age).__name__})")
print(f"age_str = '{age_str}' (type: {type(age_str).__name__})")

print("\n=== String to Float ===")
height_str = "5.7"
height = float(height_str)
print(f"height_str = '{height_str}' (type: {type(height_str).__name__})")
print(f"height = {height} (type: {type(height).__name__})")

print("\n=== Float to Integer (loses decimals) ===")
price = 19.99
price_int = int(price)
print(f"price = {price} (type: {type(price).__name__})")
print(f"price_int = {price_int} (type: {type(price_int).__name__})")
print("Note: Decimal part is lost!")

print("\n=== Integer to Float ===")
age = 25
age_float = float(age)
print(f"age = {age} (type: {type(age).__name__})")
print(f"age_float = {age_float} (type: {type(age_float).__name__})")

print("\n=== String to Boolean ===")
print(f"bool('Hello') = {bool('Hello')}")  # True (non-empty string)
print(f"bool('') = {bool('')}")            # False (empty string)
print(f"bool(1) = {bool(1)}")              # True
print(f"bool(0) = {bool(0)}")              # False
print(f"bool([1,2,3]) = {bool([1,2,3])}") # True (non-empty list)
print(f"bool([]) = {bool([])}")            # False (empty list)
