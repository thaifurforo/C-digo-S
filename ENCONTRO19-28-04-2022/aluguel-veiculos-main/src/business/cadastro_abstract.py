from abc import ABC, abstractmethod
from src.entities.entity import Entity
from typing import List

class CadastroAbtract(ABC):

    @abstractmethod
    def inserir(self, entity: Entity):
        pass

    @abstractmethod
    def consultar(self, id: str) -> Entity:
        pass

    @abstractmethod
    def remover_por_id(self, id: str) -> Entity:
        # id é um atributo da variável entity que armazena o objeto
        pass

    @abstractmethod
    def remover_por_entidade(self, entity: Entity) -> Entity:
        # entity é a variável que armazena o objeto
        pass

    @abstractmethod
    def listar_todos() -> List[Entity]:
        # o list normal do python quando definido na tipagem da saída não tem como receber que tipo de item terá dentro da lista. pra fazer isso, deve ser importado o módulo built-in typing e usar a função List[tipo de item dentro da lista]
        pass
