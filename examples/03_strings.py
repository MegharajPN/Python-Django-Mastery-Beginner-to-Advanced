"""
Example 03: Strings
===================

Learn string operations, formatting, and methods.
"""

print("=== STRING BASICS ===")
name = "Alice"
greeting = "Hello, World!"

print(f"Name: {name}")
print(f"Greeting: {greeting}")
print(f"Name length: {len(name)}")
print()

print("=== STRING INDEXING ===")
text = "Python"
print(f"First letter: {text[0]}")
print(f"Last letter: {text[-1]}")
print(f"Characters 1-3: {text[1:3]}")
print()

print("=== STRING FORMATTING ===")
age = 25
city = "New York"

# f-strings (modern)
print(f"I am {age} years old and live in {city}")

# format() method
print("I am {} years old".format(age))

# String concatenation
full_info = "Name: " + name + ", Age: " + str(age)
print(full_info)
print()

print("=== STRING METHODS ===")
text = "  Hello, World!  "

print(f"Original: '{text}'")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Strip: '{text.strip()}'")
print()

print("=== STRING OPERATIONS ===")
email = "alice@example.com"
parts = email.split("@")
print(f"Email: {email}")
print(f"Username: {parts[0]}")
print(f"Domain: {parts[1]}")
print()

print("=== COMMON CHECKS ===")
text = "Hello, World!"
print(f"Contains 'World': {'World' in text}")
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with '!': {text.endswith('!')}")
print(f"Count of 'l': {text.count('l')}")
print()

print("=== ESCAPE SEQUENCES ===")
print("Line 1\nLine 2")  # \n = newline
print("Column1\tColumn2")  # \t = tab
print("Quotes: \"Hello\"")  # \" = quote
