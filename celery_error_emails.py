from celery.signals import task_failure
from django.core.mail import mail_admins

@task_failure.connect()
def celery_task_failure_email(**kwargs):
    subject = "Celery error in {sender.name}".format(**kwargs)
    message = """{einfo}
Task was called with args: {args} kwargs: {kwargs}.""".format(**kwargs)
    mail_admins(subject, message)