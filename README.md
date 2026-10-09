# Python & Django Backend Mastery

A comprehensive, hands-on learning repository for becoming a professional Python and Django backend developer.

## 📚 What's Inside

This repository contains:

- **Python Curriculum**: Beginner → Intermediate → Advanced
- **Django Curriculum**: Fundamentals → Advanced Features → Production Deployment
- **Practical Projects**: Real-world applications built step-by-step
- **Interview Preparation**: Questions, coding challenges, system design
- **Complete Documentation**: Explanations, code examples, exercises, solutions
- **Testing & Best Practices**: Unit tests, integration tests, debugging

## 🚀 Quick Start

### 1. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
python --version
django-admin --version
pytest --version
```

## 📖 Learning Path

### Phase 1: Python Fundamentals (Weeks 1-3)
- Variables, data types, operators
- Control flow (if/else, loops)
- Functions and scope
- Data structures (lists, dicts, sets, tuples)
- Exception handling
- File I/O and JSON

**Start here:** `docs/01-python-basics/README.md`

### Phase 2: Python Intermediate (Weeks 4-6)
- Object-oriented programming
- Decorators and generators
- List/dict comprehensions
- Type hints and dataclasses
- Regular expressions
- Unit testing with pytest

**Start here:** `docs/02-python-intermediate/README.md`

### Phase 3: Python Advanced (Weeks 7-9)
- Asynchronous programming (asyncio)
- Threading and multiprocessing
- Memory management
- Performance optimization
- Design patterns

**Start here:** `docs/03-python-advanced/README.md`

### Phase 4: Django Fundamentals (Weeks 10-12)
- Django project structure
- MTV architecture
- Models, views, templates
- URL routing
- Django ORM basics

**Start here:** `docs/05-django-fundamentals/README.md`

### Phase 5: Django ORM & CRUD (Weeks 13-15)
- Models and fields
- Migrations
- QuerySets and filtering
- Relationships (1-to-1, 1-to-many, many-to-many)
- Aggregations and annotations

**Start here:** `docs/06-django-orm-and-crud/README.md`

### Phase 6: Authentication & Security (Weeks 16-17)
- User authentication
- Permissions and decorators
- Sessions and cookies
- Password hashing
- CSRF protection

**Start here:** `docs/07-authentication-and-security/README.md`

### Phase 7: Django REST Framework (Weeks 18-20)
- Serializers
- API views and ViewSets
- Routers and URL patterns
- Pagination and filtering
- Authentication (JWT)

**Start here:** `docs/08-django-rest-framework/README.md`

### Phase 8: Advanced Topics (Weeks 21-26)
- Redis caching
- Celery and background tasks
- WebSockets and real-time updates
- Testing and debugging
- Docker and deployment

**Start here:** `docs/09-redis-and-caching/README.md`

## 🎯 Learning Approach

Each topic follows this structure:

1. **Concept Explanation**: What it is and why it matters
2. **Runnable Examples**: Small code you can execute immediately
3. **Code Walkthrough**: Line-by-line explanation
4. **Practical Exercise**: Implement something yourself
5. **Hints & Solutions**: Separate solution files
6. **Integration**: Add it to the main project
7. **Tests**: Write and run tests
8. **Interview Questions**: Common interview questions with answers

## 📁 Directory Structure

```
python-django-mastery/
├── README.md                 # This file
├── PROGRESS.md              # Track your learning progress
├── requirements.txt         # Project dependencies
├── .env.example             # Environment variable template
├── .venv/                   # Virtual environment
│
├── docs/                    # Complete documentation
│   ├── 00-setup/           # Setup and installation
│   ├── 01-python-basics/   # Python fundamentals
│   ├── 02-python-intermediate/
│   ├── 03-python-advanced/
│   ├── 04-sql-and-databases/
│   ├── 05-django-fundamentals/
│   ├── 06-django-orm-and-crud/
│   ├── 07-authentication-and-security/
│   ├── 08-django-rest-framework/
│   ├── 09-redis-and-caching/
│   ├── 10-celery-and-job-scheduling/
│   ├── 11-testing/
│   ├── 12-system-design/
│   ├── 13-docker-and-deployment/
│   └── 14-interview-preparation/
│
├── examples/                # Runnable code examples
├── exercises/               # Exercise problems
├── solutions/               # Solution code
├── projects/                # Mini and major projects
├── advanced_backend/        # Main mastery platform
├── tests/                   # Test suites
└── scripts/                 # Utility scripts
```

## 📊 Progress Tracking

Check `PROGRESS.md` to see what's been learned and what's coming next.

## 🛠️ Tools & Technologies

- **Python**: 3.11+
- **Django**: 4.2 LTS
- **Django REST Framework**: 3.14
- **PostgreSQL**: Production database
- **Redis**: Caching and job queue
- **Celery**: Background task processing
- **Docker**: Containerization
- **pytest**: Testing framework

## 📝 Key Principles

✅ **Learn by Doing**: Every concept has runnable code
✅ **Real-World Examples**: Projects based on actual applications
✅ **Complete Documentation**: Every file is documented
✅ **Step-by-Step**: Start simple, gradually increase complexity
✅ **Best Practices**: Follow Django and Python conventions
✅ **Production Ready**: Code follows professional standards

## 💡 Tips for Success

1. **Code Along**: Don't just read—type out the examples
2. **Experiment**: Modify examples and see what happens
3. **Do Exercises**: Don't skip—exercises build muscle memory
4. **Run Tests**: Verify your code works with tests
5. **Understand WHY**: Read explanations, not just HOW
6. **Build Projects**: Apply concepts to real projects
7. **Debug**: Use the debugger to understand code flow
8. **Ask Questions**: If confused, review concepts again

## 🔗 Resources

- Official Django Documentation: https://docs.djangoproject.com/
- Python Official Docs: https://docs.python.org/3/
- Django REST Framework: https://www.django-rest-framework.org/
- Real Python Tutorials: https://realpython.com/
- Celery Documentation: https://docs.celeryproject.org/

## 📬 Getting Help

If stuck:
1. Re-read the concept explanation
2. Check the runnable examples
3. Look at the solution code
4. Review the interview Q&A section
5. Search the documentation

## 🎓 Learning Goals

By completing this repository, you will:

- ✅ Master Python from basics to advanced
- ✅ Build production-grade Django applications
- ✅ Design RESTful APIs with Django REST Framework
- ✅ Implement caching, background jobs, and real-time features
- ✅ Write tests and debug like a professional
- ✅ Deploy applications with Docker and production servers
- ✅ Handle authentication, authorization, and security
- ✅ Optimize performance and manage databases
- ✅ Ace technical interviews

## 📅 Estimated Timeline

- **Beginner**: 3 weeks (Python basics)
- **Intermediate**: 3 weeks (Python intermediate + Django intro)
- **Advanced**: 8 weeks (Advanced Python, Django advanced, projects)
- **Specialization**: 6 weeks (Caching, async, deployment)

**Total**: ~20 weeks (5 months) of consistent study

## ✨ Start Your Journey

Begin with Phase 1: **`docs/01-python-basics/README.md`**

Good luck! 🚀
