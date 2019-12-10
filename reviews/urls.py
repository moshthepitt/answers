from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from reviews.views import PublicReviewView, ReviewView, ReviewDatatableView, PeerReviewDatatableView
from reviews.views import ReviewAdd, ReviewUpdate, PeerReviewUpdate, PeerReviewAdd
from reviews.views import TestReportView


urlpatterns = [
    url(r'^review/(?P<pk>\d+)/$', login_required(ReviewView.as_view()), name='review'),
    url(r'^anonymous/(?P<pk>\d+)/$', PublicReviewView.as_view(), name='anonymous_review'),
    url(r'^test-report/(?P<pk>\d+)/$', TestReportView.as_view(), name='test_report'),
    url(r'^reviews/add/$', login_required(ReviewAdd.as_view()), name='review_add'),
    url(r'^reviews/edit/(?P<pk>\d+)/$', login_required(ReviewUpdate.as_view()), name='review_edit'),
    url(r'^reviews/$', login_required(ReviewDatatableView.as_view()), name='review_list'),
    url(r'^peer-reviews/add/$', login_required(PeerReviewAdd), name='peer_review_add'),
    url(r'^peer-reviews/edit/(?P<pk>\d+)/$', login_required(PeerReviewUpdate), name='peer_review_edit'),
    url(r'^peer-reviews/$', login_required(PeerReviewDatatableView.as_view()), name='peer_review_list'),
    url(r'^thanks/$', TemplateView.as_view(template_name="reviews/thanks.html"), name='thanks'),
]
