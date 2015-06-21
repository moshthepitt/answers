from django.views.generic.base import TemplateView

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
        context['pending_reviews'] = Review.objects.filter(
            reviewers=self.request.user.userprofile).exclude(answer__user=self.request.user)
        return context
