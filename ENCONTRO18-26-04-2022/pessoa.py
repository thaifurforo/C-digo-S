from abc import ABC, abstractmethod

class Pessoa (ABC):
    
    @abstractmethod
    def acordar(self):
        pass
    
    @abstractmethod
    def pensar(self):
        pass