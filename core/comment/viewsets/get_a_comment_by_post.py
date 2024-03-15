from rest_framework.response import Response
from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment
from core.post.models import Post
from core.comment.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status


class CommentDetailView(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_object(self):
        post_pk = self.kwargs.get('pk_post')
        comment_pk = self.kwargs.get('pk_comment')

        # Verificar si el post existe
        post = get_object_or_404(Post, public_id=post_pk)

        # Obtener el comentario si existe en relación con el post
        comment = get_object_or_404(Comment, post=post, public_id=comment_pk)

        self.check_object_permissions(self.request, comment)
        return comment

    def get(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = self.serializer_class(comment)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = self.serializer_class(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
