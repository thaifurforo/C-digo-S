"""
How bootcamps - Stone / código[s]
Data: 22/02/2022
Facilitador: Henrique Junqueira Branco
"""

### LISTAS ###

notas = []
# Lista vazia

notas = [10, 8.5, 6]

media = sum(notas)/len(notas)

media_arred = round(media)

aluno = 'Thainara Furforo'

print(f'O aluno {aluno.title()} ficou com a média {media}.')

print(f'A primeira nota é {notas[0]} do tipo {type(notas[0])}')
print(f'\nA segunda nota é {notas[1]} do tipo {type(notas[1])}')

lista_exemplo = [10, 4.5, None, 'teste', [4, 5, 6]]

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


nome = 'Thainara Lessa Furforo'

print(nome.split())

print(nome.split('a'))

print(f'Meu nome tem comprimento {len(nome)}.')
# conta os espaços também

notas = [10, 7, 9]
notas.append(8)

print(f"Notas: {notas}")

notas.extend([6, 3, 4])
# adiciona um identável à lista - se colocar uma string ao invés de outra lista, irá adicionar letra por letra

print(f"Notas: {notas}")

notas.insert(1, 5)
# insere item em uma posição específica (index, item_inserido)
# nesse caso insere 5 na posição 1
# funciona igual o append, porém determinando a posição

print(f"Notas: {notas}")

qtd_notas_10 = notas.count(10)

print(f'Número de notas 10: {qtd_notas_10}.')
