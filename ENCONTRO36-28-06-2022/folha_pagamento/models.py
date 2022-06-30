import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class Funcionario(models.Model):
  matricula = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=6)
  nome = models.CharField(max_length=100, default='')
  cpf = models.CharField(max_length=11, default='', unique=True)
  data_admissao = models.DateField(default=timezone.now())
  cargo = models.ForeignKey('folha_pagamento.Cargo', on_delete=models.CASCADE, default=0)

  def __str__(self) -> str:
    return self.nome

class Cargo(models.Model):
  codigo_cargo = models.IntegerField(primary_key=True, default=0)
  cargo = models.CharField(max_length=100, default='')
  salario_base = models.FloatField()

  def __str__(self) -> str:
    return self.cargo