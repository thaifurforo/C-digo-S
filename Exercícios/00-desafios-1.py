from random import randint


def chute_usuario() -> int:
    numero_usuario = int(input('Informe um número inteiro entre 1 e 100: '))
    while numero_usuario < 1 or numero_usuario > 100:
        numero_usuario = int(
            input('Entrada inválida!\nInforme um número inteiro entre 1 e 100: '))
    return numero_usuario


def sorteio() -> int:
    numero_sorteado = randint(1, 100)
    return numero_sorteado


def partida():

    print('*** Jogo da adivinhação ***')

    numero_sorteado = sorteio()

    numero_usuario = chute_usuario()

    tentativas = 1

    while numero_sorteado != numero_usuario:

        if numero_sorteado > numero_usuario:
            print('O número sorteado é maior.\n')
        else:
            print('O número sorteado é menor.\n')

        tentativas += 1

        numero_usuario = chute_usuario()

    print(
        f'\nParabéns! Você acertou o número sorteado: {numero_sorteado}.\nTotal de tentativas efetuadas: {tentativas}')


def nova_partida() -> str:

    novo_jogo = input(
        'Deseja jogar novamente? Digite S para sim, N para não: ').upper()
    while novo_jogo != 'S' and novo_jogo != 'N':
        novo_jogo = input(
            'Entrada inválida!\nDeseja jogar novamente? Digite S para sim, N para não: ').upper()
    if novo_jogo == 'S':
        partida()
    else:
        print('Jogo encerrado!')


partida()
