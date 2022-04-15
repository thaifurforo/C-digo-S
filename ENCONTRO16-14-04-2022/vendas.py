from impostos import *


class Venda:

    def __init__(self, valor_bruto: float, imposto: Imposto) -> None:
        self.valor_bruto = valor_bruto
        self.imposto = imposto
        self.valor_liquido = self.calcula_valor_liquido()

    def calcula_valor_liquido(self):
        imposto = self.imposto()
        self.valor_liquido = self.valor_bruto * (1 - imposto.percentual)
        return self.valor_liquido

    def __str__(self):
        return f'O imposto utilizado é {self.imposto.__name__}.\nO valor bruto da venda é {self.valor_bruto}.\nO valor líquido da venda é {self.valor_liquido}'


venda1 = Venda(100, ICMS)
print(venda1)
