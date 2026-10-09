# Lesson 01: Django Settings Configuration

## 📖 Understanding settings.py

The `settings.py` file controls all Django configuration for your project.

## 🔑 Key Settings

### DEBUG Mode

```python
# settings.py
DEBUG = True  # Development mode - shows detailed errors
DEBUG = False # Production - hides sensitive info
```

### ALLOWED_HOSTS

```python
# Allow specific domains
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'example.com',
    'www.example.com'
]
```

### INSTALLED_APPS

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Third-party
    'accounts',        # Your app
]
```

### DATABASES

```python
# SQLite (default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### SECRET_KEY

```python
# Never commit this!
SECRET_KEY = 'your-secret-key-here'

# In production, use environment variable
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
```

### MIDDLEWARE

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
```

### TEMPLATES

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]
```

### STATIC Files

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

### MEDIA Files

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### LOGGING

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
```

## 🌍 Environment-Based Settings

```python
# settings.py
import os
from pathlib import Path

# Development vs Production
ENV = os.environ.get('ENV', 'development')

if ENV == 'production':
    DEBUG = False
    ALLOWED_HOSTS = ['example.com']
else:
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

## 🔐 Security Settings

```python
# HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {
    'default-src': ("'self'",),
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
```

## 📊 REST Framework Settings

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

## ✅ Summary

✅ DEBUG - development vs production
✅ INSTALLED_APPS - register your apps
✅ DATABASES - database configuration
✅ STATIC_FILES - CSS, JavaScript, images
✅ SECRET_KEY - never commit
✅ MIDDLEWARE - request/response processing
✅ Environment-based configuration

---

**Continue to [Lesson 02: URL Routing](02_url_routing.md)**
