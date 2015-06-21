from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse

from reviews.models import Review
from reviews.mixins import ReviewMixin
from questions.forms import make_quiz_form, quiz_form_helper, save_quiz_form


class ReviewView(ReviewMixin, FormMixin, DetailView):
    model = Review

    def get_success_url(self):
        return reverse('dashboard')

    def get_form_class(self):
        return make_quiz_form(self.object.quiz)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        save_quiz_form(self.object.quiz, form, self.request.user, self.object)
        return super(ReviewView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        form = self.get_form()
        context['form'] = form
        context['form_helper'] = quiz_form_helper(self.object.quiz)
        return context

    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        return super(ReviewView, self).dispatch(*args, **kwargs)
