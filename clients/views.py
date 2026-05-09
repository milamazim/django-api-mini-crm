from rest_framework.viewsets import ModelViewSet
from clients.models import Client
from clients.serializers import ClientSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all().order_by('-created_at')
    serializer_class = ClientSerializer

