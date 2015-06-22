from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from reports.views import ReviewView, ReviewReportDatatableView

urlpatterns = [
    url(r'^review/(?P<pk>\d+)/$', login_required(ReviewView.as_view()), name='review'),
    url(r'^peer_review/(?P<pk>\d+)/$', login_required(ReviewView.as_view(show_individual=True)), name='peer_review'),
    url(r'^reports/$', login_required(ReviewReportDatatableView.as_view()), name='report_list'),
]
