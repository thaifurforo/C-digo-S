import csv
from collections import defaultdict
from random import choice

# Duas equipes completas ganham da Stone
# Uma equipe completa ganha da How
# 3 alunos ganham da Stone individual

brindes = {'how': 5, 'stone': 13}

equipes = defaultdict(list)

with open('Sorteio.csv') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=';', quotechar="|")
    for linha in arquivo:
        if linha[0] == 'Nome do Aluno':
            continue
        nome_aluno = linha[0].strip().replace(" ", " ")
        numero_equipe = linha[1]
        equipes[numero_equipe].append(nome_aluno)

equipes_ja_sorteadas = []

for _ in range(2):
    print('\nSorteio brinde da Stone!', end='\n\n')
    equipe_sorteada = choice(list(equipes.keys()))
    pessoas_sorteadas = equipes[equipe_sorteada]
    print(f'A equipe sorteada foi: {equipe_sorteada}')
    for pessoa in pessoas_sorteadas:
        print(
            f'Parabéns {pessoa}, você ganhou um brinde da Stone!')

    equipes.pop(equipe_sorteada)
    print('*' * 60)


print('\nSorteio brinde da How!', end='\n\n')
equipe_sorteada = choice(list(equipes.keys()))
pessoas_sorteadas = equipes[equipe_sorteada]
print(f'A equipe sorteada foi: {equipe_sorteada}')
for pessoa in pessoas_sorteadas:
    print(
        f'Parabéns {pessoa}, você ganhou um brinde da How!')

equipes.pop(equipe_sorteada)
print('*' * 60)

pessoas_nao_sorteadas = []

for lista_nomes in equipes.values():
    pessoas_nao_sorteadas.extend(lista_nomes)

print('\nSorteio individual dos brindes da Stone!', end='\n\n')
for _ in range(3):
    pessoa_sortuda = choice(pessoas_nao_sorteadas)
    pessoa_sortuda_indice = pessoas_nao_sorteadas.index(pessoa_sortuda)

    print(f'Parabéns {pessoa_sortuda}! Você ganhou um brinde individual!')

    pessoas_nao_sorteadas.pop(pessoa_sortuda_indice)
