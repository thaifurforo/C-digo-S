from abc import ABC, abstractmethod


class Poligono(ABC):

    @abstractmethod
    def numero_lados(self):
        pass

    @abstractmethod
    def calcula_area(self):
        pass


class Triangulo(Poligono):

    def __init__(self, *args) -> None:
        if len(args) != 3:
            raise ValueError('Numero inválido de lados para um triângulo!')
        else:
            self.lados = args
            self.s = (self.lados[0] + self.lados[1] + self.lados[2]) / 2

    def numero_lados(self):
        print('Eu tenho 3 lados!')

    def calcula_area(self) -> float:
        return (self.s * (self.s - self.lados[0]) * (self.s - self.lados[1]) * (self.s - self.lados[2])) ** (1/2)


class Pentagono(Poligono):

    def numero_lados(self):
        print('Eu tenho 5 lados!')

    def calcula_area(self):
        pass


class Retangulo(Poligono):

    def __init__(self, *args) -> None:
        # O nome args é uma convenção, o que dá o resultado é o * antes do nome. Poderia ser qualquer coisa, como *list ou *xyz
        if len(args) != 4:
            raise ValueError('Numero inválido de lados para um retângulo!')
        else:
            self.lados = tuple(set(args))

    def numero_lados(self):
        print('Eu tenho 4 lados!')

    def calcula_area(self) -> float:
        return self.lados[0] * self.lados[1]


class Hexagono(Poligono):

    def numero_lados(self):
        print('Eu tenho 6 lados!')

    def calcula_area(self):
        pass


tri = Triangulo(3, 4, 5)
tri.numero_lados()
print(tri.calcula_area())

quad = Retangulo(2, 4, 2, 4)
quad.numero_lados()
print(quad.calcula_area())
