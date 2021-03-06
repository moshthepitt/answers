# -*- coding: utf-8 -*-
from collections import OrderedDict

from django.forms.models import fields_for_model
from django.forms import BaseForm, ModelForm, CharField, ValidationError
from django.forms import Select, BaseInlineFormSet, RadioSelect
from django.utils.translation import ugettext as _
from django.forms.models import inlineformset_factory
from django.utils.html import format_html
from django.utils.encoding import smart_str
from django.utils.safestring import mark_safe
from django.conf import settings

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Fieldset
from crispy_forms.bootstrap import Field, FormActions
from sorl.thumbnail import get_thumbnail

from questions.models import MultipleChoiceOption, MultipleChoiceQuestion, Quiz, RatingQuestion
from questions.models import Sitting, Category
from answers.models import MultipleChoiceOtherAnswer, MultipleChoiceAnswer, RatingAnswer

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
                HTML(
                    "<a class='btn btn-default' href='{% url \"questions:sitting_list\" %}'>Cancel</a>")
            )
        )


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'order']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'question-category-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('order'),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML(
                    "<a class='btn btn-default' href='{% url \"questions:category_list\" %}'>Cancel</a>")
            )
        )


class QuizForm(ModelForm):

    class Meta:
        model = Quiz
        fields = ['title', 'description', 'use_categories', 'question_ordering']

    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'quiz-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('description'),
            Field('use_categories'),
            Field('question_ordering'),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML(
                    "<a class='btn btn-default' href='{% url \"questions:quiz_list\" %}'>Cancel</a>")
            )
        )


class QuestionForm(ModelForm):

    class Meta:
        model = RatingQuestion
        fields = ['title', 'category', 'order']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True


class QuestionFormSetHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(QuestionFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.form_method = 'post'
        self.template = 'bootstrap3/table_inline_formset.html'


class BaseQuestionFormSet(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(BaseQuestionFormSet, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            quiz_instance = kwargs['instance']
            for form in self.forms:
                if 'category' in form.fields:
                    form.fields['category'].queryset = Category.objects.filter(
                        customer=quiz_instance.customer)


QuestionFormSet = inlineformset_factory(
    Quiz, RatingQuestion, form=QuestionForm, formset=BaseQuestionFormSet, can_delete=True, extra=5)


def make_quiz_form(quiz, select_to_radio=False):
    """
    Generates a form on the fly based on the Quiz questions
    """
    form_fields = OrderedDict()
    for question in quiz.get_questions():
        AnswerModel = question.get_answer_class()
        model_fields = fields_for_model(AnswerModel, exclude=['userprofile', 'review'])
        if AnswerModel == MultipleChoiceAnswer or AnswerModel == RatingAnswer:
            if select_to_radio or (quiz.question_widget == quiz.RADIO_WIDGET) or (question.widget == question.RADIO_WIDGET):
                model_fields = fields_for_model(
                    AnswerModel, exclude=['userprofile', 'review'], formfield_callback=multiplechoice_to_radio)
                # Begin Diry hack
                # for when radio select has for some reason not been set by fields_for_model
                # this happens for RatingAnswer objects
                # first we check if choices exist to avoid none choice fields
                if hasattr(model_fields['answer'], '_choices'):
                    # then we check if the widget is still Select
                    if isinstance(model_fields['answer'].widget, Select):
                        # we manually make it into a Radio Select field
                        model_fields['answer'].widget = RadioSelect()
                        # we remove the empty answer choice usually preset in Select Fields
                        if not model_fields['answer']._choices[0][0]:
                            model_fields['answer']._choices.pop(0)
                # End Diry hack

        answer_field = model_fields['answer']
        answer_field.required = question.required
        # answer_field.question = question ?? should this be included
        answer_field.has_image_answers = question.has_image_answers
        answer_field.widget_to_use = question.widget
        other_field = None
        if question.image:
            thumb_size = getattr(settings, 'QUESTION_LABEL_THUMBS_SIZE', "500x400")
            thumb = get_thumbnail(question.image.file, thumb_size)
            answer_field.label = format_html(
                "<img src='{thumb}' class='img-responsive question-label' alt='{qtitle}' title='{qtitle}' /><span class='question-text-latel'>{qtitle}</span>", thumb=thumb.url, qtitle=smart_str(question.title))
            if quiz.show_question_numbers:
                answer_field.label = format_html(
                    "<img src='{thumb}' class='img-responsive question-label' alt='{qtitle}' title='{qtitle}' /><span class='question-text-latel'>{qtitle}</span>", thumb=thumb.url, qtitle=smart_str("{}. {}".format(question.order, question.title)))
        else:
            this_label = question.title
            if quiz.show_question_numbers:
                this_label = "{}. {}".format(question.order, this_label)
            if question.description:
                answer_field.label = format_html("<span class='question-text-latel'>{}</span><div class='question-description'>{}</div>", smart_str(
                    this_label), mark_safe(smart_str(question.description).replace('\n', '<br />')))
            else:
                answer_field.label = smart_str(this_label)
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


def quiz_form_helper(quiz, form_to_use=None, select_to_radio=False):
    if form_to_use:
        form = form_to_use
    else:
        form = make_quiz_form(quiz, select_to_radio)
    helper = FormHelper()
    helper.form_id = 'quiz-{}-form'.format(quiz.id)
    helper.form_class = 'form quiz_form quiz-{}'.format(quiz.id)
    helper.form_method = 'post'
    helper.html5_required = True
    helper.render_required_fields = True
    helper.layout = Layout(*form.base_fields.keys())
    if quiz.use_categories:
        #  use fieldsets to separate question categories
        categories = Category.objects.filter(question__quiz=quiz).distinct()
        quiz_cats = {'answer_{}'.format(x.id): x.category for x in quiz.get_questions()}
        layout_items = []
        for cat in categories:
            fieldset_items = [cat.title]
            for answer_field in form.base_fields.keys():
                if quiz_cats[answer_field] == cat:
                    fieldset_items.append(answer_field)
            layout_items.append(Fieldset(*fieldset_items))
        helper.layout = Layout(*layout_items)
    if select_to_radio or quiz.question_widget == quiz.RADIO_WIDGET:
        helper.all().wrap(Field, css_class="question-field",
                          template="answers/bootstrap3/multichoice_radio_field.html")
    else:
        helper.all().wrap(Field, css_class="question-field")
    helper.add_input(Submit('submit', _('Submit'), css_class='btn-success btn-block btn-lg'))
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
