from animal import Animal
from pessoa import Pessoa

class Leao(Animal):

    def alimentar(self):
        print('Leão foi alimentado como um rei!')

    def caminhar(self):
        print('O leão andou com a graça de um rei!')


class Cobra(Animal):

    def alimentar(self):
        print('A comida foi jogada pra cobra!')

    def caminhar(self):
        print('A cobra rastejou pelo chão!')


class Tigre(Animal):

    def alimentar(self):
        print('O tigre rasgou a carne com o dente e comeu!')

    def caminhar(self):
        print('O tigre deu passos sorrateiros!')

# Herança simples
# super().__init__()

# Herança múltipla
# Animal.__init__()
# Pessoa.__init__()

# Algumas linguagens não têm herança múltipla
# Quanto mais simples melhor - > evitar heranças múltiplas

class Lobisomem (Animal, Pessoa): # Duas classes mães para uma classe filha - sendo ambas abstratas
    def alimentar(self):
        print('O lobismomem comeu carne humana!')

    def caminhar(self):
        print('O lobismomem deu seus passos em duas patas!') 
        
    def pensar(self):
        print('O lobisomem não pensa, age por instinto!')
        
    def acordar(self):
        print('Em uma noite de Lua Cheia, o Lobisomem acorda!')


leo = Leao()
siriguela = Cobra()
tio_sam = Tigre()

zoo = [leo, siriguela, tio_sam]  # Poderia haver muitos outros animais aqui

# Itera por todos os animais da lista
for animal in zoo:
    animal.alimentar()

for animal in zoo:
    animal.caminhar()

for animal in zoo:
    animal.atacar()

print('*****Teste múltiplas classes abstratas herdadas******')

lupus = Lobisomem()

print('*Métodos abstratos da classe Pessoa:')
lupus.acordar()
lupus.pensar()
print('*Métodos abstratos da classe Animal:')
lupus.alimentar()
lupus.caminhar()
print('*Métodos concretos herdados da classe Animal:')
lupus.atacar()