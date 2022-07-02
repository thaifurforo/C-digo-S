from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
  PESSOA_FISICA = 'PF'
  PESSOA_JURIDICA = 'PJ'

  CLIENTE_CHOICES = [(PESSOA_FISICA, 'Física'), (PESSOA_JURIDICA, 'Jurídica')]
  nome = models.CharField(max_length= 100, default='')
  endereco = models.CharField(max_length= 100, default='')
  telefone = models.CharField(max_length= 14, default='')
  cpf = models.CharField(max_length= 11, null= True, blank= True)
  cnpj = models.CharField(max_length= 14, null= True, blank= True)
  tipo = models.CharField(max_length=2, choices=CLIENTE_CHOICES, default=PESSOA_FISICA)

  def __str__(self) -> str:
    return self.nome

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
