from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.translation import ugettext as _
from django.utils.html import format_html
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from datatableview.views import DatatableView
from core.mixins import AdminMixin
from saas.mixins import CustomerSaveMixin, CustomerListViewMixin, CustomerCheckMixin

from questions.models import Quiz, Sitting, Category
from questions.forms import QuizForm, QuestionFormSet, QuestionFormSetHelper, SittingForm
from questions.forms import CategoryForm
from questions.forms import make_quiz_form, quiz_form_helper, save_quiz_form


class QuizView(FormMixin, DetailView):
    model = Quiz

    def get_success_url(self):
        return reverse('dashboard')

    def get_form_class(self):
        return make_quiz_form(self.object)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        save_quiz_form(self.object, form)
        return super(QuizView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        form = self.get_form()
        context['form'] = form
        context['form_helper'] = quiz_form_helper(self.object)
        return context

    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        return super(QuizView, self).dispatch(*args, **kwargs)


class SittingDatatableView(AdminMixin, CustomerListViewMixin, DatatableView):
    """
    Allows you to manage sittings
    """

    model = Sitting
    template_name = "questions/sitting_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            'title',
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['title'],
        'unsortable_columns': ['id'],
    }

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{0}">Edit</a> | <a href="{1}">Completion Report</a> | <a href="{2}">Company Report</a>', reverse(
                'questions:sitting_edit', args=[instance.pk]), reverse(
                'reports:sitting_completion_report', args=[instance.pk]), reverse(
                'reports:sitting', args=[instance.pk])
        )


class SittingUpdate(AdminMixin, CustomerCheckMixin, CustomerSaveMixin, UpdateView):
    model = Sitting
    form_class = SittingForm
    template_name = "questions/sitting_edit.html"
    success_url = reverse_lazy('questions:sitting_list')


class SittingAdd(AdminMixin, CustomerSaveMixin, CreateView):
    model = Sitting
    form_class = SittingForm
    template_name = "questions/sitting_add.html"
    success_url = reverse_lazy('questions:sitting_list')


class QuizDatatableView(AdminMixin, CustomerListViewMixin, DatatableView):
    """
    Allows you to manage question sets
    """

    model = Quiz
    template_name = "questions/quiz_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            'title',
            'use_categories',
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['title'],
        'unsortable_columns': ['id'],
    }

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Questions</a>', reverse(
                'questions:quiz_edit', args=[instance.pk]), reverse('questions:quiz_questions', args=[instance.pk])
        )


class QuizUpdate(AdminMixin, CustomerCheckMixin, CustomerSaveMixin, UpdateView):
    model = Quiz
    form_class = QuizForm
    template_name = "questions/quiz_edit.html"
    success_url = reverse_lazy('questions:quiz_list')


class QuizAdd(AdminMixin, CustomerSaveMixin, CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = "questions/quiz_add.html"
    success_url = reverse_lazy('questions:quiz_list')


def quiz_questions(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk, customer=request.user.userprofile.customer)
    if request.method == "POST":
        formset = QuestionFormSet(request.POST, instance=quiz)
        if formset.is_valid():
            formset.save()
            messages.add_message(
                request, messages.SUCCESS, _('Successfully saved {0}'.format(quiz._meta.verbose_name.title())))
            return redirect(reverse('questions:quiz_list'))
    else:
        formset = QuestionFormSet(instance=quiz)
    return render(request, "questions/quiz_questions.html", {
        "QuestionFormSet": formset,
        'QuestionFormSetHelper': QuestionFormSetHelper,
        "object": quiz
    })


class QuestionCategoryDatatableView(AdminMixin, CustomerListViewMixin, DatatableView):
    """
    Allows you to manage sittings
    """

    model = Category
    template_name = "questions/category_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            'title',
            'order',
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['title'],
        'unsortable_columns': ['id'],
    }

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{0}">Edit</a>', reverse(
                'questions:category_edit', args=[instance.pk])
        )


class QuestionCategoryUpdate(AdminMixin, CustomerCheckMixin, CustomerSaveMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "questions/category_edit.html"
    success_url = reverse_lazy('questions:category_list')


class QuestionCategoryAdd(AdminMixin, CustomerSaveMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "questions/category_add.html"
    success_url = reverse_lazy('questions:category_list')
