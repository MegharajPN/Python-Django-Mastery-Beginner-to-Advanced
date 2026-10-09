# Project 01: Django CRUD Application

## 📖 Overview

Build a complete CRUD (Create, Read, Update, Delete) application for managing tasks.

## 🎯 Learning Goals

- Create Django models
- Build CRUD views
- Create HTML forms
- Handle form validation
- Implement pagination
- Add search functionality

## 📋 Features to Build

1. **Task Model**
   - Title (CharField)
   - Description (TextField)
   - Completed (BooleanField)
   - Created (DateTimeField)
   - Updated (DateTimeField)

2. **Task Views**
   - List all tasks
   - Create new task
   - View task detail
   - Update task
   - Delete task

3. **User Interface**
   - List page with search
   - Create form
   - Edit form
   - Confirmation delete

## 🚀 Quick Start

### 1. Create Project Structure

```bash
cd projects/01-django-crud
django-admin startproject taskmanager
cd taskmanager
python manage.py startapp tasks
```

### 2. Create Model

```python
# tasks/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title
```

### 3. Create Views

```python
# tasks/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
```

### 4. Create Forms

```python
# tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
```

### 5. Create URLs

```python
# tasks/urls.py
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]
```

## 📝 Templates to Create

1. **task_list.html** - List all tasks with links
2. **task_form.html** - Create/edit form
3. **task_detail.html** - View single task
4. **task_confirm_delete.html** - Confirm deletion

## 🧪 Testing

```bash
# Run tests
python manage.py test

# Create test data
python manage.py shell
```

## 🎓 What You'll Learn

✅ Django models and migrations
✅ CRUD operations
✅ Forms and validation
✅ URL routing
✅ Template rendering
✅ Database queries

## 📊 Completion Checklist

- [ ] Model created and migrated
- [ ] All 5 CRUD views working
- [ ] Forms validated
- [ ] Templates created
- [ ] URLs configured
- [ ] Tests written
- [ ] Application running

---

**Start building!** 🚀
