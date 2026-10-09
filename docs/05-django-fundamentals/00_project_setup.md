# Lesson 00: Django Project Setup

## 📖 What You'll Learn

In this lesson:
- Create your first Django project
- Create your first Django app
- Understand project structure
- Run the development server
- Register an app

## 🚀 Step 1: Create a Django Project

A **project** is a complete Django application. A **project** contains one or more **apps**.

Navigate to the projects folder:

```bash
cd C:\Users\Administrator\Desktop\Python-Django\projects
```

Create a new project:

```bash
django-admin startproject mastery_platform
cd mastery_platform
```

This creates:
```
mastery_platform/
├── manage.py              # Project CLI
├── mastery_platform/      # Project package
│   ├── __init__.py
│   ├── asgi.py           # ASGI application
│   ├── settings.py       # Configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI application
└── db.sqlite3            # Database (created later)
```

## 📝 Understanding Each File

### `manage.py`
Command-line utility for project management:
- Run server: `python manage.py runserver`
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Create admin: `python manage.py createsuperuser`

### `settings.py`
Configuration file with:
- `DEBUG`: Development mode (True) or production (False)
- `ALLOWED_HOSTS`: Allowed domain names
- `INSTALLED_APPS`: List of installed apps
- `DATABASES`: Database configuration
- `SECRET_KEY`: Secret key (never commit this!)

### `urls.py`
URL routing configuration:
```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

### `asgi.py` and `wsgi.py`
Interfaces for web servers (don't modify for now).

## 🎯 Step 2: Create Your First App

An **app** is a module in your project that does something specific.

Inside the `mastery_platform` directory:

```bash
python manage.py startapp accounts
```

This creates:
```
accounts/
├── migrations/          # Database migrations folder
│   └── __init__.py
├── __init__.py
├── admin.py            # Admin configuration
├── apps.py             # App configuration
├── models.py           # Database models
├── tests.py            # Tests
├── urls.py             # App-specific URLs (create this)
└── views.py            # Views (business logic)
```

## 🔧 Step 3: Register the App

Tell Django about your new app by adding it to `INSTALLED_APPS` in `settings.py`.

Edit `mastery_platform/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',  # Add this line
]
```

## 💾 Step 4: Initial Database Setup

Django comes with default tables. Create them:

```bash
python manage.py migrate
```

Output:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

This creates `db.sqlite3` with Django's default tables.

## 🌐 Step 5: Run the Development Server

```bash
python manage.py runserver
```

Output:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

October 09, 2026 - 10:30:00
Django version 4.2.15, using settings 'mastery_platform.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Visit `http://127.0.0.1:8000/` in your browser. You'll see:

```
The install worked successfully! Congratulations!

You are now running Django 4.2.15

Next, start your first app by running python manage.py startapp [app_name].
```

Stop the server with **Ctrl+C**.

## ✅ Step 6: Create Your First View

A **view** handles HTTP requests and returns responses.

Edit `accounts/views.py`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Django!")
```

## 🔗 Step 7: Create URLs for Your App

Create file `accounts/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

## 🔀 Step 8: Include App URLs in Project URLs

Edit `mastery_platform/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```

## 🧪 Step 9: Test Your View

Run the server again:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and you'll see:

```
Hello from Django!
```

**Success!** You've created your first Django view.

## 📊 Project Structure After Setup

```
Python-Django/
├── projects/
│   └── mastery_platform/
│       ├── manage.py
│       ├── db.sqlite3
│       ├── mastery_platform/
│       │   ├── __init__.py
│       │   ├── asgi.py
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       └── accounts/
│           ├── migrations/
│           ├── __init__.py
│           ├── admin.py
│           ├── apps.py
│           ├── models.py
│           ├── tests.py
│           ├── urls.py  # Created
│           └── views.py # Modified
```

## 🎓 Common Mistakes

### ❌ Mistake 1: Forgetting to register app
If the app isn't in `INSTALLED_APPS`, Django won't recognize it.

### ❌ Mistake 2: Missing `include()` in URLs
Without `include()`, app URLs won't be included in project URLs.

### ❌ Mistake 3: Forgetting to create `urls.py` in app
Each app should have its own `urls.py` file.

### ❌ Mistake 4: Not running migrations
Django requires initial migrations for built-in apps.

## 🏃 Practical Exercise

**Task**: Create a second app and a view

**Steps**:
1. Create app: `python manage.py startapp blog`
2. Add to `INSTALLED_APPS` in settings.py
3. Create view in `blog/views.py` that returns "Blog Home"
4. Create `blog/urls.py` with a route
5. Include in `mastery_platform/urls.py` at `path('blog/', include('blog.urls'))`
6. Test at `http://127.0.0.1:8000/blog/`

## ✅ Summary

✅ Created Django project with `django-admin startproject`
✅ Created app with `python manage.py startapp`
✅ Registered app in `INSTALLED_APPS`
✅ Ran migrations with `python manage.py migrate`
✅ Created first view
✅ Set up URL routing
✅ Ran development server

## 🎯 What's Next?

→ **[Lesson 01: Settings and Configuration](01_settings.md)**

In the next lesson:
- Understand `settings.py`
- Configure databases
- Debug mode
- Allowed hosts
- Secret key

---

**Ready?** Continue to [Lesson 01: Settings & Configuration](01_settings.md)
