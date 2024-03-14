import logging
import json
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers.register import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Configura el logger
logger = logging.getLogger(__name__)


class CreateUserViewSet(APIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    try:
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      refresh = RefreshToken.for_user(user)
      res = {
          "refresh": str(refresh),
          "access": str(refresh.access_token),
      }
      logger.info(f"Usuario creado exitosamente: {user.email}")
      return Response({
          "user": serializer.data,
          "refresh": res["refresh"],
          "token": res["access"]
      }, status=status.HTTP_201_CREATED)
    except Exception as e:
      error_message = str(e)
      logger.error(f"Error al crear usuario: {str(e)}")
      return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
