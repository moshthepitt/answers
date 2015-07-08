from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext as _

from users.models import UserGroup
from core.utils import lists_overlap


class ReportMixin(object):

    """
    Can the user view this report?
    """

    def dispatch(self, *args, **kwargs):
        review = self.get_object()
        if not self.request.user.userprofile.is_admin:
            # the user can see his own reports
            if review.userprofile == self.request.user.userprofile:
                pass
            # the user can see reports of those he managers directly
            elif review.userprofile.manager == self.request.user.userprofile:
                pass
            # the user can see reports of members of groups in which he is a manager
            elif lists_overlap(review.userprofile.group.all(), UserGroup.objects.filter(manager=self.request.user.userprofile)):
                pass
            # if all the above fails then redirect away
            else:
                messages.add_message(
                    self.request, messages.WARNING, _('Sorry, you do not have access to that report'))
                return redirect('reports:report_list')
        return super(ReportMixin, self).dispatch(*args, **kwargs)
