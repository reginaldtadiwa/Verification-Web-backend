"""from rest_framework import viewsets
from .models import results
from .serializers import ResSerializer
from .filters import ResultModelFilter

class ResultModelViewSet(viewsets.ModelViewSet):
    queryset = results.objects.all()
    serializer_class = ResSerializer
    filterset_class = ResultModelFilter """
"""
    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply any additional filtering logic here if needed
        return queryset.filter(**self.request.query_params)
"""

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import results
from .serializers import ResSerializer
from .filters import ResultModelFilter

class ResultModelViewSet(viewsets.ModelViewSet):
    queryset = results.objects.all()
    serializer_class = ResSerializer
    filterset_class = ResultModelFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            return Response({"detail": "No results found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)