from abc import ABC, abstractmethod


class CadastroAbstract(ABC):
    def __init__(self) -> None:
        self.__lista = []

    def inserir(self, entity):
        self.__lista.append(entity)
        return True

    def consultar(self, id):
        lista = list(filter(lambda x: x.id == id, self.__lista))
        if len(lista) > 0:
            return lista[0]

    def remover_por_id(self, id):
        try:
            entitiy = self.consultar(id)
            self.__lista.remove(entitiy)
        except Exception as ex:
            raise ex
        else:
            return True

    def remover_por_entidade(self, entitiy):
        try:
            self.__lista.remove(entitiy)
        except Exception as ex:
            raise ex
        else:
            return True
          
    def listar_todos(self, cadastro):
        if len(self.__lista) > 0:
            return self.__lista
