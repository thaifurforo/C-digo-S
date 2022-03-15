
# :list define que o argumento tem que ser list
# -> float define que o resultado será float
# a tipagem não é obrigatória
def calcula_media(lista: list) -> float:
    '''Calcula a média aritmética'''

    return sum(lista) / len(lista)

# Operador pipe | só funciona no Python 10
def calcula_media_ponderada(valores: list, pesos: list = []) -> float:
    '''Calcula a média ponderada'''
    if pesos == []:
        pesos = [1 for n in range(len(valores))]
    #Inicia uma soma acumulativa no zero
    numerador = 0

    # Calcula o denominador da média ponderada
    denominador = sum(pesos)

    # Usa for para calcular o numerador da média ponderada
    # função zip retorna um objeto zip que contém tuplas combinando cada valor da lista 1 com o respectivo valor da lista 2 (mesma posição)
    for valor, peso in zip(valores, pesos):

        numerador = numerador + valor * peso
    
    return numerador / denominador

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
    pesos = []

    uso_pesos = input('Deseja usar pesos específicos para as notas do aluno? S ou N? ').upper()

    while nova_nota == 'S':
        notas.append(
            float(input(f'Digite a nota nº {n_nota} do aluno {aluno}: ')))
        
        if uso_pesos == 'S':
            pesos.append(float(input(f'Digite o peso para a nota nº {n_nota} do aluno {aluno}: ')))
        
        n_nota += 1
        
        nova_nota = input('Deseja inserir mais uma nota? S ou N? ').upper()
        
        if nova_nota != 'S' and nova_nota != 'N':
            nova_nota = input(
                'Opção inválida. Deseja inserir mais uma nota? Digite "S" para "Sim" ou "N" para "Não": ').upper()
    notas_por_aluno[aluno] = [notas, pesos]
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
    media_do_aluno[aluno] = calcula_media_ponderada(notas_do_aluno[0], notas_do_aluno[1])
    if media_do_aluno[aluno] >= nota_minima_aprovacao:
        status = 'aprovado'
    elif media_do_aluno[aluno] >= nota_minima_recuperacao:
        status = 'para recuperação'
    else:
        status = 'reprovado'
    print(
        f'A nota média do aluno {aluno} é {media_do_aluno[aluno]}. O aluno foi {status}.')