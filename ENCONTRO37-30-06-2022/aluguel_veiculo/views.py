from rest_framework import viewsets
from aluguel_veiculo.models import Aluguel, Cliente, Veiculo
from aluguel_veiculo.serializer import AluguelSerializer, ClienteSerializer, VeiculoSerializer

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
  queryset = Veiculo.objects.all()
  serializer_class = VeiculoSerializer

class AluguelViewSet(viewsets.ModelViewSet):
  queryset = Aluguel.objects.all()
  serializer_class = AluguelSerializer