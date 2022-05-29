from src.entity import Entity

class Veiculo(Entity):
    def __init__(self, id: str, placa: str, km: float) -> None:
        
        super().__init__(id)

        if type(placa) is str:
            self.__placa = placa
        else:
            raise TypeError('A placa deve ser uma string')

        if type(km) is float or type(km) is int:
            self.__km = float(km)
        else:
            raise TypeError('O valor do km deve ser um número (int ou float)')

    @property
    def placa(self):
        return self.__placa

    @property
    def km(self):
        return self.__km
