from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from reviews.views import PeerReviewView


urlpatterns = patterns('',
    url(r'^peer-review/(?P<pk>\d+)/$', login_required(PeerReviewView.as_view()), name='peer_review'),
)
