# celery-error-emails

Automatically send error emails about failing Celery tasks in your Django
project.

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
