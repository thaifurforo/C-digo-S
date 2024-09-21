from django.db import models

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