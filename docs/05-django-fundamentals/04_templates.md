# Lesson 04: Templates (HTML with Django)

## 📖 What are Templates?

**Templates** are HTML files with Django template syntax for dynamic content.

## 📝 Basic Template

```html
<!-- accounts/templates/accounts/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome, {{ user.first_name }}!</h1>
    <p>{{ message }}</p>
</body>
</html>
```

## 🔄 Template Variables

Pass data from view to template:

```python
# views.py
def profile(request):
    context = {
        'user': request.user,
        'title': 'User Profile'
    }
    return render(request, 'profile.html', context)

# template
<h1>{{ title }}</h1>
<p>Name: {{ user.first_name }} {{ user.last_name }}</p>
```

## 🔀 Conditionals

```html
{% if user.is_authenticated %}
    <p>Welcome back, {{ user.username }}!</p>
{% else %}
    <p><a href="{% url 'login' %}">Login</a></p>
{% endif %}

{% if articles %}
    <h2>{{ articles|length }} articles found</h2>
{% else %}
    <p>No articles available</p>
{% endif %}
```

## 🔄 Loops

```html
<ul>
    {% for item in items %}
        <li>{{ item.name }} - ${{ item.price }}</li>
    {% empty %}
        <li>No items available</li>
    {% endfor %}
</ul>
```

## 🏛️ Template Inheritance

### Base Template

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Site</h1>
    </header>
    
    {% block content %}
    {% endblock %}
    
    <footer>
        <p>&copy; 2026 My Site</p>
    </footer>
</body>
</html>
```

### Child Template

```html
<!-- home.html -->
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
    <h2>Welcome!</h2>
    <p>{{ message }}</p>
{% endblock %}
```

## 🔧 Template Filters

Transform data in templates:

```html
{{ text|upper }}              <!-- HELLO -->
{{ text|lower }}              <!-- hello -->
{{ text|capfirst }}           <!-- Hello -->
{{ items|length }}            <!-- 5 -->
{{ price|floatformat:2 }}     <!-- 19.99 -->
{{ date|date:"Y-m-d" }}       <!-- 2026-10-09 -->
```

## 📋 Template Tags

```html
<!-- Load static files -->
{% load static %}
<img src="{% static 'images/logo.png' %}">

<!-- URL reverse -->
<a href="{% url 'user_detail' user_id %}">Profile</a>

<!-- Include another template -->
{% include 'sidebar.html' %}

<!-- Set variable -->
{% with total=business.employees.count %}
    Total employees: {{ total }}
{% endwith %}
```

## 📝 Complete Example

```html
<!-- articles/list.html -->
{% extends "base.html" %}

{% block title %}Articles{% endblock %}

{% block content %}
<h2>Articles</h2>

{% if articles %}
    <ul>
    {% for article in articles %}
        <li>
            <h3>{{ article.title }}</h3>
            <p>{{ article.content|truncatewords:20 }}</p>
            <a href="{% url 'article_detail' article.id %}">Read More</a>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>No articles found.</p>
{% endif %}
{% endblock %}
```

## ✅ Summary

✅ Templates contain dynamic content
✅ Pass context from views
✅ Use {{ }} for variables
✅ Use {% %} for logic
✅ Template inheritance for consistency
✅ Filters transform data

---

**Continue to [Lesson 05: Static Files](05_static_files.md)**
