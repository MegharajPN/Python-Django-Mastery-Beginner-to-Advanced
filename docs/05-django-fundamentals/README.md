# Django Fundamentals - Complete Guide

Welcome to Django! This module teaches you how to build web applications.

## 📖 What is Django?

**Django** is a free, open-source Python web framework that helps you build web applications quickly and securely.

### What Can You Build?
- Websites with dynamic content
- RESTful APIs
- E-commerce platforms
- Social networks
- Real-time applications
- Content management systems

### Why Use Django?
✅ Fast to develop
✅ Secure by default
✅ Scalable
✅ Batteries-included (admin, ORM, testing)
✅ Huge ecosystem
✅ Used by Instagram, Pinterest, Spotify, Dropbox

## 🏗️ Django Architecture - MTV

Django follows the **MTV** pattern:

### Model
- Represents your database
- Defines data structure
- Written in Python (ORM)

### Template
- HTML files with dynamic content
- Jinja2 template language
- User interface

### View
- Business logic
- Processes requests
- Returns responses

```
User Request
    ↓
URLs (routing)
    ↓
View (logic)
    ↓
Model (database)
    ↓
Template (HTML)
    ↓
Response to User
```

## ✅ Getting Started

### 1. Django is Already Installed

Check installation:
```bash
python -m django --version
django-admin --version
```

### 2. Create Your First Django Project

```bash
cd projects
django-admin startproject mastery_platform
cd mastery_platform
```

This creates:
```
mastery_platform/
├── manage.py              # Project management script
└── mastery_platform/      # Project package
    ├── __init__.py
    ├── asgi.py           # ASGI config
    ├── settings.py       # Settings
    ├── urls.py           # URL routing
    └── wsgi.py           # WSGI config
```

### 3. Create Your First Django App

```bash
python manage.py startapp accounts
```

This creates:
```
accounts/
├── migrations/          # Database migrations
├── __init__.py
├── admin.py            # Admin interface config
├── apps.py             # App configuration
├── models.py           # Database models
├── tests.py            # Tests
├── views.py            # Views (business logic)
└── urls.py             # App-specific URLs
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

**Note**: The app won't be visible until registered in settings.

### 5. Register the App

Edit `mastery_platform/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',  # Add your app here
]
```

## 📚 Lesson Order

Work through the lessons in order:

1. **[00 - Project Setup](00_project_setup.md)** - Create a Django project
2. **[01 - Settings & Configuration](01_settings.md)** - Understand settings.py
3. **[02 - URL Routing](02_url_routing.md)** - Map URLs to views
4. **[03 - Views](03_views.md)** - Write function-based views
5. **[04 - Templates](04_templates.md)** - Create HTML templates
6. **[05 - Static Files](05_static_files.md)** - Manage CSS, JS, images
7. **[06 - Admin Interface](06_admin.md)** - Customize Django admin
8. **[07 - Models Basics](07_models_basics.md)** - Define data models
9. **[08 - Migrations](08_migrations.md)** - Manage database schema
10. **[09 - QuerySets](09_querysets.md)** - Query the database

## 📋 Key Django Concepts

### manage.py
Command-line utility for administrative tasks:
```bash
python manage.py migrate          # Apply migrations
python manage.py createsuperuser # Create admin user
python manage.py runserver       # Start dev server
python manage.py startapp        # Create new app
python manage.py shell           # Python interactive shell
```

### settings.py
Configuration file for your project:
- Database connection
- Installed apps
- Middleware
- Templates
- Static files
- Secret key

### urls.py
Maps URL paths to views:
```python
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
```

### views.py
Handles HTTP requests and returns responses:
```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")
```

### models.py
Defines database tables:
```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```

### templates/
HTML files with dynamic content:
```html
<h1>Hello, {{ name }}!</h1>
```

## 🔄 Request-Response Cycle

```
1. User visits URL (e.g., example.com/hello/)
                ↓
2. Django matches URL to a view (urls.py)
                ↓
3. View function receives the request
                ↓
4. View processes the request (queries database, etc.)
                ↓
5. View renders a template with data
                ↓
6. HTML response is sent back to browser
                ↓
7. Browser displays the page to user
```

## 💡 Best Practices

✅ Keep views thin—put logic in models
✅ Use templates for all HTML
✅ Follow Django naming conventions
✅ Don't commit `secrets.py` or `.env` files
✅ Use migrations for database changes
✅ Test your code with tests.py
✅ Use Django ORM instead of raw SQL when possible

## 🎯 Your First Django Project

We'll build a **Blog Application** with:
- Create, read, update, delete (CRUD) functionality
- User authentication
- Comments
- Tags
- Search functionality

## 📁 Complete Project Structure

```
mastery_platform/
├── manage.py
├── mastery_platform/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/accounts/
├── blog/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/blog/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── media/
│   └── uploads/
└── templates/
    └── base.html
```

## 🔗 Resources

- Official Django Docs: https://docs.djangoproject.com/
- Django for Beginners: https://djangoforbeginners.com/
- Real Python Django Tutorials: https://realpython.com/tutorials/django/

## 🎓 Learning Timeline

- **Lessons 1-3**: 1 day (setup, routing, views)
- **Lessons 4-6**: 1 day (templates, static files, admin)
- **Lessons 7-10**: 2 days (models, migrations, queries)

**Total**: 4 days to complete Django fundamentals

## ✨ Getting Started

👉 **Begin with [Lesson 00: Project Setup](00_project_setup.md)**

---

**Ready?** Create your first Django project → [Lesson 00: Project Setup](00_project_setup.md)
