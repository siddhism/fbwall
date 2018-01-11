from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.generic.edit import FormView
from django.views.generic.edit import FormMixin    

from .models import Like, Post
from .forms import PostForm

class IndexView(FormMixin, ListView):
    form_class = PostForm
    model = Post

    def get_success_url(self):
        return reverse('home:index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super(CreatePostView, self).form_valid(form)


class CreatePostView(FormView):
    form_class = PostForm
    template_name = 'post/post_create.html'

    def get_success_url(self):
        return reverse('home:index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super(CreatePostView, self).form_valid(form)
