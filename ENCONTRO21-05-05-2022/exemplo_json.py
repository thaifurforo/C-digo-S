import json


class Veiculo():
    def __init__(self):
        self.marca = None
        self.modelo = None


class Pessoa():
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cidade = None
        self.veiculo: list = []


maicon = Pessoa()
maicon.nome = 'Maicon'
maicon.idade = 35
maicon.cidade = 'Curitiba'

fusca = Veiculo()
fusca.marca = 'VW'
fusca.modelo = 'Fusca'

chevete = Veiculo()
chevete.marca = 'GM'
chevete.modelo = 'chevete'

maicon.veiculo.append(fusca.__dict__)
maicon.veiculo.append(chevete.__dict__)

maicon_json = json.dumps(maicon.__dict__)

with open('files/maicon.json', 'w') as arquivo:
  arquivo.write(maicon_json)
  
