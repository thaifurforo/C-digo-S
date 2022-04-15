from pessoas import Funcionario


funcionario1 = Funcionario('João', 'Pereira Félix', 10_000)
funcionario2 = Funcionario('Ana Maria', 'Conceição')
print(funcionario1.email)
print(funcionario2.email)


funcionario1.dar_aumento(15)

print(funcionario1.salario_inicial)
print(funcionario1.salario_atual)

funcionario1.dar_aumento(10)
print(funcionario1.salario_atual)

funcionario1.dar_aumento(funcionario1.reajuste_anual)
print(funcionario1.salario_atual)

funcionario2.dar_aumento(funcionario2.reajuste_anual)
print(funcionario2.salario_inicial)
print(funcionario2.salario_atual)