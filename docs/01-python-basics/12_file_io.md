# Lesson 12: File I/O (Reading and Writing Files)

## 📖 Working with Files

Read and write files using Python.

## 📝 Writing Files

### Basic Write

```python
# Open file for writing
file = open("data.txt", "w")

# Write content
file.write("Hello, World!\n")
file.write("Second line\n")

# Close file
file.close()
```

### Using with Statement (Better)

```python
# Automatically closes file
with open("data.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")
```

## 📖 Reading Files

### Read All Content

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### Read Lines

```python
with open("data.txt", "r") as file:
    lines = file.readlines()  # Returns list
    for line in lines:
        print(line.strip())
```

### Read Line by Line

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## 🔄 File Modes

| Mode | Purpose |
|------|---------|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites) |
| `"a"` | Append (add to end) |
| `"x"` | Create (fails if exists) |
| `"b"` | Binary mode |

### Append to File

```python
with open("data.txt", "a") as file:
    file.write("New line\n")
```

## 📋 File Methods

```python
file = open("data.txt", "r")

# Read content
file.read()          # All content
file.readline()      # One line
file.readlines()     # All lines as list

# File position
file.seek(0)         # Go to start
file.tell()          # Current position

# Close
file.close()
```

## 🔍 Checking Files Exist

```python
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")
```

## 📝 Complete Example

```python
# Write data
data = ["Alice", "Bob", "Charlie"]

with open("names.txt", "w") as file:
    for name in data:
        file.write(name + "\n")

# Read data
with open("names.txt", "r") as file:
    names = [line.strip() for line in file]
    print(names)
```

## ✅ Summary

✅ Open files with `open()`
✅ Use `with` statement for safety
✅ Read with `.read()`, `.readline()`
✅ Write with `.write()`
✅ Append with mode `"a"`
✅ Always close files

---

**Continue to [Lesson 13: JSON and CSV](13_json_csv.md)**
