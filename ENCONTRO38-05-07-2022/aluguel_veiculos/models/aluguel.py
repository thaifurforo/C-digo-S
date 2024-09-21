from django.db import models
from django.utils import timezone
from aluguel_veiculos.models.cliente import Cliente
from aluguel_veiculos.models.veiculo import Veiculo

class Aluguel(models.Model):

  veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
  cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  data_retirada = models.DateField(default= timezone.now())
  data_devolucao = models.DateField(default= timezone.now())
  km_rodado = models.FloatField(default= 0)

  def __str__(self) -> str:
    return str(self.id)

  class Meta():
      verbose_name_plural = 'Aluguéis'
