# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, ButtonHolder

from reviews.models import Review


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'quiz', 'reviewers']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['reviewers'].required = False
        self.helper.form_id = 'review-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('quiz'),
            Field('reviewers'),
            ButtonHolder(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML("<a class='btn btn-default' href='{% url \"reviews:review_list\" %}'>Cancel</a>")
            )
        )


class PeerReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'userprofile', 'quiz', 'reviewers']

    def __init__(self, *args, **kwargs):
        super(PeerReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['reviewers'].required = False
        self.fields['userprofile'].required = True
        self.helper.form_id = 'review-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('userprofile'),
            Field('quiz'),
            Field('reviewers'),
            ButtonHolder(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML("<a class='btn btn-default' href='{% url \"reviews:peer_review_list\" %}'>Cancel</a>")
            )
        )
