from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import UserProfile

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created or not instance.userprofile:
        profile, profile_created = UserProfile.objects.get_or_create(user=instance)
