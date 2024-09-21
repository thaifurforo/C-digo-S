from rest_framework import viewsets, permissions
from aluguel_veiculos.models import Aluguel
from aluguel_veiculos.serializers import AluguelSerializer

# Create your views here.
class AluguelViewSet(viewsets.ModelViewSet):
  queryset = Aluguel.objects.all()
  serializer_class = AluguelSerializer
  permission_classes = [permissions.IsAuthenticated]