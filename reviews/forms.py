# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import Field, FormActions

from reviews.models import Review


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'sitting', 'quiz', 'reviewers']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['reviewers'].required = False
        self.fields['sitting'].required = True
        self.helper.form_id = 'review-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('sitting'),
            Field('quiz', id="select-quiz"),
            Field('reviewers', id="select-reviewers"),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML("<a class='btn btn-default' href='{% url \"reviews:review_list\" %}'>Cancel</a>")
            )
        )


class PeerReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'sitting', 'userprofile', 'quiz', 'reviewers']

    def __init__(self, *args, **kwargs):
        super(PeerReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['reviewers'].required = False
        self.fields['userprofile'].required = True
        self.fields['sitting'].required = True
        self.helper.form_id = 'review-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('sitting'),
            Field('userprofile', id="select-user"),
            Field('quiz', id="select-quiz"),
            Field('reviewers', id="select-reviewers"),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML("<a class='btn btn-default' href='{% url \"reviews:peer_review_list\" %}'>Cancel</a>")
            )
        )
