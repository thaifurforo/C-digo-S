"""
How Bootcamps - Stone - /código[s]
Data: 19/04/2022
Autor: Henrique Junqueira Branco
Enunciado: POO - parte 3
"""

a = 1
b = 0

# trata apenas erros da classe ZeroDivisionError em códigos dentro do try:
try:
    print(a / b)
except ZeroDivisionError:
    print("O código continua normalmente!!!")

#trata apenas erros da classe NameError em códigos dentro do try:
try:
    # se colocar print(a/b) aqui por exemplo, irá dar erro na execução do código - não irá gerar exceção por não ser NameError
    print(d['sobrenome'])
except NameError:
    print("O código continua normalmente!!!")
    

#trata qualquer tipo de erro em códigos dentro do try (exceto erros de sintaxe):
try:
    print(a / b)
    print(d['sobrenome'])
except:
    print("O código continua normalmente!!!")
    

#trata apenas erros da classe NameError ou ZeroDivisionError em códigos dentro do try:
try:
    print(a / b)
    print(d['sobrenome'])
except (ZeroDivisionError, NameError):
    print("O código continua normalmente!!!")
    

# só pega um erro se tiver dois erros em um mesmo bloco try:
try:
    print(a / b)
    print(d['sobrenome'])
# podem ser feitos diferentes tipos de tratamento se houver possibilidade de dois tipos de erro em um mesmo try (lembrando que só irá executar o tratamento do primeiro erro encontrado):
except ZeroDivisionError:
    print("Capturei meu ZeroDivisionError")
except NameError:
    print("Capturei meu NameError")
    
try:
    print(b + a)
    print(d['sobrenome'])
# podem ser feitos diferentes tipos de tratamento se houver possibilidade de dois tipos de erro em um mesmo try (lembrando que só irá executar o tratamento do primeiro erro encontrado)
# nesse caso, o ideal seria dentro do tratamento do possível primeiro erro, executar novamente o código do segundo, com outro try específico pra ele
# porém, o melhor seria separar os blocos em trys diferentes
except ZeroDivisionError:
    print("Capturei meu ZeroDivisionError")
except NameError:
    print("Capturei meu NameError")    

# Má prática except: pass - ERRO SILENCIOSO!!!

try:
    print(d['sobrenome'])
except NameError:
    raise NameError('nome')

class SalaryNotInRangeError(Exception):
    """Exceção gerada quando o salário não está dentro da faixa especificada.

    Attributes:
        salary (int): salário que gerou o erro
        message (str): mensagem ao usuário
    """

    def __init__(self, salary, message="Salário não está na faixa especificada (5000, 15000)"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.salary} -> {self.message}"


salary = int(input("Digite um salário: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
