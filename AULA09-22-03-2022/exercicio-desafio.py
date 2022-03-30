from math import *

"""
A superfície da Terra é curva, e a distância entre os graus de longitude varia com a latitude.
Como resultado, encontrar a distância entre dois pontos na superfície da Terra é mais complicado do que simplesmente 
Sejam (t1, g1) e (t2, g2) a latitude e a longitude de dois pontos na superfície da Terra.
A distância entre esses pontos, acompanhando a superfície da Terra, em quilômetros, é:

distancia = 6371,01 x arcos(sen(t1) x sen(t2) + cos(t1) x cos(t2) x cos(g1 - g2))

O valor 6371,01 na equação anterior não foi selecionado aleatoriamente.
É o raio médio da Terra em quilômetros.

Crie um programa que permita ao usuário inserir a latitude e longitude de dois pontos da Terra em graus.
Seu programa deve exibir a distância entre os pontos, seguindo a superfície da Terra, em quilômetros.add()

Dica 1: as funções trigonométricas do Python operam em radianos.
Como resultado, você vai precisar converter a entrada do usuário de graus para radianos antes de calcular a distância com a fórmula discutida anteriormente.
O módulo math contém uma função chamada radianos que converte de graus para radianos.

Dica 2: Latitude varia -90 (sul) até +90 (norte). O ponto de latitude 0 é a linha do equador.
Longitude varia de -180 (leste) até 180 (oeste). O ponto de longitude 0 é o meridiano de Greenwich.

"""


def distancia_superficie() -> float:
    t1 = radians(
        float(input('Digite a latitude do primeiro ponto em graus: ')))
    g1 = radians(
        float(input('Digite a longitude do primeiro ponto em graus: ')))
    t2 = radians(
        float(input('Digite a latitude do segundo ponto em graus: ')))
    g2 = radians(
        float(input('Digite a longitude do segundo ponto em graus: ')))
    return round((6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))), 2)


print(f'A distância é de {distancia_superficie()} quilômetros.')
