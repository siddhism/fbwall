from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class ErrorConfig(object):
    already_likes = 'User already likes this post'

class Post(models.Model):

    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='media',null=True, blank=True)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_liked_by(self, user):
        try:
            like = Like.objects.get(user=user, post=post)
            return Response({'status': True}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'status': False}, status=status.HTTP_200_OK)


    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    

class Like(models.Model):

    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)

    def save(self, **kwargs):
        super(Like, self).save(**kwargs)
        # qs = Like.objects.filter(post=self.post, user=self.user)
        # if qs.exists():
        #     raise ValidationError(ErrorConfig.already_likes)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        unique_together = ['post', 'user']

    def __str__(self):
        return self.user.username + " likes " + self.post.title
