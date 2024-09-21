from rest_framework import serializers
from locadora.models.cliente import Cliente

class ClienteSerializer(serializers.ModelSerializer):
  nome = serializers.CharField(max_length=120)

  class Meta:
    model = Cliente
    fields = '__all__'