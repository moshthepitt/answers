from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse

from reviews.models import PeerReview
from reviews.mixins import PeerReviewMixin
from reviews.utils import save_peer_review
from questions.forms import make_quiz_form, quiz_form_helper


class PeerReviewView(PeerReviewMixin, FormMixin, DetailView):
    model = PeerReview

    def get_success_url(self):
        return reverse('home')

    def get_form_class(self):
        return make_quiz_form(self.object.quiz)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        save_peer_review(self.object.quiz, form)
        return super(PeerReviewView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PeerReviewView, self).get_context_data(**kwargs)
        form = self.get_form()
        context['form'] = form
        context['form_helper'] = quiz_form_helper(self.object.quiz)
        return context

    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        return super(PeerReviewView, self).dispatch(*args, **kwargs)
