from random import sample


# Passo número 0
def cartela():
    variacoes = {'B': (1, 15), 'I': (16, 30), 'N': (
        31, 45), 'G': (46, 60), 'O': (61, 75)}
    cartela = {}
    for key, values in variacoes.items():
        cartela[key] = list(map(str, sorted(
            sample(range(values[0], values[1]+1), 5))))
    return cartela


# Passo número 1
def imprime_cartela(cartela=cartela()):
    print(f"\n{'B':^5} {'I':^5} {'N':^5} {'G':^5} {'O':^5}")
    for n in range(len(cartela)):
        print(
            f"{cartela['B'][n].zfill(2):^5} {cartela['I'][n]:^5} {cartela['N'][n]:^5} {cartela['G'][n]:^5} {cartela['O'][n]:^5}")
