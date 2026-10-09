# Interview Preparation Guide

## 🎯 Overview

Complete interview preparation for Python and Django positions.

## 📚 Sections

### Python Questions (50+)
- Language fundamentals
- OOP concepts
- Decorators and generators
- Asyncio and concurrency
- Data structures
- Common modules

### Django Questions (40+)
- Project architecture
- ORM and queries
- Request lifecycle
- Signals and middleware
- Authentication
- Performance optimization

### Django REST Framework (30+)
- Serializers
- Views and ViewSets
- Authentication and permissions
- API design patterns

### System Design (20+)
- Scalability
- Database design
- Caching strategies
- Message queues
- Monitoring

### Coding Problems (30+)
- Easy problems (10)
- Medium problems (10)
- Hard problems (10)

---

## 🎓 Sample Questions

### Python Basics
**Q: What's the difference between a list and a tuple?**
- Lists are mutable, tuples are immutable
- Tuples are hashable (can be dict keys)
- Tuples have slightly better performance

**Q: Explain decorators**
- Functions that modify other functions
- Used for logging, timing, validation
- Use @decorator syntax

### Django
**Q: What is a migration?**
- Django's way of propagating database schema changes
- Created with `makemigrations`
- Applied with `migrate`

**Q: Explain the request-response cycle**
1. Client sends request
2. URL routing matches pattern
3. View processes request
4. Template renders with data
5. Response sent to client

### Coding Challenge Example
**Problem: Find the two numbers that sum to a target**
```python
def two_sum(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return [seen[complement], nums.index(num)]
        seen[num] = nums.index(num)
    return None
```

---

## 📖 How to Use

1. **Study sections in order**: Python → Django → System Design
2. **Answer questions out loud**: Explain your thinking
3. **Write code solutions**: Practice coding problems
4. **Time yourself**: Interview conditions
5. **Review weak areas**: Focus on gaps

## ⏱️ Mock Interview Timeline

- **30 min**: Warm-up questions (5-10 easy)
- **45 min**: Technical discussion (3-5 medium)
- **30 min**: Coding problem (1 hard)
- **15 min**: Questions for interviewer

---

## 🎯 Success Metrics

✅ Answer fundamental questions confidently
✅ Explain architecture decisions
✅ Solve medium problems in 20 minutes
✅ Write clean, testable code
✅ Ask intelligent questions

---

**Start with [Python Interview Questions](python_questions.md)**
