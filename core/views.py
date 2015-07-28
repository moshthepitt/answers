from django.views.generic.base import TemplateView
from django.db.models import Q

from reviews.models import Review


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


class DashboardView(TemplateView):

    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        pending_reviews = Review.objects.filter(
            Q(reviewers=self.request.user.userprofile) | Q(public=True)).exclude(
            Q(answer__userprofile=self.request.user.userprofile) & Q(quiz__single_attempt=True)
        )
        context['pending_reviews'] = pending_reviews
        return context
