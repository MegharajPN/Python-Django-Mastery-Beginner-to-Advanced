# 🚀 Quick Reference Guide - Commands & Key Info

## ⚡ Essential Commands

### Virtual Environment

```powershell
# Activate (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate (Linux/Mac)
source .venv/bin/activate

# Verify activation (should see .venv prefix)
python --version

# Deactivate
deactivate
```

### Python

```bash
# Run a script
python examples/00_hello_world.py

# Start interactive shell
python

# Exit interactive shell
exit()

# Run specific module
python -m json.tool data.json
```

### Django

```bash
# Check Django version
django-admin --version

# Start development server (from mastery_platform folder)
cd projects/mastery_platform
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Django shell
python manage.py shell

# Create new app
python manage.py startapp blog

# Run tests
python manage.py test
```

### Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest exercises/01_student_profile.py

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=.
```

### Git

```bash
# Initialize repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial setup"

# Check status
git status

# View history
git log --oneline
```

---

## 📂 File Locations

### Documentation
- **Python Basics**: `docs/01-python-basics/`
- **Django Basics**: `docs/05-django-fundamentals/`
- **Project Guide**: `LEARNING_ROADMAP.md`
- **Getting Started**: `GETTING_STARTED.md`

### Code
- **Examples**: `examples/` (run with `python examples/XX_topic.py`)
- **Exercises**: `exercises/` (solve problems here)
- **Solutions**: `solutions/` (check after trying)

### Projects
- **Django Project**: `projects/mastery_platform/`
- **Mini Projects**: `projects/` (0-8 folders)

---

## 🔑 Key Keyboard Shortcuts

### PowerShell
| Shortcut | Action |
|----------|--------|
| Ctrl+C | Stop running command |
| Ctrl+L | Clear screen |
| ↑ Arrow | Previous command |
| ↓ Arrow | Next command |
| Tab | Auto-complete |

### Python REPL
| Command | Action |
|---------|--------|
| `help(object)` | Get help |
| `dir(object)` | List attributes |
| `type(object)` | Get type |
| `exit()` | Exit REPL |

### Django
| Command | Action |
|---------|--------|
| Ctrl+C | Stop server |
| http://127.0.0.1:8000/ | Local development |
| http://127.0.0.1:8000/admin | Admin panel |

---

## 📋 Python Syntax Quick Reference

### Variables
```python
name = "Alice"
age = 25
score = 95.5
active = True
```

### Data Types
```python
list_items = [1, 2, 3]
tuple_items = (1, 2, 3)
dict_items = {"name": "Alice", "age": 25}
set_items = {1, 2, 3}
```

### Control Flow
```python
if condition:
    # do something
elif other_condition:
    # do something else
else:
    # default

for item in list:
    print(item)

while condition:
    # repeat
```

### Functions
```python
def function_name(param1, param2):
    """Docstring"""
    return param1 + param2

result = function_name(5, 3)
```

### Classes
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"

person = Person("Alice", 25)
print(person.greet())
```

### Exception Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup")
```

---

## 🌐 Django Syntax Quick Reference

### URL Patterns
```python
# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
```

### Views
```python
# views.py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello")

def list_items(request):
    items = Item.objects.all()
    return render(request, 'items.html', {'items': items})
```

### Models
```python
# models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```

### Templates
```html
<!-- template.html -->
{% for item in items %}
    <h3>{{ item.name }}</h3>
    <p>{{ item.description }}</p>
{% endfor %}
```

---

## 📊 Quick Lookup Tables

### Python Data Type Methods

#### String
```python
"hello".upper()      # "HELLO"
"HELLO".lower()      # "hello"
"hello".capitalize() # "Hello"
"hello".split(",")   # List split by comma
"a,b,c".join()       # "abc"
```

#### List
```python
list.append(item)      # Add item
list.remove(item)      # Remove item
list.sort()            # Sort list
list.reverse()         # Reverse list
list.pop()             # Remove and return last
```

#### Dictionary
```python
dict.keys()            # Get keys
dict.values()          # Get values
dict.items()           # Get key-value pairs
dict.get(key)          # Get value safely
```

### File Operations
```python
open(file, "r")  # Read
open(file, "w")  # Write
open(file, "a")  # Append
with open(file) as f:
    content = f.read()
```

---

## 🎯 Learning Checklist

### Week 1
- [ ] Activate virtual environment
- [ ] Run `examples/00_hello_world.py`
- [ ] Read Lesson 00 & 01
- [ ] Do exercises for 00 & 01
- [ ] Complete Lesson 02 & 03

### Week 2
- [ ] Complete Lesson 04 & 05
- [ ] Complete Lesson 06 & 07
- [ ] Do corresponding exercises
- [ ] Review solutions

### Week 3
- [ ] Complete Lesson 08-11
- [ ] Start Functions exercises
- [ ] Begin Django setup
- [ ] Read Django Lesson 00

### Week 4+
- [ ] Continue with Django
- [ ] Build projects
- [ ] Move to intermediate topics

---

## 🐛 Troubleshooting

### Problem: "Python not found"
```powershell
# Check installation
python --version

# If not found, install from python.org
# Then restart terminal
```

### Problem: "Virtual environment not activating"
```powershell
# Recreate venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Problem: "Module not found"
```powershell
# Check requirements installed
pip install -r requirements.txt

# Check if in virtual environment
# (should see .venv prefix in prompt)
```

### Problem: "Django project not running"
```bash
cd projects/mastery_platform
python manage.py migrate
python manage.py runserver
```

---

## 📚 Resources

### Official Documentation
- Python: https://docs.python.org/3/
- Django: https://docs.djangoproject.com/
- DRF: https://www.django-rest-framework.org/

### Learning Resources
- Real Python: https://realpython.com/
- Django for Beginners: https://djangoforbeginners.com/
- GeeksforGeeks: https://www.geeksforgeeks.org/

### Tools
- VS Code: Code editor
- PyCharm Community: Full IDE
- Django Extensions: `pip install django-extensions`

---

## 💡 Pro Tips

1. **Test often** - Run examples after reading lessons
2. **Try exercises** - Don't skip them
3. **Compare solutions** - Understand different approaches
4. **Read errors** - Python tells you what's wrong
5. **Use REPL** - Test quick ideas
6. **Document code** - Add comments and docstrings
7. **Debug actively** - Use print() or pdb
8. **Version control** - Commit your work
9. **Take breaks** - Learning is mental work
10. **Join communities** - Python/Django Discord, Reddit

---

## 📞 When You're Stuck

### Check In Order
1. **Error message** - Read it carefully
2. **Lesson documentation** - Review the topic
3. **Example code** - Compare to your code
4. **Exercise hints** - Review hints provided
5. **Solution code** - See official solution
6. **Google** - Search the error
7. **Communities** - Ask for help

### Ask Better Questions
- What you tried
- What error you got
- Expected output vs actual
- Code snippet
- Python version

---

## ✨ Success Tips

✅ Code every day (even 30 minutes)
✅ Type code, don't copy-paste
✅ Test everything
✅ Read error messages
✅ Review solutions
✅ Build projects
✅ Take breaks
✅ Be patient with yourself
✅ Celebrate progress
✅ Keep learning

---

**Remember**: Everyone starts as a beginner. Keep coding! 🚀
