"""
How Bootcamps - Stone - /código[s]
Data: 25/05/2022
Autor: Henrique Junqueira Branco
Enunciado: BINGO do zero!

Uma cartela de BINGO consiste em 5 colunas de 5 números que são rotulados com as letras B, I, N, G e O.
Atenção: Google it, para quem nunca viu uma cartela dessas!

Existem 15 números que podem aparecer sob cada letra respeitando a regra abaixo.
- B -> números variando de 1 a 15  (inclusos)
- I -> números variando de 16 a 50 (inclusos)
- N -> números variando de 51 a 55 (inclusos)
- ... e assim por diante

Passo número 0:
- Escreva uma função que crie uma cartela de BINGO aleatória. Dica(podemos usar um dicionário!).
- As chaves serão as letras B, I, N, G e O.
- Os valores serão as listas de cinco números aleatórios respeitando a regra dos intervalos de cada letra.

Passo número 1:
- Escreva uma segunda função que exiba a cartela de BINGO com as colunas rotuladas apropriadamente
- Formate a saída no terminal para que a cartela seja impressa em forma de colunas (letras e seus valores abaixo)

Passo número 2:
- Sorteie uma letra e número aleatório (respeitando a regra) e veja se a cartela contém aquele número.

Passo número 5:
- Sorteie 50 (letras e) números e verifique se a cartela é vencedora ou não.
- Uma cartela é vencedora quando preencher uma linha ou coluna inteira com números sorteados.

"""

from sorteios import *
from cartela import *
from modos_jogos import *


def main():
    modo_jogo = int(input(
        '*** Bem vindo ao BINGO! ***\n\nSelecione o modo de jogo (digite o número):\n1 - Sorteio único de todos os números\n2 - Sorteios individuais\n\nR:'))
    numero_sorteios = int(
        input('\nDigite quantos números serão sorteados:\nR:'))
    if modo_jogo == 1:
        modo_sorteio_multiplo(numero_sorteios)
    elif modo_jogo == 2:
        modo_sorteios_individuais(numero_sorteios)
    else:
        while modo_jogo not in [1, 2]:
            int(input('Modo de jogo inválido! Selecione o modo de jogo (digite o número):\n1 - Sorteio único de todos os números\n2 - Sorteios individuais\n\n\R:'))


if (__name__ == '__main__'):
    main()
