from django.views.generic.detail import DetailView

from questions.models import Quiz
from questions.utils import make_quiz_form, quiz_form_helper


class QuizView(DetailView):
    model = Quiz

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        context['form'] = make_quiz_form(self.get_object())
        context['form_helper'] = quiz_form_helper(self.get_object())
        return context
