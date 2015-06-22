from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.html import format_html

from datatableview.views import DatatableView

from users.models import UserProfile
from users.forms import UserProfileForm


class UserProfileUpdate(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "users/user_edit.html"
    success_url = reverse_lazy('users:user_list')


class UserProfileDatatableView(DatatableView):
    model = UserProfile
    template_name = "users/user_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            (_("Username"), 'user__username'),
            (_("First Name"), 'user__first_name'),
            (_("Last Name"), 'user__last_name'),
            'manager',
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['userprofile__user__last_name', 'userprofile__user__first_name', 'userprofile__user__username'],
        'unsortable_columns': ['id'],
    }

    def get_queryset(self):
        queryset = super(UserProfileDatatableView, self).get_queryset()
        return queryset

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{}">Edit</a>', reverse(
                'users:user_edit', args=[instance.pk])
        )
