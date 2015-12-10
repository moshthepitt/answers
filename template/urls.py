from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from django.conf import settings

from core.views import HomePageView, DashboardView, GenericMessageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^dashboard/$', login_required(DashboardView.as_view()), name='dashboard'),
    url(r'^send-message/$', login_required(GenericMessageView.as_view()), name='dashboard'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^q/', include('questions.urls', namespace='questions')),
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),
    url(r'^reports/', include('reports.urls', namespace='reports')),
    url(r'^users/', include('users.urls', namespace='users')),

    url(r'^page/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    ]
