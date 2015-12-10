from celery.decorators import task

from saas.models import Customer

from .utils import send_email_to_users


@task(name="send_feedback_email_task")
def task_send_email_to_users(customer_id, from_name, from_email, subject, message):
    customer = Customer.objects.get(pk=customer_id)
    return send_email_to_users(customer, from_name, from_email, subject, message)
