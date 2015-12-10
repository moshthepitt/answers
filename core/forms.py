# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import Field, FormActions

from users.utils import send_email_to_users


class GenericMessage(forms.Form):
    from_name = forms.CharField(
        label=_("From Name")
    )
    from_email = forms.EmailField(
        label=_("From Email (Sender)")
    )
    subject = forms.CharField(
        label=_("Email Subject")
    )
    message = forms.CharField(
        label=_("Email Message"),
        widget=forms.Textarea
    )

    def send_email(self, customer):
        from_name = self.cleaned_data['from_name']
        from_email = self.cleaned_data['from_email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        return send_email_to_users(customer, from_name, from_email, subject, message)

    def __init__(self, *args, **kwargs):
        super(GenericMessage, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'generic-message-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('from_name'),
            Field('from_email'),
            Field('subject'),
            Field('message'),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                css_class="form-group"
            )
        )

