from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from users.views import UserProfileDatatableView, UserProfileUpdate


urlpatterns = [
    url(r'^users/edit/(?P<pk>\d+)/$', login_required(UserProfileUpdate.as_view()), name='user_edit'),
    url(r'^users/$', login_required(UserProfileDatatableView.as_view()), name='user_list')
]
