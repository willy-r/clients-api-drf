from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from clients.serializers import ClientSerializer
from clients.models import Client


class ClientViewSet(viewsets.ModelViewSet):
    """Listing all clients."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['is_active']
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
