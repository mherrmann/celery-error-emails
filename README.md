# celery_error_emails

Automatically send error emails about failing Celery tasks in your Django
project.

# Installation

```
pip install celery_error_emails
```

# Usage

Celery's [documentation](https://docs.celeryq.dev/en/v5.2.6/django/first-steps-with-django.html)
recommends creating a file `celery.py` in your Django project. This has lines
similar to the following:

```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')
```

To enable error emails, you can simply add the following import:

```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

import celery_error_emails # <- this is new

app = Celery('proj')
```