from rest_framework import viewsets
from aluguel_veiculo.models import Cliente, Veiculo
from aluguel_veiculo.serializer import ClienteSerializer, VeiculoSerializer

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
  queryset = Veiculo.objects.all()
  serializer_class = VeiculoSerializer