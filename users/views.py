from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.html import format_html

from datatableview.views import DatatableView
from core.mixins import AdminMixin

from users.models import UserProfile, UserGroup
from users.forms import UserProfileForm, UserGroupForm


class UserProfileUpdate(AdminMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "users/user_edit.html"
    success_url = reverse_lazy('users:user_list')


class UserProfileDatatableView(AdminMixin, DatatableView):
    model = UserProfile
    template_name = "users/user_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            (_("First Name"), 'user__first_name'),
            (_("Last Name"), 'user__last_name'),
            (_("Email"), 'user__email'),
            'manager',
            (_('Group'), 'group', 'get_groups'),
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['userprofile__user__last_name', 'userprofile__user__first_name', 'userprofile__user__email'],
        'unsortable_columns': ['id', 'group'],
    }

    def get_queryset(self):
        queryset = super(UserProfileDatatableView, self).get_queryset()
        return queryset

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{}">Edit</a>', reverse(
                'users:user_edit', args=[instance.pk])
        )

    def get_groups(self, instance, *args, **kwargs):
        return ", ".join(map(str, [x.name for x in instance.group.all()]))


class UserGroupAdd(AdminMixin, CreateView):
    model = UserGroup
    form_class = UserGroupForm
    template_name = "users/user_group_add.html"
    success_url = reverse_lazy('users:user_group_list')


class UserGroupUpdate(AdminMixin, UpdateView):
    model = UserGroup
    form_class = UserGroupForm
    template_name = "users/user_group_edit.html"
    success_url = reverse_lazy('users:user_group_list')


class UserGroupDatatableView(AdminMixin, DatatableView):
    model = UserGroup
    template_name = "users/user_group_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            'name',
            'parent',
            'manager',
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['name'],
        'unsortable_columns': ['id'],
    }

    def get_queryset(self):
        queryset = super(UserGroupDatatableView, self).get_queryset()
        return queryset

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{}">Edit</a>', reverse(
                'users:user_group_edit', args=[instance.pk])
        )
