from core.abstract.viewsets import AbstractViewSet
from rest_framework.permissions import IsAuthenticated
from core.post.serializers import PostSerializer
from core.post.models import Post
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status


class LikeUser(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    def get_object(self, pk):
        try:
            return Post.objects.get(public_id=pk)
        except Post.DoesNotExist:
            raise NotFound("Post not found")

    def post(self, request, *args, **kwargs):
        post = self.get_object(pk=kwargs['pk'])
        user = self.request.user
        user.like(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
