"""
How bootcamps - Stone / código[s]
Data: 08-03-2022
Facilitador: Henrique Junqueira Branco
Tema: Estrutura de repetição
"""

numero_de_alunos = int(input('Digite o número de alunos: '))
numero_de_notas = int(input('Digite o número de notas por aluno: '))

notas_por_aluno = dict()
# dict() cria dicionário vazio, equivalente a = {}

# O underline _ na variável do for significa que a variável não faz diferença
for _ in range(numero_de_alunos):
    aluno = input('Digite o nome do aluno: ')
    notas = list()
    # list() cria lista vazia, equivalente a = []
    for n in range(numero_de_notas):
        notas.append(int(input(f'Digite a nota nº {n+1} do aluno {aluno}: ')))
    notas_por_aluno[aluno] = notas

media_do_aluno = dict()

nota_minima_aprovacao = 7
nota_minima_recuperacao = 6

for aluno, notas_do_aluno in notas_por_aluno.items():
    media_do_aluno[aluno] = sum(notas_do_aluno) / len(notas_do_aluno)
    if media_do_aluno[aluno] >= nota_minima_aprovacao:
        status = 'aprovado'
    elif media_do_aluno[aluno] >= nota_minima_recuperacao:
        status = 'para recuperação'
    else:
        status = 'reprovado'
    print(
        f'A nota média do aluno {aluno} é {media_do_aluno[aluno]}. O aluno foi {status}.')
