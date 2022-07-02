from django.contrib import admin

from aluguel_veiculo.models import Aluguel, Cliente, Veiculo

class ClienteAdmin(admin.ModelAdmin):
  fields = ('nome', 'endereco')
  list_display = ('tipo', 'nome', 'endereco')

class AluguelAdmin(admin.ModelAdmin):
  list_display = ('veiculo', 'cliente', 'data_retirada', 'data_devolucao', 'km')

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Aluguel)

