from rest_framework import serializers
from aluguel_veiculos.models import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    telefone = serializers.CharField(min_length=9)
    cnpj = serializers.CharField(required=False)

    class Meta():
        model = Cliente
        fields = ['url', 'nome', 'endereco', 'telefone', 'cpf', 'cnpj', 'tipo']

    def validate(self, data):
        if (data['tipo'] == 'PJ' and data['cnpj'] == None):
            raise serializers.ValidationError(
                {'CNPJ': 'Obrigatório informar CNPJ caso Pessoa Jurídica'})
        elif (data['tipo'] == 'PF' and data['cpf'] == None):
            raise serializers.ValidationError(
                {'CPF': 'Obrigatório informar CPF caso Pessoa Física'})
        return data
