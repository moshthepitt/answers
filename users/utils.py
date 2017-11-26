from core.emails import generic_email

from .models import UserProfile, UserGroup


def send_email_to_users(customer, from_name, from_email, subject, message):
    userprofiles = UserProfile.objects.filter(customer=customer)
    if userprofiles:
        sender = '{0} <{1}>'.format(from_name, from_email)
        for userprofile in userprofiles:
            generic_email(userprofile.user, sender, subject, message)


def get_user_display(user):
    return user.userprofile.get_display_name()


def get_user_group(name, customer):
    group, created = UserGroup.objects.get_or_create(name=name,
                                                     customer=customer)
    return group
