from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status
from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment
from core.post.models import Post
from core.comment.serializers import CommentSerializer
# from core.auth.permissions import UserPermission
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class CommentViewSet(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_pk = self.kwargs.get('pk_post')
        get_object_or_404(Post, public_id=post_pk)
        queryset = Comment.objects.filter(post__public_id=post_pk).order_by('-id')
        return queryset

    def get(self, request, *args, **kwargs):
        comments = self.get_queryset()
        serializer = self.serializer_class(comments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            post_pk = self.kwargs.get('pk_post')
            post = get_object_or_404(Post, public_id=post_pk)
            serializer.save(post=post)  # Asignar el post al comentario
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
