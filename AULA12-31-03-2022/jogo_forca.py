"""
How Bootcamps - Stone - /código[s]
Data: 31/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Construa um jogo da forca!
A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.
Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

# from random import ?

import csv
from distutils.log import error
from random import choice
import bonecos
import palavras


def get_secret_word(words: list = palavras.words) -> str:
    """Devolve uma palavra aleatória de uma lista.

    Args:
      words (list): lista possíveis palavras

    Returns:
      str: palavra secreta aleatória sorteada"""

    secret_word = choice(words)[0].upper()
    return secret_word


def print_game_board():
    """Imprime a situação atual do jogo.

    Print:
        Imprime o game board com a ilustração da Forca e a palavra com os tracinhos
    Returns:
        None"""

    doll = bonecos.dolls[error]

    game_board = ''
    for letter in secret_word:
        if letter in correct_letters:
            game_board += letter + ' '
        else:
            game_board += '_ '

    print(
        f'\n\nTentativas erradas: {missed_letters}\n{doll}\nPalavra: {game_board}')

    return None


def read_input_player() -> str:
    """Lê uma letra do usuário.

    Returns:
      user_guess(str): letra inputada pelo usuário"""

    user_guess = input(
        '\nDigite uma letra:\n').upper()
    return user_guess


def guess_letter(letter: str):
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada.

    Args:
      letter (str): letra inputada pelo usuário

    Returns:
      False: se a letra já foi jogada anteriormente, ou se não estiver na palavra secreta
      True: se a letra não foi jogada anteriormente e estiver na palavra secreta"""

    if letter in correct_letters or letter in missed_letters:
        return False
    elif letter not in secret_word:
        return False
    else:
        return True


def game_continue():
    """Função que decide se jogo já encerrou ou não.

    Returns:
        False: se o jogo foi finalizado (porque o usuário venceu ou porque acabaram as chances)
        True: se o jogo ainda não foi finalizado

    Print:
        Se o jogo foi finalizado, imprime o título do Jogo da Forca, as chances disponíveis e o resultado do jogo
        Cas ocontrário não imprime nada
    """
    if set(secret_word) == set(correct_letters):
        print(
            f'\n\n*********************\n*** JOGO DA FORCA ***\n*********************\n\nChances disponíveis: {attempts - error} de {attempts}\n\n______________________________\n\n*** Parabéns! Você venceu! ***\n______________________________')
        print_game_board()
        print('\n\n__________________________________________')
        return False

    elif error < attempts:

        if set(secret_word) != set(correct_letters):
            return True
        else:
            return False

    else:
        print(
            f'\n\n*********************\n*** JOGO DA FORCA ***\n*********************\n\nChances disponíveis: {attempts - error} de {attempts}\n\n_____________________\n\n*** Você perdeu! ***\n_____________________')
        print_game_board()
        print(
            f'A palavra secreta é: {secret_word}\n\n__________________________________________')
        return False


def letter_result(letter: str):
    """Função que coloca a letra (letter) na lista adequada, de letras corretas ou erradas, de acordo com a palavra secreta (secret_word)

    Args:
        letter (str): letra inputada pelo usuário

    Returns:
        None
    """

    if letter in correct_letters or letter in missed_letters:
        pass
    elif letter not in secret_word:
        missed_letters.append(letter)
    else:
        correct_letters.append(letter)

    return None


secret_word = get_secret_word()
correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadas
attempts = 6  # tentativas
error = 0  # erro inicial


while game_continue():
    print(
        f'\n\n*********************\n*** JOGO DA FORCA ***\n*********************\n\nChances disponíveis: {attempts - error} de {attempts}')
    print_game_board()
    letter = read_input_player()
    if not guess_letter(letter):
        error += 1
    letter_result(letter)
