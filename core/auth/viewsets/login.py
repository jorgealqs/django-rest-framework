from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.response import Response
from rest_framework import status
from core.auth.serializers.login import LoginSerializer
from core.abstract.viewsets import AbstractViewSet

class LoginViewSet(AbstractViewSet):
  serializer_class = LoginSerializer
  permission_classes = (AllowAny,)

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    try:
      serializer.is_valid(raise_exception=True)
    except TokenError as e:
      raise InvalidToken(e.args[0])
    return Response(serializer.validated_data, status=status.HTTP_200_OK)
