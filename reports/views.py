from django.views.generic.detail import DetailView
from django.db.models import Value, Avg, Q, F, Count, ExpressionWrapper, FloatField
from django.db.models.functions import Coalesce
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.utils.html import format_html
from django.shortcuts import get_object_or_404

from datatableview.views import DatatableView

from reports.mixins import ReportMixin
from core.mixins import AdminMixin
from saas.mixins import CustomerListViewMixin, CustomerCheckMixin
from reviews.models import Review
from answers.models import Answer
from questions.models import RatingQuestion, EssayQuestion, Sitting


def user_review_report(review):
    scores = []
    for question in review.quiz.get_questions().instance_of(RatingQuestion):
        score = Answer.objects.filter(question=question).filter(
            review=review).aggregate(avg=Coalesce(Avg('ratinganswer__answer'), Value(0)))
        company_score = Answer.objects.filter(question=question).filter(review__sitting=review.sitting).filter(
            review__quiz=review.quiz).aggregate(avg=Coalesce(Avg('ratinganswer__answer'), Value(0)))
        question.score = score['avg']
        question.percentage_score = question.score * 100 / 5
        question.company_score = company_score['avg']
        question.company_percentage_score = question.company_score * 100 / 5
        scores.append(question)

    if scores:
        number_of_reviewers = Answer.objects.filter(
            review=review, review__sitting=review.sitting).count() / review.quiz.get_questions().count()

    overall_score = Answer.objects.filter(review=review).aggregate(
        avg=Coalesce(Avg('ratinganswer__answer'), Value(0)))
    overall_company_score = Answer.objects.filter(review__quiz=review.quiz).filter(review__sitting=review.sitting).aggregate(
        avg=Coalesce(Avg('ratinganswer__answer'), Value(0)))

    review.score = overall_score['avg']
    review.percentage_score = review.score * 100 / 5
    review.company_score = overall_company_score['avg']
    review.company_percentage_score = review.company_score * 100 / 5
    review.number_of_reviewers = number_of_reviewers
    return (review, scores)


def user_text_answers(review):
    """
    returns all the Essay type questions
    """
    result = []
    for question in review.quiz.get_questions().instance_of(EssayQuestion):
        question.answers = Answer.objects.filter(question=question).filter(review=review)
        result.append(question)
    return result


class ReviewView(CustomerCheckMixin, ReportMixin, DetailView):
    model = Review
    template_name = "reports/review.html"
    show_individual = False

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        report = user_review_report(self.get_object())
        context['review'] = report[0]
        context['scores'] = report[1]
        context['text_answers'] = user_text_answers(self.get_object())
        context['show_individual'] = self.show_individual
        return context


class ReviewReportDatatableView(CustomerListViewMixin, DatatableView):

    """
    Displays a list of reviews that the user has access to
    """
    model = Review
    template_name = "reports/report_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            'title',
            'sitting',
            'quiz',
            (_("User"), 'userprofile', 'get_user'),
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['title', 'userprofile__user__last_name', 'userprofile__user__first_name', 'userprofile__user__username'],
        'unsortable_columns': ['id'],
    }

    def get_user(self, instance, *args, **kwargs):
        if instance.userprofile:
            return instance.userprofile.get_display_name()
        return ""

    def get_queryset(self):
        """
        return any report which is about the current user, or which they have access to
        one has access to:
            any report of someone they manage
        """
        queryset = super(ReviewReportDatatableView, self).get_queryset()
        queryset = queryset.filter(Q(userprofile=self.request.user.userprofile) | Q(
            userprofile__manager=self.request.user.userprofile) | Q(userprofile__group__manager=self.request.user.userprofile))
        return queryset.distinct()

    def get_actions(self, instance, *args, **kwargs):
        if instance.userprofile:
            return format_html(
                '<a href="{}">Report</a>', reverse('reports:peer_review', args=[instance.pk])
            )
        else:
            return format_html(
                '<a href="{}">Report</a>', reverse('reports:review', args=[instance.pk])
            )


class PendingReviewsReportDatatableView(AdminMixin, CustomerListViewMixin, DatatableView):

    """
    Displays a list of reviews and how many people have reviewed
    """
    model = Review
    template_name = "reports/report_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            (_("User"), 'userprofile', 'get_user'),
            'title',
            'sitting',
            'quiz',
            (_("No. of Reviewers"), 'no_reviewers', 'get_no_reviewers'),
            (_("Completed"), 'answered', 'get_answered'),
        ],
        'search_fields': ['title', 'userprofile__user__last_name', 'userprofile__user__first_name', 'userprofile__user__username'],
        'unsortable_columns': ['id'],
    }

    def get_user(self, instance, *args, **kwargs):
        if instance.userprofile:
            return instance.userprofile.get_display_name()
        return ""

    def get_answered(self, instance, *args, **kwargs):
        return int(instance.answered)

    def get_no_reviewers(self, instance, *args, **kwargs):
        return instance.no_reviewers

    def get_queryset(self):
        """
        return any report which is about the current user, or which they have access to
        one has access to:
            any report of someone they manage
        """
        queryset = super(PendingReviewsReportDatatableView, self).get_queryset()
        queryset = queryset.exclude(userprofile=None).filter(sitting=self.sitting).annotate(
            no_reviewers=Count('reviewers', distinct=True)).annotate(
            no_answers=Count('answer', distinct=True)).annotate(
            no_questions=Count('quiz__question', distinct=True)).annotate(
            answered=ExpressionWrapper(F('no_answers') / F('no_questions'), output_field=FloatField())).order_by('answered')

        return queryset.distinct()

    def dispatch(self, *args, **kwargs):
        self.sitting = get_object_or_404(Sitting, pk=self.kwargs['pk'])
        return super(PendingReviewsReportDatatableView, self).dispatch(*args, **kwargs)
