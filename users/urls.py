from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from users.views import UserProfileDatatableView, UserProfileUpdate
from users.views import UserGroupAdd, UserGroupUpdate, UserGroupDatatableView


urlpatterns = [
    url(r'^users/edit/(?P<pk>\d+)/$', login_required(UserProfileUpdate.as_view()), name='user_edit'),
    url(r'^users/$', login_required(UserProfileDatatableView.as_view()), name='user_list'),
    url(r'^groups/add/$', login_required(UserGroupAdd.as_view()), name='user_group_add'),
    url(r'^groups/edit/(?P<pk>\d+)/$', login_required(UserGroupUpdate.as_view()), name='user_group_edit'),
    url(r'^groups/$', login_required(UserGroupDatatableView.as_view()), name='user_group_list')
]
