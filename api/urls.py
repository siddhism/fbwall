from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^like/$', LikeView.as_view(), name='like'),
    url(r'^userlikes/$', LikeDetail.as_view(), name='userlikes'),
]
