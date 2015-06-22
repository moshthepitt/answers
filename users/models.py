from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):

    """
    Model used to store more information on users
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    user = models.OneToOneField(User, verbose_name=_("User"))
    is_manager = models.BooleanField(
        _("Is Manager"), help_text=_("Is this user a manager"), default=False)
    manager = models.ForeignKey("self", verbose_name=_('Manager'), help_text=_(
        "Select this user's manager"), blank=True, null=True, default=None)
    is_admin = models.BooleanField(
        _("Is Administrator"), help_text=_("Should this user have administrative privileges"), default=False)

    class Meta:
        verbose_name = _("Staff Profile")
        verbose_name_plural = _("Staff Profiles")
        ordering = ['user__first_name', 'created_on']

    def get_display_name(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username

    def __str__(self):
        return self.get_display_name()


# S I G N A L S
from users import signals
