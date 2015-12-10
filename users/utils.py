from core.emails import generic_email

from .models import UserProfile


def send_email_to_users(customer, from_name, from_email, subject, message):
    userprofiles = UserProfile.objects.filter(customer=customer)
    if userprofiles:
        sender = '{0} <{1}>'.format(from_name, from_email)
        for userprofile in userprofiles:
            generic_email(userprofile.user, sender, subject, message)
