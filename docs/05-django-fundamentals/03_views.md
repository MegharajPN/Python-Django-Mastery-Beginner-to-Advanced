# Lesson 03: Views (Function-Based and Class-Based)

## 📖 What are Views?

A **view** is a Python function or class that handles HTTP requests and returns responses.

## 🔧 Function-Based Views (FBV)

### Basic View

```python
# accounts/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to our site!")
```

### Using render()

```python
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home',
        'message': 'Welcome!'
    }
    return render(request, 'home.html', context)
```

### Accessing Request Data

```python
def submit_form(request):
    if request.method == 'POST':
        # GET POST data
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # Process data
        return HttpResponse(f"Thank you, {name}!")
    else:
        return render(request, 'form.html')
```

### URL Parameters

```python
# urls.py
path('user/<int:user_id>/', views.user_detail, name='user_detail')

# views.py
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_detail.html', {'user': user})
```

## 🏛️ Class-Based Views (CBV)

### Basic CBV

```python
from django.views import View
from django.http import HttpResponse

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello!")
    
    def post(self, request):
        return HttpResponse("Data received")

# urls.py
path('hello/', HelloView.as_view(), name='hello')
```

### Generic Views

```python
from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 10

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'

# urls.py
path('articles/', ArticleListView.as_view(), name='article_list')
path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail')
```

### CRUD with CBVs

```python
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    success_url = '/posts/'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    success_url = '/posts/'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/posts/'
```

## 🔐 Login Required

### For Function-Based Views

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# urls.py
path('dashboard/', views.dashboard, name='dashboard')
```

### For Class-Based Views

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request):
        return render(request, 'dashboard.html')
```

## 🎓 FBV vs CBV

| Feature | FBV | CBV |
|---------|-----|-----|
| Simplicity | ✓ Simpler | Complex |
| Reusability | ✗ Limited | ✓ Good |
| Customization | ✓ Easy | Complex |
| Standard operations | ✗ Verbose | ✓ Built-in |

## 📝 Complete Example

```python
# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'
    ordering = '-created_at'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'blog_id'
```

## ✅ Summary

✅ Function-based views are simple
✅ Class-based views are powerful
✅ Generic views save time
✅ Decorators add functionality
✅ Mixins provide reusability
✅ Choose based on complexity

---

**Continue to [Lesson 04: Templates](04_templates.md)**
