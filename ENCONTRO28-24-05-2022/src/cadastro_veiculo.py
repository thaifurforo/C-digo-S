from src.cadastro_abstract import CadastroAbstract


class CadastroVeiculo(CadastroAbstract):
    
    def __init__(self) -> None:
        super().__init__()
        self.__lista = []
    
    @property
    def lista(self):
        return self.__lista
