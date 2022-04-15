# Classe mãe / classe super
class Ave:
  def __init__(self, numero_de_patas, cor, tamanho):
    self.numero_de_patas = numero_de_patas
    self.cor = cor
    self.tamanho = tamanho
    
  def voar(self):
    print('Ave voando!')
    
# Classe filha / classe sub / herdou a classe Ave
class Tucano(Ave):
  def __init__(self, cor_do_bico):
      # super() se refere à classe mãe - determina os atributos da classe mãe correspondentes a essa subclasse
      super().__init__(2, "colorido", "pequeno porte")
      self.tem_mancha_no_olho = True
      self.cor_do_bico = cor_do_bico
      
  def voar(self):
    print('Voando como um tucano!')

tucano = Tucano('preto')
tucano.voar()

print(tucano.tem_mancha_no_olho)
print(tucano.cor_do_bico)

corvo = Ave(2, "preto", "grande porte")