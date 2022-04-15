"""
How bootcamps - Stone / código[s]
Data: 08-03-2022
Facilitador: Henrique Junqueira Branco
Tema: Estrutura de repetição
"""

notas_por_aluno = dict()
# dict() cria dicionário vazio, equivalente a = {}

novo_aluno = 'S'
n_aluno = 1

# O underline _ na variável do for significa que a variável não faz diferença
while novo_aluno == 'S':
    aluno = input(f'Digite o nome do {n_aluno}º aluno: ')
    notas = list()
    # list() cria lista vazia, equivalente a = []

    nova_nota = 'S'
    n_nota = 1

    while nova_nota == 'S':
        notas.append(
            int(input(f'Digite a nota nº {n_nota} do aluno {aluno}: ')))
        n_nota += 1
        nova_nota = input('Deseja inserir mais uma nota? S ou N? ').upper()
        if nova_nota != 'S' and nova_nota != 'N':
            nova_nota = input(
                'Opção inválida. Deseja inserir mais uma nota? Digite "S" para "Sim" ou "N" para "Não": ').upper()
    notas_por_aluno[aluno] = notas
    novo_aluno = input(
        'Deseja inserir as notas de mais um aluno? S ou N? ').upper()
    if novo_aluno != 'S' and novo_aluno != 'N':
        nova_nota = input(
            'Opção inválida. Deseja inserir as notas de mais um aluno? Digite "S" para "Sim" ou "N" para "Não": ').upper()

    n_aluno += 1

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
