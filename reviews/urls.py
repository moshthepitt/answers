from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from reviews.views import ReviewView


urlpatterns = patterns('',
    url(r'^peer-review/(?P<pk>\d+)/$', login_required(ReviewView.as_view()), name='review'),
)
