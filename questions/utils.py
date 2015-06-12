from collections import OrderedDict

from django.forms.models import fields_for_model
from django.forms import BaseForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, ButtonHolder, Div, Submit, Button


def make_quiz_form(quiz):
    form_fields = OrderedDict()
    for question in quiz.get_questions():
        answer_class = question.get_answer_class()
        model_fields = fields_for_model(answer_class)
        answer_field = model_fields['answer']
        answer_field.required = True
        answer_field.label = question.title
        form_fields['answer_{}'.format(question.id)] = answer_field
    return type('QuizForm', (BaseForm,), {'base_fields': form_fields})


def quiz_form_helper(quiz):
    form = make_quiz_form(quiz)
    helper = FormHelper()
    helper.form_id = 'quiz-{}-form'.format(quiz.id)
    helper.form_method = 'post'
    helper.layout = Layout(*form.base_fields.keys())
    helper.add_input(Button('submit', "Submit", css_class='btn btn-primary'))
    return helper
