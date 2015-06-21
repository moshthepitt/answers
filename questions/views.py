from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.translation import ugettext as _
from django.utils.html import format_html

from datatableview.views import DatatableView

from questions.models import Quiz
from questions.forms import QuizForm#, QuestionFormSet
from questions.forms import make_quiz_form, quiz_form_helper, save_quiz_form


class QuizView(FormMixin, DetailView):
    model = Quiz

    def get_success_url(self):
        return reverse('home')

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


class QuizDatatableView(DatatableView):
    model = Quiz
    template_name = "questions/quiz_list.html"
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
            '<a href="{}">Edit</a> <a href="{}">Questions</a>', reverse(
                'questions:quiz_edit', args=[instance.pk]), reverse('questions:quiz_questions', args=[instance.pk])
        )


class QuizUpdate(UpdateView):
    model = Quiz
    form_class = QuizForm
    template_name = "questions/quiz_edit.html"
    success_url = reverse_lazy('questions:quiz_list')


class QuizAdd(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = "questions/quiz_add.html"
    success_url = reverse_lazy('questions:quiz_list')


# class QuizQuestions(UpdateView):
#     form_class = QuizForm
#     template_name = 'questions/quiz_questions.html'

#     def get_context_data(self, **kwargs):
#         data = super(QuizQuestions, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['QuestionFormSet'] = QuestionFormSet(self.request.POST, instance=self.get_object())
#         else:
#             data['QuestionFormSet'] = QuestionFormSet(instance=self.get_object())
#         return data

#     def form_valid(self, form):
#         # context = self.get_context_data()
#         # sponsorships = context['sponsorships']
#         # with transaction.commit_on_success():
#         #     form.instance.created_by = self.request.user
#         #     form.instance.updated_by = self.request.user
#         #     self.object = form.save()
#         # if sponsorships.is_valid():
#         #     sponsorships.instance = self.object
#         #     sponsorships.save()
#         return super(QuizQuestions, self).form_valid(form)

#     def get_success_url(self):
#         return reverse('sponsors')
