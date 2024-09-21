from rest_framework import serializers
from aluguel_veiculos.models import Aluguel

class AluguelSerializer(serializers.HyperlinkedModelSerializer):
  
  class Meta():
    model = Aluguel
    fields = ['url', 'veiculo', 'cliente', 'data_retirada', 'data_devolucao', 'km_rodado']