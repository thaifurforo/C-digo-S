from rest_framework import viewsets, permissions
from aluguel_veiculos.models import Cliente
from aluguel_veiculos.serializers import ClienteSerializer

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer
  permission_classes = [permissions.IsAuthenticated]