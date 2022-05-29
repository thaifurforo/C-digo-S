
from src.veiculo import Veiculo


class Caminhao(Veiculo):
    def __init__(self, id: str, placa: str, km: float, carga: float) -> None:
        super().__init__(id, placa, km)
        
        if type(carga) is float or type(carga) is int:
            self.__carga = float(carga)
        else:
            raise TypeError('O valor da carga deve ser um número (int ou float)')
        
    @property
    def carga(self):
        return self.__carga
        