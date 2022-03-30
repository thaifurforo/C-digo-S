'''
Passo número desafio:
- Simule 1.000 jogos que sorteiam TODOS os números até que uma mesma cartela seja preenchida e contabilize:
    * O número mínimo de sorteios para que a cartela seja vencedora (não necessariamente preencher toda a cartela!)
    * A média do número de sorteios para que a cartela seja vencedora
    * O número máximo de sorteios para que a cartela seja vencedora
'''

from sorteios import *
from cartela import *

cartela_teste = cartela()
numero_sorteios_por_jogo = []

for _ in range(1000):
    numero_sorteios = 0
    resultado_final = ''
    numeros_sorteados = []
    while resultado_final != 'Parabéns! Cartela premiada!':
        numero_sorteios += 1
        numeros_sorteados.append(sorteio_unico(cartela_teste))
        resultado_final = resultado_cartela(
            numeros_sorteados, cartela_teste)[1]
    numero_sorteios_por_jogo.append(numero_sorteios)

print(
    f'O número mínimo de sorteios para que a cartela seja vencedora é: {min(numero_sorteios_por_jogo)}')
print(
    f'O número médio de sorteios para que a cartela seja vencedora é: {round(sum(numero_sorteios_por_jogo)/len(numero_sorteios_por_jogo),2)}')
print(
    f'O número máximo de sorteios para que a cartela seja vencedora é: {max(numero_sorteios_por_jogo)}')
