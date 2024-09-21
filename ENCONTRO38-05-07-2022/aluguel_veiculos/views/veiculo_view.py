from rest_framework import viewsets, permissions
from aluguel_veiculos.models import Veiculo
from aluguel_veiculos.serializers import VeiculoSerializer

# Create your views here.
class VeiculoViewSet(viewsets.ModelViewSet):
  queryset = Veiculo.objects.all()
  serializer_class = VeiculoSerializer
  permission_classes = [permissions.IsAuthenticated]