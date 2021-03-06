from setuptools import setup

setup(
    name = "celery-error-emails",
    version = "0.3",
    author = "Michael Herrmann",
    author_email = "michaelREMOVETHISIFYOUAREHUMAN@herrmann.io",
    description = "Automatically send error emails about failing Celery tasks in your Django project.",
    license = "MIT",
    keywords = "celery error emails django",
    url = "https://github.com/mherrmann/celery-error-emails",
    long_description = "For more details, please see https://github.com/mherrmann/celery-error-emails",
    py_modules=['celery_error_emails'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Celery",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ]
)
