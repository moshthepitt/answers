from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from reviews.models import Review

from answers.models import Answer
from django.db.models import Value, Avg
from django.db.models.functions import Coalesce


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


class ReviewListView(ListView):

    model = Review
    template_name = "reports/reviews_list.html"

    def get_queryset(self):
        return Review.objects.exclude(answer=None)

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        return context


class ReviewView(DetailView):
    model = Review
    template_name = "reports/review.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        report = user_review_report(self.get_object())
        context['review'] = report[0]
        context['scores'] = report[1]
        return context
