class Entity():
    def __init__(self, id: str) -> None:

        if type(id) is str:
            self.__id = id
        else:
            raise TypeError('O ID deve ser uma string')

    @property
    def id(self):
        return self.__id
