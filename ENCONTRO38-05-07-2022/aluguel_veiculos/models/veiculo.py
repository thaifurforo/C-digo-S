from django.db import models

class Veiculo(models.Model):
  TIPO_AUTOMOVEL = 'VL'
  TIPO_CAMINHAO = 'VP'

  VEICULO_CHOICES = [(TIPO_AUTOMOVEL, 'Automóvel'), (TIPO_CAMINHAO, 'Caminhão')]

  placa = models.CharField(max_length= 7, default='')
  km = models.FloatField(default= 0)
  carga = models.FloatField(default= 0)
  bagageiro = models.IntegerField(default= 0)
  portas = models.CharField(max_length= 2, choices= VEICULO_CHOICES, default=TIPO_AUTOMOVEL)

  def __str__(self) -> str:
    return self.placa
