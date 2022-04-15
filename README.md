# celery-error-emails

Automatically send error emails about failing Celery tasks in your Django
project.

**Sample email:**

*Subject: Celery error in your.module.task*

```
Traceback (most recent call last):
  File ".../site-packages/celery/app/trace.py", line 412, in trace_task
    R = retval = fun(*args, **kwargs)
  File ".../site-packages/celery/app/trace.py", line 704, in __protected_call__
    return self.run(*args, **kwargs)
  File "/home/project/main/tasks/_task.py", line 31, in new_func
    result = func(*args, **kwargs)
  File "/home/project/main/tasks/__init__.py", line 71, in task
    typo
NameError: name 'typo' is not defined

Task was called with args: [] kwargs: {}.
```

# Installation

```
pip install celery-error-emails
```

# Usage

Celery's [documentation](https://docs.celeryq.dev/en/v5.2.6/django/first-steps-with-django.html)
recommends creating a file `celery.py` in your Django project. This has lines
similar to the following:

```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')
```

To enable error emails, you can simply add the following import between the
above lines:

```
import celery_error_emails
```

(Other places may work as well for adding the import.)
