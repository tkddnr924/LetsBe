from django.conf.urls import url
from analy.views import *


urlpatterns = [
    # Example : /result/user_id
    url(r'^(?P<pk>\d+)$', UserDV.as_view(), name='index'),

    # Example : /result/user_id/picture_list
    url(r'^(?P<pk>\d+)/picture_list', PictureDV.as_view(), name='picture_list'),

    # Exmaple : /another_user
    url(r'^another_user', UserLV.as_view(), name='another_user'),

    # Example : /another_user/user_id
    url(r'^another_user/(?P<pk>\d+)', AnotherUserDV.as_view(), name='another'),
]