# Lesson 13: JSON and CSV Data Formats

## 📖 JSON - JavaScript Object Notation

JSON is a popular data format for storing and exchanging data.

```json
{
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}
```

## 📥 JSON in Python

### Parse JSON String

```python
import json

json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)

print(data["name"])  # Alice
print(data["age"])   # 25
```

### Convert to JSON String

```python
import json

data = {
    "name": "Bob",
    "age": 30,
    "email": "bob@example.com"
}

json_string = json.dumps(data)
print(json_string)
# {"name": "Bob", "age": 30, "email": "bob@example.com"}
```

### Write JSON to File

```python
import json

data = {
    "users": [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
```

### Read JSON from File

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)
    
print(data["users"])
```

## 📊 CSV - Comma-Separated Values

CSV files store tabular data.

```
name,age,email
Alice,25,alice@example.com
Bob,30,bob@example.com
```

## 📥 CSV in Python

### Read CSV File

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list
```

### Write CSV File

```python
import csv

data = [
    ["name", "age", "email"],
    ["Alice", 25, "alice@example.com"],
    ["Bob", 30, "bob@example.com"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

### CSV as Dictionaries

```python
import csv

# Read as dictionaries
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])

# Write as dictionaries
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

with open("data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)
```

## 📝 Complete Example

```python
import json
import csv

# Create data
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 92}
]

# Save as JSON
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

# Save as CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "grade"])
    writer.writeheader()
    writer.writerows(students)

# Read JSON
with open("students.json", "r") as file:
    json_data = json.load(file)
    print("JSON:", json_data)

# Read CSV
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']}: {row['grade']}")
```

## ✅ Summary

✅ JSON is text-based data format
✅ `json.loads()` - string to Python
✅ `json.dumps()` - Python to string
✅ `json.load()` - read file
✅ `json.dump()` - write file
✅ CSV is tabular data format
✅ `csv.reader` - read CSV
✅ `csv.writer` - write CSV

---

**Continue to [Lesson 14: Debugging](14_debugging.md)**
