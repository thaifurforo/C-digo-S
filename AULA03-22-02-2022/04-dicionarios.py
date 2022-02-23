"""
How bootcamps - Stone / código[s]
Data: 22/02/2022
Facilitador: Henrique Junqueira Branco
"""

estados = {'SP': 'São Paulo', 'MG': 'Minas Gerais'}
# SP e MG são keys ; São Paulo e Minas Gerais são valores.

print(type(estados))

print(estados['SP'])

fechamento = {'notas': [10, 9, 7], 'alunos': ['João', 'Maria', 'Tiago']}
print(f'\n{fechamento}')

fechamento['alunos'].append('Ander')
fechamento['notas'].append(8)
print(f'\n{fechamento}')
# modificou a lista: lista é mutável

fechamento['notas_recuperacao'] = [2, 3, 1, 4]
print(f'\n{fechamento}')
# modificou o dicionário, dicionário é mutável

# fechamento[0] - gera key error
# valores do dicionário não podem ser acessados por posição, apenas pela key

print(f'\nlist(dict) -> {list(fechamento)}')
# faz uma lista com as keys do dicionário

print(f'\nlen(dict) -> {len(fechamento)}')

print(f'\nkey in dict -> {"notas" in fechamento}')
# verifica se existe esta key no dicionário para

print(f'\ndict.items() -> {fechamento.items()}')
# retorna lista de tuplas com os pares de chave (key) e valor, para que seja possível separar os valores depois

print(f'\ndict.keys() -> {fechamento.keys()}')
# retorna uma lista com as keys do dicionário

print(f'\ndict.values() -> {fechamento.values()}')
# retorna uma lista com os valores pares de cada key do dicionário
