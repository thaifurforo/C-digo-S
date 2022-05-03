"""
How Bootcamps - Stone - /código[s]
Data: 19/04/2022
Autor: Henrique Junqueira Branco
Enunciado: POO - parte 3 - comparação entre objetos de classes próprias
"""


class Employee:

    lvls = ('jr', 'pl', 'sr')

    def __init__(self, name, salary, lvl) -> None:
        self.name = name
        self.salary = salary
        self.lvl = lvl

    # eq = equal (igualdade)
    # quando define o método equa dentro da classe (sobrescreve o método builtin dentro da classe), define quando os dois objetos serão considerados iguais nessa classe quando usar ==
    def __eq__(self, obj: object) -> bool:
        return (self.name == obj.name) and (self.salary == obj.salary) and (self.lvl == obj.lvl)

    # greater than or equal (maior ou igual que)
    # quando define o método ge dentro da classe (sobrescreve o método builtin dentro da classe), define quando um objeto será considerado maior ou igual ao outro nessa classe quando usar >=
    def __ge__(self, other) -> bool:
        return Employee.lvls.index(self.lvl) >= Employee.lvls.index(other.lvl)

    # less than or equal (menor ou igual que)
    def __le__(self, other) -> bool:
        return Employee.lvls.index(self.lvl) <= Employee.lvls.index(other.lvl)

    # greater than (maior que)
    def __gt__(self, other) -> bool:
        return Employee.lvls.index(self.lvl) > Employee.lvls.index(other.lvl)

    # less than (menor que)
    def __lt__(self, other) -> bool:
        return Employee.lvls.index(self.lvl) < Employee.lvls.index(other.lvl)


emp1 = Employee("Joao", 2000, 'sr')
emp2 = Employee("Joao", 5000, 'pl')
emp3 = emp1

print(id(emp1))
print(id(emp3))
print(emp1 is emp3)
# Resultado do print acima é True porque os dois objetos terão o mesmo ID, por conta da variável emp3 ter sido definida como uma cópia da emp1

print('*******')

print(emp1 is emp2)
print(emp1 == emp2)
print(emp1 >= emp2)
print(emp1 <= emp2)
print(emp1 > emp2)
print(emp1 < emp2)

emp4 = Employee("Joao", 2000, 'sr')
print('*******')
print(id(emp1))
print(id(emp4))
# Resultado abaixo - is é False e == é True, porque não é o mesmo objeto (IDs diferentes como pode ser visto nos dois prints acima), mas os valores são iguais, conforme definido na função __eq__ da classe, que define se dois objetos dessa classe são iguais
print(emp1 is emp4)
print(emp1 == emp4)
print(emp1 >= emp4)
print(emp1 <= emp4)
print(emp1 > emp4)
print(emp1 < emp4)
