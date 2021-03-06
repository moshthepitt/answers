from django.views.generic.base import TemplateView
from django.db.models import Q
from django.views.generic.edit import FormView

from reviews.models import Review
from reports.views import user_review_report

from .mixins import AdminMixin
from .forms import GenericMessage


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


class DashboardView(TemplateView):

    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        pending_reviews = Review.objects.filter(customer=self.request.user.userprofile.customer).filter(
            Q(reviewers=self.request.user.userprofile) | Q(public=True)).exclude(
            Q(answer__userprofile=self.request.user.userprofile) & Q(quiz__single_attempt=True)
        )

        reports = []
        reviews = Review.objects.filter(customer=self.request.user.userprofile.customer).filter(
            userprofile=self.request.user.userprofile).order_by('-created_on')[:4]
        if reviews:
            sittings = [i.sitting for i in reviews]
            current_sitting = max(set(sittings), key=sittings.count)
            reviews = Review.objects.filter(customer=self.request.user.userprofile.customer).filter(
                userprofile=self.request.user.userprofile).filter(
                sitting=current_sitting).order_by('-created_on')[:3]
            for review in reviews:
                report = user_review_report(review)
                reports.append(report)

        context['pending_reviews'] = pending_reviews
        context['reports'] = reports
        return context


class GenericMessageView(AdminMixin, FormView):
    template_name = 'core/generic-message.html'
    form_class = GenericMessage
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.send_email(self.request.user.userprofile.customer)
        return super(GenericMessageView, self).form_valid(form)
