from django.conf.urls import patterns, url

from questions.views import QuizView


urlpatterns = patterns('',
    url(r'^view/(?P<slug>[\w-]+)/$', QuizView.as_view(), name='quiz'),
)
