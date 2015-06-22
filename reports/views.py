from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.utils.html import format_html
from django.db.models import Value, Avg
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404
from django.http import Http404

from datatableview.views import DatatableView

from reviews.models import Review
from answers.models import Answer
from users.models import UserProfile


def user_review_report(review):
    scores = []
    for question in review.quiz.get_questions():
        score = Answer.objects.filter(question=question).filter(
            review=review).aggregate(avg=Coalesce(Avg('ratinganswer__answer'), Value(0)))
        company_score = Answer.objects.filter(question=question).filter(
            review__quiz=review.quiz).aggregate(avg=Coalesce(Avg('ratinganswer__answer'), Value(0)))
        question.score = score['avg']
        question.percentage_score = question.score * 100 / 5
        question.company_score = company_score['avg']
        question.company_percentage_score = question.company_score * 100 / 5
        scores.append(question)
    overall_score = Answer.objects.filter(review=review).aggregate(
        avg=Coalesce(Avg('ratinganswer__answer'), Value(0)))
    overall_company_score = Answer.objects.filter(review__quiz=review.quiz).aggregate(
        avg=Coalesce(Avg('ratinganswer__answer'), Value(0)))
    review.score = overall_score['avg']
    review.percentage_score = review.score * 100 / 5
    review.company_score = overall_company_score['avg']
    review.company_percentage_score = review.company_score * 100 / 5
    return (review, scores)


class ReviewView(DetailView):
    model = Review
    template_name = "reports/review.html"
    show_individual = False

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        report = user_review_report(self.get_object())
        context['review'] = report[0]
        context['scores'] = report[1]
        context['show_individual'] = self.show_individual
        return context


class ReviewersDatatableView(DatatableView):
    model = UserProfile
    template_name = "reports/reviewers_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            (_("Username"), 'user__username'),
            (_("First Name"), 'user__first_name'),
            (_("Last Name"), 'user__last_name'),
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['title'],
        'unsortable_columns': ['id'],
    }
    review_type = None

    def get_queryset(self):
        # queryset = super(ReviewersDatatableView, self).get_queryset()
        queryset = self.object.userprofile_set.all()
        return queryset

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{}">Report</a>', 1
        )

    def dispatch(self, *args, **kwargs):
        if 'pk' not in kwargs:
            raise Http404
        self.object = get_object_or_404(Review, pk=kwargs['pk'])
        return super(ReviewersDatatableView, self).dispatch(*args, **kwargs)
