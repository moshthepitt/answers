from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext as _


class ReportMixin(object):
    """
    Can the user view this report?
    """

    def dispatch(self, *args, **kwargs):
        review = self.get_object()
        if not self.request.user.userprofile.is_admin:
            if (review.userprofile != self.request.user.userprofile) and (review.userprofile.manager != self.request.user.userprofile):
                messages.add_message(
                    self.request, messages.WARNING, _('Sorry, you do not have access to that report'))
                return redirect('reports:report_list')
        return super(ReportMixin, self).dispatch(*args, **kwargs)
