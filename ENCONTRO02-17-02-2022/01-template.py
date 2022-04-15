""" 
How Bootcamps - Stone /código[s]
Data: 17/02/2022
Autor: Henrique Junqueira Branco
Enunciado: Introdução à sintaxe e tipos de dados
"""

# Cálculo de média de duas notas
nota1 = 8
nota2 = 10
print(nota1 + nota2 / 2)
# Errado porque faz a divisão de nota2 por 2 primeiro e depois soma a nota1 ao resultado

media = (nota1 + nota2) / 2
print(media)
# Correto. Obs.: divisão sempre retorna número float, mesmo quando o resultado for inteiro.

print(type(nota1))
print(type(nota2))
print(type(media))

nota1 = 8.0
print(type(nota1))
print(type(nota2))
print(type(media))

numero = - 3 ** 2
print(numero)
numero = (-3) ** 2
print(numero)

aluno = 'thainara furforo'

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media_float = (nota1 + nota2 + nota3) / 3
media = round(media_float)
print(f'O aluno {aluno.title()} ficou com a média {media}.')

print(aluno.upper())
print(aluno.capitalize())

letra = 'a'

print(f'No meu nome existem {aluno.count(letra)} letras {letra}.')

string_vazia = '       '

print(f'Na string vazia tem {len(string_vazia)} caracteres.')

novo_nome = aluno.replace("a", "e")

print(
    f'Se substituir todos os "a" do meu nome por "e", o meu novo nome seria: {novo_nome}')

nome = 'Thainara'
sobrenome = 'Furforo'

print(nome+''+sobrenome)
print(nome, '', sobrenome)
print(f'{nome} {sobrenome}')
