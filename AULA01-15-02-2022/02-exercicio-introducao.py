"""
How Bootcamps - Stone - /código[s]
Data: 15/02/2022
Autor: Henrique Junqueira Branco
Enunciado (desafio aluno): Provavelmente um cálculo relativo a custo para aluguel de um carro. Recebe do usuário os km percorridos e os dias que ficou com o carro, sendo que ambos os valores serão convertidos para o número inteiro (type integer). Multiplica o preço por dia (R$60,00) pela quantidade de dias informada pelo usuário, e o preço por km (R$0,15) pela quantidade de quilômetros informada pelo usuário. Somam-se os dois resultados e imprime-se na tela o total a resultado, que corresponde ao total a pagar.
"""

# Desafio 02: o que esse pequeno trecho de código faz?

qtd_km = int(input('Digite a quantidade de quilômetros percorridos: '))

qtd_dias = int(input('Digite quantos dias você ficou com o carro:'))

preco_por_dia = 60
preco_por_km = 0.15

preco_total_km = qtd_km * preco_por_km
preco_total_dia = qtd_dias * preco_por_dia

preco_a_pagar = preco_total_km + preco_total_dia

print(f"Total a pagar: R$ {preco_a_pagar:7.2f}")
