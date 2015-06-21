from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from reviews.views import ReviewView, ReviewDatatableView, PeerReviewDatatableView
from reviews.views import ReviewAdd, ReviewUpdate, PeerReviewUpdate, PeerReviewAdd


urlpatterns = [
    url(r'^review/(?P<pk>\d+)/$', login_required(ReviewView.as_view()), name='review'),
    url(r'^reviews/add/$', login_required(ReviewAdd.as_view()), name='review_add'),
    url(r'^reviews/edit/(?P<pk>\d+)/$', login_required(ReviewUpdate.as_view()), name='review_edit'),
    url(r'^reviews/$', login_required(ReviewDatatableView.as_view()), name='review_list'),
    url(r'^peer-reviews/add/$', login_required(PeerReviewAdd), name='peer_review_add'),
    url(r'^peer-reviews/edit/(?P<pk>\d+)/$', login_required(PeerReviewUpdate), name='peer_review_edit'),
    url(r'^peer-reviews/$', login_required(PeerReviewDatatableView.as_view()), name='peer_review_list'),
]
