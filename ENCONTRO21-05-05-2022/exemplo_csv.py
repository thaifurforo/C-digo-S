import csv


class Pessoa():
    def __init__(self, nome: str = None, idade: int = None, cidade: str = None):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade


pessoa1 = Pessoa(nome='João', idade=35, cidade='São José do Rio Preto')
pessoa2 = Pessoa(nome='Maicon', idade=18, cidade='Curitiba')
pessoa3 = Pessoa(nome='William', idade=30, cidade='Lavras')
pessoa4 = Pessoa(nome='Bárbara', idade=23, cidade='Belo Horizonte')

pessoas = [pessoa1, pessoa2, pessoa3, pessoa4]

pessoas_dict = [pessoa1.__dict__, pessoa2.__dict__,
                pessoa3.__dict__, pessoa4.__dict__]

cabecalho = ['nome', 'idade', 'cidade']

with open('files/pessoas.csv', 'w', newline='\n', encoding='utf8') as csvfile:
    arquivo_csv = csv.writer(csvfile, delimiter=';',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    arquivo_csv.writerow(cabecalho)
    for p in pessoas:
        arquivo_csv.writerow([p.nome, p.idade, p.cidade])

with open('files/pessoas_dict.csv', 'w', newline='\n', encoding='utf8') as csvfile:
    arquivo_csv = csv.writer(csvfile, delimiter=';',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    arquivo_csv.writerow(cabecalho)
    for p in pessoas_dict:
        arquivo_csv.writerow([p['nome'], p['idade'], p['cidade']])

with open('files/pessoas.csv', 'r', encoding='utf8') as csvfile:
    arquivo_csv = csv.reader(csvfile, delimiter=';')
    lista_csv = []
    for index, linha in enumerate(arquivo_csv):
        lista_csv.append(linha)
        nome, idade, cidade = linha[0], linha[1], linha[2]
        print(
            f'O nome da pessoa é {nome}, idade {idade} anos, que mora em {cidade}.')

with open('files/pessoas.csv', 'r', encoding='utf8') as csvfile:
    arquivo_csv = csv.DictReader(csvfile, delimiter=';')
    dict_csv = {}
    for index, linha in enumerate(arquivo_csv):
        dict_csv[linha['nome']] = [linha['idade'], linha['cidade']]
        print(
            f"O nome da pessoa é {linha['nome']}, idade {linha['idade']} anos, que mora em {linha['cidade']}.")

print(lista_csv)
print(dict_csv)
