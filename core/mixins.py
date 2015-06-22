from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext as _


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
