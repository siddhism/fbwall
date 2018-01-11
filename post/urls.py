from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', login_required(IndexView.as_view()), name='index'),
    url(r'^create-post/$', CreatePostView.as_view(), name='create_post'),
]
