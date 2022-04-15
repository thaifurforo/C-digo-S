from cartela import *
import copy

# Passo número 2


def sorteio_unico(cartela: dict = cartela()) -> int:
    variacoes = {'B': list(map(str, range(1, 16))), 'I': list(map(str, range(16, 31))), 'N': list(map(str, range(
        31, 46))), 'G': list(map(str, range(46, 61))), 'O': list(map(str, range(61, 76)))}
    numero_sorteado = str(sample(range(1, 76), 1)[0])

    for key, values in variacoes.items():
        if numero_sorteado in values:
            letra_sorteada = key
    if numero_sorteado in cartela[letra_sorteada]:
        resultado = 'O número está na sua cartela, parabéns!'
    else:
        resultado = 'Que pena, o número não está na cartela!'
    return numero_sorteado

# Passo número 3


def sorteios(n: int, cartela: dict = cartela()) -> list:
    if n > 75:
        n = 75
    numeros_sorteados = sorted(list(map(str, sample(range(1, 76), n))))
    return numeros_sorteados


def resultado_cartela(numeros_sorteados: list, cartela: dict() = cartela()):
    cartela_final = copy.deepcopy(cartela)

    sorteados_por_letra = {}
    for key, values in cartela_final.items():
        sorteados_por_letra[key] = []
        for n in values:
            if n in numeros_sorteados:
                sorteados_por_letra[key].append(True)
                index = values.index(n)
                values[index] = '[' + values[index].zfill(2) + ']'
            else:
                sorteados_por_letra[key].append(False)

    for key, values in sorteados_por_letra.items():
        if all(values) == True:
            resultado = 'Parabéns! Cartela premiada!'
            break
        else:
            for n in range(5):
                if all([sorteados_por_letra['B'][n], sorteados_por_letra['I'][n], sorteados_por_letra['N'][n], sorteados_por_letra['G'][n], sorteados_por_letra['O'][n]]) == True:
                    resultado = 'Parabéns! Cartela premiada!'
                    break
                else:
                    resultado = 'Que pena, não foi dessa vez!'
    return cartela_final, resultado
