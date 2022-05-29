
from src.veiculo import Veiculo


class Automovel(Veiculo):
    def __init__(self, id: str, placa: str, km: float, bagageiro: int, portas: int) -> None:
        super().__init__(id, placa, km)
        
        if type(bagageiro) is int:
            self.__bagageiro = bagageiro
        else:
            raise TypeError('O valor do bagageiro deve ser int')
        
        if type(portas) is int:
            self.__portas = portas
        else:
            raise TypeError('O número de portas deve ser int')
        
        
    @property
    def bagageiro(self):
        return self.__bagageiro
    
    @property
    def portas(self):
        return self.__portas