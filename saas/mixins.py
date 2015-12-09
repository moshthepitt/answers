from django.contrib import messages
from django.http import Http404
# from django.shortcuts import redirect
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


class CustomerListViewMixin(object):

    """
    Makes sure the queryset filters by Customer
    """

    def get_queryset(self):
        if self.request.user.userprofile.customer:
            queryset = super(CustomerListViewMixin, self).get_queryset().filter(customer=self.request.user.userprofile.customer)
        else:
            queryset = super(CustomerListViewMixin, self).get_queryset().none()
        return queryset


class CustomerCheckMixin(object):

    """
    Used in detail and update views to ensure that the user has the right to view the object
    """

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            # if current user is not tied to a customer then redirect them away
            if not self.request.user.userprofile.customer:
                raise Http404
            # if current user is not tied to a subscription then redirect them away
            if self.request.user.userprofile.customer != self.get_object().customer:
                raise Http404
        return super(CustomerCheckMixin, self).dispatch(*args, **kwargs)
