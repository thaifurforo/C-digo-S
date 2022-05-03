from abc import ABC, abstractmethod


class Animal (ABC):
    
    @abstractmethod
    def alimentar(self):
        """Teste  de documentação"""
        pass
    
    @abstractmethod
    def caminhar(self):
        pass
    
    # método concreto, sem o uso do @abstractmethod - será herdado exatamente como definido a seguir pelas classes filhas, sem abstração
    def atacar(self):
        print('O animal atacou!')