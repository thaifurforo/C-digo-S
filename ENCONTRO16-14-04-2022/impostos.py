# classe genérica / classe mãe / classe super
class Imposto:

    def __init__(self, percentual: float):
        self.percentual = percentual

# herança do percentual -> classe filha / classe sub


class ICMS(Imposto):

    def __init__(self):
        super().__init__(0.05)


class IPI(Imposto):

    def __init__(self):
        super().__init__(0.15)


class ISS(Imposto):

    def __init__(self):
        super().__init__(0.10)
