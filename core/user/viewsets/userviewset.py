import uuid
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.user.serializers import UserSerializer
from core.user.models import User
from rest_framework.response import Response
from core.abstract.viewsets import AbstractViewSet

class UserViewSetApiView(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, public_id=None):
      if public_id is not None:
        try:
            # Intenta convertir el public_id en un UUID
            public_id = uuid.UUID(public_id)
        except ValueError:
            return Response({"error": "User not find"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset().filter(public_id=public_id)
        if not queryset.exists():
            return Response({"error": "User not find"}, status=status.HTTP_404_NOT_FOUND)
      else:
          queryset = self.get_queryset()

      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, public_id=None):
      if public_id is not None:
        try:
          public_id = uuid.UUID(public_id)
        except ValueError:
          return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset().filter(public_id=public_id)
        if not queryset.exists():
          return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        user = queryset.first()
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
        else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
