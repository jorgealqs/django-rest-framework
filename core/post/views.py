from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from core.abstract.viewsets import AbstractViewSet
from core.post.models import Post
from core.user.models import User
from core.post.serializers import PostSerializer
from rest_framework.exceptions import APIException
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action
from rest_framework import serializers


class PostViewSet(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Post.objects.all().order_by('-id')

    def get_object(self, pk):
        try:
            return Post.objects.get(public_id=pk)
        except Post.DoesNotExist:
            raise NotFound("Post not found")

    def delete(self, request, pk=None):
        if pk is not None:
            post = self.get_object(pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "No post ID provided"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, author_public_id=None):
        if author_public_id:
            try:
                author = User.objects.get(public_id=author_public_id)
                queryset = Post.objects.filter(author=author)
                # Aquí puedes realizar cualquier filtrado o manipulación adicional del queryset si es necesario
            except User.DoesNotExist:
                return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = self.get_queryset()

        if pk:
            try:
                post = queryset.get(public_id=pk)
                serializer = PostSerializer(post, context={'request': request})
                return Response(serializer.data)
            except Post.DoesNotExist:
                return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True, context={'request': request})
            return paginator.get_paginated_response(serializer.data)

    def put(self, request, pk):
        try:
            post = self.get_object(pk)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except APIException as e:
            # Manejo de la excepción y devolución de una respuesta personalizada
            error_message = {"error": str(e)}
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
