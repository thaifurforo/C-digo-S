from sorteios import *
from cartela import *


def modo_sorteios_individuais(numero_sorteios: int):

    cartela_jogo = cartela()

    numeros_sorteados = []

    for _ in range(numero_sorteios):

        numero_sorteado = sorteio_unico(cartela_jogo)

        numeros_sorteados.append(numero_sorteado)

        cartela_final, resultado_jogo = resultado_cartela(
            numeros_sorteados, cartela_jogo)

        imprime_cartela(cartela_final)
        print(f'O número sorteado foi: {numero_sorteado}.')

    print(f'\n\nResultado final da partida de BINGO:\n{resultado_jogo}')


def modo_sorteio_multiplo(numero_sorteios: int):

    cartela_jogo = cartela()

    numeros_sorteados = sorteios(numero_sorteios, cartela_jogo)

    cartela_final, resultado_jogo = resultado_cartela(
        numeros_sorteados, cartela_jogo)

    imprime_cartela(cartela_final)
    print(f'\nOs números sorteados foram: {numeros_sorteados}')
    print(f'\n\nResultado final da partida de BINGO:\n{resultado_jogo}')
