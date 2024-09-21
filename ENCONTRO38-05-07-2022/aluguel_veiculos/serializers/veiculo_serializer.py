from rest_framework import serializers
from aluguel_veiculos.models import Veiculo

class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
  
  class Meta():
    model = Veiculo
    fields = ['url', 'placa', 'km', 'carga', 'bagageiro', 'portas', 'tipo']