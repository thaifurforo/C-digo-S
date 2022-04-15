"""
How bootcamps - Stone / código[s]
Data: 22/02/2022
Facilitador: Henrique Junqueira Branco
"""

### TUPLAS ###

meses = ('Jan', 'Fev', 'Mar', 'Abr')
# tupla é usada para que ninguém possa alterar os dados

print(meses[0])

# meses[0] = 'Mês errado'
# gera mensagem de erro pois a tupla é imutável
# não é possível modificar nem acrescentar ou remover elementos

meses_list = ['Jan', 'Fev', 'Mar', 'Abr']
meses_list[0] = 'Mês errado'
print(f'\n{meses_list}')

# métodos aplicáveis à tupla:
print(f'\n{meses.count("Fev")}')
print(meses.index('Mar'))

meses_tuple = tuple(meses_list)
# transforma lista em tupla

print(f'\n{meses_tuple}')
print(type(meses_tuple))
