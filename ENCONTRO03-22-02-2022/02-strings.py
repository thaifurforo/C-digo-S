"""
How bootcamps - Stone / código[s]
Data: 22/02/2022
Facilitador: Henrique Junqueira Branco
"""


### STRINGS ###

frase = 'Matheus, o carioca!'
print(f'\n{frase.upper()}')
print(frase)
# String é imutável, para modificar precisaria substituir a variável >> frase = frase.upper()
# o método não modifica a string, ele apenas devolve uma nova string

print(f'\n{frase[-1]}')
# frase[-1] = '.'
# também não funciona porque a string é imutável - dá erro

frase.replace('!', '.')
print(f'\n{frase}')
# também não fez nenhuma modifição > string é imutável
frase = frase.replace('!', '.')
print(frase)
# assim dá certo porque a variável frase foi substituída por uma nova string, na qual foi aplicado o método replace
