# Django Deployment Guide

## 🚀 Local Development with Docker

### Prerequisites
- Docker installed
- Docker Compose installed
- Project cloned

### Start Services

```bash
# Build and start all services
docker-compose up -d

# Check if running
docker-compose ps

# View logs
docker-compose logs -f web
```

### Access Services

- **Django**: http://localhost:8000
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

### Migrations

```bash
# Run migrations
docker-compose exec web python projects/mastery_platform/manage.py migrate

# Create superuser
docker-compose exec web python projects/mastery_platform/manage.py createsuperuser

# Admin panel
# http://localhost:8000/admin/
```

### Stop Services

```bash
# Stop all services
docker-compose down

# Remove volumes too
docker-compose down -v
```

---

## 🌍 Production Deployment

### 1. Environment Setup

Create `.env` file:

```env
DEBUG=False
SECRET_KEY=your-very-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@db_host:5432/db_name
REDIS_URL=redis://redis_host:6379/0
```

### 2. Settings for Production

```python
# settings.py
import os

DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Static files
STATIC_ROOT = '/var/www/static/'
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = '/var/www/media/'
MEDIA_URL = '/media/'
```

### 3. Gunicorn Setup

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn (production)
gunicorn \
  --workers 4 \
  --bind 0.0.0.0:8000 \
  --timeout 120 \
  mastery_platform.wsgi:application
```

### 4. Nginx Configuration

```nginx
upstream django {
    server web:8000;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    # SSL certificates
    ssl_certificate /etc/ssl/certs/cert.pem;
    ssl_certificate_key /etc/ssl/private/key.pem;
    
    # Static files
    location /static/ {
        alias /var/www/static/;
    }
    
    # Media files
    location /media/ {
        alias /var/www/media/;
    }
    
    # Django application
    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 5. Database Migration in Production

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

### 6. Monitor and Maintain

```bash
# Check Django logs
tail -f /var/log/django/error.log

# Check Celery workers
celery -A mastery_platform inspect active

# Check Redis connection
redis-cli ping
```

---

## 🔒 Security Checklist

- [ ] Set `DEBUG = False`
- [ ] Set strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Enable HTTPS/SSL
- [ ] Set secure cookies
- [ ] Configure CORS if needed
- [ ] Set up proper logging
- [ ] Monitor for errors
- [ ] Regular backups
- [ ] Update dependencies

---

## 📊 Performance Optimization

### Caching

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Database Optimization

```python
# Use select_related for ForeignKey
users = User.objects.select_related('profile').all()

# Use prefetch_related for ManyToMany
posts = Post.objects.prefetch_related('comments').all()

# Use only() to fetch specific fields
users = User.objects.only('id', 'username', 'email')
```

### Response Caching

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # Cache for 5 minutes
def expensive_view(request):
    return render(request, 'template.html')
```

---

## 🆘 Troubleshooting

### 500 Error
- Check logs: `tail -f error.log`
- Check settings: DEBUG=True locally
- Check database connection
- Run migrations

### Static files not loading
- Run: `python manage.py collectstatic`
- Check STATIC_URL and STATIC_ROOT
- Check Nginx configuration

### Database connection error
- Verify DATABASE_URL
- Check PostgreSQL is running
- Check credentials

---

**Deployment Complete!** 🎉
