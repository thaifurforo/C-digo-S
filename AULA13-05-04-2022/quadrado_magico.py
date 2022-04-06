"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco
Enunciado:
Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas,
com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.
Por exemplo, veja um quadrado de lado 4, com números de 1 a 16:
01  05  09  16
06  07  02  10
08  03  04  11
12  15  14  13
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
Usar um vetor (lista) de 1 a 16 parece ser mais simples que usar uma matriz 4x4.
Extra: Permita que o usuário indique o tamanho do cubo mágico (2x2, 3x3, 4x4, etc.)
"""

import itertools


def quadrado_magico(numero_de_linhas: int):
    qtd_numeros = numero_de_linhas ** 2
    numeros = list(range(1, qtd_numeros + 1))

    for combinacao in itertools.permutations(numeros, qtd_numeros):

        lista_de_somas = []

        linha = 1
        while linha <= numero_de_linhas:
            ultimo_index_linha = (numero_de_linhas * linha) - 1
            primeiro_index_linha = ultimo_index_linha - (numero_de_linhas - 1)
            conteudo_da_linha = [combinacao[i] for i in range(
                primeiro_index_linha, ultimo_index_linha + 1)]
            lista_de_somas.append(sum(conteudo_da_linha))
            linha += 1

        coluna = 1
        while coluna <= numero_de_linhas:
            index = coluna - 1
            conteudo_da_coluna = []
            while index <= (qtd_numeros) - 1:
                conteudo_da_coluna.append(combinacao[index])
                index += numero_de_linhas
            lista_de_somas.append(sum(conteudo_da_coluna))
            coluna += 1

        index = 0
        conteudo_da_diagonal_1 = []
        while index <= (qtd_numeros) - 1:
            conteudo_da_diagonal_1.append(combinacao[index])
            index += numero_de_linhas + 1
        lista_de_somas.append(sum(conteudo_da_diagonal_1))

        index = (qtd_numeros) - numero_de_linhas
        conteudo_da_diagonal_2 = []
        while index > 0:
            conteudo_da_diagonal_2.append(combinacao[index])
            index -= (numero_de_linhas - 1)
        lista_de_somas.append(sum(conteudo_da_diagonal_2))

        set_somas = set(lista_de_somas)
        if len(set_somas) == 1:
            print(
                f'Quadrado mágico encontrado!\n{combinacao}', end='\n\n')
        else:
            pass


quadrado_magico(int(input('Digite o número de lados do quadrado:')))
