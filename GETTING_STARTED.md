# Getting Started - Python & Django Backend Mastery

Welcome! You now have a complete, production-ready learning environment set up. This guide will help you get started.

## ✅ What's Been Set Up

Your Python-Django learning repository includes:

### 1. **Virtual Environment**
```
.venv/          # Python virtual environment with all dependencies installed
```

**Status**: ✅ Created and ready to use

**Installed Packages**:
- Django 4.2.15
- Django REST Framework 3.14
- pytest 7.4.4
- requests 2.31.0
- python-dotenv 1.0.0
- ... and 20+ other packages

### 2. **Complete Documentation**
```
docs/
├── 01-python-basics/       # 15 Python lessons with examples
├── 02-python-intermediate/ # OOP, decorators, testing
├── 03-python-advanced/     # Async, threading, performance
├── 05-django-fundamentals/ # Django basics (4+ lessons started)
├── 06-django-orm-and-crud/ # Models, queries, forms
├── 07-authentication-and-security/
├── 08-django-rest-framework/
├── 09-redis-and-caching/
├── 10-celery-and-job-scheduling/
├── 11-testing/
├── 12-system-design/
├── 13-docker-and-deployment/
└── 14-interview-preparation/
```

**Status**: ✅ Framework created, Python basics and Django fundamentals lessons started

### 3. **Example Code**
```
examples/
├── 00_hello_world.py       # ✅ Simple print statement
├── 01_variables.py         # ✅ Data types demo
├── 01_type_conversion.py   # ✅ Type conversion
└── 02_operators.py         # ✅ All operators
```

**Status**: ✅ First 4 examples created and tested (all working!)

### 4. **Exercises**
```
exercises/
├── 00_introduction.py      # ✅ Starter exercise (with hints)
└── 01_student_profile.py   # ✅ Student profile exercise
```

**Status**: ✅ First 2 exercises created with detailed instructions

### 5. **Solutions**
```
solutions/
├── 00_introduction.py      # ✅ Solution
└── 01_student_profile.py   # ✅ Solution with comments
```

**Status**: ✅ Solutions available for reference

### 6. **Initial Django Project**
```
projects/mastery_platform/
├── manage.py               # ✅ Project management script
├── db.sqlite3              # ✅ Database with migrations applied
├── mastery_platform/       # ✅ Project package
│   ├── __init__.py
│   ├── settings.py         # ✅ Updated (accounts app registered)
│   ├── urls.py             # ✅ Main URL routing
│   ├── asgi.py
│   └── wsgi.py
└── accounts/               # ✅ First Django app created
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

**Status**: ✅ Django project created, migrations applied, ready to use

### 7. **Project Structure**
```
Python-Django/
├── README.md              # Main project guide
├── PROGRESS.md            # Track your learning
├── LEARNING_ROADMAP.md    # 26-week learning plan
├── GETTING_STARTED.md     # This file
├── requirements.txt       # Dependencies (23 packages)
├── .env.example           # Environment template
├── .gitignore             # Git ignore rules
├── .venv/                 # Virtual environment ✅
├── docs/                  # Documentation ✅
├── examples/              # Code examples ✅
├── exercises/             # Exercises ✅
├── solutions/             # Solutions ✅
├── projects/              # Mini & major projects
│   └── mastery_platform/  # Main Django project ✅
├── tests/                 # Test suite
├── scripts/               # Utility scripts
└── advanced_backend/      # Advanced project (starter)
```

**Status**: ✅ Complete structure created

---

## 🚀 Quick Start (First 5 Minutes)

### 1. Open Terminal in Project Directory

**Windows (PowerShell)**:
```powershell
cd C:\Users\Administrator\Desktop\Python-Django
```

### 2. Activate Virtual Environment

**Windows (PowerShell)**:
```powershell
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the start of your prompt.

### 3. Run Your First Python Example

```bash
python examples/00_hello_world.py
```

**Expected Output**:
```
Hello, World!
Welcome to Python!

This is example 00_hello_world.py
```

### 4. Run Your First Django Project

```bash
cd projects\mastery_platform
python manage.py runserver
```

**Expected Output**:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

October 09, 2026 - 11:00:00
Django version 4.2.15, using settings 'mastery_platform.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Visit `http://127.0.0.1:8000/` in your browser. You'll see the Django welcome page.

Press **Ctrl+Break** (or **Ctrl+C**) to stop the server.

---

## 📚 Your Learning Path

### Phase 1: Python Fundamentals (This Week!)

**What you'll learn**:
- Variables and data types
- Operators
- Strings
- Lists, tuples, dicts
- Control flow (if/else, loops)
- Functions
- Exception handling
- File I/O

**How to start**:

1. Read the overview: `docs/01-python-basics/README.md`
2. Read Lesson 00: `docs/01-python-basics/00_interpreter.md`
3. Read Lesson 01: `docs/01-python-basics/01_variables_and_types.md`
4. Run the examples:
   ```bash
   python examples/00_hello_world.py
   python examples/01_variables.py
   python examples/01_type_conversion.py
   ```
5. Do the exercises:
   ```bash
   # Edit and solve
   python exercises/00_introduction.py
   python exercises/01_student_profile.py
   ```
6. Check solutions:
   ```bash
   python solutions/00_introduction.py
   python solutions/01_student_profile.py
   ```

### Phase 2: Learn to Run Tests

Install pytest (already installed):
```bash
pytest --version
```

Run example tests:
```bash
pytest exercises/ -v
```

### Phase 3: Django Basics (Next Week)

**Start Here**:
1. Read: `docs/05-django-fundamentals/README.md`
2. Read: `docs/05-django-fundamentals/00_project_setup.md`
3. Explore the created project:
   ```bash
   cd projects/mastery_platform
   python manage.py shell
   # Now you have an interactive Python shell with Django loaded!
   ```

### Phase 4: Build Projects

After fundamentals, build real projects:
- Blog application
- Employee API
- E-commerce API
- ... and more!

---

## 🛠️ Essential Commands

### Python & Virtual Environment

```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1          # Windows PowerShell

# Run Python script
python examples/00_hello_world.py

# Run Python interactive shell (REPL)
python

# Exit REPL
exit()
```

### Django

```bash
# Start Django development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Django shell (interactive)
python manage.py shell

# Run tests
python manage.py test

# View SQL for a queryset
python manage.py sqlshell
```

### Testing

```bash
# Run all tests
pytest

# Run tests in a directory
pytest exercises/

# Run tests with verbose output
pytest -v

# Run tests with coverage
pytest --cov=

# Run a specific test
pytest exercises/00_introduction.py
```

### Git (When You're Ready)

```bash
# Initialize repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial project setup"

# View history
git log
```

---

## 📊 Progress Tracking

Update `PROGRESS.md` as you complete sections:

```markdown
## Phase 1: Python Fundamentals

### Week 1: Python Basics
- [x] Variables and data types
- [x] Operators
- [ ] Strings (IN PROGRESS)
- [ ] Type conversion (COMING NEXT)
```

Check your progress:
```bash
cat PROGRESS.md
```

---

## 📖 Documentation Files You Should Read Today

Priority order:

1. **`README.md`** (5 min) - Overview of the project
2. **`LEARNING_ROADMAP.md`** (10 min) - 26-week learning plan
3. **`docs/01-python-basics/README.md`** (10 min) - Python basics overview
4. **`docs/01-python-basics/00_interpreter.md`** (15 min) - First Python lesson

**Total**: ~40 minutes to understand the full scope.

---

## 🎯 Your First 24 Hours

### Hour 0-1: Setup & Exploration
- [ ] Read `README.md` and `LEARNING_ROADMAP.md`
- [ ] Explore project structure with file explorer
- [ ] Verify Python installation
- [ ] Run `python examples/00_hello_world.py`

### Hour 1-2: Python Basics - Lesson 00
- [ ] Read `docs/01-python-basics/README.md`
- [ ] Read `docs/01-python-basics/00_interpreter.md`
- [ ] Understand how Python works
- [ ] Experiment with Python REPL (`python`)

### Hour 2-3: Python Basics - Lesson 01
- [ ] Read `docs/01-python-basics/01_variables_and_types.md`
- [ ] Run examples: `01_variables.py`, `01_type_conversion.py`
- [ ] Understand data types

### Hour 3-4: Exercise & Practice
- [ ] Do exercise `00_introduction.py`
- [ ] Compare with solution
- [ ] Do exercise `01_student_profile.py`
- [ ] Modify exercises and experiment

### Hour 4-5: Operators
- [ ] Read `docs/01-python-basics/02_operators.md`
- [ ] Run `examples/02_operators.py`
- [ ] Do operator exercises

### Hour 5+: Continue Learning
- [ ] Update `PROGRESS.md` with what you've learned
- [ ] Move to next lessons: strings, lists, dictionaries
- [ ] Keep coding!

---

## 🆘 Troubleshooting

### Virtual Environment Not Activating

**Windows PowerShell** - If you get an error about ExecutionPolicy:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

### Python Not Found

Verify Python is installed:
```bash
python --version
```

If not found, reinstall Python from python.org (make sure to add to PATH).

### Django Not Found

Make sure virtual environment is activated and requirements installed:
```bash
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### ImportError When Running Examples

Make sure you're in the project root directory:
```bash
cd C:\Users\Administrator\Desktop\Python-Django
python examples/00_hello_world.py  # ✅ This works
```

Not from subdirectories:
```bash
cd C:\Users\Administrator\Desktop\Python-Django\examples
python 00_hello_world.py  # ❌ Might have import issues
```

---

## 💡 Tips for Success

1. **Type Code Yourself**: Don't copy-paste. Typing builds muscle memory.
2. **Run Every Example**: Seeing output helps understanding.
3. **Experiment**: Change values and see what happens.
4. **Use REPL**: Test quick ideas with `python` interactive mode.
5. **Read Error Messages**: They tell you exactly what's wrong.
6. **Take Breaks**: Learning is hard. Rest helps your brain process.
7. **Code Every Day**: 30 minutes daily > 6 hours on weekend.
8. **Join Communities**: Python Discord, Reddit r/learnprogramming.
9. **Ask Questions**: No question is stupid.
10. **Build Projects**: Apply learning to real problems.

---

## 📞 Getting Help

### If You're Stuck

1. **Re-read the lesson**: Maybe something wasn't clear the first time
2. **Check the example**: Run it and compare to your code
3. **Read error messages**: Python tells you exactly what's wrong
4. **Google the error**: Most errors have been solved before
5. **Ask in communities**: Python Discord, Stack Overflow, Reddit

### Useful Resources

- **Official Python Docs**: https://docs.python.org/3/
- **Python Real Python**: https://realpython.com/
- **Django Official Docs**: https://docs.djangoproject.com/
- **Stack Overflow**: https://stackoverflow.com/
- **Python Discord**: https://discordapp.com/invite/python

---

## 🎓 Next Steps

1. **Right Now** (5 min): Activate virtual environment and run first example
2. **Today** (1-2 hours): Complete Python Basics Lessons 00-01
3. **Tomorrow** (2-3 hours): Complete Operators Lesson and exercises
4. **This Week**: Complete all Python Fundamentals (Lessons 0-14)
5. **Next Week**: Start Python Intermediate or Django Fundamentals

---

## 📝 Checklist

Before you start, make sure:

- [ ] Virtual environment is activated (see `(.venv)` in prompt)
- [ ] Python works: `python --version` shows 3.11+
- [ ] Django works: `django-admin --version` shows 4.2+
- [ ] Examples run: `python examples/00_hello_world.py` works
- [ ] Django runs: `python manage.py runserver` starts successfully
- [ ] You've read `LEARNING_ROADMAP.md`
- [ ] You understand the project structure
- [ ] You know where to find documentation

---

## 🚀 You're Ready!

Everything is set up. You have:

✅ Complete learning environment
✅ Working Python installation
✅ Working Django project
✅ All documentation
✅ Examples that work
✅ Exercises to practice
✅ Solutions for reference

**The only thing left is to start coding.**

---

### 👉 **Begin Your Journey**

**Next Action**: 
1. Activate venv: `.\.venv\Scripts\Activate.ps1`
2. Run example: `python examples/00_hello_world.py`
3. Read lesson: `docs/01-python-basics/00_interpreter.md`

**Good luck!** You've got this! 🚀

---

**Last Updated**: 2026-10-09
**Total Setup Time**: ~2 hours
**Your Commitment**: 20-26 weeks, 8-11 hours/week
**Your Reward**: Professional Python/Django developer skills
