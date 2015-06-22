from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from questions.views import QuizView, QuizDatatableView, QuizAdd, QuizUpdate
from questions.views import quiz_questions

urlpatterns = [
    url(r'^view/(?P<slug>[\w-]+)/$', login_required(QuizView.as_view()), name='quiz'),
    url(r'^question-sets/add/$', login_required(QuizAdd.as_view()), name='quiz_add'),
    url(r'^question-sets/edit/(?P<pk>\d+)/$', login_required(QuizUpdate.as_view()), name='quiz_edit'),
    url(r'^question-sets/$', login_required(QuizDatatableView.as_view()), name='quiz_list'),
    url(r'^quiz-questions/(?P<pk>\d+)/$', login_required(quiz_questions), name='quiz_questions'),
]
