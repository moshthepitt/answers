from collections import OrderedDict

from django.forms.models import fields_for_model
from django.forms import BaseForm
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from questions.models import MultipleChoiceOption, MultipleChoiceQuestion


def make_quiz_form(quiz):
    form_fields = OrderedDict()
    for question in quiz.get_questions():
        AnswerModel = question.get_answer_class()
        model_fields = fields_for_model(AnswerModel)
        answer_field = model_fields['answer']
        answer_field.label = question.title
        if question._meta.model == MultipleChoiceQuestion:
            answer_field.queryset = MultipleChoiceOption.objects.filter(question=question)
        form_fields['answer_{}'.format(question.id)] = answer_field
    return type('QuizForm', (BaseForm,), {'base_fields': form_fields})


def quiz_form_helper(quiz):
    form = make_quiz_form(quiz)
    helper = FormHelper()
    helper.form_id = 'quiz-{}-form'.format(quiz.id)
    helper.form_method = 'post'
    helper.layout = Layout(*form.base_fields.keys())
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
                user=user,
                review=review
            )
            answer.save()
