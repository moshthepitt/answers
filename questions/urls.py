from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from questions.views import QuizView, QuizDatatableView


urlpatterns = [
    url(r'^view/(?P<slug>[\w-]+)/$', login_required(QuizView.as_view()), name='quiz'),
    url(r'^question-sets/$', login_required(QuizDatatableView.as_view()), name='quiz_list'),
]
