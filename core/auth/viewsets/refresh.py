from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

class RefreshViewSet(TokenRefreshView):

  permission_classes = (AllowAny,)

  def post(self, request: Request, *args, **kwargs) -> Response:
    serializer = self.get_serializer(data=request.data)
    try:
      serializer.is_valid(raise_exception=True)
    except TokenError as e:
      raise InvalidToken(e.args[0])
    return Response(serializer.validated_data, status=status.HTTP_200_OK)
