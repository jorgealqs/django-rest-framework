from rest_framework import filters
from rest_framework.views import APIView

class AbstractViewSet(APIView):
  filter_backends = [filters.OrderingFilter]
  ordering_fields = ['updated', 'created']
  ordering = ['-updated']