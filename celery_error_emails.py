# from celery.signals import task_failure
# from django.core.mail import mail_admins

# @task_failure.connect()
def celery_task_failure_email(**kwargs):
    subject = "Celery error in {sender.name}: {exception}".format(**kwargs)
    message = """Task {sender.name} raised exception:

{exception!r}

Task was called with args: {args} kwargs: {kwargs}.

{einfo}
    """.format(**kwargs)
    mail_admins(subject, message)