# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import Field, FormActions

from users.models import UserProfile, UserGroup


class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['is_manager', 'is_admin', 'manager', 'group']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'userprofile-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('manager', id="manager"),
            Field('group', id="group"),
            Field('is_manager'),
            Field('is_admin'),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML("<a class='btn btn-default' href='{% url \"users:user_list\" %}'>Cancel</a>")
            )
        )


class UserGroupForm(ModelForm):

    class Meta:
        model = UserGroup
        fields = ['name', 'parent', 'manager']

    def __init__(self, *args, **kwargs):
        super(UserGroupForm, self).__init__(*args, **kwargs)
        # print self.fields['parent'].queryset.exclude(id__exact=self.instance.id)
        self.helper = FormHelper()
        self.helper.form_id = 'usergroup-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name'),
            Field('parent', id="parent"),
            Field('manager', id="manager"),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML("<a class='btn btn-default' href='{% url \"users:user_group_list\" %}'>Cancel</a>")
            )
        )
