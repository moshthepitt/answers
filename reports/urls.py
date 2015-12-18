from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from reports.views import ReviewView, ReviewReportDatatableView, PendingReviewsReportDatatableView
from reports.views import SittingReport

urlpatterns = [
    url(r'^review/(?P<pk>\d+)/$', login_required(ReviewView.as_view()), name='review'),
    url(r'^peer-review/(?P<pk>\d+)/$',
        login_required(ReviewView.as_view(show_individual=True)), name='peer_review'),
    url(r'^reports/$', login_required(ReviewReportDatatableView.as_view()), name='report_list'),
    url(r'^sitting/(?P<pk>\d+)/$', login_required(SittingReport.as_view()), name='sitting'),
    url(r'^completion/sitting/(?P<pk>\d+)/$',
        login_required(PendingReviewsReportDatatableView.as_view()), name='sitting_completion_report'),
]
