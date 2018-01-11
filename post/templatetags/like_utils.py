from django import template
from django.shortcuts import get_object_or_404

from post.models import Like, Post

register = template.Library()

@register.simple_tag(name='is_liked_by')
def is_liked_by(post_id, user):
    post = get_object_or_404(Post, pk=post_id)
    try:
        like = Like.objects.get(user=user, post=post)
        return True
    except Like.DoesNotExist:
        return False

@register.filter(name='addclass')
def addclass(field, css):
    if field:
        return field.as_widget(attrs={"class":css})
    else:
        return ''
