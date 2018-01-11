from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^like/(?P<post_id>\d+)/$', LikeView.as_view(), name='like'),
    url(r'^userlikes/(?P<post_id>\d+)/$', LikeDetail.as_view(), name='userlikes'),
]
