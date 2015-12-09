from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from saas.models import Customer

User = settings.AUTH_USER_MODEL


@python_2_unicode_compatible
class UserGroup(models.Model):
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    customer = models.ForeignKey(Customer, verbose_name=_(
        "Customer"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    name = models.CharField(_("Group Name"), max_length=300, blank=False)
    parent = models.ForeignKey(
        "self", verbose_name=_('Parent Group'), blank=True, null=True, default=None, on_delete=models.PROTECT)
    manager = models.ForeignKey(
        "UserProfile", verbose_name=_('Group Manager'), blank=True, null=True, default=None, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("User Group")
        verbose_name_plural = _("User Groups")
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class UserProfile(models.Model):

    """
    Model used to store more information on users
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    user = models.OneToOneField(User, verbose_name=_("User"))
    customer = models.ForeignKey(Customer, verbose_name=_(
        "Customer"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    is_manager = models.BooleanField(
        _("Is Manager"), help_text=_("Is this user a manager"), default=False)
    manager = models.ForeignKey("self", verbose_name=_('Manager'), help_text=_(
        "Select this user's manager"), blank=True, null=True, default=None, on_delete=models.PROTECT)
    is_admin = models.BooleanField(
        _("Is Administrator"), help_text=_("Should this user have administrative privileges"), default=False)
    group = models.ManyToManyField(UserGroup, blank=True, default=None)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")
        ordering = ['user__first_name', 'created_on']

    def get_display_name(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username

    def __str__(self):
        return self.get_display_name()


# S I G N A L S
from users import signals
