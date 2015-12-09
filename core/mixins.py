from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext as _

from users.models import UserProfile, UserGroup
from questions.models import Quiz, Sitting


class AdminMixin(object):

    """
    Restricts views to only admin users
    """

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            messages.add_message(
                self.request, messages.WARNING, _('Please log in'))
            return redirect('dashboard')
        if not self.request.user.userprofile.is_admin:
            messages.add_message(
                self.request, messages.WARNING, _('Sorry, you do not have access to that section'))
            return redirect('dashboard')
        return super(AdminMixin, self).dispatch(*args, **kwargs)


class CustomerQuerysetMixin(object):

    """
    Restricts form field querysets to only those of the customer
    """

    def get_context_data(self, **kwargs):
        context = super(CustomerQuerysetMixin, self).get_context_data(**kwargs)
        form = self.get_form()

        try:
            self.get_object()
            detail_view = True
        except AttributeError:
            detail_view = False

        try:
            form.fields['sitting'].queryset = Sitting.objects.filter(
                customer=self.request.user.userprofile.customer)
        except KeyError:
            pass

        try:
            form.fields['quiz'].queryset = Quiz.objects.filter(
                customer=self.request.user.userprofile.customer)
        except KeyError:
            pass

        try:
            form.fields['reviewers'].queryset = UserProfile.objects.filter(
                customer=self.request.user.userprofile.customer)
        except KeyError:
            pass

        try:
            form.fields['userprofile'].queryset = UserProfile.objects.filter(
                customer=self.request.user.userprofile.customer)
        except KeyError:
            pass

        try:
            form.fields['group'].queryset = UserGroup.objects.filter(
                customer=self.request.user.userprofile.customer)
        except KeyError:
            pass

        try:
            form.fields['parent'].queryset = UserGroup.objects.filter(
                customer=self.request.user.userprofile.customer
            )
            if type(self.get_object()) == UserGroup and detail_view:
                form.fields['parent'].queryset = UserGroup.objects.filter(
                    customer=self.request.user.userprofile.customer
                ).exclude(id__exact=self.get_object().id)
        except KeyError:
            pass

        try:
            form.fields['manager'].queryset = UserProfile.objects.filter(
                customer=self.request.user.userprofile.customer)
            if type(self.get_object()) == UserProfile and detail_view:
                form.fields['manager'].queryset = UserProfile.objects.filter(
                    customer=self.request.user.userprofile.customer
                ).exclude(id__exact=self.get_object().id)
        except KeyError:
            pass

        context['form'] = form
        return context
