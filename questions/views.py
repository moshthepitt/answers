from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse

from questions.models import Quiz
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
