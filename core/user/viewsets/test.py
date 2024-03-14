from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

class testViewSet(APIView):

  permission_classes = (AllowAny,)

  def get(self, request):
    return Response({'status':"statyus"}, status=status.HTTP_202_ACCEPTED)
