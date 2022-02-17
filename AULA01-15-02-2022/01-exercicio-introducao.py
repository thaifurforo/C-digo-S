"""
How bootcamps - Stone / código[s]
Data: 15/02/2022
Autor: Henrique Junqueira Branco
Enunciado: recebe do usuário distância em km e velocidade média em km/h e imprime na tela o tempo em horas de viagem"""

# Desafio 01: feito!

distancia = float(input('Digite a distância em km: '))

velocidade_media = float(input('Digite a vvelocidade média em km/h: '))

tempo_total_horas = distancia / velocidade_media

print(f"\nO tempo estimado é de {tempo_total_horas:.2f} horas\n")
