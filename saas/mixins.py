from django.contrib import messages
from django.utils.translation import ugettext as _


class CustomerSaveMixin(object):

    """
    Used when saving an object that has a customer field e.g. SomeObject.customer
    It adds the current customer to the object being saved
    Shoudl be used in a View that has FormMixin
    """

    def form_valid(self, form):
        self.saved_object = form.save()
        if self.request.user.userprofile and self.request.user.userprofile.customer:
            if not self.saved_object.customer or (self.saved_object.customer and self.saved_object.customer != self.request.user.userprofile.customer):
                self.saved_object.customer = self.request.user.userprofile.customer
                self.saved_object.save()
        messages.add_message(
            self.request, messages.SUCCESS, _('Successfully saved {0}'.format(self.model._meta.verbose_name.title())))
        return super(CustomerSaveMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING, _('Please fix the errors below'))
        return super(CustomerSaveMixin, self).form_invalid(form)
