from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^like/$', LikeView.as_view(), name='like'),
]
