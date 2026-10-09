# Lesson 02: URL Routing with path() and include()

## 📖 How URLs Work in Django

When a user visits a URL, Django routes it to the appropriate view.

```
User visits: http://example.com/hello/
        ↓
Django matches against urls.py patterns
        ↓
Finds matching path: 'hello/'
        ↓
Calls the view function
        ↓
View returns response
        ↓
User sees response
```

## 🔗 Basic URL Pattern

### Project URLs

```python
# mastery_platform/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```

### App URLs

```python
# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

## 📝 URL with Variables

Capture values from URL:

```python
# accounts/urls.py
urlpatterns = [
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
]

# accounts/views.py
def user_detail(request, user_id):
    return HttpResponse(f"User {user_id}")

def post_detail(request, slug):
    return HttpResponse(f"Post: {slug}")
```

## 🔄 URL Converters

| Converter | Matches | Example |
|-----------|---------|---------|
| `int` | Integer | `/user/123/` |
| `str` | String | `/post/hello-world/` |
| `slug` | Slug | `/post/hello-world/` |
| `uuid` | UUID | `/item/abc123def/` |
| `path` | Path with slashes | `/files/docs/report.pdf` |

## 🔀 URL Namespaces

Organize URLs by app:

```python
# mastery_platform/urls.py
urlpatterns = [
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('blog/', include(('blog.urls', 'blog'))),
]

# accounts/urls.py
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
]

# blog/urls.py
app_name = 'blog'
urlpatterns = [
    path('', views.list_posts, name='list'),
    path('<int:post_id>/', views.detail, name='detail'),
]

# In template:
# <a href="{% url 'accounts:login' %}">Login</a>
# <a href="{% url 'blog:detail' post_id=5 %}">Post</a>
```

## 🏷️ Naming URLs

Give names to URLs for reverse lookup:

```python
# urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
]

# In views
from django.urls import reverse

url = reverse('home')  # '/'
url = reverse('user_detail', args=[123])  # '/user/123/'

# In templates
<a href="{% url 'home' %}">Home</a>
<a href="{% url 'user_detail' user_id %}">Profile</a>
```

## 📋 Regular Expressions (Advanced)

```python
from django.urls import re_path

urlpatterns = [
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
]
```

## 📝 Complete Example

```python
# mastery_platform/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'))),
    path('auth/', include(('accounts.urls', 'accounts'))),
]

# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
]

# accounts/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def profile(request, user_id):
    # Get user and render
    return HttpResponse(f"Profile of user {user_id}")
```

## ✅ Summary

✅ path() - simple URL patterns
✅ include() - include app URLs
✅ URL converters - int, str, slug, uuid
✅ URL names - reverse lookups
✅ Namespaces - organize URLs
✅ URL parameters - capture from URL

---

**Continue to [Lesson 03: Views](03_views.md)**
