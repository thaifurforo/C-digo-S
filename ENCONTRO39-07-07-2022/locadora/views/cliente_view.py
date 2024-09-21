from rest_framework import viewsets
from locadora.models.cliente import Cliente
from locadora.serializers.cliente_serializer import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):

  queryset = Cliente.objects.all().order_by('nome')
  serializer_class = ClienteSerializer

