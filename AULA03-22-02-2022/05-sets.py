"""
How bootcamps - Stone / código[s]
Data: 22/02/2022
Facilitador: Henrique Junqueira Branco
"""

### SETS ###
# Teoria dos conjuntos

nome = 'Thainara Lessa Furforo'
nome_set = set(nome)
print(type(nome_set))
print(nome_set)
# Valores únicos dentro de um conjunto - string, lista etc
# O set não tem ordem, por isso não é possível acessar um valor do mesmo

nome_set_lista = list(nome_set)
# transforma o set em lista
print(nome_set_lista)

nome_esposo = set('Alex Cesar da Silva')
print(nome_esposo)

caracteres_em_comum = nome_set & nome_esposo
# intersection
print(caracteres_em_comum)

caracteres_diferentes = nome_set - nome_esposo
# difference
print(caracteres_diferentes)
