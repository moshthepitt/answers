from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from django.conf import settings

from core.views import HomePageView, DashboardView

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^dashboard/$', login_required(DashboardView.as_view()), name='dashboard'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^q/', include('questions.urls', namespace='questions')),
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),

    url(r'^page/', include('django.contrib.flatpages.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    )
