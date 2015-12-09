from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from phonenumber_field.modelfields import PhoneNumberField


@python_2_unicode_compatible
class Customer(models.Model):
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    name = models.CharField(_('Customer name'), max_length=255, blank=False)
    email = models.EmailField(_('Email address'), blank=True)
    phone = PhoneNumberField(_('Phone Number'), max_length=255, blank=True)
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text=_('Designates whether this customer should be treated as '
                                                'active.'))

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

