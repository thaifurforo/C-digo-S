from unidecode import unidecode


class Funcionario:
  
    # criar uma variável que será igual para todas as instâncias de objeto dessa classe:
    reajuste_anual: float = 10

    def __init__(self, nome: str, sobrenome: str, salario_inicial: float = 1_000):
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.salario_inicial: float = salario_inicial
        self.email = f'{unidecode(self.nome.lower().split()[0])}.{unidecode(self.sobrenome.lower().split()[-1])}@email.com'

    def dar_aumento(self, aumento_percentual: float) -> None:
        if hasattr(self, "novo_salario"):
            self.salario_atual = round(
                self.salario_atual * (1 + aumento_percentual/100), 2)
        else:
            self.salario_atual = round(
                self.salario_inicial * (1 + aumento_percentual/100), 2)
    
    @property        
    def salario_inicial(self):
        return self._salario_inicial