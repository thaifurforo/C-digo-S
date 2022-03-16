# Definição da função para cálculo da média
# A função recebe uma lista como parâmetro e retorna um float
def calcula_media(lst: list) -> float:
    """Calcula a média aritimérica."""

    # Retorna o cálculo da média da lista
    return sum(lst) / len(lst)

# Função para cálculo da média ponderada
# A função recebe `valores` que é uma lista, `pesos` que é uma tupla e retorna um float
# O parâmetro valores é obrigatório
# O parâmetro pesos é opcional. Se não for passado:
#   * Criamos uma tupla com vários números de mesmo tamanho (número de elementos) do parâmetro `valores`


def calcula_media_ponderada(valores: list, pesos: tuple or None = None) -> float:
    """Calcula a média ponderada."""

    # Se não for passado o parâmetro de pesos
    if not pesos:

        # Criamos uma tupla cheia de 1, com mesmo número de elementos de `valores`
        pesos = (1,) * len(valores)

    # Inicia uma soma acumulativa com zero
    numerador = 0

    # Soma dos pesos
    denominador = sum(pesos)

    # Iterando por cada par de valor, peso
    for valor, peso in zip(valores, pesos):

        # Soma cumulativa da multiplicação de cada valor por cada peso
        numerador = numerador + valor * peso

    # Retornando a média ponderada
    return numerador / denominador
