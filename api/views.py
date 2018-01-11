from post.models import Like, Post, ErrorConfig
from django.shortcuts import get_object_or_404
from django.db.utils import DatabaseError, IntegrityError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class LikeStatus(object):
    liked = 'liked'
    unliked = 'unliked'
    unknown = 'unknown'

class LikeView(APIView):
    """
    Like or Unlike integration for a user - post.
    Params : 
    - post_id : post_id which we need to mark liked/unliked
    If it is a new user-post call, API will mark it liked
    If user is already liking the post, API will mark it unliked now
    Returns:
    - status : 'liked' or 'unliked'
    """
    allowed_methods = ['GET', 'POST']

    def get(self, request, *args, **kwargs):
        user = request.user
        post_id = request.query_params.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        try:
            like = Like.objects.create(user=user, post=post)
            return Response({'status': LikeStatus.liked}, status=status.HTTP_200_OK)
        except IntegrityError as e:
            # IntegrityError : user already likes this post, unlike it
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response({'status': LikeStatus.unliked, 'reason': ErrorConfig.already_likes}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': LikeStatus.unknown}, status=status.HTTP_400_BAD_REQUEST)
