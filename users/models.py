from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

class UserProfile(models.Model):
    """
    Model used to store more information on users
    """
    user = models.OneToOneField(User)

    def __unicode__(self):
    	return "%s's profile" %(self.user)

#### S I G N A L S ####
from users import signals

