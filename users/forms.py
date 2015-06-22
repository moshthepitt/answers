# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, ButtonHolder

from users.models import UserProfile


class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['is_manager', 'manager']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'reviewn-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('manager'),
            Field('is_manager'),
            ButtonHolder(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML("<a class='btn btn-default' href='{% url \"users:user_list\" %}'>Cancel</a>")
            )
        )
