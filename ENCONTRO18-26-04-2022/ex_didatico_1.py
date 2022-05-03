class Leao:
  def alimentar(self):
    print('Leão foi alimentado como um rei!')

class Cobra:
  def dar_comida(self):
    print('A comida foi jogada pra cobra!')
  
class Tigre:
  def jogar_carne(self):
    print('O tigre rasgou a carne com o dente e comeu!')
    
leo = Leao()
siriguela = Cobra()
tio_sam = Tigre()

leo.alimentar()
siriguela.dar_comida()
tio_sam.jogar_carne()

# E se colocarmos todos os animais em uma lista?
zoo = [leo, siriguela, tio_sam] # Poderia haver muitos outros animais aqui

#Itera por todos os animais da lista
# for animal in zoo:
# Mas, espere? O que colocamos aqui agora?
# animal.alimentar() ou animal.dar_comida()?
# independente do que colocarmos aqui teremos um erro!


