from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):

    """
    Model used to store more information on users
    """
    user = models.OneToOneField(User)

    def __unicode__(self):
        return "%s's profile" % (self.user)


# S I G N A L S
from users import signals
