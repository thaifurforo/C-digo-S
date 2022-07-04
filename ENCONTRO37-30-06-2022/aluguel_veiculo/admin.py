from django.contrib import admin

from aluguel_veiculo.models import Aluguel, Cliente, Veiculo

class ClienteAdmin(admin.ModelAdmin):
  fields = ('nome', 'endereco')
  list_display = ('tipo', 'nome', 'endereco')

class VeiculoAdmin(admin.ModelAdmin):
  fields = ('placa', 'km', 'carga', 'bagageiro', 'portas', 'tipo')
  list_display = ('placa', 'km')

class AluguelAdmin(admin.ModelAdmin):
  fields = ('veiculo', 'cliente', 'data_retirada', 'data_devolucao', 'km_rodado')
  list_display = ('veiculo', 'cliente', 'data_retirada', 'data_devolucao', 'km_rodado')

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Aluguel, AluguelAdmin)

