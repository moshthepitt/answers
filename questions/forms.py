# -*- coding: utf-8 -*-
from collections import OrderedDict

from django.forms.models import fields_for_model
from django.forms import BaseForm, ModelForm, CharField, ValidationError
from django.utils.translation import ugettext as _
from django.forms.models import inlineformset_factory
from django.utils.html import format_html
from django.utils.encoding import smart_str
from django.conf import settings

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import Field, FormActions
from sorl.thumbnail import get_thumbnail

from questions.models import MultipleChoiceOption, MultipleChoiceQuestion, Quiz, RatingQuestion
from questions.models import Sitting
from answers.models import MultipleChoiceOtherAnswer

from .utils import multiplechoice_to_radio


class SittingForm(ModelForm):

    class Meta:
        model = Sitting
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(SittingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'sitting-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML("<a class='btn btn-default' href='{% url \"questions:sitting_list\" %}'>Cancel</a>")
            )
        )


class QuizForm(ModelForm):

    class Meta:
        model = Quiz
        fields = ['title', 'description', 'question_ordering']

    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'quiz-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('description'),
            Field('question_ordering'),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML("<a class='btn btn-default' href='{% url \"questions:quiz_list\" %}'>Cancel</a>")
            )
        )


class QuestionForm(ModelForm):

    class Meta:
        model = RatingQuestion
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True


class QuestionFormSetHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(QuestionFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.form_method = 'post'
        self.template = 'bootstrap3/table_inline_formset.html'


QuestionFormSet = inlineformset_factory(
    Quiz, RatingQuestion, form=QuestionForm, can_delete=True, extra=5)


def make_quiz_form(quiz, select_to_radio=False):
    """
    Generates a form on the fly based on the Quiz questions
    """
    form_fields = OrderedDict()
    for question in quiz.get_questions():
        AnswerModel = question.get_answer_class()
        if select_to_radio:
            model_fields = fields_for_model(AnswerModel, formfield_callback=multiplechoice_to_radio)
        else:
            model_fields = fields_for_model(AnswerModel)
        answer_field = model_fields['answer']
        answer_field.label = question.title
        answer_field.required = question.required
        # answer_field.question = question ?? should this be included
        answer_field.has_image_answers = question.has_image_answers
        other_field = None
        if question.image:
            thumb_size = getattr(settings, 'QUESTION_LABEL_THUMBS_SIZE', "500x400")
            thumb = get_thumbnail(question.image.file, thumb_size)
            answer_field.label = format_html(
                "<img src='{}' class='img-responsive question-label' alt='{}' title='{}' /><span class='question-text-latel'>{}</span>", thumb.url, smart_str(question.title), smart_str(question.title), smart_str(question.title))
        else:
            answer_field.label = smart_str(question.title)
        if question._meta.model == MultipleChoiceQuestion:
            answer_field.queryset = MultipleChoiceOption.objects.filter(question=question)
            if answer_field.queryset.filter(other=True).exists():
                other_field = CharField()
                other_field.widget.attrs['class'] = "other-field id_answer_{}".format(question.id)
                other_field.label = _("If you selected Other, please specify what you meant")
                other_field.required = False
        form_fields['answer_{}'.format(question.id)] = answer_field
        if other_field:
            form_fields['other_{}'.format(question.id)] = other_field
    return type('QuizForm', (BaseForm,), {'base_fields': form_fields})


def make_custom_cleaned_quiz_form(quiz, select_to_radio=False):
    """
    Generates a form on the fly based on the Quiz questions
    Adds certain custom clean methods, i.e.:
        1. Validate "Other" multiple choice option
    """
    QuizForm = make_quiz_form(quiz, select_to_radio)

    class NewForm(QuizForm):

        def clean(self):
            cleaned_data = super(NewForm, self).clean()
            for question in quiz.get_questions():
                answer_field = 'answer_{}'.format(question.id)
                if answer_field in cleaned_data and question._meta.model == MultipleChoiceQuestion:
                    questions_answer = cleaned_data[answer_field]
                    if questions_answer:
                        other_field = 'other_{}'.format(question.id)
                        if questions_answer.other:
                            if (other_field not in cleaned_data) or (not cleaned_data[other_field]):
                                raise ValidationError({other_field: _("Please input a value")})
            return cleaned_data

    return NewForm


def quiz_form_helper(quiz, select_to_radio=False):
    form = make_quiz_form(quiz)
    helper = FormHelper()
    helper.form_id = 'quiz-{}-form'.format(quiz.id)
    helper.form_class = 'form quiz_form quiz-{}'.format(quiz.id)
    helper.form_method = 'post'
    helper.html5_required = True
    helper.layout = Layout(*form.base_fields.keys())
    if select_to_radio:
        helper.all().wrap(Field, css_class="question-field", template="answers/bootstrap3/multichoice_radio_field.html")
    else:
        helper.all().wrap(Field, css_class="question-field")
    helper.add_input(Submit('submit', _('Submit'), css_class='btn-success'))
    return helper


def save_quiz_form(quiz, form, user=None, review=None):
    for question in quiz.get_questions():
        answer_field = 'answer_{}'.format(question.id)
        if answer_field in form.cleaned_data:
            questions_answer = form.cleaned_data[answer_field]
            AnswerModel = question.get_answer_class()
            answer = AnswerModel(
                question=question,
                answer=questions_answer,
                review=review
            )
            if not user.is_anonymous():
                answer.userprofile = user.userprofile
            answer.save()
        if question._meta.model == MultipleChoiceQuestion:
            other_field = 'other_{}'.format(question.id)
            if questions_answer and questions_answer.other and other_field and other_field in form.cleaned_data:
                questions_other = form.cleaned_data[other_field]
                other_answer = MultipleChoiceOtherAnswer(
                    answer=answer,
                    body=questions_other
                )
                other_answer.save()
